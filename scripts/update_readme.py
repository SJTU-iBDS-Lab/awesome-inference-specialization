#!/usr/bin/env python3
"""Generate bilingual overviews and detailed views from the canonical CSV."""
from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'catalog' / 'projects.csv'
SCHEMA = json.loads((ROOT / 'catalog' / 'schema.json').read_text(encoding='utf-8'))
FAMILIES = SCHEMA['families']
START = '<!-- CATALOG-START -->'
END = '<!-- CATALOG-END -->'
SOURCES = {'public-code': 'public code', 'closed-core': 'closed core',
           'documentation-only': 'documentation only', 'review-only': 'review-use restriction'}
EFFECTS = {'layout-scheduling': 'layout / scheduling', 'reduced-precision': 'reduced precision',
           'selective-approximation': 'selective approximation', 'stale-state': 'earlier-state reuse',
           'verified-proposals': 'target-verified proposals', 'trained-model': 'model / router training',
           'configurable': 'configuration-dependent', 'tool-dependent': 'generated-artifact dependent'}


def md_cell(value: str) -> str:
    return html.escape(str(value), quote=False).replace('|', '&#124;').replace('\n', ' ').strip()


def load_rows(path: Path = CSV_PATH) -> list[dict[str, str]]:
    with path.open(encoding='utf-8', newline='') as fp:
        return list(csv.DictReader(fp))


def items(row: dict[str, str], field: str) -> list[str]:
    return row[field].split(';')


def effect_label(row: dict[str, str]) -> str:
    return ', '.join(EFFECTS[x] for x in items(row, 'semantic_effect'))


def render_overview(rows: list[dict[str, str]], chinese: bool = False) -> str:
    by_id = {r['id']: r for r in rows}
    day = max(r['checked_on'] for r in rows)
    if chinese:
        lines = [f'**{len(rows)} 个项目 · 8 个机制入口 · 最近核查 {day}**', '',
                 '每个项目选一个主要入口；模态、产物类型和具体机制另外标注。构建与验证工具单独标识，数量不代表质量排名。', '',
                 '| 机制入口 | 改变了什么 | 从这些项目开始 |', '| --- | --- | --- |']
    else:
        lines = [f'**{len(rows)} projects · 8 mechanism families · Last source review {day}**', '',
                 'One primary home per project; modality, artifact type and mechanism tags remain independent. Construction tools support execution rather than being another runtime class.', '',
                 '| Mechanism family | What changes | Start with |', '| --- | --- | --- |']
    for f in FAMILIES:
        count = sum(r['family'] == f['id'] for r in rows)
        title = f['title_cn'] if chinese else f['title']
        desc = f['description_cn'] if chinese else f['description']
        refs = ', '.join(f"[{md_cell(by_id[id]['project'])}](docs/catalog.md#{id})" for id in f['examples'])
        lines.append(f"| [{title} ({count})](docs/catalog.md#{f['id']}) | {desc} | {refs} |")
    return '\n'.join(lines)


def updated_text(before: str, generated: str) -> str:
    if before.count(START) != 1 or before.count(END) != 1 or before.index(START) > before.index(END):
        raise ValueError('Expected one ordered pair of catalog markers')
    prefix, after = before.split(START, 1)
    _, suffix = after.split(END, 1)
    return prefix + START + '\n\n' + generated + '\n\n' + END + suffix


