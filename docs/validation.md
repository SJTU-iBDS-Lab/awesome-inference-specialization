# Correctness and quality validation / 正确性与质量验证

[Engines](systems.md#system) · [Construction](systems.md#construction) · **Validation** · [Benchmarks](benchmarks.md) · [Supporting resources](resources.md)

Validation is a central subject: **what evidence allows a constructed execution path to be accepted, and at what checking cost?** This guide indexes methods embedded in engines, construction workflows and evaluators. A method does not need a separate repository to matter, and listing it here does not add another project to the catalog.

A validation method defines a reference or oracle and an acceptance decision. A [benchmark](benchmarks.md) supplies tasks and a comparison protocol; it may incorporate several such methods. Keep these responsibilities separate. The methods below were source-inspected on **2026-10-12**; they were not executed or independently reproduced here.

## Four contracts to distinguish

| Contract | Evidence sought | What a passing check cannot establish |
| --- | --- | --- |
| **Operator / subgraph numerics** | Compare candidate outputs with a trusted reference under explicit shapes, layouts, dtypes and tolerances; include mutation and invalid-access checks where available | Whole-model quality, untested shapes, correct persistent state, or service behavior |
| **Composed model and state** | Compare the assembled forward path; separately inspect prefill/decode, caches, reset, batching and multi-step state transitions | Passing individual kernels is insufficient; a forward-only test does not cover a stateful service |
| **Generated-output quality** | Evaluate the intended output contract: text accuracy, image/video perceptual quality, speech quality, or task behavior, including admitted approximation | Perceptual similarity or an LLM verdict does not prove numerical or distributional equivalence |
| **Service and integration** | Check loading, readiness, requests/responses, error paths and execution of the intended candidate | A healthy API and plausible output do not prove reference parity, concurrency safety or production reliability |

These contracts overlap, but none automatically subsumes the others. Select checks according to what changed: a new layout, a quantized representation, a reused denoising feature and a reconstructed request scheduler create different obligations.

## Source-backed methods

<a id="numerical"></a>

### Reference checks and evaluation integrity

[KernelBench](catalog.md#kernelbench) supplies reference-based candidate evaluation. Its [evaluation guide](https://github.com/ScalingIntelligence/KernelBench/blob/main/EVAL.md) also identifies ways generated candidates can exploit an evaluator, and links adversarial tests for cached reference computations, input mutation and alternate CUDA streams. These are relevant when validation is inside an automated optimization loop. The defenses are explicitly evolving; they do not certify every submitted kernel.

[FastKernels](catalog.md#fastkernels) connects candidate replacement with [four integration levels](https://github.com/Snowflake-AI-Research/fastkernels/blob/main/README.md): individual kernels, fused operations, layers/blocks and complete pipelines. Its [benchmark runner](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/fastkernels/bench.py) and [end-to-end evaluator](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/fastkernels/eval.py) are separate inspection points. Check the actual selected task and acceptance rule; an operator result must not be reported as evidence about every deployed pipeline.

[Atrex-Bench](catalog.md#atrex-bench) embeds an [operator correctness evaluator](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/src/atrex_bench/eval/correctness.py) that checks output structure and numerical differences, declared input mutation and unexpected side effects. This makes the input/output contract more explicit than output timing alone. Coverage still depends on the supplied input generators, shapes and tolerances; it does not establish whole-model quality or arbitrary-input correctness. The project remains counted under benchmarks, while its checking method is indexed here.

<a id="model-state"></a>

### Composition checks after local generation

[KernelAgent](catalog.md#kernelagent) composes generated subgraph kernels into a forward program. The inspected [composition implementation](https://github.com/meta-pytorch/KernelAgent/blob/main/Fuser/compose_end_to_end.py) requests a reference self-test and can run the candidate when `--verify` is enabled. Verification is optional in this path; generating the file is therefore not itself evidence that it passed. The resulting finite check concerns the composed program and supplied inputs, not general equivalence or complete serving behavior.

For a stateful engine, add explicit evidence about cache ownership, sequence isolation and repeated execution. This guide does not infer that coverage from KernelAgent's forward composition check.

<a id="quality"></a>

### Perceptual quality when optimization changes outputs

[Sol-Engine](cases.md#sol-engine) combines model-specific video optimizations with output-quality checks. Its [LPIPS evaluator](https://github.com/NVlabs/Sana/blob/sol-engine/tools/vision/lpips_judge.py) compares paired baseline/candidate frames and records aggregate and per-frame distances. Video inputs are sampled; unequal frame counts can yield comparison of only the common prefix. Missing dependencies or failed scoring produce an unavailable result, not a pass.

This is a quality signal for sampled frames, not an equivalence proof or a complete assessment of temporal consistency and prompt adherence. Record the frame selection, reference configuration, metric availability and acceptance threshold alongside the [workflow's other checks](https://github.com/NVlabs/Sana/blob/sol-engine/site_docs/agent-workflow.md).

<a id="service"></a>

### Service-level functional oracles

The inspected [MetaInfer inference-framework oracle](https://github.com/MetaInfer/MetaInfer/blob/b3f6505a11ab704ee1cfb68e9c1b2c13c95ac890/metainfer/tasks/gen_infer_framework/orchestrator/oracles/correctness.py) starts `serve.sh`, waits for readiness, sends configured prompts and judges responses. It supports LLM judging and a heuristic fallback; its report records the judge mode. The implementation distinguishes hard checks from soft results when aggregating acceptance.

This supplies functional and integration feedback to the construction loop. It does **not** compare internal tensors or establish numerical equivalence with a reference engine. This description concerns the pinned `gen_infer_framework` path, not every MetaInfer task or its earlier paper snapshot. See [the workflow/output case](cases.md#vibeqwen) for the separate evidence about VibeQwen.

## Validation during sustained engine evolution

[SEIS](cases.md#seis) is an additional case, not another name for the checkers above. The [paper](https://arxiv.org/html/2610.04646v1) describes how researchers revised evaluation after some candidates passed existing gates while restricting vocabulary, mishandling termination or misusing state. Those failed candidates must not be confused with the reported best engine. Numerical and task checks cover different contracts; the public ten-trial driver is not proof that every paper gate and synchronized-chain experiment is reproduced by that artifact.

SEIS 补充的是持续改写引擎时验证规则如何暴露缺口的案例。论文中的失败候选与最佳引擎应分开；研究者修订验证规则，不等于 Agent 已自主解决验证。公开十轮示例与论文实验的范围分别见[案例记录](cases.md#seis)。

## Construction-time checks: additional evidence

[AutoMegaKernel](cases.md#automegakernel) checks a typed schedule and its dependency/counter structure before device execution. The [inspected validator](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/schedule/ir.py) assumes a trusted VM and supported IR, and some data-hazard checks have a task-count cap. Static checking and empirical reference agreement do not establish a mechanized whole-stack proof.

The [ForgeMegakernel paper](https://arxiv.org/html/2609.12379v1) adds intermediate KV/logit comparisons, poisoned future-KV probes and per-lane-position checks. This is paper evidence rather than source-inspected validation tooling: an official implementation was not established in this review. A finite oracle and source scan should not be described as an unconditional correctness guarantee.

[VibeServe / VibeSys](cases.md#vibeserve) separates candidate construction from target-specific measurement. The [current host wiring](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/src/vibesys/core_wiring.py) records evaluator/workload/environment identities and configured measurement gates; identities help trace evidence but do not prove the adequacy of those gates.

本节补充三种不同边界：受限 IR 的静态检查、论文提出的中间状态检验、构建框架对验收流程和结果来源的管理。未运行这些上游验证，也不把缺少源码的论文方案称为已检查的实现；首页原有四类验证入口保持不变。

## Embedded numerical and state checks — November 2026

These are methods inside existing engine records, not additional validation-tool projects. See the [source review](source-review-2026-11-05.md) for inspection scope.

- **Basalt:** [NVFP4 prefill tests](https://github.com/jesdga95/basalt/blob/dc047a77beeddf1e91234d983a91d6bf929e9619/tests/cuda/prefill_fp4_test.cpp) distinguish same-A4-rounding kernel parity (gate/up RMS <=1e-5, down <=1e-4) from approximation against unrounded arithmetic (layer RMS <=0.2). Grouping and optional peer checks test composition. The [teacher-forced KL implementation](https://github.com/jesdga95/basalt/blob/dc047a77beeddf1e91234d983a91d6bf929e9619/include/basalt/program/ppl_gate.hpp) omits base log-probability <=-16 terms; its [256-token prompt / positions 256–510 protocol](https://github.com/jesdga95/basalt/blob/dc047a77beeddf1e91234d983a91d6bf929e9619/docs/precision/quality.md) does not cover long-context sparse selection or W4A4 prompt execution. An interval including zero in an author ablation is not a universal equivalence proof.
- **gr8:** [Trellis codebook tests](https://github.com/kindlingai/gr8/blob/35a8f1c771991a87b0c6308006b74ce70faf0378/engine/kernels/tests/tr3_e4m3_test.cu) enumerate codebook states, compare fixed hashes across implementations and check random packed tiles. [Pool-stash checks](https://github.com/kindlingai/gr8/blob/35a8f1c771991a87b0c6308006b74ce70faf0378/engine/runtime/s2/tests/pool_stash_test.cpp) model token rows on two host ranks to assert restore/order/digest contracts; they do not execute GPU attention or RoCE. Shared-step and solo output need distinct references.

以上测试均仅审阅源码、未在本次执行。相同量化舍入下的内核一致性、有限样本质量与缓存状态恢复是不同验收合同；不能合并成整栈无损或性能已验证结论。

## Generated Mac engines and synthesis gates — 2026-11-07

[JITEngine / SkySynth](cases.md#jitengine) adds two linked validation boundaries; the [pinned review](source-review-2026-11-07.md) traces their integration.

- **Engine loading and output:** Flash-Next M4 Pro [kernel self-checks](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/src/jitengine_qwen3_8_flash_next_m4pro/kernels/selfcheck.py) use finite model-specific reference comparisons and control kernel fallback/disable paths. The [end-to-end gate](https://github.com/skydiscover-ai/jitengine/blob/2c34508d617800ab7448a69e14a6dd551aec156e/engines/qwen3.8-flash-next-m4pro/tests/e2e/test_gate.py) combines a configurable fixed greedy text hash over three repeats with checks that intended paths engaged. Its speed floor is optional; missing Metal/checkpoints can skip hardware tests. Exactness concerns the stated quantized reference, not full-precision weights or every serving mode.
- **Construction-loop integrity:** SkySynth's [test-admission script](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/workflow/scripts/validate_test.py) requires ordinary new tests to pass a reference and catch a mutant; timeouts do not count as a catch and seed tests have an exception. [The runner](https://github.com/skydiscover-ai/skydiscover/blob/0d932b690670a7e544388ad362e9876c8bd256a0/skydiscover/synthesize/workflow/scripts/run_tests.py) distinguishes failure from unavailable/incomplete checks, with optional release gates. Task-defined tests remain the oracle; the separate formal-proof path does not certify JITEngine.

本轮仅检查源码，未运行上述门禁。加载自检、有限输出回归、候选审计与形式化证明是不同证据；测试框架的存在不等于所有模型、设备和状态轨迹已经通过验证。

## Query-aware KV state and metric contracts — 2026-11-09

[Quail](cases.md#quail) adds a state-machine oracle distinct from a model-quality benchmark; see the [pinned review](source-review-2026-11-09.md).

- **KV history:** its [hash-model checker](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/tests/helpers/kv_checker.py) tracks tokens, positions and attended history through physical pages. [Rewind](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/tests/engine/test_stage_rewind.py) and [prefix-borrow](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/tests/engine/test_stage_resident_prefix.py) tests check expected histories, work accounting and final ownership. A synthetic forward model can expose wrong state reads without certifying GPU numerics or task accuracy.
- **Diagnostic versus gate:** the [hybrid join parity experiment](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/experiments/cells/hybrid_join_parity.py) records logit-margin errors and Boolean agreement against vLLM. The stated numerical predictions are not enforced acceptance assertions in its reporting path.
- **Measurement integrity:** [QUAIL-B's metric contract](https://github.com/fsdatalab/quail-bench/blob/2a883383c8062e0aa522b9e0cf4da8db64ffb16b/quail_b/reporting.py) distinguishes requested input lengths including KV hits, engine-reported fresh tokens and repeated work above an unlimited-KV minimum. Reference-answer agreement is conditional on evaluated rows/pairs, not proof of universal quality. Source inspection here does not constitute a separate benchmark admission.

上述检查仅审阅源码，未运行；验证成本未量化。缓存状态正确、神经网络数值一致、任务标签一致与吞吐量计数是不同合同，不能互相替代。

## Efficient validation: an open research question

Automation alone does not establish efficiency. A useful report accounts for candidate compilation, reference runs, device time, judge calls, human review and failed attempts. It must also state what coverage was reduced to save that cost.

A practical investigation can compare staged checking: inexpensive build/shape checks first, local numerical tests next, composed execution and state tests after integration, then representative quality and service workloads. Reuse of reference outputs needs a valid key covering model revision, weights, precision, inputs and configuration. Changing these conditions invalidates the evidence unless reuse is justified.

The question is whether a method catches relevant failures at lower cost **for the same stated acceptance contract**. Fewer samples, looser tolerances or a weaker oracle change that contract. The inspected examples above expose mechanisms and coverage boundaries; this repository has not measured their relative validation cost.

## What to record when adding a method

- **Object and change:** kernel, model program, stateful engine or service; exact intended preservation versus admitted approximation.
- **Oracle and acceptance:** reference revision, inputs, tolerance, quality threshold or judge; handling of missing checks and infrastructure failures.
- **Coverage:** supported models, devices, shapes, dtypes, trajectories and service modes; omitted or optional checks.
- **Cost:** measured checking time, compute, reference/judge calls and human work; mark unavailable data as unknown.
- **Integrity and reproducibility:** isolation from candidate edits, task visibility, retained results, failure examples and independent reproduction status.

Follow the [evidence policy](evidence-policy.md). Add a standalone `validation` catalog record when the checker itself is a distinct contribution; otherwise keep its containing project in its main role and link the relevant method here.
