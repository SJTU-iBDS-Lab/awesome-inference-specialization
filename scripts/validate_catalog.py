#!/usr/bin/env python3
"""Offline structural checks for the machine-readable research catalog."""
from __future__ import annotations

import datetime as dt
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

from update_readme import CSV_PATH, CATEGORIES, load_rows

AXES = set('model hardware memory precision workload domain algorithm execution parallelism builder verification'.split())
CATEGORIES_SET = {x[0] for x in CATEGORIES}
TIERS = {'Core', 'Adjacent', 'Watchlist'}
VISIBILITY = {'public-code', 'closed-core', 'documentation-only', 'review-only'}
AI = {'intrinsic', 'disclosed', 'not-established'}
MANDATORY = {'id', 'project', 'category', 'tier', 'axes', 'target', 'mechanism',
             'source_visibility', 'ai_involvement', 'url', 'evidence_url', 'caveat', 'checked_on'}


def valid_url(s: str) -> bool:
    u = urlparse(s)
    return u.scheme == 'https' and bool(u.netloc) and not re.search(r'\s', s)


def main() -> int:
    rows = load_rows()
    errors: list[str] = []
    if not rows:
        errors.append('Catalog is empty')
    if rows:
        missing = MANDATORY - rows[0].keys()
        if missing:
            errors.append(f'Missing CSV columns: {sorted(missing)}')
    seen: set[str] = set()
    for index, r in enumerate(rows, start=2):
        label = f'CSV row {index}'
        absent = [key for key in MANDATORY if not r.get(key, '').strip()]
        if absent:
            errors.append(f'{label}: missing {sorted(absent)}')
            continue
        id_ = r['id'].strip()
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', id_):
            errors.append(f'{label}: invalid id {id_!r}')
        if id_ in seen:
            errors.append(f'{label}: duplicate id {id_}')
        seen.add(id_)
        if r['category'] not in CATEGORIES_SET:
            errors.append(f'{label}: unsupported category {r["category"]}')
        if r['tier'] not in TIERS:
            errors.append(f'{label}: unsupported tier {r["tier"]}')
        if r['source_visibility'] not in VISIBILITY:
            errors.append(f'{label}: unsupported source visibility')
        if r['ai_involvement'] not in AI:
            errors.append(f'{label}: unsupported AI involvement')
        bad_axes = set(r['axes'].split(';')) - AXES
        if bad_axes:
            errors.append(f'{label}: unknown axes {sorted(bad_axes)}')
        for key in ('url', 'evidence_url'):
            if not valid_url(r[key]):
                errors.append(f'{label}: invalid {key} {r[key]!r}')
        try:
            date = dt.date.fromisoformat(r['checked_on'])
            if date > dt.date.today() + dt.timedelta(days=1):
                errors.append(f'{label}: future checked_on date {date}')
        except ValueError:
            errors.append(f'{label}: invalid checked_on date')
    if errors:
        print('\n'.join('ERROR ' + e for e in errors), file=sys.stderr)
        return 1
    print(f'Catalog validated: {len(rows)} unique entries in {CSV_PATH.relative_to(Path(__file__).resolve().parents[1])}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
