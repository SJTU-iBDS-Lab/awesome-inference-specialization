# Discovery pass and keyword expansion — 2026-11-08

[Home](../README.md) · [中文首页](../README_CN.md) · [Search guide / 检索指南](search-strategy.md) · [Exact queries and observations](../catalog/search_runs/2026-11-08.json)

This pass expands discovery after JITEngine / SkySynth. It searched 20 GitHub repository queries, taking one page of at most 20 results each, plus three web queries. The 400 returned GitHub observations contain **359 distinct repository names**, including existing entries, unrelated results and duplicates across queries. This is not 359 qualified candidates or an exhaustive survey; total search-result counts were not exposed by the connector.

Seven leads received official README/tree inspection and bounded source reads. **None is admitted by this discovery pass.** The catalog remains **142 projects and 83 cases**, based on commit `38bcdab22d17cfb9a2318f7d286ea4a464c1c26c`. Existing project records, case facts and review dates are unchanged. No upstream build, device benchmark, model download or agent run was performed.

## What changed in retrieval

| Observation | Keyword / route change |
| --- | --- |
| Broad `inference + synthesis` returned many TTS and image-generation repositories | Pair construction terms with `engine`, `model`, `harness` or an exact seed; keep speech synthesis in its own valid search lane |
| `specialized inference` surfaced EngineSmith; its README names Molten | Add whole-system construction vocabulary and follow framework → output links |
| JITEngine credits FreeToken; Molten identifies Lily and MLX-derived code | Follow acknowledgements, VENDORED/NOTICE and reference implementations, including older projects |
| NPU and architecture-code queries expose different device paths | Add RK3588/RKNPU2, R9700/gfx1201, gfx1151, Ascend and M5 terms, with model-specific follow-ups |
| A fork-only query mostly returned ordinary copies | Keep the fork pass, then require a concrete execution delta and upstream attribution |
| Recent-creation searches miss older active work; top pages omit relevant seeds | Run creation, recent-push and undated dependency searches separately; split saturated queries and paginate before claiming coverage |

The maintained bank now has **11 keyword groups containing 131 terms**, **12 hardware groups**, **8 model-term groups** and **20 query templates**. Hardware/model terms are retrieval variants, not equivalence or compatibility claims. Exact query observations are retained separately from the vocabulary, so unproductive broad queries remain auditable without becoming preferred templates.

## Priority source follow-ups

The following dates are GitHub repository creation dates obtained from the official API, not release or admission dates. All sources below are commit-pinned in the machine-readable run record.

### EngineSmith and Molten — construction framework and generated output

