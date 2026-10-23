# Construction resources audit · 2026-10-12

本轮围绕“专用推理引擎、构建方案、验证方案”主线，核查讨论中提出的评测、性能诊断和构建知识资源。新增 **5 条项目记录**，并移除 **45 条**超出收紧后范围的记录，当前目录共 **121 条**。旧的宽泛检索快照同步删除，不另设备份目录。FastKernels 已在目录，本轮不重复增加；Atrex GPU Wiki 是 AKA 的子组件，不单独计数。ANE Field Guide 此前已作为 ane.cpp 的证据出现，本轮新增的是知识资源入口，不新增引擎案例。

This is a bounded source audit of five named resources, not another exhaustive discovery round. Every new record has an immutable revision and README plus implementation/resource evidence. Upstream code was read, not executed; no benchmark result, correctness guarantee or development-cost reduction was independently reproduced. Instructions contained in upstream skills and experiment programs were treated as source material, not as instructions to run those workflows.

## Placement / 收录位置

| Record | Primary catalog role | Supporting role | Why it belongs |
| --- | --- | --- | --- |
| `atrex-kernel-agent` | Construction · adjacent | Profiling, validation and knowledge feedback | An operator-generation harness connects coding episodes to evaluator-owned acceptance and subsequent optimization. |
| `atrex-bench` | Benchmark · foundation | Reference checks and measurement protocol | Production-derived operator tasks evaluate generated components under explicit input and hardware contracts. |
| `ncu-report-skill` | Support · foundation | Performance diagnosis | Measured kernel symptoms inform an agent's next implementation decision. |
| `kernelwiki` | Support · foundation | Construction knowledge | Searchable, source-linked implementation experience can inform hardware-specific kernel design. |
| `ane-field-guide` | Support · foundation | Hardware probes and experiment history | Empirical findings are connected to changes in the separately cataloged ane.cpp engine. |

The primary role describes the artifact's main contribution here. A benchmark can contain a correctness checker; a construction harness can contain diagnostics and a knowledge store. These secondary functions do not create additional project counts. None of these additions is classified as a complete inference engine.

## ncu-report-skill

Reviewed revision: `74a12918e9f64d78036f14da5f8765e435b949a4`.

