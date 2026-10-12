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
CASES_PATH = ROOT / 'catalog' / 'cases.json'
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


def load_cases(path: Path = CASES_PATH) -> list[dict]:
    return json.loads(path.read_text(encoding='utf-8'))


def items(row: dict[str, str], field: str) -> list[str]:
    return row[field].split(';')


def effect_label(row: dict[str, str]) -> str:
    return ', '.join(EFFECTS[x] for x in items(row, 'semantic_effect'))


def project_links(ids: list[str], by_id: dict[str, dict[str, str]], prefix: str = 'docs/') -> str:
    return ', '.join(f"[{md_cell(by_id[id]['project'])}]({prefix}catalog.md#{id})" for id in ids)


def render_overview(rows: list[dict[str, str]], chinese: bool = False) -> str:
    cases = {c['id']: c for c in load_cases()}
    key = 'title_cn' if chinese else 'title'
    summary_key = 'summary_cn' if chinese else 'summary'
    inventory = (f"**[完整目录：{len(rows)} 个项目](docs/systems.md) · [精选分析：{len(cases)} 个案例](docs/cases.md)**" if chinese else
                 f"**[Full directory: {len(rows)} projects](docs/systems.md) · [Selected analyses: {len(cases)} cases](docs/cases.md)**")
    lines = [inventory, '', '先看构建过程与产出系统，再比较复用边界和证据缺口。以下分组只是阅读顺序；AI 参与不代表效果更好，未披露也不代表纯人工实现。' if chinese else
             'Follow the construction process to its resulting system, then examine reuse boundaries and missing evidence. These groups guide reading; AI involvement does not imply better results, and missing disclosure does not imply human-only implementation.', '']
    for group in SCHEMA['case_groups']:
        lines += [f"### {group[key]}", '', '| 案例 | 为什么研究它 |' if chinese else '| Case | Why study it? |', '| --- | --- |']
        for id in group['examples']:
            c = cases[id]
            lines.append(f"| [{md_cell(c['title'].split(':', 1)[0])}](docs/cases.md#{id}) | {md_cell(c[summary_key])} |")
        lines.append('')
    lines += ['### 把案例放回已有路线中比较' if chinese else '### Compare the cases with existing routes', '',
              '- [历史与相邻路线](docs/systems.md#adjacent)：ZeRO-Inference、FlexGen、DistServe、S-LoRA、MLC LLM 等，帮助判断哪些设计早已有之。' if chinese else
              '- [Historical and adjacent routes](docs/systems.md#adjacent): ZeRO-Inference, FlexGen, DistServe, S-LoRA and MLC LLM help establish which ideas already exist.',
              '- [共享基础与对照](docs/systems.md#foundation)：通用引擎、编译器、内核和评测工具，说明系统复用了什么、应该与什么比较。' if chinese else
              '- [Shared foundations and baselines](docs/systems.md#foundation): general engines, compilers, kernels and evaluators reveal what is reused and what a fair comparison requires.', '',
              '相关性是这些材料在本 Survey 中的作用，不是质量、成熟度或年代排名。完整[资料库](docs/systems.md)保留既有收录。' if chinese else
              'Relevance describes a record’s role in this survey, not its quality, maturity or age. The full [library](docs/systems.md) retains the broader collection.', '',
              '<details>', '<summary>按执行机制检索资料库 / Browse the library by execution mechanism</summary>', '',
              ' · '.join(f"[{f[key]}](docs/catalog.md#{f['id']})" for f in FAMILIES), '', '</details>']
    return '\n'.join(lines)


def render_systems(rows: list[dict[str, str]]) -> str:
    lines = ['# Survey library / 主题资料库', '',
             '> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Core case studies](cases.md) · [Construction comparison](comparison.md) · [Mechanism index](catalog.md) · [Classification](taxonomy.md)', '',
             'The research object is the construction of specialized execution stacks. Browse by **why an entry matters to this question**, independently of whether it is a system, construction workflow or supporting component. Relevance is not a quality or maturity ranking, and the adjacent group is not an age cutoff.', '',
             '先按与主题的关系阅读，再看产物角色和技术机制。原有资料保留，但相邻优化路线不作为构建范式变化的直接证据。', '',
             ' · '.join(f"[{role['title']}](#{role['id']})" for role in SCHEMA['survey_roles']), '']
    # Preserve incoming anchors for the former artifact-role index.
    for role in SCHEMA['roles']:
        lines += [f'<a id="{role["id"]}"></a>']
    lines += ['', 'Artifact roles retained as independent labels: ' + '; '.join(f"`{r['id']}` — {r['title']}" for r in SCHEMA['roles']) + '.', '']
    for role in SCHEMA['survey_roles']:
        members = sorted((r for r in rows if r['survey_role'] == role['id']), key=lambda r: r['project'].lower())
        lines += [f'<a id="{role["id"]}"></a>', '', f"## {role['title']} / {role['title_cn']} ({len(members)})", '',
                  role['description'], '', role['description_cn'], '', '| Project and evidence | Why it is in this survey | Artifact role |', '| --- | --- | --- |']
        for r in members:
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}) | {md_cell(r['relevance_note'])} | {r['catalog_role']} / {r['artifact_type']} |")
        lines.append('')
    return '\n'.join(lines) + '\n'


