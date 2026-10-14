# Latest updates / 最近更新

[Home](../README.md) · [中文首页](../README_CN.md) · [Quick comparison](representative-comparison.md) · [Contributing](../CONTRIBUTING.md)

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
