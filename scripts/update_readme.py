#!/usr/bin/env python3
"""Generate bilingual overviews and detailed views from the canonical catalog."""
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
DOMAINS = [('multimodal', 'Multimodal understanding & interaction', '多模态理解与交互'),
           ('image', 'Image generation & processing', '图像生成与处理'),
           ('video', 'Video generation & processing', '视频生成与处理'),
           ('audio', 'Speech & audio', '语音与音频'),
           ('text', 'Language models', '语言模型'),
           ('general', 'Cross-domain infrastructure', '跨模态基础设施')]


def domain_links(chinese: bool = False, prefix: str = 'docs/') -> str:
    return ' · '.join(f'[{cn if chinese else en}]({prefix}domains.md#{id})'
                      for id, en, cn in DOMAINS)


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
    by_id = {r['id']: r for r in rows}
    key = 'title_cn' if chinese else 'title'
    lines = ['### 专用推理引擎' if chinese else '### Specialized inference engines', '',
             '从执行栈重建方式入手，再按模型、设备和机制筛选。下面是阅读入口，完整引擎索引和案例分析另页列出。' if chinese else
             'Start with how execution is rebuilt, then filter by model, device and mechanism. These are entry points into the full engine index and case analyses.', '',
             '| 执行栈阅读路线 | 代表案例 |' if chinese else '| Execution-stack reading route | Selected cases |', '| --- | --- |']
    for group in SCHEMA['case_groups'][1:]:
        selected = group.get('featured', group['examples'][:3])
        links = ' · '.join(f"[{md_cell(cases[id]['title'].split(':', 1)[0])}](docs/cases.md#{id})" for id in selected)
        lines.append(f"| {group[key]} | {links} |")
    lines += ['', '[全部引擎](docs/systems.md#system) · [全部构建案例](docs/cases.md) · [重构边界对照](docs/comparison.md)' if chinese else
              '[All engines](docs/systems.md#system) · [All construction cases](docs/cases.md) · [Compare reconstruction boundaries](docs/comparison.md)', '',
              domain_links(chinese), '',
              '### 构建与优化方案' if chinese else '### Construction and optimization', '',
              '把构建流程与生成产物连起来。内核、模型前向程序和完整服务是不同的产出范围。' if chinese else
              'Connect each workflow to its output. A kernel, model forward program and complete serving stack have different scopes.', '',
              '| 方案 | 实际产出范围 |' if chinese else '| Workflow | Output scope |', '| --- | --- |']
    for item in SCHEMA['homepage_construction']:
        row = by_id[item['id']]
        lines.append(f"| [{md_cell(row['project'])}](docs/catalog.md#{row['id']}) | {item['output_cn' if chinese else 'output']} |")
    lines += ['', '[全部构建方案](docs/systems.md#construction) · [MetaInfer → VibeQwen 案例链](docs/cases.md#vibeqwen)' if chinese else
              '[All construction workflows](docs/systems.md#construction) · [MetaInfer → VibeQwen case chain](docs/cases.md#vibeqwen)', '',
              '### 正确性与质量验证方案' if chinese else '### Correctness and quality validation', '',
              '| 检验对象 | 方案入口 |' if chinese else '| Contract to check | Method entry point |', '| --- | --- |',
              '| 数值与算子组合 | [参考实现差分、组合后复检](docs/validation.md#numerical) |' if chinese else
              '| Numerics and operator composition | [Reference comparisons and recomposition checks](docs/validation.md#numerical) |',
              '| 模型组合与状态覆盖 | [模型组合检查与状态覆盖要求](docs/validation.md#model-state) |' if chinese else
              '| Model composition and state coverage | [Composed-forward checks and state coverage](docs/validation.md#model-state) |',
              '| 图像／视频质量 | [感知质量与误差约束](docs/validation.md#quality) |' if chinese else
              '| Image / video quality | [Perceptual quality and error constraints](docs/validation.md#quality) |',
              '| 服务接口与功能 | [接口测试、判定器及其覆盖边界](docs/validation.md#service) |' if chinese else
              '| Service interfaces and function | [Interface tests, judges and coverage limits](docs/validation.md#service) |', '',
              '验证器可以内嵌在引擎或构建框架中；这里索引方案，不重复计算仓库。数值检查、感知质量和功能测试不能相互替代。' if chinese else
              'A validator can live inside an engine or construction framework; methods are indexed without duplicating repositories. Numerical, perceptual and functional checks are distinct contracts.', '',
              '### 评测基准与任务集' if chinese else '### Benchmarks and task suites', '',
              '| 基准 | 比较的问题 |' if chinese else '| Benchmark | Comparison question |', '| --- | --- |']
    for item in SCHEMA['benchmark_entries']:
        row = by_id[item['id']]
        lines.append(f"| [{md_cell(row['project'])}](docs/benchmarks.md#{row['id']}) | {item['question_cn' if chinese else 'question']} |")
    lines += ['', '基准提供任务、参考程序和比较协议；通过算子评测不等于完成整个引擎的验收。[查看评测范围与限制](docs/benchmarks.md)。' if chinese else
              'Benchmarks supply tasks, references and comparison protocols. Passing operator tasks does not validate a complete engine. [Read evaluation scopes and limits](docs/benchmarks.md).', '',
              '### 配套资源' if chinese else '### Companion resources', '',
              '| 用途 | 精选入口 |' if chinese else '| Purpose | Selected resources |', '| --- | --- |']
    for group in SCHEMA['support_groups']:
        links = project_links(group['examples'][:4], by_id)
        lines.append(f"| [{group[key]}](docs/resources.md#{group['id']}) | {links} |")
    lines += ['', '[Atrex GPU Wiki：优化轨迹 → 可复用经验](docs/resources.md#embedded-knowledge)。配套资源必须说明服务于哪个构建、验证或比较过程。' if chinese else
              '[Atrex GPU Wiki: optimization traces → reusable experience](docs/resources.md#embedded-knowledge). Each companion resource must identify the construction, validation or comparison it supports.', '',
              f'当前目录：{len(rows)} 个项目、{len(cases)} 个构建案例。按[项目角色](docs/systems.md)、[执行机制](docs/catalog.md)或[模型领域](docs/domains.md)继续查找。' if chinese else
              f'Current collection: {len(rows)} projects and {len(cases)} construction cases. Browse by [project role](docs/systems.md), [execution mechanism](docs/catalog.md) or [model domain](docs/domains.md).']
    return '\n'.join(lines)


