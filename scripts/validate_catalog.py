#!/usr/bin/env python3
"""Offline validation of the catalog, controlled facets and evidence pointers."""
from __future__ import annotations

import datetime as dt
import re
import sys
from urllib.parse import urlparse

from update_readme import CSV_PATH, FAMILIES, SCHEMA, CASE_QUESTIONS, load_rows, load_cases, load_showcase

FIELDS = set('id project survey_role relevance_note catalog_role family domains artifact_type constraints mechanisms target mechanism semantic_effect source_visibility ai_involvement url evidence_urls caveat checked_on discovery'.split())
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
    enums = {'survey_role': {role['id'] for role in SCHEMA['survey_roles']},
             'catalog_role': {role['id'] for role in SCHEMA['roles']}, 'family': family_ids, 'artifact_type': set(SCHEMA['artifact_types']),
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
    for group_name in ('build_routes', 'support_groups'):
        for group in SCHEMA[group_name]:
            for example in group['examples']:
                record = next((r for r in rows if r.get('id') == example), None)
                if record is None:
                    errors.append(f'Missing showcase example: {example}')
                elif group_name == 'support_groups' and record.get('catalog_role') != 'support':
                    errors.append(f'Support list must point to a supporting entry: {example}')
    support_ids = [id for group in SCHEMA['support_groups'] for id in group['examples']]
    if len(support_ids) != len(set(support_ids)) or set(support_ids) != {r['id'] for r in rows if r['catalog_role'] == 'support'}:
        errors.append('Companion resource groups must cover each support project exactly once')
    benchmark_ids = [entry['id'] for entry in SCHEMA['benchmark_entries']]
    if len(benchmark_ids) != len(set(benchmark_ids)) or set(benchmark_ids) != {r['id'] for r in rows if r['catalog_role'] == 'benchmark'}:
        errors.append('Benchmark index must cover each benchmark project exactly once')
    by_id = {r['id']: r for r in rows}
    for entry in SCHEMA['homepage_construction']:
        if by_id.get(entry['id'], {}).get('catalog_role') != 'construction':
            errors.append(f'Construction showcase must identify a construction workflow: {entry["id"]}')
    return errors


def validate_cases(cases: list[dict], rows: list[dict[str, str]]) -> list[str]:
    """Keep homepage claims tied to a complete, sourced construction case."""
    errors = []
    fields = {'id', 'title', 'project_ids', 'summary', 'summary_cn', 'evidence_urls', 'checked_on'} | {q[0] for q in CASE_QUESTIONS}
    by_id = {r['id']: r for r in rows}
    ids, linked = set(), set()
    if not cases:
        return ['Core case collection is empty']
    for case in cases:
        label = f"Case {case.get('id', '?')}"
        if set(case) != fields:
            errors.append(f'{label}: fields do not match case schema')
            continue
        if any(not isinstance(case[f], str) or not case[f].strip() for f in fields - {'project_ids', 'evidence_urls'}):
            errors.append(f'{label}: missing case text; state unknowns explicitly')
            continue
        if not TAG.fullmatch(case['id']) or case['id'] in ids:
            errors.append(f'{label}: invalid or duplicate case id')
        ids.add(case['id'])
        projects = case['project_ids']
        if not isinstance(projects, list) or not projects or any(not isinstance(p, str) for p in projects):
            errors.append(f'{label}: invalid project links')
            continue
        if len(projects) != len(set(projects)):
            errors.append(f'{label}: duplicate project links')
        for project in projects:
            if project not in by_id:
                errors.append(f'{label}: missing project {project}')
            linked.add(project)
        if not any(by_id.get(project, {}).get('survey_role') == 'core' for project in projects):
            errors.append(f'{label}: must identify a core project, not only dependencies')
        urls = case['evidence_urls']
        if not isinstance(urls, list) or any(not isinstance(u, str) for u in urls):
            errors.append(f'{label}: invalid case evidence')
        elif len(urls) < 2 or len(urls) != len(set(urls)) or any(not valid_url(u) for u in urls):
            errors.append(f'{label}: need distinct official HTTPS evidence pointers')
        try:
            if dt.date.fromisoformat(case['checked_on']) > dt.datetime.now(dt.timezone.utc).date() + dt.timedelta(days=1):
                errors.append(f'{label}: future case review date')
        except ValueError:
            errors.append(f'{label}: invalid case review date')
    for r in rows:
        if r['survey_role'] == 'core' and r['id'] not in linked:
            errors.append(f"Core project lacks a construction case: {r['id']}")
    featured = [id for group in SCHEMA['case_groups'] for id in group['examples']]
    if len(featured) != len(set(featured)):
        errors.append('Duplicate case-index entry')
    if set(featured) != ids:
        errors.append('Case index must match the curated case collection')
    for group in SCHEMA['case_groups']:
        if not set(group.get('featured', [])).issubset(group['examples']):
            errors.append('Homepage selection must belong to its case reading route')
    return errors


def validate_showcase(selections: list[dict], cases: list[dict], rows: list[dict[str, str]]) -> list[str]:
    """Keep compact bilingual summaries tied to existing, sourced case records."""
    errors = []
    text_fields = {field + suffix for field in ('why', 'scope', 'boundary', 'reuse', 'validation')
                   for suffix in ('', '_cn')}
    fields = {'case_id', 'project_id'} | text_fields
    by_case = {c['id']: c for c in cases}
    by_project = {r['id']: r for r in rows}
    seen = set()
    if not 10 <= len(selections) <= 15:
        errors.append('Reading selection must contain 10–15 cases')
    for entry in selections:
        if not isinstance(entry, dict) or set(entry) != fields:
            errors.append('Reading selection fields do not match schema')
            continue
        if any(not isinstance(v, str) or not v.strip() for v in entry.values()):
            errors.append('Reading selection requires nonempty bilingual text and identifiers')
            continue
        case_id = entry['case_id']
        if case_id in seen:
            errors.append(f'Duplicate reading selection: {case_id}')
        seen.add(case_id)
        case = by_case.get(case_id)
        if case is None:
            errors.append(f'Reading selection references missing case: {case_id}')
        elif entry['project_id'] not in case['project_ids'] or entry['project_id'] not in by_project:
            errors.append(f'Reading selection project must belong to its case: {case_id}')
    return errors


def main() -> int:
    rows, cases = load_rows(), load_cases()
    errors = validate(rows) + validate_cases(cases, rows) + validate_showcase(load_showcase(), cases, rows)
    if errors:
        print('\n'.join('ERROR ' + e for e in errors), file=sys.stderr)
        return 1
    print(f'Validated {len(rows)} unique records, {len(cases)} core cases and {len(FAMILIES)} mechanism families')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
