"""Offline, source-grounded homepage metadata; popularity never determines order."""
from __future__ import annotations

import datetime as dt
import html
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z')
LABELS = {'paper': ('Paper', '论文'), 'blog': ('Blog', '博客'), 'case': ('Case report', '案例报告')}


def repository_from_url(url: str) -> tuple[str, bool] | None:
    """Return the requested repository and whether the URL selects a subproject."""
    u = urlsplit(url)
    if u.scheme != 'https' or u.netloc.lower() != 'github.com':
        return None
    parts = u.path.strip('/').split('/')
    if len(parts) < 2:
        return None
    repo = '/'.join(parts[:2])
    if not REPOSITORY.fullmatch(repo):
        return None
    return repo.lower(), len(parts) > 2 or bool(u.fragment)


def format_stars(value: int) -> str:
    if type(value) is not int or value < 0:
        raise ValueError('Star count must be a nonnegative integer')
    if value < 1000:
        return str(value)
    scale, suffix = (1_000_000, 'm') if value >= 999_950 else (1000, 'k')
    return f'{value / scale:.1f}'.rstrip('0').rstrip('.') + suffix


def valid_date(value: object) -> bool:
    try:
        return isinstance(value, str) and dt.date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def valid_https(value: object) -> bool:
    if not isinstance(value, str) or re.search(r'[\s<>"|()]', value):
        return False
    u = urlsplit(value)
    return u.scheme == 'https' and bool(u.hostname) and not u.username and not u.password


def validate_config(config: dict, rows: list[dict], cases: list[dict], reading: str) -> None:
    if set(config) != {'schema_version', 'parent_repository_ids', 'links', 'recent'} or config['schema_version'] != 1:
        raise ValueError('Unsupported homepage metadata schema')
    by_id = {r['id']: r for r in rows}
    parents = config['parent_repository_ids']
    if len(parents) != len(set(parents)) or any(p not in by_id or not repository_from_url(by_id[p]['url']) for p in parents):
        raise ValueError('Parent-repository overrides must identify unique GitHub entries')
    reading_urls = set(re.findall(r'\]\((https://[^\s)]+)\)', reading))
    for project_id, links in config['links'].items():
        if project_id not in by_id or not isinstance(links, list):
            raise ValueError('Source links reference an unknown project')
        evidence = set(by_id[project_id]['evidence_urls'].split(';'))
        for case in cases:
            if case['project_ids'][0] == project_id:
                evidence.update(case['evidence_urls'])
        seen = set()
        for link in links:
            if set(link) != {'kind', 'url', 'provenance'} or link['kind'] not in LABELS:
                raise ValueError('Invalid source-link kind or fields')
            if link['kind'] in seen or not valid_https(link['url']) or link['url'] == by_id[project_id]['url']:
                raise ValueError('Duplicate source kind, invalid URL or repeated upstream link')
            seen.add(link['kind'])
            allowed = evidence if link['provenance'] == 'catalog' else reading_urls if link['provenance'] == 'reading-list' else set()
            if link['url'] not in allowed:
                raise ValueError(f'Homepage source is not in reviewed evidence: {project_id}')
    recent_ids = set()
    for item in config['recent']:
        if set(item) != {'id', 'added_on', 'label'} or item['id'] not in by_id or item['id'] in recent_ids:
            raise ValueError('Recent additions must be unique existing projects')
        if not valid_date(item['added_on']) or not isinstance(item['label'], str) or not item['label'].strip():
            raise ValueError('Recent additions need an actual catalog-addition date and label')
        recent_ids.add(item['id'])


