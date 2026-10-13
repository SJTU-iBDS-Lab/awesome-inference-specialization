"""Reader-oriented homepage layout; catalog mechanisms remain independent facets.

The canonical catalog owns identities, URLs and domain coverage. Bilingual
homepage notes own concise descriptions; this module only controls presentation.
"""
from __future__ import annotations

import html

ENGINE_DOMAINS = [
    ('text', 'Language models', '语言模型'),
    ('image', 'Image generation and processing', '图像生成与处理'),
    ('video', 'Video generation and streaming', '视频生成与流式执行'),
    ('audio', 'Speech and audio', '语音与音频'),
    ('multimodal', 'Multimodal and cross-domain', '多模态与跨领域'),
]
SHORT_DOMAINS = [
    ('text', 'Language', '语言'), ('image', 'Image', '图像'),
    ('video', 'Video', '视频'), ('audio', 'Audio', '音频'),
    ('multimodal', 'Multimodal', '多模态'), ('general', 'General', '通用'),
]
# Primary placement is editorial, not a claim about exhaustive compatibility.
# Other supported domains remain visible as tags and in docs/domains.md.
ENGINE_DOMAIN_OVERRIDES = {
    'cactus': 'multimodal', 'colibri': 'multimodal', 'gufo': 'multimodal',
    'brain': 'multimodal', 'fastflowlm': 'multimodal', 'zllm': 'multimodal',
    'pmetal': 'multimodal', 'tensorrt-edge-llm': 'multimodal',
    'stable-diffusion-cpp': 'image', 'draw-things': 'image',
    'edge-dit': 'image', 'streamdiffusion': 'image', 'saient-quartz': 'image',
    'xdit': 'video', 'lightx2v': 'video', 'telefuser': 'video',
}
STARTER_CASE_IDS = ('vibeqwen', 'splash', 'llamampere', 'nunchaku', 'mirage', 'sol-engine')
STARTER_ROUTES = {
    'vibeqwen': ('Agent-built engine', 'Agent 构建引擎'),
    'splash': ('Native runtime', '原生运行时'),
    'llamampere': ('Deep fork', '深度分叉'),
    'nunchaku': ('Specialized backend', '专用后端'),
    'mirage': ('Compiled execution', '编译生成执行'),
    'sol-engine': ('Video optimization workflow', '视频优化流程'),
}
CONSTRUCTION_GROUPS = [
    ('kernels', 'Operator kernels', '算子内核',
     'Emits or migrates individual accelerator kernels.', '生成或迁移单个加速器算子内核。',
     ('akg-agents', 'atrex-kernel-agent')),
    ('programs', 'Model programs and compiled artifacts', '模型程序与编译产物',
     'Emits composed forward programs, compiled model packages or executable graphs; hosting responsibilities differ.',
     '生成组合前向程序、编译模型包或执行图；模型宿主和服务职责各不相同。',
     ('anemll', 'kernelagent', 'mirage', 'mlc-llm', 'onediff', 'stable-fast')),
    ('stacks', 'Runtime construction and integrated optimization', '运行时构建与集成优化',
     'Builds a server or integrates changes into a model runtime. Kernel generation, configuration search and whole-engine construction are distinct scopes.',
     '构建服务或将优化集成到模型运行时；需区分内核生成、配置搜索与完整引擎构建。',
     ('agentcompile', 'metainfer', 'sol-engine')),
]
HOMEPAGE_VALIDATION = [
    ('numerical', 'Operator / subgraph numerics', '算子／子图数值',
     'Compare reference outputs under explicit shapes, dtypes and tolerances.',
     '在明确形状、精度和容差下比较参考输出。', [
         ('kernelbench', 'KernelBench', 'Reference and evaluator-integrity checks.', '参考计算与评测完整性检查。'),
         ('fastkernels', 'FastKernels', 'Kernel-to-pipeline replacement checks; coverage depends on the task.', '从内核到流水线的替换检查，覆盖取决于任务。'),
         ('atrex-bench', 'Atrex-Bench', 'Output structure, numerical errors and mutation checks.', '输出结构、数值误差和输入改写检查。')]),
    ('model-state', 'Composed model and state', '组合模型与状态',
     'Check the assembled forward program separately from persistent engine state.',
     '区分组合前向程序检查与持久引擎状态验证。', [
         ('kernelagent', 'KernelAgent composition', 'Optional --verify reference self-test of the composed forward program.', '通过可选 --verify 对组合前向程序执行参考自测。')]),
    ('quality', 'Generated-output quality', '生成输出质量',
     'Compare admitted approximations against a specified reference and quality threshold.',
     '针对允许的近似，规定参考配置与质量阈值。', [
         ('sol-engine', 'Sol-Engine LPIPS and visual review', 'Sampled-frame perceptual comparisons and visual checks.', '采样帧感知比较与视觉检查。')]),
    ('service', 'Service and integration', '服务与集成',
     'Exercise startup, requests, responses and the intended candidate.',
     '检查启动、请求、响应及预期候选是否执行。', [
         ('metainfer', 'MetaInfer inference-framework oracle', 'Runs serve.sh and judges configured prompts using an LLM or heuristic fallback.', '运行 serve.sh，以 LLM 或启发式回退判断配置中的提示词。')]),
]
VALIDATION_GAPS = {
    'numerical': ('Finite tested inputs; not automatic coverage of every model, device or persistent state.',
                  '限于已测试输入，不自动覆盖所有模型、设备或持久状态。'),
    'model-state': ('The listed composition check does not cover KV isolation, resets, batching or long trajectories; these need separate tests.',
                    '此处组合检查未覆盖 KV 隔离、重置、批处理或长轨迹，仍需独立测试。'),
    'quality': ('Sampled frames do not fully assess temporal consistency; unequal lengths may compare only a common prefix. Unavailable scoring is not a pass.',
                '采样帧未完整覆盖时间一致性；帧数不同时可能只比较共同前缀。评分不可用不算通过。'),
    'service': ('Plausible responses do not prove tensor parity or concurrency safety; prompt judging is not numerical equivalence.',
                '合理回答不证明张量一致或并发安全；提示词判定不是数值等价检查。'),
}