- [README](https://github.com/mit-han-lab/ncu-report-skill/blob/74a12918e9f64d78036f14da5f8765e435b949a4/README.md) establishes the CUDA/Nsight Compute workflow and the B200 / sm_100 emphasis.
- [Report extraction implementation](https://github.com/mit-han-lab/ncu-report-skill/blob/74a12918e9f64d78036f14da5f8765e435b949a4/helpers/analyze_reports.py) loads NCU reports, archives metrics and produces selected-metric comparisons. This is executable support beyond a prose recommendation.
- [Diagnosis playbook](https://github.com/mit-han-lab/ncu-report-skill/blob/74a12918e9f64d78036f14da5f8765e435b949a4/reference/06-diagnosis-playbook.md) relates observations to possible causes, candidate changes and exceptions.

**Boundary:** diagnosis is a hypothesis for the next experiment. A metric pattern is not proof that a suggested change helps; counter names and heuristics need checking on other GPUs. The resource does not generate an integrated model runtime. Its documented agent workflow supports `ai_involvement=intrinsic`; this does not claim that AI authored the repository.

## Atrex Kernel Agent (AKA), including GPU Wiki

Reviewed revision: `b708d9fcd0eff5214bcc5b91aae62357356e525c`.

- [README](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/README.md) describes evaluator-owned operator tasks, coding backends, isolated episodes and supported targets.
- [Campaign implementation](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/long_horizon/campaign.py) implements candidate evaluation, comparison with canonical measurements and acceptance. Fast episodes and full episodes do not use identical verification schedules.
- [Production-policy implementation](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/orchestrator/optimization_policy.py) imposes framework and implementation constraints; a production label is not an independent deployment certification.
- [NVIDIA profiling implementation](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/tools/profile_nvidia.sh) collects NCU artifacts, metric summaries and optional source-level evidence for subsequent decisions.
- [GPU Wiki workflow](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/gpu-wiki/README.md) separates trace/session extraction, knowledge distillation, admission and retrieval. It is linked as part of AKA, not a separate repository or engine.

**Boundary:** the construction target is an operator kernel. Numerical probes and policy checks do not prove correctness for arbitrary inputs or successful integration into a complete inference stack. Knowledge-store entries have their own scope and provenance; their existence alone does not establish a reduction in engineering cost. The workflow is intrinsically agent-based.

## Atrex-Bench

Reviewed revision: `22d6a57b98ebb45c8db76e98815158d820c1dca3`.

- [README](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/README.md) identifies production-derived operator tasks, executable references, DSL backends and separated generation/evaluation sessions.
- [Correctness implementation](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/src/atrex_bench/eval/correctness.py) checks output structure and numerical differences, declared input mutation and unexpected side effects under the task's contracts.
- [Performance implementation](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/src/atrex_bench/eval/performance.py) measures candidate forward calls, distinguishes eager and graph-replay modes, and scopes kernel attribution to the measured forward.

**Boundary:** “end-to-end” in this project concerns the operator-generation/evaluation process. It does not establish full-model quality, serving performance or the total cost of constructing an engine. Finite input checks depend on tolerances; roofline efficiency and application speedup are different measurements. Its agent-generation task makes AI involvement intrinsic to the evaluated workflow.

## KernelWiki

Reviewed revision: `b6b4301f15e8ce6955a56776690643ce5db369e6`.

- [README](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/README.md) identifies the Blackwell/Hopper scope, source corpus, knowledge pages, version claims and provenance bundles. It reports a PR-corpus cutoff of 2026-05-20 and documentation/release checks through 2026-08-18; these are the upstream resource's stated coverage boundaries.
- [Query implementation](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/scripts/query.py) loads source/wiki frontmatter, expands aliases, ranks keyword matches and applies metadata filters.
- [Warp-specialization knowledge page](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/wiki/techniques/warp-specialization.md) shows architecture scope, confidence, source references and an implementation fragment.
- [Captured artifact provenance](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/artifacts/kernels/warp-specialization/full/PROVENANCE.yaml) links the local asset to an upstream PR, revision, path and checksum.

**Boundary:** this audit confirms the retrieval and provenance structure, not every technical statement in the corpus. Kernel programming knowledge is not an engine or a demonstrated reduction in construction cost. Captured assets retain their upstream licensing. Packaging as an agent skill does not establish AI authorship, so the catalog retains `ai_involvement=not-established`.

## Apple Neural Engine Field Guide

Reviewed revision: `83e73eb94051dc67431829d0f3d3eb67db0b8e9b`.

- [README](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/README.md) states the empirical M3 Max scope and connection to ane.cpp.
- [Experiment workflow](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/program.md) separates standalone hardware probes from applying supported findings to the engine.
- [Experiment ledger](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/results.tsv) retains discoveries and kept/discarded changes with revision references.
- [Dispatch-scaling probe](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/tests/test_dispatch_scaling.cpp) compares evaluation and host-transfer paths and fits fixed dispatch cost plus a bandwidth term.

**Boundary:** reported measurements remain author results. They primarily concern a particular M3 Max/macOS environment and private ANE APIs; they cannot be generalized to all Apple accelerators. A documented autonomous experiment program is not enough to attribute every implementation change to AI. The resource complements the existing ane.cpp case instead of duplicating it.

## What this update establishes / 本轮能说明什么

这五项资源为新的页面结构提供了具体内容：构建方案需要性能反馈，验证需要明确的输入与语义合同，评测需要独立的任务和比较协议，构建知识需要来源与适用边界。它们不能共同替代完整推理引擎的端到端验证，也不能据此认定 AI 已经降低了构建和维护的总成本。

## Follow-up source inspection — 2026-10-23

[Mach X and Ignis review](source-review-2026-10-23.md) records two user-supplied execution-stack candidates, pinned revisions, dispatch/kernel evidence, upstream reuse, author benchmark boundaries and concrete checks. Both qualify as core cases; neither is treated as independent performance reproduction. This follow-up does not change the October 12 resource findings or older project review dates.