def validate_stats(cache: dict) -> None:
    if set(cache) != {'schema_version', 'repositories'} or cache['schema_version'] != 1:
        raise ValueError('Unsupported GitHub snapshot schema')
    if not isinstance(cache['repositories'], dict):
        raise ValueError('Repository snapshots must be an object')
    for repo, item in cache['repositories'].items():
        if not REPOSITORY.fullmatch(repo) or repo != repo.lower() or not isinstance(item, dict):
            raise ValueError('Invalid repository snapshot identity')
        if item.get('status') not in {'ok', 'unavailable'} or not valid_date(item.get('last_attempt_on')):
            raise ValueError('Snapshot status and attempt date required')
        stars = item.get('stars')
        if stars is not None:
            if type(stars) is not int or stars < 0 or not valid_date(item.get('fetched_on')):
                raise ValueError('Invalid star value or observation date')
            if type(item.get('repository_id')) is not int or item['repository_id'] < 1:
                raise ValueError('Missing stable GitHub repository ID')
            if not REPOSITORY.fullmatch(item.get('full_name', '')):
                raise ValueError('Invalid canonical repository name')
        elif item.get('status') == 'ok' or item.get('fetched_on') is not None:
            raise ValueError('Missing stars cannot be a successful observation')


def load_bundle(rows: list[dict], root: Path = ROOT) -> tuple[dict, dict]:
    config = json.loads((root / 'catalog/homepage_metadata.json').read_text(encoding='utf-8'))
    cache = json.loads((root / 'catalog/github_stats.json').read_text(encoding='utf-8'))
    cases = json.loads((root / 'catalog/cases.json').read_text(encoding='utf-8'))
    reading = (root / 'docs/reading-list.md').read_text(encoding='utf-8')
    validate_config(config, rows, cases, reading)
    validate_stats(cache)
    return config, cache


def entry_extras(row: dict, config: dict, cache: dict, chinese: bool = False) -> str:
    parts, hints = [], []
    repo = repository_from_url(row['url'])
    if repo:
        requested, subproject = repo
        item = cache['repositories'].get(requested, {})
        stars = item.get('stars')
        if type(stars) is int:
            parent = subproject or row['id'] in config['parent_repository_ids']
            label = f'★&nbsp;{format_stars(stars)}'
            if parent:
                label += '（母仓库）' if chinese else '&nbsp;(parent repo)'
            if item.get('status') != 'ok':
                label += '（缓存）' if chinese else '&nbsp;(cached)'
            parts.append(label)
            hints.append(f'{item["full_name"]}: {stars:,} repository stars; observed {item["fetched_on"]}')
    for link in config['links'].get(row['id'], []):
        label = LABELS[link['kind']][1 if chinese else 0]
        parts.append(f'[{label}]({link["url"]})')
    if not parts:
        return ''
    hint = '; '.join(hints) or ('已核实来源' if chinese else 'Reviewed sources')
    return f' <sub title="{html.escape(hint, quote=True)}">{" · ".join(parts)}</sub>'


def recent_line(config: dict, chinese: bool = False) -> str:
    items = sorted(config['recent'], key=lambda item: item['added_on'], reverse=True)[:5]
    if not items:
        return ''
    dates = sorted({item['added_on'] for item in items})
    date_label = dates[0] if len(dates) == 1 else f'{dates[0]}–{dates[-1]}'
    label = '近期收录' if chinese else 'Recently added'
    hint = '目录收录日期，不是项目发布日期' if chinese else 'Catalog addition dates, not project release dates'
    links = ' · '.join(f'[{html.escape(item["label"], quote=False)}](#project-{item["id"]})' for item in items)
    more = '[更新记录](docs/updates.md)' if chinese else '[Updates](docs/updates.md)'
    return f'<sub title="{hint}"><b>{label}</b> · {date_label} · {links} · {more}</sub>'


def snapshot_note(rows: list[dict], cache: dict, chinese: bool = False) -> str:
    repos = {parsed[0] for row in rows if (parsed := repository_from_url(row['url']))}
    records = [cache['repositories'][repo] for repo in sorted(repos) if repo in cache['repositories']]
    dates = sorted({item['fetched_on'] for item in records if type(item.get('stars')) is int})
    if not dates:
        return '[Star 数据与更新](docs/homepage-metadata.md)' if chinese else '[Star snapshots and refresh](docs/homepage-metadata.md)'
    date_label = dates[0] if len(dates) == 1 else f'{dates[0]}–{dates[-1]}'
    return (f'[★ 仓库 Star 快照 · {date_label}](docs/homepage-metadata.md)' if chinese else
            f'[★ Repository star snapshots · {date_label}](docs/homepage-metadata.md)')
