# Survey library / 主题资料库

> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).

[Home](../README.md) · [中文首页](../README_CN.md) · [Core case studies](cases.md) · [Model domains](domains.md) · [Construction comparison](comparison.md) · [Mechanism index](catalog.md) · [Classification](taxonomy.md)

The research object is the construction of specialized execution stacks. Browse by **why an entry matters to this question**, independently of whether it is a system, construction workflow or supporting component. Relevance is not a quality or maturity ranking, and the adjacent group is not an age cutoff.

先按与主题的关系阅读，再看产物角色和技术机制。原有资料保留，但相邻优化路线不作为构建范式变化的直接证据。

[Core cases](#core) · [Historical and adjacent routes](#adjacent) · [Shared foundations and baselines](#foundation)

<a id="system"></a>
<a id="construction"></a>
<a id="support"></a>

Artifact roles retained as independent labels: `system` — Specialized inference systems; `construction` — Construction workflows; `support` — Supporting infrastructure and references.

<a id="core"></a>

## Core cases / 核心案例 (63)

Purposeful reconstruction of execution paths, or a construction workflow linked to a concrete specialized artifact. These cases motivate investigation; they do not establish a new paradigm.

有明确目的的执行路径重建，或与具体专用产物相连的构建流程。用于提出和研究问题，不自动构成范式变化的证据。

| Project and evidence | Why it is in this survey | Artifact role |
| --- | --- | --- |
| [ane.cpp](catalog.md#ane-cpp) | Connects hardware probes and a documented keep/discard workflow to concrete changes in a specialized execution stack. | system / runtime |
| [ANEMLL Flash llama.cpp](catalog.md#anemll-flash-llama) | A substantial fork exposes exactly which graph/runtime boundary must change to support explicit expert residency. | system / backend |
| [Aria](catalog.md#aria) | Links an explicit author disclosure of LLM-assisted development to a complete native Stable Audio 3 artifact and controlled reference tests, without assuming lower total construction cost. | system / runtime |
| [brodiffusion](catalog.md#brodiffusion) | Owns C++ image-model pipelines and denoiser capture/replay policy over a reused tensor backend, making the boundary between model reconstruction and lower-level reuse explicit. | system / runtime |
| [Cactus](catalog.md#cactus) | Connects model graph capture and lowering to a native mobile execution stack with its own quantized state and kernels. | system / runtime |
| [CIRU runtime](catalog.md#ciru-runtime) | Model/hardware-specific deep integration with traceable borrowed kernels, artifact compatibility work and release qualification. | system / backend |
| [Colibri](catalog.md#colibri) | Exposes the alternative of several small architecture-specific execution programs sharing selected components. | system / runtime |
| [DwarfStar](catalog.md#dwarfstar) | A separately implemented runtime links disclosed AI assistance to model execution and expert-residency control. | system / runtime |
| [edge-dit.cpp](catalog.md#edge-dit) | Core by execution ownership: native DiT graphs and model-component residency, graph segmentation and staged offload reconstruct the integrated constrained-memory path. | system / runtime |
| [ExLlamaV3](catalog.md#exllamav3) | An integrated quantized-model runtime illustrates rebuilding execution around a chosen representation and supported architectures. | system / runtime |
| [FastFlowLM](catalog.md#fastflowlm) | Shows device-specific NPU execution built from model-family host runtimes and compiled kernel providers, with a visible source/binary boundary. | system / runtime |
| [FastVideo](catalog.md#fastvideo) | Core by integrated model execution: its own model implementations, registries, component loaders and denoising stages reconstruct inference, beyond the separately cataloged sparse/distillation methods. | system / runtime |
| [Flash-MoE](catalog.md#flash-moe) | A model-specific implementation links disclosed AI-assisted construction to SSD expert streaming and explicit approximation choices. | system / research-prototype |
| [Gufo](catalog.md#gufo) | Rebuilds a vertical native execution and serving stack around one integrated GPU platform, with deliberately selected models and model-owned kernels. | system / runtime |
| [Gufo RDMA](catalog.md#gufo-rdma) | Substantive deployment reconstruction from one unified-memory machine to two synchronized hosts, not merely another binary package. | system / runtime |
| [Halogen Flash](catalog.md#halogen-flash) | A model-and-device-specific runtime illustrates how narrow deployment contracts reshape implementation choices. | system / runtime |
| [Hearth](catalog.md#hearth) | Reconstructs SD-family model graphs, samplers and dependency-ordered execution in Rust over CubeCL/wgpu, illustrating native pipeline ownership without rebuilding the entire GPU layer. | system / runtime |
| [hipEngine](catalog.md#hipengine) | Native AMD reconstruction with explicit model/device qualification; Gufo cites this runtime as a design reference. | system / runtime |
| [imp](catalog.md#imp) | Explicit single-architecture reconstruction plus a direct author disclosure of end-to-end coding-agent implementation. | system / runtime |
| [Infernix](catalog.md#infernix) | Substantial descendant reconstructing heterogeneous execution for a model too large for GPU memory, with direct AI-development disclosure. | system / runtime |
| [Iris](catalog.md#iris) | A native image-model runtime exposes which graph and execution responsibilities are taken out of a general framework. | system / runtime |
| [Kipp](catalog.md#kipp) | Model-family reconstruction with explicit checkpoint rejection and native serving, beyond a teaching-only forward-pass example. | system / runtime |
| [KTransformers / kt-kernel](catalog.md#ktransformers) | A substantial heterogeneous backend provides a core case for rebuilding execution while retaining shared serving infrastructure. | system / backend |
| [LightX2V](catalog.md#lightx2v) | Core by substantive backend reconstruction: model inference, operator storage contracts and two-slot weight transfer expose owned execution and memory decisions within a shared framework. | system / runtime |
| [Lily](catalog.md#lily) | A deliberately single-checkpoint execution stack makes the compatibility cost of reconstruction explicit. | system / runtime |
| [Lithos Metal](catalog.md#lithos-metal) | Connects a graph compiler and chip-specific recipes to a concrete standalone inference runtime. | system / runtime |
| [llamAmpere](catalog.md#llamampere) | A substantial llama.cpp fork couples model-specific speculative decoding, compressed state and Ampere kernels while retaining shared runtime services. | system / runtime |
| [Llaminar](catalog.md#llaminar) | Native mixed-hardware construction route: owns model graphs, execution plans and cross-vendor coordination rather than wrapping existing engines. | system / runtime |
| [Magnitude](catalog.md#magnitude) | A dedicated inference stack exposes its kernel-composition and model-execution boundary for construction analysis. | system / runtime |
| [memra](catalog.md#memra) | Native runtime with per-model/device exactness gates and explicit evidence of the maintenance and qualification burden. | system / runtime |
| [MetaInfer](catalog.md#metainfer) | Connects a disclosed construction workflow to the VibeQwen engine case; the toolbox and generated engine are different artifacts. | construction / generator |
| [MiniMax-H3 MLX](catalog.md#minimax-h3-mlx) | Reconstructs a complete joint video/audio diffusion model on MLX, including packed modality geometry and invariant AdaLN precomputation; distinguishes making a model fit from making it fast. | system / runtime |
| [Mirage Persistent Kernel](catalog.md#mirage) | A model-to-persistent-program construction path connects generated execution schedules to a concrete runtime artifact. | construction / compiler |
| [NInfer](catalog.md#ninfer) | Rebuilds model execution and serving for selected Qwen checkpoints on one GPU; exposes the scope and ownership of a purpose-built stack. | system / runtime |
| [NInfer-3090](catalog.md#ninfer-3090) | Concrete retargeting case: kernel and memory-program changes beyond changing a CUDA architecture flag; one representative records the 3090 fork family. | system / runtime |
| [Nunchaku](catalog.md#nunchaku) | A substantial low-bit diffusion backend connects representation-specific execution to reusable pipeline integration. | system / runtime |
| [parakeet.cpp (axiom)](catalog.md#parakeet-axiom) | An independent Parakeet reconstruction uses axiom/MPSGraph instead of ggml; it exposes how model and streaming ownership can be retained while reusing a different tensor backend. | system / runtime |
| [parakeet.cpp (ggml)](catalog.md#parakeet-ggml) | Ports NeMo speech graphs and cache-aware transcription semantics into C++/ggml, exposing the conversion, streaming-state and parity work needed to build a portable native ASR stack. | system / runtime |
| [Qingming Qwen3-TTS](catalog.md#qingming-qwen3-tts) | Tests the narrowest device-specialization boundary: separate native synthesis paths for two fixed 24GB GPUs, including their memory capacities and generation/decoder concurrency contracts. | system / runtime |
| [Quartz](catalog.md#saient-quartz) | Exposes native Rust image generation and an evolving native Wan path, while a separate C++ video companion provides a concrete case for auditing claimed versus actual execution boundaries. | system / runtime |
| [Qwen-ASR (C)](catalog.md#qwen-asr-c) | Reconstructs Qwen3-ASR from waveform preprocessing through autoregressive transcription in C, making streaming context policy and CPU/GPU execution responsibilities directly inspectable. | system / runtime |
| [Qwen3-TTS (C)](catalog.md#qwen3-tts-c) | Rebuilds the Qwen3-TTS talker, code predictor and waveform decoder as one native path; published engineering records connect implementation choices to reference checks and measurement corrections. | system / runtime |
| [Saragossa](catalog.md#saragossa) | Replaces array-framework execution with an explicitly owned local runtime and regression oracles. | system / runtime |
| [Sol-Engine](catalog.md#sol-engine) | Connects agent-guided optimization with inspectable model runtimes and their acceptance checks. | construction / optimizer |
| [Splash](catalog.md#splash) | Builds model-specific execution and serving on Apple silicon, with disclosed agent-generated kernels inside a native runtime. | system / runtime |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | Core by construction boundary: the native image/video model implementation owns loading, conditioning, sampling and component placement over reusable ggml backends. | system / runtime |
| [stable-diffusion.rs](catalog.md#stable-diffusion-rs) | Documents a native Rust diffusion implementation and its Candle-to-MLX migration, exposing which model/backend boundaries can survive a device-stack change and which require new parity checks. | system / runtime |
| [Strata](catalog.md#strata) | A narrow MoE runtime makes expert placement and execution choices inspectable; AI authorship is not established. | system / runtime |
| [StreamDiffusionV2](catalog.md#streamdiffusion-v2) | Reconstructs causal video execution around chunked denoising and distributed KV ownership; concrete source and adopter evidence connect a specialized schedule to an integrated streaming artifact. | system / runtime |
| [strix-llama.cpp](catalog.md#strix-llama-cpp) | Hardware-specialized fork with substantial kernel/state changes and a documented upstream/staging boundary; represents the overlapping Strix llama.cpp fork family. | system / backend |
| [Swiftlet](catalog.md#swiftlet) | Links explicit AI-assisted authorship to a model-family-specific runtime and documented reference-based validation. | system / runtime |
| [SwiftLM](catalog.md#swiftlm) | Shows substantial backend reconstruction while retaining the MLX ecosystem and serving integration. | system / backend |
| [TeleFuser](catalog.md#telefuser) | Builds model-specific generation stages together with bounded streaming dataflow, retained session state and execution leases, connecting model execution ownership to an interactive serving workload. | system / runtime |
| [TensorFold](catalog.md#tensorfold) | A native Zig runtime exposes explicit model, format and platform contracts as a reconstruction boundary. | system / runtime |
| [TUFF](catalog.md#tuff) | A disclosed substantial fork shows how a narrow streaming runtime is adapted into several qualified model paths. | system / runtime |
| [TurboFieldfare](catalog.md#turbo-fieldfare) | A single-model native runtime publishes a detailed sequence of accepted and rejected construction experiments. | system / runtime |
| [Vidax](catalog.md#vidax) | Ports video model graphs and checkpoint layouts onto TPU meshes with explicit JAX sharding and numerical-debugging records, making hardware migration a concrete construction case. | system / runtime |
| [vla.simd](catalog.md#vla-simd) | Rebuilds selected robot-policy model paths around CPU SIMD operators and model adapters, exposing action preprocessing and numerical-porting obligations beyond a language-model runtime. | system / runtime |
| [vLLM Radiance](catalog.md#vllm-radiance) | Substantial specialized backend/distribution: preserves vLLM services while replacing device-critical execution and explicitly managing upstream patch dependencies. | system / backend |
| [VoxGen](catalog.md#voxgen) | Reconstructs VoxCPM2 speech synthesis in Rust while directly controlling Vulkan buffers, shaders and incremental PCM state, including a separately tuned RDNA3 device profile. | system / runtime |
| [VTE](catalog.md#vte) | Integrated consumer-GPU runtime with public profiling and bug-history evidence explaining why it was rebuilt. | system / runtime |
| [ZINC](catalog.md#zinc) | Consumer-hardware execution-stack reconstruction with inspectable native model paths and backend-specific measurements. | system / runtime |
| [zLLM](catalog.md#zllm) | A growing collection of native model/device execution paths, including vision-language, image generation and video restoration, with explicit per-backend capability limits. | system / runtime |

<a id="adjacent"></a>

## Historical and adjacent routes / 历史与相邻路线 (43)

Earlier and contemporary routes that explain what already exists, or illuminate a narrower or different construction boundary. This is not an age cutoff.

说明哪些思想早已有之，或构建边界较窄、不同的已有及当代路线；不按年代硬切。

| Project and evidence | Why it is in this survey | Artifact role |
| --- | --- | --- |
| [AgentCompile](catalog.md#agentcompile) | Agent-guided fusion route: a narrower construction comparison with explicit verification and timing caveats. | construction / research-prototype |
| [AKG Agents](catalog.md#akg-agents) | Agent-generated operator route: compares local code synthesis with integrated engine construction. | construction / generator |
| [ANE-LM](catalog.md#ane-lm) | The direct precursor of ane.cpp anchors what the later measurement-driven fork actually changed. | system / runtime |
| [ANEMLL](catalog.md#anemll) | An existing converter-plus-runtime route helps distinguish compiler-mediated specialization from direct native reconstruction. | construction / compiler |
| [AsyncDiff](catalog.md#asyncdiff) | Multi-device diffusion route: compares changed parallel execution and stale-state assumptions. | system / research-prototype |
| [BaseRT](catalog.md#basert) | Provides a contrasting delivery model: public format/conversion tooling around a closed specialized engine. | system / runtime |
| [bitnet.cpp](catalog.md#bitnet-cpp) | Low-bit model/runtime co-design route: compare representation-specific execution and retained framework lineage. | system / runtime |
| [BRaiN](catalog.md#brain) | A broader native training/inference framework provides a contrast to narrowly scoped stacks, including explicit limitations for individual multimodal ports. | system / runtime |
| [Cactus Needle](catalog.md#needle) | A model/runtime co-design and deployment-packaging reference; public model/export code is more inspectable than the distributed native engine. | system / runtime |
| [CoreML LLM CLI](catalog.md#coreml-llm-cli) | A cited predecessor of ANEMLL makes earlier compiled-model and host-runtime specialization visible. | system / research-prototype |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) | Historical layerwise offload route: establishes that heterogeneous specialized execution predates recent coding agents. | system / backend |
| [diffusion-rs](catalog.md#diffusion-rs) | A neighboring Rust model-port route provides a component-reuse and offload comparison; it is not evidence of agent-generated construction. | system / runtime |
| [DistriFusion](catalog.md#distrifusion) | Distributed diffusion route: establishes earlier execution and communication specialization. | system / research-prototype |
| [DistServe](catalog.md#distserve) | Serving specialization route: establishes prefill/decode separation independently of recent engine-construction claims. | system / research-prototype |
| [Draw Things Community](catalog.md#draw-things) | Local-generation application/runtime route: compares integrated product scope and reusable execution layers. | system / runtime |
| [Fiddler](catalog.md#fiddler) | Heterogeneous MoE execution route: compare CPU expert computation with transfer-centric designs. | system / research-prototype |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) | Throughput-oriented offload route: a comparison for existing memory scheduling and workload trade-offs. | system / runtime |
| [Hilum LLM Engine](catalog.md#hilum-engine) | A mobile-focused llama.cpp fork illustrates continued subsystem porting and device adaptation while retaining the general engine. | system / backend |
| [HybriMoE](catalog.md#hybrimoe) | Historical/adjacent heterogeneous MoE route directly referenced by newer native systems; establishes prior art for expert placement and movement. | system / research-prototype |
| [ik_llama.cpp](catalog.md#ik-llama) | Deep fork of a general engine: compare compatibility retention and specialized quantized execution. | system / runtime |
| [Inferix](catalog.md#inferix) | Stateful world-model execution route: an adjacent case of reorganizing generation state rather than evidence of AI-built native execution. | system / runtime |
| [KernelAgent](catalog.md#kernelagent) | Agent-generated kernel and composed-workload route: a construction comparison whose integration scope must be established. | construction / generator |
| [MetalChat](catalog.md#metalchat) | An adjacent native framework illustrates reusable model abstractions rather than a narrowly documented reconstruction experiment. | system / runtime |
| [MFLUX](catalog.md#mflux) | MLX-based model implementation route: contrasts retained tensor framework with more extensive native reconstruction. | system / runtime |
| [MLC LLM](catalog.md#mlc-llm) | Compiler specialization route: establishes existing model-to-deployment construction and portability trade-offs. | construction / runtime |
| [MoE-Infinity](catalog.md#moe-infinity) | Expert-offload route: compare established prefetch and residency policies with separately reconstructed runtimes. | system / runtime |
| [OneDiff](catalog.md#onediff) | Compiler-backed pipeline adaptation: compares generated execution without reconstructing a full serving stack. | construction / compiler |
| [Petals](catalog.md#petals) | Distributed execution route: compares a different deployment contract and system boundary. | system / runtime |
| [PMetal](catalog.md#pmetal) | A training-and-inference platform is an adjacent route for studying when specialized paths live inside a reusable ecosystem. | system / runtime |
| [PowerInfer](catalog.md#powerinfer) | Model/runtime co-design route: separates sparsity assumptions and changed models from construction-method effects. | system / runtime |
| [Punica](catalog.md#punica) | Multi-adapter execution route: compares workload-specific kernels and shared-model scheduling. | system / backend |
| [ROCmFPX](catalog.md#rocmfpx) | Adjacent format/backend construction route used by specialized Strix forks; separate from a new complete model execution stack. | system / backend |
| [S-LoRA](catalog.md#s-lora) | Multi-adapter serving route: establishes prior integrated specialization of memory and batching. | system / research-prototype |
| [Sarathi-Serve](catalog.md#sarathi-serve) | Serving specialization route: compares chunked prefill and batching independently of implementation provenance. | system / research-prototype |
| [Stable Fast](catalog.md#stable-fast) | Framework compilation and capture route: compares incremental specialization and compilation amortization. | construction / compiler |
| [StreamDiffusion](catalog.md#streamdiffusion) | Earlier workload-specific pipeline reconstruction is a comparison for newer causal video engines; most model components remain supplied by Diffusers. | system / runtime |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) | A compiler-based edge deployment reference linking exported model graphs, hardware-specific engine plans and a native multimodal runtime. | system / runtime |
| [TurboDiffusion](catalog.md#turbodiffusion) | Video acceleration route: separates distillation, precision and attention changes from runtime construction. | system / runtime |
| [Uzu](catalog.md#uzu) | A broader on-device engine and model-conversion ecosystem provides a reference for reusable native construction. | system / runtime |
| [VideoSys](catalog.md#videosys) | Video-serving framework route: compares reusable parallelization with narrowly reconstructed execution stacks. | system / runtime |
| [whisper.cpp](catalog.md#whisper-cpp) | Established native speech-model route: a historical control for what purpose-built runtimes and cross-backend maintenance already required. | system / runtime |
| [WhisperKit](catalog.md#whisperkit) | Compiler-backed speech deployment provides a comparison for how much execution control remains in the runtime versus compiled platform artifacts. | system / runtime |
| [xDiT](catalog.md#xdit) | Distributed diffusion route: compares framework-integrated parallel execution and supported-model boundaries. | system / runtime |

<a id="foundation"></a>

## Shared foundations and baselines / 共享基础与对照 (55)

General engines, compilers, kernels, components and evaluators used for reuse and controlled comparison.

提供复用关系与公平比较条件的通用引擎、编译器、内核、组件和评测工具。

| Project and evidence | Why it is in this survey | Artifact role |
| --- | --- | --- |
| [AITemplate](catalog.md#aitemplate) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [Apache TVM](catalog.md#tvm) | Reusable compiler foundation and historical source of model and schedule specialization. | support / compiler |
| [BladeDISC](catalog.md#bladedisc) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [Cache-DiT](catalog.md#cache-dit) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [DeepCache](catalog.md#deepcache) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [DeepCompressor](catalog.md#deepcompressor) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [DeepGEMM](catalog.md#deepgemm) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [DiTFastAttn](catalog.md#ditfastattn) | Related mechanism reference for controlled comparison; source availability alone does not make it a construction case. | support / research-prototype |
| [EAGLE](catalog.md#eagle) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [ExecuTorch](catalog.md#executorch) | Reusable runtime foundation or baseline for comparing retained services and implementation boundaries. | support / runtime |
| [Fast-dLLM](catalog.md#fast-dllm) | Related mechanism reference for controlled comparison; source availability alone does not make it a construction case. | support / research-prototype |
| [FastKernels](catalog.md#fastkernels) | Evaluation and integration reference for testing generated components in model workloads. | support / verification |
| [Flash Linear Attention](catalog.md#flash-linear-attention) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [FlashAttention](catalog.md#flash-attention) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [FlashInfer](catalog.md#flashinfer) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [FlashMLA](catalog.md#flashmla) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [Helion](catalog.md#helion) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [Hidet](catalog.md#hidet) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [IREE](catalog.md#iree) | Reusable compiler/runtime foundation for target-specific programs and execution orchestration. | support / compiler |
| [IREE Turbine](catalog.md#iree-turbine) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [KernelBench](catalog.md#kernelbench) | Operator evaluation foundation; local test success does not establish integrated engine validity. | support / verification |
| [Learning-to-Cache](catalog.md#learning-to-cache) | Related mechanism reference for controlled comparison; source availability alone does not make it a construction case. | support / research-prototype |
| [llama.cpp](catalog.md#llama-cpp) | General local-inference substrate and baseline; retained components must be distinguished from rewritten execution. | support / runtime |
| [LMCache](catalog.md#lmcache) | Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence. | support / backend |
| [Lookahead Decoding](catalog.md#lookahead) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [MagCache](catalog.md#magcache) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [Marlin](catalog.md#marlin) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [Medusa](catalog.md#medusa) | Related mechanism reference for controlled comparison; source availability alone does not make it a construction case. | support / research-prototype |
| [MInference](catalog.md#minference) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [Mooncake](catalog.md#mooncake) | Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence. | support / backend |
| [NIXL](catalog.md#nixl) | Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence. | support / backend |
| [NVIDIA TensorRT](catalog.md#tensorrt) | Engine-building baseline with a closed optimizer/runtime core; compare disclosed interfaces and build cost. | support / compiler |
| [ONNX Runtime GenAI](catalog.md#onnxruntime-genai) | General exported-model runtime baseline for portability and generation-state management. | support / runtime |
| [OpenVINO GenAI](catalog.md#openvino-genai) | General deployment baseline for device coverage, model export and state-management costs. | support / runtime |
| [ParaAttention](catalog.md#para-attention) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [QTIP](catalog.md#qtip) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [SageAttention](catalog.md#sageattention) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [SGLang](catalog.md#sglang) | General serving baseline and source of shared runtime abstractions and components. | support / runtime |
| [SnapKV](catalog.md#snapkv) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [SpargeAttention](catalog.md#spargeattn) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [Sparse VideoGen](catalog.md#sparse-videogen) | Related mechanism reference for controlled comparison; source availability alone does not make it a construction case. | support / research-prototype |
| [Spec-Bench](catalog.md#spec-bench) | Evaluation reference for matching speculative-decoding workloads and baseline conditions. | support / verification |
| [SwiftTransformer](catalog.md#swifttransformer) | Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence. | support / backend |
| [T-GATE](catalog.md#t-gate) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [T-MAC](catalog.md#t-mac) | Reusable kernel foundation; isolates component reuse from claims of complete engine reconstruction. | support / kernel-library |
| [TaylorSeer](catalog.md#taylorseer) | Related mechanism reference for controlled comparison; source availability alone does not make it a construction case. | support / research-prototype |
| [TeaCache](catalog.md#teacache) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [TensorRT-LLM](catalog.md#tensorrt-llm) | General GPU serving baseline and kernel source; reuse is distinct from independent full-stack implementation. | support / runtime |
| [TileLang](catalog.md#tilelang) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [tinygrad](catalog.md#tinygrad) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [ToMe for Stable Diffusion](catalog.md#tomesd) | Optimization component for integration and comparison; its mechanism alone does not establish a reconstructed execution stack. | support / optimizer |
| [Torch-TensorRT](catalog.md#torch-tensorrt) | Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence. | support / backend |
| [Triton](catalog.md#triton) | Reusable compiler foundation; compare which lowering and scheduling responsibilities a specialized stack retains or replaces. | support / compiler |
| [vAttention](catalog.md#vattention) | Reusable execution backend for integration and comparison; component capability is separate from engine construction evidence. | support / backend |
| [vLLM](catalog.md#vllm) | General-engine baseline and reusable execution components for controlled comparisons with specialized stacks. | support / runtime |

