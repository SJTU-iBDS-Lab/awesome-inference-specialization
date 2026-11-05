"""Curated reading routes, with scope copied from canonical project records."""
from __future__ import annotations

import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def load_routes(rows: list[dict], path: Path | None = None) -> dict:
    routes = json.loads((path or ROOT / 'catalog/discovery.json').read_text(encoding='utf-8'))
    validate_routes(routes, rows)
    return routes


def validate_routes(routes: dict, rows: list[dict]) -> None:
    known = {row['id'] for row in rows}
    seen = set()
    if set(routes) != {'hardware', 'models'}:
        raise ValueError('Discovery requires hardware and models routes')
    for groups in routes.values():
        if not groups:
            raise ValueError('Discovery groups must not be empty')
        for group in groups:
            identifier = group['id']
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identifier) or identifier in seen:
                raise ValueError(f'Invalid or duplicate discovery anchor: {identifier}')
            seen.add(identifier)
            if any(not isinstance(group[k], str) or not group[k].strip()
                   for k in ('label', 'label_cn', 'note', 'note_cn')):
                raise ValueError(f'Empty bilingual discovery text: {identifier}')
            ids = group['projects']
            if not ids or len(ids) != len(set(ids)) or not set(ids) <= known:
                raise ValueError(f'Unknown, empty or repeated discovery project: {identifier}')
            if not isinstance(group['homepage'], bool):
                raise ValueError(f'Discovery homepage flag must be boolean: {identifier}')


def cell(value: str) -> str:
    return html.escape(value, quote=False).replace('|', '&#124;').replace('\n', ' ')


def render_shortcuts(rows: list[dict], chinese: bool = False) -> list[str]:
    routes = load_routes(rows)
    key = 'label_cn' if chinese else 'label'
    # Word joiners keep two-character Chinese labels intact in GitHub's narrow tables.
    lines = ['<!-- DISCOVERY-START -->', '<a id="find-a-stack"></a>', '',
             '| 入&#8288;口 | 已收录的执行路径 |' if chinese else '| Find a stack | Explore reviewed paths |',
             '| :--- | :--- |']
    for kind, en, cn in [('hardware', 'Hardware', '硬&#8288;件'), ('models', 'Models', '模&#8288;型')]:
        links = [f'[{cell(g[key])}](docs/find-a-stack.md#{g["id"]})' for g in routes[kind] if g['homepage']]
        links.append(f'[{"更多" if chinese else "More"}](docs/find-a-stack.md#{kind})')
        lines.append(f'| **{cn if chinese else en}** | ' + ' · '.join(links) + ' |')
    lines += ['', '<sub>' + ('范围以已查模型、设备和配置为准；不代表兼容性认证或性能排名。' if chinese else
                            'Scope follows the reviewed model, device and configuration; no compatibility certification or speed ranking.') + '</sub>',
              '<!-- DISCOVERY-END -->', '']
    return lines


def render_guide(rows: list[dict]) -> str:
    routes, by_id = load_routes(rows), {r['id']: r for r in rows}
    lines = ['# Find a stack / 按硬件与模型查找', '',
             '> Generated from [discovery.json](../catalog/discovery.json) and [projects.csv](../catalog/projects.csv).', '',
             '[Home](../README.md#find-a-stack) · [中文首页](../README_CN.md#find-a-stack) · [Complete catalog / 全目录](catalog.md) · [Mobile execution constraints / 移动端约束](device-execution-matrix.md)', '',
             'Curated entry points into existing records, not an exhaustive support matrix or a recommendation ranking. A project may appear in multiple routes and is still counted once. Scope is copied verbatim from its reviewed catalog record; follow Details for precision, model changes, source evidence and benchmark limits. No benchmarks were independently reproduced here.', '',
             '这些入口指向现有记录，不是完整兼容性表或性能推荐。跨组重复引用不增加项目数；具体范围原样取自已核查记录。设备名称不意味着支持该系列所有型号，模型家族也不意味着支持所有检查点。详情保留量化、模型改动、源码与基准限制；本仓库未独立复现性能。', '']
    for kind, en, cn in [('hardware', 'By hardware', '按硬件'), ('models', 'By model', '按模型')]:
        lines += [f'<a id="{kind}"></a>', '', f'## {en} / {cn}', '',
                  ' · '.join(f'[{cell(g["label"])} / {cell(g["label_cn"])}](#{g["id"]})'
                             if g['label'] != g['label_cn'] else f'[{cell(g["label"])}](#{g["id"]})'
                             for g in routes[kind]), '']
        for group in routes[kind]:
            title = group['label'] if group['label'] == group['label_cn'] else group['label'] + ' / ' + group['label_cn']
            lines += [f'<a id="{group["id"]}"></a>', '', f'### {cell(title)}', '',
                      cell(group['note']), '', cell(group['note_cn']), '',
                      '| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |', '| --- | --- | --- |']
            for id in group['projects']:
                row = by_id[id]
                lines.append(f'| [{cell(row["project"])}](catalog.md#{id}) | {cell(row["target"])} | `{row["source_visibility"]}` · {row["checked_on"]} · [Details / 详情](catalog.md#{id}) |')
            lines += ['', f'[↑ {en} / {cn}](#{kind})', '']
    return '\n'.join(lines)
