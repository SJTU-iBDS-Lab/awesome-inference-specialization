# Awesome Inference Specialization

**Specialized inference execution stacks built for particular models, hardware and workloads—with a focus on whether AI-assisted development and code generation change how they are implemented, optimized and maintained.**

[中文](README_CN.md) · [Core cases](docs/cases.md) · [Construction comparison](docs/comparison.md) · [Survey library](docs/systems.md) · [Model domains](docs/domains.md) · [Research questions](docs/research-agenda.md) · [Contribute](CONTRIBUTING.md)

## Why this repository?

Specialized inference systems are not new. The question is **whether their construction methods, accessibility and economics are changing—and which system designs become practical as a result.**

We study systems that reclaim control of model execution through direct implementation, substantial adaptation or generated code, together with the workflows that build them. This can include the model graph, kernel dispatch, state, data movement or request execution while retaining shared services and lower-level libraries.

The cases help investigate an unproven causal chain:

> AI-assisted coding or code generation may lower implementation and revision costs → some narrowly targeted execution stacks may become worth building → feasible system designs and delivery practices may change.

**A faster engine, a short development period or the use of an agent does not establish that chain.** Record the motivation, reconstruction and reuse boundary, compatibility given up, actual AI participation, disclosed effort, and missing validation or maintenance evidence.

![Known deployment constraints lead to rebuilt execution decisions, construction and validation, then deployment and maintenance, compared with historical routes and shared foundations](assets/specialization.svg)

## Start with the core cases

<!-- CATALOG-START -->

**[Full directory: 161 projects](docs/systems.md) · [Selected analyses: 63 cases](docs/cases.md)**

Follow the construction process to its resulting system, then examine reuse boundaries and missing evidence. These groups guide reading; AI involvement does not imply better results, and missing disclosure does not imply human-only implementation.

