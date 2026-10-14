"""Apply four source-reviewed additions to the pinned 122-record catalog.

This one-off helper belongs only to the review-control branch. It changes
catalog content and existing group membership, never workflows or permissions.
"""
from pathlib import Path
import csv
import io
import json

DATE = '2026-10-14'
V = 'https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf'
A = 'https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34'
vp = 'https://arxiv.org/html/2605.06068v1'
ap = 'https://arxiv.org/html/2606.09682v1'
fp = 'https://arxiv.org/html/2609.12379v1'
ib = 'https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/'
iu = 'https://blog.cloudflare.com/high-performance-llms/'
kb = 'https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/'
kp = 'https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/'
hz = 'https://hazyresearch.stanford.edu/blog/2026-08-05-retire-the-abstractions'
vb = 'https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/'
entries = []


def add(id, project, role, family, domains, artifact, constraints, mechanisms,
        target, mechanism, semantics, visibility, ai, url, evidence, relevance,
        caveat, case_id, case_title, summary_cn, case_fields, en, cn):
    row = dict(id=id, project=project, survey_role='core', relevance_note=relevance,
               catalog_role=role, family=family, domains=domains,
               artifact_type=artifact, constraints=constraints, mechanisms=mechanisms,
               target=target, mechanism=mechanism, semantic_effect=semantics,
               source_visibility=visibility, ai_involvement=ai, url=url,
               evidence_urls=';'.join(evidence), caveat=caveat,
               checked_on=DATE, discovery='keyword')
    case = dict(id=case_id, title=case_title, project_ids=[id], summary=relevance,
                summary_cn=summary_cn, **case_fields, evidence_urls=evidence,
                checked_on=DATE)
    assert len(en.split()) <= 60
    assert len(case_fields) == 9
    entries.append(dict(row=row, case=case, en=en, cn=cn))


add('vibesys', 'VibeServe / VibeSys', 'construction', 'construction',
    'text;audio;multimodal', 'generator',
    'model;hardware;workload;validation-contract',
    'agent-generation;design-search;profile-feedback;evaluator-isolation;artifact-provenance',
    'The VibeServe initiative studies target-specific language serving, streaming ASR, constrained output, multimodal workloads and Apple Silicon. The current VibeSys repository also serves non-inference domains, which are outside this record.',
    'Separates design search from implementation and target-specific measurement; durable history carries hypotheses while framework-owned evaluation identities and candidate isolation connect code changes to reviewed results.',
    'tool-dependent', 'public-code', 'intrinsic', 'https://github.com/uw-syfi/vibesys',
    [vp, vb, f'{V}/README.md', f'{V}/src/vibesys/core_wiring.py'],
    'Connects generation-time model/hardware/workload specialization to a concrete serving-system initiative; the broader generator and its scenario-specific outputs are distinct artifacts.',
    'The May 2026 VibeServe paper and the October-reviewed VibeSys implementation are not identical revisions. Results concern selected scenarios and declared contracts, not arbitrary serving workloads or proven lifecycle savings. Evaluation wiring was source-inspected; no agent campaign or generated engine was executed.',
    'vibeserve', 'VibeServe / VibeSys: generation-time serving specialization',
    '按模型、硬件和负载构建专用服务栈；区分 VibeServe 论文中的产物与现行 VibeSys 通用构建框架，非推理任务不在本条范围。',
    dict(motivation='Explore whether per-target serving implementations can exploit opportunities outside a shared runtime, rather than only replacing individual operators.',
         boundary='The artifact is a construction framework whose VibeServe initiative produces target-specific serving stacks. It is not itself one universal inference runtime.',
         reuse='The documented workflow reuses serving knowledge, profiling tools, coding agents and existing model/kernel facilities where appropriate; generated outputs must disclose their own dependencies.',
         tradeoff='Each candidate is qualified against its scenario and evaluation contract. The broad current framework also includes non-inference tasks; that breadth is not inferred coverage of generated serving systems.',
         construction='The paper separates outer design search and inner implementation/evaluation. The inspected current code stores evaluator, workload and environment identities with an evaluation recipe, and rejects parallel candidate modes without suitable isolation.',
         ai_role='Coding agents participate explicitly. Humans supply objectives, domain knowledge and evaluation definitions; current framework-side measurement is distinct from an agent claiming a pass.',
         cost='This review does not establish a comparable lifecycle cost. Any reported campaign budget must be attached to its paper scenario and separated from validation, integration and subsequent maintenance.',
         validation='Inspected the README and host evaluation wiring, alongside the paper and lab report. Contract-specific tests and a read-only reviewer are not universal numerical or service-correctness proofs. No campaign was reproduced.',
         maintenance='The project now uses the VibeSys name and a broader task framework. Pin current code separately from the VibeServe paper rather than transferring historical results to all later versions.'),
    'An agent framework for model-, hardware- and workload-specific serving stacks, with design search, implementation and framework-owned evaluation. The VibeServe paper and current VibeSys code are different revisions; generated systems remain scenario- and contract-specific.',
    '通过设计搜索、实现与框架侧评测，按模型、硬件和负载构建专用服务栈。VibeServe 论文与现行 VibeSys 代码版本不同；产物的支持范围由具体场景和验收契约限定。')

