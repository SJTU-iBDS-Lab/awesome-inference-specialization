# Expanded source review — 2026-11-03

[Home](../README.md) · [中文首页](../README_CN.md) · [Earlier Flash-Next review](source-review-2026-11-03.md) · [Evidence policy](evidence-policy.md)

Starting main: `0b735b6520c80fa3b1f34c4e94d5e173cd2457a2` (133 records, 75 cases). This follow-up searched recent inference repositories and continued the earlier candidate queue. “New” here means **not previously admitted**, not necessarily released since the preceding review. Repository creation dates were checked separately: Strixite October 4, Spark Engine October 8, MobiInfer Android October 15, and Maya2 Native October 26, 2026.

The review adds four core cases after inspecting implementation paths. No candidate code, GPU test, model or installer was executed. Findings support inclusion and define its limits; they do not certify correctness, originality or performance.

| Project / inspected revision | Specific contribution | Retained substrate |
| --- | --- | --- |
| [Strixite, b455955](https://github.com/shawnshekari/strixite/tree/b455955a89683a16d0b71db0fd20b9f369d524d9) | Grouped HIP expert kernels and batched speculative recurrent state on gfx1151 | Qwen model, HIP, third-party HTTP/image utilities and studied engine references |
| [Spark Engine, ba66a57](https://github.com/fly9i/spark-engine/tree/ba66a57edbe6b47641f4ceb374284764a7b1b1f6) | GB10 model-specific CUDA execution and custom small-cluster RoCE collectives | libtorch/tch, cuBLAS/NCCL and ExLlamaV3 components |
| [MobiInfer Android, 2874bd6](https://github.com/IPADS-SAI/Mobiinfer-Android/tree/2874bd68102c3213e55c696d917a81806ff8bda6) | Flash-resident expert slots, lookahead loading and Hexagon host/DSP execution | llama.cpp, llama.cpp-omni/LES lineage and Snapdragon toolchain |
| [Maya2 Native / Maya3, c6b3768](https://github.com/MayaResearch/maya2-native/tree/c6b376868e268551d065c4206193e96257bef4a1) | Continuous speech batching, static codec state and fused depth-decoder kernels | PyTorch/Transformers/Triton, Qwen-derived speech model, Mimi and ECAPA |

Maya3 is the package/model name within `maya2-native`, not another repository record. Strixite and Spark Engine join the existing native-runtime reading group; MobiInfer joins expert placement and the device cross-index; Maya joins speech/audio. The first three have **text-only reviewed scope**; advertised vision/video/image paths require separate inspection.

## Strixite: integrated kernels with a limited public test boundary

[Model execution](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/runtime/qwen4exp.cpp) invokes `moe_group_routes`, grouped expert gather/SwiGLU and combine functions. [Grouped kernels](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/kernels/moe_grouped.hip) implement packed loads, BF16/F16 staging and WMMA paths, with shared-expert fusion. Their changed arithmetic and storage choices are inspectable rather than inferred from the server interface.

`forward_batch_verify` validates sequence identity and row limits, prepares per-sequence spare GDN buffers and row offsets, runs a batched forward, and marks verification pending. `keep_verify_full` swaps committed state; drop/prefix paths restore or replay the accepted portion. This is meaningful execution/state ownership beyond a model loader.

Important limits:

- The [served configuration](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/deploy/strix-server.conf) uses context extension, compressed KV and **enables a thinking nudge**. [Nudge code](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/serve/think_nudge.cpp) and low-bit weight choices must be separated from computation-preserving scheduling changes. Neither long-context speed nor task scores establish equivalence to an unmodified model.
- [Contribution notes](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/CONTRIBUTING.md) describe full kernel/reference tests run by the maintainer. That full suite is not present in the inspected public tree. Runtime guards are inspectable; author test-pass claims are not independently reproduced.
- [README](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/README.md) explicitly mentions a coding assistant. Mark `disclosed`, without inferring autonomous development, the share of generated code or lower total cost. The [third-party statement](https://github.com/shawnshekari/strixite/blob/b455955a89683a16d0b71db0fd20b9f369d524d9/THIRD_PARTY.md) is an author's provenance account, not a clean-room audit by this catalog.

## Spark Engine: Qwen call paths and the communication substrate

In the [Rust Qwen model](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/engine-rs/src/qwen/model.rs), `Moe::fwd_in` launches shared-expert projections, schedules router work on a side stream, joins it, then calls `ffi::moe_experts`. [CUDA routing](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/engine-rs/shim/qwen_moe.cu) implements softmax/top-10 with explicit tie handling and invokes the packed [EXL3 expert implementation](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/engine-rs/shim/moe_exl3.cuh). This is a model-owned execution path while still reusing substantial infrastructure.

The [C++ shim](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/engine-rs/shim/shim.cpp) initializes and gates custom collectives. [N-way RDMA code](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/engine-rs/shim/rdma_arn.cu) uses registered pinned host-mapped slots, CPU proxy posting of payload/sequence flags and GPU reductions in fixed rank order. Communication behavior is not inferred merely from a multi-GPU launch script. This substrate review does **not** qualify every advertised GLM/DeepSeek tensor-parallel route.

[Third-party notes](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/THIRD_PARTY.md) identify libtorch/tch, ExLlamaV3, CUDA libraries and NCCL; the stack is not dependency-free. [Precision switches](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/docs/qwen-switches.md) distinguish identity, rounding and stronger changes. An inspected [MoE probe](https://github.com/fly9i/spark-engine/blob/ba66a57edbe6b47641f4ceb374284764a7b1b1f6/reference/qwen38/test_kern_moe.py) prints reference error/routing/repeatability but has **no tolerance assertion**: it is diagnostic evidence, not an enforced correctness gate. The README separately reports prose versus counting, single versus aggregate decode, sampling settings and different measurement dates. We infer no cross-engine ranking.

## MobiInfer: actual routed experts remain authoritative

[Qwen MoE graph construction](https://github.com/IPADS-SAI/Mobiinfer-Android/blob/2874bd68102c3213e55c696d917a81806ff8bda6/src/models/qwen35moe.cpp) computes a next-layer router prediction for prefetch, then continues with the actual layer FFN. [Slot callbacks](https://github.com/IPADS-SAI/Mobiinfer-Android/blob/2874bd68102c3213e55c696d917a81806ff8bda6/src/llama-moe-slot.cpp) consume actual expert IDs and predictions separately, protect live mappings against late eviction and install missing required experts. The code checks type/shape and unresolved slot mappings; its phase split uses expert rank consistently across rows to avoid loading the wrong expert during multi-row verification.

[Hexagon host dispatch](https://github.com/IPADS-SAI/Mobiinfer-Android/blob/2874bd68102c3213e55c696d917a81806ff8bda6/ggml/src/ggml-hexagon/ggml-hexagon.cpp) includes shape-gated MoE matmul fusion; [DSP matmul](https://github.com/IPADS-SAI/Mobiinfer-Android/blob/2874bd68102c3213e55c696d917a81806ff8bda6/ggml/src/ggml-hexagon/htp/matmul-ops.c) supplies tiled HMX/HVX execution and asynchronous jobs. This warrants a substantial specialized-fork entry, not a claim that all inherited backend code was invented by this repository.

The [LES report](https://github.com/IPADS-SAI/Mobiinfer-Android/blob/2874bd68102c3213e55c696d917a81806ff8bda6/docs/les/lookahead-expert-scheduling.md) explicitly measures an **iPad M4**, with separate stages for loading/scheduling, mixed precision and DSpark. Its total speedup cannot be attributed solely to Android scheduling. [Android README](https://github.com/IPADS-SAI/Mobiinfer-Android/blob/2874bd68102c3213e55c696d917a81806ff8bda6/README.md) has different phone measurements and exposes expert-count controls; reducing top-k changes computation even though ordinary prefetch misses use demand loading. No blanket “lossless Android NPU” claim is made here.

## Maya2 Native: speech execution rather than model-training gains

The [engine tick](https://github.com/MayaResearch/maya2-native/blob/c6b376868e268551d065c4206193e96257bef4a1/maya3/engine.py) releases cancelled slots, admits new work, combines text prefill with active decode, runs depth decoding and emits a Mimi frame. [Static codec state](https://github.com/MayaResearch/maya2-native/blob/c6b376868e268551d065c4206193e96257bef4a1/serve/fast_codec.py) stores per-slot convolution history and attention rings so each bucket can replay a captured graph. This changes the execution/state organization, not just the API.

The [depth body](https://github.com/MayaResearch/maya2-native/blob/c6b376868e268551d065c4206193e96257bef4a1/serve/fast_depth.py) calls [Triton residual/LayerNorm and top-k sampling kernels](https://github.com/MayaResearch/maya2-native/blob/c6b376868e268551d065c4206193e96257bef4a1/serve/fast_depth_kernels.py). The [finite validation script](https://github.com/MayaResearch/maya2-native/blob/c6b376868e268551d065c4206193e96257bef4a1/maya3/tests/test_depth_fused.py) asserts sampler total variation below 0.03 on 200,000 draws from one fixed row, no probability mass outside top-k, and greedy agreement relative to an FP16/FP32 baseline on 16 hidden states with 0.05 slack. This is a concrete gate, not general distributional equivalence or an experiment run by this catalog.

[Engine documentation](https://github.com/MayaResearch/maya2-native/blob/c6b376868e268551d065c4206193e96257bef4a1/docs/ENGINE.md) identifies BF16 backbone/FP16 depth, default duration caps and EOS-boost loop guards. These alter generation relative to an unguarded full-precision target. It also labels some tables as **pre-release-checkpoint** measurements; the release README uses other results. Audio-seconds/s is aggregate produced audio duration per wall second, not tokens/s, and model/language quality improvements are not engine-only gains.

## Remaining leads and next inspection boundary

- [gr8](https://github.com/kindlingai/gr8): official README describes full GLM-5.3 on 3–6 Sparks, custom verbs collectives, context-parallel KV and remote state storage. Strong follow-up for communication/KV research; direct dispatch, state correctness and upstream format lineage still need inspection. It differs from Spark Engine's advertised **GLM-5.3-Flash** path; do not conflate model names.
- [Basalt](https://github.com/jesdga95/basalt): official README explicitly identifies a Strata fork, NVFP4 expert packs and optional peer-GPU expert tier. Trace the fork delta and residency paths before counting it separately.
- [Delta Inference Engine](https://github.com/musicurgy/delta-inference-engine): official README identifies a Windows port of Xolotl/Strata. It also documents a default resident-expert route bias, so advertised throughput includes a changed routing contract. A separate entry needs a demonstrated execution delta beyond packaging/portability.

Other search hits were discovery results, not source-reviewed candidates or rejected projects. AIMA and the earlier unresolved leads retain their existing follow-up status. No new claims of exhaustive coverage are made.

## Catalog maintenance / 目录维护

Counts become **137 records and 79 cases**. Added four bilingual entries/cases, pinned evidence and mechanism memberships; extended the existing device cross-index for mobile expert placement. The previous 133 records, 75 cases, summaries and source-review dates are preserved. Only four new repository star observations were added. No homepage redesign, new primary category or reclassification of unrelated entries.

Validation covers catalog/schema consistency, ten generated views, all 66 existing repository tests, old-record preservation, pinned-path existence and `git diff --check`. These are catalog checks, not upstream execution tests.

本轮补入四项：395 原生执行、GB10 模型与通信执行、Android 专家卸载、流式语音执行。特别保留默认思考／EOS 干预、专家数削减、低精度、私有测试与仅打印误差的诊断脚本等限制。对 DGX Spark 和 KV／专家搬移研究，Spark Engine、gr8、MobiInfer 值得继续逐项复现实验；这里的收录不代表已有独立性能结论。
