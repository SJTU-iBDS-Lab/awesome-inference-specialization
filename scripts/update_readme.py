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


def project_links(ids: list[str], by_id: dict[str, dict[str, str]], prefix: str = 'docs/') -> str:
    return ', '.join(f"[{md_cell(by_id[id]['project'])}]({prefix}catalog.md#{id})" for id in ids)


def render_overview(rows: list[dict[str, str]], chinese: bool = False) -> str:
    by_id = {r['id']: r for r in rows}
    key = 'title_cn' if chinese else 'title'
    desc_key = 'description_cn' if chinese else 'description'
    counts = {role['id']: sum(r['catalog_role'] == role['id'] for r in rows) for role in SCHEMA['roles']}
    counts_text = ' · '.join(f"{counts[role['id']]} {role[key]}" for role in SCHEMA['roles'])
    if chinese:
        lines = [f"**{len(rows)} 个条目：{counts_text}**", '',
                 '先看系统利用了什么条件，再看它如何构建。完整条目按[三个阅读角色](docs/systems.md)组织，原有八类机制用于交叉检索。', '',
                 '### 专用推理系统', '', '| 专用化机会 | 代表系统 | 关注的执行改变 |', '| --- | --- | --- |']
    else:
        lines = [f"**{len(rows)} entries: {counts_text}**", '',
                 'Start with the constraints a system exploits, then follow its construction. Browse all entries by [reading role](docs/systems.md); the eight mechanism families remain a cross-cutting index.', '',
                 '### Specialized inference systems', '', '| Specialization opportunity | Representative systems | Execution decision |', '| --- | --- | --- |']
    for group in SCHEMA['system_showcases']:
        lines.append(f"| {group[key]} | {project_links(group['examples'], by_id)} | {group[desc_key]} |")
    lines += ['', '### 四种构建方式' if chinese else '### Four construction routes', '',
              '| 构建方式 | 构建什么、怎样构建 | 案例 |' if chinese else '| Route | What is built and how | Cases |', '| --- | --- | --- |']
    for group in SCHEMA['build_routes']:
        lines.append(f"| {group[key]} | {group[desc_key]} | {project_links(group['examples'], by_id)} |")
    lines += ['', '这些方式可以组合；使用智能体不说明产物必然更快，测试通过也只覆盖相应验证条件。' if chinese else 'Routes can be combined. Agent involvement does not establish a faster artifact; passing tests establishes behavior only within their validation scope.', '',
              '### 支撑基础设施与参照' if chinese else '### Supporting infrastructure and references', '',
              '以下项目提供复用组件、比较基线和评测条件，帮助构建和评价前面的专用系统。' if chinese else 'These projects supply reusable components, comparison baselines and evaluation conditions for the systems above.', '']
    for group in SCHEMA['support_groups']:
        lines.append(f"- **{group[key]}:** {project_links(group['examples'], by_id)}.")
    lines += ['', '### 按机制继续查找' if chinese else '### Continue by mechanism', '',
              ' · '.join(f"[{f[key]} ({sum(r['family'] == f['id'] for r in rows)})](docs/catalog.md#{f['id']})" for f in FAMILIES), '',
              f"来源核查日期：{max(r['checked_on'] for r in rows)}。精选案例属于阅读入口，不代表性能或成熟度排名。" if chinese else f"Source review: {max(r['checked_on'] for r in rows)}. Featured cases are reading entry points, not a performance or maturity ranking."]
    return '\n'.join(lines)


def render_systems(rows: list[dict[str, str]]) -> str:
    lines = ['# Systems, construction and supporting infrastructure', '',
             '> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Mechanism index](catalog.md) · [Classification](taxonomy.md) · [Research agenda](research-agenda.md)', '',
             'Read **constraints → execution decisions → artifacts → validation → maintenance**. The roles below explain why an entry is here; they do not rank quality, maturity or importance. Each project has one editorial reading role and retains independent mechanism and artifact labels.', '',
             '按专用系统、构建流程和支撑基础设施浏览；点击项目进入机制说明、适用边界与直接证据。角色用于组织阅读，不能据此认定系统更快或更成熟。', '',
             ' · '.join(f"[{role['title']}](#{role['id']})" for role in SCHEMA['roles']), '']
    for role in SCHEMA['roles']:
        members = sorted((r for r in rows if r['catalog_role'] == role['id']), key=lambda r: r['project'].lower())
        lines += [f'<a id="{role["id"]}"></a>', '', f"## {role['title']} / {role['title_cn']} ({len(members)})", '',
                  role['description'], '', role['description_cn'], '', '| Project and evidence | Inspected scope | Artifact |', '| --- | --- | --- |']
        for r in members:
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}) | {md_cell(r['target'])} | {r['artifact_type']} |")
        lines.append('')
    return '\n'.join(lines) + '\n'