add('automegakernel', 'AutoMegaKernel', 'construction', 'execution', 'text', 'compiler',
    'model-family;hardware;single-stream;precision;schedule-ir',
    'model-lowering;persistent-kernel;schedule-search;static-dependency-checks;instruction-tuning',
    'Supported HuggingFace Llama-family graphs on CUDA, principally batch-one decode. Paper speed sweeps at position zero use synthetic weights at real model shapes; real-checkpoint quality tests have a separate scope.',
    'Lowers model graphs through a typed task/counter IR to one cooperative CUDA launch per forward pass. Agent-facing loops tune instruction implementations or structured schedules, with static IR checks and reference evaluation.',
    'tool-dependent;reduced-precision', 'public-code', 'intrinsic',
    'https://github.com/RightNow-AI/AutoMegaKernel',
    [ap, f'{A}/HARNESS.md', f'{A}/schedule/ir.py'],
    'A model-program construction case combining a restricted agent edit surface, deterministic lowering and schedule checks; contrasts with unconstrained whole-runtime generation.',
    'Static graph checks rely on a trusted VM and supported IR, not a mechanized whole-stack proof; inspected data-hazard checks have a task-count cap. Reported W8A16 wins compare against bf16 and cannot establish equal-precision superiority. The host still drives token steps; this is not a complete concurrent serving engine.',
    'automegakernel', 'AutoMegaKernel: checked generation of model-level execution',
    '通过受限调度 IR、模型降低和静态检查生成整步执行程序；不是完整服务引擎，也不是所有代码都可自由改写的 Agent 构建。',
    dict(motivation='Reduce per-operator execution boundaries while making generated whole-model schedules inspectable before device launch.',
         boundary='One persistent cooperative launch executes one forward pass; counters reset between launches, KV persists and the host advances decoding. Instruction tuning and ScheduleConfig search are different edit surfaces.',
         reuse='A handwritten trusted VM, instruction ABI, model importer, CUDA runtime and reference implementations remain shared. No per-model handwritten CUDA does not mean the trusted base is automatically generated.',
         tradeoff='Current inference scope is restricted to supported model graphs and hardware. Paper shape-level performance and real-checkpoint quality results are separate; low-bit comparisons are not equal-precision controls.',
         construction='The documented first loop tunes an ABI micro-kernel; the second proposes structured schedules lowered by the fixed VM. The inspected IR checks counters, dependencies, placement and buffer ordering.',
         ai_role='The compiler exposes an explicit coding-agent harness. Structured schedule search must not be described as unrestricted synthesis of a new runtime.',
         cost='Unattended self-tuning demonstrations compare against their own starting point. This inspection establishes neither full construction cost nor maintenance savings over a shared serving framework.',
         validation='Inspected schedule/ir.py, including static dependency and hazard checks. Some hazard checks are task-count-capped; references and supported VM semantics remain trusted. This is not a mechanized proof and no CUDA tests were run here.',
         maintenance='New operators, model features or device targets require compatible importer, ABI, validator and VM support; broad self-retargeting claims do not remove these obligations.'),
    'A Llama-family compiler and agent harness that emits one CUDA megakernel per forward pass through a checked schedule IR. The host still drives decoding. Static checks are not a whole-stack proof, and reported W8A16 wins use precision-asymmetric baselines.',
    '通过带检查的调度 IR，为 Llama 类模型生成每次前向执行的 CUDA 巨型内核，并提供 Agent 优化接口；宿主仍驱动解码。静态检查不是整栈证明，报告的 W8A16 优势采用非同精度基线。')