[Multimodal understanding & interaction](docs/domains.md#multimodal) · [Image generation & processing](docs/domains.md#image) · [Video generation & processing](docs/domains.md#video) · [Speech & audio](docs/domains.md#audio) · [Language models](docs/domains.md#text) · [Cross-domain infrastructure](docs/domains.md#general)

Modalities are overlapping search facets, not construction categories. Each group shows three entry points; expand for the remaining cases, all retained in the case index.

### Construction workflows and generated execution

| Case | Why study it? |
| --- | --- |
| [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) | An author-reported experiment adapted MetaInfer and reused existing kernels to build a deployment-specific Qwen serving stack. |
| [Sol-Engine](docs/cases.md#sol-engine) | An agent-oriented workflow assembles model-specific video execution paths from reusable optimizations and measured quality constraints. |
| [Mirage MPK](docs/cases.md#mirage) | A compiler/runtime turns an assembled LLM task graph into persistent GPU execution spanning computation and communication. |

<details>
<summary>Show 2 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [Lithos Metal](docs/cases.md#lithos-metal) | A standalone compiler/runtime turns selected model graphs into Apple-specific execution programs. |
| [Magnitude](docs/cases.md#magnitude) | The reviewed Metal path captures typed operations and constructs specialized fused kernels inside MLX’s execution machinery. |

</details>

### Native runtimes for qualified models and devices

| Case | Why study it? |
| --- | --- |
| [Splash](docs/cases.md#splash) | Integrates a matched draft, specialized kernels and memory policy into a local Apple-silicon serving stack. |
| [Gufo](docs/cases.md#gufo) | A native C++/HIP engine chooses a narrow hardware target and selected models, owning execution, state and serving while adapting existing components. |
| [zLLM](docs/cases.md#zllm) | Reimplements model-specific visual and generative pipelines inside a native runtime with explicit backend limits. |

<details>
<summary>Show 16 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [NInfer](docs/cases.md#ninfer) | Owns model execution, state and serving within a deliberately narrow checkpoint and GPU contract. |
| [Lily](docs/cases.md#lily) | A narrowly qualified Rust/Metal engine exposes the compatibility decisions made when rebuilding model execution. |
| [hipEngine](docs/cases.md#hipengine) | torch-free model execution for selected Radeon targets |
| [imp](docs/cases.md#imp) | an explicitly agent-built stack for consumer Blackwell |
| [VTE](docs/cases.md#vte) | a measured RDNA3 runtime with generated HIP kernels |
| [ZINC](docs/cases.md#zinc) | a Zig stack built around consumer GPU execution |
| [memra](docs/cases.md#memra) | a Rust/CUDA engine qualified one hardware lane at a time |
| [Kipp](docs/cases.md#kipp) | a checkpoint-bounded C11 Qwen execution stack |
| [Saragossa](docs/cases.md#saragossa) | A Rust/Metal engine concentrates on local latency and controlled model-state lifetimes. |
| [TensorFold](docs/cases.md#tensorfold) | A Zig server admits explicit model–format–platform combinations and executes their native Metal or CUDA paths. |
| [Halogen Flash](docs/cases.md#halogen-flash) | A distributed binary targets one Qwen family and AMD Strix Halo, with public deployment and quantization descriptions. |
| [ExLlamaV3](docs/cases.md#exllamav3) | A local-inference library couples EXL3 encoding, quantized state and qualified execution paths for consumer GPUs. |
| [Llaminar](docs/cases.md#llaminar) | constructing native execution plans for mixed hardware |
| [ane.cpp](docs/cases.md#ane-cpp) | An ANE-LM fork uses empirical hardware probes to guide runtime fusion, chunking and dispatch changes. |
| [Cactus](docs/cases.md#cactus) | Connects model capture and graph lowering to a mobile stack that owns quantization, state and execution. |
| [FastFlowLM](docs/cases.md#fastflowlm) | Builds around AMD NPU execution with separate model, kernel-provider and device boundaries. |

</details>

### Rebuilding around memory and expert placement

| Case | Why study it? |
| --- | --- |
| [Flash-MoE](docs/cases.md#flash-moe) | A fixed-model C/Metal prototype streams expert weights from SSD and controls the execution pipeline directly. |
| [Strata](docs/cases.md#strata) | A Qwen-specific runtime combines GPU-resident work with CPU expert execution and explicit memory budgets. |
| [Swiftlet](docs/cases.md#swiftlet) | A native Qwen hybrid-MoE runtime makes model format, streaming and device limits explicit. |

<details>
<summary>Show 6 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [DwarfStar](docs/cases.md#dwarfstar) | A native stack integrates selected model paths, state management and local serving around consumer-hardware constraints. |
| [TurboFieldfare](docs/cases.md#turbo-fieldfare) | A Gemma-specific Swift/Metal runtime makes storage and execution policy part of the same design. |
| [TUFF](docs/cases.md#tuff) | A substantive TurboFieldfare fork retains bounded streaming while adding model-specific execution paths. |
| [SwiftLM](docs/cases.md#swiftlm) | SwiftLM retains MLX while changing expert I/O, scheduling and error handling for oversized MoE inference. |
| [Colibri](docs/cases.md#colibri) | A collection of architecture-specific C engines treats expert residency and model execution as explicit design responsibilities. |
| [KTransformers](docs/cases.md#ktransformers) | A specialized heterogeneous backend uses CPU capacity and instruction sets for MoE experts while retaining GPU serving components. |

</details>

### Substantial forks and specialized backends

| Case | Why study it? |
| --- | --- |
| [llamAmpere](docs/cases.md#llamampere) | A deep llama.cpp fork integrates MTP verification, compressed KV state and SM86 execution for local long-context Qwen inference. |
| [vLLM Radiance](docs/cases.md#vllm-radiance) | a qualified RDNA4 backend inside a pinned vLLM stack |
| [ANEMLL Flash llama.cpp](docs/cases.md#anemll-flash-llama) | A specialized fork retains a general engine while rebuilding routed-expert storage and execution handoffs. |

<details>
<summary>Show 5 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [NInfer-3090](docs/cases.md#ninfer-3090) | retargeting NInfer to Ampere’s kernels and memory budget |
| [Infernix](docs/cases.md#infernix) | extending NInfer across GPU, CPU and NVMe tiers |
| [CIRU runtime](docs/cases.md#ciru-runtime) | integrating a model-specific Strix Halo runtime |
| [Gufo RDMA](docs/cases.md#gufo-rdma) | from one Strix Halo runtime to two-host tensor parallelism |
| [strix-llama.cpp](docs/cases.md#strix-llama-cpp) | a device-specific fork with an explicit upstream boundary |

</details>

### Reconstructing image-generation pipelines

| Case | Why study it? |
| --- | --- |
| [Iris](docs/cases.md#iris) | A C image-generation pipeline replaces framework-level execution for selected architectures while retaining platform acceleration. |
| [stable-diffusion.cpp](docs/cases.md#stable-diffusion-cpp) | A cross-backend native implementation reconstructs full diffusion pipelines and their component lifecycles. |
| [Nunchaku](docs/cases.md#nunchaku) | A low-bit diffusion backend co-designs packed weights and fused execution so the outlier-correction branch remains affordable. |

<details>
<summary>Show 5 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [edge-dit.cpp](docs/cases.md#edge-dit) | A native diffusion runtime controls the model graph and memory lifecycle over shared ggml primitives. |
| [Hearth](docs/cases.md#hearth) | A native image pipeline owns model graphs and node scheduling while reusing CubeCL and wgpu. |
| [brodiffusion](docs/cases.md#brodiffusion) | C++ model pipelines reuse a tensor backend while owning sampler integration and denoiser graph replay. |
| [stable-diffusion.rs](docs/cases.md#stable-diffusion-rs) | A Rust diffusion implementation documents the interface and numerical work needed to migrate its execution backend. |
| [Quartz](docs/cases.md#saient-quartz) | The repository exposes a Rust image stack and developing native video path, alongside a distinct production companion. |

</details>

### Video execution, device migration and streaming

| Case | Why study it? |
| --- | --- |
| [LightX2V](docs/cases.md#lightx2v) | A shared-framework runtime owns model execution and explicit asynchronous weight-storage contracts. |
| [Vidax](docs/cases.md#vidax) | JAX model ports and sharding policies make the device migration boundary explicit. |
| [TeleFuser](docs/cases.md#telefuser) | A workload-specific runtime connects generative model stages to bounded, session-aware execution. |

<details>
<summary>Show 3 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [FastVideo](docs/cases.md#fastvideo) | A model-aware video runtime rebuilds component resolution and denoising execution on shared tensor backends. |
| [MiniMax-H3 MLX](docs/cases.md#minimax-h3-mlx) | A full MLX model port exposes exact precomputation opportunities and the remaining dense-attention limit. |
| [StreamDiffusionV2](docs/cases.md#streamdiffusion-v2) | Streaming video execution owns chunk boundaries, denoising arrangement and distributed KV-cache movement. |

</details>

### Speech, audio diffusion and action-model runtimes

| Case | Why study it? |
| --- | --- |
| [Aria](docs/cases.md#aria) | The author explicitly reports LLM assistance while the repository exposes the resulting C execution path and parity harness. |
| [Qwen-ASR](docs/cases.md#qwen-asr-c) | A model-family C implementation owns the complete ASR execution path, including streaming policy. |
| [vla.simd](docs/cases.md#vla-simd) | The runtime rebuilds selected robot-policy model paths around CPU SIMD execution. |

<details>
<summary>Show 5 more cases in this group</summary>

| Case | Why study it? |
| --- | --- |
| [Qwen3-TTS](docs/cases.md#qwen3-tts-c) | Native synthesis modules are paired with an explicit engineering and measurement workflow. |
| [Qingming Qwen3-TTS](docs/cases.md#qingming-qwen3-tts) | Two fixed consumer GPU targets receive distinct native synthesis implementations and concurrency policies. |
| [VoxGen](docs/cases.md#voxgen) | A Rust runtime connects VoxCPM2 model stages to directly managed Vulkan execution. |
| [parakeet.cpp (ggml)](docs/cases.md#parakeet-ggml) | The NeMo-to-ggml port carries model-specific state and documents the limits of its reference comparisons. |
| [parakeet.cpp (axiom)](docs/cases.md#parakeet-axiom) | A separate C++ port uses axiom and MPSGraph while owning cached speech-model execution. |

</details>

### Compare the cases with existing routes

- [Historical and adjacent routes](docs/systems.md#adjacent): ZeRO-Inference, FlexGen, DistServe, S-LoRA and MLC LLM help establish which ideas already exist.
- [Shared foundations and baselines](docs/systems.md#foundation): general engines, compilers, kernels and evaluators reveal what is reused and what a fair comparison requires.

Relevance describes a record’s role in this survey, not its quality, maturity or age. The full [library](docs/systems.md) retains the broader collection.

<details>
<summary>按执行机制检索资料库 / Browse the library by execution mechanism</summary>

[Data residency & movement](docs/catalog.md#memory) · [Numerical representation](docs/catalog.md#precision) · [Selective computation](docs/catalog.md#selection) · [Computation reuse](docs/catalog.md#reuse) · [Generation order](docs/catalog.md#decoding) · [Parallelism & scheduling](docs/catalog.md#serving) · [Compiled & native execution](docs/catalog.md#execution) · [Construction & validation tools](docs/catalog.md#construction)

</details>

<!-- CATALOG-END -->

## Read each case as a construction decision

**Why build another stack → what is rebuilt → what is retained or given up → how it is constructed → how it is validated and maintained.**

For example, [VibeQwen](docs/cases.md#vibeqwen) is an engine outcome; [MetaInfer](docs/catalog.md#metainfer) supplies the construction workflow that was adapted for it. A case card connects them without treating the workflow and its output as the same artifact or duplicating repository counts. Author disclosures, public implementation, validation coverage and unknown effort remain distinct.

The [construction comparison](docs/comparison.md) starts with execution ownership and disclosed effort. Eight [mechanism families](docs/catalog.md) remain secondary search labels for understanding how these designs execute.

## What belongs here?

A **core case** must explain why it illuminates the construction of a specialized execution stack, beyond identifying a deployment constraint and an optimization. Identify the resulting program, the execution decisions it owns, retained dependencies and traceable sources. Unknown construction and maintenance costs are acceptable when explicitly marked unknown.

- **Core cases:** purposeful execution-stack reconstruction, or construction workflows connected to concrete specialized artifacts. Neither a dependency-free implementation nor established AI authorship is required.
- **Historical and adjacent routes:** earlier and contemporary specialized systems, compiler specialization, heterogeneous execution and related construction methods that establish what already exists and what may be changing.
- **Shared foundations and baselines:** general engines, compilers, kernels, optimization components and evaluators that explain reuse and fair comparison.

Relevance and artifact type are independent. Recency, a small codebase, agent use or speed alone does not qualify a core case. Teaching-oriented nano implementations are outside the collection’s scope. See the [classification and inclusion guide](docs/taxonomy.md).

## Evidence and research

The [current discovery audit](docs/discovery-2026-10-12.md) records source tracing, inclusion decisions and unresolved candidates.

This collection reviews sources; it does not independently reproduce project performance. Author results are not independent validation. Separate effects of quantization, approximation and model changes from runtime effects. Establish AI participation through direct disclosure or an inspectable construction workflow, never filenames, coding style or repository size. The [evidence policy](docs/evidence-policy.md) specifies appropriate claim boundaries.

The [research agenda](docs/research-agenda.md) asks what is changing: which general abstractions are worth replacing, which construction steps become automated, whether savings cover verification and maintenance, and what model or hardware changes cost to accommodate. The [historical survey](docs/survey-2026-10-12.md) records the earlier broad search; the [library](docs/systems.md) retains all existing entries.

[Project records](catalog/projects.csv) and [case records](catalog/cases.json) generate the homepage selections, case studies, relevance index, mechanism catalog and comparison. See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance. Metadata, original diagrams, commentary and scripts use the [MIT License](LICENSE); linked projects and models retain their own licenses.