def render_catalog(rows: list[dict[str, str]]) -> str:
    lines = ['# Project catalog / 项目全目录', '',
             '> Generated from [projects.csv](../catalog/projects.csv); edit the CSV, then run the generator.', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Comparison](comparison.md) · [Taxonomy](taxonomy.md) · [Evidence policy](evidence-policy.md)', '',
             f"{len(rows)} entries. Source review: {max(r['checked_on'] for r in rows)}. Descriptions report inspected mechanisms; no project benchmark was independently reproduced in this survey.", '',
             'Use the family links below, or search this page for a model, device, mechanism or project. Source visibility is not a license or correctness certification. Semantic labels identify evaluation obligations, not proven equivalence.', '',
             ' · '.join(f"[{f['title']}](#{f['id']})" for f in FAMILIES), '']
    for f in FAMILIES:
        these = sorted((r for r in rows if r['family'] == f['id']), key=lambda r: r['project'].lower())
        lines += [f'<a id="{f["id"]}"></a>', '', f"## {f['title']} / {f['title_cn']} ({len(these)})", '', f"**{f['question']}** {f['description']}", '']
        for r in these:
            lines += [f'<a id="{r["id"]}"></a>', '', f"### [{md_cell(r['project'])}]({r['url']})", '',
                      f"`{r['artifact_type']}` · `{' / '.join(items(r, 'domains'))}` · **{SOURCES[r['source_visibility']]}**", '',
                      md_cell(r['mechanism']), '', f"**Scope:** {md_cell(r['target'])}", '',
                      f"**Boundary:** {md_cell(r['caveat'])}", '',
                      f"**Semantic considerations:** {effect_label(r)}.", '',
                      '<details>', '<summary>Mechanism tags and source evidence / 机制标签与证据</summary>', '',
                      '**Mechanisms:** ' + ', '.join(f'`{x}`' for x in items(r, 'mechanisms')) + '.', '',
                      '**Constraints:** ' + ', '.join(f'`{x}`' for x in items(r, 'constraints')) + '.', '',
                      '**Evidence:** ' + ' · '.join(f'[Source {i}]({url})' for i, url in enumerate(items(r, 'evidence_urls'), 1)) + '.', '',
                      f"**Reviewed:** {r['checked_on']} · **AI involvement:** `{r['ai_involvement']}` · **Discovery:** `{r['discovery']}`.", '',
                      '</details>', '']
    return '\n'.join(lines) + '\n'


def render_comparison(rows: list[dict[str, str]]) -> str:
    lines = ['# Comparison by artifact and semantic effect', '',
             '> Generated from [projects.csv](../catalog/projects.csv). This is a capability index, not a speed or quality ranking.', '',
             '[Home](../README.md) · [Full descriptions and evidence](catalog.md) · [How to read semantic labels](taxonomy.md#semantic-effects)', '',
             'Modality tags refer to the inspected scope, not exhaustive compatibility. `general` marks tensor/compiler infrastructure. Hardware and model constraints are in each linked record. Source visibility does not establish license suitability.', '']
    for f in FAMILIES:
        lines += [f"## {f['title']}", '', '| Project | Artifact / modality | Semantic considerations |', '| --- | --- | --- |']
        for r in sorted((r for r in rows if r['family'] == f['id']), key=lambda r: r['project'].lower()):
            status = '' if r['source_visibility'] == 'public-code' else f" · **{SOURCES[r['source_visibility']]}**"
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}){status} | {r['artifact_type']} / {', '.join(items(r, 'domains'))} | {effect_label(r)} |")
        lines.append('')
    return '\n'.join(lines) + '\n'


def generated_files(rows: list[dict[str, str]]) -> dict[Path, str]:
    outputs = {}
    for name, chinese in [('README.md', False), ('README_CN.md', True)]:
        path = ROOT / name
        outputs[path] = updated_text(path.read_text(encoding='utf-8'), render_overview(rows, chinese))
    outputs[ROOT / 'docs/catalog.md'] = render_catalog(rows)
    outputs[ROOT / 'docs/comparison.md'] = render_comparison(rows)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Check all four generated views')
    args = parser.parse_args()
    rows = load_rows()
    if not rows:
        parser.error('Catalog is empty')
    changed = []
    for path, content in generated_files(rows).items():
        if not path.exists() or path.read_text(encoding='utf-8') != content:
            changed.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.write_text(content, encoding='utf-8')
    if args.check and changed:
        print('Generated views are stale: ' + ', '.join(changed), file=sys.stderr)
        return 1
    print(f'{len(rows)} entries; four generated views ' + ('in sync' if args.check else 'updated'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