CASE_QUESTIONS = [
    ('motivation', 'Why build it? / 为什么另建'),
    ('boundary', 'Execution ownership / 重构边界'),
    ('reuse', 'Retained components / 复用什么'),
    ('tradeoff', 'Scope given up / 取舍与兼容性'),
    ('construction', 'Construction process / 怎样构建'),
    ('ai_role', 'AI participation / AI 参与的直接证据'),
    ('cost', 'Disclosed effort / 构建投入'),
    ('validation', 'Validation boundary / 验证覆盖'),
    ('maintenance', 'Evolution evidence / 适配与维护')]


def render_cases(rows: list[dict[str, str]]) -> str:
    by_id = {r['id']: r for r in rows}
    cases = load_cases()
    lines = ['# Core cases: how execution stacks are built / 核心案例', '',
             '> Generated from [cases.json](../catalog/cases.json). Cases connect construction processes to artifacts; they are not additional repository counts.', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Survey library](systems.md) · [Construction comparison](comparison.md) · [Evidence policy](evidence-policy.md)', '',
             'Read motivation → execution ownership → retained components and lost generality → construction → validation and maintenance. A case can be selected without AI attribution. Rebuilding an execution path need not mean writing every dependency from scratch.', '',
             '本页关注“为何重构、重构了多少、怎样构建、是否值得维护”。未知项明确保留；作者披露、源码检查、独立复现和生产使用是不同证据。案例资格不等于证明 AI 降低了总成本。', '',
             'No case performance was independently reproduced here. “Not disclosed” and “not established” describe the reviewed sources, not an assertion that an activity never occurred.', '',
             ' · '.join(f"[{md_cell(c['title'])}](#{c['id']})" for c in cases), '']
    for c in cases:
        lines += [f'<a id="{c["id"]}"></a>', '', f"## {md_cell(c['title'])}", '',
                  '**Related project records:** ' + project_links(c['project_ids'], by_id, '') + '.', '']
        for field, label in CASE_QUESTIONS:
            lines += [f"- **{label}:** {md_cell(c[field])}"]
        lines += ['', '**Sources:** ' + ' · '.join(f'[Source {i}]({url})' for i, url in enumerate(c['evidence_urls'], 1)) + '.', '',
                  f"**Reviewed:** {c['checked_on']}. See the linked project record for mechanism-specific caveats.", '']
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
                      f"[{r['survey_role']}](systems.md#{r['survey_role']}) · `{r['catalog_role']}` · `{r['artifact_type']}` · `{' / '.join(items(r, 'domains'))}` · **{SOURCES[r['source_visibility']]}**", '',
                      f"**Survey relevance:** {md_cell(r['relevance_note'])}", '', md_cell(r['mechanism']), '', f"**Scope:** {md_cell(r['target'])}", '',
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
    lines = ['# Compare construction boundaries / 构建方式对照', '',
             '> Generated from [cases.json](../catalog/cases.json) and [projects.csv](../catalog/projects.csv). No speed, maturity or cost ranking is implied.', '',
             '[Home](../README.md) · [Core case studies](cases.md) · [Survey library](systems.md) · [Evidence policy](evidence-policy.md)', '',
             'Start with what is rebuilt and what effort is disclosed. Read each case for retained components, sacrificed compatibility, AI participation, validation and maintenance. Unknown costs cannot be treated as zero; reported build effort is not a controlled comparison of development methods.', '',
             '先比较执行栈边界和已披露的构建投入，再查机制。是否降低总成本，需要计入验证、集成、适配和维护，并与保留通用引擎的方案比较。', '',
             '| Case | Execution ownership | Construction effort evidence |', '| --- | --- | --- |']
    for c in load_cases():
        lines.append(f"| [{md_cell(c['title'].split(':', 1)[0])}](cases.md#{c['id']}) | {md_cell(c['boundary'])} | {md_cell(c['cost'])} |")
    lines += ['', '## Library facets / 资料库的独立标签', '',
              'The full mechanism-oriented index is retained below. Survey relevance and artifact role answer different questions. Modality refers to inspected scope; semantic labels identify evaluation obligations, not correctness guarantees.', '',
              '<details>', '<summary>Expand all project facets / 展开全部项目标签</summary>', '']
    for f in FAMILIES:
        lines += [f"### {f['title']}", '', '| Project / survey relevance | Artifact role / modality | Semantic considerations |', '| --- | --- | --- |']
        for r in sorted((r for r in rows if r['family'] == f['id']), key=lambda r: r['project'].lower()):
            status = '' if r['source_visibility'] == 'public-code' else f" · **{SOURCES[r['source_visibility']]}**"
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}) · {r['survey_role']}{status} | {r['catalog_role']} / {r['artifact_type']} / {', '.join(items(r, 'domains'))} | {effect_label(r)} |")
        lines.append('')
    lines += ['</details>', '']
    return '\n'.join(lines) + '\n'


def generated_files(rows: list[dict[str, str]]) -> dict[Path, str]:
    outputs = {}
    for name, chinese in [('README.md', False), ('README_CN.md', True)]:
        path = ROOT / name
        outputs[path] = updated_text(path.read_text(encoding='utf-8'), render_overview(rows, chinese))
    outputs[ROOT / 'docs/cases.md'] = render_cases(rows)
    outputs[ROOT / 'docs/systems.md'] = render_systems(rows)
    outputs[ROOT / 'docs/catalog.md'] = render_catalog(rows)
    outputs[ROOT / 'docs/comparison.md'] = render_comparison(rows)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Check all six generated views')
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
    print(f'{len(rows)} entries; six generated views ' + ('in sync' if args.check else 'updated'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