def render_systems(rows: list[dict[str, str]]) -> str:
    lines = ['# Project roles / 项目角色索引', '',
             '> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Cases](cases.md) · [Validation](validation.md) · [Benchmarks](benchmarks.md) · [Resources](resources.md) · [Model domains](domains.md)', '',
             'Browse engines, construction workflows and validation first; benchmarks have a separate entry, while diagnostics, knowledge and selected reusable infrastructure are companion resources. Each repository appears once under its primary role.', '',
             '先看引擎、构建与验证；评测单列，性能诊断、知识和精选基础设施作为配套。同一仓库按主要作用计一次，内部验证或知识模块另有方法入口。', '',
             ' · '.join(f"[{role['title_cn']} / {role['title']}](#{role['id']})" for role in SCHEMA['roles']), '',
             '## Relevance labels / 相关性标签', '']
    for role in SCHEMA['survey_roles']:
        lines += [f'<a id="{role["id"]}"></a>', '', f"**{role['id']} — {role['title_cn']} / {role['title']}**: {role['description']}", '']
    for role in SCHEMA['roles']:
        members = sorted((r for r in rows if r['catalog_role'] == role['id']), key=lambda r: (r['survey_role'] != 'core', r['project'].lower()))
        lines += [f'<a id="{role["id"]}"></a>', '', f"## {role['title']} / {role['title_cn']}", '', role['description'], '', role['description_cn'], '']
        if role['id'] == 'validation':
            lines += ['[Validation methods and coverage / 验证方案及覆盖边界](validation.md). Embedded methods are not counted as separate projects. / 内嵌方案不另计项目。', '']
        if not members:
            continue
        lines += [f'{len(members)} projects / 项目', '', '| Project and evidence | Why it belongs | Relevance / artifact |', '| --- | --- | --- |']
        for r in members:
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}) | {md_cell(r['relevance_note'])} | {r['survey_role']} / {r['artifact_type']} |")
        lines.append('')
    return '\n'.join(lines) + '\n'