add('infire', 'Cloudflare Infire', 'system', 'execution', 'text', 'runtime',
    'hardware;deployment;cpu-budget;security;startup-latency',
    'native-rust-runtime;model-specific-jit;continuous-batching;chunked-prefill;paged-kv;multi-gpu-execution',
    'Cloudflare distributed inference nodes with constrained host CPU, startup and isolation requirements. The initial Hopper-focused report and later large-model/multi-GPU update describe different deployment stages.',
    'Rebuilds the Rust HTTP, batching and execution path; overlaps model loading and model-specific kernel compilation, manages paged state and cached execution graphs, and later adds pipeline/tensor/expert parallelism.',
    'configurable', 'closed-core', 'not-established', ib, [ib, iu],
    'An industrial platform-specialization case documenting why a provider rebuilt execution instead of only configuring a general framework; useful without an AI-development attribution.',
    'The engine is proprietary; evidence is official engineering disclosure rather than source inspection or independent reproduction. Initial CPU/performance comparisons mix bare-metal and sandboxed deployment conditions. Later multi-GPU support must not be treated as present in the initial release.',
    'infire', 'Cloudflare Infire: platform-specific serving reconstruction',
    '围绕边缘节点的 CPU、启动和隔离约束重建 Rust 服务执行栈；采用官方工程披露，明确核心专有，并区分初始实现与后续多 GPU 扩展。',
    dict(motivation='Cloudflare describes a mismatch between its geographically distributed resource-constrained nodes and the deployment assumptions of its earlier vLLM setup.',
         boundary='The disclosed stack includes the HTTP server, batcher and model executor, with model-specific kernels and execution graphs. Later work extends parallel model execution.',
         reuse='The report names Hyper, HuggingFace tokenizers, CUDA and cuBLASLt for suitable operations. A native replacement still retains shared libraries and established batching/cache mechanisms.',
         tradeoff='Specialization is to a provider platform and its deployment envelope, not one checkpoint. Proprietary implementation prevents independent source-level checking in this review.',
         construction='The original report describes a Rust rewrite with asynchronous loading, JIT compilation and hardware-focused kernels. The later report describes added multi-GPU and memory/startup work.',
         ai_role='No direct AI-construction attribution was established from the reviewed engineering reports. Do not infer it from the project being a newly built engine.',
         cost='The initial report measures CPU usage and throughput in selected deployment configurations; those operational observations are not a measurement of development or lifecycle cost.',
         validation='Two official engineering reports were reviewed. The initial comparison distinguishes bare-metal vLLM, sandboxed vLLM and CPU-constrained operation; keep those conditions separate. No engine execution or source audit was possible from these materials.',
         maintenance='The later multi-GPU report supplies concrete evolution evidence. Record new scope as a later stage rather than rewriting the original report or assuming all future model support.'),
    'A proprietary Rust serving stack built for Cloudflare nodes, combining model-specific kernel compilation, batching and paged state with later multi-GPU support. Official engineering reports describe the design; deployment conditions differ across comparisons, and AI-assisted construction is not established.',
    '围绕 Cloudflare 节点重建的专有 Rust 服务栈，结合模型专用内核编译、批处理、分页状态及后续多 GPU 支持。依据官方工程报告；不同对照的部署条件有别，未确认 AI 辅助构建。')

