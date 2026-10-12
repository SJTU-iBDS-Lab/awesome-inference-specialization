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
SHOWCASE_PATH = ROOT / 'catalog' / 'showcase.json'
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


def load_showcase(path: Path = SHOWCASE_PATH) -> list[dict[str, str]]:
    return json.loads(path.read_text(encoding='utf-8'))


def items(row: dict[str, str], field: str) -> list[str]:
    return row[field].split(';')


def effect_label(row: dict[str, str]) -> str:
    return ', '.join(EFFECTS[x] for x in items(row, 'semantic_effect'))


def project_links(ids: list[str], by_id: dict[str, dict[str, str]], prefix: str = 'docs/') -> str:
    return ', '.join(f"[{md_cell(by_id[id]['project'])}]({prefix}catalog.md#{id})" for id in ids)


def render_overview(rows: list[dict[str, str]], chinese: bool = False) -> str:
    cases = {c['id']: c for c in load_cases()}
    showcase = load_showcase()
    count = len(showcase)
    key = 'why_cn' if chinese else 'why'
    lines = [f'### {count} 个起点：读完能学到什么' if chinese else f'### {count} starting points: what you can learn', '',
             '按执行控制、复用方式、构建路径和验证边界选例，覆盖引擎、编译与 Agent 工作流。这是阅读路线，不按星标、速度或成熟度排名。' if chinese else
             'Chosen to contrast execution control, reuse, construction routes and validation across engines, compilation and agent workflows. This is a reading route, not a star, speed or maturity ranking.', '',
             '| 案例 | 阅读收益 |' if chinese else '| Case | Read it to understand |', '| --- | --- |']
    for item in showcase:
        c = cases[item['case_id']]
        lines.append(f"| [{md_cell(c['title'].split(':', 1)[0])}](docs/cases.md#{c['id']}) | {md_cell(item[key])} |")
    lines += ['', f'[{count} 案例速查：模型／设备、产物、复用与验证](docs/representative-comparison.md#chinese) · [完整对照](docs/comparison.md) · [全部案例](docs/cases.md)' if chinese else
              f'[{count}-case matrix: model/device, artifact, reuse and checks](docs/representative-comparison.md) · [Full comparison](docs/comparison.md) · [All cases](docs/cases.md)', '',
              '### 按任务继续找' if chinese else '### Continue by task', '',
              '- **找引擎：**[全部引擎](docs/systems.md#system)，再按下方模型领域筛选。' if chinese else
              '- **Find an engine:** open [all engines](docs/systems.md#system), then use the model-domain links below.',
              '- **构建或优化：**[工作流索引](docs/systems.md#construction)区分内核、模型前向程序和完整服务；[内嵌构建知识](docs/resources.md#embedded-knowledge)连接优化经验与后续尝试。' if chinese else
              '- **Build or optimize:** the [workflow index](docs/systems.md#construction) distinguishes kernels, model forward programs and full services; [embedded knowledge](docs/resources.md#embedded-knowledge) connects optimization experience to later attempts.',
              '- **验证结果：**[数值](docs/validation.md#numerical)、[模型／状态](docs/validation.md#model-state)、[生成质量](docs/validation.md#quality)、[服务行为](docs/validation.md#service)是不同契约；[基准](docs/benchmarks.md)提供任务和比较协议。' if chinese else
              '- **Validate results:** [numerics](docs/validation.md#numerical), [model/state](docs/validation.md#model-state), [output quality](docs/validation.md#quality) and [service behavior](docs/validation.md#service) are different contracts; [benchmarks](docs/benchmarks.md) supply tasks and comparison protocols.',
              '- **找配套工具：**[性能诊断](docs/resources.md#diagnostics)、[构建知识](docs/resources.md#knowledge)和[复用组件](docs/resources.md#components)。' if chinese else
              '- **Find supporting tools:** [diagnostics](docs/resources.md#diagnostics), [construction knowledge](docs/resources.md#knowledge) and [reusable components](docs/resources.md#components).', '',
              domain_links(chinese), '',
              f'完整资料：{len(rows)} 个项目、{len(cases)} 个构建案例。按[执行机制](docs/catalog.md)查找，或读[跨案例结论](docs/synthesis.md)。' if chinese else
              f'Full collection: {len(rows)} projects, {len(cases)} construction cases. Browse [execution mechanisms](docs/catalog.md) or read the [cross-case synthesis](docs/synthesis.md).']
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
             '[Home](../README.md) · [Representative quick comparison](representative-comparison.md) · [Cross-case synthesis](synthesis.md) · [Core case studies](cases.md) · [Survey library](systems.md) · [Evidence policy](evidence-policy.md)', '',
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