**EngineSmith**, created October 29: [README](https://github.com/EngineSmith/enginesmith/blob/4ea26f3a93286a2aa41a06edf1f9170a54569cc5/README.md) identifies a framework for constructing a native engine for one checkpoint, machine and workload, and points to Molten. The inspected [evaluator](https://github.com/EngineSmith/enginesmith/blob/4ea26f3a93286a2aa41a06edf1f9170a54569cc5/src/enginesmith/evaluate.py) separates control prompts, paired timing and teacher-forced token/rank checks. [Acceptance rules](https://github.com/EngineSmith/enginesmith/blob/4ea26f3a93286a2aa41a06edf1f9170a54569cc5/src/enginesmith/acceptance.py) can accept an aggregate, segment or case gain under configured regression limits. A pass is therefore not necessarily bit-identical output or improvement on every workload.

Next: trace the build/run controller, native-library restrictions, held-out evaluation and actual task tolerances. Its README currently limits requests to one sequence; distinguish advertised extensibility from delivered platform support. New useful terms: `engine construction harness`, `one model one machine`, `teacher forcing`, `candidate acceptance`.

**Molten**, created October 25: [README](https://github.com/zhangshuibai/molten/blob/f70658cc386964742ff3d567f02737e5db9f0ca7/README.md) describes a Rust/Metal LFM2.5-24B-A2B engine targeting M5-series Macs with an MLX-format 4-bit checkpoint. [Source spot-check](https://github.com/zhangshuibai/molten/blob/f70658cc386964742ff3d567f02737e5db9f0ca7/src/lfm.rs) shows fixed model geometry and model-owned execution/state code. [VENDORED](https://github.com/zhangshuibai/molten/blob/f70658cc386964742ff3d567f02737e5db9f0ca7/VENDORED.md) explicitly attributes adapted runtime/kernel components to Lily and MLX. No MLX runtime dependency does not mean no MLX-derived code.

Next: trace fused kernel dispatch and state tests, then compare the reported build trajectory with current EngineSmith rules and the benchmark's different weight formats. The linked framework and output are distinct artifacts; their association alone does not authorize two admissions or a claim of development-cost savings.

### FreeToken — follow the acknowledged dependency

Created July 20, so it would be missed by a November-only creation filter. [README](https://github.com/FlashML-org/FreeToken/blob/8215a94f92449c1aff07627d95ef73377363315d/README.md) describes bandwidth-adaptive CPU/GPU MoE execution and names reused projects. [CPU executor reads](https://github.com/FlashML-org/FreeToken/blob/8215a94f92449c1aff07627d95ef73377363315d/python/freetoken/moe/cpu_executor.py) show separate submit/synchronize operations, pinned activation/routing buffers and a CPU-worker handshake, with runtime-dependent graph-safety checks. [Offload-cache reads](https://github.com/FlashML-org/FreeToken/blob/8215a94f92449c1aff07627d95ef73377363315d/python/freetoken/moe/offload_cache.py) expose per-format weight banks and fused expert-copy paths.

Next: trace policy selection into model dispatch, dynamic expert/KV budgets and numerical/synchronization tests. The policy, quantized format and baseline conditions need separate checks. The JITEngine acknowledgement is a discovery edge, not proof that JITEngine and FreeToken share an implementation. Useful terms: `bandwidth-adaptive`, `CPU-GPU co-execution`, `double-buffered prefill`, `elastic VRAM`.

### InferRSI — experiment workbench, with explicit automation limits

Created October 8. [README](https://github.com/InferMatrixLab/InferRSI/blob/3a67f2456156f1071d4821e172a5bb55393f3f08/README.md) distinguishes human/agent-prepared candidates from the workbench's comparisons; automatic model-backed search and knowledge promotion remain planned. The inspected [runner](https://github.com/InferMatrixLab/InferRSI/blob/3a67f2456156f1071d4821e172a5bb55393f3f08/src/inferrsi/harness/runner.py) snapshots source around command execution. [Evaluation](https://github.com/InferMatrixLab/InferRSI/blob/3a67f2456156f1071d4821e172a5bb55393f3f08/src/inferrsi/harness/evaluation.py) checks completed trials, required checks, quality validation and source integrity; absent evidence contributes to an inconclusive decision.

Next: inspect specific campaign validators and binding to the actual executed engine. The README's B300, Ascend, video and speech results have different protocols and include externally reported engines; do not combine them into one replicated performance claim. Useful terms: `optimization workbench`, `AB/BA`, `source fingerprint`, `INCONCLUSIVE`, `knowledge reuse`.

### Saber — R9700-specific Rust/HIP execution

Created November 5; [README](https://github.com/GGZ14/saber-engine/blob/c8a1e84b39e73363495e549d480a6f6c3893800c/README.md) specifies Qwen3.8-27B and Flash-Next on gfx1201/R9700, with different TP=1/TP=2 contracts. [Forward-module reads](https://github.com/GGZ14/saber-engine/blob/c8a1e84b39e73363495e549d480a6f6c3893800c/crates/saber-exec/src/forward.rs) distinguish live versus padding GDN state slots and model/head plans. [Decode-kernel reads](https://github.com/GGZ14/saber-engine/blob/c8a1e84b39e73363495e549d480a6f6c3893800c/crates/saber-kernels/hip/mxfp4_gemm_decode.hip) contain shape-specific HIP tile/split-K implementation and identify frozen generated-code provenance.

Next: connect serving plans to selected kernel symbols, check collective ordering and DFlash2 state commits, and qualify the transformed weight packs. Kernel existence and author tok/s figures are insufficient to establish the whole served path. Useful terms: `R9700`, `gfx1201`, `kernel manifest`, `decode lanes`.

### open_rknpu2_lm_infer — RK3588 pipeline and operator-library boundary

Created October 14. [README](https://github.com/happyme531/open_rknpu2_lm_infer/blob/e1331947c00d438470e48b585f7b34d0f783f40b/README.md) identifies an open operator-library dependency and a required vendor `rknpu2` kernel driver; these are separate boundaries. The inspected [layer pipeline](https://github.com/happyme531/open_rknpu2_lm_infer/blob/e1331947c00d438470e48b585f7b34d0f783f40b/src/model/pipeline.rs) orders two lanes per layer, and [Qwen execution](https://github.com/happyme531/open_rknpu2_lm_infer/blob/e1331947c00d438470e48b585f7b34d0f783f40b/src/model/qwen35/execution.rs) connects that pipeline to layer forwards with separate scratch.

Next: trace operator submission to the NPU library and board-specific tests. Mixed W4/W8 weights, dynamic A8 activations, drafting and optional expert skipping must be separated from scheduling gains. Useful terms: `RK3588`, `RKNPU2`, `dual ubatch`, `zero-copy execution`.

### PolyStrata — distinguish its two engine boundaries

Created October 6. [README](https://github.com/simplexai-labs/PolyStrata/blob/4de79331b49e553406860470fa3e96b5256e2e50/README.md) says its Flash-Next path uses Strata's engine unchanged, while additional models use a separate poly engine. [Qwen model reads](https://github.com/simplexai-labs/PolyStrata/blob/4de79331b49e553406860470fa3e96b5256e2e50/src/poly/qwen35.cpp) show explicit GDN/attention dispatch; [kernel reads](https://github.com/simplexai-labs/PolyStrata/blob/4de79331b49e553406860470fa3e96b5256e2e50/src/poly/kernels.cu) identify llama.cpp/GGML arithmetic as a reference.

Next: compare the added execution path against Strata, trace launch selection and inspect quality/state tests. The unchanged Flash-Next path should not be counted again. Useful search routes: `derived from`, `native` plus a model name, and upstream → substantial fork.

## Existing leads and limits

Earlier unresolved leads such as Legion, Delta, AIMA and rec retain their previous review status; a new hit does not silently clear their outstanding checks. General libraries, teaching engines and packaging-only projects are not rejected merely by keyword, but still need the concrete relationship required by [CONTRIBUTING](../CONTRIBUTING.md). This run does not refresh their facts or preserve them as an alternative admitted catalog.

The GitHub sample is relevance-ranked, bounded and not a complete enumeration; the run record does not invent total-hit counts. The broad search includes irrelevant results deliberately retained as observations. Technical statements above come from official repositories, not secondary directory descriptions.

## 中文结论

本轮实际执行 20 条 GitHub 查询及 3 条网页查询，形成 7 项有源码抽查位置的优先线索。最值得补审的是 EngineSmith → Molten 的“构建框架—产物”关系，以及 JITEngine → FreeToken、Molten → Lily／MLX 的实现来源关系；Saber、RK3588 和 PolyStrata 补充硬件与深度派生路线，InferRSI 补充实验和知识复用工作台。

关键词库以机制、构建、状态、精度、负载和验证为主体，硬件／模型名作为组合维度；保留无时间限制的依赖追踪，避免只找新建仓库。候选尚未完成完整收录核查，不加入正式计数，不把作者实验描述为本轮复现。
