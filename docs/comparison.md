# Comparison by artifact and semantic effect

> Generated from [projects.csv](../catalog/projects.csv). This is a capability index, not a speed or quality ranking.

[Home](../README.md) · [Full descriptions and evidence](catalog.md) · [How to read semantic labels](taxonomy.md#semantic-effects)

Modality tags refer to the inspected scope, not exhaustive compatibility. `general` marks tensor/compiler infrastructure. Hardware and model constraints are in each linked record. Source visibility does not establish license suitability.

## Data residency & movement

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) | backend / text | layout / scheduling |
| [Fiddler](catalog.md#fiddler) | research-prototype / text | layout / scheduling |
| [Flash-MoE](catalog.md#flash-moe) | research-prototype / text | reduced precision, selective approximation |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) | runtime / text | layout / scheduling, reduced precision |
| [KTransformers / kt-kernel](catalog.md#ktransformers) | backend / text | layout / scheduling |
| [MoE-Infinity](catalog.md#moe-infinity) | runtime / text | layout / scheduling |
| [Mooncake](catalog.md#mooncake) | backend / text | layout / scheduling |
| [NIXL](catalog.md#nixl) | backend / text | layout / scheduling |
| [Strata](catalog.md#strata) | runtime / text | configuration-dependent, selective approximation |
| [vAttention](catalog.md#vattention) | backend / text | layout / scheduling |
| [vLLM](catalog.md#vllm) | runtime / text | configuration-dependent |

## Numerical representation

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [bitnet.cpp](catalog.md#bitnet-cpp) | runtime / text | reduced precision, model / router training |
| [DeepCompressor](catalog.md#deepcompressor) | optimizer / text, image | reduced precision |
| [ExLlamaV3](catalog.md#exllamav3) | runtime / text | reduced precision |
| [ik_llama.cpp](catalog.md#ik-llama) | runtime / text | reduced precision |
| [Marlin](catalog.md#marlin) | kernel-library / text | reduced precision |
| [Nunchaku](catalog.md#nunchaku) | runtime / image | reduced precision |
| [QTIP](catalog.md#qtip) | optimizer / text | reduced precision |
| [SageAttention](catalog.md#sageattention) | kernel-library / text, image, video | reduced precision |
| [T-MAC](catalog.md#t-mac) | kernel-library / text | reduced precision |

## Selective computation

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [FastVideo](catalog.md#fastvideo) | runtime / video, audio | selective approximation, model / router training |
| [MInference](catalog.md#minference) | optimizer / text | selective approximation |
| [PowerInfer](catalog.md#powerinfer) | runtime / text | selective approximation, model / router training |
| [SnapKV](catalog.md#snapkv) | optimizer / text | selective approximation |
| [SpargeAttention](catalog.md#spargeattn) | kernel-library / text, image, video | selective approximation, reduced precision |
| [Sparse VideoGen](catalog.md#sparse-videogen) | research-prototype / video | selective approximation |
| [ToMe for Stable Diffusion](catalog.md#tomesd) | optimizer / image | selective approximation |
| [TurboDiffusion](catalog.md#turbodiffusion) | runtime / video | selective approximation, reduced precision, model / router training |

## Computation reuse

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [Cache-DiT](catalog.md#cache-dit) | optimizer / image, video | earlier-state reuse |
| [DeepCache](catalog.md#deepcache) | optimizer / image, video | earlier-state reuse |
| [DiTFastAttn](catalog.md#ditfastattn) | research-prototype / image, video | earlier-state reuse, selective approximation |
| [Learning-to-Cache](catalog.md#learning-to-cache) | research-prototype / image | earlier-state reuse, model / router training |
| [LMCache](catalog.md#lmcache) | backend / text | configuration-dependent |
| [MagCache](catalog.md#magcache) | optimizer / image, video | earlier-state reuse |
| [SGLang](catalog.md#sglang) | runtime / text | configuration-dependent |
| [T-GATE](catalog.md#t-gate) | optimizer / image, video | earlier-state reuse |
| [TaylorSeer](catalog.md#taylorseer) | research-prototype / image, video | earlier-state reuse |
| [TeaCache](catalog.md#teacache) | optimizer / image, video, audio | earlier-state reuse |

## Generation order

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [EAGLE](catalog.md#eagle) | optimizer / text | target-verified proposals |
| [Fast-dLLM](catalog.md#fast-dllm) | research-prototype / text, multimodal | configuration-dependent, model / router training, earlier-state reuse |
| [Inferix](catalog.md#inferix) | runtime / video | layout / scheduling |
| [Lookahead Decoding](catalog.md#lookahead) | optimizer / text | target-verified proposals |
| [Medusa](catalog.md#medusa) | research-prototype / text | configuration-dependent, model / router training |

## Parallelism & scheduling

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [AsyncDiff](catalog.md#asyncdiff) | research-prototype / image, video | earlier-state reuse |
| [DistriFusion](catalog.md#distrifusion) | research-prototype / image | earlier-state reuse |
| [DistServe](catalog.md#distserve) | research-prototype / text | layout / scheduling |
| [OpenVINO GenAI](catalog.md#openvino-genai) | runtime / text, image, video, audio, multimodal | configuration-dependent |
| [ParaAttention](catalog.md#para-attention) | optimizer / image, video | configuration-dependent, earlier-state reuse |
| [Petals](catalog.md#petals) | runtime / text | layout / scheduling |
| [Punica](catalog.md#punica) | backend / text | layout / scheduling |
| [S-LoRA](catalog.md#s-lora) | research-prototype / text | layout / scheduling |
| [Sarathi-Serve](catalog.md#sarathi-serve) | research-prototype / text | layout / scheduling |
| [TensorRT-LLM](catalog.md#tensorrt-llm) | runtime / text, multimodal | layout / scheduling |
| [VideoSys](catalog.md#videosys) | runtime / video | configuration-dependent, earlier-state reuse |
| [xDiT](catalog.md#xdit) | runtime / image, video | configuration-dependent, earlier-state reuse |

## Compiled & native execution

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [AITemplate](catalog.md#aitemplate) | compiler / text, image, general | layout / scheduling |
| [Apache TVM](catalog.md#tvm) | compiler / text, general | layout / scheduling |
| [BladeDISC](catalog.md#bladedisc) | compiler / text, image, general | layout / scheduling |
| [DeepGEMM](catalog.md#deepgemm) | kernel-library / text | layout / scheduling |
| [Draw Things Community](catalog.md#draw-things) | runtime / image, video | configuration-dependent |
| [DwarfStar](catalog.md#dwarfstar) | runtime / text | configuration-dependent |
| [edge-dit.cpp](catalog.md#edge-dit) | runtime / image, video | configuration-dependent |
| [ExecuTorch](catalog.md#executorch) | runtime / text, general | layout / scheduling |
| [Flash Linear Attention](catalog.md#flash-linear-attention) | kernel-library / text | layout / scheduling |
| [FlashAttention](catalog.md#flash-attention) | kernel-library / text | layout / scheduling |
| [FlashInfer](catalog.md#flashinfer) | kernel-library / text | layout / scheduling |
| [FlashMLA](catalog.md#flashmla) | kernel-library / text | layout / scheduling, reduced precision |
| [Halogen Flash](catalog.md#halogen-flash) · **closed core** | runtime / text | reduced precision |
| [Hidet](catalog.md#hidet) | compiler / text, image, general | layout / scheduling |
| [IREE](catalog.md#iree) | compiler / text, image, general | layout / scheduling |
| [IREE Turbine](catalog.md#iree-turbine) | compiler / text, general | layout / scheduling |
| [Iris](catalog.md#iris) | runtime / image | layout / scheduling |
| [LightX2V](catalog.md#lightx2v) | runtime / image, video, audio | configuration-dependent |
| [llama.cpp](catalog.md#llama-cpp) | runtime / text | configuration-dependent |
| [Magnitude](catalog.md#magnitude) | runtime / text | layout / scheduling |
| [MFLUX](catalog.md#mflux) | runtime / image | configuration-dependent, reduced precision |
| [Mirage Persistent Kernel](catalog.md#mirage) | compiler / text | layout / scheduling |
| [MLC LLM](catalog.md#mlc-llm) | runtime / text | layout / scheduling |
| [NVIDIA TensorRT](catalog.md#tensorrt) · **closed core** | compiler / text, image, general | layout / scheduling |
| [OneDiff](catalog.md#onediff) | compiler / image, video | layout / scheduling |
| [ONNX Runtime GenAI](catalog.md#onnxruntime-genai) | runtime / text, audio, multimodal | layout / scheduling |
| [Stable Fast](catalog.md#stable-fast) | compiler / image, video | layout / scheduling |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | runtime / image, video | configuration-dependent |
| [SwiftTransformer](catalog.md#swifttransformer) | backend / text | layout / scheduling |
| [TensorFold](catalog.md#tensorfold) | runtime / text | configuration-dependent |
| [tinygrad](catalog.md#tinygrad) | compiler / text, image, general | layout / scheduling |
| [Torch-TensorRT](catalog.md#torch-tensorrt) | backend / text, image, general | layout / scheduling |

## Construction & validation tools

| Project | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [AgentCompile](catalog.md#agentcompile) · **review-use restriction** | research-prototype / text, image | generated-artifact dependent |
| [AKG Agents](catalog.md#akg-agents) | generator / general | generated-artifact dependent |
| [FastKernels](catalog.md#fastkernels) | verification / text, image, video, audio, multimodal, general | generated-artifact dependent |
| [Helion](catalog.md#helion) | compiler / text, general | generated-artifact dependent |
| [KernelAgent](catalog.md#kernelagent) | generator / general | generated-artifact dependent |
| [KernelBench](catalog.md#kernelbench) | verification / general | generated-artifact dependent |
| [MetaInfer](catalog.md#metainfer) | generator / text | generated-artifact dependent |
| [Sol-Engine](catalog.md#sol-engine) | optimizer / image, video | generated-artifact dependent, configuration-dependent |
| [Spec-Bench](catalog.md#spec-bench) | verification / text | generated-artifact dependent |
| [TileLang](catalog.md#tilelang) | compiler / text, image, video, general | generated-artifact dependent |
| [Triton](catalog.md#triton) | compiler / text, image, video, general | generated-artifact dependent |

