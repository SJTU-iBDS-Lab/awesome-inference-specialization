# Core cases: how execution stacks are built / 核心案例

> Generated from [cases.json](../catalog/cases.json). Cases connect construction processes to artifacts; they are not additional repository counts.

[Home](../README.md) · [中文首页](../README_CN.md) · [Survey library](systems.md) · [Construction comparison](comparison.md) · [Evidence policy](evidence-policy.md)

Read motivation → execution ownership → retained components and lost generality → construction → validation and maintenance. A case can be selected without AI attribution. Rebuilding an execution path need not mean writing every dependency from scratch.

本页关注“为何重构、重构了多少、怎样构建、是否值得维护”。未知项明确保留；作者披露、源码检查、独立复现和生产使用是不同证据。案例资格不等于证明 AI 降低了总成本。

No case performance was independently reproduced here. “Not disclosed” and “not established” describe the reviewed sources, not an assertion that an activity never occurred.

The complete reading routes below expand the homepage selections. / 以下阅读路线展开首页精选，覆盖全部构建案例。

### Construction workflows and generated execution / 构建流程与生成的执行程序

[MetaInfer → VibeQwen](#vibeqwen) · [Sol-Engine](#sol-engine) · [Mirage MPK](#mirage) · [Lithos Metal](#lithos-metal) · [Magnitude](#magnitude) · [SEIS](#seis) · [VibeServe / VibeSys](#vibeserve) · [AutoMegaKernel](#automegakernel)

### Native runtimes for qualified models and devices / 围绕指定模型与设备重建原生运行时

[Splash](#splash) · [Gufo](#gufo) · [zLLM](#zllm) · [NInfer](#ninfer) · [Lily](#lily) · [hipEngine](#hipengine) · [imp](#imp) · [VTE](#vte) · [ZINC](#zinc) · [memra](#memra) · [Kipp](#kipp) · [Saragossa](#saragossa) · [TensorFold](#tensorfold) · [Halogen Flash](#halogen-flash) · [ExLlamaV3](#exllamav3) · [Llaminar](#llaminar) · [ane.cpp](#ane-cpp) · [Cactus](#cactus) · [FastFlowLM](#fastflowlm) · [Cloudflare Infire](#infire) · [Kog Inference Engine](#kie)

### Rebuilding around memory and expert placement / 围绕内存与专家驻留重建执行

[Flash-MoE](#flash-moe) · [Strata](#strata) · [Swiftlet](#swiftlet) · [DwarfStar](#dwarfstar) · [TurboFieldfare](#turbo-fieldfare) · [TUFF](#tuff) · [SwiftLM](#swiftlm) · [Colibri](#colibri) · [KTransformers](#ktransformers)

### Substantial forks and specialized backends / 通过深度分叉与专用后端改变执行

[llamAmpere](#llamampere) · [vLLM Radiance](#vllm-radiance) · [ANEMLL Flash llama.cpp](#anemll-flash-llama) · [NInfer-3090](#ninfer-3090) · [Infernix](#infernix) · [CIRU runtime](#ciru-runtime) · [Gufo RDMA](#gufo-rdma) · [strix-llama.cpp](#strix-llama-cpp)

### Reconstructing image-generation pipelines / 重建图像生成流水线

[Iris](#iris) · [stable-diffusion.cpp](#stable-diffusion-cpp) · [Nunchaku](#nunchaku) · [edge-dit.cpp](#edge-dit) · [Hearth](#hearth) · [brodiffusion](#brodiffusion) · [stable-diffusion.rs](#stable-diffusion-rs) · [Quartz](#saient-quartz)

### Video execution, device migration and streaming / 视频执行、设备移植与连续生成

[LightX2V](#lightx2v) · [Vidax](#vidax) · [TeleFuser](#telefuser) · [FastVideo](#fastvideo) · [MiniMax-H3 MLX](#minimax-h3-mlx) · [StreamDiffusionV2](#streamdiffusion-v2)

### Speech, audio diffusion and action-model runtimes / 语音、音频扩散与动作模型运行时

[Aria](#aria) · [Qwen-ASR](#qwen-asr-c) · [vla.simd](#vla-simd) · [Qwen3-TTS](#qwen3-tts-c) · [Qingming Qwen3-TTS](#qingming-qwen3-tts) · [VoxGen](#voxgen) · [parakeet.cpp (ggml)](#parakeet-ggml) · [parakeet.cpp (axiom)](#parakeet-axiom)

<a id="vibeqwen"></a>

## MetaInfer → VibeQwen: from construction workflow to serving stack

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

<a id="lithos-metal"></a>

## Lithos Metal: compiled mixer programs and GPU-resident control

**Related project records:** [Lithos Metal](catalog.md#lithos-metal).

- **Why build it? / 为什么另建:** Avoid repeated dispatch and intermediate traffic while retaining enough GPU parallelism for local Qwen inference.
- **Execution ownership / 重构边界:** Owns typed IR, fusion, memory planning, kernel emission, program ABI and generation-state replay.
- **Retained components / 复用什么:** Uses Metal and checkpoint formats; Mirage inspires the task model but is not a runtime dependency.
- **Scope given up / 取舍与兼容性:** Fusion is layer-local and recipe-dependent. Normalization fusion may alter rounding; unmeasured chips use conservative fallbacks.
- **Construction process / 怎样构建:** Model packages lower into registered operations; chip recipes select layouts and task schedules before native pipeline compilation. Extension contracts specify qualification gates.
- **AI participation / AI 参与的直接证据:** Not established by the inspected sources; runtime use by coding agents is not authorship evidence.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Contract, kernel, layer and model-oracle tiers exist. Published target-compute projections must not be read as end-to-end throughput.
- **Evolution evidence / 适配与维护:** New models and devices need adapter/recipe qualification; the documented extension workflow does not quantify long-term maintenance effort.

**Sources:** [Source 1](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/README.md) · [Source 2](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/docs/design/design.md) · [Source 3](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/docs/design/extensions.md) · [Source 4](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/monolith/runtime/engine.py) · [Source 5](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/CONTRIBUTING.md).

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

<a id="seis"></a>

## SEIS: sustained evolution of an existing inference engine

**Related project records:** [SEIS: Self-Evolving Inference Systems](catalog.md#seis).

- **Why build it? / 为什么另建:** Study whether accumulated agent work can improve an entire inference system rather than isolated kernels or independent one-shot attempts.
- **Execution ownership / 重构边界:** Starts from mini-sglang, not an empty implementation. The inspected trial-10 engine installs quantized weights and uses graph-captured greedy selection; the paper additionally describes prompt-lookup verification and coordinated KV/runtime changes.
- **Retained components / 复用什么:** Retains mini-sglang infrastructure, pretrained checkpoints, PyTorch/CUDA and existing attention facilities where used. The coding agent itself is not trained or evolved.
- **Scope given up / 取舍与兼容性:** The principal paper setting is a small model, one H100 and single-request greedy inference. Low-bit execution is not the original numerical computation; results are not a general multi-model or concurrent-serving comparison.
- **Construction process / 怎样构建:** Paper: independent sessions, sequential inheritance and synchronized chains. Public scaffold: a shell loop launches ten fresh coding sessions and keeps their logs; written instructions and learning notes guide subsequent work. These are related but distinct levels of disclosed implementation.
- **AI participation / AI 参与的直接证据:** Agent participation is explicit in the paper and executable session driver. Initial goals and evaluation rules are human-provided; researchers revise evaluation after discovering untested failure modes.
- **Disclosed effort / 构建投入:** The public demo reports approximately USD 100 of Claude usage for ten trials. The inspected driver sets a USD 20 per-trial cap, not measured spend. These values do not account for the paper experiment, human work, GPU costs or lifetime maintenance.
- **Validation boundary / 验证覆盖:** The paper checks numerical drift and downstream math/retrieval performance, and reports previously accepted candidates with vocabulary, termination or state-handling failures. Its best-engine audit is distinct from those failed candidates. The public driver and inspected evolved code do not by themselves reproduce the full paper evaluation.
- **Evolution evidence / 适配与维护:** Code and reports are inherited, and working ideas may transfer between chains. Misleading reports and integration repairs remain part of the process; long-term production adaptation costs are not established.

**Sources:** [Source 1](https://arxiv.org/html/2610.04646v1) · [Source 2](https://github.com/smth-fun/self-evolving-inference-system/blob/bf2ddc5c5882a2573756b744c0e88c1b154739fa/README.md) · [Source 3](https://github.com/smth-fun/self-evolving-inference-system/blob/bf2ddc5c5882a2573756b744c0e88c1b154739fa/run_trial.sh) · [Source 4](https://github.com/smth-fun/mini-sglang/blob/2c1f6c307c96aa165873ad785cb0fa71fb71f9d3/python/minisgl/engine/engine.py) · [Source 5](https://github.com/nehzux/SEIS) · [Source 6](https://github.com/smth-fun/self-evolving-inference-system/blob/bf2ddc5c5882a2573756b744c0e88c1b154739fa/posts/post-2-evolve.md).

**Reviewed:** 2026-10-14. See the linked project record for mechanism-specific caveats.

<a id="vibeserve"></a>

## VibeServe / VibeSys: generation-time serving specialization

**Related project records:** [VibeServe / VibeSys](catalog.md#vibesys).

- **Why build it? / 为什么另建:** Explore whether per-target serving implementations can exploit opportunities outside a shared runtime, rather than only replacing individual operators.
- **Execution ownership / 重构边界:** The artifact is a construction framework whose VibeServe initiative produces target-specific serving stacks. It is not itself one universal inference runtime.
- **Retained components / 复用什么:** The documented workflow reuses serving knowledge, profiling tools, coding agents and existing model/kernel facilities where appropriate; generated outputs must disclose their own dependencies.
- **Scope given up / 取舍与兼容性:** Each candidate is qualified against its scenario and evaluation contract. The broad current framework also includes non-inference tasks; that breadth is not inferred coverage of generated serving systems.
- **Construction process / 怎样构建:** The paper separates outer design search and inner implementation/evaluation. The inspected current code stores evaluator, workload and environment identities with an evaluation recipe, and rejects parallel candidate modes without suitable isolation.
- **AI participation / AI 参与的直接证据:** Coding agents participate explicitly. Humans supply objectives, domain knowledge and evaluation definitions; current framework-side measurement is distinct from an agent claiming a pass.
- **Disclosed effort / 构建投入:** This review does not establish a comparable lifecycle cost. Any reported campaign budget must be attached to its paper scenario and separated from validation, integration and subsequent maintenance.
- **Validation boundary / 验证覆盖:** Inspected the README and host evaluation wiring, alongside the paper and lab report. Contract-specific tests and a read-only reviewer are not universal numerical or service-correctness proofs. No campaign was reproduced.
- **Evolution evidence / 适配与维护:** The project now uses the VibeSys name and a broader task framework. Pin current code separately from the VibeServe paper rather than transferring historical results to all later versions.

**Sources:** [Source 1](https://arxiv.org/html/2605.06068v1) · [Source 2](https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/) · [Source 3](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/README.md) · [Source 4](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/src/vibesys/core_wiring.py).

**Reviewed:** 2026-10-14. See the linked project record for mechanism-specific caveats.

<a id="automegakernel"></a>

## AutoMegaKernel: checked generation of model-level execution

**Related project records:** [AutoMegaKernel](catalog.md#automegakernel).

- **Why build it? / 为什么另建:** Reduce per-operator execution boundaries while making generated whole-model schedules inspectable before device launch.
- **Execution ownership / 重构边界:** One persistent cooperative launch executes one forward pass; counters reset between launches, KV persists and the host advances decoding. Instruction tuning and ScheduleConfig search are different edit surfaces.
- **Retained components / 复用什么:** A handwritten trusted VM, instruction ABI, model importer, CUDA runtime and reference implementations remain shared. No per-model handwritten CUDA does not mean the trusted base is automatically generated.
- **Scope given up / 取舍与兼容性:** Current inference scope is restricted to supported model graphs and hardware. Paper shape-level performance and real-checkpoint quality results are separate; low-bit comparisons are not equal-precision controls.
- **Construction process / 怎样构建:** The documented first loop tunes an ABI micro-kernel; the second proposes structured schedules lowered by the fixed VM. The inspected IR checks counters, dependencies, placement and buffer ordering.
- **AI participation / AI 参与的直接证据:** The compiler exposes an explicit coding-agent harness. Structured schedule search must not be described as unrestricted synthesis of a new runtime.
- **Disclosed effort / 构建投入:** Unattended self-tuning demonstrations compare against their own starting point. This inspection establishes neither full construction cost nor maintenance savings over a shared serving framework.
- **Validation boundary / 验证覆盖:** Inspected schedule/ir.py, including static dependency and hazard checks. Some hazard checks are task-count-capped; references and supported VM semantics remain trusted. This is not a mechanized proof and no CUDA tests were run here.
- **Evolution evidence / 适配与维护:** New operators, model features or device targets require compatible importer, ABI, validator and VM support; broad self-retargeting claims do not remove these obligations.

**Sources:** [Source 1](https://arxiv.org/html/2606.09682v1) · [Source 2](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/HARNESS.md) · [Source 3](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/schedule/ir.py).

**Reviewed:** 2026-10-14. See the linked project record for mechanism-specific caveats.

<a id="splash"></a>

## Splash: model-specific execution with agent-generated kernels

**Related project records:** [Splash](catalog.md#splash).

- **Why build it? / 为什么另建:** The stated aim is efficient local model serving by specializing model dimensions, speculative execution and memory planning rather than maximizing model coverage.
- **Execution ownership / 重构边界:** C++/Metal code owns target/draft execution, kernels, scheduling and state management; a Python frontend exposes compatible HTTP APIs and vision input.
- **Retained components / 复用什么:** Uses existing checkpoints and tokenizers, Apple runtimes, and acknowledged llama.cpp-derived quantization tables and GGUF decoding material.
- **Scope given up / 取舍与兼容性:** Targets selected Qwen families and compatible Bonsai checkpoints on recent Apple silicon. Quantized weights, KV precision and optional Neural Engine prefill affect comparison conditions.
- **Construction process / 怎样构建:** Public native modules expose integration; the official launch account describes internal agents creating and tuning kernels for model shapes, with precompiled variants shipped to users.
- **AI participation / AI 参与的直接证据:** Directly disclosed for specialized kernels. The record does not establish agent authorship of the scheduler, frontend or entire engine.
- **Disclosed effort / 构建投入:** No development-effort or total lifecycle-cost accounting was found; throughput measurements do not establish cheaper construction.
- **Validation boundary / 验证覆盖:** Upstream provides numerical oracles, Metal tests, real-model checks and author-reported HTTP benchmarks. This survey inspected sources without running them.
- **Evolution evidence / 适配与维护:** Architecture checks, pinned model revisions and documented release regressions support evolution; continuing model-porting effort and long-term maintenance cost remain unknown.

**Sources:** [Source 1](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/README.md) · [Source 2](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/DEVELOPMENT.md) · [Source 3](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/runtime/model/Runtime.cpp) · [Source 4](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/runtime/engine/Engine.cpp) · [Source 5](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/THIRD_PARTY_NOTICES) · [Source 6](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/docs/performance.md) · [Source 7](https://inco.ai/blog/splash/).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="gufo"></a>

## Gufo: a vertical runtime for Strix Halo

**Related project records:** [Gufo](catalog.md#gufo).

- **Why build it? / 为什么另建:** Focus on selected models that fit Strix Halo unified memory, concentrating optimization and testing instead of maximizing hardware and model coverage.
- **Execution ownership / 重构边界:** Owns model execution, kernels, sessions and local serving. Text/vision, ASR/TTS, image generation and video paths have different qualification levels.
- **Retained components / 复用什么:** Links ROCm/HIP and BLAS libraries; adapts llama.cpp/ggml quantized kernels, DS4 components and other attributed model code.
- **Scope given up / 取舍与兼容性:** Production is restricted to Linux x86-64 gfx1151; supported checkpoints, quantization and speculative modes impose model-specific compatibility and quality limits.
- **Construction process / 怎样构建:** The documented development loop isolates each model’s C++/HIP library, kernels and reference checks. Historical implementation effort and human–AI task division are not disclosed.
- **AI participation / AI 参与的直接证据:** Not established: reviewed sources do not directly disclose AI authorship or task division; agent instructions do not establish either.
- **Disclosed effort / 构建投入:** Total development effort, human hours, agent tokens and long-term maintenance expenditure are not disclosed in the reviewed material.
- **Validation boundary / 验证覆盖:** Author reports numerical and serving checks. Flash-Next vision fails one threshold; image coverage is small and full-video perceptual quality remains unqualified.
- **Evolution evidence / 适配与维护:** Model-owned tests and quality records expose regression boundaries. Hosted CI covers CPU/repository checks; GPU qualification remains separate. No independent reproduction here.

**Sources:** [Source 1](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/README.md) · [Source 2](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/CMakeLists.txt) · [Source 3](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/DEVELOPMENT.md) · [Source 4](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/THIRD_PARTY_NOTICES.md) · [Source 5](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/src/models/qwen38_flash_next/engine.cpp) · [Source 6](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/models/qwen3.8-flash-next/QUALITY.md) · [Source 7](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/models/qwen-image-2.1/QUALITY.md) · [Source 8](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/models/minimax-h3/QUALITY.md) · [Source 9](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/docs/TESTING.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="zllm"></a>

## zLLM: native multimodal paths with per-device qualification

**Related project records:** [zLLM](catalog.md#zllm).

- **Why build it? / 为什么另建:** Embed selected models directly and control their execution, memory and device behavior without a Python model server in the runtime path.
- **Execution ownership / 重构边界:** Owns Rust model runtimes, vision processing, state and backend dispatch. Inspected ROCm paths implement FLUX conditioning/denoising and SeedVR2 distributed video computation.
- **Retained components / 复用什么:** Keeps pretrained models, checkpoint formats and hardware APIs; native operators and device kernels provide shared primitives across explicitly implemented model families.
- **Scope given up / 取舍与兼容性:** Supported model/backend combinations differ. A qualified ROCm image pipeline does not establish CUDA support, and the QNN path is calibrated-input validation rather than unrestricted serving.
- **Construction process / 怎样构建:** Port model graphs into native runtime modules, implement or reuse backend operations, then compare qualified device paths with reference/oracle behavior and expose capability checks.
- **AI participation / AI 参与的直接证据:** Development participation by AI is not established from the reviewed README and implementation files.
- **Disclosed effort / 构建投入:** Engineering effort and per-model adaptation cost are not quantified in the inspected sources; growing model coverage alone does not measure cheaper development.
- **Validation boundary / 验证覆盖:** Implementation paths and restrictions were inspected; author hardware reports were not reproduced. Quantization and distillation effects must be separated from native execution benefits.
- **Evolution evidence / 适配与维护:** Model specifications and separate backend modules expose adaptation work. Qualification tables make unsupported combinations visible but require continued updates as models evolve.

**Sources:** [Source 1](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/README.md) · [Source 2](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/deepseek_v4/vision.rs) · [Source 3](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/flux2_klein/rocm.rs) · [Source 4](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/seedvr2/rocm_pipeline.rs) · [Source 5](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/minicpm5/qnn.rs).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="ninfer"></a>

## NInfer: a native Qwen stack for one GPU

**Related project records:** [NInfer](catalog.md#ninfer).

- **Why build it? / 为什么另建:** The stated objective is maximum single-GPU performance for selected checkpoints; general model and device coverage is outside that target.
- **Execution ownership / 重构边界:** Native operators, model programs, state/KV management, scheduling and CLI/HTTP serving form one execution stack.
- **Retained components / 复用什么:** Retains pretrained weights, CUDA runtime, FFmpeg and HTTP/JSON/logging dependencies; owning execution does not imply a dependency-free system.
- **Scope given up / 取舍与兼容性:** The upstream target is Linux with sm_120a, one resident model and startup-fixed execution lanes; it is not a general multi-device deployment contract.
- **Construction process / 怎样构建:** Public C++/CUDA modules and development contracts expose how components fit together. The actual development chronology and human–AI division of work are not disclosed.
- **AI participation / AI 参与的直接证据:** Not established. AI-assistance contribution policies and agent instruction files are not implementation-authorship evidence.
- **Disclosed effort / 构建投入:** Development effort and lifecycle costs are not disclosed; inference throughput does not establish construction economics.
- **Validation boundary / 验证覆盖:** Published tests include independent operator oracles and opt-in real-engine integration checks. This survey did not execute them or reproduce performance.
- **Evolution evidence / 适配与维护:** Explicit architecture and contribution boundaries constrain changes; artifact-version migration is documented, but sustained adaptation cost is unknown.

**Sources:** [Source 1](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/README.md) · [Source 2](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/docs/maintainer/engine-architecture.md) · [Source 3](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/src/models/qwen3_5/execution/text.cpp) · [Source 4](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/docs/maintainer/build-system.md) · [Source 5](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/tests/README.md) · [Source 6](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/CONTRIBUTING.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="lily"></a>

## Lily: one checkpoint, explicit compatibility boundary

**Related project records:** [Lily](catalog.md#lily).

- **Why build it? / 为什么另建:** Reduce local execution overhead for a particular Qwen hybrid MoE workload on recent Apple GPUs.
- **Execution ownership / 重构边界:** Owns checkpoint validation, model graph, kernels, generation and a small session cache.
- **Retained components / 复用什么:** Reuses MLX-affine checkpoint storage, tokenizer dependencies and Metal; model execution does not use MLX.
- **Scope given up / 取舍与兼容性:** Only the supported architecture and quantization layout; greedy text generation with a restricted API.
- **Construction process / 怎样构建:** Rust model paths dispatch Metal shaders compiled at runtime. Contributions require CPU-reference kernel tests and route-boundary checks.
- **AI participation / AI 参与的直接证据:** Not established by the inspected sources; runtime use by coding agents is not authorship evidence.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Kernel, shader, API and golden-model tests are public. Checkpoint-backed tests can be skipped; author benchmark reports are not independent replication.
- **Evolution evidence / 适配与维护:** Pinned toolchain and checkpoints bound regression work; another architecture requires implementation and renewed numerical qualification.

**Sources:** [Source 1](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/README.md) · [Source 2](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/src/config.rs) · [Source 3](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/src/model.rs) · [Source 4](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/CONTRIBUTING.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="hipengine"></a>

## hipEngine: torch-free model execution for selected Radeon targets

**Related project records:** [hipEngine](catalog.md#hipengine).

- **Why build it? / 为什么另建:** Treat consumer Radeon and Strix Halo as primary targets rather than accepting CUDA-oriented execution choices.
- **Execution ownership / 重构边界:** Owns model loading, HIP dispatch, generation, shared KV state, batching and HTTP serving.
- **Retained components / 复用什么:** Uses ROCm/HIP and rocBLAS; documents lineage from Nano-vLLM scheduling ideas, ParoQuant, FastDMS and GGUF.
- **Scope given up / 取舍与兼容性:** Supports qualified model/device combinations on one GPU; precision, DMS and speculation options need separate quality checks.
- **Construction process / 怎样构建:** Model runners and a detailed RDNA tuning guide show measurement-led kernel and scheduling revisions, with exact fallback paths.
- **AI participation / AI 参与的直接证据:** Not established from the reviewed README, source and tuning records; coding-agent client workloads are not authorship evidence.
- **Disclosed effort / 构建投入:** Worklogs expose experiments and rejected routes, but total human effort, agent expenditure and maintenance cost remain unknown.
- **Validation boundary / 验证覆盖:** Publishes CPU-oracle, execution-profile and hardware benchmark gates; source inspection here does not reproduce them.
- **Evolution evidence / 适配与维护:** Alpha APIs and supported combinations can change; qualification is scoped to model, hardware, quantization and request shape.

**Sources:** [Source 1](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/README.md) · [Source 2](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/hipengine/runtime/qwen35_gguf_runner.py) · [Source 3](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/hipengine/generation/batch_scheduler.py) · [Source 4](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/docs/RDNA3-TUNING-GUIDE.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="imp"></a>

## imp: an explicitly agent-built stack for consumer Blackwell

**Related project records:** [imp](catalog.md#imp).

- **Why build it? / 为什么另建:** Exploit the selected chip’s native low-bit math and memory system for long conversations and concurrent agent requests.
- **Execution ownership / 重构边界:** Owns loaders, tokenization, model execution, KV planning, graph scheduling and the serving interfaces.
- **Retained components / 复用什么:** Uses CUDA, cuBLAS/cuBLASLt and CUTLASS plus existing model formats; native runtime ownership does not mean dependency-free execution.
- **Scope given up / 取舍与兼容性:** Concentrates on sm_120a and qualified models; precision and optional approximation paths have distinct semantics.
- **Construction process / 怎样构建:** An author-disclosed Claude Code workflow is accompanied by source, a dated mission journal, profiling records and audit artifacts.
- **AI participation / AI 参与的直接证据:** Disclosed in README and CONTRIBUTING: the author attributes implementation to Claude Code; this is not independent provenance verification.
- **Disclosed effort / 构建投入:** Published iteration records do not establish total tokens, human oversight time or lifetime maintenance cost.
- **Validation boundary / 验证覆盖:** Documents correctness, benchmark and real-hardware preflight gates; this audit did not run them.
- **Evolution evidence / 适配与维护:** Compiler, model and CUDA changes require renewed gates; benchmark defaults and quantization must remain explicit.

**Sources:** [Source 1](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/README.md) · [Source 2](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/CONTRIBUTING.md) · [Source 3](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/src/runtime/engine.cpp) · [Source 4](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/src/runtime/engine_scheduler.cpp) · [Source 5](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/docs/MISSION_JOURNAL.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="vte"></a>

## VTE: a measured RDNA3 runtime with generated HIP kernels

**Related project records:** [VTE](catalog.md#vte).

- **Why build it? / 为什么另建:** Control data movement and dispatch on a small consumer GPU and work around documented Windows/ROCm integration failures.
- **Execution ownership / 重构边界:** Owns loading, kernel generation, allocation, graph execution, sampling and serving rather than launching another inference engine.
- **Retained components / 复用什么:** Reuses HIP and GGUF conventions; Python orchestrates a native GPU path through a ctypes bridge.
- **Scope given up / 取舍与兼容性:** Curated model formats and GPU targets limit compatibility; the repository retains losing comparisons on larger models.
- **Construction process / 怎样构建:** Public performance and bug records trace naive execution through profiling, graph replay, GEMV changes and reverted optimizations.
- **AI participation / AI 参与的直接证据:** No verified division of human and AI development work in the reviewed sources.
- **Disclosed effort / 构建投入:** The iteration history is visible; total engineering hours, token costs and long-term maintenance effort are not reported.
- **Validation boundary / 验证覆盖:** Publishes numerical checks and Windows RX 7600/Linux W7900 measurements; some other targets are only compiled.
- **Evolution evidence / 适配与维护:** Driver behavior, model-specific bias/recurrent paths and new GPU architectures require fresh qualification; no independent reproduction here.

**Sources:** [Source 1](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/README.md) · [Source 2](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/docs/ARCHITECTURE.md) · [Source 3](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/docs/PERFORMANCE.md) · [Source 4](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/vte/core/model.py).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="zinc"></a>

## ZINC: a Zig stack built around consumer GPU execution

**Related project records:** [ZINC](catalog.md#zinc).

- **Why build it? / 为什么另建:** Make consumer AMD hardware a first-class local inference target with predictable memory and execution behavior.
- **Execution ownership / 重构边界:** Owns GGUF loading, tokenization, forward/decode orchestration, KV state and the local API server.
- **Retained components / 复用什么:** Uses Vulkan or HIP/hipBLAS interfaces and GGUF; ROCm implements a shared accelerator ABI over the native scheduler.
- **Scope given up / 取舍与兼容性:** Each model/backend combination needs its own tuning; experimental CUDA support does not inherit AMD benchmark results.
- **Construction process / 怎样构建:** Source and development guides expose native graph construction, shader compilation, profiling and repeatable comparison artifacts.
- **AI participation / AI 参与的直接证据:** AI authorship and task division are not established from reviewed sources; agent configuration files are not sufficient evidence.
- **Disclosed effort / 构建投入:** Build and benchmark procedures are public; total development and maintenance expenditure is unknown.
- **Validation boundary / 验证覆盖:** Publishes matched-host, same-weight comparisons with raw samples and losing rows; this audit inspects source only.
- **Evolution evidence / 适配与维护:** Model additions and platform changes require separate correctness and benchmark checks; support breadth is growing, not a universal guarantee.

**Sources:** [Source 1](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/README.md) · [Source 2](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/src/compute/forward.zig) · [Source 3](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/src/rocm/rocm_shim.c) · [Source 4](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/docs/DEVELOPMENT.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="memra"></a>

## memra: a Rust/CUDA engine qualified one hardware lane at a time

**Related project records:** [memra](catalog.md#memra).

- **Why build it? / 为什么另建:** Reduce orchestration and memory overhead on particular machines, including models larger than available GPU memory.
- **Execution ownership / 重构边界:** Owns native model programs, kernel dispatch, KV/speculative state, placement and serving admission.
- **Retained components / 复用什么:** Uses CUDA libraries and CUTLASS; third-party notices identify hand-ported llama.cpp kernels decoupled from GGML.
- **Scope given up / 取舍与兼容性:** Hardware lanes and numerical programs are qualified separately; public source currently carries the FSL-1.1-ALv2 license.
- **Construction process / 怎样构建:** Architecture, source and decision ledgers expose device-specific implementation choices, rejected routes and proof gates.
- **AI participation / AI 参与的直接证据:** No verified full division of human versus agent development work in the reviewed sources.
- **Disclosed effort / 构建投入:** Hardware and experimental details are disclosed; total development tokens, labor and maintenance costs remain unknown.
- **Validation boundary / 验证覆盖:** Tiered numerical and serving gates distinguish compile-only CI from GPU qualification; this audit did not execute them.
- **Evolution evidence / 适配与维护:** The current README pauses general development and routine model bring-ups, retaining bounded research questions and existing commitments.

**Sources:** [Source 1](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/README.md) · [Source 2](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/ARCHITECTURE.md) · [Source 3](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/crates/memra-engine/src/forward.rs) · [Source 4](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/crates/memra-engine/THIRD-PARTY.md) · [Source 5](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/docs/TESTING.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="kipp"></a>

## Kipp: a checkpoint-bounded C11 Qwen execution stack

**Related project records:** [Kipp](catalog.md#kipp).

- **Why build it? / 为什么另建:** Keep one model family understandable and directly controllable rather than automatically accepting arbitrary model graphs.
- **Execution ownership / 重构边界:** Owns loading, CPU reference execution, GPU interfaces, KV sessions, batching and HTTP serving.
- **Retained components / 复用什么:** Uses GGUF conventions, CUDA or Metal APIs; Python/PyTorch are conversion tools, outside the inference path.
- **Scope given up / 取舍与兼容性:** Rejects unregistered checkpoints and unsupported tensor layouts; portability means separately implemented and tested backends.
- **Construction process / 怎样构建:** The roadmap records successive CPU, KV, Metal, CUDA, batching and serving phases with explicit completion gates.
- **AI participation / AI 参与的直接证据:** Not established; the project’s hand-written description and agent instruction files do not resolve authorship or task allocation.
- **Disclosed effort / 构建投入:** No complete development-hour, token or maintenance-cost accounting was found.
- **Validation boundary / 验证覆盖:** Publishes CPU-oracle differential gates on real GPUs and comparisons including losing rows; no independent execution in this audit.
- **Evolution evidence / 适配与维护:** New checkpoints require registry and architecture review; serving and quantization extensions must preserve the documented model contract.

**Sources:** [Source 1](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/README.md) · [Source 2](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/docs/ARCHITECTURE.md) · [Source 3](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/docs/ROADMAP.md) · [Source 4](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/src/kipp.c) · [Source 5](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/src/cuda/kipp_cuda.cu).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="saragossa"></a>

## Saragossa: resident decode with explicit state ownership

**Related project records:** [Saragossa](catalog.md#saragossa).

- **Why build it? / 为什么另建:** Reduce per-operation synchronization for resident local decode, including selected text and speech workloads.
- **Execution ownership / 重构边界:** Owns model forward paths, Metal dispatch, KV/recurrent state, scratch lifetimes and prefix snapshots.
- **Retained components / 复用什么:** Loads MLX-affine weights; speech golden fixtures were captured from a frozen earlier MLX-based reference.
- **Scope given up / 取舍与兼容性:** Local single-user policies, supported quantization layouts and precision switches constrain the comparison scope.
- **Construction process / 怎样构建:** Source separates resident-state ownership from kernel implementation. Leased scratch buffers prevent overlapping live intermediates from silently aliasing.
- **AI participation / AI 参与的直接证据:** A source comment attributes a non-clonable GPU-state constraint to Codex D; the review process, coding role and overall AI contribution are not established.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Golden fixtures, differential tests and author benchmarks are exposed. Near-tie drift and precision settings need inspection; no model run was performed.
- **Evolution evidence / 适配与维护:** Runtime switches and golden provenance support regression diagnosis; broader hardware qualification and lifecycle cost are unknown.

**Sources:** [Source 1](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/README.md) · [Source 2](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/decode_resident.rs) · [Source 3](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/decode_resident/attention.rs) · [Source 4](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/runtime_flags.rs) · [Source 5](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/tests/golden/README.md).

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

<a id="llaminar"></a>

## Llaminar: constructing native execution plans for mixed hardware

**Related project records:** [Llaminar](catalog.md#llaminar).

- **Why build it? / 为什么另建:** Use heterogeneous existing hardware, including CPU memory and older GPUs, without assuming a homogeneous accelerator fleet.
- **Execution ownership / 重构边界:** Owns model graphs, placement plans, kernels, captured execution and tensor/pipeline/expert coordination.
- **Retained components / 复用什么:** Uses GGUF and vendor GPU APIs plus NCCL, RCCL and MPI; cross-vendor communication has an explicit host bridge.
- **Scope given up / 取舍与兼容性:** Selected Qwen families and hardware recipes define support; current production activations are FP32, independent of weight/KV formats.
- **Construction process / 怎样构建:** Model graph builders feed a placement planner; source and devcontainer documentation expose patched collective dependencies and capture rules.
- **AI participation / AI 参与的直接证据:** No verified attribution or division of agent implementation work in reviewed sources.
- **Disclosed effort / 构建投入:** Planning and build procedures are public, but total engineering effort and maintenance economics are unknown.
- **Validation boundary / 验证覆盖:** Publishes end-to-end recipe qualification and separates nightly preflight from release certification; this audit inspected source only.
- **Evolution evidence / 适配与维护:** Mixed CUDA/ROCm capture and collective versions are coupled; unsupported configurations are rejected and require explicit requalification.

**Sources:** [Source 1](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/README.md) · [Source 2](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/execution/local_execution/engine/ForwardExecutionEngine.cpp) · [Source 3](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/collective/backends/HeterogeneousBackend.cpp) · [Source 4](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/planning/AutomaticOrchestrationPlanner.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="ane-cpp"></a>

## ane.cpp: hardware probes feed an ANE execution stack

**Related project records:** [ane.cpp](catalog.md#ane-cpp).

- **Why build it? / 为什么另建:** Explore useful ANE offload for background and shared-process inference, not only peak foreground token rate.
- **Execution ownership / 重构边界:** Owns MIL kernel construction, private API invocation, persistent compilation caches and CPU/ANE dispatch boundaries.
- **Retained components / 复用什么:** Forks ANE-LM; reuses CPU operations and reverse-engineering findings from the companion field guide.
- **Scope given up / 取舍与兼容性:** Selected dense text models only; private APIs, numerical constraints and CPU fallback limit portability.
- **Construction process / 怎样构建:** The documented workflow first tests isolated operations against CPU references, then ports surviving findings into the model runtime and measures changes.
- **AI participation / AI 参与的直接证据:** An autoresearch-style autonomous workflow is published; the share of actual code or experiments produced by agents is not quantified.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** The field guide records kept/discarded probes and setup-specific measurements. This audit did not reproduce ANE behavior or model quality.
- **Evolution evidence / 适配与维护:** Compiler/API changes and undocumented behavior require requalification; no total maintenance-cost evidence is available.

**Sources:** [Source 1](https://github.com/skyfallsin/ane.cpp/blob/b87bf57356c26025853a60cddfe4b58784ee4fda/README.md) · [Source 2](https://github.com/skyfallsin/ane.cpp/blob/b87bf57356c26025853a60cddfe4b58784ee4fda/core/ane_runtime.cpp) · [Source 3](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/README.md) · [Source 4](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/program.md) · [Source 5](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/results.tsv).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="cactus"></a>

## Cactus: captured model components to a mobile runtime

**Related project records:** [Cactus](catalog.md#cactus).

- **Why build it? / 为什么另建:** Make selected language, vision and speech models practical on mobile and wearable devices with constrained memory and native integration requirements.
- **Execution ownership / 重构边界:** Owns model-bundle execution, component graphs, state handling and ARM/Metal kernels; inspected model code manages quantized cross-attention state and component boundaries.
- **Retained components / 复用什么:** Retains source framework export facilities, pretrained checkpoints and platform compute APIs. Model capture uses PyTorch export; this is not elimination of all framework tooling.
- **Scope given up / 取舍与兼容性:** Prequalified models and bundles have a firmer support boundary than experimental conversion of arbitrary Hugging Face models; optional cloud handoff changes deployment assumptions.
- **Construction process / 怎样构建:** Capture supported components, canonicalize and optimize the intermediate graph, bind converted weights, then lower into Cactus graph operations executed by the native engine.
- **AI participation / AI 参与的直接证据:** AI authorship or development-stage attribution is not established by the reviewed implementation and documentation.
- **Disclosed effort / 构建投入:** No comparable total engineering effort, porting cost or maintenance-cost measurement was found in the inspected sources.
- **Validation boundary / 验证覆盖:** Source paths establish graph capture and native state ownership, not successful builds or output quality here; quantization needs separate quality assessment.
- **Evolution evidence / 适配与维护:** The bundle and component interfaces expose where new model support must be added. Expanding conversion coverage remains an explicit compatibility obligation.

**Sources:** [Source 1](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/README.md) · [Source 2](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/python/cactus/transpile/capture_pytorch.py) · [Source 3](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/python/cactus/transpile/lower.py) · [Source 4](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/cactus-engine/src/model.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="fastflowlm"></a>

## FastFlowLM: NPU-specific model engines and host integration

**Related project records:** [FastFlowLM](catalog.md#fastflowlm).

- **Why build it? / 为什么另建:** Target client NPU dataflow and power constraints through dedicated model execution instead of assuming a GPU runtime transfers unchanged.
- **Execution ownership / 重构边界:** Public host runtimes own backend selection, model loading, device tensors and decode streams. The original flm model engines remain prebuilt libraries.
- **Retained components / 复用什么:** Uses AMD runtime infrastructure and compiler/kernel providers; rai integrates ryzenai-corelib, while project history credits IRON for the original NPU construction route.
- **Scope given up / 取舍与兼容性:** Only qualified model, kernel-provider and device combinations are supported. Open integration source is not equivalent to public source for every engine.
- **Construction process / 怎样构建:** The model-addition guide separates GGUF validation, shape planning, packed weights, host operations and device execution, with Phi-4 as a worked integration example.
- **AI participation / AI 参与的直接证据:** No direct evidence in the reviewed sources attributes model-runtime construction or optimization to AI coding.
- **Disclosed effort / 构建投入:** The public development history records releases and organizational evolution, but does not establish person-hours or a controlled construction-cost comparison.
- **Validation boundary / 验证覆盖:** Inspected source and architecture documents explain the integration contract. Platform execution coverage varies; this survey did not run NPU binaries or reproduce performance.
- **Evolution evidence / 适配与维护:** Explicit model/provider/device separation is intended to keep adding one backend from breaking others; binary ABI compatibility remains an additional maintenance boundary.

**Sources:** [Source 1](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/README.md) · [Source 2](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/src/common/models/README.md) · [Source 3](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/src/common/AutoModel/model_backend.cpp) · [Source 4](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/flm_story.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="infire"></a>

## Cloudflare Infire: platform-specific serving reconstruction

**Related project records:** [Cloudflare Infire](catalog.md#infire).

- **Why build it? / 为什么另建:** Cloudflare describes a mismatch between its geographically distributed resource-constrained nodes and the deployment assumptions of its earlier vLLM setup.
- **Execution ownership / 重构边界:** The disclosed stack includes the HTTP server, batcher and model executor, with model-specific kernels and execution graphs. Later work extends parallel model execution.
- **Retained components / 复用什么:** The report names Hyper, HuggingFace tokenizers, CUDA and cuBLASLt for suitable operations. A native replacement still retains shared libraries and established batching/cache mechanisms.
- **Scope given up / 取舍与兼容性:** Specialization is to a provider platform and its deployment envelope, not one checkpoint. Proprietary implementation prevents independent source-level checking in this review.
- **Construction process / 怎样构建:** The original report describes a Rust rewrite with asynchronous loading, JIT compilation and hardware-focused kernels. The later report describes added multi-GPU and memory/startup work.
- **AI participation / AI 参与的直接证据:** No direct AI-construction attribution was established from the reviewed engineering reports. Do not infer it from the project being a newly built engine.
- **Disclosed effort / 构建投入:** The initial report measures CPU usage and throughput in selected deployment configurations; those operational observations are not a measurement of development or lifecycle cost.
- **Validation boundary / 验证覆盖:** Two official engineering reports were reviewed. The initial comparison distinguishes bare-metal vLLM, sandboxed vLLM and CPU-constrained operation; keep those conditions separate. No engine execution or source audit was possible from these materials.
- **Evolution evidence / 适配与维护:** The later multi-GPU report supplies concrete evolution evidence. Record new scope as a later stage rather than rewriting the original report or assuming all future model support.

**Sources:** [Source 1](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/) · [Source 2](https://blog.cloudflare.com/high-performance-llms/).

**Reviewed:** 2026-10-14. See the linked project record for mechanism-specific caveats.

<a id="kie"></a>

## Kog Inference Engine: model and device co-designed execution

**Related project records:** [Kog Inference Engine (KIE)](catalog.md#kie).

- **Why build it? / 为什么另建:** Target the low-latency single-request regime rather than maximizing aggregate throughput through large batches.
- **Execution ownership / 重构边界:** The vendor describes a monokernel managing sequence generation, sampling, state and cross-device communication, not only an isolated matrix multiplication.
- **Retained components / 复用什么:** Pretrained model assets, AMD/NVIDIA devices and their programming/runtime interfaces remain prerequisites. The vendor claims its own execution implementation; public engine source was not established.
- **Scope given up / 取舍与兼容性:** The reviewed preview combines a roughly 2B FP16 Laneformer model with eight GPUs and batch one. Delayed tensor parallelism changes the model architecture, so runtime and model contributions must be separated.
- **Construction process / 怎样构建:** The engineering report describes compile-time work assignment, device-side synchronization, continuous weight streaming and delayed cross-device reductions. These are documentation-backed design claims, not inspected implementation paths.
- **AI participation / AI 参与的直接证据:** No direct coding-agent construction evidence was established in the reviewed materials; relevance comes from execution co-design.
- **Disclosed effort / 构建投入:** Reported latency and tokens per second do not quantify GPU cost per request, utilization under mixed load, construction effort or lifetime maintenance.
- **Validation boundary / 验证覆盖:** Reviewed the technical monokernel article and matching preview conditions. Neither is an independent replication or a complete quality-equivalence protocol; announced future model support remains a roadmap.
- **Evolution evidence / 适配与维护:** Model and device co-design creates adaptation obligations. The release of model weights, where applicable, must not be confused with publication of the inference engine implementation.

**Sources:** [Source 1](https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/) · [Source 2](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/).

**Reviewed:** 2026-10-14. See the linked project record for mechanism-specific caveats.

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

<a id="swiftlet"></a>

## Swiftlet: AI-assisted Qwen execution on Macs and phones

**Related project records:** [Swiftlet](catalog.md#swiftlet).

- **Why build it? / 为什么另建:** Run selected Qwen checkpoints that cannot be resident within ordinary Mac or iPhone memory budgets.
- **Execution ownership / 重构边界:** Owns CPU/Metal model paths, qpack conversion, expert cache and chat-state integration.
- **Retained components / 复用什么:** Uses MLX-LM numerical references; credits TurboFieldfare design lessons and Colibri caching ideas while describing a separate implementation.
- **Scope given up / 取舍与兼容性:** Restricted model family, quantization-quality tradeoffs and costly long-prompt prefill bound the practical deployment envelope.
- **Construction process / 怎样构建:** Author describes Swift/Metal implementation against per-layer reference fixtures, with container verification and incremental-versus-full-sequence checks.
- **AI participation / AI 参与的直接证据:** Explicitly states it was built with Claude Code. Roles in design, debugging and tuning, and the fraction of generated code, are unspecified.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Public fixture, kernel, cache and decode tests are available; author/device reports are not independent reproduction.
- **Evolution evidence / 适配与维护:** The roadmap identifies prefill and phone-kernel work still needed; cross-version adaptation effort is not quantified.

**Sources:** [Source 1](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/README.md) · [Source 2](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Sources/SwiftletCore/ExpertCache.swift) · [Source 3](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Sources/SwiftletCore/QwenCPUModel.swift) · [Source 4](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Tests/SwiftletCoreTests/IncrementalDecodeTests.swift).

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

<a id="turbo-fieldfare"></a>

## TurboFieldfare: a runtime designed around an 8 GB memory budget

**Related project records:** [TurboFieldfare](catalog.md#turbo-fieldfare).

- **Why build it? / 为什么另建:** Run a checkpoint larger than available memory while keeping common weights and working state bounded.
- **Execution ownership / 重构边界:** Owns expert packaging, installation, residency, prefill/decode scheduling and model-specific kernels.
- **Retained components / 复用什么:** Reuses swift-transformers tokenization; Transformers, MLX and GGML implementations provide numerical and kernel references.
- **Scope given up / 取舍与兼容性:** Narrow model support and SSD-dependent latency replace broad compatibility and fully resident speed.
- **Construction process / 怎样构建:** Published experiments trace the move from demand paging to explicit reads, cache policy changes, kernel designs and later reversals.
- **AI participation / AI 参与的直接证据:** AI participation in the construction is not established by the inspected sources.
- **Disclosed effort / 构建投入:** The curated inventory records 103 experiments, not total developer time or monetary cost.
- **Validation boundary / 验证覆盖:** The project reports end-to-end and quality gates, including rejected low-bit KV paths. The inventory is curated design history, not independent replication.
- **Evolution evidence / 适配与维护:** Model-free tests and real-model acceptance are separated; the effort to sustain future models and platform changes is unknown.

**Sources:** [Source 1](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/README.md) · [Source 2](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/SYSTEM_DESIGN.md) · [Source 3](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/OPTIMIZATION_JOURNEY.md) · [Source 4](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/experiments/EXPERIMENT_INVENTORY.md) · [Source 5](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/IMPLEMENTATION_REFERENCES.md) · [Source 6](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/Sources/TurboFieldfare/Infrastructure/Streaming/PreadExpertStreamer.swift).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="tuff"></a>

## TUFF: extending a streaming runtime across model families

**Related project records:** [TUFF](catalog.md#tuff).

- **Why build it? / 为什么另建:** Make selected large MoE checkpoints usable on ordinary memory-constrained Macs.
- **Execution ownership / 重构边界:** Owns native model execution, expert I/O, memory policy and the model-owning decode service.
- **Retained components / 复用什么:** Explicitly credits TurboFieldfare for the original Gemma runtime and streaming foundation; uses Swift/Metal and tokenizer packages.
- **Scope given up / 取舍与兼容性:** Each new architecture needs format, kernel, prompt and real-run qualification; hardware results remain configuration-specific.
- **Construction process / 怎样构建:** Extends TurboFieldfare with Gated DeltaNet state updates, fused projections and Qwen gated-attention paths. Qualification calls for CPU references, toy-forward tests, prompt goldens and a real model run.
- **AI participation / AI 参与的直接证据:** The maintainer explicitly discloses using AI on TUFF and requires human line-by-line review; task division and amount are unspecified.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Public model-free checks and author/community benchmarks exist; most direct release testing is on one 16 GB M2 machine.
- **Evolution evidence / 适配与维护:** The contribution guide preserves old model formats and release recovery; the cost of the expanded compatibility surface is unquantified.

**Sources:** [Source 1](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/README.md) · [Source 2](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/CONTRIBUTING.md) · [Source 3](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/docs/HOW_TUFF_WORKS.md) · [Source 4](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/Sources/TUFFEngine/Infrastructure/Streaming/PreadExpertStreamer.swift) · [Source 5](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/Sources/TUFFEngine/Runtime/Inference/RealForwardRunner.swift).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="swiftlm"></a>

## SwiftLM: a specialized streaming path inside an MLX stack

**Related project records:** [SwiftLM](catalog.md#swiftlm).

- **Why build it? / 为什么另建:** Replace uncontrolled operating-system swapping with explicit expert streaming under memory pressure.
- **Execution ownership / 重构边界:** The case covers the SSD expert path and its integration; it is not a claim that every server feature is a new execution stack.
- **Retained components / 复用什么:** Reuses maintained MLX Swift and MLX Swift LM forks, Hugging Face tokenization and an HTTP framework.
- **Scope given up / 取舍与兼容性:** Expert union across speculative verification positions may increase I/O; model and release compatibility require separate checks.
- **Construction process / 怎样构建:** Source and design documents describe asynchronous reads and deliberate GPU synchronization. Release notes expose failures introduced by upstream synchronization and subsequent repairs.
- **AI participation / AI 参与的直接证据:** Not established by the inspected sources; runtime use by coding agents is not authorship evidence.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** The repository supplies configuration-specific measurements and records failed long-context checks. This audit did not run the engine or validate headline speedups.
- **Evolution evidence / 适配与维护:** Documented regressions illustrate a real cost of retaining upstream compatibility, but engineering hours and total cost remain unknown.

**Sources:** [Source 1](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/README.md) · [Source 2](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/Package.swift) · [Source 3](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/docs/moe_ssd_streaming_architecture.md) · [Source 4](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/Sources/MLXInferenceCore/SSDStreamingRecovery.swift) · [Source 5](https://github.com/SharpAI/mlx-swift-lm/blob/4f1fdaabeb490d3e97b0ff71fc0132bca4078fa2/Libraries/MLXLMCommon/SwitchLayers.swift).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="colibri"></a>

## Colibri: separate C engines with shared streaming components

**Related project records:** [Colibri](catalog.md#colibri).

- **Why build it? / 为什么另建:** Execute very large sparse models without requiring all expert weights to remain in RAM.
- **Execution ownership / 重构边界:** Owns per-family forward paths, container readers, routed expert stores and optional device tiers.
- **Retained components / 复用什么:** Uses native OS I/O and optional GPU APIs; provenance notes identify adapted DwarfStar and Swiftlet components.
- **Scope given up / 取舍与兼容性:** Supported formats and backend coverage differ by engine; storage capacity gains do not imply fast interactive generation.
- **Construction process / 怎样构建:** Independent model-family programs are checked against generated references. Contribution rules preserve a working default CPU route and require targeted validation.
- **AI participation / AI 参与的直接证据:** Inspected porting notes contain agent-oriented plans, but do not establish the actual division of coding work.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Strict synthetic oracles include an explicit teacher-forcing mismatch allowance and exact greedy checks. They are narrower than full-model quality validation.
- **Evolution evidence / 适配与维护:** The project keeps an engine/backend matrix and targeted tests; maintenance cost across this matrix has not been disclosed.

**Sources:** [Source 1](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/README.md) · [Source 2](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/c/qwen36.c) · [Source 3](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/docs/qwen36.md) · [Source 4](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/CONTRIBUTING.md) · [Source 5](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/THIRD_PARTY_NOTICES.md).

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

<a id="llamampere"></a>

## llamAmpere: specialize a shared runtime for Ampere and Qwen

**Related project records:** [llamAmpere](catalog.md#llamampere).

- **Why build it? / 为什么另建:** Fit long-context Qwen3.8-27B inference on consumer Ampere GPUs while improving speculative verification and decode efficiency.
- **Execution ownership / 重构边界:** A substantial llama.cpp/TurboQuant fork changes kernels, speculative execution and state management; it is not a runtime built from scratch.
- **Retained components / 复用什么:** Retains GGML/GGUF, llama.cpp server and model infrastructure; extends TurboQuant/MTP paths and adapts KVarN-derived cache compression.
- **Scope given up / 取舍与兼容性:** Optimized coverage centers on SM86/Qwen paths. Quantized KV and the recommended post-trained Swift derivative are not equivalent to original BF16 Qwen.
- **Construction process / 怎样构建:** Release articles trace profiling, candidate kernels, runtime fixes and rejected experiments; repeated upstream merges preserve shared capabilities and require integration repairs.
- **AI participation / AI 参与的直接证据:** Coding-agent contribution is not established. Handover notes mention Claude/Hermes sessions but do not attribute implementation or quantify task division.
- **Disclosed effort / 构建投入:** Development effort, agent expenditure and total maintenance cost are not disclosed in the reviewed sources.
- **Validation boundary / 验证覆盖:** Authors report matched-setting speed tests and numerical checks; separate engine changes from checkpoint, KV format and sampling effects. Not independently reproduced here.
- **Evolution evidence / 适配与维护:** Version 0.5.3 fixes cache-restoration and Blackwell build regressions; an unresolved parallel-8 failure limits extrapolation from single-stream results.

**Sources:** [Source 1](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN_AMPERE.md) · [Source 2](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/llamampere-v0.5/RELEASE_NOTES.md) · [Source 3](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/ggml/src/ggml-cuda/mmvq.cu) · [Source 4](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/development/sjkvarn-cuda.md) · [Source 5](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/llamampere-v0.5.3/RELEASE_NOTES.md) · [Source 6](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/docs/llamampere-v0.2/ARTICLE.md) · [Source 7](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN38_SM86_FRONTIER_HANDOVER.md) · [Source 8](https://huggingface.co/jakeatx/ATX-Swift-1.5-Qwen3.8-27B-Uncensored-IQ4_XS-M-GGUF/blob/1f3a29191771b5dae54254fa590b0a0013c18ea1/README.md) · [Source 9](https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27b/blob/b4c84d42903a8646b25857eb2827288d92ed85a4/README.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="vllm-radiance"></a>

## vLLM Radiance: a qualified RDNA4 backend inside a pinned vLLM stack

**Related project records:** [vLLM Radiance](catalog.md#vllm-radiance).

- **Why build it? / 为什么另建:** Expose RDNA4 hardware instructions and kernels that generic compiler or framework routes do not efficiently select.
- **Execution ownership / 重构边界:** Replaces attention, recurrent, GEMM and collective paths through native kernels and guarded vLLM overlays.
- **Retained components / 复用什么:** Retains vLLM, AMD PyTorch/Triton and AITER; credits StillDeadcode’s Radiance/libr4d and ggz14’s MXFP4 work.
- **Scope given up / 取舍与兼容性:** TP2 R9700 is the main qualified configuration; W4A8, approximate verify-head and speculative modes require distinct numerical scrutiny.
- **Construction process / 怎样构建:** Pins the complete compiler stack and records overlays, upstream provenance, correctness gates and release promotion rules.
- **AI participation / AI 参与的直接证据:** AI implementation participation is not established from the reviewed public sources.
- **Disclosed effort / 构建投入:** The README says a full stack build takes hours; that is build latency, not total development effort.
- **Validation boundary / 验证覆盖:** Publishes hardware and synthetic checks but explicitly leaves strict cross-mode speculative equivalence unpassed.
- **Evolution evidence / 适配与维护:** Coupled framework/compiler upgrades have caused hangs; manifests and gated patch overlays make this recurring burden visible.

**Sources:** [Source 1](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/README.md) · [Source 2](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/radiance_r4d_attn.py) · [Source 3](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/radiance_mxfp4.py) · [Source 4](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/docs/maintenance/ARCHITECTURE.md) · [Source 5](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/docs/NUMERICAL_CORRECTIONS.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="anemll-flash-llama"></a>

## ANEMLL Flash llama.cpp: changing the expert handoff inside llama.cpp

**Related project records:** [ANEMLL Flash llama.cpp](catalog.md#anemll-flash-llama).

- **Why build it? / 为什么另建:** Make large sparse checkpoints feasible with bounded memory and reduce repeated expert reads during prefill.
- **Execution ownership / 重构边界:** Changes model loading, runtime slot ownership and routed graph inputs; other engine services remain shared.
- **Retained components / 复用什么:** Reuses llama.cpp/GGML, its model implementations, formats and Metal backend.
- **Scope given up / 取舍与兼容性:** Each architecture needs explicit routing-contract integration; optional expert-count reductions are approximations, not scheduling-only gains.
- **Construction process / 怎样构建:** The porting guide separates shared storage machinery from model-specific handoffs, preserving a fallback for A/B checks before introducing native slot mapping.
- **AI participation / AI 参与的直接证据:** Not established by the inspected sources; runtime use by coding agents is not authorship evidence.
- **Disclosed effort / 构建投入:** Development hours, total cost and maintenance effort are not disclosed.
- **Validation boundary / 验证覆盖:** Trace, replay, cache estimation and model-specific comparisons are public. Stable anchor models and experimental ports have different evidence strength.
- **Evolution evidence / 适配与维护:** Upstream compatibility and architecture-specific graph contracts both require upkeep; the guide documents work but not total adaptation cost.

**Sources:** [Source 1](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/README.md) · [Source 2](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/src/llama-context.cpp) · [Source 3](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/native-slot-bank-porting.md) · [Source 4](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/flashmoe-layer-major-dedup-single-sidecar.md) · [Source 5](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/moe-bank-modeling-workflow.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="ninfer-3090"></a>

## NInfer-3090: retargeting NInfer to Ampere’s kernels and memory budget

**Related project records:** [NInfer-3090](catalog.md#ninfer-3090).

- **Why build it? / 为什么另建:** Run selected Qwen models on an existing 24 GB Ampere card whose arithmetic and capacity differ from upstream Blackwell.
- **Execution ownership / 重构边界:** Retains NInfer architecture but changes SM86 quantized execution, memory profiles, state transactions and speculative scheduling.
- **Retained components / 复用什么:** Credits Neroued/NInfer, Don-Chad’s initial 3090 port and later Infernix imports; reuses CUDA/cuBLAS and model containers.
- **Scope given up / 取舍与兼容性:** Unsupported Blackwell-native arithmetic must use alternative routes; compressed KV and cohort sizes affect accuracy and capacity.
- **Construction process / 怎样构建:** Release notes and source show tensor-core kernel additions, artifact migrations and upstream catch-up alongside measured profile changes.
- **AI participation / AI 参与的直接证据:** No verified allocation of AI coding tasks or total AI authorship was established for this continuation.
- **Disclosed effort / 构建投入:** Release and migration histories are public, but total porting and maintenance effort is unknown.
- **Validation boundary / 验证覆盖:** Publishes per-profile benchmark and correctness artifacts; these remain author-reported and were not reproduced here.
- **Evolution evidence / 适配与维护:** Model-container and KV contracts evolve upstream; the 3090 continuation must requalify kernels, conversion and profiles after merges.

**Sources:** [Source 1](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/README.md) · [Source 2](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/src/ops/linear/ggml/ggml_mmq.cuh) · [Source 3](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/src/models/qwen3_5/program/transactions/replay.cpp) · [Source 4](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/RELEASE_NOTES_0.11.0.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="infernix"></a>

## Infernix: extending NInfer across GPU, CPU and NVMe tiers

**Related project records:** [Infernix](catalog.md#infernix).

- **Why build it? / 为什么另建:** Serve a large sparse Qwen model on one consumer GPU while retaining local agent workloads and long contexts.
- **Execution ownership / 重构边界:** Adds expert residency, CPU miss execution, transfer overlap, NVMe embedding access and request-state handling to NInfer.
- **Retained components / 复用什么:** Retains NInfer’s artifact and kernel foundations; credits Strata’s model transcription and published measurements as references.
- **Scope given up / 取舍与兼容性:** Needs substantial host memory and storage; precision choices and different model conversions complicate cross-engine comparisons.
- **Construction process / 怎样构建:** Source exposes separate expert streams, CPU miss workers and cache tiers; the author describes iterative AI-assisted development.
- **AI participation / AI 参与的直接证据:** Disclosed: post-fork work used AI, principally Claude and local Qwen; the author explicitly cautions about completeness.
- **Disclosed effort / 构建投入:** A coding-tool subscription is acknowledged, but total tokens, human oversight and hardware expenditure are not reported.
- **Validation boundary / 验证覆盖:** Publishes server comparisons and perplexity checks; different quantizations must not be interpreted as isolated runtime speedups.
- **Evolution evidence / 适配与维护:** A hobby continuation tracking changing upstream formats and models; long-term support and total maintenance effort are unknown.

**Sources:** [Source 1](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/README.md) · [Source 2](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/src/ops/offloaded_sparse_moe/cpu/miss_service.cpp) · [Source 3](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/src/models/qwen4_exp/execution/expert_stream.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="ciru-runtime"></a>

## CIRU runtime: integrating a model-specific Strix Halo runtime

**Related project records:** [CIRU runtime](catalog.md#ciru-runtime).

- **Why build it? / 为什么另建:** Make selected Flash-Next weights and paged embeddings usable efficiently on Strix Halo without changing their artifact identity.
- **Execution ownership / 重构边界:** Modifies llama.cpp loading, embedding paging, expert execution, QSA and MTP state handling while retaining its server.
- **Retained components / 复用什么:** Credits llama.cpp, Halogen’s performance motivation and pwilkin’s open kernels; CIRU claims compatibility integration and qualification.
- **Scope given up / 取舍与兼容性:** Runtime, model and PLE files form a qualified bundle; unrelated quantizations or hosts cannot inherit its results.
- **Construction process / 怎样构建:** Release provenance pins upstream sources and documents typed-kernel adaptations, selective backports and numerical bug repairs.
- **AI participation / AI 参与的直接证据:** No verified AI authoring or task-division disclosure in reviewed sources.
- **Disclosed effort / 构建投入:** Build identities and qualification records are visible; total development and maintenance expenditure is not disclosed.
- **Validation boundary / 验证覆盖:** Keeps capacity, quality and serving checks, plus failed experiments; recent vision/MTP fixes make exact version identity essential.
- **Evolution evidence / 适配与维护:** Source, binaries and launch settings can differ across releases; rebuilding and requalification may be needed after corrective patches.

**Sources:** [Source 1](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/README.md) · [Source 2](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/docs/PROVENANCE.md) · [Source 3](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/ggml/src/ggml-cuda/qsa.cu) · [Source 4](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/docs/QSA_BACKPORT_STATUS.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="gufo-rdma"></a>

## Gufo RDMA: from one Strix Halo runtime to two-host tensor parallelism

**Related project records:** [Gufo RDMA](catalog.md#gufo-rdma).

- **Why build it? / 为什么另建:** Use two unified-memory machines for larger or higher-precision model state and shared inference work.
- **Execution ownership / 重构边界:** Adds tensor partitioning, communication and mirrored serving/snapshot transactions around Gufo’s model execution.
- **Retained components / 复用什么:** Retains Gufo’s kernels, model handling and server; uses libibverbs with existing RDMA-capable network stacks.
- **Scope given up / 取舍与兼容性:** Only Flash-Next currently has multi-host support; both ranks need matching artifacts, runtime settings and link qualification.
- **Construction process / 怎样构建:** Source separates partition rules and rank-control execution; TP2 documentation records build options, protocol checks and experiments.
- **AI participation / AI 参与的直接证据:** Not established from the reviewed source and deployment documentation.
- **Disclosed effort / 构建投入:** No total engineering effort, AI-token budget or maintenance-cost comparison with single-host Gufo is disclosed.
- **Validation boundary / 验证覆盖:** Publishes TP2-specific quality and concurrency artifacts separately from one-host tables; no independent execution here.
- **Evolution evidence / 适配与维护:** An unmerged Gufo variant must track upstream model changes, state protocols and network/toolchain compatibility together.

**Sources:** [Source 1](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/README.md) · [Source 2](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/docs/models/qwen3.8-flash-next/TP2.md) · [Source 3](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/src/models/qwen38_flash_next/distributed/tp_partition.cpp) · [Source 4](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/src/cli/serve/tp_executor.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="strix-llama-cpp"></a>

## strix-llama.cpp: a device-specific fork with an explicit upstream boundary

**Related project records:** [strix-llama.cpp](catalog.md#strix-llama-cpp).

- **Why build it? / 为什么另建:** Keep single-device optimizations usable while preserving a path for broadly applicable changes to reach upstream.
- **Execution ownership / 重构边界:** Replaces selected Vulkan/HIP kernels, fusion and speculative-state paths while retaining llama.cpp model and serving infrastructure.
- **Retained components / 复用什么:** Based on llama.cpp/GGML; credits ROCmFPX and Ciru for format implementations integrated into its backend.
- **Scope given up / 取舍与兼容性:** Hardware/shape guards limit applicability; speculative prefill and low-bit formats have different semantic effects from exact kernel changes.
- **Construction process / 怎样构建:** Separates upstream staging from device-only patches, with source-visible fused GDN and tailored dispatch decisions.
- **AI participation / AI 参与的直接证据:** The README permits coding-agent pull requests; actual authorship proportion and task allocation remain unestablished.
- **Disclosed effort / 构建投入:** Contribution and benchmark requirements are documented; total development, integration and maintenance effort are unknown.
- **Validation boundary / 验证覆盖:** Requires device measurements and runs a self-hosted gfx1151 job; this audit did not reproduce those checks.
- **Evolution evidence / 适配与维护:** Upstream merges, driver versions and imported quantization contracts must remain aligned; no universal speedup is implied.

**Sources:** [Source 1](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/README.md) · [Source 2](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/ggml/src/ggml-cuda/gated_delta_net.cu) · [Source 3](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/ggml/src/ggml-vulkan/ggml-vulkan.cpp) · [Source 4](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/CONTRIBUTING.md).

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

<a id="stable-diffusion-cpp"></a>

## stable-diffusion.cpp: an owned diffusion execution path

**Related project records:** [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp).

- **Why build it? / 为什么另建:** Run selected diffusion architectures through native C/C++ across local hardware while controlling model loading, sampling and memory placement.
- **Execution ownership / 重构边界:** Owns conditioning, diffusion, VAE and video orchestration, plus model-specific loading and execution decisions; this is an integrated runtime boundary.
- **Retained components / 复用什么:** Reuses ggml operators/device support and pretrained weights; its breadth of supported models does not remove the owned execution path.
- **Scope given up / 取舍与兼容性:** Quantization, tiled decoding and optional sample caches have distinct numerical effects; cache-enabled output changes should not be attributed to the native rewrite.
- **Construction process / 怎样构建:** Model builders and pipeline modules connect multiple components under a common engine, with architecture-gated cache and backend configuration.
- **AI participation / AI 参与的直接证据:** Not established: neither native implementation nor contemporary development establishes AI authorship or a new construction paradigm.
- **Disclosed effort / 构建投入:** Total engineering and maintenance effort is unknown; historical continuity makes this a useful within-core comparison rather than a cost-reduction claim.
- **Validation boundary / 验证覆盖:** Source and cache documentation were inspected without compiling or generating outputs; model/backend feature coverage and performance were not independently reproduced.
- **Evolution evidence / 适配与维护:** The expanding architecture matrix requires loader, conditioning, sampler and backend regressions; shared primitives reduce duplication but not integration responsibility.

**Sources:** [Source 1](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/README.md) · [Source 2](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/src/pipeline/diffusion_engine.cpp) · [Source 3](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/src/pipeline/video.cpp) · [Source 4](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/docs/caching.md).

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

<a id="edge-dit"></a>

## edge-dit.cpp: an owned diffusion execution path

**Related project records:** [edge-dit.cpp](catalog.md#edge-dit).

- **Why build it? / 为什么另建:** Fit selected diffusion models into constrained device memory while preserving explicit control over where components reside and when weights move.
- **Execution ownership / 重构边界:** Owns native model graphs, component lifecycle, graph segmentation and staged execution rather than merely attaching one offload option to a general pipeline.
- **Retained components / 复用什么:** Reuses ggml operators and device backends, pretrained checkpoints and related model conventions; native ownership does not require rewriting every primitive.
- **Scope given up / 取舍与兼容性:** Offload trades bandwidth and scheduling overhead for memory; optional precision, caching and skipped conditioning have separate semantic effects.
- **Construction process / 怎样构建:** C++ model execution is paired with graph-memory controls and CUDA staging code, with documents separating component, parameter and workspace budgets.
- **AI participation / AI 参与的直接证据:** Not established: reviewed source does not establish AI-assisted implementation, even though the runtime is deliberately specialized.
- **Disclosed effort / 构建投入:** Total development, porting and maintenance costs are unknown; reduced memory requirements do not measure construction economics.
- **Validation boundary / 验证覆盖:** Source, memory design and benchmark instructions were inspected without running inference; backend and model combinations were not independently qualified.
- **Evolution evidence / 适配与维护:** Model graphs, graph-cut boundaries and asynchronous ownership require regressions; adding architectures or devices entails rechecking both memory limits and numerical behavior.

**Sources:** [Source 1](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/README.md) · [Source 2](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/docs/optimization/memory-efficient-execution.md) · [Source 3](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/src/core/backend/ggml/cuda/ed_async_offload.cu) · [Source 4](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/benchmark/README.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="hearth"></a>

## Hearth: a Rust diffusion graph over a shared GPU layer

**Related project records:** [Hearth](catalog.md#hearth).

- **Why build it? / 为什么另建:** Provide local image generation through a native Rust program with GPU portability and inspectable model execution.
- **Execution ownership / 重构边界:** Owns SD-family conditioning, UNet, VAE, sampling and node-graph execution; external compatibility APIs are interfaces to that implementation.
- **Retained components / 复用什么:** Reuses CubeCL/wgpu and Vulkan device facilities, alongside released model weights; lower-level reuse is distinct from wrapping an existing diffusion server.
- **Scope given up / 取舍与兼容性:** The supported architecture and precision scope is limited; compatibility features and preliminary img2img behavior should not imply general feature parity.
- **Construction process / 怎样构建:** Rust model modules feed a node executor with explicit dependency ordering and cached node outputs, supported by tensor-level tests.
- **AI participation / AI 参与的直接证据:** Not established: reviewed artifacts do not identify AI contributions to model construction, debugging, porting or optimization.
- **Disclosed effort / 构建投入:** Total development effort and maintenance cost are unknown; a single-binary interface is not evidence that the implementation was inexpensive.
- **Validation boundary / 验证覆盖:** Source and tests were inspected without compiling or generating images; no independent end-to-end speed or quality claim is made.
- **Evolution evidence / 适配与维护:** Model coverage, operator correctness and device portability need continued qualification; the reviewed VRAM-budget scaffold does not establish a complete planner.

**Sources:** [Source 1](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/README.md) · [Source 2](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/src/unet/model.rs) · [Source 3](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/src/node/executor.rs) · [Source 4](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/Cargo.toml) · [Source 5](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/tests/tensor_ops.rs).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="brodiffusion"></a>

## brodiffusion: model-family pipelines and captured steps

**Related project records:** [brodiffusion](catalog.md#brodiffusion).

- **Why build it? / 为什么另建:** Provide a native implementation of selected image-generation families with explicit control over model loading and repeated denoising work.
- **Execution ownership / 重构边界:** Owns diffusion model graphs, conditioning integration, sampling and step-graph lifecycle; the reviewed image path is broader than an isolated kernel.
- **Retained components / 复用什么:** Reuses brotensor for CPU/CUDA/Metal/Vulkan operations and related text/image utilities, plus pretrained checkpoints and reference implementations.
- **Scope given up / 取舍与兼容性:** Graph replay is gated by shape and runtime state; precision modes and architectural coverage still constrain equivalence and portability.
- **Construction process / 怎样构建:** C++ pipeline modules implement the models directly, with warm-up, capture and replay logic plus reference and device-parity scripts.
- **AI participation / AI 参与的直接证据:** Not established: repository code and development artifacts do not identify a verified AI contribution or autonomous engine-construction history.
- **Disclosed effort / 构建投入:** Overall developer time, agent usage and maintenance costs are undisclosed; backend reuse cannot by itself quantify the savings.
- **Validation boundary / 验证覆盖:** Public parity harnesses were inspected but not executed; advertised family coverage is not an independently reproduced quality or performance result.
- **Evolution evidence / 适配与维护:** Model-specific loaders, backend precision and graph-capture invalidation require regression tests as checkpoints and supported execution modes evolve.

**Sources:** [Source 1](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/README.md) · [Source 2](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/src/pipeline_step_graph.cpp) · [Source 3](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/src/pipeline_qwenimage21.cpp) · [Source 4](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/scripts/qwenimage21_pipeline_parity.sh) · [Source 5](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/tests/test_device_parity.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="stable-diffusion-rs"></a>

## stable-diffusion.rs: rebuild and then move the backend

**Related project records:** [stable-diffusion.rs](catalog.md#stable-diffusion-rs).

- **Why build it? / 为什么另建:** Control diffusion-model execution in Rust and address backend limitations encountered while implementing supported image-generation paths.
- **Execution ownership / 重构边界:** Owns model graphs, sampling and weight interpretation; current MLX model code is separated from a small tensor/backend interface.
- **Retained components / 复用什么:** Reuses MLX device operations and released checkpoints; migration documents contrast the earlier Candle route with the resulting execution boundary.
- **Scope given up / 取舍与兼容性:** A backend interface cannot hide every tensor and numerical difference; portability requires more than changing a library dependency.
- **Construction process / 怎样构建:** Public design and seam documents accompany model implementations, dependency-ordered tasks and golden-reference checks for component integration.
- **AI participation / AI 参与的直接证据:** Not established: agent task specifications describe intended work but do not establish actual AI authorship or the extent of human supervision.
- **Disclosed effort / 构建投入:** Total implementation, migration and maintenance costs are unknown; architectural notes provide process evidence rather than a measured cost comparison.
- **Validation boundary / 验证覆盖:** Golden-check infrastructure and model sources were inspected; neither the migration nor end-to-end image quality was independently reproduced here.
- **Evolution evidence / 适配与维护:** Changes to tensor semantics, supported models and backend precision require new reference fixtures and checking that documentation matches the active implementation.

**Sources:** [Source 1](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/README.md) · [Source 2](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/backends.md) · [Source 3](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/seam.md) · [Source 4](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/agent-tasks/README.md) · [Source 5](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/xtask/golden/README.md) · [Source 6](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/crates/sd-models/src/mlx/flux.rs).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="saient-quartz"></a>

## Quartz: separate the native runtime from its companion

**Related project records:** [Quartz](catalog.md#saient-quartz).

- **Why build it? / 为什么另建:** Run local models on phones and desktops through a compact native runtime with explicit tensor and device behavior.
- **Execution ownership / 重构边界:** Owns Rust tensor execution, SD-family stages and committed Wan orchestration; the mobile Wan demonstration additionally uses a separate companion binary.
- **Retained components / 复用什么:** Reuses device APIs and pretrained weights; the companion video engine derives from stable-diffusion.cpp and must be attributed separately.
- **Scope given up / 取舍与兼容性:** Native reconstruction does not guarantee speed; documented native Wan limitations and reference differences prevent treating all demonstrated capabilities as one implementation.
- **Construction process / 怎样构建:** Model modules are built around a shared backend interface, with captured reference tensors and stage-level checks for the emerging video path.
- **AI participation / AI 参与的直接证据:** Not established: the reviewed artifacts do not substantiate an AI role in model reconstruction or backend optimization.
- **Disclosed effort / 构建投入:** Total development effort and maintenance cost are unknown; code size and successful demonstrations do not establish lower construction cost.
- **Validation boundary / 验证覆盖:** Source and reference workflow were reviewed without running models; mobile companion results are not independent validation of the native Rust Wan path.
- **Evolution evidence / 适配与维护:** Maintaining multiple device backends and the companion/native boundary requires model-stage parity checks and accurate capability documentation as integration evolves.

**Sources:** [Source 1](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/README.md) · [Source 2](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/src/sdxl_pipeline.rs) · [Source 3](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/src/wan_pipeline.rs) · [Source 4](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/reference/README.md) · [Source 5](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/Cargo.toml).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="lightx2v"></a>

## LightX2V: an owned diffusion execution path

**Related project records:** [LightX2V](catalog.md#lightx2v).

- **Why build it? / 为什么另建:** Execute large supported generative models under accelerator-memory and latency constraints through model-aware runtime policies.
- **Execution ownership / 重构边界:** Owns model-specific inference and operator storage contracts, plus planned weight layouts, prefetch streams and two-slot device buffers.
- **Retained components / 复用什么:** Reuses PyTorch/device stream facilities, pretrained checkpoints and selectable kernel implementations; the owned backend extends beyond a collection of wrappers.
- **Scope given up / 取舍与兼容性:** Offload changes data placement; quantization, caching, distillation and lightweight VAEs can change outputs and require separate attribution.
- **Construction process / 怎样构建:** Loader plans verify storage views and checkpoint coverage, while the asynchronous manager sequences transfers, initialization and buffer swapping.
- **AI participation / AI 参与的直接证据:** Not established: public implementation and optimization breadth do not identify an AI contribution to building the runtime.
- **Disclosed effort / 构建投入:** Total development and maintenance costs are undisclosed; maximum reported speedups do not quantify construction effort.
- **Validation boundary / 验证覆盖:** Source and benchmark guidance were inspected without execution; contiguous offload explicitly rejects combinations such as graph capture, caching or multi-rank execution.
- **Evolution evidence / 适配与维护:** New operator layouts, devices and acceleration combinations need contract checks and numerical regressions; configuration compatibility is part of the implementation burden.

**Sources:** [Source 1](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/README.md) · [Source 2](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/lightx2v/common/offload/manager.py) · [Source 3](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/lightx2v/common/offload/block_loader.py) · [Source 4](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/docs/EN/source/getting_started/benchmark.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="vidax"></a>

## Vidax: move video-model execution onto TPU meshes

**Related project records:** [Vidax](catalog.md#vidax).

- **Why build it? / 为什么另建:** Run selected video-generation architectures on TPUs with model-aware distributed execution rather than retaining a GPU-centric reference pipeline.
- **Execution ownership / 重构边界:** Owns model implementations, checkpoint translation, samplers and sharding decisions, while compiled primitives and collectives remain in the JAX stack.
- **Retained components / 复用什么:** Reuses JAX/Flax, Pallas kernels and original checkpoints; reference implementations provide the semantic target for translated models.
- **Scope given up / 取舍与兼容性:** Tensor/sequence parallelism and offload impose device-mesh constraints; precision decisions can change output quality independently of partitioning.
- **Construction process / 怎样构建:** Ports are built through explicit weight mapping and model modules, with debugging records documenting failures and fixes in Wan precision handling.
- **AI participation / AI 参与的直接证据:** Not established: the reviewed sources do not demonstrate what AI contributed to porting or performance tuning.
- **Disclosed effort / 构建投入:** Total engineering and maintenance cost are unknown; compile or inference timings do not measure the effort of constructing a port.
- **Validation boundary / 验证覆盖:** Benchmark instructions and numerical debugging evidence were inspected without running TPUs; author results remain specific to tested model/device configurations.
- **Evolution evidence / 适配与维护:** New architectures and mesh layouts require conversion, numerical and performance checks; intermediate casting bugs illustrate the maintenance cost of backend migration.

**Sources:** [Source 1](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/README.md) · [Source 2](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/core/attention.py) · [Source 3](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/core/sharding.py) · [Source 4](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/models/wan/wan2_1/dit.py) · [Source 5](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/docs/lessons/wan2_1_debugging.md) · [Source 6](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/docs/benchmarking.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="telefuser"></a>

## TeleFuser: model pipelines plus stateful stream scheduling

**Related project records:** [TeleFuser](catalog.md#telefuser).

- **Why build it? / 为什么另建:** Serve interactive generative workloads whose retained state, queue growth and execution scheduling differ from independent offline generation jobs.
- **Execution ownership / 重构边界:** Owns model pipelines and denoising stages; the inspected LingBot streaming service adds actor dataflow, backpressure, session ordering and resource-group execution leases.
- **Retained components / 复用什么:** Reuses PyTorch, selected Triton/attention components, pretrained models and transport services; transport is separate from model execution.
- **Scope given up / 取舍与兼容性:** LingBot session residency is separate from GPU execution leases; other services may choose different policies. Optional quantization, sparse attention and caching require explicit quality attribution.
- **Construction process / 怎样构建:** Model-stage interfaces and streaming-scheduler contracts connect project-owned pipeline implementations to session control and benchmark tooling.
- **AI participation / AI 参与的直接证据:** Not established: AI-oriented development documentation does not identify the AI contribution to the inspected implementation.
- **Disclosed effort / 构建投入:** Total developer effort, agent use and maintenance cost are not disclosed; serving capacity or delivered FPS cannot quantify construction cost.
- **Validation boundary / 验证覆盖:** Source and scheduler/benchmark documents were inspected only; delivery FPS, model compute throughput and end-to-end latency must be measured separately.
- **Evolution evidence / 适配与维护:** New stateful models require correct reset, cancellation, ordering and memory contracts, plus qualification of backend and acceleration combinations.

**Sources:** [Source 1](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/README.md) · [Source 2](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/docs/en/stream_scheduler.md) · [Source 3](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/telefuser/pipelines/wan_video/single_dit_denoising.py) · [Source 4](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/telefuser/pipelines/wan_video/wan21_video.py) · [Source 5](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/benchmarks/telefuser_aiperf/README.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="fastvideo"></a>

## FastVideo: an owned diffusion execution path

**Related project records:** [FastVideo](catalog.md#fastvideo).

- **Why build it? / 为什么另建:** Integrate supported video architectures into a controllable inference runtime with explicit loading, placement, attention and parallel-execution choices.
- **Execution ownership / 重构边界:** Owns model implementations, registries, component loaders and staged denoising; training and distillation workflows are distinct from this inference boundary.
- **Retained components / 复用什么:** Reuses tensor backends, model weights and selected kernels while replacing substantial pipeline and execution organization.
- **Scope given up / 取舍与兼容性:** Sparse attention and distilled checkpoints can change outputs; backend precision and scheduling also require model-specific qualification.
- **Construction process / 怎样构建:** Model/config/pipeline registries resolve checkpoints into project-owned model classes, whose stages implement loading and denoising with architecture-specific numerical policies.
- **AI participation / AI 参与的直接证据:** Not established: the reviewed runtime documentation does not substantiate an AI contribution to implementation or integration.
- **Disclosed effort / 构建投入:** Total construction and maintenance effort is unknown; training and inference performance metrics cannot substitute for those measurements.
- **Validation boundary / 验证覆盖:** Architecture, source and performance-benchmark guidance were inspected without running models; reported gains are not independently reproduced and must separate model changes.
- **Evolution evidence / 适配与维护:** Expanding model families requires keeping registry/configuration behavior, precision exceptions and attention backends consistent, with end-to-end regression coverage.

**Sources:** [Source 1](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/README.md) · [Source 2](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/docs/inference/architecture.md) · [Source 3](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/fastvideo/pipelines/stages/denoising.py) · [Source 4](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/docs/contributing/performance_benchmarks.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="minimax-h3-mlx"></a>

## MiniMax-H3 MLX: reconstruct joint audio/video diffusion

**Related project records:** [MiniMax-H3 MLX](catalog.md#minimax-h3-mlx).

- **Why build it? / 为什么另建:** Execute MiniMax-H3 on Apple Silicon by rebuilding its joint diffusion pipeline rather than treating it as an autoregressive language-model conversion.
- **Execution ownership / 重构边界:** Owns packed video/audio geometry, conditioning, DiT, samplers and both VAEs; model-specific AdaLN precomputation changes execution and residency.
- **Retained components / 复用什么:** Reuses MLX primitives, pretrained checkpoints and the official diffusers reference for conversion and parity checks.
- **Scope given up / 取舍与兼容性:** Weight quantization reduces memory but does not remove dense-attention work; keyframe sampling and floating-point details can differ from the reference.
- **Construction process / 怎样构建:** The port implements individual stages and loaders, then compares geometry, scheduling, component outputs and integrated generation against reference artifacts.
- **AI participation / AI 参与的直接证据:** Not established: reviewed public evidence does not identify an AI role in construction, debugging or optimization.
- **Disclosed effort / 构建投入:** Total porting effort and maintenance cost are undisclosed; runtime measurements and model-size reductions are not development-cost evidence.
- **Validation boundary / 验证覆盖:** Author parity tests and text-conditioned generation reports were inspected; keyframe inference has a narrower validation boundary, and no independent run was performed.
- **Evolution evidence / 适配与维护:** Upstream checkpoint layouts, scheduler rounding and modality packing require careful regression checks; successful execution alone does not imply practical generation latency.

**Sources:** [Source 1](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/README.md) · [Source 2](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/minimax_h3_mlx/pipeline.py) · [Source 3](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/minimax_h3_mlx/adaln.py) · [Source 4](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/tests/test_dit_parity.py) · [Source 5](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/tests/test_text_encoder_parity.py) · [Source 6](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/reference/README.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="streamdiffusion-v2"></a>

## StreamDiffusionV2: causal video state across chunks and GPUs

**Related project records:** [StreamDiffusionV2](catalog.md#streamdiffusion-v2).

- **Why build it? / 为什么另建:** Reduce streaming video latency by matching execution to causal generation rather than repeatedly invoking a complete offline video pipeline.
- **Execution ownership / 重构边界:** Owns chunk encode/denoise/decode flow, streaming state and distributed cache ownership; the source includes cache transfer when stage ownership changes.
- **Retained components / 复用什么:** Reuses PyTorch, Wan-derived causal models and CausVid/Self-Forcing components, with optional lightweight decoding and external integration.
- **Scope given up / 取舍与兼容性:** Distilled causal checkpoints and decoder choices can alter output quality; reported systems gains must be separated from changes to the model.
- **Construction process / 怎样构建:** The staged API is backed by single-device and pipeline implementations, cache-management modules and video-metric tooling.
- **AI participation / AI 参与的直接证据:** Not established: reviewed materials do not identify AI participation in constructing or tuning this execution path.
- **Disclosed effort / 构建投入:** Total implementation and maintenance cost are unknown; paper latency results are not a measure of engineering effort.
- **Validation boundary / 验证覆盖:** Source and evaluation entry points were inspected without GPU execution; roadmap items are not treated as completed features, and reported results were not reproduced.
- **Evolution evidence / 适配与维护:** Chunk position, cache ownership, reset behavior and model-version compatibility require regressions; integrations such as Scope are adopters, not additional engine records.

**Sources:** [Source 1](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/README.md) · [Source 2](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamdiffusionv2/pipeline.py) · [Source 3](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamv2v/inference_pipe.py) · [Source 4](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamv2v/communication/kv_cache_manager.py) · [Source 5](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/tools/eval_video_metrics.py).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="aria"></a>

## Aria: an AI-assisted native audio diffusion runtime

**Related project records:** [Aria](catalog.md#aria).

- **Why build it? / 为什么另建:** Execute and inspect Stable Audio 3 locally without a Python model framework, including access to intermediate generation state.
- **Execution ownership / 重构边界:** Owns text conditioning, diffusion-model execution, noise schedule, sampling and waveform decoding; this is a complete audio-generation artifact.
- **Retained components / 复用什么:** Reuses released weights and platform vector/OpenMP facilities; optional CUDA execution uses GPU libraries rather than eliminating all external components.
- **Scope given up / 取舍与兼容性:** Weight quantization and steering intentionally alter numerical behavior; those changes must be separated from native implementation and memory placement.
- **Construction process / 怎样构建:** C model modules and sampler are checked through dumped reference tensors, injected noise and an end-to-end latent/audio comparison harness.
- **AI participation / AI 参与的直接证据:** Disclosed: the README states substantial LLM assistance with human-led ideas, testing and debugging; autonomous authorship is not established.
- **Disclosed effort / 构建投入:** Total human effort, token usage, compute cost and maintenance expenditure are undisclosed; the disclosure does not establish reduced total cost.
- **Validation boundary / 验证覆盖:** Public parity tests compare controlled paths to the reference; they were inspected but not run, and do not validate every quantized generation.
- **Evolution evidence / 适配与维护:** Checkpoint variants, tokenizer exports, precision modes and CPU/CUDA paths need continued reference checks and independent audio-quality assessment.

**Sources:** [Source 1](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/README.md) · [Source 2](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/src/aria_model_sa3.c) · [Source 3](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/src/aria_sampler.c) · [Source 4](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/tests/test_e2e.c) · [Source 5](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/BENCHMARKS.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="qwen-asr-c"></a>

## Qwen-ASR: native speech preprocessing and decoding

**Related project records:** [Qwen-ASR (C)](catalog.md#qwen-asr-c).

- **Why build it? / 为什么另建:** Run the selected ASR family locally without carrying a Python model framework, while exposing CPU and accelerator execution choices.
- **Execution ownership / 重构边界:** Owns waveform preprocessing, encoder graph, decoder prompt construction and incremental transcription; serving interfaces sit outside that model boundary.
- **Retained components / 复用什么:** Reuses pretrained Qwen weights, CPU BLAS/vector facilities and optional CUDA/cuBLAS or ROCm libraries; native implementation does not mean dependency-free.
- **Scope given up / 取舍与兼容性:** Chunk rollback and context windows affect streaming behavior; reduced-precision GPU paths need separate qualification from ordinary graph implementation.
- **Construction process / 怎样构建:** C modules implement the stages directly, with a Python regression harness and a model description for reference comparisons.
- **AI participation / AI 参与的直接证据:** Not established: the reviewed implementation and documentation do not establish what AI contributed to architecture, coding or debugging.
- **Disclosed effort / 构建投入:** Total implementation effort, agent tokens, compute expenditure and maintenance cost are not disclosed in the reviewed sources.
- **Validation boundary / 验证覆盖:** Transcription regression machinery is public; this audit inspected source without compiling, running models or independently reproducing accuracy and latency.
- **Evolution evidence / 适配与维护:** Checkpoint layouts, tokenization, streaming boundaries and device kernels each require regression coverage when the supported family evolves.

**Sources:** [Source 1](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/README.md) · [Source 2](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/qwen_asr.c) · [Source 3](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/qwen_asr_encoder.c) · [Source 4](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/asr_regression.py) · [Source 5](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/MODEL.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="vla-simd"></a>

## vla.simd: CPU-native action-model execution

**Related project records:** [vla.simd](catalog.md#vla-simd).

- **Why build it? / 为什么另建:** Run selected vision-language-action policies on CPU hardware without requiring a GPU tensor framework for the inference path.
- **Execution ownership / 重构边界:** Owns tensor operators, model adapters, weight loading and action computation; Python robot integration remains outside that native execution boundary.
- **Retained components / 复用什么:** Reuses pretrained policy weights, GGUF conventions and architecture facilities such as AVX2, NEON and Apple Accelerate where selected.
- **Scope given up / 取舍与兼容性:** Quantization and precision change numerical behavior; actions produced per second are not automatically the frequency of an effective closed-loop controller.
- **Construction process / 怎样构建:** Model adapters target a shared native operator layer with architecture-specific kernels, plus conversion and parity-check tools against reference implementations.
- **AI participation / AI 参与的直接证据:** Not established: documentation and source do not substantiate AI participation in implementing or validating the runtime.
- **Disclosed effort / 构建投入:** Total engineering effort, agent costs and maintenance burden are unknown, despite public per-device benchmark and development records.
- **Validation boundary / 验证覆盖:** Reviewed benchmark notes include fixed-input numerical checks; no robot experiment or independent inference run was performed in this audit.
- **Evolution evidence / 适配与维护:** Adding policies requires matching preprocessing, action normalization and operator semantics, followed by numerical and task-level requalification on each device.

**Sources:** [Source 1](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/README.md) · [Source 2](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/src/hal/arch.h) · [Source 3](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/src/nn/linear.cpp) · [Source 4](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/docs/development.md) · [Source 5](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/docs/benchmark/intel-core-ultra-9-285k.md) · [Source 6](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/tools/check_model_parity.py).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="qwen3-tts-c"></a>

## Qwen3-TTS: rebuild the talker-to-waveform path

**Related project records:** [Qwen3-TTS (C)](catalog.md#qwen3-tts-c).

- **Why build it? / 为什么另建:** Make the selected speech family executable as a local native engine with explicit control over decoding and backend overhead.
- **Execution ownership / 重构边界:** Owns talker, residual code prediction, speech decoding and streaming integration; these are model execution components rather than an API wrapper.
- **Retained components / 复用什么:** Reuses pretrained weights, platform BLAS/Accelerate facilities and selected low-level libraries while implementing the synthesis stages in C.
- **Scope given up / 取舍与兼容性:** Precision choices and streaming segmentation need separate qualification; a faster substage does not establish equivalent perceptual quality end to end.
- **Construction process / 怎样构建:** Public pipeline and engineering documents organize reference checks, task records, dispatch decisions and corrections to earlier benchmark attribution.
- **AI participation / AI 参与的直接证据:** Not established: agent-oriented task instructions describe a workflow but do not identify actual AI-authored changes or their supervision.
- **Disclosed effort / 构建投入:** Overall human effort, agent usage and maintenance costs are undisclosed; profiling evidence is not a development-cost measurement.
- **Validation boundary / 验证覆盖:** Source and documented reference methodology were reviewed; reported measurements remain author evidence and were not reproduced by this audit.
- **Evolution evidence / 适配与维护:** Backend dispatch and model-stage regressions need repeated qualification; the documented measurement corrections illustrate the burden of maintaining reliable comparisons.

**Sources:** [Source 1](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/README.md) · [Source 2](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/qwen_tts_talker.c) · [Source 3](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/docs/pipeline.md) · [Source 4](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/docs/ENGINEERING-METHOD.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="qingming-qwen3-tts"></a>

## Qingming Qwen3-TTS: two explicit device contracts

**Related project records:** [Qingming Qwen3-TTS](catalog.md#qingming-qwen3-tts).

- **Why build it? / 为什么另建:** Specialize the complete Qwen3-TTS path for two named consumer GPUs rather than abstracting every accelerator behind one general implementation.
- **Execution ownership / 重构边界:** Owns device operators, model sequencing, memory capacities and resident generation/decoder scheduling for the supported model sizes.
- **Retained components / 复用什么:** Reuses pretrained model weights and HIP/CUDA platform facilities; the documented NVIDIA operator path avoids a framework and BLAS dependency.
- **Scope given up / 取舍与兼容性:** Fixed GPU and capacity assumptions give up general portability; chunk schedules and precision must be included when comparing speech behavior.
- **Construction process / 怎样构建:** A written contract separates Once and Resident modes, while device-specific sources and a benchmark harness make those execution choices inspectable.
- **AI participation / AI 参与的直接证据:** Not established: source availability and engineering contracts do not identify whether AI assisted design, implementation, debugging or tuning.
- **Disclosed effort / 构建投入:** Total development and maintenance effort are unknown; a narrowly targeted implementation alone is not evidence that building it was cheaper.
- **Validation boundary / 验证覆盖:** Authors describe device-local codec/WAV agreement and benchmarks; this audit reviewed artifacts without executing either GPU implementation or checking speech quality.
- **Evolution evidence / 适配与维护:** Porting to another GPU requires revisiting kernel shapes, capacity assumptions and concurrency partitions, then requalifying the complete synthesis path.

**Sources:** [Source 1](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/README.md) · [Source 2](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/CONTRACT.md) · [Source 3](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/devices/rtx4090-24g/qwen3_tts_0_6b.cu) · [Source 4](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/devices/rtx4090-24g/benchmark.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="voxgen"></a>

## VoxGen: native Vulkan speech synthesis

**Related project records:** [VoxGen](catalog.md#voxgen).

- **Why build it? / 为什么另建:** Run the selected speech model locally with explicit GPU resource control and a separate tuned path for the RX 7900 XTX.
- **Execution ownership / 重构边界:** Owns language/acoustic stages, audio decoding, request state and incremental PCM production, plus Vulkan memory and shader dispatch.
- **Retained components / 复用什么:** Reuses pretrained VoxCPM2 weights and the Vulkan API through ash; model execution is not delegated to an existing Python inference service.
- **Scope given up / 取舍与兼容性:** Quantized language weights, floating-point acoustic paths and hardware-specific shader profiles need distinct quality and performance qualification.
- **Construction process / 怎样构建:** Rust modules assemble the model stages and streaming lifecycle; public history and smoke scripts expose integration and validation work.
- **AI participation / AI 参与的直接证据:** Not established: the reviewed repository does not substantiate an AI contribution to the implementation or its optimization decisions.
- **Disclosed effort / 构建投入:** Build effort, agent expenditure and long-term maintenance cost are undisclosed; runtime throughput cannot substitute for those measurements.
- **Validation boundary / 验证覆盖:** Source and smoke-test entry points were inspected, without running inference; author measurements do not establish perceptual parity across voices and devices.
- **Evolution evidence / 适配与维护:** Driver behavior, shader capabilities, cancellation and streaming-state handling need continuing regression checks as device profiles and models change.

**Sources:** [Source 1](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/README.md) · [Source 2](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/src/runtime.rs) · [Source 3](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/src/vulkan.rs) · [Source 4](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/build_linux/smoke_pipeline_f16.sh).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="parakeet-ggml"></a>

## parakeet.cpp (ggml): port model and streaming semantics

**Related project records:** [parakeet.cpp (ggml)](catalog.md#parakeet-ggml).

- **Why build it? / 为什么另建:** Deploy supported NeMo speech models through a native, portable runtime with batch and streaming interfaces.
- **Execution ownership / 重构边界:** Owns model loading, FastConformer execution, CTC/transducer decoding and streaming session state, beyond binding to an existing speech service.
- **Retained components / 复用什么:** Reuses ggml device backends, pretrained checkpoints and NeMo as the reference implementation; conversion supplies model-specific GGUF metadata.
- **Scope given up / 取舍与兼容性:** Quantization and limited-context streaming require separate checks from the full-precision offline path; output agreement depends on model and decoding settings.
- **Construction process / 怎样构建:** Native model code is paired with conversion, batching documentation and a detailed parity report covering intermediate tensors and transcription fixtures.
- **AI participation / AI 参与的直接证据:** Not established: source and test artifacts do not establish AI participation in porting or debugging the runtime.
- **Disclosed effort / 构建投入:** Total construction effort and maintenance cost are unknown; neither code volume nor the number of supported checkpoints answers that question.
- **Validation boundary / 验证覆盖:** Reported NeMo comparisons are fixture-bound and author-run; model-dependent tests may skip without weights, and no models were run in this audit.
- **Evolution evidence / 适配与维护:** Checkpoint metadata, language conditioning and end-of-utterance behavior require explicit regressions, especially when extending cache-aware streaming support.

**Sources:** [Source 1](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/README.md) · [Source 2](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/src/model.cpp) · [Source 3](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/docs/parity.md) · [Source 4](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/docs/batching.md).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

<a id="parakeet-axiom"></a>

## parakeet.cpp (axiom): a different native ASR boundary

**Related project records:** [parakeet.cpp (axiom)](catalog.md#parakeet-axiom).

- **Why build it? / 为什么另建:** Bring Parakeet speech inference into native C++ with an Apple accelerator path and a CPU fallback.
- **Execution ownership / 重构边界:** Owns FastConformer modules, decoder integration and cache-aware convolution/attention; it is separate from the similarly named ggml implementation.
- **Retained components / 复用什么:** Reuses axiom tensor operations, MPSGraph/Metal and pretrained NeMo weights converted into the runtime format.
- **Scope given up / 取舍与兼容性:** Floating-point mode and streaming context affect comparisons; retaining a tensor backend avoids rebuilding every primitive but preserves its device constraints.
- **Construction process / 怎样构建:** Native model and streaming modules expose explicit cache updates, with conversion instructions and a public test suite for integration.
- **AI participation / AI 参与的直接证据:** Not established: reviewed source and documentation do not identify AI-authored components or a measured agent-driven construction process.
- **Disclosed effort / 构建投入:** Total porting time, developer effort and ongoing maintenance cost are not disclosed in the reviewed evidence.
- **Validation boundary / 验证覆盖:** The prominent encoder benchmark uses synthetic inputs and excludes the full transcription path; source inspection here is not an independent accuracy or speed reproduction.
- **Evolution evidence / 适配与维护:** Model conversion, backend/compiler requirements and cached/offline behavior need requalification when checkpoints, macOS toolchains or axiom interfaces change.

**Sources:** [Source 1](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/README.md) · [Source 2](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/src/models/encoder.cpp) · [Source 3](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/src/models/streaming_encoder.cpp) · [Source 4](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/tests/test_all.cpp).

**Reviewed:** 2026-10-12. See the linked project record for mechanism-specific caveats.

