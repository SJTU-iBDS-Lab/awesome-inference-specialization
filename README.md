# Awesome Inference Specialization

**Find specialized inference engines, understand how they are built, and choose the checks their outputs need.**

[中文](README_CN.md) · [Find engines](#homepage-system) · [Build workflows](#homepage-construction) · [Validate](#homepage-validation) · [Benchmarks](#homepage-benchmark) · [Resources](#homepage-support) · [Quick comparison](docs/representative-comparison.md) · [Latest updates](docs/updates.md)

Known models, devices and workloads allow different execution stacks. Browse every project, construction workflow, validation method, benchmark and supporting resource directly below, with upstream links, descriptions and model-domain tags. Language, multimodal, image, video and audio workloads are covered.

**Latest, 2026-10-12:** the homepages now list all 121 projects and expand four validation contracts with six method entries; the [case comparison](docs/representative-comparison.md) and [cross-case synthesis](docs/synthesis.md) are supplementary reading. [What changed and what was checked](docs/updates.md).

## Complete Awesome list

<!-- CATALOG-START -->

All **121 projects** are listed below, once each under their primary role. Model domains appear on every entry. Validation methods are expanded separately; embedded checks do not add repository counts.

## Contents

- [Specialized inference engines](#homepage-system) (89)
  - [Data residency & movement](#homepage-system-memory)
  - [Numerical representation](#homepage-system-precision)
  - [Selective computation](#homepage-system-selection)
  - [Computation reuse](#homepage-system-reuse)
  - [Generation order](#homepage-system-decoding)
  - [Parallelism & scheduling](#homepage-system-serving)
  - [Compiled & native execution](#homepage-system-execution)
- [Engine construction and optimization](#homepage-construction) (11)
  - [Compiled & native execution](#homepage-construction-execution)
  - [Construction & validation tools](#homepage-construction-construction)
- [Correctness and quality validation](#homepage-validation) (4 contracts, 6 method entries)
  - [Operator and subgraph numerics](#homepage-validation-numerical)
  - [Composed model and persistent state](#homepage-validation-model-state)
  - [Generated-output quality](#homepage-validation-quality)
  - [Service and integration behavior](#homepage-validation-service)
- [Benchmarks and task suites](#homepage-benchmark) (3)
- [Companion resources](#homepage-support) (18)
  - [Performance diagnosis](#homepage-support-diagnostics)
  - [Construction knowledge and experience](#homepage-support-knowledge)
  - [General-engine baselines](#homepage-support-engine-baselines)
  - [Compilers and kernel languages](#homepage-support-compilers)
  - [Reusable execution and model preparation](#homepage-support-components)
- [Selected reading and comparison](#featured-reading)

<a id="homepage-system"></a>

## Specialized inference engines

Integrated model runtimes and substantial specialized backends, including native implementations and earlier execution-stack precedents.

[Role and evidence index](docs/systems.md#system)

<a id="homepage-system-memory"></a>

### Data residency & movement (15)

Place, page, prefetch or offload weights, experts and KV state.

- <a id="project-anemll-flash-llama"></a>**[ANEMLL Flash llama.cpp](https://github.com/Anemll/anemll-flash-llama.cpp)** — Adds expert sidecars, native expert-to-slot mapping and layer-major prefill to llama.cpp, reusing each staged expert across relevant prompt rows. **[Language models]** [Scope, sources and limits](docs/catalog.md#anemll-flash-llama)
- <a id="project-colibri"></a>**[Colibri](https://github.com/JustVugg/colibri)** — Keeps dense state resident and streams routed experts through model-family-specific execution paths, with optional CPU/GPU tier placement and specialized containers. **[Language models / Image generation & processing / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#colibri)
- <a id="project-zero-inference"></a>**[DeepSpeed ZeRO-Inference](https://github.com/deepspeedai/DeepSpeedExamples)** — Hosts weights in CPU or NVMe memory and streams them layer by layer to GPU, using prefetch and large token batches to amortize transfer costs while preserving GPU memory for activations. **[Language models]** [Scope, sources and limits](docs/catalog.md#zero-inference)
- <a id="project-fiddler"></a>**[Fiddler](https://github.com/efeslab/fiddler)** — Executes uncached MoE experts on CPU by transferring small activations instead of moving their large weights to GPU, while keeping selected experts resident on GPU. **[Language models]** [Scope, sources and limits](docs/catalog.md#fiddler)
- <a id="project-flash-moe"></a>**[Flash-MoE](https://github.com/danveloper/flash-moe)** — Streams selected quantized expert blobs with parallel pread and executes a fixed Qwen hybrid-attention pipeline using custom Metal dequantization and fused expert kernels. **[Language models]** [Scope, sources and limits](docs/catalog.md#flash-moe)
- <a id="project-flexllmgen"></a>**[FlexLLMGen (FlexGen)](https://github.com/FMInference/FlexLLMGen)** — Uses a block generation schedule and GPU/CPU/disk tensor placement to reuse layer weights across microbatches while overlapping transfers and optionally compressing weights and KV state. **[Language models]** [Scope, sources and limits](docs/catalog.md#flexllmgen)
- <a id="project-hybrimoe"></a>**[HybriMoE](https://github.com/PKU-SEC-Lab/HybriMoE)** — Extends a KTransformers-based execution path with hybrid CPU/GPU expert scheduling, impact-driven prefetching and score-based expert-cache management. **[Language models]** [Scope, sources and limits](docs/catalog.md#hybrimoe)
- <a id="project-infernix"></a>**[Infernix](https://github.com/wallawalla47/infernix)** — Extends NInfer with a GPU hot-expert cache, pinned-host experts, CPU computation of selected misses, overlapped PCIe transfers and an NVMe-backed n-gram volume. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#infernix)
- <a id="project-ktransformers"></a>**[KTransformers / kt-kernel](https://github.com/kvcache-ai/ktransformers)** — Runs memory-heavy MoE experts through ISA-specific CPU kernels and NUMA-aware placement while integrating with GPU serving runtimes for the remaining model computation. **[Language models]** [Scope, sources and limits](docs/catalog.md#ktransformers)
- <a id="project-moe-infinity"></a>**[MoE-Infinity](https://github.com/EfficientMoE/MoE-Infinity)** — Offloads expert weights to host memory and SSD, retains hot experts in an activation-aware GPU cache and uses trace/prediction-driven prefetching through a native transfer engine. **[Language models]** [Scope, sources and limits](docs/catalog.md#moe-infinity)
- <a id="project-strata"></a>**[Strata](https://github.com/Niko1221/Strata)** — Keeps attention and hot experts on GPU, computes nonresident experts on CPU concurrently, and budgets GPU/RAM/file tiers for experts and long-context KV state. **[Language models]** [Scope, sources and limits](docs/catalog.md#strata)
- <a id="project-swiftlet"></a>**[Swiftlet](https://github.com/leonickson1/Swiftlet)** — Implements Swift/Metal forward paths with a small resident dense core, fixed-stride expert containers, pread slot caching and native KV/recurrent state. **[Language models]** [Scope, sources and limits](docs/catalog.md#swiftlet)
- <a id="project-swiftlm"></a>**[SwiftLM](https://github.com/SharpAI/SwiftLM)** — Extends MLX Swift execution through maintained forks, explicit expert reads, asynchronous I/O workers and synchronization boundaries coordinated with model generation. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#swiftlm)
- <a id="project-tuff"></a>**[TUFF](https://github.com/rexmhall09/TUFF)** — Extends a Swift/Metal runtime with model-specific forward paths, bounded expert streaming, resident state and a separate inference service. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#tuff)
- <a id="project-turbo-fieldfare"></a>**[TurboFieldfare](https://github.com/drumih/turbo-fieldfare)** — Keeps common weights and FP16 KV resident, reads routed experts with bounded pread slot caches, and coordinates chunked prefill and Metal execution. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#turbo-fieldfare)

<a id="homepage-system-precision"></a>

### Numerical representation (5)

Co-design low-bit formats, layouts and execution kernels.

- <a id="project-bitnet-cpp"></a>**[bitnet.cpp](https://github.com/microsoft/BitNet)** — Executes compatible ternary LLMs with packed low-bit kernels and architecture-specific LUT paths, choosing pre-tuned or generated kernel headers for model shapes. **[Language models]** [Scope, sources and limits](docs/catalog.md#bitnet-cpp)
- <a id="project-exllamav3"></a>**[ExLlamaV3](https://github.com/turboderp-org/exllamav3)** — Pairs EXL3 weight quantization with dedicated low-bit execution, 2–8-bit paged KV storage and shape-qualified decode paths, plus CPU expert offload and parallel inference. **[Language models]** [Scope, sources and limits](docs/catalog.md#exllamav3)
- <a id="project-ik-llama"></a>**[ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)** — Extends a llama.cpp fork with additional packed quantization formats, CPU IQK matrix kernels and quantization-specific CUDA dispatch paths. **[Language models]** [Scope, sources and limits](docs/catalog.md#ik-llama)
- <a id="project-nunchaku"></a>**[Nunchaku](https://github.com/nunchux-ai/nunchaku)** — Executes SVDQuant W4A4 layers by fusing activation quantization with the low-rank down projection and low-bit GEMM with the low-rank output path. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#nunchaku)
- <a id="project-rocmfpx"></a>**[ROCmFPX](https://github.com/ROCmFPX/ROCmFPX)** — A llama.cpp downstream defines ROCmFPX quantization blocks, conversion policies and backend kernels, including RDNA3-specific MMQ layouts and an optional Vulkan plugin. **[Language models]** [Scope, sources and limits](docs/catalog.md#rocmfpx)

<a id="homepage-system-selection"></a>

### Selective computation (2)

Select neurons, tokens or attention blocks; expose approximation.

- <a id="project-powerinfer"></a>**[PowerInfer](https://github.com/Tiiny-AI/PowerInfer)** — Uses profiled neuron activation frequencies and a capacity-constrained split to place hot neurons on GPU, execute cold activated neurons on CPU and dispatch predictor-guided sparse operators. **[Language models]** [Scope, sources and limits](docs/catalog.md#powerinfer)
- <a id="project-turbodiffusion"></a>**[TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)** — Integrates SageAttention and sparse-linear attention with timestep-distilled video checkpoints and optional quantized linear layers in an executable generation stack. **[Video generation & processing]** [Scope, sources and limits](docs/catalog.md#turbodiffusion)

<a id="homepage-system-reuse"></a>

### Computation reuse (1)

Reuse request prefixes, features or attention across steps.

- <a id="project-videosys"></a>**[VideoSys](https://github.com/NUS-HPC-AI-Lab/VideoSys)** — Combines Pyramid Attention Broadcast with dynamic sequence parallelism, reusing attention outputs at type-specific intervals and changing sequence partitions across attention axes. **[Video generation & processing]** [Scope, sources and limits](docs/catalog.md#videosys)

<a id="homepage-system-decoding"></a>

### Generation order (2)

Draft and verify tokens, or reorganize block generation.

- <a id="project-inferix"></a>**[Inferix](https://github.com/alibaba-damo-academy/Inferix)** — Manages persistent KV state for semi-autoregressive diffusion blocks while separately chunking VAE decoding and streaming generated video. **[Video generation & processing]** [Scope, sources and limits](docs/catalog.md#inferix)
- <a id="project-llamampere"></a>**[llamAmpere](https://github.com/JakeATX/llamAmpere)** — Extends the llama.cpp/TurboQuant lineage with SM86 verification kernels, a draft-only vocabulary shortlist, format-specific quantized execution, SJ-KVaRN compressed KV and RAM/disk prompt-state reuse. **[Language models]** [Scope, sources and limits](docs/catalog.md#llamampere)

<a id="homepage-system-serving"></a>

### Parallelism & scheduling (6)

Partition stages, devices and requests around workload constraints.

- <a id="project-gufo-rdma"></a>**[Gufo RDMA](https://github.com/neuhaus/gufo)** — Adds model-specific tensor partitioning, RDMA collectives and mirrored request execution to Gufo, using libibverbs over InfiniBand, RoCE or qualified USB4 networking. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#gufo-rdma)
- <a id="project-llaminar"></a>**[Llaminar](https://github.com/Llaminar/llaminar)** — Builds model-specific compute graphs and rank plans, placing tensor/pipeline stages and MoE experts across devices; retained native graphs coordinate through NCCL, RCCL, MPI or heterogeneous host bridges. **[Language models]** [Scope, sources and limits](docs/catalog.md#llaminar)
- <a id="project-streamdiffusion"></a>**[StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion)** — Reorganizes Diffusers components into StreamBatch execution with residual guidance, input filtering and optional compiled UNet/VAE paths. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#streamdiffusion)
- <a id="project-streamdiffusion-v2"></a>**[StreamDiffusionV2](https://github.com/chenfengxu714/StreamDiffusionV2)** — Reorganizes denoising across streamed chunks and stages, with model-aware KV state and distributed cache ownership rather than an offline wrapper alone. **[Video generation & processing]** [Scope, sources and limits](docs/catalog.md#streamdiffusion-v2)
- <a id="project-telefuser"></a>**[TeleFuser](https://github.com/Tele-AI/TeleFuser)** — Owns model pipelines and staged denoising, plus an actor-based streaming scheduler that separates retained session state from execution leases and applies backpressure. **[Video generation & processing / Image generation & processing / Speech & audio / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#telefuser)
- <a id="project-xdit"></a>**[xDiT](https://github.com/xdit-project/xDiT)** — Combines Ulysses and Ring sequence parallelism with CFG/data parallelism and PipeFusion patch pipelines that reuse earlier-step features to overlap communication. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#xdit)

<a id="homepage-system-execution"></a>

### Compiled & native execution (58)

Fuse, lower, specialize and dispatch graphs or native kernels.

- <a id="project-ane-lm"></a>**[ANE-LM](https://github.com/johnmai-dev/ANE-LM)** — Implements Qwen forward paths combining compiled ANE kernels with CPU operations and a persistent compile cache. **[Language models]** [Scope, sources and limits](docs/catalog.md#ane-lm)
- <a id="project-ane-cpp"></a>**[ane.cpp](https://github.com/skyfallsin/ane.cpp)** — Compiles weight-bearing MIL convolution programs for ANE while retaining CPU normalization, attention and KV operations, then caches compiled variants and batches lanes. **[Language models]** [Scope, sources and limits](docs/catalog.md#ane-cpp)
- <a id="project-aria"></a>**[Aria](https://github.com/matteospanio/aria)** — Implements T5Gemma conditioning, diffusion transformer, sampler and audio decoder in C with mmap weights, optional quantization and intermediate-state steering. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#aria)
- <a id="project-basert"></a>**[BaseRT](https://github.com/basecompute/baseRT)** — A proprietary native engine executes models packaged by an open converter and exposed through public C APIs and language bindings. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#basert)
- <a id="project-brain"></a>**[BRaiN](https://github.com/swedishembedded/brain)** — Rust model implementations use a shared WGSL compute engine. Inspected Qwen3-VL integrates vision features with language decoding; Wan stages text encoding, denoising and VAE decoding to bound residency. **[Language models / Image generation & processing / Video generation & processing / Speech & audio / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#brain)
- <a id="project-brodiffusion"></a>**[brodiffusion](https://github.com/wlejon/brodiffusion)** — Implements model loaders, diffusion pipelines and samplers in C++; replays captured denoiser-step graphs when shape and runtime-state contracts permit. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#brodiffusion)
- <a id="project-cactus"></a>**[Cactus](https://github.com/cactus-compute/cactus)** — Captures supported model components into an intermediate graph, lowers to Cactus graph operations and runs a native engine with ARM/Metal kernels and quantized state. Vision/audio components and language decoding share bundle-managed execution. **[Language models / Image generation & processing / Speech & audio / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#cactus)
- <a id="project-needle"></a>**[Cactus Needle](https://github.com/cactus-compute/needle)** — Needle 3 pairs a sliceable attention architecture and quantized weights with platform-specific native engines. Python tools train/export models and fetch an engine plus weight files for deployment. **[Language models / Speech & audio]** [Scope, sources and limits](docs/catalog.md#needle)
- <a id="project-ciru-runtime"></a>**[CIRU runtime](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4)** — A llama.cpp-derived runtime integrates CIRUPLE1 paging, typed expert kernels, QSA sparse-attention paths and MTP state corrections for pinned CIRU model releases. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#ciru-runtime)
- <a id="project-coreml-llm-cli"></a>**[CoreML LLM CLI](https://github.com/smpanaro/coreml-llm-cli)** — Orchestrates chunked CoreML model execution and KV state, with reshaped convolution layouts and copy-avoiding model buffers. **[Language models]** [Scope, sources and limits](docs/catalog.md#coreml-llm-cli)
- <a id="project-diffusion-rs"></a>**[diffusion-rs](https://github.com/EricLBuehler/diffusion-rs)** — Implements FLUX component loading, sampling and residency policy on a reusable Rust tensor layer, including quantized model support. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#diffusion-rs)
- <a id="project-draw-things"></a>**[Draw Things Community](https://github.com/drawthingsai/draw-things-community)** — Provides independent Swift model graphs and samplers with hardware-backed execution and a TeaCache implementation that switches between full and reduced model execution. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#draw-things)
- <a id="project-dwarfstar"></a>**[DwarfStar](https://github.com/antirez/ds4)** — Executes selected DeepSeek, GLM and Qwen families through native model-specific paths, retaining non-routed state while fetching missing routed experts into a bounded SSD-streaming cache. **[Language models]** [Scope, sources and limits](docs/catalog.md#dwarfstar)
- <a id="project-edge-dit"></a>**[edge-dit.cpp](https://github.com/THU-MIG/edge-dit.cpp)** — Runs DiTs on ggml graphs with automatic quantization and placement, per-component or double-buffered block offload, VAE tiling and model-aware cache policies. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#edge-dit)
- <a id="project-fastflowlm"></a>**[FastFlowLM](https://github.com/ROCm/FastFlowLM)** — Selects a model-family backend, packs or loads compatible weights, owns NPU tensors and decoding streams, and dispatches shape-qualified kernels. The rai path exposes model integration over ryzenai-corelib; original flm engines ship as prebuilt libraries. **[Language models / Speech & audio / Image generation & processing / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#fastflowlm)
- <a id="project-fastvideo"></a>**[FastVideo](https://github.com/hao-ai-lab/FastVideo)** — Owns model and pipeline registries, component loading and staged denoising over shared tensor backends. Dense model paths coexist with optional Video Sparse Attention, sequence parallelism, offload and sparse or timestep-distilled checkpoints. **[Video generation & processing / Speech & audio]** [Scope, sources and limits](docs/catalog.md#fastvideo)
- <a id="project-gufo"></a>**[Gufo](https://github.com/gufo-org/gufo)** — Owns per-model C++/HIP execution, kernels and state alongside serving, batching and continuation caching; Qwen paths integrate model-specific draft/verification cycles while reusing ROCm BLAS and adapted upstream code. **[Language models / Speech & audio / Image generation & processing / Video generation & processing / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#gufo)
- <a id="project-halogen-flash"></a>**[Halogen Flash](https://github.com/peonist-ai/halogen-flash-server)** — Ships a model-and-chip-specific inference binary with mixed-precision weight layouts, a paged n-gram lookup table and dedicated attention/expert execution for Qwen3.8-Flash-Next. **[Language models]** [Scope, sources and limits](docs/catalog.md#halogen-flash)
- <a id="project-hearth"></a>**[Hearth](https://github.com/jeff-hiner/hearth)** — Rebuilds CLIP, UNet, VAE, sampler and node execution in Rust, reusing CubeCL/wgpu for tensor kernels and device access. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#hearth)
- <a id="project-hilum-engine"></a>**[Hilum LLM Engine](https://github.com/hilum-labs/hilum-local-llm-engine)** — Retains llama.cpp/GGML execution and adds mobile backend integration, Adreno shader build/dispatch paths, allocation support and per-device parameter tuning. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#hilum-engine)
- <a id="project-hipengine"></a>**[hipEngine](https://github.com/shisa-ai/hipEngine)** — A Python host drives HIP/C++ model runners, hardware-specific kernels, shared KV/prefix state and continuous batching without PyTorch in the inference runtime. **[Language models / Multimodal understanding & interaction / Speech & audio]** [Scope, sources and limits](docs/catalog.md#hipengine)
- <a id="project-imp"></a>**[imp](https://github.com/kekzl/imp)** — A C++/CUDA engine owns model loading, attention/MoE/recurrent execution, paged KV, CUDA Graph scheduling and OpenAI/Anthropic-compatible serving, with chip-specific kernels. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#imp)
- <a id="project-iris"></a>**[Iris](https://github.com/antirez/iris.c)** — Implements selected FLUX and Z-Image pipelines in C with Metal or CPU kernels, memory-mapped weights and release of text encoders after conditioning. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#iris)
- <a id="project-kipp"></a>**[Kipp](https://github.com/Polished-Snow/Kipp)** — A C11 engine implements strict loading, tokenization, model execution, paged KV/prefix sharing, batching and serving behind isolated Metal and CUDA backends. **[Language models]** [Scope, sources and limits](docs/catalog.md#kipp)
- <a id="project-lightx2v"></a>**[LightX2V](https://github.com/ModelTC/LightX2V)** — Combines model-specific inference paths with quantized operators, cache policies, parallel execution and a two-slot block-loading system for overlapping offload. **[Image generation & processing / Video generation & processing / Speech & audio]** [Scope, sources and limits](docs/catalog.md#lightx2v)
- <a id="project-lily"></a>**[Lily](https://github.com/perplexityai/pplx-garden/tree/main/lily)** — A Rust runtime owns the prefill/decode graph, dispatches model-specific Metal kernels and maintains a strict token-prefix session cache. **[Language models]** [Scope, sources and limits](docs/catalog.md#lily)
- <a id="project-lithos-metal"></a>**[Lithos Metal](https://github.com/lithos-ai/lithos-metal)** — Compiles typed model graphs into layer-mixer megakernels plus conventional kernels, replayed with Metal indirect command buffers and GPU-resident speculative state. **[Language models]** [Scope, sources and limits](docs/catalog.md#lithos-metal)
- <a id="project-magnitude"></a>**[Magnitude](https://github.com/magnitudedev/magnitude)** — Its inspected Metal/MLX path captures typed operations, selects compatible kernel plans and emits specialized fused Metal entry points inside MLX native compilation. **[Language models]** [Scope, sources and limits](docs/catalog.md#magnitude)
- <a id="project-memra"></a>**[memra](https://github.com/avifenesh/memra)** — A Rust host drives embedded ahead-of-time CUDA kernels and model-specific programs, with quantized execution, KV/prefix management, speculation and multi-device placement. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#memra)
- <a id="project-metalchat"></a>**[MetalChat](https://github.com/ybubnov/metalchat)** — Builds native tensor, layer and model abstractions with Metal kernels and a command-line generation path. **[Language models]** [Scope, sources and limits](docs/catalog.md#metalchat)
- <a id="project-mflux"></a>**[MFLUX](https://github.com/mflux-community/mflux)** — Implements selected image model components natively in MLX, with on-load low-bit weight quantization and optional adapter baking into inference weights. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#mflux)
- <a id="project-minimax-h3-mlx"></a>**[MiniMax-H3 MLX](https://github.com/PipeNetwork/minimax-h3-mlx)** — Reimplements the joint pipeline in MLX, precomputes timestep-only AdaLN values and stages conditioning/DiT/VAE components while preserving packed multimodal geometry. **[Video generation & processing / Speech & audio]** [Scope, sources and limits](docs/catalog.md#minimax-h3-mlx)
- <a id="project-ninfer"></a>**[NInfer](https://github.com/Neroued/ninfer)** — Native model code composes operators; Program owns state, KV, workspace and CUDA Graph execution, while runtime manages request scheduling, cache retention and pause/resume. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#ninfer)
- <a id="project-ninfer-3090"></a>**[NInfer-3090](https://github.com/ashalliants/ninfer-3090)** — A continuation of the NInfer/Don-Chad fork supplies SM86 quantized tensor-core paths, memory and replay-state planning, low-bit KV and model-specific speculative execution. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#ninfer-3090)
- <a id="project-parakeet-axiom"></a>**[parakeet.cpp (axiom)](https://github.com/Frikallo/parakeet.cpp)** — Implements FastConformer and decoder paths plus cached streaming convolution/attention in native C++ on axiom. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#parakeet-axiom)
- <a id="project-parakeet-ggml"></a>**[parakeet.cpp (ggml)](https://github.com/mudler/parakeet.cpp)** — Ports speech feature extraction, encoder/decoder graphs and streaming sessions to C++/ggml with GGUF conversion and reference parity fixtures. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#parakeet-ggml)
- <a id="project-pmetal"></a>**[PMetal](https://github.com/Epistates/pmetal)** — Combines model architecture implementations with native inference bridges and custom device operations within a broader ML SDK. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#pmetal)
- <a id="project-qingming-qwen3-tts"></a>**[Qingming Qwen3-TTS](https://github.com/uulong950/qingming-qwen3-tts)** — Builds separate HIP/CUDA device paths with fixed hardware contracts, native operators and resident streaming generation/decoder resource partitioning. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#qingming-qwen3-tts)
- <a id="project-saient-quartz"></a>**[Quartz](https://github.com/SaientAI/saient-quartz)** — Implements its own tensor backend and image model stages, with reference-driven native Wan orchestration under development. **[Language models / Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#saient-quartz)
- <a id="project-qwen-asr-c"></a>**[Qwen-ASR (C)](https://github.com/antirez/qwen-asr)** — Owns audio preprocessing, encoder, prompt/decode state and chunked streaming in C; CPU mmap weights and optional GPU-specific loading avoid a Python model runtime. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#qwen-asr-c)
- <a id="project-qwen3-tts-c"></a>**[Qwen3-TTS (C)](https://github.com/gabriele-mastrapasqua/qwen3-tts)** — Implements talker, code predictor and speech decoder in C, with model-specific dispatch, streaming and reference-driven qualification. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#qwen3-tts-c)
- <a id="project-saragossa"></a>**[Saragossa](https://github.com/azerozero/saragossa)** — Implements Rust/Metal model paths with resident decode state, leased scratch buffers, kernel dispatch and block-prefix snapshots. **[Language models / Speech & audio]** [Scope, sources and limits](docs/catalog.md#saragossa)
- <a id="project-splash"></a>**[Splash](https://github.com/incoai/splash)** — A native runtime combines model-specific Metal kernels and matched DFlash2 drafts with its own batched execution, memory admission and KV/GDN prefix reuse; kernel agents generate specialized kernels. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#splash)
- <a id="project-stable-diffusion-cpp"></a>**[stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)** — Implements image and video diffusion in ggml-backed C/C++ with quantized weights, tiled VAE execution and architecture-gated sample-cache policies. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#stable-diffusion-cpp)
- <a id="project-stable-diffusion-rs"></a>**[stable-diffusion.rs](https://github.com/andreinknv/stable-diffusion.rs)** — Implements model and sampler logic in Rust and documents a Candle-to-MLX backend migration, preserving a narrow tensor-layer interface and golden-reference workflow. **[Image generation & processing]** [Scope, sources and limits](docs/catalog.md#stable-diffusion-rs)
- <a id="project-strix-llama-cpp"></a>**[strix-llama.cpp](https://github.com/halo-box/strix-llama.cpp)** — A community llama.cpp fork adds guarded gfx1151 matmul, MoE and Gated DeltaNet fusions, on-device speculative checkpoints, adaptive drafting and selected ROCmFPX formats. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#strix-llama-cpp)
- <a id="project-tensorfold"></a>**[TensorFold](https://github.com/ashhart/TensorFold)** — Executes a qualified set of model families from a native Zig binary using format-specific packed-weight readers and Metal/CUDA paths, fusing projections only when their packing contracts match. **[Language models]** [Scope, sources and limits](docs/catalog.md#tensorfold)
- <a id="project-tensorrt-edge-llm"></a>**[TensorRT Edge-LLM](https://github.com/NVIDIA/TensorRT-Edge-LLM)** — Exports models to ONNX, builds target-specific TensorRT engines, then runs them through C++ executors managing decoder strategies, linear KV state, sampling and vision/audio embeddings. **[Language models / Image generation & processing / Speech & audio / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#tensorrt-edge-llm)
- <a id="project-uzu"></a>**[Uzu](https://github.com/trymirai/uzu)** — Rust encodable model blocks manage decoder state and dispatch native kernels; generated bindings encode Metal function-constant specializations. **[Language models]** [Scope, sources and limits](docs/catalog.md#uzu)
- <a id="project-vidax"></a>**[Vidax](https://github.com/FlyingGiraffe/vidax)** — Ports model graphs and checkpoint layouts to JAX, explicitly composes tensor/sequence sharding, attention kernels, component placement and native video samplers. **[Video generation & processing]** [Scope, sources and limits](docs/catalog.md#vidax)
- <a id="project-vla-simd"></a>**[vla.simd](https://github.com/cair-vinuni/vla.simd)** — Rebuilds model operators, GGUF loading and action inference in C++ with architecture-specific SIMD dispatch and a separate robot-client interface. **[Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#vla-simd)
- <a id="project-vllm-radiance"></a>**[vLLM Radiance](https://github.com/magiccodingman/vllm-radiance)** — A pinned vLLM stack integrates Radiance/libr4d HIP kernels and guarded patches for attention, GDN, MXFP4 W4A8, collectives and speculative execution. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#vllm-radiance)
- <a id="project-voxgen"></a>**[VoxGen](https://github.com/NullMagic2/VoxGen)** — Reconstructs the VoxCPM2 pipeline in Rust with direct Vulkan command/memory control, selected fused shaders, reference-state caching and incremental PCM production. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#voxgen)
- <a id="project-vte"></a>**[VTE](https://github.com/kyuubyN/VTE)** — Parses GGUF, generates HIP kernels from templates, manages a VRAM slab and replays decode graphs through a ctypes HIP bridge; batched prefill and decode are explicit runtime paths. **[Language models]** [Scope, sources and limits](docs/catalog.md#vte)
- <a id="project-whisper-cpp"></a>**[whisper.cpp](https://github.com/ggml-org/whisper.cpp)** — Provides an established native Whisper/ggml runtime, with converted weights, optional quantization and platform-specific encoder acceleration. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#whisper-cpp)
- <a id="project-whisperkit"></a>**[WhisperKit](https://github.com/argmaxinc/argmax-oss-swift)** — Owns speech preprocessing, encoder/decoder orchestration, caches and segmentation around Core ML artifacts within the Argmax Swift repository. **[Speech & audio]** [Scope, sources and limits](docs/catalog.md#whisperkit)
- <a id="project-zinc"></a>**[ZINC](https://github.com/zolotukhin/zinc)** — A Zig runtime owns loading, model forward/decode graphs, KV state and serving; Vulkan and HIP/ROCm paths use native dispatch, with separate Metal and experimental CUDA backends. **[Language models]** [Scope, sources and limits](docs/catalog.md#zinc)
- <a id="project-zllm"></a>**[zLLM](https://github.com/zllm-lab/zllm)** — Rust runtimes own model loading, graph execution and state. Inspected paths implement DeepSeek vision processing, ROCm FLUX text-conditioning/denoising/VAE stages and multi-GPU SeedVR2 sequence partitioning; MiniCPM QNN uses a separately validated native runner. **[Language models / Image generation & processing / Video generation & processing / Speech & audio / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#zllm)

<a id="homepage-construction"></a>

## Engine construction and optimization

Agent harnesses, compiler workflows and model-specific optimization procedures. State whether the output is a kernel, model program or serving stack.

[Role and evidence index](docs/systems.md#construction)

<a id="homepage-construction-execution"></a>

### Compiled & native execution (5)

Fuse, lower, specialize and dispatch graphs or native kernels.

- <a id="project-anemll"></a>**[ANEMLL](https://github.com/Anemll/Anemll)** — Splits and converts model components into ANE-oriented stateful packages, with prefill variants, LUT quantization and Swift/Python orchestration. **[Language models]** [Scope, sources and limits](docs/catalog.md#anemll)
- <a id="project-mirage"></a>**[Mirage Persistent Kernel](https://github.com/mirage-project/mirage)** — Compiles an explicitly assembled LLM task graph into a persistent CUDA megakernel whose GPU workers and schedulers execute computation and communication across decoding steps. **[Language models]** [Scope, sources and limits](docs/catalog.md#mirage)
- <a id="project-mlc-llm"></a>**[MLC LLM](https://github.com/mlc-ai/mlc-llm)** — Uses a TVM LLM-specific compilation pipeline to fuse dequantization and normalization, specialize low-batch GEMV, dispatch target-specific KV kernels and execute compiled models through MLCEngine. **[Language models]** [Scope, sources and limits](docs/catalog.md#mlc-llm)
- <a id="project-onediff"></a>**[OneDiff](https://github.com/siliconflow/onediff)** — Converts diffusion-model modules into deployable compiled modules through OneFlow or Nexfort and reuses compiled graphs to reduce recurring inference overhead. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#onediff)
- <a id="project-stable-fast"></a>**[Stable Fast](https://github.com/chengzeyi/stable-fast)** — Traces Diffusers components into TorchScript, replaces common convolution/GEMM/GEGLU/normalization patterns with fused operators, and optionally captures CUDA graphs. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#stable-fast)

<a id="homepage-construction-construction"></a>

### Construction & validation tools (6)

Agents, kernel languages and evaluation infrastructure.

- <a id="project-agentcompile"></a>**[AgentCompile](https://github.com/veneno1213822/AgentCompile)** — Combines LLM-guided ranking of bounded CUDA template candidates with contract-oriented fusion-kernel generation and an inference runtime. **[Language models / Image generation & processing]** [Scope, sources and limits](docs/catalog.md#agentcompile)
- <a id="project-akg-agents"></a>**[AKG Agents](https://github.com/mindspore-ai/akg)** — Generates and migrates accelerator kernels through multi-agent workflows, using UCB-based asynchronous candidate search and backend-specific verification and profiling workers. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#akg-agents)
- <a id="project-atrex-kernel-agent"></a>**[Atrex Kernel Agent (AKA)](https://github.com/alibaba/atrex-kernel-agent)** — Runs coding episodes in isolated worktrees, evaluates numerical and performance results before promotion, and uses profiler feedback plus scoped GPU Wiki retrieval to guide further revisions. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#atrex-kernel-agent)
- <a id="project-kernelagent"></a>**[KernelAgent](https://github.com/meta-pytorch/KernelAgent)** — Decomposes PyTorch programs into fusable subgraphs, synthesizes Triton kernels, composes them back into a forward pass and iterates using correctness and hardware-profile feedback. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#kernelagent)
- <a id="project-metainfer"></a>**[MetaInfer](https://github.com/MetaInfer/MetaInfer)** — Orchestrates coding agents to iteratively build deployment-specific inference servers, then launches fixed server contracts through correctness and performance oracle phases. **[Language models]** [Scope, sources and limits](docs/catalog.md#metainfer)
- <a id="project-sol-engine"></a>**[Sol-Engine](https://github.com/NVlabs/Sana/tree/sol-engine)** — Composes model-specific video inference patches for fusion, invariant/cross-KV reuse, approximate denoising cache and sparse attention, with agent-guided configuration and visual-quality checks. **[Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#sol-engine)

<a id="homepage-validation"></a>

## Correctness and quality validation

Methods that check numerical behavior, model state, generation quality or service contracts. Embedded validators are indexed as methods without duplicating their parent project.

These methods were source-inspected, not executed here. Match checks to the change: numerical behavior, composed state, output quality and service behavior do not substitute for one another.

<a id="homepage-validation-numerical"></a>

### Operator and subgraph numerics

Compare explicit shapes, layouts, dtypes and tolerances with a reference; inspect mutation and evaluator integrity. Passing local tests does not validate a whole model.

- **[KernelBench](#project-kernelbench)** — Reference evaluation plus adversarial checks for cached answers, input mutation and alternate CUDA streams; defenses are evolving.
- **[FastKernels](#project-fastkernels)** — Checks replacement at kernel, fused-operation, layer/block and full-pipeline levels; report which integration level actually ran.
- **[Atrex-Bench](#project-atrex-bench)** — Checks output structure, numerical differences, declared mutation and side effects; coverage depends on generated inputs, shapes and tolerances.

[Implementation evidence and coverage](docs/validation.md#numerical)

<a id="homepage-validation-model-state"></a>

### Composed model and persistent state

Recheck the assembled forward path, then separately cover prefill/decode, cache ownership, resets, batching and repeated state transitions.

- **[KernelAgent composition](#project-kernelagent)** — Requests a reference self-test and can execute the candidate with --verify; verification is optional, and finite forward tests do not establish stateful service correctness.

[Implementation evidence and coverage](docs/validation.md#model-state)

<a id="homepage-validation-quality"></a>

### Generated-output quality

Evaluate the admitted approximation under a stated reference and threshold. Perceptual similarity, text accuracy and task success are different contracts.

- **[Sol-Engine LPIPS and visual review](#project-sol-engine)** — Compares sampled baseline/candidate frames and records aggregate/per-frame distances. Unequal video lengths may compare only the common prefix; unavailable scoring is not a pass, and temporal consistency is not fully covered.

[Implementation evidence and coverage](docs/validation.md#quality)

<a id="homepage-validation-service"></a>

### Service and integration behavior

Check loading, readiness, requests, responses, failures and whether the intended candidate executed. A working API does not establish reference parity or concurrency safety.

- **[MetaInfer inference-framework oracle](#project-metainfer)** — Starts serve.sh, waits for readiness and judges configured prompts through an LLM or heuristic fallback; hard checks determine acceptance. This is functional feedback, not internal-tensor equivalence.

[Implementation evidence and coverage](docs/validation.md#service)

Checking cost includes compilation, reference runs, device time, judge calls, human review and failures. Automation alone does not establish efficiency; fewer samples or looser tolerances change the acceptance contract.


<a id="homepage-benchmark"></a>

## Benchmarks and task suites

Executable workloads and comparison protocols for generated kernels and integrated inference paths.

- <a id="project-atrex-bench"></a>**[Atrex-Bench](https://github.com/alibaba/atrex-bench)** — Packages reference programs and input/shape generators, separates agent-visible tasks from evaluator metadata, and checks compilation, numerical outputs/input mutations and forward timing against a roofline estimate. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#atrex-bench)
  - **Comparison question:** Does a generated operator compile, meet numerical checks and use the target hardware effectively?
- <a id="project-fastkernels"></a>**[FastKernels](https://github.com/Snowflake-AI-Research/fastkernels)** — Replaces candidate operators in production-shaped model pipelines and evaluates both kernel-level numerics/timing and end-to-end token outputs, throughput and latency. **[Language models / Image generation & processing / Video generation & processing / Speech & audio / Multimodal understanding & interaction / Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#fastkernels)
  - **Comparison question:** Do candidate-kernel gains survive model integration?
- <a id="project-kernelbench"></a>**[KernelBench](https://github.com/ScalingIntelligence/KernelBench)** — Compiles generated kernel implementations, compares them against PyTorch reference programs on randomized inputs and times only candidates that pass correctness checks. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#kernelbench)
  - **Comparison question:** How do generated implementations compare with executable references under a stated evaluation protocol?

Match model/checkpoint, device, precision, input distribution, state, concurrency and quality criteria. Passing operator tasks does not validate a complete engine.

[Benchmark scope and comparison protocols](docs/benchmarks.md)

<a id="homepage-support"></a>

## Companion resources

Performance diagnosis, construction knowledge, and selected infrastructure with a named connection to an included engine or construction workflow.

<a id="homepage-support-diagnostics"></a>

### Performance diagnosis

Turn measured hardware behavior into actionable optimization feedback; not a correctness certificate.

- <a id="project-ncu-report-skill"></a>**[ncu-report-skill](https://github.com/mit-han-lab/ncu-report-skill)** — Provides a profiling harness, extracts and compares NCU metrics and source-level stall evidence, and maps observed signals to candidate optimization directions. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#ncu-report-skill)

[Sources and use](docs/resources.md#diagnostics)

<a id="homepage-support-knowledge"></a>

### Construction knowledge and experience

Traceable optimization knowledge and hardware experiments that can inform another construction attempt.

- <a id="project-kernelwiki"></a>**[KernelWiki](https://github.com/mit-han-lab/KernelWiki)** — Indexes upstream PRs, hardware documents and optimization notes with architecture/symptom filters, and links synthesized pages to captured kernel artifacts and provenance. **[Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#kernelwiki)
- <a id="project-ane-field-guide"></a>**[Apple Neural Engine Field Guide](https://github.com/skyfallsin/apple-neural-engine-field-guide)** — Uses small MIL/ANE probes and CPU-reference checks to investigate execution limits, records kept and discarded experiments, and transfers supported findings into ane.cpp. **[Language models]** [Scope, sources and limits](docs/catalog.md#ane-field-guide)

[Sources and use](docs/resources.md#knowledge)

<a id="homepage-support-engine-baselines"></a>

### General-engine baselines

Shared services, fork origins and comparison points for included specialized stacks.

- <a id="project-vllm"></a>**[vLLM](https://github.com/vllm-project/vllm)** — Manages attention state as pooled KV blocks with reference-counted prefix sharing and schedules token-budgeted work across requests, allocating cache slots as execution advances. **[Language models]** [Scope, sources and limits](docs/catalog.md#vllm)
- <a id="project-sglang"></a>**[SGLang](https://github.com/sgl-project/sglang)** — Indexes reusable prefix KV state in a radix tree, protects active nodes with references and offers cache-aware queue policies that prioritize requests using matched-prefix information. **[Language models]** [Scope, sources and limits](docs/catalog.md#sglang)
- <a id="project-tensorrt-llm"></a>**[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)** — Combines NVIDIA-specific LLM kernels with chunked-context scheduling, generation-aware batching and reusable paged KV-cache management. **[Language models / Multimodal understanding & interaction]** [Scope, sources and limits](docs/catalog.md#tensorrt-llm)
- <a id="project-llama-cpp"></a>**[llama.cpp](https://github.com/ggml-org/llama.cpp)** — Loads GGUF model tensors and executes a native GGML graph through backend-specific quantized kernels, dispatching by tensor type and geometry with optional CPU/GPU layer placement. **[Language models]** [Scope, sources and limits](docs/catalog.md#llama-cpp)

[Sources and use](docs/resources.md#engine-baselines)

<a id="homepage-support-compilers"></a>

### Compilers and kernel languages

Compilation dependencies and output languages of included construction workflows.

- <a id="project-tvm"></a>**[Apache TVM](https://github.com/apache/tvm)** — Coordinates Relax graph transformations and tensor-level scheduling to fuse operators, dispatch libraries and lower target-specific tensor programs into deployable modules. **[Language models / Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#tvm)
- <a id="project-tensorrt"></a>**[NVIDIA TensorRT](https://github.com/NVIDIA/TensorRT)** — Builds NVIDIA inference engines specialized to optimization-profile shapes and selected kernel tactics, recording profiled decisions in a reusable editable timing cache. **[Language models / Image generation & processing / Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#tensorrt)
- <a id="project-triton"></a>**[Triton](https://github.com/triton-lang/triton)** — Compiles block-structured kernel programs for a selected GPU target and specializes cached binaries and autotuned launch configurations to argument signatures and compile-time constants. **[Language models / Image generation & processing / Video generation & processing / Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#triton)
- <a id="project-tilelang"></a>**[TileLang](https://github.com/tile-ai/tilelang)** — Lowers tile-level kernel programs through target-specific layout and software-pipeline passes, generating GPU/accelerator code for tiled memory movement and matrix operations. **[Language models / Image generation & processing / Video generation & processing / Cross-domain infrastructure]** [Scope, sources and limits](docs/catalog.md#tilelang)

[Sources and use](docs/resources.md#compilers)

<a id="homepage-support-components"></a>

### Reusable execution and model preparation

Selected dependencies used in the engine cases; model preparation remains distinct from runtime execution.

- <a id="project-deepcompressor"></a>**[DeepCompressor](https://github.com/nunchux-ai/deepcompressor)** — Calibrates quantization and SVDQuant low-rank outlier decomposition, evaluates compressed models and exports checkpoints into runtime-specific deployment layouts. **[Language models / Image generation & processing]** [Scope, sources and limits](docs/catalog.md#deepcompressor)
- <a id="project-qtip"></a>**[QTIP](https://github.com/Cornell-RelaxML/qtip)** — Quantizes incoherence-transformed weights with bitshift trellis codes and executes supported low-bit encodings through matching BitshiftLinear matrix-vector kernels. **[Language models]** [Scope, sources and limits](docs/catalog.md#qtip)
- <a id="project-marlin"></a>**[Marlin](https://github.com/IST-DASLab/marlin)** — Repacks INT4 weights/scales offline and overlaps asynchronous loads, dequantization and tensor-core MMA in a shape-specialized FP16×INT4 CUDA kernel. **[Language models]** [Scope, sources and limits](docs/catalog.md#marlin)
- <a id="project-flash-linear-attention"></a>**[Flash Linear Attention](https://github.com/fla-org/flash-linear-attention)** — Implements architecture-specific linear-attention and recurrent mixers with chunk-parallel prefill and state-update kernels, including fused gated-delta-rule intra-chunk computation. **[Language models]** [Scope, sources and limits](docs/catalog.md#flash-linear-attention)
- <a id="project-flash-attention"></a>**[FlashAttention](https://github.com/Dao-AILab/flash-attention)** — Implements attention with IO-aware tiled kernels and fused reductions, selecting hardware/shape-specific variants and providing KV-cache update-and-attend inference interfaces. **[Language models]** [Scope, sources and limits](docs/catalog.md#flash-attention)
- <a id="project-sageattention"></a>**[SageAttention](https://github.com/thu-ml/SageAttention)** — Applies outlier smoothing and hardware-specific low-precision QK and PV attention kernels, dispatching among INT8/FP8 or newer architecture-specific variants. **[Language models / Image generation & processing / Video generation & processing]** [Scope, sources and limits](docs/catalog.md#sageattention)
- <a id="project-flashinfer"></a>**[FlashInfer](https://github.com/flashinfer-ai/flashinfer)** — Builds or selects attention/GEMM/MoE kernels from dtype, head geometry, cache layout and workload metadata, with planned paged/ragged KV execution and specialized prefill/decode paths. **[Language models]** [Scope, sources and limits](docs/catalog.md#flashinfer)

[Sources and use](docs/resources.md#components)

**Embedded construction knowledge:** Atrex GPU Wiki turns optimization traces and agent sessions into candidate knowledge, checks provenance/scope and retrieves it in later attempts. It remains part of Atrex, not a second project; the workflow alone does not establish reduced total development cost. [Process details](docs/resources.md#embedded-knowledge).

<a id="featured-reading"></a>

## Selected reading and comparison

These reading choices supplement the complete list above. They contrast execution control, reuse, construction and validation; they are not a star, speed or maturity ranking.

| Case | Read it to understand |
| --- | --- |
| [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) | Connect an agent workflow to a reported deployed engine |
| [Sol-Engine](docs/cases.md#sol-engine) | See how optimization choices are accepted and composed |
| [Mirage MPK](docs/cases.md#mirage) | Follow an explicit task graph into persistent GPU execution |
| [Splash](docs/cases.md#splash) | Inspect model-shaped kernels, draft execution and serving together |
| [Gufo](docs/cases.md#gufo) | Study a device-focused stack with explicit per-model quality limits |
| [Flash-MoE](docs/cases.md#flash-moe) | Separate SSD streaming from changes to the model computation |
| [llamAmpere](docs/cases.md#llamampere) | See what a deep fork changes and what upstream still supplies |
| [Nunchaku](docs/cases.md#nunchaku) | Trace packed checkpoints into fused diffusion execution |
| [LightX2V](docs/cases.md#lightx2v) | Inspect explicit asynchronous weight-storage contracts |
| [Vidax](docs/cases.md#vidax) | Follow model conversion and numerical debugging across devices |
| [Aria](docs/cases.md#aria) | Read an AI disclosure beside an inspectable parity harness |
| [vla.simd](docs/cases.md#vla-simd) | Distinguish native action inference from robot task success |

[12-case matrix: model/device, artifact, reuse and checks](docs/representative-comparison.md) · [Full comparison](docs/comparison.md) · [All cases](docs/cases.md) · [Cross-case synthesis](docs/synthesis.md)

Model domains are visible on every project above. Supplementary cross-category domain indices:

[Multimodal understanding & interaction](docs/domains.md#multimodal) · [Image generation & processing](docs/domains.md#image) · [Video generation & processing](docs/domains.md#video) · [Speech & audio](docs/domains.md#audio) · [Language models](docs/domains.md#text) · [Cross-domain infrastructure](docs/domains.md#general)

<!-- CATALOG-END -->

## What belongs here?

A record needs a direct, documented relationship to **building or validating a specialized execution stack**: substantive engines/backends, construction workflows, validation, benchmarks or concrete supporting resources. General engines and libraries need a reuse or comparison relationship; a thin wrapper, generic optimization or teaching-only nano reproduction is insufficient. [Inclusion rules and taxonomy](docs/taxonomy.md).

## Read the evidence

Ask **why another execution path → what it controls → what it reuses or gives up → how it was built → how it is validated and maintained**. A kernel, model forward program and complete service are different artifacts. [Full case notes](docs/cases.md) retain construction, AI participation, cost, validation and maintenance evidence.

This collection reviews public sources; it has not independently reproduced project performance. AI participation requires direct disclosure or an inspectable workflow. Reported speedups and agent use alone do not establish lower lifecycle cost. Keep runtime changes separate from quantization, approximations and changed models. [Evidence policy](docs/evidence-policy.md) · [Research questions](docs/research-agenda.md) · [Resource audit](docs/resources-audit-2026-10-12.md).

<details>
<summary>Visual map of the collection</summary>

![Engines, construction workflows and validation methods; benchmarks and companion resources support their comparison](assets/specialization.svg)

</details>

[Contribute or correct a record](CONTRIBUTING.md). Directories are generated from [projects](catalog/projects.csv), [cases](catalog/cases.json), [Chinese entry descriptions](catalog/homepage_cn.json) and [reading selections](catalog/showcase.json). Metadata, original diagrams, commentary and scripts use [MIT](LICENSE); linked projects and models retain their own licenses.
