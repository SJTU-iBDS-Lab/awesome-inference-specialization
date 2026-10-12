# Core cases: how execution stacks are built / 核心案例

> Generated from [cases.json](../catalog/cases.json). Cases connect construction processes to artifacts; they are not additional repository counts.

[Home](../README.md) · [中文首页](../README_CN.md) · [Survey library](systems.md) · [Construction comparison](comparison.md) · [Evidence policy](evidence-policy.md)

Read motivation → execution ownership → retained components and lost generality → construction → validation and maintenance. A case can be selected without AI attribution. Rebuilding an execution path need not mean writing every dependency from scratch.

本页关注“为何重构、重构了多少、怎样构建、是否值得维护”。未知项明确保留；作者披露、源码检查、独立复现和生产使用是不同证据。案例资格不等于证明 AI 降低了总成本。

No case performance was independently reproduced here. “Not disclosed” and “not established” describe the reviewed sources, not an assertion that an activity never occurred.

[VibeQwen: from MetaInfer workflow to a serving stack](#vibeqwen) · [Sol-Engine: compose and qualify model-specific optimizations](#sol-engine) · [Flash-MoE: SSD-streamed experts in a native prototype](#flash-moe) · [DwarfStar: a deliberately narrow native execution stack](#dwarfstar) · [Strata: tier experts around a gaming PC](#strata) · [Iris: own the image pipeline in C](#iris) · [TensorFold: qualify native paths by checkpoint and platform](#tensorfold) · [Halogen Flash: specialize a closed binary to one chip](#halogen-flash) · [Magnitude: specialize kernels inside MLX execution](#magnitude) · [KTransformers: integrate CPU expert execution with GPU serving](#ktransformers) · [Nunchaku: build execution around an SVDQuant artifact](#nunchaku) · [ExLlamaV3: couple low-bit artifacts to a dedicated library](#exllamav3) · [Mirage MPK: compile an explicit graph into persistent execution](#mirage)

<a id="vibeqwen"></a>

## VibeQwen: from MetaInfer workflow to a serving stack

**Related project records:** [MetaInfer](catalog.md#metainfer).

- **Why build it? / 为什么另建:** Target lower latency than a general engine for Qwen-3.6-35B-A3B NVFP4 on one B200.
- **Execution ownership / 重构边界:** Model execution and serving integration, evaluated as deployed services; public VibeQwen engine source was not established.
- **Retained components / 复用什么:** vLLM/TensorRT-LLM kernels and references; MetaInfer is the adapted workflow, not VibeQwen source.
- **Scope given up / 取舍与兼容性:** NVFP4 numerical differences were accepted if accuracy against BF16 was at least as good.
- **Construction process / 怎样构建:** Agent build/deploy/profile iterations: about one week, 1.7B mostly cached tokens and approximately 200 B200-hours.
- **AI participation / AI 参与的直接证据:** Disclosed: Claude Code with human steering, deployment access and measurement tools.
- **Disclosed effort / 构建投入:** Resource usage reported; fee estimates do not establish total development cost.
- **Validation boundary / 验证覆盖:** Author-reported performance and accuracy checks; experimental, not production. No independent reproduction here.
- **Evolution evidence / 适配与维护:** Long-term compatibility, regression coverage and maintenance effort were not established by the report.

**Sources:** [Source 1](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/) · [Source 2](https://github.com/MetaInfer/MetaInfer/blob/HEAD/README.md) · [Source 3](https://github.com/MetaInfer/MetaInfer/blob/HEAD/metainfer/tasks/gen_infer_framework/orchestrator/pipeline.py).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="sol-engine"></a>

## Sol-Engine: compose and qualify model-specific optimizations

**Related project records:** [Sol-Engine](catalog.md#sol-engine).

- **Why build it? / 为什么另建:** The README identifies denoising-step redundancy, sparse interactions and repeated memory-bound operations as optimization opportunities.
- **Execution ownership / 重构边界:** The reviewed artifact is an optimized video codebase and configuration workflow, not a replacement for every serving layer.
- **Retained components / 复用什么:** Builds on SGLang multimodal_gen and existing model pipelines; combines cache, quantization, fusion, sparse attention and pruning.
- **Scope given up / 取舍与兼容性:** Cache, sparsity and precision choices can change outputs; their effects must be separated from exact implementation changes.
- **Construction process / 怎样构建:** Documented workflow: executors explore configurations; an orchestrator checks, deduplicates and integrates results into reproducible run bundles.
- **AI participation / AI 参与的直接证据:** Intrinsic: the documented onboarding and optimization workflow uses coding agents; authored kernels remain reusable components.
- **Disclosed effort / 构建投入:** Total development tokens, GPU-hours and human maintenance costs are not disclosed in reviewed sources.
- **Validation boundary / 验证覆盖:** Documented gates include LPIPS, visual review and checks that optimizations actually engaged; these are not equivalence proofs.
- **Evolution evidence / 适配与维护:** Per-model hooks and backend combinations need qualification; long-term maintenance effort is not established.

**Sources:** [Source 1](https://github.com/NVlabs/Sana/blob/sol-engine/README.md) · [Source 2](https://github.com/NVlabs/Sana/blob/sol-engine/models/wan22_ti2v_5b/optimized/wan_kernel_runtime.py) · [Source 3](https://github.com/NVlabs/Sana/blob/sol-engine/models/wan22_ti2v_5b/optimized/cache_runtime.py) · [Source 4](https://github.com/NVlabs/Sana/blob/sol-engine/tools/vision/lpips_judge.py) · [Source 5](https://github.com/NVlabs/Sana/blob/sol-engine/techniques/sparse_backends/sol_attn/interface.py) · [Source 6](https://github.com/NVlabs/Sana/blob/sol-engine/site_docs/agent-workflow.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="flash-moe"></a>

## Flash-MoE: SSD-streamed experts in a native prototype

**Related project records:** [Flash-MoE](catalog.md#flash-moe).

- **Why build it? / 为什么另建:** The stated target is running Qwen3.5-397B-A17B on a 48 GB MacBook despite weights exceeding RAM.
- **Execution ownership / 重构边界:** Owns model inference, routing, I/O and Metal execution; this is a narrow research prototype rather than a generic loader.
- **Retained components / 复用什么:** Uses Apple Metal, Accelerate BLAS, dispatch groups and the operating-system page cache alongside pretrained model weights.
- **Scope given up / 取舍与兼容性:** The executable uses four experts although its source identifies ten active experts in the model; quantization adds another change.
- **Construction process / 怎样构建:** The author reports human–AI prototype construction; C/Metal sources expose the result. Detailed task division and iteration history are not established.
- **AI participation / AI 参与的直接证据:** Disclosed: the project describes a human-and-AI build. That statement does not establish autonomous correctness.
- **Disclosed effort / 构建投入:** The README reports a 24-hour human–AI prototype build; total lifecycle expenditure is not disclosed.
- **Validation boundary / 验证覆盖:** The K=4 source and reported 2-bit JSON failures prevent treating headline speed as an equivalent top-10 baseline.
- **Evolution evidence / 适配与维护:** Model geometry and packed files are specific; broader compatibility and sustained maintenance are not established.

**Sources:** [Source 1](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/README.md) · [Source 2](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/CLAUDE.md) · [Source 3](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/metal_infer/infer.m) · [Source 4](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/metal_infer/shaders.metal).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="dwarfstar"></a>

## DwarfStar: a deliberately narrow native execution stack

**Related project records:** [DwarfStar](catalog.md#dwarfstar).

- **Why build it? / 为什么另建:** The author explicitly cites capable local models, expert quantization, compressed KV and fast SSDs as reasons for specialization.
- **Execution ownership / 重构边界:** Owns a narrow inference path plus CLI/server integration; it deliberately does not accept arbitrary GGUF models.
- **Retained components / 复用什么:** Its ds4.c inference path does not link GGML, but credits llama.cpp/GGML and retains or adapts quantization layouts, CPU logic and kernels.
- **Scope given up / 取舍与兼容性:** Capacity depends on resident state, expert precision and SSD traffic; model coverage is intentionally selective.
- **Construction process / 怎样构建:** Public artifacts show native model paths and adapted lower-level code; the author describes humans guiding agent-assisted implementation, testing and debugging.
- **AI participation / AI 参与的直接证据:** Disclosed: strong coding-agent assistance, with humans leading ideas, testing and debugging.
- **Disclosed effort / 构建投入:** Total construction time, token usage and engineering expenditure are not disclosed in reviewed sources.
- **Validation boundary / 验证覆盖:** The repository describes release QA and integrated tests; this survey did not reproduce its performance or numerical results.
- **Evolution evidence / 适配与维护:** The author calls it beta and rapidly changing; supported models may be replaced as the project evolves.

**Sources:** [Source 1](https://github.com/antirez/ds4/blob/HEAD/README.md) · [Source 2](https://github.com/antirez/ds4/blob/HEAD/docs/SSD_STREAMING.md) · [Source 3](https://github.com/antirez/ds4/blob/HEAD/metal/moe.metal).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="strata"></a>

## Strata: tier experts around a gaming PC

**Related project records:** [Strata](catalog.md#strata).

- **Why build it? / 为什么另建:** The stated goal is local Qwen3.8-Flash-Next inference on consumer NVIDIA or AMD PCs rather than server-sized GPU memory.
- **Execution ownership / 重构边界:** Integrates inference, memory policy and local APIs around one model family and qualified quantized layouts.
- **Retained components / 复用什么:** Credits GGML quantization formats, GPU dot/dequantization code, CPU expert kernels and the mtmd vision helper.
- **Scope given up / 取舍与兼容性:** Eligible configurations enable route-tail-skip by default, dropping some missed experts; residency and CPU/GPU rounding also affect outputs.
- **Construction process / 怎样构建:** Public artifacts show a C++ runtime with CUDA/HIP and GGML-derived components. Development tools, task division and iteration history are not disclosed.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources. Compatibility with coding-agent clients is not evidence of AI-authored implementation.
- **Disclosed effort / 构建投入:** Development time, token expenditure and controlled construction-cost comparisons are not disclosed.
- **Validation boundary / 验证覆盖:** Documented benchmark scenarios and source inspection expose configuration differences; no independent performance or quality reproduction was run.
- **Evolution evidence / 适配与维护:** Device, quantization and skip-policy combinations require version-specific checks; maintenance effort is not disclosed.

**Sources:** [Source 1](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/README.md) · [Source 2](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/docs/DETAILS.md) · [Source 3](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/src/core/expert_cache.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="iris"></a>

## Iris: own the image pipeline in C

**Related project records:** [Iris](catalog.md#iris).

- **Why build it? / 为什么另建:** The README emphasizes minimal runtime dependencies and memory-mapped execution on machines with limited RAM.
- **Execution ownership / 重构边界:** Implements text encoding, diffusion-transformer execution and image decoding for selected FLUX and Z-Image variants.
- **Retained components / 复用什么:** Consumes existing model weights and safetensors; accelerated paths use system Metal/MPS and optional BLAS.
- **Scope given up / 取舍与兼容性:** Native implementation narrows dependencies, but CPU fallbacks and different model variants do not have identical performance or quality.
- **Construction process / 怎样构建:** Public artifacts show architecture-specific C implementation and platform backends. Sources describe C/Python reference debugging, but not the full development sequence or task division.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources; disclosure from the author’s other projects must not be transferred to Iris.
- **Disclosed effort / 构建投入:** Construction time, AI-token spending and maintenance economics are not disclosed in reviewed sources.
- **Validation boundary / 验证覆盖:** The repository describes reference-image checks and C/Python debugging comparisons; performance and output claims were not independently reproduced.
- **Evolution evidence / 适配与维护:** New architectures need implementation and reference checks; the reviewed sources do not quantify that continuing effort.

**Sources:** [Source 1](https://github.com/antirez/iris.c/blob/main/README.md) · [Source 2](https://github.com/antirez/iris.c/blob/main/iris_safetensors.c) · [Source 3](https://github.com/antirez/iris.c/blob/main/iris_transformer_flux.c).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="tensorfold"></a>

## TensorFold: qualify native paths by checkpoint and platform

**Related project records:** [TensorFold](catalog.md#tensorfold).

- **Why build it? / 为什么另建:** Documented objective: serve qualified language-model checkpoints directly from a binary without a Python or MLX serving installation.
- **Execution ownership / 重构边界:** Owns loading, tokenization, serving and execution for admitted combinations; experimental Living Weights is a separate model-changing feature.
- **Retained components / 复用什么:** Reuses existing model checkpoints, quantization encodings and platform GPU runtimes; reading an MLX format does not mean running MLX.
- **Scope given up / 取舍与兼容性:** Packed formats and backend capabilities constrain fusion; a supported model name alone does not qualify every checkpoint.
- **Construction process / 怎样构建:** Public artifacts show native Zig model paths and format-aware readers. The authoring workflow and division of implementation work are not disclosed.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources; native code or compact packaging does not identify its authorship process.
- **Disclosed effort / 构建投入:** Development time, token/GPU expenditure and long-term engineering costs are not disclosed.
- **Validation boundary / 验证覆盖:** The README provides qualification tables, golden-test commands and cache-state checks; this survey did not rerun them.
- **Evolution evidence / 适配与维护:** Qualification is versioned and hardware-specific; adding readers or platforms creates additional compatibility obligations.

**Sources:** [Source 1](https://github.com/ashhart/TensorFold/blob/HEAD/README.md) · [Source 2](https://github.com/ashhart/TensorFold/blob/HEAD/docs/quantization.md) · [Source 3](https://github.com/ashhart/TensorFold/blob/HEAD/zig/src/families/nemotron/forward.zig).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="halogen-flash"></a>

## Halogen Flash: specialize a closed binary to one chip

**Related project records:** [Halogen Flash](catalog.md#halogen-flash).

- **Why build it? / 为什么另建:** The README explicitly trades portability for model-and-chip specialization, targeting long local coding-agent sessions.
- **Execution ownership / 重构边界:** Public material exposes deployment and behavior; the core engine and complete tensor-level quantization choices are not publicly inspectable.
- **Retained components / 复用什么:** Uses pretrained weights and accepts selected llama.cpp GGUF files; underlying implementation reuse is not established by public documentation.
- **Scope given up / 取舍与兼容性:** Mixed precision and narrow hardware support shape the result; repeatable binary benchmarks cannot substitute for source-level inspection.
- **Construction process / 怎样构建:** Documentation describes dedicated attention/expert kernels, separate state budgets and a paged n-gram lookup table.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources; serving agents does not establish that agents built the engine.
- **Disclosed effort / 构建投入:** Development time, token usage and engineering costs are not disclosed in reviewed sources.
- **Validation boundary / 验证覆盖:** The publisher provides verification and benchmark modes; their numerical guarantees and performance were not independently reproduced here.
- **Evolution evidence / 适配与维护:** Compatibility follows binary releases and supported hardware; maintenance effort and reproducible source builds are not established.

**Sources:** [Source 1](https://github.com/peonist-ai/halogen-flash-server/blob/HEAD/README.md) · [Source 2](https://github.com/peonist-ai/halogen-flash-server/blob/HEAD/docs/QUANT.md) · [Source 3](https://github.com/peonist-ai/halogen-flash-server/blob/HEAD/LICENSE.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="magnitude"></a>

## Magnitude: specialize kernels inside MLX execution

**Related project records:** [Magnitude](catalog.md#magnitude).

- **Why build it? / 为什么另建:** The README presents local, hardware-specific compilation and tuning for agent inference; historical framework bottlenecks are not established.
- **Execution ownership / 重构边界:** The inspected kernel layer owns planning and generated entry points, not a second device runtime or independent scheduler.
- **Retained components / 复用什么:** Retains MLX arrays, tracing, compilation and dependency management, combining upstream primitives with handwritten Metal implementations.
- **Scope given up / 取舍与兼容性:** Encodings, shapes and numerical contracts restrict legal composition; unfamiliar operations and shapeless compilation retain upstream behavior.
- **Construction process / 怎样构建:** Capture operations, select compatible implementations, emit Metal entry points, then reconnect the transformed graph to native MLX compilation.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources; an engine for agents is not automatically an agent-generated engine.
- **Disclosed effort / 构建投入:** Total development effort and amortization of device-specific tuning are not disclosed in reviewed sources.
- **Validation boundary / 验证覆盖:** Design documents define qualification obligations; inspecting compiler code does not prove every handwritten kernel satisfies them.
- **Evolution evidence / 适配与维护:** The evidence covers inference-v2 Metal/MLX; other backends and continuing qualification costs remain outside this audit.

**Sources:** [Source 1](https://github.com/magnitudedev/magnitude/blob/HEAD/README.md) · [Source 2](https://github.com/magnitudedev/magnitude/blob/HEAD/inference-v2/design/kernels.md) · [Source 3](https://github.com/magnitudedev/magnitude/blob/HEAD/inference-v2/src/magnitude_engine/kernels/core/compiler.py).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="ktransformers"></a>

## KTransformers: integrate CPU expert execution with GPU serving

**Related project records:** [KTransformers / kt-kernel](catalog.md#ktransformers).

- **Why build it? / 为什么另建:** The documented use case is large MoE inference with limited GPU resources and substantial CPU memory.
- **Execution ownership / 重构边界:** The reviewed kt-kernel path is an integrated backend; it is distinct from legacy injection examples and separate training features.
- **Retained components / 复用什么:** Reuses GPU serving integrations, model formats and libraries including a llamafile-based CPU backend, alongside AMX/AVX-specific implementations.
- **Scope given up / 取舍与兼容性:** The useful partition depends on CPU ISA, NUMA placement, precision and communication costs; CPU capacity alone does not guarantee speed.
- **Construction process / 怎样构建:** The project documents kt-kernel implementations and serving integration. Its development iterations and division of work between people and tools are not established.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources. Supporting agent workloads does not disclose an AI development process.
- **Disclosed effort / 构建投入:** Hardware configurations are documented; controlled construction-time and maintenance-cost accounting is not disclosed.
- **Validation boundary / 验证覆盖:** README support matrices and an AMX MoE implementation were inspected; benchmark and correctness claims were not independently reproduced.
- **Evolution evidence / 适配与维护:** Kernel variants, weight formats and serving integrations evolve separately and require compatible versions.

**Sources:** [Source 1](https://github.com/kvcache-ai/ktransformers/blob/HEAD/README.md) · [Source 2](https://github.com/kvcache-ai/ktransformers/blob/HEAD/kt-kernel/README.md) · [Source 3](https://github.com/kvcache-ai/ktransformers/blob/HEAD/kt-kernel/operators/amx/moe.hpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="nunchaku"></a>

## Nunchaku: build execution around an SVDQuant artifact

**Related project records:** [Nunchaku](catalog.md#nunchaku).

- **Why build it? / 为什么另建:** The documented problem is that an otherwise useful low-rank branch adds activation reads and writes that erode quantization gains.
- **Execution ownership / 重构边界:** Implements specialized diffusion-model execution components and integrations; it does not replace all text encoding, decoding or application layers.
- **Retained components / 复用什么:** Uses DeepCompressor-prepared checkpoints and existing PyTorch/Diffusers integrations; low-bit and low-rank CUDA kernels supply the specialized path.
- **Scope given up / 取舍与兼容性:** Quantization changes numerical computation; reduced offloading, optional caching and checkpoint changes must be separated from kernel-level benefits.
- **Construction process / 怎样构建:** Source exposes custom CUDA operations through Python model adapters. The development chronology and division of automated and human work are not established.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources; model quantization and automatic kernels do not imply coding-agent authorship.
- **Disclosed effort / 构建投入:** Calibration and conversion are preparation work; developer effort and total construction economics are not disclosed.
- **Validation boundary / 验证覆盖:** Public examples, quality results and kernels support inspection, but this survey did not independently reproduce image quality or speed.
- **Evolution evidence / 适配与维护:** Support depends on checkpoint format, model adapters and CUDA/PyTorch compatibility; maintenance effort is not quantified.

**Sources:** [Source 1](https://github.com/nunchux-ai/nunchaku/blob/main/README.md) · [Source 2](https://github.com/nunchux-ai/nunchaku/blob/main/nunchaku/models/linear.py) · [Source 3](https://github.com/nunchux-ai/nunchaku/blob/main/src/kernels/zgemm/gemm_w4a4.cu).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="exllamav3"></a>

## ExLlamaV3: couple low-bit artifacts to a dedicated library

**Related project records:** [ExLlamaV3](catalog.md#exllamav3).

- **Why build it? / 为什么另建:** The README targets flexible quantization, parallel inference and large models with limited consumer-GPU resources.
- **Execution ownership / 重构边界:** Provides model execution and generation machinery; the recommended OpenAI-compatible server is the separate TabbyAPI project.
- **Retained components / 复用什么:** EXL3 builds on QTIP; the project uses PyTorch and credits FlashAttention, Marlin and vendored Flash Linear Attention kernels.
- **Scope given up / 取舍与兼容性:** Weight/KV precision, model layout and decode geometry constrain optimized paths; quantized results are not the full-precision reference.
- **Construction process / 怎样构建:** Public artifacts provide a dedicated inference library and conversion tools. The development workflow is not disclosed; weight conversion is deployment preparation, not engine authorship evidence.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources. Automated conversion and dispatch do not identify the software’s development process.
- **Disclosed effort / 构建投入:** The README reports conversion in minutes to hours on a high-end consumer GPU, depending on model size; total engineering costs are unknown.
- **Validation boundary / 验证覆盖:** Optimization documentation and quantized-cache code were inspected; conversion quality and end-to-end speed were not independently reproduced.
- **Evolution evidence / 适配与维护:** Model support, kernel eligibility and PyTorch/CUDA/Triton versions create separate compatibility obligations.

**Sources:** [Source 1](https://github.com/turboderp-org/exllamav3/blob/HEAD/README.md) · [Source 2](https://github.com/turboderp-org/exllamav3/blob/HEAD/doc/optimize.md) · [Source 3](https://github.com/turboderp-org/exllamav3/blob/HEAD/exllamav3/cache/quant.py).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="mirage"></a>

## Mirage MPK: compile an explicit graph into persistent execution

**Related project records:** [Mirage Persistent Kernel](catalog.md#mirage).

- **Why build it? / 为什么另建:** The documented objective is reducing inference latency by moving model-wide execution into a single persistent megakernel.
- **Execution ownership / 重构边界:** This case covers the MPK branch and its supported task graph, not automatic support for arbitrary Hugging Face models.
- **Retained components / 复用什么:** Attaches existing PyTorch tensors, uses CUDA and NVSHMEM resources, and assembles supported fused operations rather than inventing model weights.
- **Scope given up / 取舍与兼容性:** Graph coverage, tensor geometry and worker/scheduler allocation constrain generated programs; hardware resources must be budgeted explicitly.
- **Construction process / 怎样构建:** Define inputs, outputs and fused tasks, configure GPU workers, compile the graph and execute the resulting persistent program.
- **AI participation / AI 参与的直接证据:** Not established in reviewed sources; compiler automation is not itself evidence of coding-agent participation.
- **Disclosed effort / 构建投入:** End-to-end construction, tuning and maintenance costs are not disclosed in reviewed sources.
- **Validation boundary / 验证覆盖:** Public demos and profiling interfaces expose execution; this survey inspected compiler/runtime boundaries without reproducing reported speedups.
- **Evolution evidence / 适配与维护:** New models require supported task implementations and graph assembly; hardware changes require configuration and compatibility checks.

**Sources:** [Source 1](https://github.com/mirage-project/mirage/blob/mpk/README.md) · [Source 2](https://github.com/mirage-project/mirage/blob/mpk/python/mirage/mpk/persistent_kernel.py) · [Source 3](https://github.com/mirage-project/mirage/blob/mpk/include/mirage/persistent_kernel/persistent_kernel.cuh).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