add('kie', 'Kog Inference Engine (KIE)', 'system', 'execution', 'text', 'runtime',
    'model;hardware;single-request;multi-gpu;latency',
    'persistent-monokernel;weight-streaming;device-side-sampling;topology-aware-synchronization;delayed-tensor-parallelism',
    'The reviewed low-latency preview uses an FP16 approximately 2B Laneformer model, batch one and eight AMD MI300X GPUs; the companion announcement also reports an eight-H200 configuration.',
    'Co-designs a persistent device-side generation loop with weight streaming, sampling, topology-aware handoffs and Laneformer delayed tensor-parallel communication, according to the vendor engineering report.',
    'layout-scheduling;trained-model', 'documentation-only', 'not-established', kb, [kb, kp],
    'An industrial model/runtime/hardware co-design case with an explicitly narrow low-latency operating point; distinguishes a purpose-built execution architecture from a generic serving configuration.',
    'The review covers vendor documents, not public engine source or reproduced results. The headline preview combines Laneformer/DTP with an eight-GPU FP16 setup; it is not evidence of the same gain on an unchanged arbitrary model, and third-party model roadmap statements are not implemented support.',
    'kie', 'Kog Inference Engine: model and device co-designed execution',
    '按单请求低延迟目标联动设计模型、持久执行与多卡通信；依据厂商文档，明确 Laneformer/DTP、八卡和 FP16 条件，不当作原模型通用加速结果。',
    dict(motivation='Target the low-latency single-request regime rather than maximizing aggregate throughput through large batches.',
         boundary='The vendor describes a monokernel managing sequence generation, sampling, state and cross-device communication, not only an isolated matrix multiplication.',
         reuse='Pretrained model assets, AMD/NVIDIA devices and their programming/runtime interfaces remain prerequisites. The vendor claims its own execution implementation; public engine source was not established.',
         tradeoff='The reviewed preview combines a roughly 2B FP16 Laneformer model with eight GPUs and batch one. Delayed tensor parallelism changes the model architecture, so runtime and model contributions must be separated.',
         construction='The engineering report describes compile-time work assignment, device-side synchronization, continuous weight streaming and delayed cross-device reductions. These are documentation-backed design claims, not inspected implementation paths.',
         ai_role='No direct coding-agent construction evidence was established in the reviewed materials; relevance comes from execution co-design.',
         cost='Reported latency and tokens per second do not quantify GPU cost per request, utilization under mixed load, construction effort or lifetime maintenance.',
         validation='Reviewed the technical monokernel article and matching preview conditions. Neither is an independent replication or a complete quality-equivalence protocol; announced future model support remains a roadmap.',
         maintenance='Model and device co-design creates adaptation obligations. The release of model weights, where applicable, must not be confused with publication of the inference engine implementation.'),
    'A vendor-described low-latency monokernel co-designing execution, weight streaming, sampling and multi-GPU communication. The reviewed FP16 preview uses Laneformer/DTP and eight MI300X GPUs; public engine source is not established, and these are not unchanged-model speedup results.',
    '厂商披露的低延迟持久单内核，联动设计执行、权重流式读取、采样与多卡通信。已审阅的 FP16 预览使用 Laneformer/DTP 和八张 MI300X；未确认引擎源码公开，不能视为不改模型的加速结果。')

