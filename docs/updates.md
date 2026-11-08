# Latest updates / 最近更新

[Home](../README.md) · [中文首页](../README_CN.md) · [Quick comparison](representative-comparison.md) · [Contributing](../CONTRIBUTING.md)

## 2026-11-08 — Discovery vocabulary and source follow-up queue / 检索词库与源码补审线索

- Established a [maintained keyword bank](../catalog/search_keywords.json): 11 groups with 131 terms, 12 hardware groups, 8 model-term groups and 20 query templates. The [search guide](search-strategy.md) separates retrieval, source triage and catalog admission.
- Executed 20 GitHub repository queries and three web queries; preserved the exact queries and 400 returned observations (359 distinct repository names) in the [bounded run record](../catalog/search_runs/2026-11-08.json). Broad synthesis/RSI terms, capped result pages and ordinary forks exposed retrieval limits; no exhaustive-coverage claim is made.
- The [discovery report](discovery-2026-11-08.md) records seven source-spot-checked leads: EngineSmith, Molten, FreeToken, InferRSI, Saber, open_rknpu2_lm_infer and PolyStrata. Framework/output and upstream-reuse relationships guide the remaining checks.
- This pass changes discovery resources, not admission decisions: **142 projects and 83 cases** remain. Existing entries, review dates, star observations and homepage layout are unchanged. No upstream build, benchmark or agent run was performed.

补充“构建框架 → 产物”“致谢 → 上游依赖”“硬件代号 → 执行路径”三类检索路线；候选与正式收录分开，搜索命中不作为性能或正确性结论。

## 2026-11-07 — Synthesized Mac engines and executable construction gates / 合成的 Mac 引擎与可执行构建门禁

