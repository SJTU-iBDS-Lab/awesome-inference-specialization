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

## Library facets / 资料库的独立标签

The full mechanism-oriented index is retained below. Survey relevance and artifact role answer different questions. Modality refers to inspected scope; semantic labels identify evaluation obligations, not correctness guarantees.

<details>
<summary>Expand all project facets / 展开全部项目标签</summary>

### Data residency & movement

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) · adjacent | system / backend / text | layout / scheduling |
| [Fiddler](catalog.md#fiddler) · adjacent | system / research-prototype / text | layout / scheduling |
| [Flash-MoE](catalog.md#flash-moe) · core | system / research-prototype / text | reduced precision, selective approximation |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) · adjacent | system / runtime / text | layout / scheduling, reduced precision |
| [KTransformers / kt-kernel](catalog.md#ktransformers) · core | system / backend / text | layout / scheduling |
| [MoE-Infinity](catalog.md#moe-infinity) · adjacent | system / runtime / text | layout / scheduling |
| [Mooncake](catalog.md#mooncake) · foundation | support / backend / text | layout / scheduling |
| [NIXL](catalog.md#nixl) · foundation | support / backend / text | layout / scheduling |
| [Strata](catalog.md#strata) · core | system / runtime / text | configuration-dependent, selective approximation |
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
| [SageAttention](catalog.md#sageattention) · foundation | support / kernel-library / text, image, video | reduced precision |
| [T-MAC](catalog.md#t-mac) · foundation | support / kernel-library / text | reduced precision |

### Selective computation

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [FastVideo](catalog.md#fastvideo) · adjacent | system / runtime / video, audio | selective approximation, model / router training |
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
| [OpenVINO GenAI](catalog.md#openvino-genai) · foundation | support / runtime / text, image, video, audio, multimodal | configuration-dependent |
| [ParaAttention](catalog.md#para-attention) · foundation | support / optimizer / image, video | configuration-dependent, earlier-state reuse |
| [Petals](catalog.md#petals) · adjacent | system / runtime / text | layout / scheduling |
| [Punica](catalog.md#punica) · adjacent | system / backend / text | layout / scheduling |
| [S-LoRA](catalog.md#s-lora) · adjacent | system / research-prototype / text | layout / scheduling |
| [Sarathi-Serve](catalog.md#sarathi-serve) · adjacent | system / research-prototype / text | layout / scheduling |
| [TensorRT-LLM](catalog.md#tensorrt-llm) · foundation | support / runtime / text, multimodal | layout / scheduling |
| [VideoSys](catalog.md#videosys) · adjacent | system / runtime / video | configuration-dependent, earlier-state reuse |
| [xDiT](catalog.md#xdit) · adjacent | system / runtime / image, video | configuration-dependent, earlier-state reuse |

### Compiled & native execution

| Project / survey relevance | Artifact role / modality | Semantic considerations |
| --- | --- | --- |
| [AITemplate](catalog.md#aitemplate) · foundation | support / compiler / text, image, general | layout / scheduling |
| [Apache TVM](catalog.md#tvm) · foundation | support / compiler / text, general | layout / scheduling |
| [BladeDISC](catalog.md#bladedisc) · foundation | support / compiler / text, image, general | layout / scheduling |
| [DeepGEMM](catalog.md#deepgemm) · foundation | support / kernel-library / text | layout / scheduling |
| [Draw Things Community](catalog.md#draw-things) · adjacent | system / runtime / image, video | configuration-dependent |
| [DwarfStar](catalog.md#dwarfstar) · core | system / runtime / text | configuration-dependent |
| [edge-dit.cpp](catalog.md#edge-dit) · adjacent | system / runtime / image, video | configuration-dependent |
| [ExecuTorch](catalog.md#executorch) · foundation | support / runtime / text, general | layout / scheduling |
| [Flash Linear Attention](catalog.md#flash-linear-attention) · foundation | support / kernel-library / text | layout / scheduling |
| [FlashAttention](catalog.md#flash-attention) · foundation | support / kernel-library / text | layout / scheduling |
| [FlashInfer](catalog.md#flashinfer) · foundation | support / kernel-library / text | layout / scheduling |
| [FlashMLA](catalog.md#flashmla) · foundation | support / kernel-library / text | layout / scheduling, reduced precision |
| [Gufo](catalog.md#gufo) · core | system / runtime / text, audio, image, video, multimodal | configuration-dependent, reduced precision, target-verified proposals |
| [Halogen Flash](catalog.md#halogen-flash) · core · **closed core** | system / runtime / text | reduced precision |
| [Hidet](catalog.md#hidet) · foundation | support / compiler / text, image, general | layout / scheduling |
| [IREE](catalog.md#iree) · foundation | support / compiler / text, image, general | layout / scheduling |
| [IREE Turbine](catalog.md#iree-turbine) · foundation | support / compiler / text, general | layout / scheduling |
| [Iris](catalog.md#iris) · core | system / runtime / image | layout / scheduling |
| [LightX2V](catalog.md#lightx2v) · adjacent | system / runtime / image, video, audio | configuration-dependent |
| [llama.cpp](catalog.md#llama-cpp) · foundation | support / runtime / text | configuration-dependent |
| [Magnitude](catalog.md#magnitude) · core | system / runtime / text | layout / scheduling |
| [MFLUX](catalog.md#mflux) · adjacent | system / runtime / image | configuration-dependent, reduced precision |
| [Mirage Persistent Kernel](catalog.md#mirage) · core | construction / compiler / text | layout / scheduling |
| [MLC LLM](catalog.md#mlc-llm) · adjacent | construction / runtime / text | layout / scheduling |
| [NInfer](catalog.md#ninfer) · core | system / runtime / text, multimodal | configuration-dependent, reduced precision, target-verified proposals |
| [NVIDIA TensorRT](catalog.md#tensorrt) · foundation · **closed core** | support / compiler / text, image, general | layout / scheduling |
| [OneDiff](catalog.md#onediff) · adjacent | construction / compiler / image, video | layout / scheduling |
| [ONNX Runtime GenAI](catalog.md#onnxruntime-genai) · foundation | support / runtime / text, audio, multimodal | layout / scheduling |
| [Splash](catalog.md#splash) · core | system / runtime / text, multimodal | configuration-dependent, reduced precision, target-verified proposals |
| [Stable Fast](catalog.md#stable-fast) · adjacent | construction / compiler / image, video | layout / scheduling |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) · adjacent | system / runtime / image, video | configuration-dependent |
| [SwiftTransformer](catalog.md#swifttransformer) · foundation | support / backend / text | layout / scheduling |
| [TensorFold](catalog.md#tensorfold) · core | system / runtime / text | configuration-dependent |
| [tinygrad](catalog.md#tinygrad) · foundation | support / compiler / text, image, general | layout / scheduling |
| [Torch-TensorRT](catalog.md#torch-tensorrt) · foundation | support / backend / text, image, general | layout / scheduling |

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

