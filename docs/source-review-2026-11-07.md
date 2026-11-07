# Source review: JITEngine and SkyDiscover / SkySynth — 2026-11-07

[Home](../README.md) · [中文首页](../README_CN.md) · [Linked case](cases.md#jitengine) · [Validation](validation.md)

Admission is based on concrete construction and execution changes, not the headline speedup. This review adds **two repositories and one linked case**: JITEngine as a specialized runtime and SkyDiscover, through SkySynth, as a construction framework. Six engine packages do not become six repository records; SkySynth is part of SkyDiscover, not a third repository.

| Repository | Inspected commit | Inspection depth |
| --- | --- | --- |
| [JITEngine](https://github.com/skydiscover-ai/jitengine) | `2c34508d617800ab7448a69e14a6dd551aec156e` | Installer and package boundaries; detailed Flash-Next M4 Pro model/expert/kernel/check path; bounded spot-checks of Qwen3.6, Flash-Next M2 scheduling and Flint M4 Pro persistent execution |
| [SkyDiscover](https://github.com/skydiscover-ai/skydiscover) | `0d932b690670a7e544388ad362e9876c8bd256a0` | Synthesis workflow, executable test admission/runner, export checks and the separate NVIDIA L4 inference task |

This was source inspection only: no upstream installation, Metal/GPU experiment, model download or agent synthesis was run. The inspection is not a complete originality audit or qualification of every package. Both repository roots declare Apache-2.0; model/checkpoint terms remain separate.

## What “generated for a model and a Mac” means

The [package overview](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/README.md) describes three models, Qwen3.6-35B-A3B, Qwen3.8-Flash-Next and Flint, each with an M2 and M4 Pro package. All six build on MLX. The [installer](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/install.sh) selects an existing package from the chosen model, chip and memory, downloads a specified checkpoint and installs that package. It does not call SkySynth to invent a new engine on each launch. Development-time synthesis, selecting a released package and runtime Metal compilation are distinct operations.

The [author's construction report](https://skydiscover-ai.github.io/blog-jitengine.html) associates these outputs with SkyDiscover's synthesis workflow. The public implementation is stronger evidence than a wrapper or API adapter, but attribution to agents does not independently establish absence of human contribution or lower total development cost. [Package relationships](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/README.md) also disclose reuse between builds. Flash-Next [credits FreeToken](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/DETAILS.md) for its expert-offload strategy; MLX arithmetic, quantized weights and model MTP heads remain upstream dependencies.

## Execution changes that support inclusion

### Flash-Next on M4 Pro: trace the selected path

1. **Integrated expert kernels.** [The model](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/model/model.py) selects `_forward_lookahead` for its eligible single-row, single-token path. [Speculative expert execution](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/model/moe/speculative.py) calls [grouped quantized Metal kernels](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/kernels/grouped_expert_qmv.py) through a device slot table. This connects custom computation to inference rather than merely publishing an unused kernel.
2. **Repair, not intentional expert dropping.** `spec_settle_begin` resolves router choices, starts missing expert transfers and detects changed slot/generation identities. `_correction` recomputes affected expert contributions; `spec_settle_finish` reconciles the completed transfers. The model queues the next layer ahead, but restores saved recurrent/PLE state and rebuilds that layer when correction invalidates provisional work. This speculative cache execution is distinct from MTP token proposals and from omitting experts for speed.
3. **A narrower lossless representation.** [Pack16](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/kernels/pack16.py) reconstructs scale/bias metadata for existing quantized experts from compact records, with escape handling and errors for unrepresentable cases. Its preservation claim concerns the already-quantized representation, not original full-precision weights. This memory-layout contribution should not be confused with training a smaller model or claiming quantization is lossless.
4. **Checks control dispatch.** [Engine initialization](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/engine/engine.py) invokes [kernel self-checks](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/kernels/selfcheck.py), records failures, disables rejected paths and can disable MTP. Checks include model-specific finite inputs and both bit-identity and bounded-error contracts; they are not a single universal equivalence guarantee.

### Other packages: bounded corroborating checks

- [Flash-Next M2 scheduling](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m2/src/jitengine_qwen3_8_flash_next_m2/scheduler/decode.py) rotates the active request after a configured decode quantum. The [engine default](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m2/src/jitengine_qwen3_8_flash_next_m2/engine/engine.py) is 64 tokens, trading shared batching for a device/SSD-specific serving policy.
- [Flint M4 Pro's runner](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/flint-m4pro/src/jitengine_flint_m4pro/kernels/runner.py) owns persistent scratch/history and compiles the Metal execution program. [Its layer implementation](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/flint-m4pro/src/jitengine_flint_m4pro/kernels/megakernel_layers.metal) contains actual fused model work. [Engine load checks](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/flint-m4pro/src/jitengine_flint_m4pro/engine/engine.py) select that backend, reject pinned configurations that fail, or fall back to stock MLX when permitted. Co-residency and barrier checks are device constraints, not universal portability.
- [Qwen3.6 M4 Pro](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.6-35b-a3b-m4pro/README.md) explicitly separates its exact profile from a faster `relaxed` profile that fails the same-output check. Flint also has an optional KV8 profile. Neither relaxed arithmetic nor KV quantization inherits the exact profile's validation contract.

These reads corroborate substantial specialization across the collection, but do not extend the detailed Flash-Next M4 audit to every kernel or serving mode in all six packages.

## What the 2.72× result actually compares

The [Flash-Next M4 Pro results](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/DETAILS.md) support the following **author-reported** comparison:

| Item | Condition / limitation |
| --- | --- |
| JITEngine | 32.9 tok/s; Flash-Next 4-bit, one user, 48 GB M4 Pro with a **40 decimal GB** budget, MTP head and pack16 present |
| Baseline | slotstream **0.2.11**, 12.1 tok/s, MTP on; measured **September 23** and not rerun on a newer version |
| Ratio | Approximately 2.72× from those two values; not a current-version, same-session retest |
| Current-build experiment | The 32.94 figure is from alternating this JITEngine build against its previous build: four pairs, medians of run medians, versus 23.83 tok/s |
| Earlier paired comparison | An earlier JITEngine build measured 21.6 versus slotstream's 12.1 in one September 23 session, approximately 1.8× |
| Budget interpretation | Smaller budgets on the M4 Pro do not emulate a smaller Mac's GPU or SSD |

The [published benchmark client](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/benchmarks/benchmark.py) measures decode from the first streamed content to stream completion and reports TTFT separately. It re-tokenizes output, bounds reported token counts and flags large count discrepancies or insufficient streaming. This is a useful protocol, not proof of a universal speedup. Other packages use different baselines, and some comparison values are attributed to an external published chart. No cross-package ranking or full request-latency gain is inferred here.

The [end-to-end gate](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/tests/e2e/test_gate.py) defaults to a fixed 512-token greedy text hash (`07a676778e3a6720`) over three repeats and checks that intended kernel paths engaged. The expected hash is configurable; a minimum speed floor is optional. Metal/checkpoint-dependent checks can skip when prerequisites are absent. Passing a CPU-only test collection would therefore not qualify this hardware path. A fixed text hash also does not certify arbitrary prompts, sampled distributions, concurrency or long-context quality.

## SkyDiscover is broader than evolutionary code search

The [root overview](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/README.md) distinguishes **Optimize**, which evolves programs against scores, from **Synthesize / SkySynth**, which constructs a system from a specification. The [synthesis workflow](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/README.md) describes planning, implementation, evaluation, criticism and audit roles, retained checkpoints and feedback. The evolutionary branch makes the AlphaEvolve comparison understandable, but it does not fully describe the workflow linked to JITEngine.

Concrete enforcement points were inspected rather than assuming a workflow description guarantees correctness:

- [The suite runner](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/workflow/scripts/suite.py) passes the selected implementation via `SKYDISCOVER_IMPL` to the task's `test.sh`. [The test command](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/workflow/scripts/run_tests.py) distinguishes passed, failed and incomplete/timeout outcomes and optionally requires release-readiness checks. Test content and whether it adequately exercises the candidate remain task responsibilities.
- [Test admission](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/workflow/scripts/validate_test.py) requires an ordinary added test to pass the reference and catch at least one mutant; a mutant timeout is not a successful catch. Supplied `--seed` tests can take the reference-only path. These rules constrain test admission, not the completeness of the oracle.
- [Export verification](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/spec/run.py) checks implementation/artifact digests and audit coverage against the checkpoint. Identity checks support traceability; relocating a verification bundle is not an operating-system sandbox or a proof of correctness.

The separate [inference example](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/examples/inference-engine/README.md) contains a task, benchmark client and prompts, not a complete generated engine or prebuilt correctness suite. [Its task](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/examples/inference-engine/task.md) specifies Qwen3-4B/BF16 on one NVIDIA L4, shared-prefix branches and separate deterministic/sampled checks. This is not the six Mac packages or evidence reproducing their results. SkySynth also offers a formal-specification/proof mode; no inspected evidence establishes that the JITEngine LLM implementations were formally proved.

## 中文结论

两项均符合收录范围：JITEngine 有实际接入模型调用链的 Metal 内核、缓存修复、状态回滚和设备专用调度；SkyDiscover 的 SkySynth 分支提供与这些产物直接关联的系统构建流程和可执行门禁。二者分别列入引擎与构建方案，并共用一个案例，目录合计 **142 个项目、83 个案例**。

“按需生成”应理解为针对模型和设备的构建过程；当前安装器选择已有版本，并非每次启动现场生成。引擎建立在 MLX 等组件上，不把继承的卸载策略或量化权重归为新发明。最高 2.72 倍为作者特定解码数据，且基线版本较早；本轮未独立复现。测试脚本、有限样本输出一致与整栈正确性／形式化证明分别记录。原有 140 条项目记录、82 个案例和核查日期保持不变。
