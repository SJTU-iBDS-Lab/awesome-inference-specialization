#!/usr/bin/env python3
"""Offline validation of the catalog, controlled facets and evidence pointers."""
from __future__ import annotations

import datetime as dt
import re
import sys
from urllib.parse import urlparse

from update_readme import CSV_PATH, FAMILIES, SCHEMA, load_rows

FIELDS = set('id project family domains artifact_type constraints mechanisms target mechanism semantic_effect source_visibility ai_involvement url evidence_urls caveat checked_on discovery'.split())
TAG = re.compile(r'[a-z0-9][a-z0-9-]*\Z')


def valid_url(value: str) -> bool:
    u = urlparse(value)
    return u.scheme == 'https' and bool(u.netloc) and not re.search(r'[\s<>"|]', value)


def validate(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if not rows:
        return ['Catalog is empty']
    ids: set[str] = set()
    urls: set[str] = set()
    family_ids = {f['id'] for f in FAMILIES}
    enums = {'family': family_ids, 'artifact_type': set(SCHEMA['artifact_types']),
             'source_visibility': set(SCHEMA['source_visibility']),
             'ai_involvement': {'intrinsic', 'disclosed', 'not-established'},
             'discovery': {'initial', 'keyword', 'dependency'}}
    for n, r in enumerate(rows, 2):
        label = f'CSV row {n} ({r.get("id", "?")})'
        if set(r) != FIELDS:
            errors.append(f'{label}: columns do not match schema')
            continue
        if any(not isinstance(v, str) or not v.strip() for v in r.values()):
            errors.append(f'{label}: missing or malformed field')
            continue
        if not TAG.fullmatch(r['id']):
            errors.append(f'{label}: invalid id')
        if r['id'] in ids:
            errors.append(f'{label}: duplicate id')
        ids.add(r['id'])
        canonical_url = r['url'].rstrip('/').lower()
        if canonical_url in urls:
            errors.append(f'{label}: duplicate project URL')
        urls.add(canonical_url)
        for field, allowed in enums.items():
            if r[field] not in allowed:
                errors.append(f'{label}: unsupported {field}: {r[field]}')
        for field in ('domains', 'constraints', 'mechanisms', 'semantic_effect'):
            values = r[field].split(';')
            if len(set(values)) != len(values) or any(not TAG.fullmatch(v) for v in values):
                errors.append(f'{label}: malformed or duplicate {field} tags')
            allowed = SCHEMA['domains'] if field == 'domains' else SCHEMA['semantic_effects'] if field == 'semantic_effect' else None
            if allowed is not None and set(values) - set(allowed):
                errors.append(f'{label}: unknown {field} tag')
        evidence = r['evidence_urls'].split(';')
        if len(evidence) < 2 or len(set(evidence)) != len(evidence):
            errors.append(f'{label}: need at least two distinct evidence pointers')
        for url in [r['url'], *evidence]:
            if not valid_url(url):
                errors.append(f'{label}: invalid HTTPS URL: {url!r}')
        try:
            day = dt.date.fromisoformat(r['checked_on'])
            if day > dt.datetime.now(dt.timezone.utc).date() + dt.timedelta(days=1):
                errors.append(f'{label}: future review date')
        except ValueError:
            errors.append(f'{label}: invalid review date')
    for f in FAMILIES:
        members = {r.get('id') for r in rows if r.get('family') == f['id']}
        if not members:
            errors.append(f'Empty family: {f["id"]}')
        for example in f['examples']:
            if example not in members:
                errors.append(f'Invalid featured example for {f["id"]}: {example}')
    return errors


def main() -> int:
    errors = validate(load_rows())
    if errors:
        print('\n'.join('ERROR ' + e for e in errors), file=sys.stderr)
        return 1
    print(f'Validated {len(load_rows())} unique records and {len(FAMILIES)} families in {CSV_PATH.name}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