def cell(value: str) -> str:
    return html.escape(str(value), quote=False).replace('|', '&#124;').replace('\n', ' ').strip()


def primary_domain(row: dict[str, str]) -> str:
    domain = ENGINE_DOMAIN_OVERRIDES.get(row['id'])
    available = set(row['domains'].split(';'))
    if domain is not None:
        if domain != 'multimodal' and domain not in available:
            raise ValueError(f"Homepage domain override is outside catalog scope: {row['id']}")
        return domain
    for candidate in ('text', 'video', 'image', 'audio'):
        if candidate in available:
            return candidate
    if available & {'multimodal', 'general'}:
        return 'multimodal'
    raise ValueError(f"No homepage domain for {row['id']}")


def validate_notes(rows: list[dict[str, str]], notes_en: dict[str, str], notes_cn: dict[str, str]) -> None:
    expected = {r['id'] for r in rows}
    for language, notes in [('English', notes_en), ('Chinese', notes_cn)]:
        if set(notes) != expected:
            missing = sorted(expected - set(notes))
            extra = sorted(set(notes) - expected)
            raise ValueError(f'{language} homepage descriptions: missing={missing}, extra={extra}')
        if any(not isinstance(text, str) or not text.strip() for text in notes.values()):
            raise ValueError(f'{language} homepage descriptions must be nonempty strings')


