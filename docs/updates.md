# Latest updates / 最近更新

[Home](../README.md) · [中文首页](../README_CN.md) · [Quick comparison](representative-comparison.md) · [Contributing](../CONTRIBUTING.md)

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