REVIEW = f'''# Source review: construction workflows and industrial execution

Reviewed on **2026-10-14**, starting from `7dd83ff`. This is a focused follow-up on six named candidates, not an exhaustive survey or independent performance reproduction.

[Home](../README.md) · [Reading list](reading-list.md) · [Updates](updates.md)

## Decisions

| Work | Decision | Evidence boundary |
| --- | --- | --- |
| VibeServe / VibeSys | Add one construction record and the VibeServe case | May paper and lab blog; separately pinned current README and evaluation wiring. Do not duplicate the renamed repository or include unrelated VibeSys tasks. |
| AutoMegaKernel | Add a model-program construction record and case | Paper, agent harness and schedule-IR implementation. Restricted schedule generation is not unconstrained whole-runtime synthesis. |
| Cloudflare Infire | Add an industrial runtime record and case | Two official engineering reports; proprietary core, no source-level verification. Initial and later multi-GPU stages are distinct. |
| Kog Inference Engine | Add an industrial co-design record and case | Technical article plus matching preview report; engine source not established. Preserve the Laneformer/DTP, FP16, batch-one and eight-GPU conditions. |
| ForgeMegakernel | Add to reading and validation discussion; no separate software record yet | Paper reviewed. Exact-name GitHub and web searches did not establish an official implementation. This is a retrieval limitation, not proof that code does not exist. |
| Retire the Abstractions | Add as a perspective in the reading list | First-party Hazy Research account, not a software project or controlled cost study. |

## What the review changes

**Construction has different output boundaries.** VibeServe targets serving stacks. AutoMegaKernel emits a per-forward program through a fixed VM/IR and separate instruction/schedule loops. The ForgeMegakernel paper describes per-model decode generation integrated with SGLang. These should not be counted as the same kind of artifact.

**Checks must retain their actual scope.** AutoMegaKernel's inspected validator has task-count-capped data-hazard checks and assumes its supported IR and trusted VM. ForgeMegakernel describes reference KV/logit checks and functional probes, not a mechanized correctness proof. Its public implementation remains unverified in this review.

**Industrial specialization is not automatically evidence of AI authorship.** Infire supplies a platform-focused reconstruction example; KIE supplies model/runtime/device co-design. Operational performance does not establish lower construction cost. No AI-development attribution was established for either from the reviewed reports.

## Discovery and follow-up

Use papers and citations, author/lab blogs and vendor engineering reports as discovery routes, then follow canonical code and implementation evidence. News is a lead, not the final authority. Do not filter candidates by stars or require the term “inference engine” in a title. Conversely, a promising title or related dependency is insufficient for inclusion.

For ForgeMegakernel, recheck the authors' paper landing page and any subsequently linked repository before changing artifact status. Do not treat the arXiv abstract and HTML rendering as two independent implementation sources. For the admitted records, retain the exact reviewed revisions and distinguish later maintenance from historical paper results.

## Reviewed primary sources

- VibeServe: [paper]({vp}), [SyFI lab report]({vb}), [current VibeSys README]({V}/README.md), [host evaluation wiring]({V}/src/vibesys/core_wiring.py).
- AutoMegaKernel: [paper]({ap}), [agent integration contract]({A}/HARNESS.md), [schedule IR and validator]({A}/schedule/ir.py).
- Infire: [initial design report]({ib}), [later large-model and multi-GPU work]({iu}).
- KIE: [monokernel design]({kb}), [preview conditions]({kp}).
- ForgeMegakernel: [paper]({fp}).
- Perspective: [Retire the Abstractions]({hz}).

## 中文结论

本轮新增四项有明确边界的记录及案例：VibeServe/VibeSys、AutoMegaKernel、Infire、KIE。前两项分别是服务栈构建和模型级执行生成；后两项是工业平台特化与软硬件协同设计，不推定 AI 作者身份。ForgeMegakernel 已纳入文献及验证讨论，但未找到可确认的官方代码，不标作开源工具；Hazy Research 文章作为观点材料，不增加项目计数。检索范围限于这六项及其直接来源，未运行上游引擎、付费 Agent 或 GPU 实验，也未重新审查整个既有目录。
'''

ADDITION_READING = '''- [VibeServe paper](https://arxiv.org/abs/2605.06068) and [current VibeSys framework](https://github.com/uw-syfi/vibesys) — target-specific serving-stack construction; keep the paper and later implementation revisions separate. [Case](cases.md#vibeserve).
- [AutoMegaKernel](https://arxiv.org/abs/2606.09682) — model-level persistent execution generated through a restricted schedule IR and trusted VM; static checks are not a whole-stack proof. [Case](cases.md#automegakernel).
'''

READING_SECTIONS = f'''## Model-level generation: paper evidence

- [ForgeMegakernel]({fp}) — milestone-guided decode megakernel generation with reference KV/logit and functional checks, followed by SGLang integration. Reviewed as a paper; an official implementation was not established by this search. It is not currently counted as an independently verified software project. [Review and next check](source-review-2026-10-14.md).

## Industrial execution-stack design

- [Cloudflare Infire](cases.md#infire) — proprietary Rust execution tailored to deployment constraints; [initial design]({ib}) and [later multi-GPU development]({iu}) provide separate stages of evidence.
- [Kog Inference Engine](cases.md#kie) — vendor-described persistent execution and model/device co-design. Read the [implementation discussion]({kb}) with the [preview's model and eight-GPU conditions]({kp}), not as an unchanged-model generic speedup.

## Perspectives on construction and abstraction

- [Retire the Abstractions]({hz}), Hazy Research, August 5, 2026 — a first-party account arguing that agents can replace some implementation scaffolding while references, tests and domain knowledge remain necessary. This is a perspective grounded in one team's experience, not causal evidence that general runtimes are obsolete.

'''

