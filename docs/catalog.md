# Project catalog / 项目全目录

> Generated from [projects.csv](../catalog/projects.csv); edit the CSV, then run the generator.

[Home](../README.md) · [中文首页](../README_CN.md) · [Systems & construction](systems.md) · [Comparison](comparison.md) · [Taxonomy](taxonomy.md) · [Evidence policy](evidence-policy.md)

126 entries. Source review: 2026-10-14. Descriptions report inspected mechanisms; no project benchmark was independently reproduced in this survey.

Use the family links below, or search this page for a model, device, mechanism or project. Source visibility is not a license or correctness certification. Semantic labels identify evaluation obligations, not proven equivalence.

[Data residency & movement](#memory) · [Numerical representation](#precision) · [Selective computation](#selection) · [Computation reuse](#reuse) · [Generation order](#decoding) · [Parallelism & scheduling](#serving) · [Compiled & native execution](#execution) · [Construction & validation tools](#construction)

<a id="memory"></a>

## Data residency & movement / 数据驻留与搬移 (16)

**What stays close to compute?** Place, page, prefetch or offload weights, experts and KV state.

<a id="anemll-flash-llama"></a>

### [ANEMLL Flash llama.cpp](https://github.com/Anemll/anemll-flash-llama.cpp)

[core](systems.md#core) · `system` · `backend` · `text` · **public code**

**Survey relevance:** A substantial fork exposes exactly which graph/runtime boundary must change to support explicit expert residency.

Adds expert sidecars, native expert-to-slot mapping and layer-major prefill to llama.cpp, reusing each staged expert across relevant prompt rows.

**Scope:** Selected GGUF MoE architectures on Apple Silicon with sidecar expert storage and bounded slot-bank memory.

**Boundary:** Model maturity varies; optional top-k reductions and shared-only diagnostics change computation and must not be compared as exact execution.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-streaming`, `slot-bank`, `layer-major-prefill`, `graph-rewrite`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/README.md) · [Source 2](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/src/llama-context.cpp) · [Source 3](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/native-slot-bank-porting.md) · [Source 4](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/flashmoe-layer-major-dedup-single-sidecar.md) · [Source 5](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/moe-bank-modeling-workflow.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="colibri"></a>

### [Colibri](https://github.com/JustVugg/colibri)

[core](systems.md#core) · `system` · `runtime` · `text / image / multimodal` · **public code**

**Survey relevance:** Exposes the alternative of several small architecture-specific execution programs sharing selected components.

Keeps dense state resident and streams routed experts through model-family-specific execution paths, with optional CPU/GPU tier placement and specialized containers.

**Scope:** Models much larger than RAM, with architecture-specific C engines and optional device-specific backends.

**Boundary:** Backend maturity, numerical formats and speculative/approximate options vary per engine; synthetic oracle agreement does not establish every advertised model/backend combination.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `expert-streaming`, `heterogeneous-placement`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/README.md) · [Source 2](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/c/qwen36.c) · [Source 3](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/docs/qwen36.md) · [Source 4](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/CONTRIBUTING.md) · [Source 5](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/THIRD_PARTY_NOTICES.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

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

<a id="hybrimoe"></a>

### [HybriMoE](https://github.com/PKU-SEC-Lab/HybriMoE)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** Historical/adjacent heterogeneous MoE route directly referenced by newer native systems; establishes prior art for expert placement and movement.

Extends a KTransformers-based execution path with hybrid CPU/GPU expert scheduling, impact-driven prefetching and score-based expert-cache management.

**Scope:** MoE models exceeding GPU memory incur on-demand expert-loading latency and unbalanced CPU/GPU use.

**Boundary:** The official prototype depends on PyTorch/KTransformers and model-specific optimization rules. Paper-level claims are not independently reproduced in this audit.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hybrid-expert-scheduling`, `expert-prefetch`, `expert-caching`.

**Constraints:** `model`, `hardware`, `memory`.

**Evidence:** [Source 1](https://github.com/PKU-SEC-Lab/HybriMoE/blob/508a85b9a43dff37124370d8816e411e74827803/README.md) · [Source 2](https://github.com/PKU-SEC-Lab/HybriMoE/blob/508a85b9a43dff37124370d8816e411e74827803/ktransformers/operators/experts.py) · [Source 3](https://github.com/PKU-SEC-Lab/HybriMoE/blob/508a85b9a43dff37124370d8816e411e74827803/ktransformers/ktransformers_ext/operators/llamafile/moe.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="infernix"></a>

### [Infernix](https://github.com/wallawalla47/infernix)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Substantial descendant reconstructing heterogeneous execution for a model too large for GPU memory, with direct AI-development disclosure.

Extends NInfer with a GPU hot-expert cache, pinned-host experts, CPU computation of selected misses, overlapped PCIe transfers and an NVMe-backed n-gram volume.

**Scope:** Qwen Flash-Next experts and n-gram embeddings exceed a single RTX 5090’s memory, while local agent sessions demand prefix reuse and bounded concurrency.

**Boundary:** Hobby project; author warns AI-written descriptions may be incomplete. Strata comparisons use different native quantizations, and long-context/low-bit modes require separate quality qualification.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-caching`, `cpu-gpu-scheduling`, `nvme-embedding-access`.

**Constraints:** `model`, `hardware`, `memory`, `workload`.

**Evidence:** [Source 1](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/README.md) · [Source 2](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/src/ops/offloaded_sparse_moe/cpu/miss_service.cpp) · [Source 3](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/src/models/qwen4_exp/execution/expert_stream.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `dependency`.

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

<a id="swiftlet"></a>

### [Swiftlet](https://github.com/leonickson1/Swiftlet)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Links explicit AI-assisted authorship to a model-family-specific runtime and documented reference-based validation.

Implements Swift/Metal forward paths with a small resident dense core, fixed-stride expert containers, pread slot caching and native KV/recurrent state.

**Scope:** Selected Qwen hybrid MoE architectures on macOS/iOS, using qpack containers and bounded resident memory.

**Boundary:** The public roadmap notes expensive long-prompt prefill and limited phone throughput; quantization tiers have different quality behavior.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `expert-streaming`, `model-specific-container`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/README.md) · [Source 2](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Sources/SwiftletCore/ExpertCache.swift) · [Source 3](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Sources/SwiftletCore/QwenCPUModel.swift) · [Source 4](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Tests/SwiftletCoreTests/IncrementalDecodeTests.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `dependency`.

</details>

<a id="swiftlm"></a>

### [SwiftLM](https://github.com/SharpAI/SwiftLM)

[core](systems.md#core) · `system` · `backend` · `text / multimodal` · **public code**

**Survey relevance:** Shows substantial backend reconstruction while retaining the MLX ecosystem and serving integration.

Extends MLX Swift execution through maintained forks, explicit expert reads, asynchronous I/O workers and synchronization boundaries coordinated with model generation.

**Scope:** Oversized MoE checkpoints on Apple Silicon with explicit SSD streaming alongside selected speculative and memory controls.

**Boundary:** Streaming and speculative verification can multiply I/O; upstream synchronization broke quantized streaming in earlier releases, and fixed-version results must not be generalized.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-streaming`, `asynchronous-io`, `specialized-backend`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/README.md) · [Source 2](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/Package.swift) · [Source 3](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/docs/moe_ssd_streaming_architecture.md) · [Source 4](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/Sources/MLXInferenceCore/SSDStreamingRecovery.swift) · [Source 5](https://github.com/SharpAI/mlx-swift-lm/blob/4f1fdaabeb490d3e97b0ff71fc0132bca4078fa2/Libraries/MLXLMCommon/SwitchLayers.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="tuff"></a>

### [TUFF](https://github.com/rexmhall09/TUFF)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** A disclosed substantial fork shows how a narrow streaming runtime is adapted into several qualified model paths.

Extends a Swift/Metal runtime with model-specific forward paths, bounded expert streaming, resident state and a separate inference service.

**Scope:** Selected MoE families on Apple Silicon Macs with limited unified memory and SSD capacity.

**Boundary:** Author testing centers on a 16 GB M2; model capability, vision support and performance differ by machine. A UI feature comparison is not a speed benchmark.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-streaming`, `native-model-path`, `bounded-memory`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/README.md) · [Source 2](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/CONTRIBUTING.md) · [Source 3](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/docs/HOW_TUFF_WORKS.md) · [Source 4](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/Sources/TUFFEngine/Infrastructure/Streaming/PreadExpertStreamer.swift) · [Source 5](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/Sources/TUFFEngine/Runtime/Inference/RealForwardRunner.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `dependency`.

</details>

<a id="turbo-fieldfare"></a>

### [TurboFieldfare](https://github.com/drumih/turbo-fieldfare)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** A single-model native runtime publishes a detailed sequence of accepted and rejected construction experiments.

Keeps common weights and FP16 KV resident, reads routed experts with bounded pread slot caches, and coordinates chunked prefill and Metal execution.

**Scope:** Gemma 4 26B-A4B on memory-constrained Apple Silicon, with separate optional vision support.

**Boundary:** Research system with a narrow architecture contract; reported footprint excludes the full disk checkpoint and throughput depends on cache warmth, context and hardware.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `expert-streaming`, `bounded-cache`, `native-model-path`, `chunked-prefill`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/README.md) · [Source 2](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/SYSTEM_DESIGN.md) · [Source 3](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/OPTIMIZATION_JOURNEY.md) · [Source 4](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/experiments/EXPERIMENT_INVENTORY.md) · [Source 5](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/IMPLEMENTATION_REFERENCES.md) · [Source 6](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/Sources/TurboFieldfare/Infrastructure/Streaming/PreadExpertStreamer.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="vllm"></a>

### [vLLM](https://github.com/vllm-project/vllm)

[foundation](systems.md#foundation) · `support` · `runtime` · `text` · **public code**

**Survey relevance:** General-engine reference for the VibeQwen construction case and upstream serving infrastructure retained by the Radiance specialized backend.

Manages attention state as pooled KV blocks with reference-counted prefix sharing and schedules token-budgeted work across requests, allocating cache slots as execution advances.

**Scope:** Variable request lengths, overlapping prompts, finite KV capacity and layer-specific attention/state layouts determine block ownership and admission.

**Boundary:** Paged KV management is one subsystem in a broad runtime; prefix reuse requires matching cache identity, and hybrid attention/state models need distinct cache rules rather than a universal layout.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `paged-kv`, `prefix-reuse`, `continuous-batching`.

**Constraints:** `memory`, `workload`, `context`, `model`.

**Evidence:** [Source 1](https://github.com/vllm-project/vllm/blob/HEAD/README.md) · [Source 2](https://github.com/vllm-project/vllm/blob/HEAD/vllm/v1/core/block_pool.py) · [Source 3](https://github.com/vllm-project/vllm/blob/HEAD/vllm/v1/core/sched/scheduler.py) · [Source 4](https://github.com/vllm-project/vllm/blob/HEAD/docs/design/hybrid_kv_cache_manager.md) · [Source 5](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/README.md).

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

**Survey relevance:** Model preparation used for the Nunchaku/SVDQuant execution path; calibration and exported weights must be distinguished from runtime gains.

Calibrates quantization and SVDQuant low-rank outlier decomposition, evaluates compressed models and exports checkpoints into runtime-specific deployment layouts.

**Scope:** Requires calibration data, supported model adapters and a compatible deployment engine such as Nunchaku for actual low-bit acceleration.

**Boundary:** Fake-quantized evaluation does not itself provide fast low-bit execution; preparation cost and deployment runtime gains are separate.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `post-training-quantization`, `low-rank-outlier-decomposition`, `checkpoint-conversion`.

**Constraints:** `low-precision`, `calibration`, `deployment-backend`.

**Evidence:** [Source 1](https://github.com/nunchux-ai/deepcompressor/blob/main/README.md) · [Source 2](https://github.com/nunchux-ai/deepcompressor/blob/main/examples/diffusion/README.md) · [Source 3](https://github.com/nunchux-ai/nunchaku/blob/main/README.md).

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

**Survey relevance:** Quantized linear-kernel and packing reference used in the ExLlamaV3 construction account; separates reusable low-level work from engine ownership.

Repacks INT4 weights/scales offline and overlaps asynchronous loads, dequantization and tensor-core MMA in a shape-specialized FP16×INT4 CUDA kernel.

**Scope:** Weight-only INT4 formats, compatible group/shape alignment and NVIDIA tensor-core hardware enable its inference-oriented memory/compute pipeline.

**Boundary:** The original project is a specialized linear kernel and packing format, not a complete server or a claim of fourfold end-to-end speedup for all models and batches.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `offline-layout`, `dequant-mma-pipeline`, `weight-streaming`.

**Constraints:** `hardware`, `precision`, `shape`, `layout`.

**Evidence:** [Source 1](https://github.com/IST-DASLab/marlin/blob/HEAD/README.md) · [Source 2](https://github.com/IST-DASLab/marlin/blob/HEAD/marlin/marlin_cuda_kernel.cu) · [Source 3](https://github.com/turboderp-org/exllamav3/blob/HEAD/README.md).

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

**Survey relevance:** Trellis quantization and matching execution provide a representation-design reference credited in the ExLlamaV3 case, rather than a second complete engine.

Quantizes incoherence-transformed weights with bitshift trellis codes and executes supported low-bit encodings through matching BitshiftLinear matrix-vector kernels.

**Scope:** Trellis/codebook parameters, tile dimensions and the supported 2/3/4-bit HYB encoding determine which quantized artifact has a fast inference path.

**Boundary:** The supplied fast kernels cover specific HYB-code settings, and the README states public interactive generation does not include the matrix fusion used for its headline timing table.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `trellis-quantization`, `packed-matvec`, `hadamard-transform`.

**Constraints:** `precision`, `codebook`, `shape`, `hardware`.

**Evidence:** [Source 1](https://github.com/Cornell-RelaxML/qtip/blob/HEAD/README.md) · [Source 2](https://github.com/Cornell-RelaxML/qtip/blob/HEAD/lib/codebook/bitshift.py) · [Source 3](https://github.com/turboderp-org/exllamav3/blob/HEAD/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="rocmfpx"></a>

### [ROCmFPX](https://github.com/ROCmFPX/ROCmFPX)

[adjacent](systems.md#adjacent) · `system` · `backend` · `text` · **public code**

**Survey relevance:** Adjacent format/backend construction route used by specialized Strix forks; separate from a new complete model execution stack.

A llama.cpp downstream defines ROCmFPX quantization blocks, conversion policies and backend kernels, including RDNA3-specific MMQ layouts and an optional Vulkan plugin.

**Scope:** AMD RDNA execution motivates compact weight blocks with explicit disk contracts and matching CPU, Vulkan and HIP arithmetic.

**Boundary:** Experimental formats and recipe-dependent accuracy; frozen tensor layouts do not imply all backend combinations are equally qualified. Preserve original and downstream provenance.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `quantized-formats`, `backend-kernels`, `layout-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/README.md) · [Source 2](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/docs/rocmfpx/README.md) · [Source 3](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/ggml/rocmfpx/rocmfpx_mmq_rdna3.cuh) · [Source 4](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/docs/rocmfpx/UPSTREAM-MAINTENANCE.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="sageattention"></a>

### [SageAttention](https://github.com/thu-ml/SageAttention)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text / image / video` · **public code**

**Survey relevance:** Low-precision attention component integrated into the included FastVideo/video execution paths, with a separate quality-validation obligation.

Applies outlier smoothing and hardware-specific low-precision QK and PV attention kernels, dispatching among INT8/FP8 or newer architecture-specific variants.

**Scope:** Targets supported NVIDIA architectures, layouts and head dimensions, with precision choice constrained by model sensitivity.

**Boundary:** It is an operator library rather than an end-to-end diffusion runtime; operator speedups and reported quality metrics do not guarantee equal pipeline gains or identical outputs.

**Semantic considerations:** reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `quantized-attention`, `outlier-smoothing`, `device-dispatch`.

**Constraints:** `device`, `low-precision`, `attention-shape`.

**Evidence:** [Source 1](https://github.com/thu-ml/SageAttention/blob/main/README.md) · [Source 2](https://github.com/thu-ml/SageAttention/blob/main/sageattention/core.py) · [Source 3](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/fastvideo/attention/backends/sage_attn.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="selection"></a>

## Selective computation / 选择性计算 (2)

**Which work can be omitted?** Select neurons, tokens or attention blocks; expose approximation.

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

## Computation reuse / 计算复用 (2)

**Which earlier results can be reused?** Reuse request prefixes, features or attention across steps.

<a id="sglang"></a>

### [SGLang](https://github.com/sgl-project/sglang)

[foundation](systems.md#foundation) · `support` · `runtime` · `text` · **public code**

**Survey relevance:** Shared serving infrastructure used alongside KTransformers and model components reused by Sol-Engine; separates specialized execution from shared services.

Indexes reusable prefix KV state in a radix tree, protects active nodes with references and offers cache-aware queue policies that prioritize requests using matched-prefix information.

**Scope:** Shared token prefixes within compatible cache namespaces, finite device memory and request arrivals make prefix matching and cache-aware batching effective.

**Boundary:** Prefix hits require compatible token and extra-key namespaces; cache-aware policies are configurable and must not be assumed to be the default or to benefit workloads without shared prefixes.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `radix-prefix-reuse`, `cache-aware-scheduling`, `continuous-batching`.

**Constraints:** `workload`, `memory`, `context`, `model`.

**Evidence:** [Source 1](https://github.com/sgl-project/sglang/blob/HEAD/README.md) · [Source 2](https://github.com/sgl-project/sglang/blob/HEAD/python/sglang/srt/mem_cache/radix_cache.py) · [Source 3](https://github.com/sgl-project/sglang/blob/HEAD/python/sglang/srt/managers/schedule_policy.py) · [Source 4](https://github.com/NVlabs/Sana/blob/sol-engine/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="videosys"></a>

### [VideoSys](https://github.com/NUS-HPC-AI-Lab/VideoSys)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `video` · **public code**

**Survey relevance:** Integrated video execution combining attention reuse and dynamic device partitioning; a concrete comparison for the reconstructed video runtimes in this collection.

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

<a id="decoding"></a>

## Generation order / 生成顺序 (2)

**Can more output be produced per step?** Draft and verify tokens, or reorganize block generation.

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

<a id="serving"></a>

## Parallelism & scheduling / 并行与调度 (7)

**Who executes what, and when?** Partition stages, devices and requests around workload constraints.

<a id="gufo-rdma"></a>

### [Gufo RDMA](https://github.com/neuhaus/gufo)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Substantive deployment reconstruction from one unified-memory machine to two synchronized hosts, not merely another binary package.

Adds model-specific tensor partitioning, RDMA collectives and mirrored request execution to Gufo, using libibverbs over InfiniBand, RoCE or qualified USB4 networking.

**Scope:** Two Strix Halo machines can jointly host higher-precision Qwen Flash-Next weights, but request state, tensors and speculative execution must remain synchronized across hosts.

**Boundary:** Optional build and two-host network setup required; multi-host support is limited to Qwen3.8 Flash-Next. One-host benchmark tables do not measure TP2.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `tensor-parallelism`, `rdma`, `mirrored-request-state`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/README.md) · [Source 2](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/docs/models/qwen3.8-flash-next/TP2.md) · [Source 3](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/src/models/qwen38_flash_next/distributed/tp_partition.cpp) · [Source 4](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/src/cli/serve/tp_executor.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="llaminar"></a>

### [Llaminar](https://github.com/Llaminar/llaminar)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Native mixed-hardware construction route: owns model graphs, execution plans and cross-vendor coordination rather than wrapping existing engines.

Builds model-specific compute graphs and rank plans, placing tensor/pipeline stages and MoE experts across devices; retained native graphs coordinate through NCCL, RCCL, MPI or heterogeneous host bridges.

**Scope:** A selected mixture of x86 CPUs, SM86 NVIDIA GPUs and gfx906 AMD GPUs requires explicit placement and communication across vendor-specific execution stacks.

**Boundary:** Alpha; tested hardware/model recipes are bounded. Current production activations are FP32; unsupported capture combinations error rather than silently executing eagerly.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `heterogeneous-execution`, `graph-capture`, `tensor-pipeline-parallelism`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/README.md) · [Source 2](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/execution/local_execution/engine/ForwardExecutionEngine.cpp) · [Source 3](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/collective/backends/HeterogeneousBackend.cpp) · [Source 4](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/planning/AutomaticOrchestrationPlanner.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="streamdiffusion"></a>

### [StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Earlier workload-specific pipeline reconstruction is a comparison for newer causal video engines; most model components remain supplied by Diffusers.

Reorganizes Diffusers components into StreamBatch execution with residual guidance, input filtering and optional compiled UNet/VAE paths.

**Scope:** Interactive SD/LCM image streams with overlapping denoising steps.

**Boundary:** LCM weights, guidance approximation and skipped similar frames change the workload or outputs; stream FPS must not be read as unchanged-model acceleration.

**Semantic considerations:** layout / scheduling, selective approximation, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `stream-batching`, `guidance-reuse`, `input-filtering`.

**Constraints:** `model-family`, `latency`, `workload`.

**Evidence:** [Source 1](https://github.com/cumulo-autumn/StreamDiffusion/blob/b623251dc055e1fd858d53509aa43e09dfc5cdc0/README.md) · [Source 2](https://github.com/cumulo-autumn/StreamDiffusion/blob/b623251dc055e1fd858d53509aa43e09dfc5cdc0/src/streamdiffusion/pipeline.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="streamdiffusion-v2"></a>

### [StreamDiffusionV2](https://github.com/chenfengxu714/StreamDiffusionV2)

[core](systems.md#core) · `system` · `runtime` · `video` · **public code**

**Survey relevance:** Reconstructs causal video execution around chunked denoising and distributed KV ownership; concrete source and adopter evidence connect a specialized schedule to an integrated streaming artifact.

Reorganizes denoising across streamed chunks and stages, with model-aware KV state and distributed cache ownership rather than an offline wrapper alone.

**Scope:** Causal Wan video generation with low-latency streaming and single/multiple GPU execution.

**Boundary:** Causal/distilled checkpoints and optional lightweight decoding change the comparison target; paper features and README roadmap items must not be assumed present in every released path.

**Semantic considerations:** layout / scheduling, model / router training, configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `stream-batching`, `pipeline-parallelism`, `kv-state-management`.

**Constraints:** `model-family`, `latency`, `workload`.

**Evidence:** [Source 1](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/README.md) · [Source 2](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamdiffusionv2/pipeline.py) · [Source 3](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamv2v/inference_pipe.py) · [Source 4](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamv2v/communication/kv_cache_manager.py) · [Source 5](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/tools/eval_video_metrics.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="telefuser"></a>

### [TeleFuser](https://github.com/Tele-AI/TeleFuser)

[core](systems.md#core) · `system` · `runtime` · `video / image / audio / multimodal` · **public code**

**Survey relevance:** Builds model-specific generation stages together with bounded streaming dataflow, retained session state and execution leases, connecting model execution ownership to an interactive serving workload.

Owns model pipelines and staged denoising, plus an actor-based streaming scheduler that separates retained session state from execution leases and applies backpressure.

**Scope:** Streaming generative/world-model workloads with per-session state, bounded queues and GPU resource groups.

**Boundary:** Transport delivery FPS differs from model compute FPS. In the inspected LingBot service, session residency and GPU execution leases are separate; other services can differ. Optional cache/sparsity/precision modes change semantics.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `stateful-streaming`, `resource-scheduling`, `model-specific-graph`, `block-offload`.

**Constraints:** `model-family`, `latency`, `workload`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/README.md) · [Source 2](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/docs/en/stream_scheduler.md) · [Source 3](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/telefuser/pipelines/wan_video/single_dit_denoising.py) · [Source 4](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/telefuser/pipelines/wan_video/wan21_video.py) · [Source 5](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/benchmarks/telefuser_aiperf/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="tensorrt-llm"></a>

### [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

[foundation](systems.md#foundation) · `support` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** General-engine comparison point in the VibeQwen case; record matching model, hardware, precision and workload before comparing the specialized result.

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

## Compiled & native execution / 编译与原生执行 (72)

**How does a graph become an executable?** Fuse, lower, specialize and dispatch graphs or native kernels.

<a id="ane-lm"></a>

### [ANE-LM](https://github.com/johnmai-dev/ANE-LM)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** The direct precursor of ane.cpp anchors what the later measurement-driven fork actually changed.

Implements Qwen forward paths combining compiled ANE kernels with CPU operations and a persistent compile cache.

**Scope:** Dense Qwen3 and Qwen3.5 text execution using private Apple Neural Engine APIs.

**Boundary:** Private API dependence and narrow model support limit portability; public generation examples do not establish broad quality qualification.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `mil-compilation`, `heterogeneous-execution`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/johnmai-dev/ANE-LM/blob/04b1af12aa30b3f280f511d286398469764b4326/README.md) · [Source 2](https://github.com/johnmai-dev/ANE-LM/blob/04b1af12aa30b3f280f511d286398469764b4326/models/llm/qwen3.cpp) · [Source 3](https://github.com/johnmai-dev/ANE-LM/blob/04b1af12aa30b3f280f511d286398469764b4326/core/ane_runtime.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="ane-cpp"></a>

### [ane.cpp](https://github.com/skyfallsin/ane.cpp)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Connects hardware probes and a documented keep/discard workflow to concrete changes in a specialized execution stack.

Compiles weight-bearing MIL convolution programs for ANE while retaining CPU normalization, attention and KV operations, then caches compiled variants and batches lanes.

**Scope:** Dense Qwen3/Qwen3.5 text inference through private ANE APIs, with M3 Max-specific empirical constraints.

**Boundary:** Private APIs can change; tested ANE paths do not move every operator off CPU, and measured speculative variants have been slower than baseline.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `mil-compilation`, `heterogeneous-execution`, `kernel-fusion`, `dispatch-batching`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/skyfallsin/ane.cpp/blob/b87bf57356c26025853a60cddfe4b58784ee4fda/README.md) · [Source 2](https://github.com/skyfallsin/ane.cpp/blob/b87bf57356c26025853a60cddfe4b58784ee4fda/core/ane_runtime.cpp) · [Source 3](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/README.md) · [Source 4](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/program.md) · [Source 5](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/results.tsv).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="anemll"></a>

### [ANEMLL](https://github.com/Anemll/Anemll)

[adjacent](systems.md#adjacent) · `construction` · `compiler` · `text` · **public code**

**Survey relevance:** An existing converter-plus-runtime route helps distinguish compiler-mediated specialization from direct native reconstruction.

Splits and converts model components into ANE-oriented stateful packages, with prefill variants, LUT quantization and Swift/Python orchestration.

**Scope:** Selected LLM architectures converted to CoreML for Apple Neural Engine, with size, shape, context and quantization restrictions.

**Boundary:** CoreML chooses actual placement; unsupported operators, OS versions, package sizing and quantization require target-specific verification.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-partitioning`, `coreml-compilation`, `stateful-kv`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/Anemll/Anemll/blob/f4ad26d061dc2e426faa19f81c367343bdeb9f0d/README.md) · [Source 2](https://github.com/Anemll/Anemll/blob/f4ad26d061dc2e426faa19f81c367343bdeb9f0d/docs/ANE_converter.md) · [Source 3](https://github.com/Anemll/Anemll/blob/f4ad26d061dc2e426faa19f81c367343bdeb9f0d/anemll/ane_converter/llama_converter.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="tvm"></a>

### [Apache TVM](https://github.com/apache/tvm)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / general` · **public code**

**Survey relevance:** Compiler infrastructure underlying the included MLC LLM model-to-runtime construction route.

Coordinates Relax graph transformations and tensor-level scheduling to fuse operators, dispatch libraries and lower target-specific tensor programs into deployable modules.

**Scope:** Compilation targets, tensor shapes, legal operators and schedule rules define the specialization boundary.

**Boundary:** TVM is reusable compiler infrastructure for many workloads; a TVM-backed project needs its own model pipeline, runtime policy and evaluation.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `graph-fusion`, `hardware-codegen`, `kernel-autotuning`.

**Constraints:** `hardware`, `shape`, `workload`.

**Evidence:** [Source 1](https://github.com/apache/tvm/blob/HEAD/README.md) · [Source 2](https://github.com/apache/tvm/blob/HEAD/python/tvm/relax/backend/cuda/pipeline.py) · [Source 3](https://github.com/apache/tvm/blob/HEAD/docs/deep_dive/tensor_ir/tutorials/dlight_gpu_scheduling.py) · [Source 4](https://github.com/mlc-ai/mlc-llm/blob/HEAD/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="aria"></a>

### [Aria](https://github.com/matteospanio/aria)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Links an explicit author disclosure of LLM-assisted development to a complete native Stable Audio 3 artifact and controlled reference tests, without assuming lower total construction cost.

Implements T5Gemma conditioning, diffusion transformer, sampler and audio decoder in C with mmap weights, optional quantization and intermediate-state steering.

**Scope:** Stable Audio 3 small/medium local text-to-audio diffusion on CPU and optional CUDA.

**Boundary:** Reference parity tests use controlled conditioning/noise; quantized and steered outputs need separate evaluation. AI assistance is disclosed, but total construction cost is unknown.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `memory-mapping`, `weight-quantization`, `model-specific-kernels`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/README.md) · [Source 2](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/src/aria_model_sa3.c) · [Source 3](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/src/aria_sampler.c) · [Source 4](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/tests/test_e2e.c) · [Source 5](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/BENCHMARKS.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `keyword`.

</details>

<a id="automegakernel"></a>

### [AutoMegaKernel](https://github.com/RightNow-AI/AutoMegaKernel)

[core](systems.md#core) · `construction` · `compiler` · `text` · **public code**

**Survey relevance:** A model-program construction case combining a restricted agent edit surface, deterministic lowering and schedule checks; contrasts with unconstrained whole-runtime generation.

Lowers model graphs through a typed task/counter IR to one cooperative CUDA launch per forward pass. Agent-facing loops tune instruction implementations or structured schedules, with static IR checks and reference evaluation.

**Scope:** Supported HuggingFace Llama-family graphs on CUDA, principally batch-one decode. Paper speed sweeps at position zero use synthetic weights at real model shapes; real-checkpoint quality tests have a separate scope.

**Boundary:** Static graph checks rely on a trusted VM and supported IR, not a mechanized whole-stack proof; inspected data-hazard checks have a task-count cap. Reported W8A16 wins compare against bf16 and cannot establish equal-precision superiority. The host still drives token steps; this is not a complete concurrent serving engine.

**Semantic considerations:** generated-artifact dependent, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-lowering`, `persistent-kernel`, `schedule-search`, `static-dependency-checks`, `instruction-tuning`.

**Constraints:** `model-family`, `hardware`, `single-stream`, `precision`, `schedule-ir`.

**Evidence:** [Source 1](https://arxiv.org/html/2606.09682v1) · [Source 2](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/HARNESS.md) · [Source 3](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/schedule/ir.py).

**Reviewed:** 2026-10-14 · **AI involvement:** `intrinsic` · **Discovery:** `keyword`.

</details>

<a id="basert"></a>

### [BaseRT](https://github.com/basecompute/baseRT)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text / multimodal` · **closed core**

**Survey relevance:** Provides a contrasting delivery model: public format/conversion tooling around a closed specialized engine.

A proprietary native engine executes models packaged by an open converter and exposed through public C APIs and language bindings.

**Scope:** Selected Apple Silicon and NVIDIA GB10 deployments with an engine-specific .base format and device-specific quantization profiles.

**Boundary:** The execution core is not in the public repository; kernel mechanisms and performance rely on author documentation rather than source verification.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `device-specialization`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/basecompute/baseRT/blob/24badc8dd173e4111b64996a718d0e056405ea62/README.md) · [Source 2](https://github.com/basecompute/baseRT/blob/24badc8dd173e4111b64996a718d0e056405ea62/CONTRIBUTING.md) · [Source 3](https://github.com/basecompute/baseRT/blob/24badc8dd173e4111b64996a718d0e056405ea62/base-convert/FORMAT.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="brain"></a>

### [BRaiN](https://github.com/swedishembedded/brain)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text / image / video / audio / multimodal` · **public code**

**Survey relevance:** A broader native training/inference framework provides a contrast to narrowly scoped stacks, including explicit limitations for individual multimodal ports.

Rust model implementations use a shared WGSL compute engine. Inspected Qwen3-VL integrates vision features with language decoding; Wan stages text encoding, denoising and VAE decoding to bound residency.

**Scope:** Multiple native model ports across CPU and GPU/WebGPU; support is architecture- and action-specific.

**Boundary:** Do not interpret the README model list as uniform full-scale validation. The LTX path documents tiny random-weight DiT and stub text conditioning for some generation commands; Qwen3-VL video input requires decoded frames.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `wgsl-kernels`, `staged-residency`, `vision-language-fusion`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/README.md) · [Source 2](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/docs/models/qwen3vl.md) · [Source 3](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/crates/wan/src/pipeline.rs) · [Source 4](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/docs/models/ltxv.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="brodiffusion"></a>

### [brodiffusion](https://github.com/wlejon/brodiffusion)

[core](systems.md#core) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** Owns C++ image-model pipelines and denoiser capture/replay policy over a reused tensor backend, making the boundary between model reconstruction and lower-level reuse explicit.

Implements model loaders, diffusion pipelines and samplers in C++; replays captured denoiser-step graphs when shape and runtime-state contracts permit.

**Scope:** Selected diffusion image families on CPU and brotensor CUDA/Metal/Vulkan paths.

**Boundary:** Model and device support differ; tensor/pipeline parity scripts are not a proof of universal image equivalence, and non-image library modules do not imply complete CLI workflows.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `graph-replay`, `model-specific-graph`.

**Constraints:** `model-family`, `device`, `shape`.

**Evidence:** [Source 1](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/README.md) · [Source 2](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/src/pipeline_step_graph.cpp) · [Source 3](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/src/pipeline_qwenimage21.cpp) · [Source 4](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/scripts/qwenimage21_pipeline_parity.sh) · [Source 5](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/tests/test_device_parity.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="cactus"></a>

### [Cactus](https://github.com/cactus-compute/cactus)

[core](systems.md#core) · `system` · `runtime` · `text / image / audio / multimodal` · **public code**

**Survey relevance:** Connects model graph capture and lowering to a native mobile execution stack with its own quantized state and kernels.

Captures supported model components into an intermediate graph, lowers to Cactus graph operations and runs a native engine with ARM/Metal kernels and quantized state. Vision/audio components and language decoding share bundle-managed execution.

**Scope:** Mobile and wearable deployments; model bundles tested on selected Liquid, Gemma, Qwen and speech families.

**Boundary:** General Hugging Face conversion is experimental; supported bundle paths are narrower than the headline. Quantization and optional cloud handoff must be separated from local runtime gains.

**Semantic considerations:** layout / scheduling, reduced precision, configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `graph-lowering`, `native-runtime`, `component-execution`, `low-bit-state`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/README.md) · [Source 2](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/python/cactus/transpile/capture_pytorch.py) · [Source 3](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/python/cactus/transpile/lower.py) · [Source 4](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/cactus-engine/src/model.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="needle"></a>

### [Cactus Needle](https://github.com/cactus-compute/needle)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text / audio` · **closed core**

**Survey relevance:** A model/runtime co-design and deployment-packaging reference; public model/export code is more inspectable than the distributed native engine.

Needle 3 pairs a sliceable attention architecture and quantized weights with platform-specific native engines. Python tools train/export models and fetch an engine plus weight files for deployment.

**Scope:** Small automation models across desktop, mobile, embedded and browser targets; current source generation is Needle 3.

**Boundary:** The reviewed repository exposes model and packaging code, not the distributed C++ engine implementation. The build command fetching a binary is not evidence of source compilation or agent-generated runtime construction.

**Semantic considerations:** model / router training, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-runtime-codesign`, `model-slicing`, `quantization`, `binary-packaging`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/cactus-compute/needle/blob/3da4261073199444f2e070800854436fbc31fb6a/README.md) · [Source 2](https://github.com/cactus-compute/needle/blob/3da4261073199444f2e070800854436fbc31fb6a/needle/model/run.py) · [Source 3](https://github.com/cactus-compute/needle/blob/3da4261073199444f2e070800854436fbc31fb6a/needle/agent/fetch.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="ciru-runtime"></a>

### [CIRU runtime](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4)

[core](systems.md#core) · `system` · `backend` · `text / multimodal` · **public code**

**Survey relevance:** Model/hardware-specific deep integration with traceable borrowed kernels, artifact compatibility work and release qualification.

A llama.cpp-derived runtime integrates CIRUPLE1 paging, typed expert kernels, QSA sparse-attention paths and MTP state corrections for pinned CIRU model releases.

**Scope:** Qwen3.8 Flash model artifacts, paged embeddings and Strix Halo unified memory require coordinated quantization, sparse attention and speculative-state paths.

**Boundary:** Custom model formats and builds are tightly coupled. Some releases required attention or vision/MTP correctness fixes; published speed observations are not always matched before/after experiments.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/README.md) · [Source 2](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/docs/PROVENANCE.md) · [Source 3](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/ggml/src/ggml-cuda/qsa.cu) · [Source 4](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/docs/QSA_BACKPORT_STATUS.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="infire"></a>

### [Cloudflare Infire](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/)

[core](systems.md#core) · `system` · `runtime` · `text` · **closed core**

**Survey relevance:** An industrial platform-specialization case documenting why a provider rebuilt execution instead of only configuring a general framework; useful without an AI-development attribution.

Rebuilds the Rust HTTP, batching and execution path; overlaps model loading and model-specific kernel compilation, manages paged state and cached execution graphs, and later adds pipeline/tensor/expert parallelism.

**Scope:** Cloudflare distributed inference nodes with constrained host CPU, startup and isolation requirements. The initial Hopper-focused report and later large-model/multi-GPU update describe different deployment stages.

**Boundary:** The engine is proprietary; evidence is official engineering disclosure rather than source inspection or independent reproduction. Initial CPU/performance comparisons mix bare-metal and sandboxed deployment conditions. Later multi-GPU support must not be treated as present in the initial release.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-rust-runtime`, `model-specific-jit`, `continuous-batching`, `chunked-prefill`, `paged-kv`, `multi-gpu-execution`.

**Constraints:** `hardware`, `deployment`, `cpu-budget`, `security`, `startup-latency`.

**Evidence:** [Source 1](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/) · [Source 2](https://blog.cloudflare.com/high-performance-llms/).

**Reviewed:** 2026-10-14 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="coreml-llm-cli"></a>

### [CoreML LLM CLI](https://github.com/smpanaro/coreml-llm-cli)

[adjacent](systems.md#adjacent) · `system` · `research-prototype` · `text` · **public code**

**Survey relevance:** A cited predecessor of ANEMLL makes earlier compiled-model and host-runtime specialization visible.

Orchestrates chunked CoreML model execution and KV state, with reshaped convolution layouts and copy-avoiding model buffers.

**Scope:** CoreML-converted Llama 2 on ANE with fixed chunking and IOSurface-backed buffers.

**Boundary:** Demonstration-focused scope with a small model/device matrix; the compiled model and runtime must be evaluated together.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-chunking`, `buffer-sharing`, `coreml-execution`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/README.md) · [Source 2](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/Sources/Kit/ModelPipeline.swift) · [Source 3](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/Sources/Kit/KVCacheProcessor.swift) · [Source 4](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/Sources/Kit/MultiArrayStore.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="diffusion-rs"></a>

### [diffusion-rs](https://github.com/EricLBuehler/diffusion-rs)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** A neighboring Rust model-port route provides a component-reuse and offload comparison; it is not evidence of agent-generated construction.

Implements FLUX component loading, sampling and residency policy on a reusable Rust tensor layer, including quantized model support.

**Scope:** FLUX image generation through Rust tensor operations and optional component offload.

**Boundary:** Supported models and validation breadth are limited by the implementation; source inspection does not establish an advantage over optimized existing engines.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `component-offload`, `weight-quantization`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/README.md) · [Source 2](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/Cargo.toml) · [Source 3](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/diffusion_rs_core/src/pipelines/flux/mod.rs) · [Source 4](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/diffusion_rs_core/src/pipelines/flux/sampling.rs).

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

[core](systems.md#core) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Core by execution ownership: native DiT graphs and model-component residency, graph segmentation and staged offload reconstruct the integrated constrained-memory path.

Runs DiTs on ggml graphs with automatic quantization and placement, per-component or double-buffered block offload, VAE tiling and model-aware cache policies.

**Scope:** Prioritizes constrained GPU memory and explicit component placement, with CUDA as the primary optimized backend.

**Boundary:** Backend maturity and cache support differ by model; memory-budget comparisons require the same precision and offload policy.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `weight-quantization`, `block-offload`, `vae-tiling`, `activation-reuse`, `hybrid-parallelism`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/README.md) · [Source 2](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/docs/optimization/memory-efficient-execution.md) · [Source 3](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/src/core/backend/ggml/cuda/ed_async_offload.cu) · [Source 4](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/benchmark/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="fastflowlm"></a>

### [FastFlowLM](https://github.com/ROCm/FastFlowLM)

[core](systems.md#core) · `system` · `runtime` · `text / audio / image / multimodal` · **closed core**

**Survey relevance:** Shows device-specific NPU execution built from model-family host runtimes and compiled kernel providers, with a visible source/binary boundary.

Selects a model-family backend, packs or loads compatible weights, owns NPU tensors and decoding streams, and dispatches shape-qualified kernels. The rai path exposes model integration over ryzenai-corelib; original flm engines ship as prebuilt libraries.

**Scope:** AMD XDNA2 client NPUs, including supported Ryzen AI platforms; selected language, vision and audio models.

**Boundary:** Public host code does not make every NPU engine open source. Original flm engines are prebuilt; rai source coverage and platform validation vary. Do not transfer one model/hardware result to all listed modes.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `npu-dataflow`, `model-backend-dispatch`, `weight-packing`, `native-runtime`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/README.md) · [Source 2](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/src/common/models/README.md) · [Source 3](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/src/common/AutoModel/model_backend.cpp) · [Source 4](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/flm_story.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="fastvideo"></a>

### [FastVideo](https://github.com/hao-ai-lab/FastVideo)

[core](systems.md#core) · `system` · `runtime` · `video / audio` · **public code**

**Survey relevance:** Core by integrated model execution: its own model implementations, registries, component loaders and denoising stages reconstruct inference, beyond the separately cataloged sparse/distillation methods.

Owns model and pipeline registries, component loading and staged denoising over shared tensor backends. Dense model paths coexist with optional Video Sparse Attention, sequence parallelism, offload and sparse or timestep-distilled checkpoints.

**Scope:** Supported video and audio-video architectures on qualified backends; ordinary dense and accelerated model paths have distinct checkpoint and precision requirements.

**Boundary:** VSA and timestep distillation can change the model; current MLX VSA documentation explicitly distinguishes a reference path from an experimental Metal path with output differences.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-specific-execution`, `staged-denoising`, `sequence-parallelism`, `block-offload`, `block-sparse-attention`, `distillation`.

**Constraints:** `long-sequence`, `device`, `model-family`.

**Evidence:** [Source 1](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/README.md) · [Source 2](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/docs/inference/architecture.md) · [Source 3](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/fastvideo/pipelines/stages/denoising.py) · [Source 4](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/docs/contributing/performance_benchmarks.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="flash-linear-attention"></a>

### [Flash Linear Attention](https://github.com/fla-org/flash-linear-attention)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Reusable recurrent and linear-attention kernels in the ExLlamaV3 execution stack; state semantics must survive integration.

Implements architecture-specific linear-attention and recurrent mixers with chunk-parallel prefill and state-update kernels, including fused gated-delta-rule intra-chunk computation.

**Scope:** The mixer equations, recurrent-state structure, sequence chunking and backend capabilities define legal execution decompositions.

**Boundary:** Replacing softmax attention with a linear mixer changes the model; these kernels accelerate compatible architectures rather than providing a semantics-preserving replacement for arbitrary attention.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `chunked-recurrence`, `recurrent-state-kernels`, `kernel-fusion`.

**Constraints:** `architecture`, `hardware`, `shape`, `state`.

**Evidence:** [Source 1](https://github.com/fla-org/flash-linear-attention/blob/HEAD/README.md) · [Source 2](https://github.com/fla-org/flash-linear-attention/blob/HEAD/fla/ops/gated_delta_rule/chunk.py) · [Source 3](https://github.com/turboderp-org/exllamav3/blob/HEAD/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="flash-attention"></a>

### [FlashAttention](https://github.com/Dao-AILab/flash-attention)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Attention implementation reused by included model runtimes such as ExLlamaV3; an optimized component does not establish an end-to-end gain.

Implements attention with IO-aware tiled kernels and fused reductions, selecting hardware/shape-specific variants and providing KV-cache update-and-attend inference interfaces.

**Scope:** Attention head dimensions, dtype, mask/dropout mode and GPU generation constrain the fused kernel configuration and supported release path.

**Boundary:** Exact attention describes the mathematical operation, not guaranteed bitwise equality with every implementation; FA2, Hopper FA3 and CuTeDSL FA4 have different hardware and feature contracts.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `io-aware-tiling`, `online-softmax`, `kernel-fusion`.

**Constraints:** `hardware`, `shape`, `precision`, `memory`.

**Evidence:** [Source 1](https://github.com/Dao-AILab/flash-attention/blob/HEAD/README.md) · [Source 2](https://github.com/Dao-AILab/flash-attention/blob/HEAD/flash_attn/flash_attn_interface.py) · [Source 3](https://github.com/turboderp-org/exllamav3/blob/HEAD/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="flashinfer"></a>

### [FlashInfer](https://github.com/flashinfer-ai/flashinfer)

[foundation](systems.md#foundation) · `support` · `kernel-library` · `text` · **public code**

**Survey relevance:** Optional standard paged-attention backend used by MoE-Infinity where supported; preserves the distinction between reusable kernels and the reconstructed engine.

Builds or selects attention/GEMM/MoE kernels from dtype, head geometry, cache layout and workload metadata, with planned paged/ragged KV execution and specialized prefill/decode paths.

**Scope:** GPU architecture, head dimensions, precision, positional encoding, batch shape and KV layout determine eligible backends and generated kernel modules.

**Boundary:** It is a multi-backend kernel library and generator rather than a standalone inference server, and support varies by feature and compute capability.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `jit-specialization`, `backend-selection`, `paged-kv-kernels`, `workload-planning`.

**Constraints:** `hardware`, `shape`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/flashinfer-ai/flashinfer/blob/HEAD/README.md) · [Source 2](https://github.com/flashinfer-ai/flashinfer/blob/HEAD/flashinfer/decode.py) · [Source 3](https://github.com/EfficientMoE/MoE-Infinity/blob/HEAD/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

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

<a id="hearth"></a>

### [Hearth](https://github.com/jeff-hiner/hearth)

[core](systems.md#core) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** Reconstructs SD-family model graphs, samplers and dependency-ordered execution in Rust over CubeCL/wgpu, illustrating native pipeline ownership without rebuilding the entire GPU layer.

Rebuilds CLIP, UNet, VAE, sampler and node execution in Rust, reusing CubeCL/wgpu for tensor kernels and device access.

**Scope:** SD1.5/SDXL on GPUs reachable through CubeCL/wgpu Vulkan execution.

**Boundary:** Compatibility interfaces and img2img are early; a VRAM-budget scaffold should not be interpreted as a fully implemented memory planner or proven performance advantage.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-graph`, `graph-execution`.

**Constraints:** `model-family`, `device`.

**Evidence:** [Source 1](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/README.md) · [Source 2](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/src/unet/model.rs) · [Source 3](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/src/node/executor.rs) · [Source 4](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/Cargo.toml) · [Source 5](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/tests/tensor_ops.rs).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="hilum-engine"></a>

### [Hilum LLM Engine](https://github.com/hilum-labs/hilum-local-llm-engine)

[adjacent](systems.md#adjacent) · `system` · `backend` · `text / multimodal` · **public code**

**Survey relevance:** A mobile-focused llama.cpp fork illustrates continued subsystem porting and device adaptation while retaining the general engine.

Retains llama.cpp/GGML execution and adds mobile backend integration, Adreno shader build/dispatch paths, allocation support and per-device parameter tuning.

**Scope:** Android Adreno/Vulkan and Apple Metal mobile deployments with GGUF models.

**Boundary:** The inspected mobile integration does not establish a separate model-specific runtime or that every shader originated in this fork. Performance is an internal report; full upstream delta and device correctness were not independently audited.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `mobile-backend-adaptation`, `device-dispatch`, `parameter-tuning`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/hilum-labs/hilum-local-llm-engine/blob/dacf8c60173c05331970b16fcbaf15efbc755f73/README.md) · [Source 2](https://github.com/hilum-labs/hilum-local-llm-engine/blob/dacf8c60173c05331970b16fcbaf15efbc755f73/ggml/src/ggml-vulkan/CMakeLists.txt).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="hipengine"></a>

### [hipEngine](https://github.com/shisa-ai/hipEngine)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal / audio` · **public code**

**Survey relevance:** Native AMD reconstruction with explicit model/device qualification; Gufo cites this runtime as a design reference.

A Python host drives HIP/C++ model runners, hardware-specific kernels, shared KV/prefix state and continuous batching without PyTorch in the inference runtime.

**Scope:** RDNA3 gfx1100 and Strix Halo gfx1151 need native model kernels, recurrent-state handling and request scheduling qualified for their memory and execution geometry.

**Boundary:** Alpha; single-GPU only. Low-bit KV, DMS and speculative modes have different quality and qualification scopes; CPU execution is an oracle, not a supported generation backend.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/README.md) · [Source 2](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/hipengine/runtime/qwen35_gguf_runner.py) · [Source 3](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/hipengine/generation/batch_scheduler.py) · [Source 4](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/docs/RDNA3-TUNING-GUIDE.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="imp"></a>

### [imp](https://github.com/kekzl/imp)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Explicit single-architecture reconstruction plus a direct author disclosure of end-to-end coding-agent implementation.

A C++/CUDA engine owns model loading, attention/MoE/recurrent execution, paged KV, CUDA Graph scheduling and OpenAI/Anthropic-compatible serving, with chip-specific kernels.

**Scope:** A single RTX 5090-class sm_120a target and local agent workloads motivate native FP4 arithmetic, memory planning and low-overhead concurrent serving.

**Boundary:** Author-reported results are model/quantization/workload specific; comparisons using different weight formats do not isolate runtime gains. Other GPU families are outside the main target.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/README.md) · [Source 2](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/CONTRIBUTING.md) · [Source 3](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/src/runtime/engine.cpp) · [Source 4](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/src/runtime/engine_scheduler.cpp) · [Source 5](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/docs/MISSION_JOURNAL.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `disclosed` · **Discovery:** `keyword`.

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

<a id="kipp"></a>

### [Kipp](https://github.com/Polished-Snow/Kipp)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Model-family reconstruction with explicit checkpoint rejection and native serving, beyond a teaching-only forward-pass example.

A C11 engine implements strict loading, tokenization, model execution, paged KV/prefix sharing, batching and serving behind isolated Metal and CUDA backends.

**Scope:** A pinned Qwen3 checkpoint registry and small native runtime motivate explicit model contracts and hardware-checked CPU/Metal/CUDA paths.

**Boundary:** Only registered checkpoints and GGUF subsets are admitted. Quantized variants are not bit-identical; backend gates and performance results are hardware specific.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/README.md) · [Source 2](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/docs/ARCHITECTURE.md) · [Source 3](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/docs/ROADMAP.md) · [Source 4](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/src/kipp.c) · [Source 5](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/src/cuda/kipp_cuda.cu).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="kie"></a>

### [Kog Inference Engine (KIE)](https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/)

[core](systems.md#core) · `system` · `runtime` · `text` · **documentation only**

**Survey relevance:** An industrial model/runtime/hardware co-design case with an explicitly narrow low-latency operating point; distinguishes a purpose-built execution architecture from a generic serving configuration.

Co-designs a persistent device-side generation loop with weight streaming, sampling, topology-aware handoffs and Laneformer delayed tensor-parallel communication, according to the vendor engineering report.

**Scope:** The reviewed low-latency preview uses an FP16 approximately 2B Laneformer model, batch one and eight AMD MI300X GPUs; the companion announcement also reports an eight-H200 configuration.

**Boundary:** The review covers vendor documents, not public engine source or reproduced results. The headline preview combines Laneformer/DTP with an eight-GPU FP16 setup; it is not evidence of the same gain on an unchanged arbitrary model, and third-party model roadmap statements are not implemented support.

**Semantic considerations:** layout / scheduling, model / router training.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `persistent-monokernel`, `weight-streaming`, `device-side-sampling`, `topology-aware-synchronization`, `delayed-tensor-parallelism`.

**Constraints:** `model`, `hardware`, `single-request`, `multi-gpu`, `latency`.

**Evidence:** [Source 1](https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/) · [Source 2](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/).

**Reviewed:** 2026-10-14 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="lightx2v"></a>

### [LightX2V](https://github.com/ModelTC/LightX2V)

[core](systems.md#core) · `system` · `runtime` · `image / video / audio` · **public code**

**Survey relevance:** Core by substantive backend reconstruction: model inference, operator storage contracts and two-slot weight transfer expose owned execution and memory decisions within a shared framework.

Combines model-specific inference paths with quantized operators, cache policies, parallel execution and a two-slot block-loading system for overlapping offload.

**Scope:** Targets large supported image and video models on memory-constrained accelerators and multi-device systems.

**Boundary:** Reported maximum speedups can combine runtime changes, quantization, step-distilled weights and lightweight VAEs, which need separate attribution.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `block-offload`, `weight-quantization`, `activation-reuse`, `hybrid-parallelism`.

**Constraints:** `device`, `memory-capacity`, `model-family`.

**Evidence:** [Source 1](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/README.md) · [Source 2](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/lightx2v/common/offload/manager.py) · [Source 3](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/lightx2v/common/offload/block_loader.py) · [Source 4](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/docs/EN/source/getting_started/benchmark.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="lily"></a>

### [Lily](https://github.com/perplexityai/pplx-garden/tree/main/lily)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A deliberately single-checkpoint execution stack makes the compatibility cost of reconstruction explicit.

A Rust runtime owns the prefill/decode graph, dispatches model-specific Metal kernels and maintains a strict token-prefix session cache.

**Scope:** One exact Qwen3.6-35B-A3B MLX-affine Q4 checkpoint, group size 64, on Apple GPU family 10+ and macOS 26+.

**Boundary:** Greedy, text-only, non-streaming API; unsupported checkpoints and sampling options are rejected. Published comparisons do not establish independent reproduction.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `device-specialization`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/README.md) · [Source 2](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/src/config.rs) · [Source 3](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/src/model.rs) · [Source 4](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/CONTRIBUTING.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="lithos-metal"></a>

### [Lithos Metal](https://github.com/lithos-ai/lithos-metal)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Connects a graph compiler and chip-specific recipes to a concrete standalone inference runtime.

Compiles typed model graphs into layer-mixer megakernels plus conventional kernels, replayed with Metal indirect command buffers and GPU-resident speculative state.

**Scope:** Registered Apple chip backends and selected Qwen target/draft checkpoints, with explicit recipe, format and context constraints.

**Boundary:** Some chip backends are unmeasured, hybrid MoE integration is experimental, and default normalization fusion changes BF16 rounding; target-compute projections exclude draft and verification overhead.

**Semantic considerations:** configuration-dependent, target-verified proposals.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `graph-compilation`, `megakernel`, `gpu-resident-control`, `verified-speculation`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/README.md) · [Source 2](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/docs/design/design.md) · [Source 3](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/docs/design/extensions.md) · [Source 4](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/monolith/runtime/engine.py) · [Source 5](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/CONTRIBUTING.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="llama-cpp"></a>

### [llama.cpp](https://github.com/ggml-org/llama.cpp)

[foundation](systems.md#foundation) · `support` · `runtime` · `text` · **public code**

**Survey relevance:** Upstream execution stack for the llamAmpere, CIRU, Strix and ANEMLL Flash forks; makes inherited code and changed execution paths comparable.

Loads GGUF model tensors and executes a native GGML graph through backend-specific quantized kernels, dispatching by tensor type and geometry with optional CPU/GPU layer placement.

**Scope:** Checkpoint quantization type, tensor layout, matrix geometry, CPU instruction sets and accelerator memory determine eligible kernels and placement.

**Boundary:** Backend and quantization support are not uniform across every operation or device; native low-bit execution does not imply identical accuracy or speed for all GGUF formats.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `quantized-layout`, `native-kernel-dispatch`, `cpu-gpu-placement`.

**Constraints:** `precision`, `hardware`, `layout`, `shape`, `memory`.

**Evidence:** [Source 1](https://github.com/ggml-org/llama.cpp/blob/HEAD/README.md) · [Source 2](https://github.com/ggml-org/llama.cpp/blob/HEAD/ggml/src/ggml-cpu/ggml-cpu.c) · [Source 3](https://github.com/ggml-org/llama.cpp/blob/HEAD/ggml/src/ggml-cuda/mmvq.cu) · [Source 4](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN_AMPERE.md).

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

<a id="memra"></a>

### [memra](https://github.com/avifenesh/memra)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Native runtime with per-model/device exactness gates and explicit evidence of the maintenance and qualification burden.

A Rust host drives embedded ahead-of-time CUDA kernels and model-specific programs, with quantized execution, KV/prefix management, speculation and multi-device placement.

**Scope:** Per-card Blackwell execution, limited device memory and low-concurrency or large-model workloads motivate native model programs and explicit state placement.

**Boundary:** General engine development and routine model bring-ups are paused at the reviewed revision. Source is FSL-1.1-ALv2, not an unconditional Apache release; hardware paths have separate qualifications.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/README.md) · [Source 2](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/ARCHITECTURE.md) · [Source 3](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/crates/memra-engine/src/forward.rs) · [Source 4](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/crates/memra-engine/THIRD-PARTY.md) · [Source 5](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/docs/TESTING.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="metalchat"></a>

### [MetalChat](https://github.com/ybubnov/metalchat)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** An adjacent native framework illustrates reusable model abstractions rather than a narrowly documented reconstruction experiment.

Builds native tensor, layer and model abstractions with Metal kernels and a command-line generation path.

**Scope:** Selected Llama/Gemma-family models on Apple Silicon through a native C++/Metal library.

**Boundary:** The API is explicitly unstable and the inspected integration test demonstrates generation without a comprehensive quality gate.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `device-specialization`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/README.md) · [Source 2](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/src/gemma.cc) · [Source 3](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/test/test_gemma.cc) · [Source 4](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/documentation/guides/getting_started.rst).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

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

<a id="minimax-h3-mlx"></a>

### [MiniMax-H3 MLX](https://github.com/PipeNetwork/minimax-h3-mlx)

[core](systems.md#core) · `system` · `runtime` · `video / audio` · **public code**

**Survey relevance:** Reconstructs a complete joint video/audio diffusion model on MLX, including packed modality geometry and invariant AdaLN precomputation; distinguishes making a model fit from making it fast.

Reimplements the joint pipeline in MLX, precomputes timestep-only AdaLN values and stages conditioning/DiT/VAE components while preserving packed multimodal geometry.

**Scope:** MiniMax-H3 joint video/audio diffusion on Apple Silicon with large unified memory.

**Boundary:** Dense attention remains compute-heavy; quantization mainly changes fit, and only the text-conditioned generation path is reported end-to-end, not every implemented keyframe path.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `invariant-precompute`, `component-offload`, `weight-quantization`.

**Constraints:** `model`, `device`, `memory-capacity`, `long-sequence`.

**Evidence:** [Source 1](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/README.md) · [Source 2](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/minimax_h3_mlx/pipeline.py) · [Source 3](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/minimax_h3_mlx/adaln.py) · [Source 4](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/tests/test_dit_parity.py) · [Source 5](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/tests/test_text_encoder_parity.py) · [Source 6](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/reference/README.md).

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

<a id="ninfer-3090"></a>

### [NInfer-3090](https://github.com/ashalliants/ninfer-3090)

[core](systems.md#core) · `system` · `runtime` · `text / multimodal` · **public code**

**Survey relevance:** Concrete retargeting case: kernel and memory-program changes beyond changing a CUDA architecture flag; one representative records the 3090 fork family.

A continuation of the NInfer/Don-Chad fork supplies SM86 quantized tensor-core paths, memory and replay-state planning, low-bit KV and model-specific speculative execution.

**Scope:** Qwen dense/MoE serving on a 24 GB RTX 3090 requires SM86-compatible kernels and a smaller memory budget than upstream consumer Blackwell.

**Boundary:** Inherited model/container contracts constrain compatibility. SM86 does not provide Blackwell-native FP4/FP8 arithmetic; context, KV accuracy and concurrency tradeoffs are profile dependent.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/README.md) · [Source 2](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/src/ops/linear/ggml/ggml_mmq.cuh) · [Source 3](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/src/models/qwen3_5/program/transactions/replay.cpp) · [Source 4](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/RELEASE_NOTES_0.11.0.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="tensorrt"></a>

### [NVIDIA TensorRT](https://github.com/NVIDIA/TensorRT)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / general` · **closed core**

**Survey relevance:** Model-compilation and execution foundation for the included TensorRT Edge-LLM deployment route.

Builds NVIDIA inference engines specialized to optimization-profile shapes and selected kernel tactics, recording profiled decisions in a reusable editable timing cache.

**Scope:** NVIDIA devices, supported operators, precision contracts and min/opt/max input-shape profiles define an engine build.

**Boundary:** The public repository contains plugins, parsers and samples, not the complete TensorRT optimizer/runtime core; internals beyond these interfaces were not inspected.

**Semantic considerations:** layout / scheduling.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `aot-specialization`, `tactic-selection`, `graph-fusion`, `shape-profiles`.

**Constraints:** `hardware`, `shape`, `precision`.

**Evidence:** [Source 1](https://github.com/NVIDIA/TensorRT/blob/HEAD/README.md) · [Source 2](https://github.com/NVIDIA/TensorRT/blob/HEAD/samples/sampleDynamicReshape/sampleDynamicReshape.cpp) · [Source 3](https://github.com/NVIDIA/TensorRT/blob/HEAD/samples/sampleEditableTimingCache/README.md) · [Source 4](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/README.md).

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

<a id="parakeet-axiom"></a>

### [parakeet.cpp (axiom)](https://github.com/Frikallo/parakeet.cpp)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** An independent Parakeet reconstruction uses axiom/MPSGraph instead of ggml; it exposes how model and streaming ownership can be retained while reusing a different tensor backend.

Implements FastConformer and decoder paths plus cached streaming convolution/attention in native C++ on axiom.

**Scope:** Parakeet ASR on CPU and Apple Metal/MPSGraph through the axiom tensor library.

**Boundary:** This is a distinct implementation from mudler/parakeet.cpp; highlighted synthetic encoder-forward benchmarks must not be read as end-to-end transcription results.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `chunked-streaming`, `backend-dispatch`.

**Constraints:** `model-family`, `device`, `latency`.

**Evidence:** [Source 1](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/README.md) · [Source 2](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/src/models/encoder.cpp) · [Source 3](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/src/models/streaming_encoder.cpp) · [Source 4](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/tests/test_all.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="parakeet-ggml"></a>

### [parakeet.cpp (ggml)](https://github.com/mudler/parakeet.cpp)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Ports NeMo speech graphs and cache-aware transcription semantics into C++/ggml, exposing the conversion, streaming-state and parity work needed to build a portable native ASR stack.

Ports speech feature extraction, encoder/decoder graphs and streaming sessions to C++/ggml with GGUF conversion and reference parity fixtures.

**Scope:** NeMo FastConformer CTC/RNNT/TDT families, including cache-aware streaming, on ggml backends.

**Boundary:** The parity report uses selected fixtures and backend settings; several model-dependent tests skip without external model files, so passing ordinary CI is not broad ASR equivalence.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `weight-quantization`, `chunked-streaming`, `backend-dispatch`.

**Constraints:** `model-family`, `device`, `latency`.

**Evidence:** [Source 1](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/README.md) · [Source 2](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/src/model.cpp) · [Source 3](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/docs/parity.md) · [Source 4](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/docs/batching.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="pmetal"></a>

### [PMetal](https://github.com/Epistates/pmetal)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `general` · **public code**

**Survey relevance:** A training-and-inference platform is an adjacent route for studying when specialized paths live inside a reusable ecosystem.

Combines model architecture implementations with native inference bridges and custom device operations within a broader ML SDK.

**Scope:** Apple Silicon training and inference across MLX, native Metal and ANE-oriented components.

**Boundary:** The inspection covers a Qwen native forward path and cached-decode tests, not every advertised model or ANE capability.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `device-specialization`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/README.md) · [Source 2](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/CONTRIBUTING.md) · [Source 3](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/crates/pmetal-bridge/src/qwen3_native/forward.rs) · [Source 4](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/crates/pmetal-models/tests/cached_decode.rs).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="qingming-qwen3-tts"></a>

### [Qingming Qwen3-TTS](https://github.com/uulong950/qingming-qwen3-tts)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Tests the narrowest device-specialization boundary: separate native synthesis paths for two fixed 24GB GPUs, including their memory capacities and generation/decoder concurrency contracts.

Builds separate HIP/CUDA device paths with fixed hardware contracts, native operators and resident streaming generation/decoder resource partitioning.

**Scope:** Qwen3-TTS on AMD RX 7900 XTX 24GB and NVIDIA RTX 4090 24GB.

**Boundary:** Device-specific Once/Resident agreement is not cross-reference perceptual equivalence; fixed capacities and GPU assumptions limit portability.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-kernels`, `resource-partitioning`, `streaming-decoder`.

**Constraints:** `model-family`, `device`, `memory-capacity`, `latency`.

**Evidence:** [Source 1](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/README.md) · [Source 2](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/CONTRACT.md) · [Source 3](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/devices/rtx4090-24g/qwen3_tts_0_6b.cu) · [Source 4](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/devices/rtx4090-24g/benchmark.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="saient-quartz"></a>

### [Quartz](https://github.com/SaientAI/saient-quartz)

[core](systems.md#core) · `system` · `runtime` · `text / image / video` · **public code**

**Survey relevance:** Exposes native Rust image generation and an evolving native Wan path, while a separate C++ video companion provides a concrete case for auditing claimed versus actual execution boundaries.

Implements its own tensor backend and image model stages, with reference-driven native Wan orchestration under development.

**Scope:** Native Rust local inference with SD1.5/SDXL and an evolving Wan path on CPU/CUDA/Vulkan.

**Boundary:** The demonstrated mobile Wan path uses a separate stable-diffusion.cpp-based companion; do not attribute that result to the native Rust Wan implementation. Native support and speed remain path-specific.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-graph`, `backend-dispatch`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/README.md) · [Source 2](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/src/sdxl_pipeline.rs) · [Source 3](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/src/wan_pipeline.rs) · [Source 4](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/reference/README.md) · [Source 5](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/Cargo.toml).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="qwen-asr-c"></a>

### [Qwen-ASR (C)](https://github.com/antirez/qwen-asr)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Reconstructs Qwen3-ASR from waveform preprocessing through autoregressive transcription in C, making streaming context policy and CPU/GPU execution responsibilities directly inspectable.

Owns audio preprocessing, encoder, prompt/decode state and chunked streaming in C; CPU mmap weights and optional GPU-specific loading avoid a Python model runtime.

**Scope:** Qwen3-ASR 0.6B/1.7B on local CPU and optional CUDA/ROCm devices.

**Boundary:** Streaming context/rollback, quantization and backend choices require separate transcript and numerical checks; regression scripts were inspected but not run.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `memory-mapping`, `chunked-streaming`, `backend-dispatch`.

**Constraints:** `model-family`, `device`, `latency`.

**Evidence:** [Source 1](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/README.md) · [Source 2](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/qwen_asr.c) · [Source 3](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/qwen_asr_encoder.c) · [Source 4](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/asr_regression.py) · [Source 5](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/MODEL.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="qwen3-tts-c"></a>

### [Qwen3-TTS (C)](https://github.com/gabriele-mastrapasqua/qwen3-tts)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Rebuilds the Qwen3-TTS talker, code predictor and waveform decoder as one native path; published engineering records connect implementation choices to reference checks and measurement corrections.

Implements talker, code predictor and speech decoder in C, with model-specific dispatch, streaming and reference-driven qualification.

**Scope:** Qwen3-TTS 0.6B/1.7B speech synthesis on CPU and supported CUDA/Metal paths.

**Boundary:** Engineering task instructions are not proof of AI authorship; per-stage timings and qualified backend cases do not establish universal TTS quality or total development cost.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-kernels`, `streaming-decoder`, `backend-dispatch`.

**Constraints:** `model-family`, `device`, `latency`.

**Evidence:** [Source 1](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/README.md) · [Source 2](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/qwen_tts_talker.c) · [Source 3](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/docs/pipeline.md) · [Source 4](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/docs/ENGINEERING-METHOD.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="saragossa"></a>

### [Saragossa](https://github.com/azerozero/saragossa)

[core](systems.md#core) · `system` · `runtime` · `text / audio` · **public code**

**Survey relevance:** Replaces array-framework execution with an explicitly owned local runtime and regression oracles.

Implements Rust/Metal model paths with resident decode state, leased scratch buffers, kernel dispatch and block-prefix snapshots.

**Scope:** Single-user local latency on Apple Silicon for selected text and speech architectures with MLX affine integer weights.

**Boundary:** Model and precision coverage is explicit; the single-user serving design and configuration-dependent KV precision do not imply general multi-tenant performance.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `device-specialization`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/README.md) · [Source 2](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/decode_resident.rs) · [Source 3](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/decode_resident/attention.rs) · [Source 4](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/runtime_flags.rs) · [Source 5](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/tests/golden/README.md).

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

[core](systems.md#core) · `system` · `runtime` · `image / video` · **public code**

**Survey relevance:** Core by construction boundary: the native image/video model implementation owns loading, conditioning, sampling and component placement over reusable ggml backends.

Implements image and video diffusion in ggml-backed C/C++ with quantized weights, tiled VAE execution and architecture-gated sample-cache policies.

**Scope:** Targets multiple local CPU and GPU backends and models that fit supported GGUF and execution paths.

**Boundary:** Cache modes and backend features are model-dependent; enabling a cache can alter outputs and is distinct from the native runtime rewrite.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `weight-quantization`, `vae-tiling`, `activation-reuse`.

**Constraints:** `device`, `model-family`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/README.md) · [Source 2](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/src/pipeline/diffusion_engine.cpp) · [Source 3](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/src/pipeline/video.cpp) · [Source 4](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/docs/caching.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `initial`.

</details>

<a id="stable-diffusion-rs"></a>

### [stable-diffusion.rs](https://github.com/andreinknv/stable-diffusion.rs)

[core](systems.md#core) · `system` · `runtime` · `image` · **public code**

**Survey relevance:** Documents a native Rust diffusion implementation and its Candle-to-MLX migration, exposing which model/backend boundaries can survive a device-stack change and which require new parity checks.

Implements model and sampler logic in Rust and documents a Candle-to-MLX backend migration, preserving a narrow tensor-layer interface and golden-reference workflow.

**Scope:** Selected diffusion models on Apple MLX, with an explicit Rust model/backend boundary.

**Boundary:** Agent task specifications do not establish AI authorship; backend design notes may describe previous states, so current model-source paths determine implemented support.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `backend-migration`, `model-specific-graph`.

**Constraints:** `model-family`, `device`.

**Evidence:** [Source 1](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/README.md) · [Source 2](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/backends.md) · [Source 3](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/seam.md) · [Source 4](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/agent-tasks/README.md) · [Source 5](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/xtask/golden/README.md) · [Source 6](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/crates/sd-models/src/mlx/flux.rs).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="strix-llama-cpp"></a>

### [strix-llama.cpp](https://github.com/halo-box/strix-llama.cpp)

[core](systems.md#core) · `system` · `backend` · `text / multimodal` · **public code**

**Survey relevance:** Hardware-specialized fork with substantial kernel/state changes and a documented upstream/staging boundary; represents the overlapping Strix llama.cpp fork family.

A community llama.cpp fork adds guarded gfx1151 matmul, MoE and Gated DeltaNet fusions, on-device speculative checkpoints, adaptive drafting and selected ROCmFPX formats.

**Scope:** Strix Halo gfx1151 shares limited bandwidth between CPU and GPU and exhibits device/driver-specific Vulkan and HIP behavior.

**Boundary:** Optional speculative prefill omits target work and is approximate. Low-bit formats and driver-dependent dispatch require separate checks; welcoming agent PRs does not establish AI authorship.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/README.md) · [Source 2](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/ggml/src/ggml-cuda/gated_delta_net.cu) · [Source 3](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/ggml/src/ggml-vulkan/ggml-vulkan.cpp) · [Source 4](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/CONTRIBUTING.md).

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

<a id="tensorrt-edge-llm"></a>

### [TensorRT Edge-LLM](https://github.com/NVIDIA/TensorRT-Edge-LLM)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text / image / audio / multimodal` · **public code**

**Survey relevance:** A compiler-based edge deployment reference linking exported model graphs, hardware-specific engine plans and a native multimodal runtime.

Exports models to ONNX, builds target-specific TensorRT engines, then runs them through C++ executors managing decoder strategies, linear KV state, sampling and vision/audio embeddings.

**Scope:** Supported Jetson, DRIVE and other qualified NVIDIA platforms; model and precision support follow the release matrix.

**Boundary:** Reuses TensorRT compilation and CUDA plugins; engine plans and exports must be rebuilt across incompatible runtime versions. A platform SDK is a construction baseline, not direct evidence of lower AI-assisted development cost.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `engine-compilation`, `native-runtime`, `multimodal-execution`, `kv-state-management`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/README.md) · [Source 2](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/docs/source/developer_guide/software-design/engine-builder.md) · [Source 3](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/docs/source/developer_guide/software-design/llm-inference-runtime.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="uzu"></a>

### [Uzu](https://github.com/trymirai/uzu)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** A broader on-device engine and model-conversion ecosystem provides a reference for reusable native construction.

Rust encodable model blocks manage decoder state and dispatch native kernels; generated bindings encode Metal function-constant specializations.

**Scope:** On-device Apple deployment using its supported configurations, converted model format and native Metal backend.

**Boundary:** Its broad SDK scope differs from a single deployment-specific case; source inspection does not establish performance or AI authorship.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-model-path`, `device-specialization`.

**Constraints:** `model`, `hardware`, `memory`, `precision`.

**Evidence:** [Source 1](https://github.com/trymirai/uzu/blob/bd374af567221e281538de47987ce35429f91376/README.md) · [Source 2](https://github.com/trymirai/uzu/blob/bd374af567221e281538de47987ce35429f91376/crates/uzu-engine/src/encodable_block/decoder.rs) · [Source 3](https://github.com/trymirai/uzu/blob/bd374af567221e281538de47987ce35429f91376/crates/uzu-engine/build/metal/bindgen/specialize.rs) · [Source 4](https://github.com/trymirai/lalamo/blob/831accb8252a6b6606c378048caeb44178f1a050/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="vidax"></a>

### [Vidax](https://github.com/FlyingGiraffe/vidax)

[core](systems.md#core) · `system` · `runtime` · `video` · **public code**

**Survey relevance:** Ports video model graphs and checkpoint layouts onto TPU meshes with explicit JAX sharding and numerical-debugging records, making hardware migration a concrete construction case.

Ports model graphs and checkpoint layouts to JAX, explicitly composes tensor/sequence sharding, attention kernels, component placement and native video samplers.

**Scope:** Selected video-generation models on JAX/Flax TPU meshes.

**Boundary:** TPU/model combinations require individual qualification; debugging notes show that residual and intermediate precision can alter video quality despite superficially similar math.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `model-port`, `tensor-parallelism`, `sequence-parallelism`, `model-specific-kernels`.

**Constraints:** `model-family`, `device`, `long-sequence`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/README.md) · [Source 2](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/core/attention.py) · [Source 3](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/core/sharding.py) · [Source 4](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/models/wan/wan2_1/dit.py) · [Source 5](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/docs/lessons/wan2_1_debugging.md) · [Source 6](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/docs/benchmarking.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="vla-simd"></a>

### [vla.simd](https://github.com/cair-vinuni/vla.simd)

[core](systems.md#core) · `system` · `runtime` · `multimodal` · **public code**

**Survey relevance:** Rebuilds selected robot-policy model paths around CPU SIMD operators and model adapters, exposing action preprocessing and numerical-porting obligations beyond a language-model runtime.

Rebuilds model operators, GGUF loading and action inference in C++ with architecture-specific SIMD dispatch and a separate robot-client interface.

**Scope:** Selected vision-language-action policies on x86 AVX2 and ARM NEON/Apple CPU paths.

**Boundary:** Action throughput is not closed-loop robot control frequency; numerical fixtures and model support do not establish safety or general task success after quantization.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `simd-dispatch`, `weight-quantization`, `model-specific-kernels`.

**Constraints:** `model-family`, `device`, `latency`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/README.md) · [Source 2](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/src/hal/arch.h) · [Source 3](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/src/nn/linear.cpp) · [Source 4](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/docs/development.md) · [Source 5](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/docs/benchmark/intel-core-ultra-9-285k.md) · [Source 6](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/tools/check_model_parity.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="vllm-radiance"></a>

### [vLLM Radiance](https://github.com/magiccodingman/vllm-radiance)

[core](systems.md#core) · `system` · `backend` · `text / multimodal` · **public code**

**Survey relevance:** Substantial specialized backend/distribution: preserves vLLM services while replacing device-critical execution and explicitly managing upstream patch dependencies.

A pinned vLLM stack integrates Radiance/libr4d HIP kernels and guarded patches for attention, GDN, MXFP4 W4A8, collectives and speculative execution.

**Scope:** Dual Radeon AI PRO R9700 gfx1201 serving exposes missing efficient RDNA4 attention, recurrent, low-bit and collective paths in a general framework.

**Boundary:** Experimental; primary qualification is TP2 R9700 with FP8 KV. Speculative equivalence gates remain unmet, W4A8 changes checkpoint arithmetic, and NVFP4 conversion is not native NVFP4 execution.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/README.md) · [Source 2](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/radiance_r4d_attn.py) · [Source 3](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/radiance_mxfp4.py) · [Source 4](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/docs/maintenance/ARCHITECTURE.md) · [Source 5](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/docs/NUMERICAL_CORRECTIONS.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="voxgen"></a>

### [VoxGen](https://github.com/NullMagic2/VoxGen)

[core](systems.md#core) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Reconstructs VoxCPM2 speech synthesis in Rust while directly controlling Vulkan buffers, shaders and incremental PCM state, including a separately tuned RDNA3 device profile.

Reconstructs the VoxCPM2 pipeline in Rust with direct Vulkan command/memory control, selected fused shaders, reference-state caching and incremental PCM production.

**Scope:** VoxCPM2 speech synthesis with Vulkan, including a tuned AMD RDNA3 profile.

**Boundary:** Normal and tuned GPU profiles have different qualification scope; smoke tests and author throughput reports are not a broad speech-quality evaluation.

**Semantic considerations:** layout / scheduling, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-kernels`, `kernel-fusion`, `streaming-decoder`.

**Constraints:** `model-family`, `device`, `latency`.

**Evidence:** [Source 1](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/README.md) · [Source 2](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/src/runtime.rs) · [Source 3](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/src/vulkan.rs) · [Source 4](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/build_linux/smoke_pipeline_f16.sh).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="vte"></a>

### [VTE](https://github.com/kyuubyN/VTE)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Integrated consumer-GPU runtime with public profiling and bug-history evidence explaining why it was rebuilt.

Parses GGUF, generates HIP kernels from templates, manages a VRAM slab and replays decode graphs through a ctypes HIP bridge; batched prefill and decode are explicit runtime paths.

**Scope:** Consumer RDNA3 GPUs, especially RX 7600 with 8 GB VRAM and Windows driver constraints, motivate direct control of memory and dispatch.

**Boundary:** Curated architectures and quantizations; larger models can trail llama.cpp. Driver, platform and compile-only GPU targets must be distinguished from hardware-tested paths.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/README.md) · [Source 2](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/docs/ARCHITECTURE.md) · [Source 3](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/docs/PERFORMANCE.md) · [Source 4](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/vte/core/model.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="whisper-cpp"></a>

### [whisper.cpp](https://github.com/ggml-org/whisper.cpp)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Established native speech-model route: a historical control for what purpose-built runtimes and cross-backend maintenance already required.

Provides an established native Whisper/ggml runtime, with converted weights, optional quantization and platform-specific encoder acceleration.

**Scope:** Whisper ASR on local CPU and diverse accelerator backends.

**Boundary:** Historical native execution establishes precedent, not evidence that recent AI coding reduced construction cost; backend and precision results need controlled comparisons.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `weight-quantization`, `backend-dispatch`.

**Constraints:** `model-family`, `device`, `memory-capacity`.

**Evidence:** [Source 1](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/README.md) · [Source 2](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/src/whisper.cpp) · [Source 3](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/CMakeLists.txt) · [Source 4](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/tests/CMakeLists.txt).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="whisperkit"></a>

### [WhisperKit](https://github.com/argmaxinc/argmax-oss-swift)

[adjacent](systems.md#adjacent) · `system` · `runtime` · `audio` · **public code**

**Survey relevance:** Compiler-backed speech deployment provides a comparison for how much execution control remains in the runtime versus compiled platform artifacts.

Owns speech preprocessing, encoder/decoder orchestration, caches and segmentation around Core ML artifacts within the Argmax Swift repository.

**Scope:** Apple Silicon speech recognition through compiled Core ML model components.

**Boundary:** The canonical repository now contains multiple products; this entry covers WhisperKit only. Core ML compilation and model qualification differ from a new native tensor engine.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `compiled-model`, `decoder-orchestration`, `chunked-streaming`.

**Constraints:** `model-family`, `device`, `latency`.

**Evidence:** [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/README.md) · [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/Sources/WhisperKit/Core/WhisperKit.swift) · [Source 3](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/Sources/WhisperKit/Core/TextDecoder.swift) · [Source 4](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/Tests/WhisperKitTests/UnitTests.swift).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="zinc"></a>

### [ZINC](https://github.com/zolotukhin/zinc)

[core](systems.md#core) · `system` · `runtime` · `text` · **public code**

**Survey relevance:** Consumer-hardware execution-stack reconstruction with inspectable native model paths and backend-specific measurements.

A Zig runtime owns loading, model forward/decode graphs, KV state and serving; Vulkan and HIP/ROCm paths use native dispatch, with separate Metal and experimental CUDA backends.

**Scope:** Local consumer GPUs motivate explicit memory ownership and native per-backend execution for a selected GGUF model catalog.

**Boundary:** Backend coverage and measurements differ. ROCm and Vulkan trade prefill/decode performance; current results are not universal hardware or model claims.

**Semantic considerations:** configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-execution`, `kernel-specialization`.

**Constraints:** `hardware`, `model`, `workload`.

**Evidence:** [Source 1](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/README.md) · [Source 2](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/src/compute/forward.zig) · [Source 3](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/src/rocm/rocm_shim.c) · [Source 4](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/docs/DEVELOPMENT.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="zllm"></a>

### [zLLM](https://github.com/zllm-lab/zllm)

[core](systems.md#core) · `system` · `runtime` · `text / image / video / audio / multimodal` · **public code**

**Survey relevance:** A growing collection of native model/device execution paths, including vision-language, image generation and video restoration, with explicit per-backend capability limits.

Rust runtimes own model loading, graph execution and state. Inspected paths implement DeepSeek vision processing, ROCm FLUX text-conditioning/denoising/VAE stages and multi-GPU SeedVR2 sequence partitioning; MiniCPM QNN uses a separately validated native runner.

**Scope:** Selected model/backend pairs across Metal, CUDA, ROCm and CPU; experimental Snapdragon HTP paths.

**Boundary:** Broad model lists do not mean every backend supports every model. MiniCPM QNN checks calibrated prompt tokens and expected output; it is not arbitrary-prompt serving. Video restoration is distinct from video generation; throughput is author-reported.

**Semantic considerations:** layout / scheduling, reduced precision, configuration-dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `native-runtime`, `model-specific-execution`, `vision-language-fusion`, `diffusion-pipeline`, `sequence-parallelism`.

**Constraints:** `model-architecture`, `target-device`.

**Evidence:** [Source 1](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/README.md) · [Source 2](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/deepseek_v4/vision.rs) · [Source 3](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/flux2_klein/rocm.rs) · [Source 4](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/seedvr2/rocm_pipeline.rs) · [Source 5](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/minicpm5/qnn.rs).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `keyword`.

</details>

<a id="construction"></a>

## Construction & validation tools / 构建与验证工具 (16)

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

<a id="ane-field-guide"></a>

### [Apple Neural Engine Field Guide](https://github.com/skyfallsin/apple-neural-engine-field-guide)

[foundation](systems.md#foundation) · `support` · `knowledge-base` · `text` · **public code**

**Survey relevance:** Concrete hardware-investigation knowledge and accepted/rejected experiments feed the separately cataloged ane.cpp engine.

Uses small MIL/ANE probes and CPU-reference checks to investigate execution limits, records kept and discarded experiments, and transfers supported findings into ane.cpp.

**Scope:** Empirical Apple M3 Max ANE behavior, private framework APIs and Qwen-family execution motivate targeted probes.

**Boundary:** Findings and timing reports are author-measured and primarily M3-Max-specific; private APIs may change. This is a knowledge/probe resource linked to ane.cpp, not an additional inference engine.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hardware-probing`, `experiment-ledger`, `knowledge-transfer`.

**Constraints:** `hardware`, `model`, `toolchain`.

**Evidence:** [Source 1](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/README.md) · [Source 2](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/program.md) · [Source 3](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/results.tsv) · [Source 4](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/tests/test_dispatch_scaling.cpp).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="atrex-kernel-agent"></a>

### [Atrex Kernel Agent (AKA)](https://github.com/alibaba/atrex-kernel-agent)

[adjacent](systems.md#adjacent) · `construction` · `generator` · `general` · **public code**

**Survey relevance:** Operator-level construction harness connecting coding agents, measured feedback, acceptance gates and reusable optimization knowledge.

Runs coding episodes in isolated worktrees, evaluates numerical and performance results before promotion, and uses profiler feedback plus scoped GPU Wiki retrieval to guide further revisions.

**Scope:** Evaluator-owned GPU operator tasks, target DSL/device and fixed optimization budgets constrain candidate search and acceptance.

**Boundary:** Produces operator kernels, not a complete inference engine. Fast and full episodes use different measurement gates; production policy and finite numerical probes do not prove arbitrary-input correctness. GPU Wiki is a component of this record, not another repository count.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `profile-feedback`, `candidate-validation`, `knowledge-retrieval`.

**Constraints:** `hardware`, `workload`, `dsl`, `validation-budget`.

**Evidence:** [Source 1](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/README.md) · [Source 2](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/long_horizon/campaign.py) · [Source 3](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/orchestrator/optimization_policy.py) · [Source 4](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/tools/profile_nvidia.sh) · [Source 5](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/gpu-wiki/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `dependency`.

</details>

<a id="atrex-bench"></a>

### [Atrex-Bench](https://github.com/alibaba/atrex-bench)

[foundation](systems.md#foundation) · `benchmark` · `benchmark` · `general` · **public code**

**Survey relevance:** Production-derived operator tasks and separated evaluation provide a benchmark for generated execution components.

Packages reference programs and input/shape generators, separates agent-visible tasks from evaluator metadata, and checks compilation, numerical outputs/input mutations and forward timing against a roofline estimate.

**Scope:** Production-trace operator shapes, executable PyTorch references and target GPU/DSL determine the generation and evaluation contract.

**Boundary:** End-to-end refers to operator generation and evaluation, not a complete serving stack; correctness uses finite inputs and tolerances, and roofline efficiency is not an application-level speedup.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `trace-derived-tasks`, `reference-validation`, `roofline-evaluation`.

**Constraints:** `workload`, `hardware`, `dsl`, `precision`.

**Evidence:** [Source 1](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/README.md) · [Source 2](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/src/atrex_bench/eval/correctness.py) · [Source 3](https://github.com/alibaba/atrex-bench/blob/22d6a57b98ebb45c8db76e98815158d820c1dca3/src/atrex_bench/eval/performance.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `dependency`.

</details>

<a id="fastkernels"></a>

### [FastKernels](https://github.com/Snowflake-AI-Research/fastkernels)

[foundation](systems.md#foundation) · `benchmark` · `benchmark` · `text / image / video / audio / multimodal / general` · **public code**

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

[foundation](systems.md#foundation) · `benchmark` · `benchmark` · `general` · **public code**

**Survey relevance:** Executable tasks for kernel and model-program construction workflows such as KernelAgent; task-level acceptance remains separate from deployed-engine validation.

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

<a id="kernelwiki"></a>

### [KernelWiki](https://github.com/mit-han-lab/KernelWiki)

[foundation](systems.md#foundation) · `support` · `knowledge-base` · `general` · **public code**

**Survey relevance:** Retrievable hardware and kernel experience connects prior engineering work with subsequent specialized implementation decisions.

Indexes upstream PRs, hardware documents and optimization notes with architecture/symptom filters, and links synthesized pages to captured kernel artifacts and provenance.

**Scope:** NVIDIA Blackwell / Hopper kernel programming, hardware features and version-specific CUDA/DSL behavior delimit the knowledge corpus.

**Boundary:** Kernel-level knowledge support rather than an engine or proof of lower development cost. Corpus cutoffs and source confidence matter; included assets retain upstream licensing and are not independently reproduced by this survey.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `source-linked-knowledge`, `scoped-retrieval`, `versioned-provenance`.

**Constraints:** `hardware`, `dsl`, `toolchain`.

**Evidence:** [Source 1](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/README.md) · [Source 2](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/scripts/query.py) · [Source 3](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/wiki/techniques/warp-specialization.md) · [Source 4](https://github.com/mit-han-lab/KernelWiki/blob/b6b4301f15e8ce6955a56776690643ce5db369e6/artifacts/kernels/warp-specialization/full/PROVENANCE.yaml).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="metainfer"></a>

### [MetaInfer](https://github.com/MetaInfer/MetaInfer)

[core](systems.md#core) · `construction` · `generator` · `text` · **public code**

**Survey relevance:** Connects a disclosed construction workflow to the VibeQwen engine case; the toolbox and generated engine are different artifacts.

Orchestrates coding agents to iteratively build deployment-specific inference servers, then launches fixed server contracts through correctness and performance oracle phases.

**Scope:** Requested model, hardware, parallelism, precision, API contract and iteration budget define the generated artifact.

**Boundary:** The inspected correctness oracle uses fixed prompts with LLM or heuristic judgments; only hard-case results determine its aggregate pass. This checks selected functional behavior, not numerical equivalence or unrestricted model correctness.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `contract-validation`, `benchmark-feedback`.

**Constraints:** `model`, `hardware`, `precision`, `workload`.

**Evidence:** [Source 1](https://github.com/MetaInfer/MetaInfer/blob/HEAD/README.md) · [Source 2](https://github.com/MetaInfer/MetaInfer/blob/HEAD/metainfer/tasks/gen_infer_framework/orchestrator/pipeline.py) · [Source 3](https://github.com/MetaInfer/MetaInfer/blob/HEAD/metainfer/tasks/gen_infer_framework/orchestrator/oracles/correctness.py).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `initial`.

</details>

<a id="ncu-report-skill"></a>

### [ncu-report-skill](https://github.com/mit-han-lab/ncu-report-skill)

[foundation](systems.md#foundation) · `support` · `diagnostic` · `general` · **public code**

**Survey relevance:** Diagnostic companion for connecting measured kernel bottlenecks to an agent-guided optimization decision.

Provides a profiling harness, extracts and compares NCU metrics and source-level stall evidence, and maps observed signals to candidate optimization directions.

**Scope:** CUDA kernel profiling with Nsight Compute; metric selection and examples primarily target NVIDIA B200 / sm_100.

**Boundary:** A reusable diagnosis workflow rather than a kernel generator or inference runtime; counter names and heuristics require device-specific checking, and suggested fixes need measured validation.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `profile-feedback`, `counter-analysis`, `diagnosis-playbook`.

**Constraints:** `hardware`, `workload`, `toolchain`.

**Evidence:** [Source 1](https://github.com/mit-han-lab/ncu-report-skill/blob/74a12918e9f64d78036f14da5f8765e435b949a4/README.md) · [Source 2](https://github.com/mit-han-lab/ncu-report-skill/blob/74a12918e9f64d78036f14da5f8765e435b949a4/helpers/analyze_reports.py) · [Source 3](https://github.com/mit-han-lab/ncu-report-skill/blob/74a12918e9f64d78036f14da5f8765e435b949a4/reference/06-diagnosis-playbook.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `intrinsic` · **Discovery:** `dependency`.

</details>

<a id="seis"></a>

### [SEIS: Self-Evolving Inference Systems](https://github.com/smth-fun/self-evolving-inference-system)

[core](systems.md#core) · `construction` · `generator` · `text` · **public code**

**Survey relevance:** Sustained agent-driven reconstruction of an existing inference engine connects inherited code and reports to kernel, runtime and decoding changes; the study also exposes gaps in its evolving validation gates.

Keeps the coding agent fixed while successive sessions inherit and revise engine code and reports; the paper also exchanges discoveries across chains. Changes span quantized kernels, fusion, CUDA Graph execution, scheduler/state handling and prompt-lookup decoding.

**Scope:** The paper centers on Qwen3-0.6B on one H100 with single-request greedy decoding, with supplementary Llama-3.2-1B experiments. The linked public ten-trial example uses RTX PRO 6000 Blackwell and is a separate configuration.

**Boundary:** The paper reports 3.27x natural-request throughput on H100; the linked public demo reports 512 to 1016 tokens/s on RTX PRO 6000 Blackwell. Do not conflate these artifacts or budgets. Quantization changes numerics, finite gates do not prove equivalence, and the public ten-trial driver does not establish availability of every paper experiment or synchronization protocol. No independent execution was performed here.

**Semantic considerations:** generated-artifact dependent, reduced precision.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `code-inheritance`, `cross-session-optimization`, `kernel-runtime-cooptimization`, `quality-validation`.

**Constraints:** `model`, `hardware`, `workload`, `precision`.

**Evidence:** [Source 1](https://arxiv.org/html/2610.04646v1) · [Source 2](https://github.com/smth-fun/self-evolving-inference-system/blob/bf2ddc5c5882a2573756b744c0e88c1b154739fa/README.md) · [Source 3](https://github.com/smth-fun/self-evolving-inference-system/blob/bf2ddc5c5882a2573756b744c0e88c1b154739fa/run_trial.sh) · [Source 4](https://github.com/smth-fun/mini-sglang/blob/2c1f6c307c96aa165873ad785cb0fa71fb71f9d3/python/minisgl/engine/engine.py).

**Reviewed:** 2026-10-14 · **AI involvement:** `intrinsic` · **Discovery:** `keyword`.

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

<a id="tilelang"></a>

### [TileLang](https://github.com/tile-ai/tilelang)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / video / general` · **public code**

**Survey relevance:** Kernel language supported by the included Atrex Kernel Agent campaigns; a generated kernel remains distinct from a complete model runtime.

Lowers tile-level kernel programs through target-specific layout and software-pipeline passes, generating GPU/accelerator code for tiled memory movement and matrix operations.

**Scope:** Device architecture, tile shapes, tensor-memory features, data precision and supported backend passes constrain generated kernels.

**Boundary:** TileLang is a kernel DSL/compiler, not a full inference runtime; backend maturity differs and some targets deliberately disable unvalidated asynchronous pipeline paths.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hardware-codegen`, `tile-layouts`, `software-pipelining`, `kernel-autotuning`.

**Constraints:** `hardware`, `shape`, `precision`.

**Evidence:** [Source 1](https://github.com/tile-ai/tilelang/blob/HEAD/README.md) · [Source 2](https://github.com/tile-ai/tilelang/blob/HEAD/tilelang/engine/lower.py) · [Source 3](https://github.com/tile-ai/tilelang/blob/HEAD/src/transform/pipeline_planning.cc) · [Source 4](https://github.com/alibaba/atrex-kernel-agent/blob/b708d9fcd0eff5214bcc5b91aae62357356e525c/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="triton"></a>

### [Triton](https://github.com/triton-lang/triton)

[foundation](systems.md#foundation) · `support` · `compiler` · `text / image / video / general` · **public code**

**Survey relevance:** Kernel language emitted or optimized by KernelAgent and Atrex Kernel Agent, linking generated programs to their compilation and validation boundary.

Compiles block-structured kernel programs for a selected GPU target and specializes cached binaries and autotuned launch configurations to argument signatures and compile-time constants.

**Scope:** Target architecture, pointer/value signatures, compile-time constants, warp/stage counts and autotuning keys determine kernel variants.

**Boundary:** Triton supplies kernel construction infrastructure; it does not supply model loading, serving policy or end-to-end inference correctness by itself.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `hardware-codegen`, `kernel-specialization`, `kernel-autotuning`.

**Constraints:** `hardware`, `shape`, `precision`.

**Evidence:** [Source 1](https://github.com/triton-lang/triton/blob/HEAD/README.md) · [Source 2](https://github.com/triton-lang/triton/blob/HEAD/python/triton/compiler/compiler.py) · [Source 3](https://github.com/triton-lang/triton/blob/HEAD/python/triton/runtime/autotuner.py) · [Source 4](https://github.com/meta-pytorch/KernelAgent/blob/HEAD/README.md).

**Reviewed:** 2026-10-12 · **AI involvement:** `not-established` · **Discovery:** `dependency`.

</details>

<a id="vibesys"></a>

### [VibeServe / VibeSys](https://github.com/uw-syfi/vibesys)

[core](systems.md#core) · `construction` · `generator` · `text / audio / multimodal` · **public code**

**Survey relevance:** Connects generation-time model/hardware/workload specialization to a concrete serving-system initiative; the broader generator and its scenario-specific outputs are distinct artifacts.

Separates design search from implementation and target-specific measurement; durable history carries hypotheses while framework-owned evaluation identities and candidate isolation connect code changes to reviewed results.

**Scope:** The VibeServe initiative studies target-specific language serving, streaming ASR, constrained output, multimodal workloads and Apple Silicon. The current VibeSys repository also serves non-inference domains, which are outside this record.

**Boundary:** The May 2026 VibeServe paper and the October-reviewed VibeSys implementation are not identical revisions. Results concern selected scenarios and declared contracts, not arbitrary serving workloads or proven lifecycle savings. Evaluation wiring was source-inspected; no agent campaign or generated engine was executed.

**Semantic considerations:** generated-artifact dependent.

<details>
<summary>Mechanism tags and source evidence / 机制标签与证据</summary>

**Mechanisms:** `agent-generation`, `design-search`, `profile-feedback`, `evaluator-isolation`, `artifact-provenance`.

**Constraints:** `model`, `hardware`, `workload`, `validation-contract`.

**Evidence:** [Source 1](https://arxiv.org/html/2605.06068v1) · [Source 2](https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/) · [Source 3](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/README.md) · [Source 4](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/src/vibesys/core_wiring.py).

**Reviewed:** 2026-10-14 · **AI involvement:** `intrinsic` · **Discovery:** `keyword`.

</details>