def updated_text(before: str, generated: str) -> str:
    if before.count(START) != 1 or before.count(END) != 1 or before.index(START) > before.index(END):
        raise ValueError('Expected one ordered pair of catalog markers')
    prefix, after = before.split(START, 1)
    _, suffix = after.split(END, 1)
    return prefix + START + '\n\n' + generated + '\n\n' + END + suffix


def render_catalog(rows: list[dict[str, str]]) -> str:
    lines = ['# Project catalog / 项目全目录', '',
             '> Generated from [projects.csv](../catalog/projects.csv); edit the CSV, then run the generator.', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Systems & construction](systems.md) · [Comparison](comparison.md) · [Taxonomy](taxonomy.md) · [Evidence policy](evidence-policy.md)', '',
             f"{len(rows)} entries. Source review: {max(r['checked_on'] for r in rows)}. Descriptions report inspected mechanisms; no project benchmark was independently reproduced in this survey.", '',
             'Use the family links below, or search this page for a model, device, mechanism or project. Source visibility is not a license or correctness certification. Semantic labels identify evaluation obligations, not proven equivalence.', '',
             ' · '.join(f"[{f['title']}](#{f['id']})" for f in FAMILIES), '']
    for f in FAMILIES:
        these = sorted((r for r in rows if r['family'] == f['id']), key=lambda r: r['project'].lower())
        lines += [f'<a id="{f["id"]}"></a>', '', f"## {f['title']} / {f['title_cn']} ({len(these)})", '', f"**{f['question']}** {f['description']}", '']
        for r in these:
            lines += [f'<a id="{r["id"]}"></a>', '', f"### [{md_cell(r['project'])}]({r['url']})", '',
                      f"[{r['catalog_role']}](systems.md#{r['catalog_role']}) · `{r['artifact_type']}` · `{' / '.join(items(r, 'domains'))}` · **{SOURCES[r['source_visibility']]}**", '',
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
             '[Home](../README.md) · [Systems & construction](systems.md) · [Full descriptions and evidence](catalog.md) · [How to read semantic labels](taxonomy.md#semantic-effects)', '',
             'Reading roles identify systems, construction workflows and supporting references. Modality tags refer to the inspected scope, not exhaustive compatibility. `general` marks tensor/compiler infrastructure. Hardware and model constraints are in each linked record. Source visibility does not establish license suitability.', '']
    for f in FAMILIES:
        lines += [f"## {f['title']}", '', '| Project / reading role | Artifact / modality | Semantic considerations |', '| --- | --- | --- |']
        for r in sorted((r for r in rows if r['family'] == f['id']), key=lambda r: r['project'].lower()):
            status = '' if r['source_visibility'] == 'public-code' else f" · **{SOURCES[r['source_visibility']]}**"
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}) · {r['catalog_role']}{status} | {r['artifact_type']} / {', '.join(items(r, 'domains'))} | {effect_label(r)} |")
        lines.append('')
    return '\n'.join(lines) + '\n'


def generated_files(rows: list[dict[str, str]]) -> dict[Path, str]:
    outputs = {}
    for name, chinese in [('README.md', False), ('README_CN.md', True)]:
        path = ROOT / name
        outputs[path] = updated_text(path.read_text(encoding='utf-8'), render_overview(rows, chinese))
    outputs[ROOT / 'docs/systems.md'] = render_systems(rows)
    outputs[ROOT / 'docs/catalog.md'] = render_catalog(rows)
    outputs[ROOT / 'docs/comparison.md'] = render_comparison(rows)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Check all five generated views')
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
    print(f'{len(rows)} entries; five generated views ' + ('in sync' if args.check else 'updated'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