VALIDATION = f'''## Construction-time checks: additional evidence

[AutoMegaKernel](cases.md#automegakernel) checks a typed schedule and its dependency/counter structure before device execution. The [inspected validator]({A}/schedule/ir.py) assumes a trusted VM and supported IR, and some data-hazard checks have a task-count cap. Static checking and empirical reference agreement do not establish a mechanized whole-stack proof.

The [ForgeMegakernel paper]({fp}) adds intermediate KV/logit comparisons, poisoned future-KV probes and per-lane-position checks. This is paper evidence rather than source-inspected validation tooling: an official implementation was not established in this review. A finite oracle and source scan should not be described as an unconditional correctness guarantee.

[VibeServe / VibeSys](cases.md#vibeserve) separates candidate construction from target-specific measurement. The [current host wiring]({V}/src/vibesys/core_wiring.py) records evaluator/workload/environment identities and configured measurement gates; identities help trace evidence but do not prove the adequacy of those gates.

本节补充三种不同边界：受限 IR 的静态检查、论文提出的中间状态检验、构建框架对验收流程和结果来源的管理。未运行这些上游验证，也不把缺少源码的论文方案称为已检查的实现；首页原有四类验证入口保持不变。

'''

UPDATES = '''## 2026-10-14 — Literature and industrial follow-up / 论文与工业案例补查

- Added four records and associated construction cases: [VibeServe/VibeSys](catalog.md#vibesys), [AutoMegaKernel](catalog.md#automegakernel), [Infire](catalog.md#infire), and [KIE](catalog.md#kie). The catalog now contains **126 project records and 68 cases**.
- Added ForgeMegakernel as paper evidence and Hazy Research's perspective to the [reading list](reading-list.md), without inflating repository counts or claiming unavailable code is open.
- Recorded distinct construction boundaries, precision/deployment caveats, code visibility and pinned implementation evidence. Extended the detailed validation guide and corrected stale contributor instructions to match the existing bilingual/domain-first homepage.
- Preserved the six starter cards, banner assets, layout policy, existing records and their review dates. The [source-review note](source-review-2026-10-14.md) records decisions and unresolved artifact checks.

本轮落实六项补审：四项进入目录与案例，两项进入阅读材料。检索了论文、官方代码与工程博客；没有运行上游 GPU/Agent 实验，不把厂商报告或静态检查包装成独立复现或整栈证明。

'''

root = Path('.')
assert (root / 'catalog/projects.csv').is_file(), 'Run from the checked-out repository root'


def load(path):
    return json.loads((root / path).read_text(encoding='utf-8'))