- Added [JITEngine](catalog.md#jitengine) and [SkyDiscover / SkySynth](catalog.md#skydiscover), with one [workflow/output case](cases.md#jitengine): **142 projects and 83 cases**. Six engine packages remain one repository record; SkySynth is part of SkyDiscover.
- The [pinned source review](source-review-2026-11-07.md) traces Flash-Next Metal expert execution, cache correction, lookahead rollback and compact quantization metadata, with bounded scheduling/persistent-kernel checks in other packages. MLX, inherited offload strategy and quantized checkpoints are explicitly credited.
- Clarified that the installer chooses released builds. The 2.72× claim uses author-reported 32.9 versus 12.1 tok/s on M4 Pro at a 40 GB budget, with the slotstream 0.2.11 baseline from an earlier session. Optional relaxed profiles and quantized-reference exactness are separated; no upstream build, GPU benchmark or synthesis run was performed.
- Recorded SkySynth's task-dependent test admission, runner and artifact gates, distinguishing its separate evolutionary and formal-proof paths. Updated bilingual entries, construction grouping, Apple/Qwen discovery, validation evidence, recent additions and generated views. Prior records/cases/dates and homepage layout are preserved; only the two new star observations were added.

新增条目依据实际执行和构建实现，不以速度宣传代替技术核查。保留模型／设备边界、上游复用与验证缺口；“已生成版本安装”“运行时内核编译”和“系统合成”分别表述。

## 2026-11-05 — Hardware/model discovery and concise homepages / 硬件模型入口与首页精简

- Added a compact hardware/model finder near the top of both homepages and a [generated scope guide](find-a-stack.md) with 13 curated routes. Existing project IDs, canonical target scope, source visibility and review dates remain the authority; overlapping routes add no records or compatibility claims.
- Shortened 17 bilingual summary pairs, retaining upstream attribution, closed cores, model/precision changes, default expert reduction and material verification gaps. A shared evidence note states that benchmark performance has not been independently reproduced.
- Refined the four light/dark, wide/compact SVG banners with stronger hierarchy and numbered execution layers. Kept all **140 projects** expanded exactly once on each homepage, the domain-first organization and all **82 cases**.
- Updated generators, contributor guidance and referential-integrity checks. This presentation update does not refresh technical review dates, star snapshots or performance evidence.

按设备／模型查找入口前置，长摘要精简，头图加强主次与深浅主题适配。范围页直接引用原始记录，不把硬件家族标签当作全面兼容性承诺；原有手机执行机制交叉索引继续保留。

## 2026-11-05 — Cluster execution, Blackwell reconstruction and BC-250 offload / 集群执行、Blackwell 重构与 BC-250 卸载

- Added three source-reviewed core cases: [gr8](catalog.md#gr8), [Basalt](catalog.md#basalt) and [N3komata](catalog.md#n3komata). The catalog now contains **140 records and 82 cases**. Only N3komata was created after the preceding review; admission dates are not release dates.
- The [pinned source review](source-review-2026-11-05.md) traces trellis/collective/KV integration, Strata-derived device-planned expert windows and Infernix-adapted FP4 prefill, and a llama.cpp/Vulkan graph/cache/upload patch. Upstream tiering and quantization are not presented as new inventions.
- Distinguished topology-dependent precision, shared-step numerics, finite quality gates, optional routing/drafting approximations and N3komata's default expert reduction. The complete N3komata release profile lacks a controlled end-to-end benchmark. All performance remains author-reported; no upstream build or GPU test was run.
- Updated bilingual summaries, cases, classifications, recent additions, validation evidence and generated indexes. Added only three new star observations. Prior project/case facts, dates, reading selections and homepage organization remain unchanged. Overall repository improvement ideas were reviewed separately, without implementing a redesign or new workflow.

新增三项均有实际执行改造证据：gr8 为完整 GLM 的 Spark 集群路径，Basalt 为明确归因上游的 Blackwell 深度分支，N3komata 为带近似默认配置的 BC-250 补丁栈。Legion 继续核查，LiteMoE 暂不作为教学型引擎新增；未把新建日期、源码检查或作者实验混同为独立复现。

## 2026-11-03 — Expanded native, mobile and speech execution / 原生、移动与语音执行扩展核查

- Added four source-reviewed core cases: [Strixite](catalog.md#strixite), [Spark Engine](catalog.md#spark-engine), [MobiInfer Android](catalog.md#mobiinfer-android), and [Maya2 Native / Maya3](catalog.md#maya2-native). The catalog now contains **137 records and 79 cases**.
- The [expanded review](source-review-2026-11-03-expanded.md) traces HIP/CUDA kernel dispatch, recurrent-state commit/rollback, RoCE collectives, external-expert slot callbacks, and CUDA-graph speech execution. Upstream reuse is explicit; Maya3 is not counted separately from its repository.
- Qualified author benchmarks and numerical contracts: Strixite's default thinking nudge and unavailable full test suite, Spark Engine's diagnostic-only MoE probe, iPad versus Android LES results, and Maya's precision/EOS guards and pre-release measurements. No upstream hardware experiment was run.
- Updated bilingual entries, cases, evidence, recent additions and generated views; added mobile expert placement to the existing device cross-index. All prior records and review dates are preserved. gr8, Basalt and Delta remain leads pending direct implementation/delta checks.

本轮新增四项，覆盖 395、DGX Spark、手机 NPU 和流式语音；目录共 137 个项目、79 个案例。收录依据具体执行实现，不依据作者速度排名。保留原有首页组织，并明确模型改动、上游复用和验证覆盖范围。

## 2026-11-03 — Flash-Next on Strix Halo / Strix Halo 专用执行补查

- Added [Qwenox](catalog.md#qwenox) and [Crucible](catalog.md#crucible) as source-reviewed core systems and native-runtime cases. Refreshed the existing [Halogen Flash](catalog.md#halogen-flash) entry, preserving its closed-core classification. The catalog now contains **133 records and 75 cases**.
- The [pinned review](source-review-2026-11-03.md) traces actual kernel dispatch, weight-format reuse, speculative state and concrete validation contracts. It separates adapted Gufo/hipfire kernels from Qwenox integration, EXL3 packs from Crucible execution, and Halogen's public documentation from its unavailable core source.
- Current Halogen documentation includes Anthropic Messages and persistent disk caching; these are not Qwenox-exclusive features. Default cache identity, W4A4 approximation, adaptive draft width and author-only benchmark limitations are explicit. The supplied third-party comparison is a discovery lead, not an independently reproduced ranking.
- Updated bilingual summaries, classification, evidence, recent additions, generated indexes and three focused star observations. Preserved unrelated records, review dates and homepage organization; broader candidates and outstanding checks are recorded without inflating counts.

新增两项、更新 Halogen 原条目；共 133 个项目、75 个案例。完成源码与文档核查及目录一致性检查，未运行上游 GPU 实验。量化、缓存与投机配置的影响单独注明，不以同权重推断数值等价，不把单次任务分数解释为已证实的质量结论。

## 2026-10-23 — Device constraint cross-index / 设备约束与执行机制对照

- Added a [bilingual device × execution matrix](device-execution-matrix.md) linking existing catalog entries to phone-specific CPU, GPU, NPU, KV-state and multimodal mechanisms **without changing primary categories, six starters, catalog counts or source-review dates**.
- Inspected pinned official MNN Hexagon/C4 and UbiquitousLearning/mllm QNN AOT documentation and code; separated not-yet-admitted implementations from established catalog members and from ExecuTorch/LiteRT-LM construction comparators. MNN 3.6.1 phase-specific performance numbers are author reports, not reproduced measurements; PowerInfer-2 remains a paper-only lead.
- Extended offline regression coverage for the repository's banner and normal README generation commands without modifying any Actions workflow; upstream phone/GPU experiments were not run.

新增端侧横向检索表，不新增“手机端”一级分类，也不把研究线索直接计入项目数。候选源码已区分为官方证据、已核实路径和未独立复现结论；全量目录正式收录须另行执行源数据变更及生成校验。

## 2026-10-23 — Arc execution and NInfer-based reconstruction / Arc 执行与基于 NInfer 的重构

- Added two source-reviewed core systems and cases: [Mach X](catalog.md#machx), with model-dispatched SYCL/XMX attention and lane serving on Intel Arc; [Ignis](catalog.md#ignis), with a new batch/state execution program over inherited NInfer kernels and integrated top-k / adapted prefill replacements. The catalog now contains **131 records and 73 cases**.
- [Pinned source review](source-review-2026-10-23.md) traces dispatch, fallback, provenance and concrete test contracts. It distinguishes Mach X's local old/new-kernel bit-identity claim from reference equivalence, and Ignis's original/adapted work from upstream ports, quantization and changed checkpoints. All quoted performance remains author-reported; no upstream GPU execution was performed.
- Updated bilingual summaries, case classification, evidence, recent additions and all generated indexes. Fetched only the two new GitHub star observations; existing snapshots and technical review dates retain their actual dates. Existing records, reading selections and homepage organization are preserved.

新增两项均有源码调用链支持，不按宣传性能收录。Mach X 的 32K 测试为两张 B70 上的版本对比；Ignis 的 1,065 tok/s 为八路聚合结果，相关更新包含上游移植。低精度、草稿模型及部分未公开原始实验记录的限制已写入；未宣称独立复现。

## 2026-10-16 — Specialized decoding, video placement and MoE lanes / 专用解码、视频驻留与专家并发

- Added three source-reviewed **core execution cases**: [dInfer](catalog.md#dinfer) (diffusion language decoding and KV refresh), [FreeVideo](catalog.md#freevideo) (VDN-H3 resource-aware video execution), and [peregrine](catalog.md#peregrine) (Rust CPU/NVMe/optional CUDA expert concurrency). The catalog now has **129 project records and 71 cases**.
- Pinned direct upstream code and design evidence, retained strong qualifications on model changes and resource limits, and recorded that peregrine's single-sequence disk-bound benchmark is *slower* than Colibri; no independent GPU experiment was run.
- Added bilingual summaries, three official GitHub star observations dated 2026-10-16 and a direct dInfer Paper link. Existing 2026-10-14 snapshots are within the seven-day freshness window and were not needlessly refreshed; six starter cards, project anchors and technical review dates of older entries are unchanged.
- [Focused review decisions](source-review-2026-10-16.md) detail candidates excluded or deferred, evidence depth and the next refresh boundary. ForgeMegakernel's official implementation was not established in this review.

本轮新增扩散语言模型、低显存视频及异构 MoE 并发三个不同的执行案例，核查并固定实现与限制；新增项目的 Star 单独采集，已有快照未到期不强制更新。未运行上游 GPU 实验，也不推断 AI 开发参与或普遍性能收益。

## 2026-10-14 — Star snapshots and direct sources / 关注度快照与来源直达

- Added compact GitHub repository-star snapshots beside project names, with observation dates, explicit parent-repository labels and failure-safe cached values. Stars do not change order or inclusion.
- Promoted selected already-reviewed Paper / Blog / Case report links into the bilingual entries. Added a small recent-additions line whose dates mean catalog admission, not upstream release.
- Added an opt-in, bounded metadata refresher and offline regression tests. Kept all 126 project records, 68 cases, technical review dates, descriptions, source evidence, banners and starter cards unchanged.
- [Metadata and maintenance rules](homepage-metadata.md) explain cache age, missing numbers, parent repositories and the existing weekly maintenance path. This is a presentation/metadata change, not another source audit or engine benchmark.

新增紧凑 Star 快照、已核实来源入口与近期收录提示。母仓库不冒充子项目，缺失或获取失败不记为零；关注度更新时间与技术核查日期分离。布局、条目与原有测试保持不变，普通生成和 CI 不联网。

## 2026-10-14 — Literature and industrial follow-up / 论文与工业案例补查

- Added four records and associated construction cases: [VibeServe/VibeSys](catalog.md#vibesys), [AutoMegaKernel](catalog.md#automegakernel), [Infire](catalog.md#infire), and [KIE](catalog.md#kie). The catalog now contains **126 project records and 68 cases**.
- Added ForgeMegakernel as paper evidence and Hazy Research's perspective to the [reading list](reading-list.md), without inflating repository counts or claiming unavailable code is open.
- Recorded distinct construction boundaries, precision/deployment caveats, code visibility and pinned implementation evidence. Extended the detailed validation guide and corrected stale contributor instructions to match the existing bilingual/domain-first homepage.
- Preserved the six starter cards, banner assets, layout policy, existing records and their review dates. The [source-review note](source-review-2026-10-14.md) records decisions and unresolved artifact checks.

本轮落实六项补审：四项进入目录与案例，两项进入阅读材料。检索了论文、官方代码与工程博客；没有运行上游 GPU/Agent 实验，不把厂商报告或静态检查包装成独立复现或整栈证明。

## 2026-10-14 — SEIS construction case / 纳入 SEIS 构建案例

- Added [SEIS](catalog.md#seis) as a core construction workflow and linked its [whole-engine evolution case](cases.md#seis), paper and pinned public implementation evidence.
- Distinguished the paper's H100 experiment from the public ten-trial Blackwell demonstration; did not merge their speed, cost or validation claims.
- Added equivalent English/Chinese homepage summaries, the existing runtime-construction group, reading-list and validation cross-links. Counts become **122 project records and 64 construction cases**; the six starter cards, visual design and existing project records remain unchanged.
- This update is a focused source review, not an independent engine benchmark or a fresh review of all existing projects.

本次新增 SEIS 项目记录与构建案例，并同步双语首页、阅读入口和验证说明。区分 H100 论文实验与公开十轮 Blackwell 示例，保留量化与验证边界，不重复计数关联介绍页、脚手架和引擎分支。未复现上游性能。

## 2026-10-12 — Complete listings on both homepages / 中英文首页完整展开

- Both homepages now contain all **121 projects**, always expanded with direct upstream links, concise explanations and model-domain labels. The full list is grouped into engines, construction, benchmarks and support, with mechanism-oriented subcategories.
- Validation is expanded in place: four contracts and six named method entries explain what is checked and what a pass cannot establish. Methods embedded in a project do not add duplicate repository counts.
- Construction outputs, benchmark comparison questions, and the uses of diagnostics, knowledge and reusable components are explained on the homepage. The table of contents jumps to these local sections.
- The 12-case matrix and synthesis remain useful supplements below the complete list. The homepage is no longer a short directory of links to other pages.
- Regression tests enforce complete, unique project coverage and direct upstream links on both language versions.

中英文首页现按类别完整展开 **121 个项目**，每项附上游链接、说明和模型领域。引擎、构建、验证、评测、配套资源均在首页讲清楚；四类验证契约和六个具名方法也直接展开，内嵌方法不重复计数。精选案例与对照只作补充，目录链接直接跳转本页相应部分。测试保证两种语言完整且不重复地展示所有项目。

This corrects the earlier overly compressed homepage layout; source-review dates and the underlying project/case evidence are unchanged. / 本次修正此前过度压缩的首页布局，来源检查日期及底层项目、案例证据不变。

## Earlier on 2026-10-12 — Comparison and synthesis / 当日较早更新：对照与综合

- Added curated reading choices; the shortened-homepage layout was subsequently replaced by the complete listings described above.
- The generated [12-case matrix](representative-comparison.md) exposes reviewed model/device scope, execution ownership, retained components, validation limits and direct upstream sources. [Selection reasons](representative-comparison.md#why-these-cases--为什么选这些案例) explain the reading benefit rather than rank projects.
- The [cross-case synthesis](synthesis.md) connects execution control, reuse, construction evidence, validation and requalification.
- All **121 project records and 63 construction cases** remain available. The [full comparison](comparison.md), [case evidence](cases.md), [taxonomy](taxonomy.md) and [research agenda](research-agenda.md) remain the deeper reference.
- A [manual, capped external-link check](../scripts/check_external_links.py) can sample selected documentation. Offline catalog checks remain deterministic; access restrictions, rate limits and timeouts are not labeled dead links.

这次更新压缩中英文首页，解释选例的阅读收益；新增生成式速查矩阵与跨案例综合。121 个项目、63 个案例及完整证据与研究框架均保留。外链检查按需手动、限量运行，访问受限和超时不直接判作失效。

**Verification boundary:** this is a presentation/tooling update based on existing records. It does not claim a fresh inspection of every upstream project, an executed engine benchmark or a completed external-link audit. Source-review dates are preserved in the records; documentation-update dates do not replace them.

**检查边界：**本次基于已有记录改进阅读与维护工具，不表示重新检查了所有上游项目，也没有运行引擎评测或完成全量外链审计。记录中的源码检查日期保持不变，文档更新日期不能代替它。

## Source-review context / 源码核查背景

The [2026-10-12 resource audit](resources-audit-2026-10-12.md) records the earlier resource review and its scope. Individual [project](catalog.md) and [case](cases.md) entries carry their own source pointers and caveats.

此前的[资源核查](resources-audit-2026-10-12.md)说明当轮来源与范围；具体证据、日期及限制仍以项目和案例记录为准。