def render_representative_comparison(rows: list[dict[str, str]]) -> str:
    by_id = {r['id']: r for r in rows}
    cases = {c['id']: c for c in load_cases()}
    showcase = load_showcase()
    count = len(showcase)
    lines = ['# Representative comparison / 代表案例速查', '',
             '> Generated from [showcase.json](../catalog/showcase.json), [cases.json](../catalog/cases.json) and [projects.csv](../catalog/projects.csv).', '',
             '[Home](../README.md) · [中文表格](#chinese) · [Full comparison](comparison.md) · [Case synthesis](synthesis.md) · [Validation guide](validation.md)', '',
             f'{count} deliberately different reading examples: native runtimes, a deep fork, memory/representation-driven execution, compilation, agent workflows and model ports. Selection balances construction and validation lessons across model domains; it is not a popularity, performance or maturity ranking.', '',
             'Scope means the reviewed configuration, not a complete current support list. Where a record does not enumerate model names or devices, the table says so rather than guessing. Open the case for the selection lesson, construction/AI evidence, effort and maintenance, and the source for exact version limits.', '',
             'These are source-review summaries, not reproduced benchmarks. Unknown lifecycle costs remain in the full cases; absence of disclosure is not zero cost. [Evidence policy](evidence-policy.md).', '']
    for chinese in (False, True):
        if chinese:
            lines += ['<a id="chinese"></a>', '', '## 中文速查', '',
                      f'这 {count} 个例子覆盖原生运行时、深度分叉、内存与表示驱动的执行、编译、Agent 工作流和模型移植。选例依据是构建与验证的阅读价值，不是星标、速度或成熟度。范围只代表已检查的配置，不是完整支持列表；记录未列明的模型／设备不会补猜。全部记录均未在本仓库独立复现性能，完整案例保留投入与维护的未知项。', '']
        lines += ['| 案例／来源 | 已查模型与设备 | 产物与执行控制 | 保留的组件 | 验证边界 |' if chinese else
                  '| Case / source | Reviewed model & device | Artifact & execution control | Retained components | Validation boundary |',
                  '| --- | --- | --- | --- | --- |']
        for item in showcase:
            c, r = cases[item['case_id']], by_id[item['project_id']]
            label = md_cell(c['title'].split(':', 1)[0])
            links = f"[{label}](cases.md#{c['id']}) · [upstream]({r['url']}) · [source]({c['evidence_urls'][0]})"
            suffix = '_cn' if chinese else ''
            cells = [md_cell(item[field + suffix]) for field in ('scope', 'boundary', 'reuse', 'validation')]
            lines.append('| ' + ' | '.join([links, *cells]) + ' |')
        lines.append('')
    lines += ['## Why these cases? / 为什么选这些案例', '',
              '| Case / 案例 | Reading benefit / 阅读收益 |', '| --- | --- |']
    for item in showcase:
        c = cases[item['case_id']]
        lines.append(f"| [{md_cell(c['title'].split(':', 1)[0])}](cases.md#{c['id']}) | {md_cell(item['why'])} / {md_cell(item['why_cn'])} |")
    lines += ['', 'For all cases and disclosed construction effort, use the [full comparison](comparison.md). For references, trade-offs and maintenance details, use the [case collection](cases.md). / 全量边界与投入见完整对照，具体来源、取舍及维护见案例全文。', '']
    return '\n'.join(lines)


def generated_files(rows: list[dict[str, str]]) -> dict[Path, str]:
    outputs = {}
    for name, chinese in [('README.md', False), ('README_CN.md', True)]:
        path = ROOT / name
        outputs[path] = updated_text(path.read_text(encoding='utf-8'), render_overview(rows, chinese))
    outputs[ROOT / 'docs/cases.md'] = render_cases(rows)
    outputs[ROOT / 'docs/systems.md'] = render_systems(rows)
    outputs[ROOT / 'docs/catalog.md'] = render_catalog(rows)
    outputs[ROOT / 'docs/comparison.md'] = render_comparison(rows)
    outputs[ROOT / 'docs/representative-comparison.md'] = render_representative_comparison(rows)
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
    outputs = generated_files(rows)
    for path, content in outputs.items():
        if not path.exists() or path.read_text(encoding='utf-8') != content:
            changed.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.write_text(content, encoding='utf-8')
    if args.check and changed:
        print('Generated views are stale: ' + ', '.join(changed), file=sys.stderr)
        return 1
    print(f'{len(rows)} entries; {len(outputs)} generated views ' + ('in sync' if args.check else 'updated'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