def render_homepage(rows: list[dict[str, str]], schema: dict, notes_en: dict[str, str],
                    notes_cn: dict[str, str], showcase: list[dict], cases: list[dict],
                    chinese: bool = False) -> str:
    validate_notes(rows, notes_en, notes_cn)
    by_id = {r['id']: r for r in rows}
    by_case = {c['id']: c for c in cases}
    choices = {c['case_id']: c for c in showcase}
    if any(id not in choices or id not in by_case for id in STARTER_CASE_IDS):
        raise ValueError('Homepage starter cases must belong to the canonical showcase and cases')
    select = lambda en, cn: cn if chinese else en
    notes = notes_cn if chinese else notes_en
    engines = [r for r in rows if r['catalog_role'] == 'system']
    group_members = {d: sorted((r for r in engines if primary_domain(r) == d), key=lambda r: r['project'].lower())
                     for d, _, _ in ENGINE_DOMAINS}
    construction_ids = [id for group in CONSTRUCTION_GROUPS for id in group[-1]]
    if set(construction_ids) != {r['id'] for r in rows if r['catalog_role'] == 'construction'} or len(construction_ids) != len(set(construction_ids)):
        raise ValueError('Update construction output groups to cover every construction project exactly once')
    support_ids = [id for g in schema['support_groups'] for id in g['examples']]
    if set(support_ids) != {r['id'] for r in rows if r['catalog_role'] == 'support'} or len(support_ids) != len(set(support_ids)):
        raise ValueError('Support groups must cover every companion resource exactly once')
    allowed_roles = {'system', 'construction', 'validation', 'benchmark', 'support'}
    if any(r['catalog_role'] not in allowed_roles for r in rows):
        raise ValueError('Unsupported homepage role')

    def entry(row: dict[str, str]) -> str:
        domains = set(row['domains'].split(';'))
        tags = ' '.join(f'`{select(en, cn)}`' for id, en, cn in SHORT_DOMAINS if id in domains)
        return (f'- <a id="project-{row["id"]}"></a>**[{cell(row["project"])}]({row["url"]})** — '
                f'{cell(notes[row["id"]])} {tags} '
                f'[{select("Details", "详情")}](docs/catalog.md#{row["id"]})')

    counts = {role: sum(r['catalog_role'] == role for r in rows) for role in allowed_roles}
    lines = [select(
        f'**{len(rows)} projects** · {counts["system"]} engines · {counts["construction"]} construction workflows · {counts["benchmark"]} benchmarks · {counts["support"]} companion resources. All entries remain expanded and link directly upstream.',
        f'**{len(rows)} 个项目** · {counts["system"]} 个引擎 · {counts["construction"]} 个构建流程 · {counts["benchmark"]} 个基准 · {counts["support"]} 项配套资源。全部条目直接展开，项目名直达上游。'), '',
        '**' + select('Browse engines:', '按领域找引擎：') + '** ' + ' · '.join(
            f'[{select(en, cn)}](#homepage-system-{id})' for id, en, cn in ENGINE_DOMAINS), '',
        '<a id="featured-reading"></a>', '', select('## Start here', '## 从这里开始'), '',
        select('Six different ways to obtain control over inference execution. These are reading routes, not performance or maturity rankings.',
               '六种获得推理执行控制权的方式；这是阅读入口，不是性能或成熟度排名。'), '',
        select('| Approach | Case | What to look for |', '| 构建形态 | 案例 | 阅读重点 |'), '| --- | --- | --- |']
    for id in STARTER_CASE_IDS:
        item, case = choices[id], by_case[id]
        name = cell(case['title'].split(':', 1)[0])
        lines.append(f'| {select(*STARTER_ROUTES[id])} | [{name}](docs/cases.md#{id}) | {cell(item["why_cn" if chinese else "why"])} |')
    lines += ['', select(f'[Compare all {len(showcase)} representative cases](docs/representative-comparison.md) · [Cross-case synthesis](docs/synthesis.md)',
                         f'[{len(showcase)} 个代表案例速查](docs/representative-comparison.md#chinese) · [跨案例综合](docs/synthesis.md)'), '',
              select('## Contents', '## 目录'), '']
    role_titles = [('system', 'Inference engines', '推理引擎'), ('construction', 'Build and optimize', '构建与优化'),
                   ('validation', 'Validation: coverage and gaps', '验证：覆盖与缺口'), ('benchmark', 'Benchmarks', '评测基准'),
                   ('support', 'Companion resources', '配套资源')]
    for id, en, cn in role_titles:
        lines.append(f'- [{select(en, cn)}](#homepage-{id})')
    lines += [select('- [Further reading](#further-reading)', '- [深入阅读](#further-reading)'), '',
              '<a id="homepage-system"></a>', '', select('## Inference engines', '## 推理引擎'), '',
              select('Browse by the main task; short tags preserve additional domains. Native runtimes, deep forks, specialized backends and relevant precedents are included. Mechanisms are secondary facets, not mutually exclusive engine classes.',
                     '按主要任务查找，短标签保留其他模型领域。覆盖原生运行时、深度分叉、专用后端与相关先行系统；机制是辅助标签，不再作为互斥的引擎分类。'), '',
              select('[Relevance and execution boundaries](docs/systems.md#system) · [All overlapping domains](docs/domains.md)',
                     '[相关性与执行边界](docs/systems.md#system) · [跨领域完整索引](docs/domains.md)'), '',
              select('**By mechanism:** ', '**按机制检索：** ') + ' · '.join(
                  f'<a id="homepage-system-{f["id"]}"></a>[{f["title_cn" if chinese else "title"]}](docs/catalog.md#{f["id"]})'
                  for f in schema['families'] if f['id'] != 'construction'), '']
    for domain, en, cn in ENGINE_DOMAINS:
        members = group_members[domain]
        lines += [f'<a id="homepage-system-{domain}"></a>', '', f'### {select(en, cn)} ({len(members)})', '']
        lines.extend(entry(row) for row in members)
        lines.append('')
    lines += ['<a id="homepage-construction"></a>', '', select('## Build and optimize', '## 构建与优化'), '',
              select('Group workflows by what they produce. Compiler and agent involvement describe the method; they do not turn a generated kernel into a complete engine.',
                     '按产物区分构建流程。编译器或 Agent 描述构建方法；生成内核不等于构建了完整引擎。'), '',
              select('[Construction boundaries and sources](docs/systems.md#construction)', '[构建边界与来源](docs/systems.md#construction)'), '',
              '<a id="homepage-construction-execution"></a>', '<a id="homepage-construction-construction"></a>', '']
    for id, en, cn, explanation, explanation_cn, ids in CONSTRUCTION_GROUPS:
        lines += [f'<a id="homepage-construction-{id}"></a>', '', f'### {select(en, cn)} ({len(ids)})', '',
                  select(explanation, explanation_cn), '']
        lines.extend(entry(by_id[id]) for id in sorted(ids, key=lambda id: by_id[id]['project'].lower()))
        lines.append('')
    lines += ['<a id="homepage-validation"></a>', '', select('## Validation: coverage and gaps', '## 验证：覆盖与缺口'), '',
              select('Four contracts, with six source-inspected method entries. Checks embedded in a project are linked below without counting another repository. These methods were not executed here.',
                     '四类契约、六个已做来源检查的方法入口。内嵌检查直接关联所属项目，不重复计数；本仓库未执行这些验证。'), '',
              select('| Object | Available methods and observed coverage | Remaining gap |', '| 验证对象 | 已有方法与实际覆盖 | 主要缺口 |'),
              '| --- | --- | --- |']
    for id, en, cn, explanation, explanation_cn, methods in HOMEPAGE_VALIDATION:
        method_text = '<br>'.join(f'[{label}](#project-{project_id}): {cell(select(note, note_cn))}'
                                  for project_id, label, note, note_cn in methods)
        object_text = f'<a id="homepage-validation-{id}"></a>[{select(en, cn)}](docs/validation.md#{id})'
        lines.append(f'| {object_text} | {cell(select(explanation, explanation_cn))}<br>{method_text} | {cell(select(*VALIDATION_GAPS[id]))} |')
    lines += ['', select('Validation cost includes reference execution, candidate compilation, device/judge calls and human review. Compare costs under the same acceptance contract; a weaker check is not an equivalent efficiency improvement.',
                         '验证成本包括参考运行、候选编译、设备与判定器调用和人工复核；应在相同验收契约下比较成本，削弱检查不等于等效提速。'), '',
              select('[Implementation evidence and validation design](docs/validation.md)', '[实现证据与验证设计](docs/validation.md)'), '']
    lines.extend(entry(r) for r in rows if r['catalog_role'] == 'validation')
    lines += ['<a id="homepage-benchmark"></a>', '', select('## Benchmarks', '## 评测基准'), '',
              select('Tasks and comparison protocols complement the checks above. Match model, device, precision, workload, state and quality before comparing results.',
                     '任务与比较协议补充上方验证方法。比较结果前应匹配模型、设备、精度、负载、状态和质量要求。'), '']
    lines.extend(entry(r) for r in sorted(rows, key=lambda r: r['project'].lower()) if r['catalog_role'] == 'benchmark')
    lines += ['', select('[Benchmark scope and comparison protocols](docs/benchmarks.md)', '[基准范围与比较协议](docs/benchmarks.md)'), '',
              '<a id="homepage-support"></a>', '', select('## Companion resources', '## 配套资源'), '',
              select('Selected resources with a concrete construction, reuse or comparison relationship to an included system—not a general GPU-tool directory.',
                     '仅收录与已列系统存在具体构建、复用或比较关系的资源，而非通用 GPU 工具大全。'), '']
    for group in schema['support_groups']:
        lines += [f'<a id="homepage-support-{group["id"]}"></a>', '', f'### {group["title_cn" if chinese else "title"]}', '']
        lines.extend(entry(by_id[id]) for id in group['examples'])
        lines += ['', f'[{select("Relationships and sources", "复用关系与来源")}](docs/resources.md#{group["id"]})', '']
    lines += [select('**Embedded knowledge:** Atrex GPU Wiki connects optimization traces and retrieved experience to later construction attempts; it remains part of Atrex. [How it is used](docs/resources.md#embedded-knowledge).',
                     '**内嵌知识：**Atrex GPU Wiki 将优化轨迹与检索经验用于后续构建，仍属于 Atrex，不另计项目。[使用方式](docs/resources.md#embedded-knowledge)。'), '',
              '<a id="further-reading"></a>', '', select('## Further reading', '## 深入阅读'), '',
              select('Additional cases extend the six starting routes into hardware constraints, memory movement, audio, model porting and action inference.',
                     '以下案例补充设备约束、内存搬移、音频、模型移植与动作推理等观察。'), '',
              select('| Case | Reading benefit |', '| 案例 | 阅读收益 |'), '| --- | --- |']
    for item in showcase:
        id = item['case_id']
        if id in STARTER_CASE_IDS:
            continue
        name = cell(by_case[id]['title'].split(':', 1)[0])
        lines.append(f'| [{name}](docs/cases.md#{id}) | {cell(item["why_cn" if chinese else "why"])} |')
    lines += ['', select('[All cases](docs/cases.md) · [Full comparison](docs/comparison.md) · [Mechanism index](docs/catalog.md) · [Research questions](docs/research-agenda.md) · [Latest updates](docs/updates.md)',
                         '[全部案例](docs/cases.md) · [完整对照](docs/comparison.md) · [机制索引](docs/catalog.md) · [研究问题](docs/research-agenda.md) · [最近更新](docs/updates.md)')]
    return '\n'.join(lines)
