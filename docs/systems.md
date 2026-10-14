# Project roles / 项目角色索引

> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).

[Home](../README.md) · [中文首页](../README_CN.md) · [Cases](cases.md) · [Validation](validation.md) · [Benchmarks](benchmarks.md) · [Resources](resources.md) · [Model domains](domains.md)

Browse engines, construction workflows and validation first; benchmarks have a separate entry, while diagnostics, knowledge and selected reusable infrastructure are companion resources. Each repository appears once under its primary role.

先看引擎、构建与验证；评测单列，性能诊断、知识和精选基础设施作为配套。同一仓库按主要作用计一次，内部验证或知识模块另有方法入口。

[专用推理引擎 / Specialized inference engines](#system) · [引擎构建与优化方案 / Engine construction and optimization](#construction) · [正确性与质量验证方案 / Correctness and quality validation](#validation) · [评测基准与任务集 / Benchmarks and task suites](#benchmark) · [配套资源 / Companion resources](#support)

## Relevance labels / 相关性标签

<a id="core"></a>

**core — 核心案例 / Core cases**: Purposeful reconstruction of execution paths, or a construction workflow linked to a concrete specialized artifact. These cases motivate investigation; they do not establish a new paradigm.

<a id="adjacent"></a>

**adjacent — 历史与相邻路线 / Historical and adjacent routes**: Earlier and contemporary routes that explain what already exists, or illuminate a narrower or different construction boundary. This is not an age cutoff.

<a id="foundation"></a>

**foundation — 共享基础与对照 / Shared foundations and baselines**: Selected shared infrastructure, knowledge and evaluators with an explicit construction, validation or comparison relationship.

<a id="system"></a>

## Specialized inference engines / 专用推理引擎

Integrated model runtimes and substantial specialized backends, including native implementations and earlier execution-stack precedents.

集成模型运行时和实质专用后端，涵盖原生实现与有直接参照意义的既有执行栈。

91 projects / 项目

| Project and evidence | Why it belongs | Relevance / artifact |
| --- | --- | --- |
| [ane.cpp](catalog.md#ane-cpp) | Connects hardware probes and a documented keep/discard workflow to concrete changes in a specialized execution stack. | core / runtime |
| [ANEMLL Flash llama.cpp](catalog.md#anemll-flash-llama) | A substantial fork exposes exactly which graph/runtime boundary must change to support explicit expert residency. | core / backend |
| [Aria](catalog.md#aria) | Links an explicit author disclosure of LLM-assisted development to a complete native Stable Audio 3 artifact and controlled reference tests, without assuming lower total construction cost. | core / runtime |
| [brodiffusion](catalog.md#brodiffusion) | Owns C++ image-model pipelines and denoiser capture/replay policy over a reused tensor backend, making the boundary between model reconstruction and lower-level reuse explicit. | core / runtime |
| [Cactus](catalog.md#cactus) | Connects model graph capture and lowering to a native mobile execution stack with its own quantized state and kernels. | core / runtime |
| [CIRU runtime](catalog.md#ciru-runtime) | Model/hardware-specific deep integration with traceable borrowed kernels, artifact compatibility work and release qualification. | core / backend |
| [Cloudflare Infire](catalog.md#infire) | An industrial platform-specialization case documenting why a provider rebuilt execution instead of only configuring a general framework; useful without an AI-development attribution. | core / runtime |
| [Colibri](catalog.md#colibri) | Exposes the alternative of several small architecture-specific execution programs sharing selected components. | core / runtime |
| [DwarfStar](catalog.md#dwarfstar) | A separately implemented runtime links disclosed AI assistance to model execution and expert-residency control. | core / runtime |
| [edge-dit.cpp](catalog.md#edge-dit) | Core by execution ownership: native DiT graphs and model-component residency, graph segmentation and staged offload reconstruct the integrated constrained-memory path. | core / runtime |
| [ExLlamaV3](catalog.md#exllamav3) | An integrated quantized-model runtime illustrates rebuilding execution around a chosen representation and supported architectures. | core / runtime |
| [FastFlowLM](catalog.md#fastflowlm) | Shows device-specific NPU execution built from model-family host runtimes and compiled kernel providers, with a visible source/binary boundary. | core / runtime |
| [FastVideo](catalog.md#fastvideo) | Core by integrated model execution: its own model implementations, registries, component loaders and denoising stages reconstruct inference, beyond the separately cataloged sparse/distillation methods. | core / runtime |
| [Flash-MoE](catalog.md#flash-moe) | A model-specific implementation links disclosed AI-assisted construction to SSD expert streaming and explicit approximation choices. | core / research-prototype |
| [Gufo](catalog.md#gufo) | Rebuilds a vertical native execution and serving stack around one integrated GPU platform, with deliberately selected models and model-owned kernels. | core / runtime |
| [Gufo RDMA](catalog.md#gufo-rdma) | Substantive deployment reconstruction from one unified-memory machine to two synchronized hosts, not merely another binary package. | core / runtime |
| [Halogen Flash](catalog.md#halogen-flash) | A model-and-device-specific runtime illustrates how narrow deployment contracts reshape implementation choices. | core / runtime |
| [Hearth](catalog.md#hearth) | Reconstructs SD-family model graphs, samplers and dependency-ordered execution in Rust over CubeCL/wgpu, illustrating native pipeline ownership without rebuilding the entire GPU layer. | core / runtime |
| [hipEngine](catalog.md#hipengine) | Native AMD reconstruction with explicit model/device qualification; Gufo cites this runtime as a design reference. | core / runtime |
| [imp](catalog.md#imp) | Explicit single-architecture reconstruction plus a direct author disclosure of end-to-end coding-agent implementation. | core / runtime |
| [Infernix](catalog.md#infernix) | Substantial descendant reconstructing heterogeneous execution for a model too large for GPU memory, with direct AI-development disclosure. | core / runtime |
| [Iris](catalog.md#iris) | A native image-model runtime exposes which graph and execution responsibilities are taken out of a general framework. | core / runtime |
| [Kipp](catalog.md#kipp) | Model-family reconstruction with explicit checkpoint rejection and native serving, beyond a teaching-only forward-pass example. | core / runtime |
| [Kog Inference Engine (KIE)](catalog.md#kie) | An industrial model/runtime/hardware co-design case with an explicitly narrow low-latency operating point; distinguishes a purpose-built execution architecture from a generic serving configuration. | core / runtime |
| [KTransformers / kt-kernel](catalog.md#ktransformers) | A substantial heterogeneous backend provides a core case for rebuilding execution while retaining shared serving infrastructure. | core / backend |
| [LightX2V](catalog.md#lightx2v) | Core by substantive backend reconstruction: model inference, operator storage contracts and two-slot weight transfer expose owned execution and memory decisions within a shared framework. | core / runtime |
| [Lily](catalog.md#lily) | A deliberately single-checkpoint execution stack makes the compatibility cost of reconstruction explicit. | core / runtime |
| [Lithos Metal](catalog.md#lithos-metal) | Connects a graph compiler and chip-specific recipes to a concrete standalone inference runtime. | core / runtime |
| [llamAmpere](catalog.md#llamampere) | A substantial llama.cpp fork couples model-specific speculative decoding, compressed state and Ampere kernels while retaining shared runtime services. | core / runtime |
| [Llaminar](catalog.md#llaminar) | Native mixed-hardware construction route: owns model graphs, execution plans and cross-vendor coordination rather than wrapping existing engines. | core / runtime |
| [Magnitude](catalog.md#magnitude) | A dedicated inference stack exposes its kernel-composition and model-execution boundary for construction analysis. | core / runtime |
| [memra](catalog.md#memra) | Native runtime with per-model/device exactness gates and explicit evidence of the maintenance and qualification burden. | core / runtime |
| [MiniMax-H3 MLX](catalog.md#minimax-h3-mlx) | Reconstructs a complete joint video/audio diffusion model on MLX, including packed modality geometry and invariant AdaLN precomputation; distinguishes making a model fit from making it fast. | core / runtime |
| [NInfer](catalog.md#ninfer) | Rebuilds model execution and serving for selected Qwen checkpoints on one GPU; exposes the scope and ownership of a purpose-built stack. | core / runtime |
| [NInfer-3090](catalog.md#ninfer-3090) | Concrete retargeting case: kernel and memory-program changes beyond changing a CUDA architecture flag; one representative records the 3090 fork family. | core / runtime |
| [Nunchaku](catalog.md#nunchaku) | A substantial low-bit diffusion backend connects representation-specific execution to reusable pipeline integration. | core / runtime |
| [parakeet.cpp (axiom)](catalog.md#parakeet-axiom) | An independent Parakeet reconstruction uses axiom/MPSGraph instead of ggml; it exposes how model and streaming ownership can be retained while reusing a different tensor backend. | core / runtime |
| [parakeet.cpp (ggml)](catalog.md#parakeet-ggml) | Ports NeMo speech graphs and cache-aware transcription semantics into C++/ggml, exposing the conversion, streaming-state and parity work needed to build a portable native ASR stack. | core / runtime |
| [Qingming Qwen3-TTS](catalog.md#qingming-qwen3-tts) | Tests the narrowest device-specialization boundary: separate native synthesis paths for two fixed 24GB GPUs, including their memory capacities and generation/decoder concurrency contracts. | core / runtime |
| [Quartz](catalog.md#saient-quartz) | Exposes native Rust image generation and an evolving native Wan path, while a separate C++ video companion provides a concrete case for auditing claimed versus actual execution boundaries. | core / runtime |
| [Qwen-ASR (C)](catalog.md#qwen-asr-c) | Reconstructs Qwen3-ASR from waveform preprocessing through autoregressive transcription in C, making streaming context policy and CPU/GPU execution responsibilities directly inspectable. | core / runtime |
| [Qwen3-TTS (C)](catalog.md#qwen3-tts-c) | Rebuilds the Qwen3-TTS talker, code predictor and waveform decoder as one native path; published engineering records connect implementation choices to reference checks and measurement corrections. | core / runtime |
| [Saragossa](catalog.md#saragossa) | Replaces array-framework execution with an explicitly owned local runtime and regression oracles. | core / runtime |
| [Splash](catalog.md#splash) | Builds model-specific execution and serving on Apple silicon, with disclosed agent-generated kernels inside a native runtime. | core / runtime |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | Core by construction boundary: the native image/video model implementation owns loading, conditioning, sampling and component placement over reusable ggml backends. | core / runtime |
| [stable-diffusion.rs](catalog.md#stable-diffusion-rs) | Documents a native Rust diffusion implementation and its Candle-to-MLX migration, exposing which model/backend boundaries can survive a device-stack change and which require new parity checks. | core / runtime |
| [Strata](catalog.md#strata) | A narrow MoE runtime makes expert placement and execution choices inspectable; AI authorship is not established. | core / runtime |
| [StreamDiffusionV2](catalog.md#streamdiffusion-v2) | Reconstructs causal video execution around chunked denoising and distributed KV ownership; concrete source and adopter evidence connect a specialized schedule to an integrated streaming artifact. | core / runtime |
| [strix-llama.cpp](catalog.md#strix-llama-cpp) | Hardware-specialized fork with substantial kernel/state changes and a documented upstream/staging boundary; represents the overlapping Strix llama.cpp fork family. | core / backend |
| [Swiftlet](catalog.md#swiftlet) | Links explicit AI-assisted authorship to a model-family-specific runtime and documented reference-based validation. | core / runtime |
| [SwiftLM](catalog.md#swiftlm) | Shows substantial backend reconstruction while retaining the MLX ecosystem and serving integration. | core / backend |
| [TeleFuser](catalog.md#telefuser) | Builds model-specific generation stages together with bounded streaming dataflow, retained session state and execution leases, connecting model execution ownership to an interactive serving workload. | core / runtime |
| [TensorFold](catalog.md#tensorfold) | A native Zig runtime exposes explicit model, format and platform contracts as a reconstruction boundary. | core / runtime |
| [TUFF](catalog.md#tuff) | A disclosed substantial fork shows how a narrow streaming runtime is adapted into several qualified model paths. | core / runtime |
| [TurboFieldfare](catalog.md#turbo-fieldfare) | A single-model native runtime publishes a detailed sequence of accepted and rejected construction experiments. | core / runtime |
| [Vidax](catalog.md#vidax) | Ports video model graphs and checkpoint layouts onto TPU meshes with explicit JAX sharding and numerical-debugging records, making hardware migration a concrete construction case. | core / runtime |
| [vla.simd](catalog.md#vla-simd) | Rebuilds selected robot-policy model paths around CPU SIMD operators and model adapters, exposing action preprocessing and numerical-porting obligations beyond a language-model runtime. | core / runtime |
| [vLLM Radiance](catalog.md#vllm-radiance) | Substantial specialized backend/distribution: preserves vLLM services while replacing device-critical execution and explicitly managing upstream patch dependencies. | core / backend |
| [VoxGen](catalog.md#voxgen) | Reconstructs VoxCPM2 speech synthesis in Rust while directly controlling Vulkan buffers, shaders and incremental PCM state, including a separately tuned RDNA3 device profile. | core / runtime |
| [VTE](catalog.md#vte) | Integrated consumer-GPU runtime with public profiling and bug-history evidence explaining why it was rebuilt. | core / runtime |
| [ZINC](catalog.md#zinc) | Consumer-hardware execution-stack reconstruction with inspectable native model paths and backend-specific measurements. | core / runtime |
| [zLLM](catalog.md#zllm) | A growing collection of native model/device execution paths, including vision-language, image generation and video restoration, with explicit per-backend capability limits. | core / runtime |
| [ANE-LM](catalog.md#ane-lm) | The direct precursor of ane.cpp anchors what the later measurement-driven fork actually changed. | adjacent / runtime |
| [BaseRT](catalog.md#basert) | Provides a contrasting delivery model: public format/conversion tooling around a closed specialized engine. | adjacent / runtime |
| [bitnet.cpp](catalog.md#bitnet-cpp) | Low-bit model/runtime co-design route: compare representation-specific execution and retained framework lineage. | adjacent / runtime |
| [BRaiN](catalog.md#brain) | A broader native training/inference framework provides a contrast to narrowly scoped stacks, including explicit limitations for individual multimodal ports. | adjacent / runtime |
| [Cactus Needle](catalog.md#needle) | A model/runtime co-design and deployment-packaging reference; public model/export code is more inspectable than the distributed native engine. | adjacent / runtime |
| [CoreML LLM CLI](catalog.md#coreml-llm-cli) | A cited predecessor of ANEMLL makes earlier compiled-model and host-runtime specialization visible. | adjacent / research-prototype |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) | Historical layerwise offload route: establishes that heterogeneous specialized execution predates recent coding agents. | adjacent / backend |
| [diffusion-rs](catalog.md#diffusion-rs) | A neighboring Rust model-port route provides a component-reuse and offload comparison; it is not evidence of agent-generated construction. | adjacent / runtime |
| [Draw Things Community](catalog.md#draw-things) | Local-generation application/runtime route: compares integrated product scope and reusable execution layers. | adjacent / runtime |
| [Fiddler](catalog.md#fiddler) | Heterogeneous MoE execution route: compare CPU expert computation with transfer-centric designs. | adjacent / research-prototype |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) | Throughput-oriented offload route: a comparison for existing memory scheduling and workload trade-offs. | adjacent / runtime |
| [Hilum LLM Engine](catalog.md#hilum-engine) | A mobile-focused llama.cpp fork illustrates continued subsystem porting and device adaptation while retaining the general engine. | adjacent / backend |
| [HybriMoE](catalog.md#hybrimoe) | Historical/adjacent heterogeneous MoE route directly referenced by newer native systems; establishes prior art for expert placement and movement. | adjacent / research-prototype |
| [ik_llama.cpp](catalog.md#ik-llama) | Deep fork of a general engine: compare compatibility retention and specialized quantized execution. | adjacent / runtime |
| [Inferix](catalog.md#inferix) | Stateful world-model execution route: an adjacent case of reorganizing generation state rather than evidence of AI-built native execution. | adjacent / runtime |
| [MetalChat](catalog.md#metalchat) | An adjacent native framework illustrates reusable model abstractions rather than a narrowly documented reconstruction experiment. | adjacent / runtime |
| [MFLUX](catalog.md#mflux) | MLX-based model implementation route: contrasts retained tensor framework with more extensive native reconstruction. | adjacent / runtime |
| [MoE-Infinity](catalog.md#moe-infinity) | Expert-offload route: compare established prefetch and residency policies with separately reconstructed runtimes. | adjacent / runtime |
| [PMetal](catalog.md#pmetal) | A training-and-inference platform is an adjacent route for studying when specialized paths live inside a reusable ecosystem. | adjacent / runtime |
| [PowerInfer](catalog.md#powerinfer) | Model/runtime co-design route: separates sparsity assumptions and changed models from construction-method effects. | adjacent / runtime |
| [ROCmFPX](catalog.md#rocmfpx) | Adjacent format/backend construction route used by specialized Strix forks; separate from a new complete model execution stack. | adjacent / backend |
| [StreamDiffusion](catalog.md#streamdiffusion) | Earlier workload-specific pipeline reconstruction is a comparison for newer causal video engines; most model components remain supplied by Diffusers. | adjacent / runtime |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) | A compiler-based edge deployment reference linking exported model graphs, hardware-specific engine plans and a native multimodal runtime. | adjacent / runtime |
| [TurboDiffusion](catalog.md#turbodiffusion) | Video acceleration route: separates distillation, precision and attention changes from runtime construction. | adjacent / runtime |
| [Uzu](catalog.md#uzu) | A broader on-device engine and model-conversion ecosystem provides a reference for reusable native construction. | adjacent / runtime |
| [VideoSys](catalog.md#videosys) | Integrated video execution combining attention reuse and dynamic device partitioning; a concrete comparison for the reconstructed video runtimes in this collection. | adjacent / runtime |
| [whisper.cpp](catalog.md#whisper-cpp) | Established native speech-model route: a historical control for what purpose-built runtimes and cross-backend maintenance already required. | adjacent / runtime |
| [WhisperKit](catalog.md#whisperkit) | Compiler-backed speech deployment provides a comparison for how much execution control remains in the runtime versus compiled platform artifacts. | adjacent / runtime |
| [xDiT](catalog.md#xdit) | Distributed diffusion route: compares framework-integrated parallel execution and supported-model boundaries. | adjacent / runtime |

<a id="construction"></a>

## Engine construction and optimization / 引擎构建与优化方案

Agent harnesses, compiler workflows and model-specific optimization procedures. State whether the output is a kernel, model program or serving stack.

Agent harness、编译流程与模型专用优化；区分内核、模型程序与服务执行栈的产出边界。

14 projects / 项目

| Project and evidence | Why it belongs | Relevance / artifact |
| --- | --- | --- |
| [AutoMegaKernel](catalog.md#automegakernel) | A model-program construction case combining a restricted agent edit surface, deterministic lowering and schedule checks; contrasts with unconstrained whole-runtime generation. | core / compiler |
| [MetaInfer](catalog.md#metainfer) | Connects a disclosed construction workflow to the VibeQwen engine case; the toolbox and generated engine are different artifacts. | core / generator |
| [Mirage Persistent Kernel](catalog.md#mirage) | A model-to-persistent-program construction path connects generated execution schedules to a concrete runtime artifact. | core / compiler |
| [SEIS: Self-Evolving Inference Systems](catalog.md#seis) | Sustained agent-driven reconstruction of an existing inference engine connects inherited code and reports to kernel, runtime and decoding changes; the study also exposes gaps in its evolving validation gates. | core / generator |
| [Sol-Engine](catalog.md#sol-engine) | Connects agent-guided optimization with inspectable model runtimes and their acceptance checks. | core / optimizer |
| [VibeServe / VibeSys](catalog.md#vibesys) | Connects generation-time model/hardware/workload specialization to a concrete serving-system initiative; the broader generator and its scenario-specific outputs are distinct artifacts. | core / generator |
| [AgentCompile](catalog.md#agentcompile) | Agent-guided fusion route: a narrower construction comparison with explicit verification and timing caveats. | adjacent / research-prototype |
| [AKG Agents](catalog.md#akg-agents) | Agent-generated operator route: compares local code synthesis with integrated engine construction. | adjacent / generator |
| [ANEMLL](catalog.md#anemll) | An existing converter-plus-runtime route helps distinguish compiler-mediated specialization from direct native reconstruction. | adjacent / compiler |
| [Atrex Kernel Agent (AKA)](catalog.md#atrex-kernel-agent) | Operator-level construction harness connecting coding agents, measured feedback, acceptance gates and reusable optimization knowledge. | adjacent / generator |
| [KernelAgent](catalog.md#kernelagent) | Agent-generated kernel and composed-workload route: a construction comparison whose integration scope must be established. | adjacent / generator |
| [MLC LLM](catalog.md#mlc-llm) | Compiler specialization route: establishes existing model-to-deployment construction and portability trade-offs. | adjacent / runtime |
| [OneDiff](catalog.md#onediff) | Compiler-backed pipeline adaptation: compares generated execution without reconstructing a full serving stack. | adjacent / compiler |
| [Stable Fast](catalog.md#stable-fast) | Framework compilation and capture route: compares incremental specialization and compilation amortization. | adjacent / compiler |

<a id="validation"></a>

## Correctness and quality validation / 正确性与质量验证方案

Methods that check numerical behavior, model state, generation quality or service contracts. Embedded validators are indexed as methods without duplicating their parent project.

检验数值行为、模型状态、生成质量或服务契约；内嵌验证模块按方案索引，不重复计算所属仓库。

[Validation methods and coverage / 验证方案及覆盖边界](validation.md). Embedded methods are not counted as separate projects. / 内嵌方案不另计项目。

<a id="benchmark"></a>

## Benchmarks and task suites / 评测基准与任务集

Executable workloads and comparison protocols for generated kernels and integrated inference paths.

用于生成内核和集成推理路径的可执行负载、参考实现与比较协议。

3 projects / 项目

| Project and evidence | Why it belongs | Relevance / artifact |
| --- | --- | --- |
| [Atrex-Bench](catalog.md#atrex-bench) | Production-derived operator tasks and separated evaluation provide a benchmark for generated execution components. | foundation / benchmark |
| [FastKernels](catalog.md#fastkernels) | Evaluation and integration reference for testing generated components in model workloads. | foundation / benchmark |
| [KernelBench](catalog.md#kernelbench) | Executable tasks for kernel and model-program construction workflows such as KernelAgent; task-level acceptance remains separate from deployed-engine validation. | foundation / benchmark |

<a id="support"></a>

## Companion resources / 配套资源

Performance diagnosis, construction knowledge, and selected infrastructure with a named connection to an included engine or construction workflow.

性能诊断、构建知识，以及与收录引擎或构建流程有明确关系的精选基础设施。

18 projects / 项目

| Project and evidence | Why it belongs | Relevance / artifact |
| --- | --- | --- |
| [Apache TVM](catalog.md#tvm) | Compiler infrastructure underlying the included MLC LLM model-to-runtime construction route. | foundation / compiler |
| [Apple Neural Engine Field Guide](catalog.md#ane-field-guide) | Concrete hardware-investigation knowledge and accepted/rejected experiments feed the separately cataloged ane.cpp engine. | foundation / knowledge-base |
| [DeepCompressor](catalog.md#deepcompressor) | Model preparation used for the Nunchaku/SVDQuant execution path; calibration and exported weights must be distinguished from runtime gains. | foundation / optimizer |
| [Flash Linear Attention](catalog.md#flash-linear-attention) | Reusable recurrent and linear-attention kernels in the ExLlamaV3 execution stack; state semantics must survive integration. | foundation / kernel-library |
| [FlashAttention](catalog.md#flash-attention) | Attention implementation reused by included model runtimes such as ExLlamaV3; an optimized component does not establish an end-to-end gain. | foundation / kernel-library |
| [FlashInfer](catalog.md#flashinfer) | Optional standard paged-attention backend used by MoE-Infinity where supported; preserves the distinction between reusable kernels and the reconstructed engine. | foundation / kernel-library |
| [KernelWiki](catalog.md#kernelwiki) | Retrievable hardware and kernel experience connects prior engineering work with subsequent specialized implementation decisions. | foundation / knowledge-base |
| [llama.cpp](catalog.md#llama-cpp) | Upstream execution stack for the llamAmpere, CIRU, Strix and ANEMLL Flash forks; makes inherited code and changed execution paths comparable. | foundation / runtime |
| [Marlin](catalog.md#marlin) | Quantized linear-kernel and packing reference used in the ExLlamaV3 construction account; separates reusable low-level work from engine ownership. | foundation / kernel-library |
| [ncu-report-skill](catalog.md#ncu-report-skill) | Diagnostic companion for connecting measured kernel bottlenecks to an agent-guided optimization decision. | foundation / diagnostic |
| [NVIDIA TensorRT](catalog.md#tensorrt) | Model-compilation and execution foundation for the included TensorRT Edge-LLM deployment route. | foundation / compiler |
| [QTIP](catalog.md#qtip) | Trellis quantization and matching execution provide a representation-design reference credited in the ExLlamaV3 case, rather than a second complete engine. | foundation / optimizer |
| [SageAttention](catalog.md#sageattention) | Low-precision attention component integrated into the included FastVideo/video execution paths, with a separate quality-validation obligation. | foundation / kernel-library |
| [SGLang](catalog.md#sglang) | Shared serving infrastructure used alongside KTransformers and model components reused by Sol-Engine; separates specialized execution from shared services. | foundation / runtime |
| [TensorRT-LLM](catalog.md#tensorrt-llm) | General-engine comparison point in the VibeQwen case; record matching model, hardware, precision and workload before comparing the specialized result. | foundation / runtime |
| [TileLang](catalog.md#tilelang) | Kernel language supported by the included Atrex Kernel Agent campaigns; a generated kernel remains distinct from a complete model runtime. | foundation / compiler |
| [Triton](catalog.md#triton) | Kernel language emitted or optimized by KernelAgent and Atrex Kernel Agent, linking generated programs to their compilation and validation boundary. | foundation / compiler |
| [vLLM](catalog.md#vllm) | General-engine reference for the VibeQwen construction case and upstream serving infrastructure retained by the Radiance specialized backend. | foundation / runtime |