def render_benchmarks(rows: list[dict[str, str]]) -> str:
    by_id = {r['id']: r for r in rows}
    lines = ['# Benchmarks and task suites / 评测基准与任务集', '',
             '> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Validation methods](validation.md) · [Construction workflows](systems.md#construction)', '',
             'A benchmark defines tasks, executable references, inputs and a comparison protocol. A validation method checks a contract; one benchmark may incorporate several methods. Keep these roles distinct even when both live in the same project.', '',
             '评测基准规定任务、参考程序、输入和比较协议；验证方案判断某项契约是否满足。包含数值检查的基准仍按主要用途列在这里，不重复计数。', '']
    for item in SCHEMA['benchmark_entries']:
        r = by_id[item['id']]
        lines += [f'<a id="{r["id"]}"></a>', '', f"## {md_cell(r['project'])}", '',
                  f"**Scope / 范围:** {item['scope']} / {item['scope_cn']}", '',
                  f"**Question / 比较问题:** {item['question']} / {item['question_cn']}", '',
                  md_cell(r['mechanism']), '', f"**Limits / 边界:** {md_cell(r['caveat'])}", '',
                  f"[Project record and inspected sources / 项目记录与已核来源](catalog.md#{r['id']}) · [Upstream / 上游]({r['url']})", '']
    lines += ['## What a complete-engine comparison still needs / 完整引擎还需要比较什么', '',
              'Record the model/checkpoint, device, precision, input distribution, state/cache conditions, concurrency, software revisions and quality criterion. Measure end-to-end latency/throughput and memory under the same workload; disclose fallback and unsupported cases.', '',
              'The listed suites do not by themselves establish the cost or reliability of constructing an entire engine. Construction comparisons also need human effort, agent/tool/GPU budgets, failed attempts, validation and integration effort, plus adaptation and maintenance over a stated horizon.', '',
              '上述基准不能单独证明整个引擎的构建成本或可靠性。构建方式的比较还须记录人工投入、Agent／工具／GPU 预算、失败尝试、验证集成成本与后续维护。', '']
    return '\n'.join(lines) + '\n'


def render_resources(rows: list[dict[str, str]]) -> str:
    by_id = {r['id']: r for r in rows}
    lines = ['# Companion resources / 配套资源', '',
             '> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Construction](systems.md#construction) · [Validation](validation.md) · [Benchmarks](benchmarks.md)', '',
             'Resources belong here through a concrete connection to building, checking or comparing an included execution stack. This is a selected dependency and knowledge map, not a general GPU-tool directory.', '',
             '只收录与执行栈构建、验证或比较有具体联系的资源。性能诊断和构建知识服务于构建流程，通用组件须写明复用关系。', '']
    for group in SCHEMA['support_groups']:
        lines += [f'<a id="{group["id"]}"></a>', '', f"## {group['title']} / {group['title_cn']}", '', group['description'], '', group['description_cn'], '',
                  '| Resource | Concrete role in this collection |', '| --- | --- |']
        for id in group['examples']:
            r = by_id[id]
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{id}) | {md_cell(r['relevance_note'])} |")
        lines.append('')
    lines += ['<a id="embedded-knowledge"></a>', '', '## Knowledge inside a construction workflow / 构建流程中的知识模块', '',
              'The [Atrex Kernel Agent](catalog.md#atrex-kernel-agent) includes [GPU Wiki](https://github.com/alibaba/atrex-kernel-agent/blob/main/gpu-wiki/README.md): optimization traces and agent sessions feed candidate knowledge, provenance/scope checks gate admission, and later optimization episodes retrieve it. It remains part of the parent project rather than a second repository record.', '',
              'Atrex 的 GPU Wiki 把优化轨迹和 Agent 会话转成候选知识，检查来源与适用范围后再供后续优化检索；它属于构建框架内部模块，不单独增加仓库数量。公开工作流不等于已经证明总开发成本下降。', '',
              'The [ANE field guide](catalog.md#ane-field-guide) links hardware experiments to [ane.cpp](catalog.md#ane-cpp). Read kept and discarded findings together and retain the tested hardware boundary.', '']
    return '\n'.join(lines) + '\n'


