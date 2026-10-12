# Compare construction boundaries / 构建方式对照

> Generated from [cases.json](../catalog/cases.json) and [projects.csv](../catalog/projects.csv). No speed, maturity or cost ranking is implied.

[Home](../README.md) · [Core case studies](cases.md) · [Survey library](systems.md) · [Evidence policy](evidence-policy.md)

Start with what is rebuilt and what effort is disclosed. Read each case for retained components, sacrificed compatibility, AI participation, validation and maintenance. Unknown costs cannot be treated as zero; reported build effort is not a controlled comparison of development methods.

先比较执行栈边界和已披露的构建投入，再查机制。是否降低总成本，需要计入验证、集成、适配和维护，并与保留通用引擎的方案比较。

| Case | Execution ownership | Construction effort evidence |
| --- | --- | --- |
| [MetaInfer → VibeQwen](cases.md#vibeqwen) | Model execution and serving integration, evaluated as deployed services; public VibeQwen engine source was not established. | Resource usage reported; fee estimates do not establish total development cost. |
| [Sol-Engine](cases.md#sol-engine) | The reviewed artifact is an optimized video codebase and configuration workflow, not a replacement for every serving layer. | Total development tokens, GPU-hours and human maintenance costs are not disclosed in reviewed sources. |
| [Flash-MoE](cases.md#flash-moe) | Owns model inference, routing, I/O and Metal execution; this is a narrow research prototype rather than a generic loader. | The README reports a 24-hour human–AI prototype build; total lifecycle expenditure is not disclosed. |
| [DwarfStar](cases.md#dwarfstar) | Owns a narrow inference path plus CLI/server integration; it deliberately does not accept arbitrary GGUF models. | Total construction time, token usage and engineering expenditure are not disclosed in reviewed sources. |
| [Strata](cases.md#strata) | Integrates inference, memory policy and local APIs around one model family and qualified quantized layouts. | Development time, token expenditure and controlled construction-cost comparisons are not disclosed. |
| [NInfer](cases.md#ninfer) | Native operators, model programs, state/KV management, scheduling and CLI/HTTP serving form one execution stack. | Development effort and lifecycle costs are not disclosed; inference throughput does not establish construction economics. |
| [Splash](cases.md#splash) | C++/Metal code owns target/draft execution, kernels, scheduling and state management; a Python frontend exposes compatible HTTP APIs and vision input. | No development-effort or total lifecycle-cost accounting was found; throughput measurements do not establish cheaper construction. |
| [llamAmpere](cases.md#llamampere) | A substantial llama.cpp/TurboQuant fork changes kernels, speculative execution and state management; it is not a runtime built from scratch. | Development effort, agent expenditure and total maintenance cost are not disclosed in the reviewed sources. |
| [Gufo](cases.md#gufo) | Owns model execution, kernels, sessions and local serving. Text/vision, ASR/TTS, image generation and video paths have different qualification levels. | Total development effort, human hours, agent tokens and long-term maintenance expenditure are not disclosed in the reviewed material. |
| [Iris](cases.md#iris) | Implements text encoding, diffusion-transformer execution and image decoding for selected FLUX and Z-Image variants. | Construction time, AI-token spending and maintenance economics are not disclosed in reviewed sources. |
| [TensorFold](cases.md#tensorfold) | Owns loading, tokenization, serving and execution for admitted combinations; experimental Living Weights is a separate model-changing feature. | Development time, token/GPU expenditure and long-term engineering costs are not disclosed. |
| [Halogen Flash](cases.md#halogen-flash) | Public material exposes deployment and behavior; the core engine and complete tensor-level quantization choices are not publicly inspectable. | Development time, token usage and engineering costs are not disclosed in reviewed sources. |
| [Magnitude](cases.md#magnitude) | The inspected kernel layer owns planning and generated entry points, not a second device runtime or independent scheduler. | Total development effort and amortization of device-specific tuning are not disclosed in reviewed sources. |
| [KTransformers](cases.md#ktransformers) | The reviewed kt-kernel path is an integrated backend; it is distinct from legacy injection examples and separate training features. | Hardware configurations are documented; controlled construction-time and maintenance-cost accounting is not disclosed. |
| [Nunchaku](cases.md#nunchaku) | Implements specialized diffusion-model execution components and integrations; it does not replace all text encoding, decoding or application layers. | Calibration and conversion are preparation work; developer effort and total construction economics are not disclosed. |
| [ExLlamaV3](cases.md#exllamav3) | Provides model execution and generation machinery; the recommended OpenAI-compatible server is the separate TabbyAPI project. | The README reports conversion in minutes to hours on a high-end consumer GPU, depending on model size; total engineering costs are unknown. |
| [Mirage MPK](cases.md#mirage) | This case covers the MPK branch and its supported task graph, not automatic support for arbitrary Hugging Face models. | End-to-end construction, tuning and maintenance costs are not disclosed in reviewed sources. |
| [Lily](cases.md#lily) | Owns checkpoint validation, model graph, kernels, generation and a small session cache. | Development hours, total cost and maintenance effort are not disclosed. |
| [Lithos Metal](cases.md#lithos-metal) | Owns typed IR, fusion, memory planning, kernel emission, program ABI and generation-state replay. | Development hours, total cost and maintenance effort are not disclosed. |
| [Saragossa](cases.md#saragossa) | Owns model forward paths, Metal dispatch, KV/recurrent state, scratch lifetimes and prefix snapshots. | Development hours, total cost and maintenance effort are not disclosed. |
| [TurboFieldfare](cases.md#turbo-fieldfare) | Owns expert packaging, installation, residency, prefill/decode scheduling and model-specific kernels. | The curated inventory records 103 experiments, not total developer time or monetary cost. |
| [TUFF](cases.md#tuff) | Owns native model execution, expert I/O, memory policy and the model-owning decode service. | Development hours, total cost and maintenance effort are not disclosed. |
| [Colibri](cases.md#colibri) | Owns per-family forward paths, container readers, routed expert stores and optional device tiers. | Development hours, total cost and maintenance effort are not disclosed. |
| [ane.cpp](cases.md#ane-cpp) | Owns MIL kernel construction, private API invocation, persistent compilation caches and CPU/ANE dispatch boundaries. | Development hours, total cost and maintenance effort are not disclosed. |
| [Swiftlet](cases.md#swiftlet) | Owns CPU/Metal model paths, qpack conversion, expert cache and chat-state integration. | Development hours, total cost and maintenance effort are not disclosed. |
| [SwiftLM](cases.md#swiftlm) | The case covers the SSD expert path and its integration; it is not a claim that every server feature is a new execution stack. | Development hours, total cost and maintenance effort are not disclosed. |
| [ANEMLL Flash llama.cpp](cases.md#anemll-flash-llama) | Changes model loading, runtime slot ownership and routed graph inputs; other engine services remain shared. | Development hours, total cost and maintenance effort are not disclosed. |
| [hipEngine](cases.md#hipengine) | Owns model loading, HIP dispatch, generation, shared KV state, batching and HTTP serving. | Worklogs expose experiments and rejected routes, but total human effort, agent expenditure and maintenance cost remain unknown. |
| [VTE](cases.md#vte) | Owns loading, kernel generation, allocation, graph execution, sampling and serving rather than launching another inference engine. | The iteration history is visible; total engineering hours, token costs and long-term maintenance effort are not reported. |
| [ZINC](cases.md#zinc) | Owns GGUF loading, tokenization, forward/decode orchestration, KV state and the local API server. | Build and benchmark procedures are public; total development and maintenance expenditure is unknown. |
| [imp](cases.md#imp) | Owns loaders, tokenization, model execution, KV planning, graph scheduling and the serving interfaces. | Published iteration records do not establish total tokens, human oversight time or lifetime maintenance cost. |
| [memra](cases.md#memra) | Owns native model programs, kernel dispatch, KV/speculative state, placement and serving admission. | Hardware and experimental details are disclosed; total development tokens, labor and maintenance costs remain unknown. |
| [Kipp](cases.md#kipp) | Owns loading, CPU reference execution, GPU interfaces, KV sessions, batching and HTTP serving. | No complete development-hour, token or maintenance-cost accounting was found. |
| [vLLM Radiance](cases.md#vllm-radiance) | Replaces attention, recurrent, GEMM and collective paths through native kernels and guarded vLLM overlays. | The README says a full stack build takes hours; that is build latency, not total development effort. |
| [NInfer-3090](cases.md#ninfer-3090) | Retains NInfer architecture but changes SM86 quantized execution, memory profiles, state transactions and speculative scheduling. | Release and migration histories are public, but total porting and maintenance effort is unknown. |
| [Infernix](cases.md#infernix) | Adds expert residency, CPU miss execution, transfer overlap, NVMe embedding access and request-state handling to NInfer. | A coding-tool subscription is acknowledged, but total tokens, human oversight and hardware expenditure are not reported. |
| [CIRU runtime](cases.md#ciru-runtime) | Modifies llama.cpp loading, embedding paging, expert execution, QSA and MTP state handling while retaining its server. | Build identities and qualification records are visible; total development and maintenance expenditure is not disclosed. |
| [Gufo RDMA](cases.md#gufo-rdma) | Adds tensor partitioning, communication and mirrored serving/snapshot transactions around Gufo’s model execution. | No total engineering effort, AI-token budget or maintenance-cost comparison with single-host Gufo is disclosed. |
| [Llaminar](cases.md#llaminar) | Owns model graphs, placement plans, kernels, captured execution and tensor/pipeline/expert coordination. | Planning and build procedures are public, but total engineering effort and maintenance economics are unknown. |
| [strix-llama.cpp](cases.md#strix-llama-cpp) | Replaces selected Vulkan/HIP kernels, fusion and speculative-state paths while retaining llama.cpp model and serving infrastructure. | Contribution and benchmark requirements are documented; total development, integration and maintenance effort are unknown. |
| [Cactus](cases.md#cactus) | Owns model-bundle execution, component graphs, state handling and ARM/Metal kernels; inspected model code manages quantized cross-attention state and component boundaries. | No comparable total engineering effort, porting cost or maintenance-cost measurement was found in the inspected sources. |
| [FastFlowLM](cases.md#fastflowlm) | Public host runtimes own backend selection, model loading, device tensors and decode streams. The original flm model engines remain prebuilt libraries. | The public development history records releases and organizational evolution, but does not establish person-hours or a controlled construction-cost comparison. |
| [zLLM](cases.md#zllm) | Owns Rust model runtimes, vision processing, state and backend dispatch. Inspected ROCm paths implement FLUX conditioning/denoising and SeedVR2 distributed video computation. | Engineering effort and per-model adaptation cost are not quantified in the inspected sources; growing model coverage alone does not measure cheaper development. |
| [Qwen-ASR](cases.md#qwen-asr-c) | Owns waveform preprocessing, encoder graph, decoder prompt construction and incremental transcription; serving interfaces sit outside that model boundary. | Total implementation effort, agent tokens, compute expenditure and maintenance cost are not disclosed in the reviewed sources. |
| [Qwen3-TTS](cases.md#qwen3-tts-c) | Owns talker, residual code prediction, speech decoding and streaming integration; these are model execution components rather than an API wrapper. | Overall human effort, agent usage and maintenance costs are undisclosed; profiling evidence is not a development-cost measurement. |
| [Qingming Qwen3-TTS](cases.md#qingming-qwen3-tts) | Owns device operators, model sequencing, memory capacities and resident generation/decoder scheduling for the supported model sizes. | Total development and maintenance effort are unknown; a narrowly targeted implementation alone is not evidence that building it was cheaper. |
| [VoxGen](cases.md#voxgen) | Owns language/acoustic stages, audio decoding, request state and incremental PCM production, plus Vulkan memory and shader dispatch. | Build effort, agent expenditure and long-term maintenance cost are undisclosed; runtime throughput cannot substitute for those measurements. |
| [parakeet.cpp (ggml)](cases.md#parakeet-ggml) | Owns model loading, FastConformer execution, CTC/transducer decoding and streaming session state, beyond binding to an existing speech service. | Total construction effort and maintenance cost are unknown; neither code volume nor the number of supported checkpoints answers that question. |
| [parakeet.cpp (axiom)](cases.md#parakeet-axiom) | Owns FastConformer modules, decoder integration and cache-aware convolution/attention; it is separate from the similarly named ggml implementation. | Total porting time, developer effort and ongoing maintenance cost are not disclosed in the reviewed evidence. |
| [Aria](cases.md#aria) | Owns text conditioning, diffusion-model execution, noise schedule, sampling and waveform decoding; this is a complete audio-generation artifact. | Total human effort, token usage, compute cost and maintenance expenditure are undisclosed; the disclosure does not establish reduced total cost. |
| [vla.simd](cases.md#vla-simd) | Owns tensor operators, model adapters, weight loading and action computation; Python robot integration remains outside that native execution boundary. | Total engineering effort, agent costs and maintenance burden are unknown, despite public per-device benchmark and development records. |
| [Hearth](cases.md#hearth) | Owns SD-family conditioning, UNet, VAE, sampling and node-graph execution; external compatibility APIs are interfaces to that implementation. | Total development effort and maintenance cost are unknown; a single-binary interface is not evidence that the implementation was inexpensive. |
| [brodiffusion](cases.md#brodiffusion) | Owns diffusion model graphs, conditioning integration, sampling and step-graph lifecycle; the reviewed image path is broader than an isolated kernel. | Overall developer time, agent usage and maintenance costs are undisclosed; backend reuse cannot by itself quantify the savings. |
| [stable-diffusion.rs](cases.md#stable-diffusion-rs) | Owns model graphs, sampling and weight interpretation; current MLX model code is separated from a small tensor/backend interface. | Total implementation, migration and maintenance costs are unknown; architectural notes provide process evidence rather than a measured cost comparison. |
| [MiniMax-H3 MLX](cases.md#minimax-h3-mlx) | Owns packed video/audio geometry, conditioning, DiT, samplers and both VAEs; model-specific AdaLN precomputation changes execution and residency. | Total porting effort and maintenance cost are undisclosed; runtime measurements and model-size reductions are not development-cost evidence. |
| [Vidax](cases.md#vidax) | Owns model implementations, checkpoint translation, samplers and sharding decisions, while compiled primitives and collectives remain in the JAX stack. | Total engineering and maintenance cost are unknown; compile or inference timings do not measure the effort of constructing a port. |
| [TeleFuser](cases.md#telefuser) | Owns model pipelines and denoising stages; the inspected LingBot streaming service adds actor dataflow, backpressure, session ordering and resource-group execution leases. | Total developer effort, agent use and maintenance cost are not disclosed; serving capacity or delivered FPS cannot quantify construction cost. |
| [StreamDiffusionV2](cases.md#streamdiffusion-v2) | Owns chunk encode/denoise/decode flow, streaming state and distributed cache ownership; the source includes cache transfer when stage ownership changes. | Total implementation and maintenance cost are unknown; paper latency results are not a measure of engineering effort. |
| [Quartz](cases.md#saient-quartz) | Owns Rust tensor execution, SD-family stages and committed Wan orchestration; the mobile Wan demonstration additionally uses a separate companion binary. | Total development effort and maintenance cost are unknown; code size and successful demonstrations do not establish lower construction cost. |
| [edge-dit.cpp](cases.md#edge-dit) | Owns native model graphs, component lifecycle, graph segmentation and staged execution rather than merely attaching one offload option to a general pipeline. | Total development, porting and maintenance costs are unknown; reduced memory requirements do not measure construction economics. |
| [stable-diffusion.cpp](cases.md#stable-diffusion-cpp) | Owns conditioning, diffusion, VAE and video orchestration, plus model-specific loading and execution decisions; this is an integrated runtime boundary. | Total engineering and maintenance effort is unknown; historical continuity makes this a useful within-core comparison rather than a cost-reduction claim. |
| [LightX2V](cases.md#lightx2v) | Owns model-specific inference and operator storage contracts, plus planned weight layouts, prefetch streams and two-slot device buffers. | Total development and maintenance costs are undisclosed; maximum reported speedups do not quantify construction effort. |
| [FastVideo](cases.md#fastvideo) | Owns model implementations, registries, component loaders and staged denoising; training and distillation workflows are distinct from this inference boundary. | Total construction and maintenance effort is unknown; training and inference performance metrics cannot substitute for those measurements. |

## Library facets / 资料库的独立标签

The full mechanism-oriented index is retained below. Survey relevance and artifact role answer different questions. Modality refers to inspected scope; semantic labels identify evaluation obligations, not correctness guarantees.

<details>
<summary>Expand all project facets / 展开全部项目标签</summary>

### Data residency & movement

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [ANEMLL Flash llama.cpp](catalog.md#anemll-flash-llama) · core | system / backend / text | configuration-dependent |
| [Colibri](catalog.md#colibri) · core | system / runtime / text, image, multimodal | configuration-dependent |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) · adjacent | system / backend / text | layout / scheduling |
| [Fiddler](catalog.md#fiddler) · adjacent | system / research-prototype / text | layout / scheduling |
| [Flash-MoE](catalog.md#flash-moe) · core | system / research-prototype / text | reduced precision, selective approximation |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) · adjacent | system / runtime / text | layout / scheduling, reduced precision |
| [HybriMoE](catalog.md#hybrimoe) · adjacent | system / research-prototype / text | layout / scheduling |
| [Infernix](catalog.md#infernix) · core | system / runtime / text, multimodal | configuration-dependent |
| [KTransformers / kt-kernel](catalog.md#ktransformers) · core | system / backend / text | layout / scheduling |
| [MoE-Infinity](catalog.md#moe-infinity) · adjacent | system / runtime / text | layout / scheduling |
| [Mooncake](catalog.md#mooncake) · foundation | support / backend / text | layout / scheduling |
| [NIXL](catalog.md#nixl) · foundation | support / backend / text | layout / scheduling |
| [Strata](catalog.md#strata) · core | system / runtime / text | configuration-dependent, selective approximation |
| [Swiftlet](catalog.md#swiftlet) · core | system / runtime / text | configuration-dependent |
| [SwiftLM](catalog.md#swiftlm) · core | system / backend / text, multimodal | configuration-dependent |
| [TUFF](catalog.md#tuff) · core | system / runtime / text, multimodal | configuration-dependent |
| [TurboFieldfare](catalog.md#turbo-fieldfare) · core | system / runtime / text, multimodal | configuration-dependent |
| [vAttention](catalog.md#vattention) · foundation | support / backend / text | layout / scheduling |
| [vLLM](catalog.md#vllm) · foundation | support / runtime / text | configuration-dependent |

### Numerical representation

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [bitnet.cpp](catalog.md#bitnet-cpp) · adjacent | system / runtime / text | reduced precision, model / router training |
| [DeepCompressor](catalog.md#deepcompressor) · foundation | support / optimizer / text, image | reduced precision |
| [ExLlamaV3](catalog.md#exllamav3) · core | system / runtime / text | reduced precision |
| [ik_llama.cpp](catalog.md#ik-llama) · adjacent | system / runtime / text | reduced precision |
| [Marlin](catalog.md#marlin) · foundation | support / kernel-library / text | reduced precision |
| [Nunchaku](catalog.md#nunchaku) · core | system / runtime / image | reduced precision |
| [QTIP](catalog.md#qtip) · foundation | support / optimizer / text | reduced precision |
| [ROCmFPX](catalog.md#rocmfpx) · adjacent | system / backend / text | reduced precision |
| [SageAttention](catalog.md#sageattention) · foundation | support / kernel-library / text, image, video | reduced precision |
| [T-MAC](catalog.md#t-mac) · foundation | support / kernel-library / text | reduced precision |

### Selective computation

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [MInference](catalog.md#minference) · foundation | support / optimizer / text | selective approximation |
| [PowerInfer](catalog.md#powerinfer) · adjacent | system / runtime / text | selective approximation, model / router training |
| [SnapKV](catalog.md#snapkv) · foundation | support / optimizer / text | selective approximation |
| [SpargeAttention](catalog.md#spargeattn) · foundation | support / kernel-library / text, image, video | selective approximation, reduced precision |
| [Sparse VideoGen](catalog.md#sparse-videogen) · foundation | support / research-prototype / video | selective approximation |
| [ToMe for Stable Diffusion](catalog.md#tomesd) · foundation | support / optimizer / image | selective approximation |
| [TurboDiffusion](catalog.md#turbodiffusion) · adjacent | system / runtime / video | selective approximation, reduced precision, model / router training |

### Computation reuse

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [Cache-DiT](catalog.md#cache-dit) · foundation | support / optimizer / image, video | earlier-state reuse |
| [DeepCache](catalog.md#deepcache) · foundation | support / optimizer / image, video | earlier-state reuse |
| [DiTFastAttn](catalog.md#ditfastattn) · foundation | support / research-prototype / image, video | earlier-state reuse, selective approximation |
| [Learning-to-Cache](catalog.md#learning-to-cache) · foundation | support / research-prototype / image | earlier-state reuse, model / router training |
| [LMCache](catalog.md#lmcache) · foundation | support / backend / text | configuration-dependent |
| [MagCache](catalog.md#magcache) · foundation | support / optimizer / image, video | earlier-state reuse |
| [SGLang](catalog.md#sglang) · foundation | support / runtime / text | configuration-dependent |
| [T-GATE](catalog.md#t-gate) · foundation | support / optimizer / image, video | earlier-state reuse |
| [TaylorSeer](catalog.md#taylorseer) · foundation | support / research-prototype / image, video | earlier-state reuse |
| [TeaCache](catalog.md#teacache) · foundation | support / optimizer / image, video, audio | earlier-state reuse |

### Generation order

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [EAGLE](catalog.md#eagle) · foundation | support / optimizer / text | target-verified proposals |
| [Fast-dLLM](catalog.md#fast-dllm) · foundation | support / research-prototype / text, multimodal | configuration-dependent, model / router training, earlier-state reuse |
| [Inferix](catalog.md#inferix) · adjacent | system / runtime / video | layout / scheduling |
| [llamAmpere](catalog.md#llamampere) · core | system / runtime / text | target-verified proposals, reduced precision, model / router training |
| [Lookahead Decoding](catalog.md#lookahead) · foundation | support / optimizer / text | target-verified proposals |
| [Medusa](catalog.md#medusa) · foundation | support / research-prototype / text | configuration-dependent, model / router training |

### Parallelism & scheduling

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [AsyncDiff](catalog.md#asyncdiff) · adjacent | system / research-prototype / image, video | earlier-state reuse |
| [DistriFusion](catalog.md#distrifusion) · adjacent | system / research-prototype / image | earlier-state reuse |
| [DistServe](catalog.md#distserve) · adjacent | system / research-prototype / text | layout / scheduling |
| [Gufo RDMA](catalog.md#gufo-rdma) · core | system / runtime / text, multimodal | configuration-dependent |
| [Llaminar](catalog.md#llaminar) · core | system / runtime / text | configuration-dependent |
| [OpenVINO GenAI](catalog.md#openvino-genai) · foundation | support / runtime / text, image, video, audio, multimodal | configuration-dependent |
| [ParaAttention](catalog.md#para-attention) · foundation | support / optimizer / image, video | configuration-dependent, earlier-state reuse |
| [Petals](catalog.md#petals) · adjacent | system / runtime / text | layout / scheduling |
| [Punica](catalog.md#punica) · adjacent | system / backend / text | layout / scheduling |
| [S-LoRA](catalog.md#s-lora) · adjacent | system / research-prototype / text | layout / scheduling |
| [Sarathi-Serve](catalog.md#sarathi-serve) · adjacent | system / research-prototype / text | layout / scheduling |
| [StreamDiffusion](catalog.md#streamdiffusion) · adjacent | system / runtime / image, video | layout / scheduling, selective approximation, model / router training |
| [StreamDiffusionV2](catalog.md#streamdiffusion-v2) · core | system / runtime / video | layout / scheduling, model / router training, configuration-dependent |
| [TeleFuser](catalog.md#telefuser) · core | system / runtime / video, image, audio, multimodal | configuration-dependent |
| [TensorRT-LLM](catalog.md#tensorrt-llm) · foundation | support / runtime / text, multimodal | layout / scheduling |
| [VideoSys](catalog.md#videosys) · adjacent | system / runtime / video | configuration-dependent, earlier-state reuse |
| [xDiT](catalog.md#xdit) · adjacent | system / runtime / image, video | configuration-dependent, earlier-state reuse |

### Compiled & native execution

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [AITemplate](catalog.md#aitemplate) · foundation | support / compiler / text, image, general | layout / scheduling |
| [ANE-LM](catalog.md#ane-lm) · adjacent | system / runtime / text | configuration-dependent |
| [ane.cpp](catalog.md#ane-cpp) · core | system / runtime / text | configuration-dependent |
| [ANEMLL](catalog.md#anemll) · adjacent | construction / compiler / text | configuration-dependent |
| [Apache TVM](catalog.md#tvm) · foundation | support / compiler / text, general | layout / scheduling |
| [Aria](catalog.md#aria) · core | system / runtime / audio | configuration-dependent |
| [BaseRT](catalog.md#basert) · adjacent · **closed core** | system / runtime / text, multimodal | configuration-dependent |
| [BladeDISC](catalog.md#bladedisc) · foundation | support / compiler / text, image, general | layout / scheduling |
| [BRaiN](catalog.md#brain) · adjacent | system / runtime / text, image, video, audio, multimodal | configuration-dependent |
| [brodiffusion](catalog.md#brodiffusion) · core | system / runtime / image | configuration-dependent |
| [Cactus](catalog.md#cactus) · core | system / runtime / text, image, audio, multimodal | layout / scheduling, reduced precision, configuration-dependent |
| [Cactus Needle](catalog.md#needle) · adjacent · **closed core** | system / runtime / text, audio | model / router training, reduced precision |
| [CIRU runtime](catalog.md#ciru-runtime) · core | system / backend / text, multimodal | configuration-dependent |
| [CoreML LLM CLI](catalog.md#coreml-llm-cli) · adjacent | system / research-prototype / text | configuration-dependent |
| [DeepGEMM](catalog.md#deepgemm) · foundation | support / kernel-library / text | layout / scheduling |
| [diffusion-rs](catalog.md#diffusion-rs) · adjacent | system / runtime / image | configuration-dependent |
| [Draw Things Community](catalog.md#draw-things) · adjacent | system / runtime / image, video | configuration-dependent |
| [DwarfStar](catalog.md#dwarfstar) · core | system / runtime / text | configuration-dependent |
| [edge-dit.cpp](catalog.md#edge-dit) · core | system / runtime / image, video | configuration-dependent |
| [ExecuTorch](catalog.md#executorch) · foundation | support / runtime / text, general | layout / scheduling |
| [FastFlowLM](catalog.md#fastflowlm) · core · **closed core** | system / runtime / text, audio, image, multimodal | configuration-dependent |
| [FastVideo](catalog.md#fastvideo) · core | system / runtime / video, audio | configuration-dependent |
| [Flash Linear Attention](catalog.md#flash-linear-attention) · foundation | support / kernel-library / text | layout / scheduling |
| [FlashAttention](catalog.md#flash-attention) · foundation | support / kernel-library / text | layout / scheduling |
| [FlashInfer](catalog.md#flashinfer) · foundation | support / kernel-library / text | layout / scheduling |
| [FlashMLA](catalog.md#flashmla) · foundation | support / kernel-library / text | layout / scheduling, reduced precision |
| [Gufo](catalog.md#gufo) · core | system / runtime / text, audio, image, video, multimodal | configuration-dependent, reduced precision, target-verified proposals |
| [Halogen Flash](catalog.md#halogen-flash) · core · **closed core** | system / runtime / text | reduced precision |
| [Hearth](catalog.md#hearth) · core | system / runtime / image | configuration-dependent |
| [Hidet](catalog.md#hidet) · foundation | support / compiler / text, image, general | layout / scheduling |
| [Hilum LLM Engine](catalog.md#hilum-engine) · adjacent | system / backend / text, multimodal | configuration-dependent |
| [hipEngine](catalog.md#hipengine) · core | system / runtime / text, multimodal, audio | configuration-dependent |
| [imp](catalog.md#imp) · core | system / runtime / text, multimodal | configuration-dependent |
| [IREE](catalog.md#iree) · foundation | support / compiler / text, image, general | layout / scheduling |
| [IREE Turbine](catalog.md#iree-turbine) · foundation | support / compiler / text, general | layout / scheduling |
| [Iris](catalog.md#iris) · core | system / runtime / image | layout / scheduling |
| [Kipp](catalog.md#kipp) · core | system / runtime / text | configuration-dependent |
| [LightX2V](catalog.md#lightx2v) · core | system / runtime / image, video, audio | configuration-dependent |
| [Lily](catalog.md#lily) · core | system / runtime / text | configuration-dependent |
| [Lithos Metal](catalog.md#lithos-metal) · core | system / runtime / text | configuration-dependent, target-verified proposals |
| [llama.cpp](catalog.md#llama-cpp) · foundation | support / runtime / text | configuration-dependent |
| [Magnitude](catalog.md#magnitude) · core | system / runtime / text | layout / scheduling |
| [memra](catalog.md#memra) · core | system / runtime / text, multimodal | configuration-dependent |
| [MetalChat](catalog.md#metalchat) · adjacent | system / runtime / text | configuration-dependent |
| [MFLUX](catalog.md#mflux) · adjacent | system / runtime / image | configuration-dependent, reduced precision |
| [MiniMax-H3 MLX](catalog.md#minimax-h3-mlx) · core | system / runtime / video, audio | configuration-dependent |
| [Mirage Persistent Kernel](catalog.md#mirage) · core | construction / compiler / text | layout / scheduling |
| [MLC LLM](catalog.md#mlc-llm) · adjacent | construction / runtime / text | layout / scheduling |
| [NInfer](catalog.md#ninfer) · core | system / runtime / text, multimodal | configuration-dependent, reduced precision, target-verified proposals |
| [NInfer-3090](catalog.md#ninfer-3090) · core | system / runtime / text, multimodal | configuration-dependent |
| [NVIDIA TensorRT](catalog.md#tensorrt) · foundation · **closed core** | support / compiler / text, image, general | layout / scheduling |
| [OneDiff](catalog.md#onediff) · adjacent | construction / compiler / image, video | layout / scheduling |
| [ONNX Runtime GenAI](catalog.md#onnxruntime-genai) · foundation | support / runtime / text, audio, multimodal | layout / scheduling |
| [parakeet.cpp (axiom)](catalog.md#parakeet-axiom) · core | system / runtime / audio | configuration-dependent |
| [parakeet.cpp (ggml)](catalog.md#parakeet-ggml) · core | system / runtime / audio | configuration-dependent |
| [PMetal](catalog.md#pmetal) · adjacent | system / runtime / general | configuration-dependent |
| [Qingming Qwen3-TTS](catalog.md#qingming-qwen3-tts) · core | system / runtime / audio | configuration-dependent |
| [Quartz](catalog.md#saient-quartz) · core | system / runtime / text, image, video | configuration-dependent |
| [Qwen-ASR (C)](catalog.md#qwen-asr-c) · core | system / runtime / audio | configuration-dependent |
| [Qwen3-TTS (C)](catalog.md#qwen3-tts-c) · core | system / runtime / audio | configuration-dependent |
| [Saragossa](catalog.md#saragossa) · core | system / runtime / text, audio | configuration-dependent |
| [Splash](catalog.md#splash) · core | system / runtime / text, multimodal | configuration-dependent, reduced precision, target-verified proposals |
| [Stable Fast](catalog.md#stable-fast) · adjacent | construction / compiler / image, video | layout / scheduling |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) · core | system / runtime / image, video | configuration-dependent |
| [stable-diffusion.rs](catalog.md#stable-diffusion-rs) · core | system / runtime / image | configuration-dependent |
| [strix-llama.cpp](catalog.md#strix-llama-cpp) · core | system / backend / text, multimodal | configuration-dependent |
| [SwiftTransformer](catalog.md#swifttransformer) · foundation | support / backend / text | layout / scheduling |
| [TensorFold](catalog.md#tensorfold) · core | system / runtime / text | configuration-dependent |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) · adjacent | system / runtime / text, image, audio, multimodal | configuration-dependent |
| [tinygrad](catalog.md#tinygrad) · foundation | support / compiler / text, image, general | layout / scheduling |
| [Torch-TensorRT](catalog.md#torch-tensorrt) · foundation | support / backend / text, image, general | layout / scheduling |
| [Uzu](catalog.md#uzu) · adjacent | system / runtime / text | configuration-dependent |
| [Vidax](catalog.md#vidax) · core | system / runtime / video | configuration-dependent |
| [vla.simd](catalog.md#vla-simd) · core | system / runtime / multimodal | configuration-dependent |
| [vLLM Radiance](catalog.md#vllm-radiance) · core | system / backend / text, multimodal | configuration-dependent |
| [VoxGen](catalog.md#voxgen) · core | system / runtime / audio | layout / scheduling, reduced precision |
| [VTE](catalog.md#vte) · core | system / runtime / text | configuration-dependent |
| [whisper.cpp](catalog.md#whisper-cpp) · adjacent | system / runtime / audio | configuration-dependent |
| [WhisperKit](catalog.md#whisperkit) · adjacent | system / runtime / audio | configuration-dependent |
| [ZINC](catalog.md#zinc) · core | system / runtime / text | configuration-dependent |
| [zLLM](catalog.md#zllm) · core | system / runtime / text, image, video, audio, multimodal | layout / scheduling, reduced precision, configuration-dependent |

### Construction & validation tools

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [AgentCompile](catalog.md#agentcompile) · adjacent · **review-use restriction** | construction / research-prototype / text, image | generated-artifact dependent |
| [AKG Agents](catalog.md#akg-agents) · adjacent | construction / generator / general | generated-artifact dependent |
| [FastKernels](catalog.md#fastkernels) · foundation | support / verification / text, image, video, audio, multimodal, general | generated-artifact dependent |
| [Helion](catalog.md#helion) · foundation | support / compiler / text, general | generated-artifact dependent |
| [KernelAgent](catalog.md#kernelagent) · adjacent | construction / generator / general | generated-artifact dependent |
| [KernelBench](catalog.md#kernelbench) · foundation | support / verification / general | generated-artifact dependent |
| [MetaInfer](catalog.md#metainfer) · core | construction / generator / text | generated-artifact dependent |
| [Sol-Engine](catalog.md#sol-engine) · core | construction / optimizer / image, video | generated-artifact dependent, configuration-dependent |
| [Spec-Bench](catalog.md#spec-bench) · foundation | support / verification / text | generated-artifact dependent |
| [TileLang](catalog.md#tilelang) · foundation | support / compiler / text, image, video, general | generated-artifact dependent |
| [Triton](catalog.md#triton) · foundation | support / compiler / text, image, video, general | generated-artifact dependent |

</details>