def save(path, value):
    (root / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def insert(path, marker, value):
    p = root / path
    old = p.read_text(encoding='utf-8')
    assert old.count(marker) == 1, f'Unexpected structure in {path}'
    p.write_text(old.replace(marker, value + marker, 1), encoding='utf-8')


old_csv = (root / 'catalog/projects.csv').read_text(encoding='utf-8')
reader = csv.DictReader(io.StringIO(old_csv))
original_rows = list(reader)
assert len(original_rows) == 122, 'Refresh against the current catalog before applying'
ids = {r['id'] for r in original_rows}
urls = {r['url'].rstrip('/').lower() for r in original_rows}
for e in entries:
    assert e['row']['id'] not in ids and e['row']['url'].rstrip('/').lower() not in urls
    assert set(e['row']) == set(reader.fieldnames)
buf = io.StringIO(newline='')
csv.DictWriter(buf, fieldnames=reader.fieldnames, lineterminator='\n').writerows(e['row'] for e in entries)
(root / 'catalog/projects.csv').write_text(old_csv + ('' if old_csv.endswith('\n') else '\n') + buf.getvalue(), encoding='utf-8')
assert list(csv.DictReader(io.StringIO((root / 'catalog/projects.csv').read_text(encoding='utf-8'))))[:-4] == original_rows
cases = load('catalog/cases.json')
assert len(cases) == 64
assert not ({c['id'] for c in cases} & {e['case']['id'] for e in entries})
assert all(set(e['case']) == set(cases[0]) for e in entries)
save('catalog/cases.json', cases + [e['case'] for e in entries])
for language in ('en', 'cn'):
    p = f'catalog/homepage_{language}.json'
    data = load(p)
    assert set(data) == ids
    data.update({e['row']['id']: e[language] for e in entries})
    save(p, data)
schema = load('catalog/schema.json')
for lookup, new_ids in [('vibeqwen', ['vibeserve', 'automegakernel']), ('ninfer', ['infire', 'kie'])]:
    groups = [g for g in schema['case_groups'] if lookup in g['examples']]
    assert len(groups) == 1
    groups[0]['examples'].extend(new_ids)
schema['homepage_construction'].extend([
    {'id': 'vibesys', 'output': 'Scenario-specific serving stacks; separate VibeServe and VibeSys revisions', 'output_cn': '场景专用服务栈；区分 VibeServe 与 VibeSys 版本'},
    {'id': 'automegakernel', 'output': 'Checked model-forward program; not a complete serving engine', 'output_cn': '带检查的模型前向程序；不是完整服务引擎'}])
save('catalog/schema.json', schema)
p = root / 'scripts/homepage_layout.py'
text = p.read_text(encoding='utf-8')
for old, new in [
    ("('anemll', 'kernelagent', 'mirage', 'mlc-llm', 'onediff', 'stable-fast')", "('anemll', 'automegakernel', 'kernelagent', 'mirage', 'mlc-llm', 'onediff', 'stable-fast')"),
    ("('agentcompile', 'metainfer', 'seis', 'sol-engine')", "('agentcompile', 'metainfer', 'seis', 'sol-engine', 'vibesys')")]:
    assert text.count(old) == 1
    text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
p = root / 'docs/reading-list.md'
text = p.read_text(encoding='utf-8')
marker = '## Engine generation, testing, and evidence\n\n'
assert text.count(marker) == 1
text = text.replace(marker, marker + ADDITION_READING, 1)
marker = '## Important counterexamples\n'
assert text.count(marker) == 1
p.write_text(text.replace(marker, READING_SECTIONS + marker, 1), encoding='utf-8')
insert('docs/validation.md', '## Efficient validation: an open research question\n', VALIDATION)
insert('docs/updates.md', '## 2026-10-14 — SEIS construction case / 纳入 SEIS 构建案例', UPDATES)
p = root / 'docs/source-review-2026-10-14.md'
assert not p.exists()
p.write_text(REVIEW, encoding='utf-8')
# Correct obsolete maintenance guidance without changing the current layout policy.
p = root / 'CONTRIBUTING.md'
text = p.read_text(encoding='utf-8')
replacements = {
    'Group by primary role and mechanism; supporting resources use their existing purpose groups. Display model-domain labels on each entry.':
    'Group engines by primary model domain and construction workflows by output boundary; supporting resources retain their purpose groups. Avoid repeating the section domain; keep additional domains as secondary text.',
    'English descriptions come from `projects.csv` (`mechanism`); `catalog/homepage_cn.json` supplies a source-grounded Chinese description for every project ID. Update both when a record changes.':
    'Concise homepage descriptions come from `catalog/homepage_en.json` and `catalog/homepage_cn.json`; maintain equivalent facts for every project ID in both languages. Project identities, scope and detailed mechanisms remain in `projects.csv`. Update the source records and both summaries when facts change.',
    '`HOMEPAGE_VALIDATION` in `scripts/update_readme.py`':
    '`HOMEPAGE_VALIDATION` in `scripts/homepage_layout.py`'}
for old, new in replacements.items():
    assert text.count(old) == 1
    text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
assert len(load('catalog/cases.json')) == 68
print('Applied four reviewed records/cases; preserved previous entries, review dates and showcase.')