def render_domains(rows: list[dict[str, str]]) -> str:
    lines = ['# Browse by model domain / 按模型领域查找', '',
             '> Generated from [projects.csv](../catalog/projects.csv). Domain labels overlap; counts below must not be summed as unique projects.', '',
             '[Home](../README.md) · [中文首页](../README_CN.md) · [Core cases](cases.md) · [Survey roles](systems.md) · [Execution mechanisms](catalog.md)', '',
             'Use these facets to find relevant workloads, then inspect what the system actually rebuilds. Image/video processing includes generation, restoration and perception; the row describes which task is implemented. A multimodal label does not mean every input/output combination is supported.', '',
             '模态标签可重叠，数量不能相加。图像和视频包含生成、修复与感知，具体能力以条目为准；多模态标签不表示支持所有输入输出组合。先列核心与相邻系统，再折叠共享基础。', '',
             domain_links(prefix=''), '']
    for id, en, cn in DOMAINS:
        members = [r for r in rows if id in items(r, 'domains')]
        systems = sorted((r for r in members if r['survey_role'] != 'foundation'),
                         key=lambda r: (r['survey_role'] != 'core', r['project'].lower()))
        foundations = sorted((r for r in members if r['survey_role'] == 'foundation'), key=lambda r: r['project'].lower())
        lines += [f'<a id="{id}"></a>', '', f'## {en} / {cn}', '',
                  f'{len(systems)} core/adjacent entries; {len(foundations)} shared foundations. Counts reflect reviewed scope, not identical capability or maturity.', '',
                  '| Project | Survey role | Inspected execution scope |', '| --- | --- | --- |']
        for r in systems:
            lines.append(f"| [{md_cell(r['project'])}](catalog.md#{r['id']}) | {r['survey_role']} | {md_cell(r['target'])} |")
        if foundations:
            lines += ['', '<details>', '<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>', '',
                      ' · '.join(f"[{md_cell(r['project'])}](catalog.md#{r['id']})" for r in foundations), '', '</details>']
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
             'The complete reading routes below expand the homepage selections. / 以下阅读路线展开首页精选，覆盖全部构建案例。', '']
    by_case = {c['id']: c for c in cases}
    for group in SCHEMA['case_groups']:
        lines += [f"### {group['title']} / {group['title_cn']}", '',
                  ' · '.join(f"[{md_cell(by_case[id]['title'].split(':', 1)[0])}](#{id})" for id in group['examples']), '']
    for id in [id for group in SCHEMA['case_groups'] for id in group['examples']]:
        c = by_case[id]
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
    outputs[ROOT / 'docs/domains.md'] = render_domains(rows)
    outputs[ROOT / 'docs/benchmarks.md'] = render_benchmarks(rows)
    outputs[ROOT / 'docs/resources.md'] = render_resources(rows)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Check all generated views')
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
    print(f'{len(rows)} entries; nine generated views ' + ('in sync' if args.check else 'updated'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
