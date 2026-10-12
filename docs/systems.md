# Survey library / 主题资料库

> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).

[Home](../README.md) · [中文首页](../README_CN.md) · [Core case studies](cases.md) · [Construction comparison](comparison.md) · [Mechanism index](catalog.md) · [Classification](taxonomy.md)

The research object is the construction of specialized execution stacks. Browse by **why an entry matters to this question**, independently of whether it is a system, construction workflow or supporting component. Relevance is not a quality or maturity ranking, and the adjacent group is not an age cutoff.

先按与主题的关系阅读，再看产物角色和技术机制。原有资料保留，但相邻优化路线不作为构建范式变化的直接证据。

[Core cases](#core) · [Historical and adjacent routes](#adjacent) · [Shared foundations and baselines](#foundation)

<a id="system"></a>
<a id="construction"></a>
<a id="support"></a>

Artifact roles retained as independent labels: `system` — Specialized inference systems; `construction` — Construction workflows; `support` — Supporting infrastructure and references.

<a id="core"></a>

## Core cases / 核心案例 (17)

Purposeful reconstruction of execution paths, or a construction workflow linked to a concrete specialized artifact. These cases motivate investigation; they do not establish a new paradigm.

有明确目的的执行路径重建，或与具体专用产物相连的构建流程。用于提出和研究问题，不自动构成范式变化的证据。

| Project and evidence | Why it is in this survey | Artifact role |
| --- | --- | --- |
| [DwarfStar](catalog.md#dwarfstar) | A separately implemented runtime links disclosed AI assistance to model execution and expert-residency control. | system / runtime |
| [ExLlamaV3](catalog.md#exllamav3) | An integrated quantized-model runtime illustrates rebuilding execution around a chosen representation and supported architectures. | system / runtime |
| [Flash-MoE](catalog.md#flash-moe) | A model-specific implementation links disclosed AI-assisted construction to SSD expert streaming and explicit approximation choices. | system / research-prototype |
| [Gufo](catalog.md#gufo) | Rebuilds a vertical native execution and serving stack around one integrated GPU platform, with deliberately selected models and model-owned kernels. | system / runtime |
| [Halogen Flash](catalog.md#halogen-flash) | A model-and-device-specific runtime illustrates how narrow deployment contracts reshape implementation choices. | system / runtime |
| [Iris](catalog.md#iris) | A native image-model runtime exposes which graph and execution responsibilities are taken out of a general framework. | system / runtime |
| [KTransformers / kt-kernel](catalog.md#ktransformers) | A substantial heterogeneous backend provides a core case for rebuilding execution while retaining shared serving infrastructure. | system / backend |
| [llamAmpere](catalog.md#llamampere) | A substantial llama.cpp fork couples model-specific speculative decoding, compressed state and Ampere kernels while retaining shared runtime services. | system / runtime |
| [Magnitude](catalog.md#magnitude) | A dedicated inference stack exposes its kernel-composition and model-execution boundary for construction analysis. | system / runtime |
| [MetaInfer](catalog.md#metainfer) | Connects a disclosed construction workflow to the VibeQwen engine case; the toolbox and generated engine are different artifacts. | construction / generator |
| [Mirage Persistent Kernel](catalog.md#mirage) | A model-to-persistent-program construction path connects generated execution schedules to a concrete runtime artifact. | construction / compiler |
| [NInfer](catalog.md#ninfer) | Rebuilds model execution and serving for selected Qwen checkpoints on one GPU; exposes the scope and ownership of a purpose-built stack. | system / runtime |
| [Nunchaku](catalog.md#nunchaku) | A substantial low-bit diffusion backend connects representation-specific execution to reusable pipeline integration. | system / runtime |
| [Sol-Engine](catalog.md#sol-engine) | Connects agent-guided optimization with inspectable model runtimes and their acceptance checks. | construction / optimizer |
| [Splash](catalog.md#splash) | Builds model-specific execution and serving on Apple silicon, with disclosed agent-generated kernels inside a native runtime. | system / runtime |
| [Strata](catalog.md#strata) | A narrow MoE runtime makes expert placement and execution choices inspectable; AI authorship is not established. | system / runtime |
| [TensorFold](catalog.md#tensorfold) | A native Zig runtime exposes explicit model, format and platform contracts as a reconstruction boundary. | system / runtime |

<a id="adjacent"></a>

## Historical and adjacent routes / 历史与相邻路线 (30)

Earlier and contemporary routes that explain what already exists, or illuminate a narrower or different construction boundary. This is not an age cutoff.

说明哪些思想早已有之，或构建边界较窄、不同的已有及当代路线；不按年代硬切。

| Project and evidence | Why it is in this survey | Artifact role |
| --- | --- | --- |
| [AgentCompile](catalog.md#agentcompile) | Agent-guided fusion route: a narrower construction comparison with explicit verification and timing caveats. | construction / research-prototype |
| [AKG Agents](catalog.md#akg-agents) | Agent-generated operator route: compares local code synthesis with integrated engine construction. | construction / generator |
| [AsyncDiff](catalog.md#asyncdiff) | Multi-device diffusion route: compares changed parallel execution and stale-state assumptions. | system / research-prototype |
| [bitnet.cpp](catalog.md#bitnet-cpp) | Low-bit model/runtime co-design route: compare representation-specific execution and retained framework lineage. | system / runtime |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) | Historical layerwise offload route: establishes that heterogeneous specialized execution predates recent coding agents. | system / backend |
| [DistriFusion](catalog.md#distrifusion) | Distributed diffusion route: establishes earlier execution and communication specialization. | system / research-prototype |
| [DistServe](catalog.md#distserve) | Serving specialization route: establishes prefill/decode separation independently of recent engine-construction claims. | system / research-prototype |
| [Draw Things Community](catalog.md#draw-things) | Local-generation application/runtime route: compares integrated product scope and reusable execution layers. | system / runtime |
| [edge-dit.cpp](catalog.md#edge-dit) | Native diffusion route: useful adjacent comparison for component placement, reuse and compatibility boundaries. | system / runtime |
| [FastVideo](catalog.md#fastvideo) | Video-model pipeline route: contrasts integrated optimization and model changes with execution-stack reconstruction. | system / runtime |
| [Fiddler](catalog.md#fiddler) | Heterogeneous MoE execution route: compare CPU expert computation with transfer-centric designs. | system / research-prototype |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) | Throughput-oriented offload route: a comparison for existing memory scheduling and workload trade-offs. | system / runtime |
| [ik_llama.cpp](catalog.md#ik-llama) | Deep fork of a general engine: compare compatibility retention and specialized quantized execution. | system / runtime |
| [Inferix](catalog.md#inferix) | Stateful world-model execution route: an adjacent case of reorganizing generation state rather than evidence of AI-built native execution. | system / runtime |
| [KernelAgent](catalog.md#kernelagent) | Agent-generated kernel and composed-workload route: a construction comparison whose integration scope must be established. | construction / generator |
| [LightX2V](catalog.md#lightx2v) | Video inference framework route: compares breadth of model integration with narrower execution designs. | system / runtime |
| [MFLUX](catalog.md#mflux) | MLX-based model implementation route: contrasts retained tensor framework with more extensive native reconstruction. | system / runtime |
| [MLC LLM](catalog.md#mlc-llm) | Compiler specialization route: establishes existing model-to-deployment construction and portability trade-offs. | construction / runtime |
| [MoE-Infinity](catalog.md#moe-infinity) | Expert-offload route: compare established prefetch and residency policies with separately reconstructed runtimes. | system / runtime |
| [OneDiff](catalog.md#onediff) | Compiler-backed pipeline adaptation: compares generated execution without reconstructing a full serving stack. | construction / compiler |
| [Petals](catalog.md#petals) | Distributed execution route: compares a different deployment contract and system boundary. | system / runtime |
| [PowerInfer](catalog.md#powerinfer) | Model/runtime co-design route: separates sparsity assumptions and changed models from construction-method effects. | system / runtime |
| [Punica](catalog.md#punica) | Multi-adapter execution route: compares workload-specific kernels and shared-model scheduling. | system / backend |
| [S-LoRA](catalog.md#s-lora) | Multi-adapter serving route: establishes prior integrated specialization of memory and batching. | system / research-prototype |
| [Sarathi-Serve](catalog.md#sarathi-serve) | Serving specialization route: compares chunked prefill and batching independently of implementation provenance. | system / research-prototype |
| [Stable Fast](catalog.md#stable-fast) | Framework compilation and capture route: compares incremental specialization and compilation amortization. | construction / compiler |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | Native diffusion framework route: compares existing cross-backend implementation and compatibility costs. | system / runtime |
| [TurboDiffusion](catalog.md#turbodiffusion) | Video acceleration route: separates distillation, precision and attention changes from runtime construction. | system / runtime |
| [VideoSys](catalog.md#videosys) | Video-serving framework route: compares reusable parallelization with narrowly reconstructed execution stacks. | system / runtime |
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

