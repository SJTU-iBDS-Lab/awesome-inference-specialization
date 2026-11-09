# Quail: query-aware inference / 查询驱动的专用推理

[Home](../README.md) · [中文首页](../README_CN.md) · [Catalog](catalog.md#quail) · [Case](cases.md#quail) · [Updates](updates.md)

Reviewed on **2026-11-09**, against catalog baseline `43bd84a483fd07a99b0070b24e5822bbd186605c`. Quail was absent from the catalog. This review admits **one engine and one case**, bringing the catalog to **143 projects and 84 cases**. QUAIL-B is inspected as supporting evaluation evidence, without a separate admission decision.

## Decision and revisions

**Admit Quail as a core system, with computation reuse as its primary mechanism family.** Its query planner, physical operator execution, KV ownership and fused forward path materially change execution. Reusing vLLM's loader and model modules does not make this merely a SQL/API wrapper.

| Source | Reviewed revision / boundary |
| --- | --- |
| [Quail](https://github.com/fsdatalab/quail) | `4072f9b61e3a2f435b0bb65fc8d91469b7d3a591`; planner-to-runtime trace, Qwen3 forward/attention path, KV state and selected validation code |
| [QUAIL-B](https://github.com/fsdatalab/quail-bench) | `2a883383c8062e0aa522b9e0cf4da8db64ffb16b`; token/time accounting and scoring contract, not execution of its suite |
| [CMU launch report](https://fsdatalab.github.io/blog/introducing-quail/) and [Modal report](https://modal.com/blog/quail-billion-tpm) | Both dated **2026-09-24**; historical author measurements, not measurements of the reviewed November revisions |

The user-supplied article supplied the lead. Two web probes (`Modal Quail inference engine billion tokens minute H100`, `Quail Full Stack Data Lab github AI SQL inference`) and a direct official-repository lookup resolved its identity. This is a targeted follow-up, not an exhaustive search pass. MIT licensing is explicit in the pinned [LICENSE](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/LICENSE).

## Execution evidence

| Boundary | Inspected implementation | Contribution and limit |
| --- | --- | --- |
| Query planning | [Join search](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/planner/search/join_order.py), [backend lowering](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/lowering.py) | Searches operator order and anchor orientation using estimated survivors and reusable KV; lowers to physical nodes with tokenized questions and answer IDs. The join cost model assumes unlimited reuse for its lower-bound estimate; finite HBM still causes recomputation. |
| Operator execution | [Filter](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/operators/filter.py), [join](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/operators/join.py), [stage executor](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/stage_executor.py) | Groups predicates and partner requests around document/anchor state, carries prefix trees into shared scheduling, and feeds packed work into the model pipeline. This is execution control below the SQL interface. |
| KV lifetime | [Arena](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/arena.py), [retention](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/retention.py) | Allocates, pins, borrows, rewinds and frees pages. Join completion retains reusable document prefixes; future uses and surviving rows influence retention. Borrowers hold pages until release. Reuse requires valid token positions and state. |
| Model and kernel integration | [Qwen3 pipeline](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/models/qwen3.py), [attention and Triton kernels](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/attention.py) | The forward loop calls fused normalization/quantization, Q/K normalization/RoPE and activation/quantization. `attention_tree` computes causal suffix attention and grouped reads of retained KV, then merges softmax states and optionally quantizes. The ordinary join path composes existing attention calls with custom packing/merge kernels; it is not a wholly new attention primitive. |
| Bounded answer head | [Readout](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/readout.py), [model loading](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/executor/model_loading.py) | `AnswerRows` selects TRUE/FALSE token variants and compares their best logits. Boolean operators can answer directly from prefill. Restricting the output vocabulary defines a classification task, not equivalence to unconstrained text generation. Other readouts have different contracts. |

Upstream reuse is explicit: vLLM supplies processed model modules/loading and kernel utilities; DeepGEMM and device-selected FlashAttention implementations perform major GPU operations. SQLGlot and Arrow supply frontend/data components. Hydragen and SpecInfer are algorithmic precedents cited by the authors; citation alone does not establish copied code. The current [backend](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/quail/backends/quail/backend.py) pins a vLLM runtime dependency separately from the launch benchmark version.

The inspected Qwen3 path uses an existing checkpoint, including its FP8 representation. Scheduling, fusion and KV reuse are engine contributions; FP8 accuracy, prompt arrangement and output restrictions require their own controls. No new training is needed for this path, and no claim about all newer model paths follows from that observation.

## Performance evidence and counting

The launch report compares Qwen3 4B FP8 with BF16 KV on one H100, using matching prompts and planner-selected order for both engines. Its 29-query, scale-factor-0.1 geometric mean is **1.84×** over stock vLLM; BIO-4 at scale factor 1.0 reaches **14.04×** and **19.03 million requested input tokens/s**. These are author results. The reported AGENT-1 counterexample takes **2.32×** as long as vLLM. They do not establish performance of the November code.

The pinned [metric contract](https://github.com/fsdatalab/quail-bench/blob/2a883383c8062e0aa522b9e0cf4da8db64ffb16b/quail_b/reporting.py) and [calculation](https://github.com/fsdatalab/quail-bench/blob/2a883383c8062e0aa522b9e0cf4da8db64ffb16b/quail_b/run.py) separate:

- **Requested input tokens:** full lengths of evaluated prompts, including positions served from retained KV. Throughput divides this count by query time. Thus the billion-token headline is neither output generation nor a billion newly computed token positions.
- **Fresh tokens:** positions actually processed by forward passes, reported by the engine. **Minimum tokens** estimates distinct required prefixes with unlimited KV; their difference is KV regret. Missing evidence remains unavailable rather than zero.
- **Cost/time:** query GPU time is distinct from model startup, result collection, scoring and saving. A per-token GPU cost is not total deployment or development cost; adapter timing boundaries must be checked for each run.

No raw historical benchmark execution was reproduced here. The current benchmark README describes **85 queries**; do not silently substitute that suite for the launch report's 29 queries.

## Current code versus launch limitations

The [current README](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/README.md) includes classification, scoring, extraction and `AI.MAP`, as well as additional models and GPUs. Therefore **prefill-only describes the reviewed Boolean workload, not every operation in the current engine**. SQL dialect spellings do not establish complete compatibility with the corresponding hosted database services.

Current filter/join execution passes a prefix tree into the stage executor. The [resident-prefix test](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/tests/engine/test_stage_resident_prefix.py) exercises borrowing shared document prefixes. The old missing-cross-row-prefix explanation remains a historical benchmark finding; it is not a current blanket limitation. Source support does not establish that the AGENT-1 regression has disappeared: that needs a new controlled run.

## Construction and validation

The CMU report explicitly discloses heavy AI coding-agent use, including fused-kernel construction. This supports **`ai_involvement=disclosed`**, without establishing autonomous whole-system synthesis, a particular agent framework, human effort saved or total construction cost.

The [hash-model KV checker](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/tests/helpers/kv_checker.py) replaces neural computation with token/position/history hashes. Reads from wrong pages or invalid histories fail its expected-answer lookup. [Rewind tests](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/tests/engine/test_stage_rewind.py) and resident-prefix tests check stage behavior, work accounting and final ownership. These are useful state-machine checks, not GPU floating-point or task-accuracy proofs.

A separate [hybrid join parity probe](https://github.com/fsdatalab/quail/blob/4072f9b61e3a2f435b0bb65fc8d91469b7d3a591/experiments/cells/hybrid_join_parity.py) records TRUE/FALSE margin errors and bit agreement against vLLM. Its introductory numerical predictions are not enforced pass/fail assertions in the inspected reporting path. Do not present them as passed acceptance gates. QUAIL-B reference-answer agreement also depends on which rows/pairs were evaluated and on the reference labels.

This review ran **no Quail build, GPU test, benchmark or agent workflow**. Remaining evaluation needs include matched revisions/checkpoints, prompt layout, quality, cold/warm state, concurrency and per-operator numerical coverage. Maintenance follows model layouts, vLLM interfaces, device kernels and KV rules; comparable development and maintenance costs remain unknown.

## 中文结论

应收录。已追踪查询规划到算子调度、KV 回退／保留、Qwen3 前向与融合内核的实际调用链，具有实质执行改造；vLLM、DeepGEMM、FlashAttention 等复用来源明确。收录不以速度宣传为依据。

标题吞吐量包含缓存复用的完整输入长度，不能与输出生成速度或实际新增计算量混用。作者旧版基准与本次源码版本分开记录；当前已有前缀共享与生成类算子，不能照搬“永远只有 prefill”“仍无跨行缓存”的说法。AI 编程参与有直接披露，但节省了多少开发成本仍未知。本次只完成源码和证据核查，未独立复现性能。
