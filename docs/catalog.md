# Project catalog / 项目全目录

> Generated from [projects.csv](../catalog/projects.csv); edit the CSV, then run the generator.

[Home](../README.md) · [中文首页](../README_CN.md) · [Systems & construction](systems.md) · [Comparison](comparison.md) · [Taxonomy](taxonomy.md) · [Evidence policy](evidence-policy.md)

102 entries. Source review: 2026-10-12. Descriptions report inspected mechanisms; no project benchmark was independently reproduced in this survey.

Use the family links below, or search this page for a model, device, mechanism or project. Source visibility is not a license or correctness certification. Semantic labels identify evaluation obligations, not proven equivalence.

[Data residency & movement](#memory) · [Numerical representation](#precision) · [Selective computation](#selection) · [Computation reuse](#reuse) · [Generation order](#decoding) · [Parallelism & scheduling](#serving) · [Compiled & native execution](#execution) · [Construction & validation tools](#construction)

<a id="memory"></a>

## Data residency & movement / 数据驻留与搬移 (11)

**What stays close to compute?** Place, page, prefetch or offload weights, experts and KV state.

<a id="zero-inference"></a>

### [DeepSpeed ZeRO-Inference](https://github.com/deepspeedai/DeepSpeedExamples)

[adjacent](systems.md#adjacent) · `system` · `backend` · `text` · **public code**

**Survey relevance:** Historical layerwise offload route: establishes that heterogeneous specialized execution predates recent coding agents.

Hosts weights in CPU or NVMe memory and streams them layer by layer to GPU, using prefetch and large token batches to amortize transfer costs while preserving GPU memory for activations.

**Scope:** Models exceeding GPU memory and throughput-oriented workloads that tolerate large batches or sequences motivate layerwise offload and transfer/computation overlap.

**Boundary:** ZeRO-Inference is a throughput-oriented offload path within DeepSpeed; the published KV-offload example requires model-specific changes and a Transformers fork, and capacity does not imply low interactive latency.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `layer-weight-streaming`, `layer-prefetch`, `throughput-batching`.

**Constraints:** `memory`, `workload`, `hardware`.

**Evidence:** [Source 1](https://www.deepspeed.ai/2022/09/09/zero-inference.html) · [Source 2](https://github.com/deepspeedai/DeepSpeedExamples/blob/HEAD/inference/huggingface/zero_inference/README.md) · [Source 3](https://github.com/deepspeedai/DeepSpeedExamples/blob/HEAD/inference/huggingface/zero_inference/run_model.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="fiddler"></a>

### [Fiddler](https://github.com/efeslab/fiddler)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** Heterogeneous MoE execution route: compare CPU expert computation with transfer-centric designs.

Executes uncached MoE experts on CPU by transferring small activations instead of moving their large weights to GPU, while keeping selected experts resident on GPU.

**Scope:** Small-batch local Mixtral-8x7B inference and GPU memory smaller than the unquantized model make activation transfer cheaper than expert-weight transfer.

**Boundary:** The official prototype is limited to 16-bit Mixtral-8x7B and relies on PyTorch CPU expert execution; the README explicitly calls out poor CPU performance without AVX512.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `heterogeneous-execution`, `activation-transfer`.

**Constraints:** `model`, `memory`, `workload`, `hardware`.

**Evidence:** [Source 1](https://github.com/efeslab/fiddler/blob/HEAD/README.md) · [Source 2](https://github.com/efeslab/fiddler/blob/HEAD/src/fiddler/infer.py) · [Source 3](https://github.com/efeslab/fiddler/blob/HEAD/src/fiddler/mixtral.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="flash-moe"></a>

### [Flash-MoE](https://github.com/danveloper/flash-moe)

[core](systems.md#core) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** A model-specific implementation links disclosed AI-assisted construction to SSD expert streaming and explicit approximation choices.

Streams selected quantized expert blobs with parallel pread and executes a fixed Qwen hybrid-attention pipeline using custom Metal dequantization and fused expert kernels.

**Scope:** The implementation targets Qwen3.5-397B-A17B on Apple unified-memory hardware with SSD capacity far exceeding RAM and fixed model geometry.

**Boundary:** The source states the model has ten active experts but the executable uses K=4, so its reported speed is not an equivalent top-10 baseline; the README also reports broken tool JSON for its 2-bit mode.

**Semantic considerations:** reduced precision, selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `ssd-expert-streaming`, `packed-low-bit`, `kernel-fusion`.

**Constraints:** `model`, `hardware`, `memory`, `precision`, `sparsity`.

**Evidence:** [Source 1](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/CLAUDE.md) · [Source 2](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/metal_infer/infer.m) · [Source 3](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/metal_infer/shaders.metal).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `initial`.

</details>

<a id="flexllmgen"></a>

### [FlexLLMGen (FlexGen)](https://github.com/FMInference/FlexLLMGen)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Throughput-oriented offload route: a comparison for existing memory scheduling and workload trade-offs.

Uses a block generation schedule and GPU/CPU/disk tensor placement to reuse layer weights across microbatches while overlapping transfers and optionally compressing weights and KV state.

**Scope:** Throughput-oriented workloads with large effective batches, limited GPU memory and available host/SSD capacity expose the latency–throughput trade-off.

**Boundary:** This is an OPT-centric throughput/offload implementation, not evidence of interactive low-latency performance for arbitrary contemporary models; the repository is now named FlexLLMGen.

**Semantic considerations:** layout / scheduling, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `tensor-tiering`, `weight-reuse-schedule`, `io-compute-overlap`, `low-bit-compression`.

**Constraints:** `memory`, `workload`, `hardware`.

**Evidence:** [Source 1](https://github.com/FMInference/FlexLLMGen/blob/HEAD/README.md) · [Source 2](https://github.com/FMInference/FlexLLMGen/blob/HEAD/flexllmgen/flex_opt.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="ktransformers"></a>

### [KTransformers / kt-kernel](https://github.com/kvcache-ai/ktransformers)

[core](systems.md#core) · `system` · `backend` · `text` · **public code**

**Survey relevance:** A substantial heterogeneous backend provides a core case for rebuilding execution while retaining shared serving infrastructure.

Runs memory-heavy MoE experts through ISA-specific CPU kernels and NUMA-aware placement while integrating with GPU serving runtimes for the remaining model computation.

**Scope:** CPU AMX/AVX capabilities, NUMA topology, GPU memory and expert precision constrain the heterogeneous placement and execution backend.

**Boundary:** The current repository exposes kt-kernel inference and separate fine-tuning capabilities; legacy YAML-injection examples and training speedups should not be generalized to its current serving path.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `heterogeneous-execution`, `numa-placement`, `cpu-isa-kernels`.

**Constraints:** `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/kvcache-ai/ktransformers/blob/HEAD/README.md) · [Source 2](https://github.com/kvcache-ai/ktransformers/blob/HEAD/kt-kernel/README.md) · [Source 3](https://github.com/kvcache-ai/ktransformers/blob/HEAD/kt-kernel/operators/amx/moe.hpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="moe-infinity"></a>

### [MoE-Infinity](https://github.com/EfficientMoE/MoE-Infinity)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Expert-offload route: compare established prefetch and residency policies with separately reconstructed runtimes.

Offloads expert weights to host memory and SSD, retains hot experts in an activation-aware GPU cache and uses trace/prediction-driven prefetching through a native transfer engine.

**Scope:** Sparse expert activation, per-model offload stores, GPU-memory budgets and model-specific resident tensors constrain caching and transfer decisions.

**Boundary:** The public HuggingFace-friendly implementation differs from the paper system; some configuration flags are reserved or scaffolded and DeepSeek MLA does not automatically use FlashInfer acceleration.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-tiering`, `activation-aware-cache`, `expert-prefetch`.

**Constraints:** `sparsity`, `memory`, `hardware`, `model`.

**Evidence:** [Source 1](https://github.com/EfficientMoE/MoE-Infinity/blob/HEAD/README.md) · [Source 2](https://github.com/EfficientMoE/MoE-Infinity/blob/HEAD/ARCHITECTURE.md) · [Source 3](https://github.com/EfficientMoE/MoE-Infinity/blob/HEAD/docs/configuration.md) · [Source 4](https://github.com/EfficientMoE/MoE-Infinity/blob/HEAD/moe_infinity/memory/expert_prefetcher.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="mooncake"></a>

### [Mooncake](https://github.com/kvcache-ai/Mooncake)

[foundation](systems.md#foundation) · `support` · `backend` · `text` · **public code**

**Survey relevance:** Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence.

Provides a transfer engine and distributed store for moving and retaining KV data across accelerators, host memory and storage.

**Scope:** Disaggregated inference and distributed KV storage

**Boundary:** The published transfer/store components and a complete serving deployment are different artifacts; transport and hardware configuration remain workload-dependent.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `kv-transfer`, `tiered-kv`, `prefill-decode-disaggregation`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/kvcache-ai/Mooncake/blob/main/README.md) · [Source 2](https://github.com/kvcache-ai/Mooncake/blob/main/mooncake-transfer-engine/src/transfer_engine.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="nixl"></a>

### [NIXL](https://github.com/ai-dynamo/nixl)

[foundation](systems.md#foundation) · `support` · `backend` · `text` · **public code**

**Survey relevance:** Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence.

Exposes asynchronous point-to-point transfers through pluggable transports over host/device memory and storage.

**Scope:** Inference data transfers across heterogeneous memory and storage

**Boundary:** Transport infrastructure does not decide cache admission or serving placement by itself; the documented platform is Linux.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `asynchronous-transfer`, `tiered-memory`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/ai-dynamo/nixl/blob/main/README.md) · [Source 2](https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="strata"></a>

### [Strata](https://github.com/Niko1221/Strata)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A narrow MoE runtime makes expert placement and execution choices inspectable; AI authorship is not established.

Keeps attention and hot experts on GPU, computes nonresident experts on CPU concurrently, and budgets GPU/RAM/file tiers for experts and long-context KV state.

**Scope:** The Qwen3.8-Flash-Next model family, supported quantized layouts, consumer GPU VRAM and CPU memory/bandwidth define expert residency and transfer-versus-compute choices.

**Boundary:** The documented route-tail-skip path is enabled by default in eligible CUDA and some HIP configurations and drops low-ranked missed experts; CPU/GPU rounding and changing residency can also change outputs.

**Semantic considerations:** configuration-dependent, selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-tiering`, `heterogeneous-execution`, `kv-tiering`, `approximate-expert-skipping`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/README.md) · [Source 2](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/docs/DETAILS.md) · [Source 3](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/src/core/expert_cache.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="vattention"></a>

### [vAttention](https://github.com/microsoft/vattention)

[foundation](systems.md#foundation) · `support` · `backend` · `text` · **public code**

**Survey relevance:** Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence.

Uses CUDA virtual memory to decouple contiguous virtual KV tensors from physical allocation, retaining conventional attention-kernel interfaces.

**Scope:** Growing KV state with contiguous virtual address requirements

**Boundary:** The artifact includes Sarathi integration and experiments with modified UVM support; page-size and driver assumptions affect deployability.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `virtual-kv`, `cuda-virtual-memory`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/microsoft/vattention/blob/main/README.md) · [Source 2](https://github.com/microsoft/vattention/blob/main/sarathi-lean/sarathi/worker/cache_engine/vATTN_cache_engine.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="vllm"></a>

### [vLLM](https://github.com/vllm-project/vllm)

[foundation](systems.md#foundation) · `support` · `runtime` · `text` · **public code**

**Survey relevance:** General-engine baseline and reusable execution components for controlled comparisons with specialized stacks.

Manages attention state as pooled KV blocks with reference-counted prefix sharing and schedules token-budgeted work across requests, allocating cache slots as execution advances.

**Scope:** Variable request lengths, overlapping prompts, finite KV capacity and layer-specific attention/state layouts determine block ownership and admission.

**Boundary:** Paged KV management is one subsystem in a broad runtime; prefix reuse requires matching cache identity, and hybrid attention/state models need distinct cache rules rather than a universal layout.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `paged-kv`, `prefix-reuse`, `continuous-batching`.

**Constraints:** `memory`, `workload`, `context`, `model`.

**Evidence:** [Source 1](https://github.com/vllm-project/vllm/blob/HEAD/README.md) · [Source 2](https://github.com/vllm-project/vllm/blob/HEAD/vllm/v1/core/block_pool.py) · [Source 3](https://github.com/vllm-project/vllm/blob/HEAD/vllm/v1/core/sched/scheduler.py) · [Source 4](https://github.com/vllm-project/vllm/blob/HEAD/docs/design/hybrid_kv_cache_manager.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="precision"></a>

## Numerical representation / 数值表示与低比特执行 (9)

**How is each value represented?** Co-design low-bit formats, layouts and execution kernels.

<a id="bitnet-cpp"></a>

### [bitnet.cpp](https://github.com/microsoft/BitNet)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Low-bit model/runtime co-design route: compare representation-specific execution and retained framework lineage.

Executes compatible ternary LLMs with packed low-bit kernels and architecture-specific LUT paths, choosing pre-tuned or generated kernel headers for model shapes.

**Scope:** BitNet-compatible 1.58-bit model layouts and supported ARM/x86 or GPU paths enable specialized arithmetic instead of generic dense matrix multiplication.

**Boundary:** Lossless refers to the already-ternary model representation, not conversion of an arbitrary FP16 LLM without quality change; supported model/kernel pairs differ by platform.

**Semantic considerations:** reduced precision, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `ternary-kernels`, `lookup-table`, `model-shape-codegen`.

**Constraints:** `model`, `precision`, `hardware`, `shape`.

**Evidence:** [Source 1](https://github.com/microsoft/BitNet/blob/HEAD/README.md) · [Source 2](https://github.com/microsoft/BitNet/blob/HEAD/src/README.md) · [Source 3](https://github.com/microsoft/BitNet/blob/HEAD/src/ggml-bitnet-lut.cpp) · [Source 4](https://github.com/microsoft/BitNet/blob/HEAD/setup_env.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="deepcompressor"></a>

### [DeepCompressor](https://github.com/nunchux-ai/deepcompressor)

[foundation](systems.md#foundation) · `support` · `optimizer` · `text / image` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Calibrates quantization and SVDQuant low-rank outlier decomposition, evaluates compressed models and exports checkpoints into runtime-specific deployment layouts.

**Scope:** Requires calibration data, supported model adapters and a compatible deployment engine such as Nunchaku for actual low-bit acceleration.

**Boundary:** Fake-quantized evaluation does not itself provide fast low-bit execution; preparation cost and deployment runtime gains are separate.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `post-training-quantization`, `low-rank-outlier-decomposition`, `checkpoint-conversion`.

**Constraints:** `low-precision`, `calibration`, `deployment-backend`.

**Evidence:** [Source 1](https://github.com/nunchux-ai/deepcompressor/blob/main/README.md) · [Source 2](https://github.com/nunchux-ai/deepcompressor/blob/main/examples/diffusion/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="exllamav3"></a>

### [ExLlamaV3](https://github.com/turboderp-org/exllamav3)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** An integrated quantized-model runtime illustrates rebuilding execution around a chosen representation and supported architectures.

Pairs EXL3 weight quantization with dedicated low-bit execution, 2–8-bit paged KV storage and shape-qualified decode paths, plus CPU expert offload and parallel inference.

**Scope:** EXL3/codebook formats, supported model architectures, CUDA GPU capabilities and small decode shapes determine the available optimized path.

**Boundary:** Quantized weights and KV are not the full-precision reference, and optimized paths have explicit eligibility and fallback conditions rather than universal model/backend coverage.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `packed-low-bit`, `quantized-kv`, `graph-replay`, `heterogeneous-execution`.

**Constraints:** `precision`, `hardware`, `memory`, `shape`.

**Evidence:** [Source 1](https://github.com/turboderp-org/exllamav3/blob/HEAD/README.md) · [Source 2](https://github.com/turboderp-org/exllamav3/blob/HEAD/doc/optimize.md) · [Source 3](https://github.com/turboderp-org/exllamav3/blob/HEAD/exllamav3/cache/quant.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="ik-llama"></a>

### [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Deep fork of a general engine: compare compatibility retention and specialized quantized execution.

Extends a llama.cpp fork with additional packed quantization formats, CPU IQK matrix kernels and quantization-specific CUDA dispatch paths.

**Scope:** Quantized tensor type, row layout and CPU SIMD or CUDA support determine dispatch, repacking legality and usable offload combinations.

**Boundary:** The README qualifies CPU and CUDA as its fully functional performance backends and warns that RAM repacking can obstruct hybrid MoE offload; other inherited backends are not equivalently supported.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `packed-low-bit`, `isa-dispatch`, `layout-repacking`.

**Constraints:** `precision`, `hardware`, `memory`.

**Evidence:** [Source 1](https://github.com/ikawrakow/ik_llama.cpp/blob/HEAD/README.md) · [Source 2](https://github.com/ikawrakow/ik_llama.cpp/blob/HEAD/ggml/src/iqk/iqk_mul_mat.cpp) · [Source 3](https://github.com/ikawrakow/ik_llama.cpp/blob/HEAD/ggml/src/ggml-cuda/iqk_mmvq.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="marlin"></a>

### [Marlin](https://github.com/IST-DASLab/marlin)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Repacks INT4 weights/scales offline and overlaps asynchronous loads, dequantization and tensor-core MMA in a shape-specialized FP16×INT4 CUDA kernel.

**Scope:** Weight-only INT4 formats, compatible group/shape alignment and NVIDIA tensor-core hardware enable its inference-oriented memory/compute pipeline.

**Boundary:** The original project is a specialized linear kernel and packing format, not a complete server or a claim of fourfold end-to-end speedup for all models and batches.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `offline-layout`, `dequant-mma-pipeline`, `weight-streaming`.

**Constraints:** `hardware`, `precision`, `shape`, `layout`.

**Evidence:** [Source 1](https://github.com/IST-DASLab/marlin/blob/HEAD/README.md) · [Source 2](https://github.com/IST-DASLab/marlin/blob/HEAD/marlin/marlin_cuda_kernel.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="nunchaku"></a>

### [Nunchaku](https://github.com/nunchux-ai/nunchaku)

[core](systems.md#core) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** A substantial low-bit diffusion backend connects representation-specific execution to reusable pipeline integration.

Executes SVDQuant W4A4 layers by fusing activation quantization with the low-rank down projection and low-bit GEMM with the low-rank output path.

**Scope:** Targets supported low-bit diffusion checkpoints and compatible NVIDIA GPU kernels, reducing model memory and repeated activation traffic.

**Boundary:** Quantization changes numerical computation; engine-only gains must be separated from reduced offloading and optional cache or distilled-checkpoint gains.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `low-bit-gemm`, `low-rank-outlier-path`, `kernel-fusion`, `block-offload`.

**Constraints:** `low-precision`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/nunchux-ai/nunchaku/blob/main/README.md) · [Source 2](https://github.com/nunchux-ai/nunchaku/blob/main/nunchaku/models/linear.py) · [Source 3](https://github.com/nunchux-ai/nunchaku/blob/main/src/kernels/zgemm/gemm_w4a4.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="qtip"></a>

### [QTIP](https://github.com/Cornell-RelaxML/qtip)

[foundation](systems.md#foundation) · `support` · `optimizer` · `text` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Quantizes incoherence-transformed weights with bitshift trellis codes and executes supported low-bit encodings through matching BitshiftLinear matrix-vector kernels.

**Scope:** Trellis/codebook parameters, tile dimensions and the supported 2/3/4-bit HYB encoding determine which quantized artifact has a fast inference path.

**Boundary:** The supplied fast kernels cover specific HYB-code settings, and the README states public interactive generation does not include the matrix fusion used for its headline timing table.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `trellis-quantization`, `packed-matvec`, `hadamard-transform`.

**Constraints:** `precision`, `codebook`, `shape`, `hardware`.

**Evidence:** [Source 1](https://github.com/Cornell-RelaxML/qtip/blob/HEAD/README.md) · [Source 2](https://github.com/Cornell-RelaxML/qtip/blob/HEAD/lib/codebook/bitshift.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="sageattention"></a>

### [SageAttention](https://github.com/thu-ml/SageAttention)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text / image / video` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Applies outlier smoothing and hardware-specific low-precision QK and PV attention kernels, dispatching among INT8/FP8 or newer architecture-specific variants.

**Scope:** Targets supported NVIDIA architectures, layouts and head dimensions, with precision choice constrained by model sensitivity.

**Boundary:** It is an operator library rather than an end-to-end diffusion runtime; operator speedups and reported quality metrics do not guarantee equal pipeline gains or identical outputs.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `quantized-attention`, `outlier-smoothing`, `device-dispatch`.

**Constraints:** `device`, `low-precision`, `attention-shape`.

**Evidence:** [Source 1](https://github.com/thu-ml/SageAttention/blob/main/README.md) · [Source 2](https://github.com/thu-ml/SageAttention/blob/main/sageattention/core.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="t-mac"></a>

### [T-MAC](https://github.com/microsoft/T-MAC)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Generates and tunes CPU low-bit GEMM/GEMV kernels that decompose weights into bit-level operations and use activation lookup tables instead of dequantizing each weight into dense multiply-adds.

**Scope:** Weight bit width, group size, matrix dimensions and CPU vector/lookup capabilities parameterize the generated layout and schedule.

**Boundary:** It is a kernel library integrated into other runtimes, with hardware-dependent gains; the NPU extension has its own path and should not be inferred from CPU measurements.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `lookup-table`, `bitwise-decomposition`, `kernel-autotuning`.

**Constraints:** `precision`, `hardware`, `shape`, `layout`.

**Evidence:** [Source 1](https://github.com/microsoft/T-MAC/blob/HEAD/README.md) · [Source 2](https://github.com/microsoft/T-MAC/blob/HEAD/python/t_mac/ops/qgemm.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="selection"></a>

## Selective computation / 选择性计算 (8)

**Which work can be omitted?** Select neurons, tokens or attention blocks; expose approximation.

<a id="fastvideo"></a>

### [FastVideo](https://github.com/hao-ai-lab/FastVideo)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `video / audio` · **public code**

**Survey relevance:** Video-model pipeline route: contrasts integrated optimization and model changes with execution-stack reconstruction.

Provides video-generation pipelines using top-k Video Sparse Attention blocks, sequence parallelism and memory offload alongside sparse and timestep distillation workflows.

**Scope:** Targets supported video architectures with long spatiotemporal sequences; sparse checkpoints and kernels have backend-specific requirements.

**Boundary:** VSA and timestep distillation can change the model; current MLX VSA documentation explicitly distinguishes a reference path from an experimental Metal path with output differences.

**Semantic considerations:** selective approximation, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-sparse-attention`, `distillation`, `sequence-parallelism`, `block-offload`.

**Constraints:** `long-sequence`, `device`, `model-family`.

**Evidence:** [Source 1](https://github.com/hao-ai-lab/FastVideo/blob/main/README.md) · [Source 2](https://github.com/hao-ai-lab/FastVideo/blob/main/docs/attention/vsa/index.md) · [Source 3](https://github.com/hao-ai-lab/FastVideo/blob/main/docs/inference/offloading.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="minference"></a>

### [MInference](https://github.com/microsoft/MInference)

[foundation](systems.md#foundation) · `support` · `optimizer` · `text` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Assigns attention heads to offline-discovered sparse pattern families and estimates input-dependent sparse indices online before dispatching pattern-specific long-context prefill kernels.

**Scope:** Long prompts, per-layer/head sparse-pattern configurations and supported attention layouts make selective attention computation useful.

**Boundary:** This replaces dense attention with an approximation and patches existing HF/vLLM paths; quality and speed depend on model, context and sparsity configuration rather than a universal exactness guarantee.

**Semantic considerations:** selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `offline-head-pattern`, `online-sparse-index`, `sparse-prefill`.

**Constraints:** `workload`, `sparsity`, `model`, `context`.

**Evidence:** [Source 1](https://github.com/microsoft/MInference/blob/HEAD/README.md) · [Source 2](https://github.com/microsoft/MInference/blob/HEAD/minference/modules/minference_forward.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="powerinfer"></a>

### [PowerInfer](https://github.com/Tiiny-AI/PowerInfer)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Model/runtime co-design route: separates sparsity assumptions and changed models from construction-method effects.

Uses profiled neuron activation frequencies and a capacity-constrained split to place hot neurons on GPU, execute cold activated neurons on CPU and dispatch predictor-guided sparse operators.

**Scope:** ReLU-sparse model families, learned predictor weights, activation profiles and a user GPU-memory budget enable neuron-level CPU/GPU partitioning.

**Boundary:** The accelerated route requires compatible sparse models and predictors; supported ReLU/ProSparse variants can change activations and Bamboo changes model structure. It is not a drop-in accelerator for arbitrary dense checkpoints.

**Semantic considerations:** selective approximation, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `activation-locality`, `heterogeneous-execution`, `sparse-kernels`.

**Constraints:** `sparsity`, `hardware`, `memory`, `model`.

**Evidence:** [Source 1](https://github.com/Tiiny-AI/PowerInfer/blob/HEAD/README.md) · [Source 2](https://github.com/Tiiny-AI/PowerInfer/blob/HEAD/powerinfer-py/powerinfer/solver.py) · [Source 3](https://github.com/Tiiny-AI/PowerInfer/blob/HEAD/ggml-cuda.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="snapkv"></a>

### [SnapKV](https://github.com/FasterDecoding/SnapKV)

[foundation](systems.md#foundation) · `support` · `optimizer` · `text` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Uses the final prompt observation window to score and pool attention importance, gathers top-ranked historical KV positions and retains the recent window within a fixed prompt-cache capacity.

**Scope:** A bounded KV budget and the assumption that prompt-end attention predicts useful historical positions enable head-specific cache selection.

**Boundary:** KV eviction is approximate and can remove later-needed information; the released monkeypatches target specific Llama/Mistral/Mixtral Transformers versions and are not a standalone serving runtime.

**Semantic considerations:** selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `observation-window-selection`, `kv-pruning`.

**Constraints:** `context`, `workload`, `memory`, `model`.

**Evidence:** [Source 1](https://github.com/FasterDecoding/SnapKV/blob/HEAD/README.md) · [Source 2](https://github.com/FasterDecoding/SnapKV/blob/HEAD/snapkv/monkeypatch/snapkv_utils.py) · [Source 3](https://github.com/FasterDecoding/SnapKV/blob/HEAD/snapkv/monkeypatch/monkeypatch.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="spargeattn"></a>

### [SpargeAttention](https://github.com/thu-ml/SpargeAttn)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text / image / video` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Builds a block lookup table from query-key block statistics or a supplied mask and executes selected attention blocks with Sage-style low-precision kernels.

**Scope:** Requires supported head dimensions and block layouts, with top-k or threshold settings controlling sparse work and approximation.

**Boundary:** The inspected API asserts head dimensions 64 or 128 and exposes a sparsity-quality trade-off; it is not a universal lossless replacement for every attention call.

**Semantic considerations:** selective approximation, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-sparse-attention`, `quantized-attention`, `online-block-selection`.

**Constraints:** `device`, `attention-shape`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/thu-ml/SpargeAttn/blob/main/README.md) · [Source 2](https://github.com/thu-ml/SpargeAttn/blob/main/spas_sage_attn/core.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="sparse-videogen"></a>

### [Sparse VideoGen](https://github.com/svg-project/Sparse-VideoGen)

[foundation](systems.md#foundation) · `support` · `research-prototype` · `video` · **public code**

**Survey relevance:** Related mechanism reference for controlled comparison; source availability alone does not make it a construction case.

Accelerates video attention using profiled spatial-temporal masks in SVG1 and semantic clustering with token permutation and dynamic sparse kernels in SVG2.

**Scope:** Requires supported video-model attention adapters and enough sequence length for sparse selection and layout transformations to amortize their overhead.

**Boundary:** SVG1, SVG2 and SVG-EAR are distinct methods in one repository; this audit checked README and integration arguments but did not inspect their kernel internals.

**Semantic considerations:** selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-sparse-attention`, `online-profiling`, `token-permutation`.

**Constraints:** `long-sequence`, `attention-pattern`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/svg-project/Sparse-VideoGen/blob/main/README.md) · [Source 2](https://github.com/svg-project/Sparse-VideoGen/blob/main/wan_t2v_inference.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="tomesd"></a>

### [ToMe for Stable Diffusion](https://github.com/dbolya/tomesd)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Uses spatially constrained bipartite token matching to merge redundant tokens before selected transformer operations and restores the original token layout afterward.

**Scope:** Targets supported Stable Diffusion transformer blocks, with merge ratio and spatial partition parameters controlling saved work.

**Boundary:** Token merging is explicitly lossy, and its random partitioning may require controlled seeds; model and attention backend compatibility must be checked.

**Semantic considerations:** selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `token-merging`, `token-unmerging`.

**Constraints:** `token-redundancy`, `quality-budget`, `model-family`.

**Evidence:** [Source 1](https://github.com/dbolya/tomesd/blob/main/README.md) · [Source 2](https://github.com/dbolya/tomesd/blob/main/tomesd/merge.py) · [Source 3](https://github.com/dbolya/tomesd/blob/main/tomesd/patch.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="turbodiffusion"></a>

### [TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `video` · **public code**

**Survey relevance:** Video acceleration route: separates distillation, precision and attention changes from runtime construction.

Integrates SageAttention and sparse-linear attention with timestep-distilled video checkpoints and optional quantized linear layers in an executable generation stack.

**Scope:** Requires supported Wan-family or other integrated model paths and the correct quantized or unquantized checkpoint for the target GPU.

**Boundary:** Headline acceleration combines fewer denoising steps, altered attention and runtime kernels; it must not be described as a pure implementation speedup.

**Semantic considerations:** selective approximation, reduced precision, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `sparse-linear-attention`, `quantized-attention`, `low-bit-gemm`, `distillation`.

**Constraints:** `device`, `model-family`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) · [Source 2](https://github.com/thu-ml/TurboDiffusion/blob/main/turbodiffusion/ops/quant/quant.cu) · [Source 3](https://github.com/thu-ml/TurboDiffusion/blob/main/turbodiffusion/rcm/utils/attention.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="reuse"></a>

## Computation reuse / 计算复用 (10)

**Which earlier results can be reused?** Reuse request prefixes, features or attention across steps.

<a id="cache-dit"></a>

### [Cache-DiT](https://github.com/vipshop/cache-dit)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image / video` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Wraps supported Diffusers transformer blocks with managed cache contexts for DBCache and feature predictors while composing parallelism, quantization and CPU offload.

**Scope:** Relies on compatible Diffusers block adapters and user-selected cache thresholds or schedules for repeated denoising.

**Boundary:** It retains PyTorch and should not be equated with a native standalone runtime; each adapter and optimization combination has its own support boundary.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `activation-reuse`, `feature-extrapolation`, `hybrid-parallelism`, `block-offload`.

**Constraints:** `model-family`, `denoising-steps`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/vipshop/cache-dit/blob/main/README.md) · [Source 2](https://github.com/vipshop/cache-dit/blob/main/src/cache_dit/caching/cache_contexts/cache_manager.py) · [Source 3](https://github.com/vipshop/cache-dit/blob/main/src/cache_dit/caching/cache_blocks/pattern_0_1_2.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="deepcache"></a>

### [DeepCache](https://github.com/horseee/DeepCache)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image / video` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Reuses high-level U-Net branch outputs at intermediate denoising steps while recomputing inexpensive lower-level features, controlled by a cache interval and branch index.

**Scope:** Relies on supported U-Net skip-branch structure and temporal feature redundancy in SD-family pipelines.

**Boundary:** It is an approximate architecture-aware patch, not a general DiT cache; cache interval and branch depth trade computation against output drift.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `activation-reuse`, `branch-skipping`.

**Constraints:** `unet-architecture`, `denoising-steps`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/horseee/DeepCache/blob/master/README.md) · [Source 2](https://github.com/horseee/DeepCache/blob/master/DeepCache/extension/deepcache.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="ditfastattn"></a>

### [DiTFastAttn](https://github.com/thu-nics/DiTFastAttn)

[foundation](systems.md#foundation) · `support` · `research-prototype` · `image / video` · **public code**

**Survey relevance:** Related mechanism reference for controlled comparison; source availability alone does not make it a construction case.

Calibrates attention compression choices that combine local windows with cached residuals, temporal output reuse and conditional-unconditional computation sharing.

**Scope:** Targets supported DiT architectures and calibration settings where spatial, temporal or CFG redundancy is measurable.

**Boundary:** The implementation and xDiT integration have version and parallelism restrictions; compression thresholds trade approximation error against speed.

**Semantic considerations:** earlier-state reuse, selective approximation.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `window-attention`, `residual-reuse`, `cfg-reuse`, `calibrated-attention-policy`.

**Constraints:** `attention-redundancy`, `calibration`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/thu-nics/DiTFastAttn/blob/main/README.md) · [Source 2](https://github.com/thu-nics/DiTFastAttn/blob/main/dit_fast_attention.py) · [Source 3](https://github.com/xdit-project/xDiT/blob/main/docs/methods/ditfastattn.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="learning-to-cache"></a>

### [Learning-to-Cache](https://github.com/horseee/learning-to-cache)

[foundation](systems.md#foundation) · `support` · `research-prototype` · `image` · **public code**

**Survey relevance:** Related mechanism reference for controlled comparison; source availability alone does not make it a construction case.

Optimizes a router over denoising steps and transformer layers to decide which layer outputs are recomputed or served from cache while keeping base-model weights fixed.

**Scope:** Requires architecture- and sampling-schedule-specific router training or released router checkpoints for DiT or U-ViT.

**Boundary:** The base denoiser can remain fixed but the router is learned, so this should not be categorized as an entirely training-free cache.

**Semantic considerations:** earlier-state reuse, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `learned-layer-gating`, `activation-reuse`.

**Constraints:** `model-family`, `trained-router`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/horseee/learning-to-cache/blob/main/README.md) · [Source 2](https://github.com/horseee/learning-to-cache/blob/main/DiT/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="lmcache"></a>

### [LMCache](https://github.com/LMCache/LMCache)

[foundation](systems.md#foundation) · `support` · `backend` · `text` · **public code**

**Survey relevance:** Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence.

Retrieves and persists KV states through tiered storage backends; optional CacheBlend paths selectively recompute states for non-prefix reuse.

**Scope:** Repeated or shared LLM context across requests and engines

**Boundary:** Exact prefix reuse and approximate/non-prefix blending have different equivalence conditions; token identity, positional context and cache configuration matter.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `kv-reuse`, `tiered-kv`, `cache-blending`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/LMCache/LMCache/blob/dev/README.md) · [Source 2](https://github.com/LMCache/LMCache/blob/dev/lmcache/v1/cache_engine.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="magcache"></a>

### [MagCache](https://github.com/Zehong-Ma/MagCache)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image / video` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Uses calibrated residual-magnitude ratios to accumulate an estimated reuse error and skips full transformer evaluation while the error and reuse-length limits permit.

**Scope:** Requires a model and denoising-schedule magnitude profile plus threshold and maximum-reuse settings.

**Boundary:** Calibration and schedule interpolation affect validity; the inspected FLUX implementation also contains a schedule-specific refresh exception.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `activation-reuse`, `calibrated-step-gating`.

**Constraints:** `denoising-steps`, `calibration`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/Zehong-Ma/MagCache/blob/main/README.md) · [Source 2](https://github.com/Zehong-Ma/MagCache/blob/main/MagCache4FLUX/magcache_flux.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="sglang"></a>

### [SGLang](https://github.com/sgl-project/sglang)

[foundation](systems.md#foundation) · `support` · `runtime` · `text` · **public code**

**Survey relevance:** General serving baseline and source of shared runtime abstractions and components.

Indexes reusable prefix KV state in a radix tree, protects active nodes with references and offers cache-aware queue policies that prioritize requests using matched-prefix information.

**Scope:** Shared token prefixes within compatible cache namespaces, finite device memory and request arrivals make prefix matching and cache-aware batching effective.

**Boundary:** Prefix hits require compatible token and extra-key namespaces; cache-aware policies are configurable and must not be assumed to be the default or to benefit workloads without shared prefixes.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `radix-prefix-reuse`, `cache-aware-scheduling`, `continuous-batching`.

**Constraints:** `workload`, `memory`, `context`, `model`.

**Evidence:** [Source 1](https://github.com/sgl-project/sglang/blob/HEAD/README.md) · [Source 2](https://github.com/sgl-project/sglang/blob/HEAD/python/sglang/srt/mem_cache/radix_cache.py) · [Source 3](https://github.com/sgl-project/sglang/blob/HEAD/python/sglang/srt/managers/schedule_policy.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="t-gate"></a>

### [T-GATE](https://github.com/HaozheLiu-ST/T-GATE)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image / video` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Caches and reuses self-attention during early semantic planning and cross-attention during later fidelity refinement according to gate steps and refresh intervals.

**Scope:** Targets text-conditioned diffusion pipelines whose attention contributions vary across denoising phases.

**Boundary:** Gate position and refresh intervals depend on the pipeline and sampling schedule; reused attention changes outputs and need not preserve every quality dimension.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `attention-output-reuse`, `phase-gating`.

**Constraints:** `attention-phase`, `denoising-steps`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/HaozheLiu-ST/T-GATE/blob/main/README.md) · [Source 2](https://github.com/HaozheLiu-ST/T-GATE/blob/main/tgate/tgate_utils.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="taylorseer"></a>

### [TaylorSeer](https://github.com/Shenyi-Z/TaylorSeer)

[foundation](systems.md#foundation) · `support` · `research-prototype` · `image / video` · **public code**

**Survey relevance:** Related mechanism reference for controlled comparison; source availability alone does not make it a construction case.

Estimates higher-order feature derivatives from earlier full evaluations and substitutes a Taylor-series forecast for selected later block computations.

**Scope:** Assumes sufficiently smooth feature evolution across denoising steps and requires a refresh schedule and Taylor order.

**Boundary:** Forecast error depends on interval, order, model and scheduler; claimed quality preservation is metric-based, not numerical identity.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `feature-extrapolation`, `activation-reuse`.

**Constraints:** `denoising-steps`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/Shenyi-Z/TaylorSeer/blob/main/README.md) · [Source 2](https://github.com/Shenyi-Z/TaylorSeer/blob/main/TaylorSeer-DiT/taylor_utils/__init__.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="teacache"></a>

### [TeaCache](https://github.com/ali-vilab/TeaCache)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image / video / audio` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Accumulates a rescaled relative change in timestep-modulated inputs and reuses a cached transformer residual until the model-specific error threshold is exceeded.

**Scope:** Benefits from redundancy across denoising iterations and requires model-specific rescaling coefficients and thresholds.

**Boundary:** Skipping transformer computation changes the denoising trajectory; coefficients and threshold quality do not automatically transfer between models or schedules.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `activation-reuse`, `adaptive-step-gating`.

**Constraints:** `denoising-steps`, `quality-budget`, `model-family`.

**Evidence:** [Source 1](https://github.com/ali-vilab/TeaCache/blob/main/README.md) · [Source 2](https://github.com/ali-vilab/TeaCache/blob/main/TeaCache4Wan2.1/teacache_generate.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="decoding"></a>

## Generation order / 生成顺序 (6)

**Can more output be produced per step?** Draft and verify tokens, or reorganize block generation.

<a id="eagle"></a>

### [EAGLE](https://github.com/SafeAILab/EAGLE)

[foundation](systems.md#foundation) · `support` · `optimizer` · `text` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Builds a draft token tree from target-model features and verifies candidate paths in parallel; EAGLE-3 combines features from several layers.

**Scope:** Autoregressive decoding with compatible EAGLE draft checkpoints

**Boundary:** Draft checkpoints must match the target model; acceptance, sampling settings and draft overhead determine benefit. EAGLE versions use different drafting designs.

**Semantic considerations:** target-verified proposals.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `speculative-decoding`, `tree-verification`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/SafeAILab/EAGLE/blob/main/README.md) · [Source 2](https://github.com/SafeAILab/EAGLE/blob/main/eagle/model/ea_model.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="fast-dllm"></a>

### [Fast-dLLM](https://github.com/NVlabs/Fast-dLLM)

[foundation](systems.md#foundation) · `support` · `research-prototype` · `text / multimodal` · **public code**

**Survey relevance:** Related mechanism reference for controlled comparison; source availability alone does not make it a construction case.

Combines confidence-aware parallel token updates and cached states; v2 uses block-diffusion checkpoints and hierarchical caching.

**Scope:** Diffusion language models and supported multimodal derivatives

**Boundary:** Version-dependent semantics: v1 is training-free, while v2 uses fine-tuned block-diffusion models. Do not compare all variants as unchanged autoregressive execution.

**Semantic considerations:** configuration-dependent, model / router training, earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-generation`, `kv-reuse`, `parallel-decoding`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/NVlabs/Fast-dLLM/blob/main/README.md) · [Source 2](https://github.com/NVlabs/Fast-dLLM/blob/main/v2/generation_functions.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="inferix"></a>

### [Inferix](https://github.com/alibaba-damo-academy/Inferix)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `video` · **public code**

**Survey relevance:** Stateful world-model execution route: an adjacent case of reorganizing generation state rather than evidence of AI-built native execution.

Manages persistent KV state for semi-autoregressive diffusion blocks while separately chunking VAE decoding and streaming generated video.

**Scope:** Requires block-diffusion or semi-autoregressive world-model execution and must manage long-lived generation state under memory limits.

**Boundary:** A diffusion block is a model-generation unit, whereas a VAE chunk is a decoder memory unit; neither implies generic support for every video diffusion architecture.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-diffusion-execution`, `kv-cache-management`, `vae-chunking`, `streaming-output`.

**Constraints:** `block-autoregression`, `memory-capacity`, `streaming-latency`.

**Evidence:** [Source 1](https://github.com/alibaba-damo-academy/Inferix/blob/main/README.md) · [Source 2](https://github.com/alibaba-damo-academy/Inferix/blob/main/inferix/kvcache_manager/kvcache_manager.py) · [Source 3](https://github.com/alibaba-damo-academy/Inferix/blob/main/inferix/core/memory/manager.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="llamampere"></a>

### [llamAmpere](https://github.com/JakeATX/llamAmpere)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A substantial llama.cpp fork couples model-specific speculative decoding, compressed state and Ampere kernels while retaining shared runtime services.

Extends the llama.cpp/TurboQuant lineage with SM86 verification kernels, a draft-only vocabulary shortlist, format-specific quantized execution, SJ-KVaRN compressed KV and RAM/disk prompt-state reuse.

**Scope:** Qwen3.8-27B with an MTP head, primarily single-stream inference on Ampere RTX 3090/3090 Ti, where verification width and long-context state compete for compute and VRAM.

**Boundary:** The optimized path is a deep fork, not a new runtime from scratch. Current examples use a post-trained Swift 1.5 derivative plus quantized weights/KV; those changes must be separated from engine-only gains. v0.5.3 documents an unresolved parallel-8 startup failure; other GPU generations are not equivalently tuned.

**Semantic considerations:** target-verified proposals, reduced precision, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `mtp-speculation`, `draft-vocabulary-shortlist`, `shape-specific-cuda`, `quantized-kv`, `prompt-cache-tiering`.

**Constraints:** `model`, `hardware`, `memory`, `precision`, `context`, `workload`.

**Evidence:** [Source 1](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN_AMPERE.md) · [Source 2](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/llamampere-v0.5/RELEASE_NOTES.md) · [Source 3](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/ggml/src/ggml-cuda/mmvq.cu) · [Source 4](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/development/sjkvarn-cuda.md) · [Source 5](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/llamampere-v0.5.3/RELEASE_NOTES.md) · [Source 6](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/llamampere-v0.2/ARTICLE.md) · [Source 7](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN38_SM86_FRONTIER_HANDOVER.md) · [Source 8](https://huggingface.co/jakeatx/ATX-Swift-1.5-Qwen3.8-27B-Uncensored-IQ4_XS-M-GGUF/blob/1f3a29191771b5dae54254fa590b0a0013c18ea1/README.md) · [Source 9](https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27b/blob/b4c84d42903a8646b25857eb2827288d92ed85a4/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="lookahead"></a>

### [Lookahead Decoding](https://github.com/hao-ai-lab/LookaheadDecoding)

[foundation](systems.md#foundation) · `support` · `optimizer` · `text` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Collects n-gram candidates from Jacobi trajectories and combines parallel lookahead with target-model verification without a separate draft model.

**Scope:** Autoregressive decoding with spare parallel compute

**Boundary:** More parallel work is exchanged for fewer sequential steps; window size, accepted-token count and model integration determine benefit.

**Semantic considerations:** target-verified proposals.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `jacobi-decoding`, `ngram-pool`, `tree-verification`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/hao-ai-lab/LookaheadDecoding/blob/main/README.md) · [Source 2](https://github.com/hao-ai-lab/LookaheadDecoding/blob/main/lade/decoding.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="medusa"></a>

### [Medusa](https://github.com/FasterDecoding/Medusa)

[foundation](systems.md#foundation) · `support` · `research-prototype` · `text` · **public code**

**Survey relevance:** Related mechanism reference for controlled comparison; source availability alone does not make it a construction case.

Adds multiple future-token heads, packs their candidates into tree attention, and accepts a verified prefix.

**Scope:** Autoregressive LLMs with trained auxiliary prediction heads

**Boundary:** Medusa-1 keeps the base model fixed; Medusa-2 can jointly train it. Typical acceptance in non-greedy modes is not a blanket guarantee of the original sampling distribution.

**Semantic considerations:** configuration-dependent, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `multi-token-heads`, `tree-verification`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/FasterDecoding/Medusa/blob/main/README.md) · [Source 2](https://github.com/FasterDecoding/Medusa/blob/main/medusa/model/medusa_model.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="serving"></a>

## Parallelism & scheduling / 并行与调度 (12)

**Who executes what, and when?** Partition stages, devices and requests around workload constraints.

<a id="asyncdiff"></a>

### [AsyncDiff](https://github.com/czg1225/AsyncDiff)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `image / video` · **public code**

**Survey relevance:** Multi-device diffusion route: compares changed parallel execution and stale-state assumptions.

Partitions a denoiser into device-owned components and broadcasts cached component outputs so later denoising iterations can execute asynchronously in parallel.

**Scope:** Requires multiple GPUs and temporal hidden-state redundancy, with component count, warmup and stride controlling parallel behavior.

**Boundary:** Using earlier-step states changes computation and adds communication; warmup and optional time shifting alter the speed-quality trade-off.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `asynchronous-model-parallelism`, `stale-activation-reuse`.

**Constraints:** `multi-device`, `interconnect`, `denoising-steps`.

**Evidence:** [Source 1](https://github.com/czg1225/AsyncDiff/blob/main/README.md) · [Source 2](https://github.com/czg1225/AsyncDiff/blob/main/asyncdiff/async_sd.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="distrifusion"></a>

### [DistriFusion](https://github.com/mit-han-lab/distrifuser)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `image` · **public code**

**Survey relevance:** Distributed diffusion route: establishes earlier execution and communication specialization.

Splits image computation across devices, synchronizes patch context during warmup, then uses previous-step remote activations while asynchronously communicating fresh updates.

**Scope:** Targets high-resolution diffusion on multiple GPUs with temporal activation redundancy and sufficient work to hide communication.

**Boundary:** Stale remote features and corrected asynchronous normalization approximate synchronous inference; additional GPUs and resolution change the speed trade-off.

**Semantic considerations:** earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `patch-parallelism`, `stale-activation-reuse`, `communication-overlap`.

**Constraints:** `multi-device`, `high-resolution`, `interconnect`.

**Evidence:** [Source 1](https://github.com/mit-han-lab/distrifuser/blob/main/README.md) · [Source 2](https://github.com/mit-han-lab/distrifuser/blob/main/distrifuser/modules/pp/attn.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="distserve"></a>

### [DistServe](https://github.com/LLMServe/DistServe)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** Serving specialization route: establishes prefill/decode separation independently of recent engine-construction claims.

Separates prefill and decode workers, chooses their resource/parallelism configurations independently, and migrates KV state between them.

**Scope:** Latency-constrained online LLM serving on multiple GPUs

**Boundary:** KV transfer and placement costs depend on the interconnect; the released research stack supports a narrower model/software set than current general engines.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `prefill-decode-disaggregation`, `kv-transfer`, `pipeline-parallelism`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/LLMServe/DistServe/blob/main/README.md) · [Source 2](https://github.com/LLMServe/DistServe/blob/main/distserve/context_stage_scheduler.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="openvino-genai"></a>

### [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai)

[foundation](systems.md#foundation) · `support` · `runtime` · `text / image / video / audio / multimodal` · **public code**

**Survey relevance:** General deployment baseline for device coverage, model export and state-management costs.

Adds generative pipelines and continuous-batching policy above OpenVINO compiled models, using device-specific KV layouts, block allocation and prefix-cache reuse.

**Scope:** OpenVINO-supported CPU/GPU/NPU devices, model export format, cache precision and per-device feature support constrain execution.

**Boundary:** It reuses the OpenVINO runtime rather than replacing the lower compiler stack; cache eviction and sparse-attention options may change model outputs and require separate quality checks.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `backend-delegation`, `kv-management`, `workload-scheduling`, `prefix-reuse`.

**Constraints:** `hardware`, `memory`, `workload`, `precision`.

**Evidence:** [Source 1](https://github.com/openvinotoolkit/openvino.genai/blob/HEAD/README.md) · [Source 2](https://github.com/openvinotoolkit/openvino.genai/blob/HEAD/src/cpp/src/continuous_batching/pipeline.cpp) · [Source 3](https://github.com/openvinotoolkit/openvino.genai/blob/HEAD/src/cpp/src/continuous_batching/cache/kv_cache_manager.hpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="para-attention"></a>

### [ParaAttention](https://github.com/chengzeyi/ParaAttention)

[foundation](systems.md#foundation) · `support` · `optimizer` · `image / video` · **public code**

**Survey relevance:** Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack.

Provides compile-friendly Ring/Ulysses context parallel adapters and First Block Cache, which gates later transformer blocks using the change in the first block residual.

**Scope:** Requires compatible Diffusers adapters; distributed speed depends on communication, while cache behavior depends on a residual threshold.

**Boundary:** Context parallelism and approximate residual reuse are separate features and must be enabled and evaluated independently.

**Semantic considerations:** configuration-dependent, earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `sequence-parallelism`, `first-block-gating`, `activation-reuse`, `graph-compilation`.

**Constraints:** `multi-device`, `denoising-steps`, `quality-budget`.

**Evidence:** [Source 1](https://github.com/chengzeyi/ParaAttention/blob/main/README.md) · [Source 2](https://github.com/chengzeyi/ParaAttention/blob/main/src/para_attn/first_block_cache/utils.py) · [Source 3](https://github.com/chengzeyi/ParaAttention/blob/main/src/para_attn/first_block_cache/diffusers_adapters/flux.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="petals"></a>

### [Petals](https://github.com/bigscience-workshop/petals)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Distributed execution route: compares a different deployment contract and system boundary.

Places transformer blocks on peers and routes stateful inference sessions through a latency-aware sequence of remote block servers.

**Scope:** Models distributed across networked user-contributed devices

**Boundary:** Network latency, peer availability and trust assumptions differ from a controlled single-cluster deployment; this is not a local drop-in engine.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `pipeline-parallelism`, `peer-routing`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/bigscience-workshop/petals/blob/main/README.md) · [Source 2](https://github.com/bigscience-workshop/petals/blob/main/src/petals/client/routing/sequence_manager.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="punica"></a>

### [Punica](https://github.com/punica-ai/punica)

[adjacent](systems.md#adjacent) · `system` · `backend` · `text` · **public code**

**Survey relevance:** Multi-adapter execution route: compares workload-specific kernels and shared-model scheduling.

Batches the common base-model computation while segmented gather matrix-vector kernels apply different low-rank adapter updates per request.

**Scope:** Concurrent LoRA requests with shared base weights

**Boundary:** Adapter rank, layout and supported kernels constrain batching; compare against a tuned multi-adapter serving baseline.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `multi-adapter-batching`, `segmented-gather-matvec`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/punica-ai/punica/blob/master/README.md) · [Source 2](https://github.com/punica-ai/punica/blob/master/csrc/sgmv/sgmv_cutlass.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="s-lora"></a>

### [S-LoRA](https://github.com/S-LoRA/S-LoRA)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** Multi-adapter serving route: establishes prior integrated specialization of memory and batching.

Pages adapter weights and KV states in a unified memory pool and batches heterogeneous adapter ranks using specialized LoRA kernels.

**Scope:** Many LoRA adapters sharing one base model

**Boundary:** Requires a shared base-model family and supported adapter layouts; this is not batching arbitrary independent models.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `multi-adapter-batching`, `unified-paging`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/S-LoRA/S-LoRA/blob/main/README.md) · [Source 2](https://github.com/S-LoRA/S-LoRA/blob/main/slora/models/bmm/lora_bmm_infer.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="sarathi-serve"></a>

### [Sarathi-Serve](https://github.com/microsoft/sarathi-serve)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** Serving specialization route: compares chunked prefill and batching independently of implementation provenance.

Splits prefills into bounded chunks and schedules ongoing decode tokens before filling the remaining batch budget with prefill work.

**Scope:** Mixed prefill/decode traffic with token-latency targets

**Boundary:** Chunk size trades throughput against latency; this research fork does not promise full feature parity with upstream vLLM.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `chunked-prefill`, `decode-first-batching`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/microsoft/sarathi-serve/blob/main/README.md) · [Source 2](https://github.com/microsoft/sarathi-serve/blob/main/sarathi/core/scheduler/sarathi_scheduler.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="tensorrt-llm"></a>

### [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

[foundation](systems.md#foundation) · `support` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** General GPU serving baseline and kernel source; reuse is distinct from independent full-stack implementation.

Combines NVIDIA-specific LLM kernels with chunked-context scheduling, generation-aware batching and reusable paged KV-cache management.

**Scope:** NVIDIA GPU architecture, model/attention structure, batch-token budgets, KV capacity and precision modes drive execution choices.

**Boundary:** It is a broad serving runtime and a strong baseline; current PyTorch executor paths mean it should not be described solely as a static TensorRT model compiler.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `workload-scheduling`, `kv-management`, `hardware-kernels`, `graph-replay`.

**Constraints:** `hardware`, `workload`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/NVIDIA/TensorRT-LLM/blob/HEAD/README.md) · [Source 2](https://github.com/NVIDIA/TensorRT-LLM/blob/HEAD/tensorrt_llm/_torch/pyexecutor/scheduler/scheduler.py) · [Source 3](https://github.com/NVIDIA/TensorRT-LLM/blob/HEAD/cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="videosys"></a>

### [VideoSys](https://github.com/NUS-HPC-AI-Lab/VideoSys)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `video` · **public code**

**Survey relevance:** Video-serving framework route: compares reusable parallelization with narrowly reconstructed execution stacks.

Combines Pyramid Attention Broadcast with dynamic sequence parallelism, reusing attention outputs at type-specific intervals and changing sequence partitions across attention axes.

**Scope:** Targets supported video transformers with separable spatial, temporal and cross-modal attention and multi-GPU execution.

**Boundary:** PAB is approximate reuse and its supported model set differs from the broader framework; the repository also contains training optimizations that are not inference mechanisms.

**Semantic considerations:** configuration-dependent, earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `attention-output-reuse`, `axis-switching-parallelism`.

**Constraints:** `spatiotemporal-architecture`, `multi-device`, `denoising-steps`.

**Evidence:** [Source 1](https://github.com/NUS-HPC-AI-Lab/VideoSys/blob/master/README.md) · [Source 2](https://github.com/NUS-HPC-AI-Lab/VideoSys/blob/master/docs/pab.md) · [Source 3](https://github.com/NUS-HPC-AI-Lab/VideoSys/blob/master/docs/dsp.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="xdit"></a>

### [xDiT](https://github.com/xdit-project/xDiT)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Distributed diffusion route: compares framework-integrated parallel execution and supported-model boundaries.

Combines Ulysses and Ring sequence parallelism with CFG/data parallelism and PipeFusion patch pipelines that reuse earlier-step features to overlap communication.

**Scope:** Targets distributed DiT inference where sequence length, attention-head count and device interconnect determine useful parallel degrees.

**Boundary:** USP and PipeFusion are different execution choices; stale-feature pipelining is not numerically equivalent to exact synchronous parallelism and some combinations are unsupported.

**Semantic considerations:** configuration-dependent, earlier-state reuse.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `sequence-parallelism`, `patch-pipeline`, `cfg-parallelism`, `stale-activation-reuse`.

**Constraints:** `multi-device`, `interconnect`, `model-family`.

**Evidence:** [Source 1](https://github.com/xdit-project/xDiT/blob/main/README.md) · [Source 2](https://github.com/xdit-project/xDiT/blob/main/docs/methods/pipefusion.md) · [Source 3](https://github.com/xdit-project/xDiT/blob/main/docs/methods/usp.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="execution"></a>

## Compiled & native execution / 编译与原生执行 (35)

**How does a graph become an executable?** Fuse, lower, specialize and dispatch graphs or native kernels.

<a id="aitemplate"></a>

### [AITemplate](https://github.com/facebookincubator/AITemplate)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Profiles CUDA/HIP kernel choices, performs graph and memory fusion, plans intermediate storage and emits a self-contained model shared library.

**Scope:** GPU architecture, supported operator templates, FP16-oriented execution and declared shape ranges constrain compilation.

**Boundary:** Operator coverage is incomplete and hardware/compiler compatibility matters; FX2AIT can leave unsupported portions outside the generated engine.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `graph-fusion`, `kernel-autotuning`, `memory-planning`.

**Constraints:** `hardware`, `precision`, `shape`.

**Evidence:** [Source 1](https://github.com/facebookincubator/AITemplate/blob/HEAD/README.md) · [Source 2](https://github.com/facebookincubator/AITemplate/blob/HEAD/python/aitemplate/compiler/compiler.py) · [Source 3](https://github.com/facebookincubator/AITemplate/blob/HEAD/python/aitemplate/compiler/transform/memory_planning.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="tvm"></a>

### [Apache TVM](https://github.com/apache/tvm)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / general` · **public code**

**Survey relevance:** Reusable compiler foundation and historical source of model and schedule specialization.

Coordinates Relax graph transformations and tensor-level scheduling to fuse operators, dispatch libraries and lower target-specific tensor programs into deployable modules.

**Scope:** Compilation targets, tensor shapes, legal operators and schedule rules define the specialization boundary.

**Boundary:** TVM is reusable compiler infrastructure for many workloads; a TVM-backed project needs its own model pipeline, runtime policy and evaluation.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `graph-fusion`, `hardware-codegen`, `kernel-autotuning`.

**Constraints:** `hardware`, `shape`, `workload`.

**Evidence:** [Source 1](https://github.com/apache/tvm/blob/HEAD/README.md) · [Source 2](https://github.com/apache/tvm/blob/HEAD/python/tvm/relax/backend/cuda/pipeline.py) · [Source 3](https://github.com/apache/tvm/blob/HEAD/docs/deep_dive/tensor_ir/tutorials/dlight_gpu_scheduling.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="bladedisc"></a>

### [BladeDISC](https://github.com/alibaba/BladeDISC)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Clusters supported framework operations and specializes MLIR fusion kernels with runtime shape predicates while supporting dynamic-shape execution in plugin or standalone modes.

**Scope:** Dynamic dimensions, supported fusion patterns, framework integration and CPU/GPU target capabilities constrain generated regions.

**Boundary:** Its README contains older framework validation matrices; current compatibility and performance should be checked against a pinned build, and unsupported operations may stay in the host framework.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `dynamic-shape-specialization`, `graph-fusion`, `graph-partitioning`, `hardware-codegen`.

**Constraints:** `shape`, `hardware`, `framework`.

**Evidence:** [Source 1](https://github.com/alibaba/BladeDISC/blob/HEAD/README.md) · [Source 2](https://github.com/alibaba/BladeDISC/blob/HEAD/tao_compiler/mlir/disc/transforms/disc_specialize_fusion_with_speculation.cc) · [Source 3](https://github.com/alibaba/BladeDISC/blob/HEAD/docs/developers/bladedisc_torch_overview.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="deepgemm"></a>

### [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

JIT-compiles tensor-core kernels with shape, tile and pipeline constants, using MoE-specific grouped layouts and optional fused expert computation/communication paths.

**Scope:** Supported NVIDIA architectures, precision/scaling formats, alignment and shared expert N/K dimensions determine legal GEMM and grouped-GEMM specializations.

**Boundary:** Input casting and transposition remain caller responsibilities, grouped experts have shape/alignment contracts, and broad feature listings do not establish support on every NVIDIA generation.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `jit-specialization`, `grouped-gemm`, `layout-specialization`, `compute-communication-fusion`.

**Constraints:** `hardware`, `precision`, `shape`, `layout`.

**Evidence:** [Source 1](https://github.com/deepseek-ai/DeepGEMM/blob/HEAD/README.md) · [Source 2](https://github.com/deepseek-ai/DeepGEMM/blob/HEAD/csrc/jit_kernels/impls/sm90_fp8_gemm_1d1d.hpp) · [Source 3](https://github.com/deepseek-ai/DeepGEMM/blob/HEAD/csrc/apis/gemm.hpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="draw-things"></a>

### [Draw Things Community](https://github.com/drawthingsai/draw-things-community)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Local-generation application/runtime route: compares integrated product scope and reusable execution layers.

Provides independent Swift model graphs and samplers with hardware-backed execution and a TeaCache implementation that switches between full and reduced model execution.

**Scope:** Serves local image and video generation across supported macOS and CUDA server deployments.

**Boundary:** The public repository is a growing set of application components, not proof that every part of the shipping application or all backends is open.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-graph`, `activation-reuse`.

**Constraints:** `device`, `model-family`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/drawthingsai/draw-things-community/blob/main/README.md) · [Source 2](https://github.com/drawthingsai/draw-things-community/blob/main/Libraries/SwiftDiffusion/Sources/Models/Flux1.swift) · [Source 3](https://github.com/drawthingsai/draw-things-community/blob/main/Libraries/SwiftDiffusion/Sources/TeaCache/TeaCache.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="dwarfstar"></a>

### [DwarfStar](https://github.com/antirez/ds4)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A separately implemented runtime links disclosed AI assistance to model execution and expert-residency control.

Executes selected DeepSeek, GLM and Qwen families through native model-specific paths, retaining non-routed state while fetching missing routed experts into a bounded SSD-streaming cache.

**Scope:** Supported model-specific GGUF layouts, backend capabilities and the memory remaining after non-routed weights, graph buffers and KV state determine which experts stay resident.

**Boundary:** The engine is intentionally not a generic GGUF runner, and SSD-streaming support and budgets vary by model and backend; capacity gains do not imply resident-speed decoding.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `expert-tiering`, `packed-low-bit`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/antirez/ds4/blob/HEAD/README.md) · [Source 2](https://github.com/antirez/ds4/blob/HEAD/docs/SSD_STREAMING.md) · [Source 3](https://github.com/antirez/ds4/blob/HEAD/metal/moe.metal).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `initial`.

</details>

<a id="edge-dit"></a>

### [edge-dit.cpp](https://github.com/THU-MIG/edge-dit.cpp)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Native diffusion route: useful adjacent comparison for component placement, reuse and compatibility boundaries.

Runs DiTs on ggml graphs with automatic quantization and placement, per-component or double-buffered block offload, VAE tiling and model-aware cache policies.

**Scope:** Prioritizes constrained GPU memory and explicit component placement, with CUDA as the primary optimized backend.

**Boundary:** Backend maturity and cache support differ by model; memory-budget comparisons require the same precision and offload policy.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `weight-quantization`, `block-offload`, `vae-tiling`, `activation-reuse`, `hybrid-parallelism`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/THU-MIG/edge-dit.cpp/blob/main/README.md) · [Source 2](https://github.com/THU-MIG/edge-dit.cpp/blob/main/docs/optimization/memory-efficient-execution.md) · [Source 3](https://github.com/THU-MIG/edge-dit.cpp/blob/main/src/core/backend/ggml/cuda/ed_async_offload.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="executorch"></a>

### [ExecuTorch](https://github.com/pytorch/executorch)

[foundation](systems.md#foundation) · `support` · `runtime` · `text / general` · **public code**

**Survey relevance:** Reusable runtime foundation or baseline for comparing retained services and implementation boundaries.

Exports PyTorch graphs ahead of time, partitions supported subgraphs to hardware delegates and plans reusable tensor storage for a lightweight on-device runtime.

**Scope:** Mobile and embedded device capabilities, delegate operator coverage and bounded memory requirements determine the exported program.

**Boundary:** Backend delegates may retain vendor SDK dependencies, and unsupported operators can remain in portable execution; whole-model acceleration depends on partition coverage.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `backend-delegation`, `memory-planning`, `selective-runtime`.

**Constraints:** `hardware`, `memory`, `deployment-footprint`.

**Evidence:** [Source 1](https://github.com/pytorch/executorch/blob/HEAD/README.md) · [Source 2](https://github.com/pytorch/executorch/blob/HEAD/exir/backend/backend_api.py) · [Source 3](https://github.com/pytorch/executorch/blob/HEAD/exir/passes/memory_planning_pass.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="flash-linear-attention"></a>

### [Flash Linear Attention](https://github.com/fla-org/flash-linear-attention)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Implements architecture-specific linear-attention and recurrent mixers with chunk-parallel prefill and state-update kernels, including fused gated-delta-rule intra-chunk computation.

**Scope:** The mixer equations, recurrent-state structure, sequence chunking and backend capabilities define legal execution decompositions.

**Boundary:** Replacing softmax attention with a linear mixer changes the model; these kernels accelerate compatible architectures rather than providing a semantics-preserving replacement for arbitrary attention.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `chunked-recurrence`, `recurrent-state-kernels`, `kernel-fusion`.

**Constraints:** `architecture`, `hardware`, `shape`, `state`.

**Evidence:** [Source 1](https://github.com/fla-org/flash-linear-attention/blob/HEAD/README.md) · [Source 2](https://github.com/fla-org/flash-linear-attention/blob/HEAD/fla/ops/gated_delta_rule/chunk.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="flash-attention"></a>

### [FlashAttention](https://github.com/Dao-AILab/flash-attention)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Implements attention with IO-aware tiled kernels and fused reductions, selecting hardware/shape-specific variants and providing KV-cache update-and-attend inference interfaces.

**Scope:** Attention head dimensions, dtype, mask/dropout mode and GPU generation constrain the fused kernel configuration and supported release path.

**Boundary:** Exact attention describes the mathematical operation, not guaranteed bitwise equality with every implementation; FA2, Hopper FA3 and CuTeDSL FA4 have different hardware and feature contracts.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `io-aware-tiling`, `online-softmax`, `kernel-fusion`.

**Constraints:** `hardware`, `shape`, `precision`, `memory`.

**Evidence:** [Source 1](https://github.com/Dao-AILab/flash-attention/blob/HEAD/README.md) · [Source 2](https://github.com/Dao-AILab/flash-attention/blob/HEAD/flash_attn/flash_attn_interface.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="flashinfer"></a>

### [FlashInfer](https://github.com/flashinfer-ai/flashinfer)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Builds or selects attention/GEMM/MoE kernels from dtype, head geometry, cache layout and workload metadata, with planned paged/ragged KV execution and specialized prefill/decode paths.

**Scope:** GPU architecture, head dimensions, precision, positional encoding, batch shape and KV layout determine eligible backends and generated kernel modules.

**Boundary:** It is a multi-backend kernel library and generator rather than a standalone inference server, and support varies by feature and compute capability.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `jit-specialization`, `backend-selection`, `paged-kv-kernels`, `workload-planning`.

**Constraints:** `hardware`, `shape`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/flashinfer-ai/flashinfer/blob/HEAD/README.md) · [Source 2](https://github.com/flashinfer-ai/flashinfer/blob/HEAD/flashinfer/decode.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="flashmla"></a>

### [FlashMLA](https://github.com/deepseek-ai/FlashMLA)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction.

Uses DeepSeek-specific latent/sparse-attention geometry, precomputed scheduler metadata and quantized KV layouts to run sparse decode/prefill and fused RoPE–attention paths.

**Scope:** At the checked HEAD, DeepSeek-V4.1 geometry, NVIDIA SM100/SM103 or Ascend 950, sparse indices and explicit FP8/FP4 KV layouts constrain the available kernels.

**Boundary:** The 2026-09-30 breaking release removed Hopper and earlier-model support and changed KV formats; old SM90/V3 descriptions apply only to the linked legacy commit. Fused RoPE paths have narrower backend support.

**Semantic considerations:** layout / scheduling, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-specific-attention`, `sparse-attention-kernel`, `fused-attention-boundary`.

**Constraints:** `model`, `hardware`, `precision`, `shape`.

**Evidence:** [Source 1](https://github.com/deepseek-ai/FlashMLA/blob/2e5429fc5653bab6e081f09477126f731882a6a9/README.md) · [Source 2](https://github.com/deepseek-ai/FlashMLA/blob/2e5429fc5653bab6e081f09477126f731882a6a9/flash_mla/flash_mla_interface.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="gufo"></a>

### [Gufo](https://github.com/gufo-org/gufo)

[core](systems.md#core) · `system` · `runtime` · `text / audio / image / video / multimodal` · **public code**

**Survey relevance:** Rebuilds a vertical native execution and serving stack around one integrated GPU platform, with deliberately selected models and model-owned kernels.

Owns per-model C++/HIP execution, kernels and state alongside serving, batching and continuation caching; Qwen paths integrate model-specific draft/verification cycles while reusing ROCm BLAS and adapted upstream code.

**Scope:** Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit.

**Boundary:** Quality is model-specific: Flash-Next retains a vision parity failure; Qwen-Image has only three complete qualification trajectories and H3 lacks full-video perceptual qualification. Published benchmarks are author-reported; AI authorship is not established.

**Semantic considerations:** configuration-dependent, reduced precision, target-verified proposals.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `model-specific-kernels`, `speculative-decoding`, `continuous-batching`, `conversation-cache`.

**Constraints:** `model`, `hardware`, `memory`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/README.md) · [Source 2](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/CMakeLists.txt) · [Source 3](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/DEVELOPMENT.md) · [Source 4](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/THIRD_PARTY_NOTICES.md) · [Source 5](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/src/models/qwen38_flash_next/engine.cpp) · [Source 6](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/models/qwen3.8-flash-next/QUALITY.md) · [Source 7](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/models/qwen-image-2.1/QUALITY.md) · [Source 8](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/models/minimax-h3/QUALITY.md) · [Source 9](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/TESTING.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="halogen-flash"></a>

### [Halogen Flash](https://github.com/peonist-ai/halogen-flash-server)

[core](systems.md#core) · `system` · `runtime` · `text` · **closed core**

**Survey relevance:** A model-and-device-specific runtime illustrates how narrow deployment contracts reshape implementation choices.

Ships a model-and-chip-specific inference binary with mixed-precision weight layouts, a paged n-gram lookup table and dedicated attention/expert execution for Qwen3.8-Flash-Next.

**Scope:** One model family and AMD gfx1151 unified-memory machines motivate tensor-specific precision choices and separate budgets for resident weights, KV state and the paged lookup table.

**Boundary:** The engine is distributed as a closed-source binary; public deployment files and quantization documentation cannot establish kernel implementation or all numerical-equivalence claims.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `mixed-precision-layout`, `paged-lookup-table`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/peonist-ai/halogen-flash-server/blob/HEAD/README.md) · [Source 2](https://github.com/peonist-ai/halogen-flash-server/blob/HEAD/docs/QUANT.md) · [Source 3](https://github.com/peonist-ai/halogen-flash-server/blob/HEAD/LICENSE.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="hidet"></a>

### [Hidet](https://github.com/hidet-org/hidet)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Compiles PyTorch or ONNX graphs to CUDA kernels using graph rewrites, tunable operator schedules and explicit mappings from logical tasks to hardware workers.

**Scope:** NVIDIA GPU inference, operator coverage, task layouts and tuning-space size constrain the generated execution.

**Boundary:** Hidet is an optimizing compiler/backend rather than a deployment-specific serving engine; tuning and frontend compatibility must be evaluated for the chosen workload.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hardware-codegen`, `task-mapping`, `kernel-autotuning`, `graph-fusion`.

**Constraints:** `hardware`, `shape`, `workload`.

**Evidence:** [Source 1](https://github.com/hidet-org/hidet/blob/HEAD/README.md) · [Source 2](https://github.com/hidet-org/hidet/blob/HEAD/python/hidet/transforms/lower_task_mapping.py) · [Source 3](https://github.com/hidet-org/hidet/blob/HEAD/python/hidet/ir/library/tune.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="iree"></a>

### [IREE](https://github.com/iree-org/iree)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **public code**

**Survey relevance:** Reusable compiler/runtime foundation for target-specific programs and execution orchestration.

Lowers MLIR programs into device executables and a runtime schedule, partitioning streamable work and planning resource lifetimes and allocations before deployment.

**Scope:** Hardware target, memory lifetime, asynchronous dependencies and the accepted input dialect constrain generated programs.

**Boundary:** IREE is a general compiler/runtime toolkit; importing a model and selecting a target do not by themselves establish competitive model-level performance.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `asynchronous-execution`, `memory-planning`, `hardware-codegen`.

**Constraints:** `hardware`, `memory`, `shape`.

**Evidence:** [Source 1](https://github.com/iree-org/iree/blob/HEAD/README.md) · [Source 2](https://github.com/iree-org/iree/blob/HEAD/compiler/src/iree/compiler/Dialect/Stream/Transforms/ScheduleExecution.cpp) · [Source 3](https://github.com/iree-org/iree/blob/HEAD/compiler/src/iree/compiler/Dialect/Stream/Transforms/ScheduleAllocation.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="iree-turbine"></a>

### [IREE Turbine](https://github.com/iree-org/iree-turbine)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Captures PyTorch modules or exported programs into IREE-compatible Torch IR, exposing AOT deployment, parameter handling and custom-operation integration.

**Scope:** PyTorch exportability, dynamic-shape representation, custom operations and compatible IREE compiler/runtime versions constrain deployment.

**Boundary:** Turbine is the PyTorch-to-IREE frontend and tooling layer, not an independent serving engine; the README warns that some dynamic-shape paths do not work with every head/release combination.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `graph-capture`, `custom-op-lowering`.

**Constraints:** `framework`, `shape`, `hardware`.

**Evidence:** [Source 1](https://github.com/iree-org/iree-turbine/blob/HEAD/README.md) · [Source 2](https://github.com/iree-org/iree-turbine/blob/HEAD/iree/turbine/aot/exporter.py) · [Source 3](https://github.com/iree-org/iree-turbine/blob/HEAD/iree/turbine/aot/compiled_module.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="iris"></a>

### [Iris](https://github.com/antirez/iris.c)

[core](systems.md#core) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** A native image-model runtime exposes which graph and execution responsibilities are taken out of a general framework.

Implements selected FLUX and Z-Image pipelines in C with Metal or CPU kernels, memory-mapped weights and release of text encoders after conditioning.

**Scope:** Targets selected image-model architectures and local machines, with an optimized Apple Silicon path and CPU fallbacks.

**Boundary:** Its supported architectures and precision paths are explicit; C implementation alone does not establish an end-to-end speed advantage over optimized frameworks.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `memory-mapping`, `model-specific-kernels`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/antirez/iris.c/blob/main/README.md) · [Source 2](https://github.com/antirez/iris.c/blob/main/iris_safetensors.c) · [Source 3](https://github.com/antirez/iris.c/blob/main/iris_transformer_flux.c).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="lightx2v"></a>

### [LightX2V](https://github.com/ModelTC/LightX2V)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image / video / audio` · **public code**

**Survey relevance:** Video inference framework route: compares breadth of model integration with narrower execution designs.

Combines model-specific inference paths with quantized operators, cache policies, parallel execution and a two-slot block-loading system for overlapping offload.

**Scope:** Targets large supported image and video models on memory-constrained accelerators and multi-device systems.

**Boundary:** Reported maximum speedups can combine runtime changes, quantization, step-distilled weights and lightweight VAEs, which need separate attribution.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-offload`, `weight-quantization`, `activation-reuse`, `hybrid-parallelism`.

**Constraints:** `device`, `memory-capacity`, `model-family`.

**Evidence:** [Source 1](https://github.com/ModelTC/LightX2V/blob/main/README.md) · [Source 2](https://github.com/ModelTC/LightX2V/blob/main/lightx2v/common/offload/manager.py) · [Source 3](https://github.com/ModelTC/LightX2V/blob/main/lightx2v/common/offload/block_loader.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="llama-cpp"></a>

### [llama.cpp](https://github.com/ggml-org/llama.cpp)

[foundation](systems.md#foundation) · `support` · `runtime` · `text` · **public code**

**Survey relevance:** General local-inference substrate and baseline; retained components must be distinguished from rewritten execution.

Loads GGUF model tensors and executes a native GGML graph through backend-specific quantized kernels, dispatching by tensor type and geometry with optional CPU/GPU layer placement.

**Scope:** Checkpoint quantization type, tensor layout, matrix geometry, CPU instruction sets and accelerator memory determine eligible kernels and placement.

**Boundary:** Backend and quantization support are not uniform across every operation or device; native low-bit execution does not imply identical accuracy or speed for all GGUF formats.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `quantized-layout`, `native-kernel-dispatch`, `cpu-gpu-placement`.

**Constraints:** `precision`, `hardware`, `layout`, `shape`, `memory`.

**Evidence:** [Source 1](https://github.com/ggml-org/llama.cpp/blob/HEAD/README.md) · [Source 2](https://github.com/ggml-org/llama.cpp/blob/HEAD/ggml/src/ggml-cpu/ggml-cpu.c) · [Source 3](https://github.com/ggml-org/llama.cpp/blob/HEAD/ggml/src/ggml-cuda/mmvq.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="magnitude"></a>

### [Magnitude](https://github.com/magnitudedev/magnitude)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A dedicated inference stack exposes its kernel-composition and model-execution boundary for construction analysis.

Its inspected Metal/MLX path captures typed operations, selects compatible kernel plans and emits specialized fused Metal entry points inside MLX native compilation.

**Scope:** Encoding, dtype, tensor geometry, layout, numerical contracts and target capabilities constrain kernel composition, while dynamic positions remain operands.

**Boundary:** The concrete source audit covers the inference-v2 Metal/MLX path only; it does not establish identical specialization depth for CUDA, AMD or CPU backends or the advertised speedups.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `jit-specialization`, `graph-fusion`, `kernel-planning`.

**Constraints:** `hardware`, `model`, `shape`, `precision`, `numerical-contract`.

**Evidence:** [Source 1](https://github.com/magnitudedev/magnitude/blob/HEAD/README.md) · [Source 2](https://github.com/magnitudedev/magnitude/blob/HEAD/inference-v2/design/kernels.md) · [Source 3](https://github.com/magnitudedev/magnitude/blob/HEAD/inference-v2/src/magnitude_engine/kernels/core/compiler.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="mflux"></a>

### [MFLUX](https://github.com/mflux-community/mflux)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** MLX-based model implementation route: contrasts retained tensor framework with more extensive native reconstruction.

Implements selected image model components natively in MLX, with on-load low-bit weight quantization and optional adapter baking into inference weights.

**Scope:** Primarily targets local Apple Silicon execution and explicitly supported MLX model implementations, with documented newer NVIDIA support.

**Boundary:** Quantized checkpoints and adapter baking have format and precision constraints; a native MLX port is not evidence of universal speedup or identical outputs.

**Semantic considerations:** configuration-dependent, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-mlx-runtime`, `weight-quantization`, `adapter-baking`.

**Constraints:** `device`, `model-family`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) · [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/common/README.md) · [Source 3](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/seedvr2/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="mirage"></a>

### [Mirage Persistent Kernel](https://github.com/mirage-project/mirage)

[core](systems.md#core) · `construction` · `compiler` · `text` · **public code**

**Survey relevance:** A model-to-persistent-program construction path connects generated execution schedules to a concrete runtime artifact.

Compiles an explicitly assembled LLM task graph into a persistent CUDA megakernel whose GPU workers and schedulers execute computation and communication across decoding steps.

**Scope:** NVIDIA GPU architecture, SM worker/scheduler allocation, model graph, batch shape and multi-GPU topology constrain the compiled execution.

**Boundary:** MPK requires supported task implementations and graph construction; its reported gains are workload-specific and are not an automatic guarantee for arbitrary Hugging Face models.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `persistent-execution`, `device-scheduling`, `graph-fusion`, `communication-fusion`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/mirage-project/mirage/blob/mpk/README.md) · [Source 2](https://github.com/mirage-project/mirage/blob/mpk/python/mirage/mpk/persistent_kernel.py) · [Source 3](https://github.com/mirage-project/mirage/blob/mpk/include/mirage/persistent_kernel/persistent_kernel.cuh).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="mlc-llm"></a>

### [MLC LLM](https://github.com/mlc-ai/mlc-llm)

[adjacent](systems.md#adjacent) · `construction` · `runtime` · `text` · **public code**

**Survey relevance:** Compiler specialization route: establishes existing model-to-deployment construction and portability trade-offs.

Uses a TVM LLM-specific compilation pipeline to fuse dequantization and normalization, specialize low-batch GEMV, dispatch target-specific KV kernels and execute compiled models through MLCEngine.

**Scope:** Target device, model architecture, quantization, sequence bounds, tensor parallelism and low-batch workload determine compilation and runtime choices.

**Boundary:** This is a broad multi-platform compiler-backed LLM engine, not a separate hand-written runtime for each model; support and tuning remain backend-dependent.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `graph-fusion`, `precision-fusion`, `kernel-autotuning`, `kv-management`.

**Constraints:** `hardware`, `model`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/mlc-ai/mlc-llm/blob/HEAD/README.md) · [Source 2](https://github.com/mlc-ai/mlc-llm/blob/HEAD/python/mlc_llm/compiler_pass/pipeline.py) · [Source 3](https://github.com/mlc-ai/mlc-llm/blob/HEAD/cpp/serve/engine.cc).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="ninfer"></a>

### [NInfer](https://github.com/Neroued/ninfer)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Rebuilds model execution and serving for selected Qwen checkpoints on one GPU; exposes the scope and ownership of a purpose-built stack.

Native model code composes operators; Program owns state, KV, workspace and CUDA Graph execution, while runtime manages request scheduling, cache retention and pause/resume.

**Scope:** Selected Qwen Dense/MoE checkpoints on Linux and one RTX 5090 (sm_120a), with one resident model and one to eight startup-fixed execution lanes.

**Boundary:** Weight/KV precision and speculative paths require configuration-specific checks; published results are author-reported. Agent instruction files and AI-client compatibility do not establish AI authorship.

**Semantic considerations:** configuration-dependent, reduced precision, target-verified proposals.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `cuda-graphs`, `low-bit-kernels`, `paged-kv`, `speculative-decoding`.

**Constraints:** `model`, `hardware`, `memory`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/README.md) · [Source 2](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/docs/maintainer/engine-architecture.md) · [Source 3](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/src/models/qwen3_5/execution/text.cpp) · [Source 4](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/docs/maintainer/build-system.md) · [Source 5](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/tests/README.md) · [Source 6](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/CONTRIBUTING.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="tensorrt"></a>

### [NVIDIA TensorRT](https://github.com/NVIDIA/TensorRT)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **closed core**

**Survey relevance:** Engine-building baseline with a closed optimizer/runtime core; compare disclosed interfaces and build cost.

Builds NVIDIA inference engines specialized to optimization-profile shapes and selected kernel tactics, recording profiled decisions in a reusable editable timing cache.

**Scope:** NVIDIA devices, supported operators, precision contracts and min/opt/max input-shape profiles define an engine build.

**Boundary:** The public repository contains plugins, parsers and samples, not the complete TensorRT optimizer/runtime core; internals beyond these interfaces were not inspected.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `tactic-selection`, `graph-fusion`, `shape-profiles`.

**Constraints:** `hardware`, `shape`, `precision`.

**Evidence:** [Source 1](https://github.com/NVIDIA/TensorRT/blob/HEAD/README.md) · [Source 2](https://github.com/NVIDIA/TensorRT/blob/HEAD/samples/sampleDynamicReshape/sampleDynamicReshape.cpp) · [Source 3](https://github.com/NVIDIA/TensorRT/blob/HEAD/samples/sampleEditableTimingCache/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="onediff"></a>

### [OneDiff](https://github.com/siliconflow/onediff)

[adjacent](systems.md#adjacent) · `construction` · `compiler` · `image / video` · **public code**

**Survey relevance:** Compiler-backed pipeline adaptation: compares generated execution without reconstructing a full serving stack.

Converts diffusion-model modules into deployable compiled modules through OneFlow or Nexfort and reuses compiled graphs to reduce recurring inference overhead.

**Scope:** Requires a compatible compiler backend, PyTorch/CUDA versions and shape policy, with dynamic shapes trading specialization against recompilation.

**Boundary:** The inspected public adapter code delegates core compilation to backend packages; this audit did not establish that every backend component is public or current-version compatible.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `graph-compilation`, `backend-dispatch`, `compiled-graph-cache`.

**Constraints:** `device`, `pipeline-shape`, `compile-amortization`.

**Evidence:** [Source 1](https://github.com/siliconflow/onediff/blob/main/README.md) · [Source 2](https://github.com/siliconflow/onediff/blob/main/src/onediff/infer_compiler/backends/nexfort/README.md) · [Source 3](https://github.com/siliconflow/onediff/blob/main/src/onediff/infer_compiler/backends/nexfort/deployable_module.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="onnxruntime-genai"></a>

### [ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai)

[foundation](systems.md#foundation) · `support` · `runtime` · `text / audio / multimodal` · **public code**

**Survey relevance:** General exported-model runtime baseline for portability and generation-state management.

Executes ONNX generative models through execution providers while selecting model- and device-specific convolutional, shared, sliding-window or quantized KV-state managers.

**Scope:** ONNX model contracts, execution-provider policy, attention/convolution structure and KV quantization determine the state-management path.

**Boundary:** This is a generative runtime on top of ONNX Runtime, not evidence that every execution provider accelerates every model or feature equally.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `backend-delegation`, `kv-management`, `model-state-specialization`, `generation-loop`.

**Constraints:** `hardware`, `model`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/microsoft/onnxruntime-genai/blob/HEAD/README.md) · [Source 2](https://github.com/microsoft/onnxruntime-genai/blob/HEAD/src/models/io/kv_cache.cpp) · [Source 3](https://github.com/microsoft/onnxruntime-genai/blob/HEAD/src/models/io/ep_managed_sliding_kv_cache.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="splash"></a>

### [Splash](https://github.com/incoai/splash)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Builds model-specific execution and serving on Apple silicon, with disclosed agent-generated kernels inside a native runtime.

A native runtime combines model-specific Metal kernels and matched DFlash2 drafts with its own batched execution, memory admission and KV/GDN prefix reuse; kernel agents generate specialized kernels.

**Scope:** Selected Qwen3.8-27B and Qwen3.6-35B-A3B checkpoints, plus compatible Ternary Bonsai 2, on Apple M3 or newer and macOS 26.4+; text and vision.

**Boundary:** AI assistance is disclosed for specialized kernel creation, not authorship of the whole engine. Quantization, INT8 KV and optional Neural Engine paths need configuration-specific checks; launch comparisons use recommended engine settings and do not isolate individual mechanisms.

**Semantic considerations:** configuration-dependent, reduced precision, target-verified proposals.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `shape-specialization`, `speculative-decoding`, `paged-kv`, `prefix-caching`, `agent-generated-kernels`.

**Constraints:** `model`, `hardware`, `memory`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/README.md) · [Source 2](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/DEVELOPMENT.md) · [Source 3](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/runtime/model/Runtime.cpp) · [Source 4](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/runtime/engine/Engine.cpp) · [Source 5](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/THIRD_PARTY_NOTICES) · [Source 6](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/docs/performance.md) · [Source 7](https://inco.ai/blog/splash/).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `keyword`.

</details>

<a id="stable-fast"></a>

### [Stable Fast](https://github.com/chengzeyi/stable-fast)

[adjacent](systems.md#adjacent) · `construction` · `compiler` · `image / video` · **public code**

**Survey relevance:** Framework compilation and capture route: compares incremental specialization and compilation amortization.

Traces Diffusers components into TorchScript, replaces common convolution/GEMM/GEGLU/normalization patterns with fused operators, and optionally captures CUDA graphs.

**Scope:** Targets NVIDIA GPU Diffusers pipelines whose repeated execution amortizes tracing and graph-capture costs.

**Boundary:** The README states active development is paused; traced graphs, lower-precision compute and backend compatibility require workload-specific validation.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `graph-compilation`, `kernel-fusion`, `cuda-graphs`, `layout-specialization`.

**Constraints:** `device`, `pipeline-shape`, `cpu-overhead`.

**Evidence:** [Source 1](https://github.com/chengzeyi/stable-fast/blob/main/README.md) · [Source 2](https://github.com/chengzeyi/stable-fast/blob/main/src/sfast/compilers/diffusion_pipeline_compiler.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="stable-diffusion-cpp"></a>

### [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Native diffusion framework route: compares existing cross-backend implementation and compatibility costs.

Implements image and video diffusion in ggml-backed C/C++ with quantized weights, tiled VAE execution and architecture-gated sample-cache policies.

**Scope:** Targets multiple local CPU and GPU backends and models that fit supported GGUF and execution paths.

**Boundary:** Cache modes and backend features are model-dependent; enabling a cache can alter outputs and is distinct from the native runtime rewrite.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `weight-quantization`, `vae-tiling`, `activation-reuse`.

**Constraints:** `device`, `model-family`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/leejet/stable-diffusion.cpp/blob/master/README.md) · [Source 2](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/caching.md) · [Source 3](https://github.com/leejet/stable-diffusion.cpp/blob/master/src/runtime/sample-cache.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="swifttransformer"></a>

### [SwiftTransformer](https://github.com/LLMServe/SwiftTransformer)

[foundation](systems.md#foundation) · `support` · `backend` · `text` · **public code**

**Survey relevance:** Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence.

Provides transformer execution with paged attention, continuous batching and tensor/pipeline parallelism behind Python bindings.

**Scope:** C++/CUDA execution substrate used by DistServe and FastServe

**Boundary:** Included as a concrete research backend dependency, not because of small code size; supported model families and software versions are limited.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `paged-attention`, `continuous-batching`, `native-runtime`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/LLMServe/SwiftTransformer/blob/main/README.md) · [Source 2](https://github.com/LLMServe/SwiftTransformer/blob/main/src/csrc/layer/attention.cc).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="tensorfold"></a>

### [TensorFold](https://github.com/ashhart/TensorFold)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A native Zig runtime exposes explicit model, format and platform contracts as a reconstruction boundary.

Executes a qualified set of model families from a native Zig binary using format-specific packed-weight readers and Metal/CUDA paths, fusing projections only when their packing contracts match.

**Scope:** Explicit model–checkpoint-format–platform qualification, quantization group/bit metadata and memory admission restrict which execution paths are accepted.

**Boundary:** The current 1.0.7 README describes a native serving runtime, so the older generic memory-virtualization label is stale; experimental readers and Living Weights must not be treated as generally qualified inference.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `packed-weight-readers`, `kernel-fusion`.

**Constraints:** `model`, `hardware`, `precision`, `memory`, `numerical-contract`.

**Evidence:** [Source 1](https://github.com/ashhart/TensorFold/blob/HEAD/README.md) · [Source 2](https://github.com/ashhart/TensorFold/blob/HEAD/docs/quantization.md) · [Source 3](https://github.com/ashhart/TensorFold/blob/HEAD/zig/src/families/nemotron/forward.zig).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="tinygrad"></a>

### [tinygrad](https://github.com/tinygrad/tinygrad)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Fuses lazy tensor graphs, searches kernel schedules and captures compiled execution sequences with TinyJit for reusable memory-planned replay.

**Scope:** Tensor metadata, chosen device backend and available schedule actions determine the captured and optimized execution.

**Boundary:** tinygrad is a full deep-learning stack with training support, not inherently a single-model inference engine; compact code size is not evidence of runtime superiority.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `graph-fusion`, `kernel-autotuning`, `graph-replay`, `memory-planning`.

**Constraints:** `hardware`, `shape`, `memory`.

**Evidence:** [Source 1](https://github.com/tinygrad/tinygrad/blob/HEAD/README.md) · [Source 2](https://github.com/tinygrad/tinygrad/blob/HEAD/tinygrad/engine/jit.py) · [Source 3](https://github.com/tinygrad/tinygrad/blob/HEAD/tinygrad/codegen/opt/search.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="torch-tensorrt"></a>

### [Torch-TensorRT](https://github.com/pytorch/TensorRT)

[foundation](systems.md#foundation) · `support` · `backend` · `text / image / general` · **public code**

**Survey relevance:** Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence.

Partitions exported PyTorch graphs into TensorRT-supported regions, compiles and caches those regions as engines and retains PyTorch execution for unsupported regions.

**Scope:** NVIDIA target hardware, TensorRT converter coverage, shape profiles and partition size constrain the delegated graph.

**Boundary:** It depends on TensorRT and can produce mixed PyTorch/TensorRT execution rather than a completely standalone runtime.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `backend-delegation`, `graph-partitioning`, `aot-specialization`, `engine-caching`.

**Constraints:** `hardware`, `framework`, `shape`.

**Evidence:** [Source 1](https://github.com/pytorch/TensorRT/blob/HEAD/README.md) · [Source 2](https://github.com/pytorch/TensorRT/blob/HEAD/py/torch_tensorrt/dynamo/_compiler.py) · [Source 3](https://github.com/pytorch/TensorRT/blob/HEAD/py/torch_tensorrt/dynamo/partitioning/_global_partitioner.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="construction"></a>

## Construction & validation tools / 构建与验证工具 (11)

**How are specialized programs built and checked?** Agents, kernel languages and evaluation infrastructure.

<a id="agentcompile"></a>

### [AgentCompile](https://github.com/veneno1213822/AgentCompile)

[adjacent](systems.md#adjacent) · `construction` · `research-prototype` · `text / image` · **review-use restriction**

**Survey relevance:** Agent-guided fusion route: a narrower construction comparison with explicit verification and timing caveats.

Combines LLM-guided ranking of bounded CUDA template candidates with contract-oriented fusion-kernel generation and an inference runtime.

**Scope:** The documented artifact targets selected models and an A800/SM80-oriented CUDA environment with model-specific fusion contracts.

**Boundary:** The inspected generic verifier and selector contain skipped checks and proxy timing placeholders; README claims about strict validation or never-worse execution require separate verification of the specialized paths.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-guided-compilation`, `template-selection`, `graph-fusion`, `kernel-validation`.

**Constraints:** `hardware`, `model`, `shape`.

**Evidence:** [Source 1](https://github.com/veneno1213822/AgentCompile/blob/043e454f55f69355e483920fa6292ff5731ecf41/README.md) · [Source 2](https://github.com/veneno1213822/AgentCompile/blob/043e454f55f69355e483920fa6292ff5731ecf41/planner/llm_recommender.py) · [Source 3](https://github.com/veneno1213822/AgentCompile/blob/043e454f55f69355e483920fa6292ff5731ecf41/verifier/verifier.py) · [Source 4](https://github.com/veneno1213822/AgentCompile/blob/043e454f55f69355e483920fa6292ff5731ecf41/benchmark/selector.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `initial`.

</details>

<a id="akg-agents"></a>

### [AKG Agents](https://github.com/mindspore-ai/akg)

[adjacent](systems.md#adjacent) · `construction` · `generator` · `general` · **public code**

**Survey relevance:** Agent-generated operator route: compares local code synthesis with integrated engine construction.

Generates and migrates accelerator kernels through multi-agent workflows, using UCB-based asynchronous candidate search and backend-specific verification and profiling workers.

**Scope:** Target backend/DSL, device architecture, reference framework, precision tolerance and concurrent-search budget constrain generated operators.

**Boundary:** AKG Agents is operator-generation infrastructure rather than a complete inference engine; backend readiness and the deprecated CLI must be distinguished from the current script/workflow APIs.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `adaptive-search`, `kernel-validation`, `profile-feedback`.

**Constraints:** `hardware`, `precision`, `dsl`.

**Evidence:** [Source 1](https://github.com/mindspore-ai/akg/blob/HEAD/akg_agents/README.md) · [Source 2](https://github.com/mindspore-ai/akg/blob/HEAD/akg_agents/python/akg_agents/op/workflows/adaptive_search_workflow.py) · [Source 3](https://github.com/mindspore-ai/akg/blob/HEAD/akg_agents/python/akg_agents/op/verifier/kernel_verifier.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `keyword`.

</details>

<a id="fastkernels"></a>

### [FastKernels](https://github.com/Snowflake-AI-Research/fastkernels)

[foundation](systems.md#foundation) · `support` · `verification` · `text / image / video / audio / multimodal / general` · **public code**

**Survey relevance:** Evaluation and integration reference for testing generated components in model workloads.

Replaces candidate operators in production-shaped model pipelines and evaluates both kernel-level numerics/timing and end-to-end token outputs, throughput and latency.

**Scope:** Architecture-specific interfaces, captured production shapes, shared weights, task composition and target GPU determine candidate validity.

**Boundary:** FastKernels also exposes a minimal serving path, but its primary distinction here is integrated evaluation; kernel-level tolerance checks and exact greedy-token tests cover different contracts.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `compositional-validation`, `kernel-replacement`, `end-to-end-evaluation`.

**Constraints:** `workload`, `hardware`, `model`.

**Evidence:** [Source 1](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/README.md) · [Source 2](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/fastkernels/bench.py) · [Source 3](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/fastkernels/eval.py) · [Source 4](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/docs/serving-framework-guide.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="helion"></a>

### [Helion](https://github.com/pytorch/helion)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Compiles Python tile programs into GPU kernels and automatically searches tile sizes, indexing, loop order and launch strategies for bound tensor arguments.

**Scope:** Input shapes/strides, device backend, traceable operations and autotuning budget constrain each bound kernel.

**Boundary:** Helion is a kernel authoring/compiler layer, not a serving runtime; first-use tuning can be substantial and optional agent source optimization is separate from the default configuration search.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `tile-layouts`, `kernel-autotuning`, `kernel-specialization`.

**Constraints:** `hardware`, `shape`, `layout`.

**Evidence:** [Source 1](https://github.com/pytorch/helion/blob/HEAD/README.md) · [Source 2](https://github.com/pytorch/helion/blob/HEAD/helion/runtime/kernel.py) · [Source 3](https://github.com/pytorch/helion/blob/HEAD/docs/api/autotuner.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="kernelagent"></a>

### [KernelAgent](https://github.com/meta-pytorch/KernelAgent)

[adjacent](systems.md#adjacent) · `construction` · `generator` · `general` · **public code**

**Survey relevance:** Agent-generated kernel and composed-workload route: a construction comparison whose integration scope must be established.

Decomposes PyTorch programs into fusable subgraphs, synthesizes Triton kernels, composes them back into a forward pass and iterates using correctness and hardware-profile feedback.

**Scope:** Traceable workload structure, target GPU, shape signatures, reference tensors and search/refinement budgets constrain synthesized code.

**Boundary:** It targets kernel/program synthesis rather than a production serving stack; composition verification is an explicit option and finite tests are not a general correctness proof.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `graph-partitioning`, `profile-feedback`, `kernel-validation`.

**Constraints:** `hardware`, `shape`, `workload`.

**Evidence:** [Source 1](https://github.com/meta-pytorch/KernelAgent/blob/HEAD/README.md) · [Source 2](https://github.com/meta-pytorch/KernelAgent/blob/HEAD/Fuser/compose_end_to_end.py) · [Source 3](https://github.com/meta-pytorch/KernelAgent/blob/HEAD/triton_kernel_agent/opt_worker_component/orchestrator/optimization_orchestrator.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `keyword`.

</details>

<a id="kernelbench"></a>

### [KernelBench](https://github.com/ScalingIntelligence/KernelBench)

[foundation](systems.md#foundation) · `support` · `verification` · `general` · **public code**

**Survey relevance:** Operator evaluation foundation; local test success does not establish integrated engine validity.

Compiles generated kernel implementations, compares them against PyTorch reference programs on randomized inputs and times only candidates that pass correctness checks.

**Scope:** Specified benchmark tasks, test-input generators, target GPU, numeric tolerances and measured baseline define what a score means.

**Boundary:** This is an evaluation environment, not an inference runtime; finite task-level success or speedup does not establish deployment-level gains.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `kernel-validation`, `benchmark-feedback`, `reference-comparison`.

**Constraints:** `hardware`, `shape`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/ScalingIntelligence/KernelBench/blob/HEAD/README.md) · [Source 2](https://github.com/ScalingIntelligence/KernelBench/blob/HEAD/src/kernelbench/eval.py) · [Source 3](https://github.com/ScalingIntelligence/KernelBench/blob/HEAD/EVAL.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="metainfer"></a>

### [MetaInfer](https://github.com/MetaInfer/MetaInfer)

[core](systems.md#core) · `construction` · `generator` · `text` · **public code**

**Survey relevance:** Connects a disclosed construction workflow to the VibeQwen engine case; the toolbox and generated engine are different artifacts.

Orchestrates coding agents to iteratively build deployment-specific inference servers, then launches fixed server contracts through correctness and performance oracle phases.

**Scope:** Requested model, hardware, parallelism, precision, API contract and iteration budget define the generated artifact.

**Boundary:** The inspected correctness oracle uses fixed prompts and LLM or heuristic judgments with hard/soft cases, which does not establish numerical equivalence to the original model.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `contract-validation`, `benchmark-feedback`.

**Constraints:** `model`, `hardware`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/MetaInfer/MetaInfer/blob/HEAD/README.md) · [Source 2](https://github.com/MetaInfer/MetaInfer/blob/HEAD/metainfer/tasks/gen_infer_framework/orchestrator/pipeline.py) · [Source 3](https://github.com/MetaInfer/MetaInfer/blob/HEAD/metainfer/tasks/gen_infer_framework/orchestrator/oracles/correctness.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `initial`.

</details>

<a id="sol-engine"></a>

### [Sol-Engine](https://github.com/NVlabs/Sana/tree/sol-engine)

[core](systems.md#core) · `construction` · `optimizer` · `image / video` · **public code**

**Survey relevance:** Connects agent-guided optimization with inspectable model runtimes and their acceptance checks.

Composes model-specific video inference patches for fusion, invariant/cross-KV reuse, approximate denoising cache and sparse attention, with agent-guided configuration and visual-quality checks.

**Scope:** Model pipeline, GPU architecture, tensor shapes, denoising schedule, precision and perceptual-quality thresholds constrain accepted configurations.

**Boundary:** Exact implementation optimizations and approximate cache/sparsity/precision changes must be separated; model-specific code and quality checks do not guarantee bitwise equivalence.

**Semantic considerations:** generated-artifact dependent, configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-optimization`, `graph-fusion`, `approximate-cache`, `sparse-attention`, `quality-validation`.

**Constraints:** `model`, `hardware`, `workload`, `precision`.

**Evidence:** [Source 1](https://github.com/NVlabs/Sana/blob/sol-engine/README.md) · [Source 2](https://github.com/NVlabs/Sana/blob/sol-engine/models/wan22_ti2v_5b/optimized/wan_kernel_runtime.py) · [Source 3](https://github.com/NVlabs/Sana/blob/sol-engine/models/wan22_ti2v_5b/optimized/cache_runtime.py) · [Source 4](https://github.com/NVlabs/Sana/blob/sol-engine/tools/vision/lpips_judge.py) · [Source 5](https://github.com/NVlabs/Sana/blob/sol-engine/techniques/sparse_backends/sol_attn/interface.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `initial`.

</details>

<a id="spec-bench"></a>

### [Spec-Bench](https://github.com/hemingkx/Spec-Bench)

[foundation](systems.md#foundation) · `support` · `verification` · `text` · **public code**

**Survey relevance:** Evaluation reference for matching speculative-decoding workloads and baseline conditions.

Integrates draft/verification methods with shared task data, accepted-token statistics, timing reports and output-comparison scripts.

**Scope:** Comparing speculative decoding under matched devices and workloads

**Boundary:** A benchmark artifact rather than a runtime; published leaderboard conditions do not validate unrelated hardware, checkpoints or serving loads.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `speculative-evaluation`, `output-comparison`.

**Constraints:** `workload`, `execution`.

**Evidence:** [Source 1](https://github.com/hemingkx/Spec-Bench/blob/main/Readme.md) · [Source 2](https://github.com/hemingkx/Spec-Bench/blob/main/evaluation/speed.py) · [Source 3](https://github.com/hemingkx/Spec-Bench/blob/main/evaluation/equal.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="tilelang"></a>

### [TileLang](https://github.com/tile-ai/tilelang)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / video / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Lowers tile-level kernel programs through target-specific layout and software-pipeline passes, generating GPU/accelerator code for tiled memory movement and matrix operations.

**Scope:** Device architecture, tile shapes, tensor-memory features, data precision and supported backend passes constrain generated kernels.

**Boundary:** TileLang is a kernel DSL/compiler, not a full inference runtime; backend maturity differs and some targets deliberately disable unvalidated asynchronous pipeline paths.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hardware-codegen`, `tile-layouts`, `software-pipelining`, `kernel-autotuning`.

**Constraints:** `hardware`, `shape`, `precision`.

**Evidence:** [Source 1](https://github.com/tile-ai/tilelang/blob/HEAD/README.md) · [Source 2](https://github.com/tile-ai/tilelang/blob/HEAD/tilelang/engine/lower.py) · [Source 3](https://github.com/tile-ai/tilelang/blob/HEAD/src/transform/pipeline_planning.cc).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="triton"></a>

### [Triton](https://github.com/triton-lang/triton)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / video / general` · **public code**

**Survey relevance:** Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces.

Compiles block-structured kernel programs for a selected GPU target and specializes cached binaries and autotuned launch configurations to argument signatures and compile-time constants.

**Scope:** Target architecture, pointer/value signatures, compile-time constants, warp/stage counts and autotuning keys determine kernel variants.

**Boundary:** Triton supplies kernel construction infrastructure; it does not supply model loading, serving policy or end-to-end inference correctness by itself.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hardware-codegen`, `kernel-specialization`, `kernel-autotuning`.

**Constraints:** `hardware`, `shape`, `precision`.

**Evidence:** [Source 1](https://github.com/triton-lang/triton/blob/HEAD/README.md) · [Source 2](https://github.com/triton-lang/triton/blob/HEAD/python/triton/compiler/compiler.py) · [Source 3](https://github.com/triton-lang/triton/blob/HEAD/python/triton/runtime/autotuner.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

