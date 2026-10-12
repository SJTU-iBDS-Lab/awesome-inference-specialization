# Comparison by artifact and semantic effect

> Generated from [projects.csv](../catalog/projects.csv). This is a capability index, not a speed or quality ranking.

[Home](../README.md) · [Systems & construction](systems.md) · [Full descriptions and evidence](catalog.md) · [How to read semantic labels](taxonomy.md#semantic-effects)

Reading roles identify systems, construction workflows and supporting references. Modality tags refer to the inspected scope, not exhaustive compatibility. `general` marks tensor/compiler infrastructure. Hardware and model constraints are in each linked record. Source visibility does not establish license suitability.

## Data residency & movement

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) · system | backend / text | layout / scheduling |
| [Fiddler](catalog.md#fiddler) · system | research-prototype / text | layout / scheduling |
| [Flash-MoE](catalog.md#flash-moe) · system | research-prototype / text | reduced precision, selective approximation |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) · system | runtime / text | layout / scheduling, reduced precision |
| [KTransformers / kt-kernel](catalog.md#ktransformers) · system | backend / text | layout / scheduling |
| [MoE-Infinity](catalog.md#moe-infinity) · system | runtime / text | layout / scheduling |
| [Mooncake](catalog.md#mooncake) · support | backend / text | layout / scheduling |
| [NIXL](catalog.md#nixl) · support | backend / text | layout / scheduling |
| [Strata](catalog.md#strata) · system | runtime / text | configuration-dependent, selective approximation |
| [vAttention](catalog.md#vattention) · support | backend / text | layout / scheduling |
| [vLLM](catalog.md#vllm) · support | runtime / text | configuration-dependent |

## Numerical representation

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [bitnet.cpp](catalog.md#bitnet-cpp) · system | runtime / text | reduced precision, model / router training |
| [DeepCompressor](catalog.md#deepcompressor) · support | optimizer / text, image | reduced precision |
| [ExLlamaV3](catalog.md#exllamav3) · system | runtime / text | reduced precision |
| [ik_llama.cpp](catalog.md#ik-llama) · system | runtime / text | reduced precision |
| [Marlin](catalog.md#marlin) · support | kernel-library / text | reduced precision |
| [Nunchaku](catalog.md#nunchaku) · system | runtime / image | reduced precision |
| [QTIP](catalog.md#qtip) · support | optimizer / text | reduced precision |
| [SageAttention](catalog.md#sageattention) · support | kernel-library / text, image, video | reduced precision |
| [T-MAC](catalog.md#t-mac) · support | kernel-library / text | reduced precision |

## Selective computation

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [FastVideo](catalog.md#fastvideo) · system | runtime / video, audio | selective approximation, model / router training |
| [MInference](catalog.md#minference) · support | optimizer / text | selective approximation |
| [PowerInfer](catalog.md#powerinfer) · system | runtime / text | selective approximation, model / router training |
| [SnapKV](catalog.md#snapkv) · support | optimizer / text | selective approximation |
| [SpargeAttention](catalog.md#spargeattn) · support | kernel-library / text, image, video | selective approximation, reduced precision |
| [Sparse VideoGen](catalog.md#sparse-videogen) · support | research-prototype / video | selective approximation |
| [ToMe for Stable Diffusion](catalog.md#tomesd) · support | optimizer / image | selective approximation |
| [TurboDiffusion](catalog.md#turbodiffusion) · system | runtime / video | selective approximation, reduced precision, model / router training |

## Computation reuse

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [Cache-DiT](catalog.md#cache-dit) · support | optimizer / image, video | earlier-state reuse |
| [DeepCache](catalog.md#deepcache) · support | optimizer / image, video | earlier-state reuse |
| [DiTFastAttn](catalog.md#ditfastattn) · support | research-prototype / image, video | earlier-state reuse, selective approximation |
| [Learning-to-Cache](catalog.md#learning-to-cache) · support | research-prototype / image | earlier-state reuse, model / router training |
| [LMCache](catalog.md#lmcache) · support | backend / text | configuration-dependent |
| [MagCache](catalog.md#magcache) · support | optimizer / image, video | earlier-state reuse |
| [SGLang](catalog.md#sglang) · support | runtime / text | configuration-dependent |
| [T-GATE](catalog.md#t-gate) · support | optimizer / image, video | earlier-state reuse |
| [TaylorSeer](catalog.md#taylorseer) · support | research-prototype / image, video | earlier-state reuse |
| [TeaCache](catalog.md#teacache) · support | optimizer / image, video, audio | earlier-state reuse |

## Generation order

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [EAGLE](catalog.md#eagle) · support | optimizer / text | target-verified proposals |
| [Fast-dLLM](catalog.md#fast-dllm) · support | research-prototype / text, multimodal | configuration-dependent, model / router training, earlier-state reuse |
| [Inferix](catalog.md#inferix) · system | runtime / video | layout / scheduling |
| [Lookahead Decoding](catalog.md#lookahead) · support | optimizer / text | target-verified proposals |
| [Medusa](catalog.md#medusa) · support | research-prototype / text | configuration-dependent, model / router training |

## Parallelism & scheduling

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [AsyncDiff](catalog.md#asyncdiff) · system | research-prototype / image, video | earlier-state reuse |
| [DistriFusion](catalog.md#distrifusion) · system | research-prototype / image | earlier-state reuse |
| [DistServe](catalog.md#distserve) · system | research-prototype / text | layout / scheduling |
| [OpenVINO GenAI](catalog.md#openvino-genai) · support | runtime / text, image, video, audio, multimodal | configuration-dependent |
| [ParaAttention](catalog.md#para-attention) · support | optimizer / image, video | configuration-dependent, earlier-state reuse |
| [Petals](catalog.md#petals) · system | runtime / text | layout / scheduling |
| [Punica](catalog.md#punica) · system | backend / text | layout / scheduling |
| [S-LoRA](catalog.md#s-lora) · system | research-prototype / text | layout / scheduling |
| [Sarathi-Serve](catalog.md#sarathi-serve) · system | research-prototype / text | layout / scheduling |
| [TensorRT-LLM](catalog.md#tensorrt-llm) · support | runtime / text, multimodal | layout / scheduling |
| [VideoSys](catalog.md#videosys) · system | runtime / video | configuration-dependent, earlier-state reuse |
| [xDiT](catalog.md#xdit) · system | runtime / image, video | configuration-dependent, earlier-state reuse |

## Compiled & native execution

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [AITemplate](catalog.md#aitemplate) · support | compiler / text, image, general | layout / scheduling |
| [Apache TVM](catalog.md#tvm) · support | compiler / text, general | layout / scheduling |
| [BladeDISC](catalog.md#bladedisc) · support | compiler / text, image, general | layout / scheduling |
| [DeepGEMM](catalog.md#deepgemm) · support | kernel-library / text | layout / scheduling |
| [Draw Things Community](catalog.md#draw-things) · system | runtime / image, video | configuration-dependent |
| [DwarfStar](catalog.md#dwarfstar) · system | runtime / text | configuration-dependent |
| [edge-dit.cpp](catalog.md#edge-dit) · system | runtime / image, video | configuration-dependent |
| [ExecuTorch](catalog.md#executorch) · support | runtime / text, general | layout / scheduling |
| [Flash Linear Attention](catalog.md#flash-linear-attention) · support | kernel-library / text | layout / scheduling |
| [FlashAttention](catalog.md#flash-attention) · support | kernel-library / text | layout / scheduling |
| [FlashInfer](catalog.md#flashinfer) · support | kernel-library / text | layout / scheduling |
| [FlashMLA](catalog.md#flashmla) · support | kernel-library / text | layout / scheduling, reduced precision |
| [Halogen Flash](catalog.md#halogen-flash) · system · **closed core** | runtime / text | reduced precision |
| [Hidet](catalog.md#hidet) · support | compiler / text, image, general | layout / scheduling |
| [IREE](catalog.md#iree) · support | compiler / text, image, general | layout / scheduling |
| [IREE Turbine](catalog.md#iree-turbine) · support | compiler / text, general | layout / scheduling |
| [Iris](catalog.md#iris) · system | runtime / image | layout / scheduling |
| [LightX2V](catalog.md#lightx2v) · system | runtime / image, video, audio | configuration-dependent |
| [llama.cpp](catalog.md#llama-cpp) · support | runtime / text | configuration-dependent |
| [Magnitude](catalog.md#magnitude) · system | runtime / text | layout / scheduling |
| [MFLUX](catalog.md#mflux) · system | runtime / image | configuration-dependent, reduced precision |
| [Mirage Persistent Kernel](catalog.md#mirage) · construction | compiler / text | layout / scheduling |
| [MLC LLM](catalog.md#mlc-llm) · construction | runtime / text | layout / scheduling |
| [NVIDIA TensorRT](catalog.md#tensorrt) · support · **closed core** | compiler / text, image, general | layout / scheduling |
| [OneDiff](catalog.md#onediff) · construction | compiler / image, video | layout / scheduling |
| [ONNX Runtime GenAI](catalog.md#onnxruntime-genai) · support | runtime / text, audio, multimodal | layout / scheduling |
| [Stable Fast](catalog.md#stable-fast) · construction | compiler / image, video | layout / scheduling |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) · system | runtime / image, video | configuration-dependent |
| [SwiftTransformer](catalog.md#swifttransformer) · support | backend / text | layout / scheduling |
| [TensorFold](catalog.md#tensorfold) · system | runtime / text | configuration-dependent |
| [tinygrad](catalog.md#tinygrad) · support | compiler / text, image, general | layout / scheduling |
| [Torch-TensorRT](catalog.md#torch-tensorrt) · support | backend / text, image, general | layout / scheduling |

## Construction & validation tools

| Project / reading role | Artifact / modality | Semantic considerations |
| --- | --- | --- |
| [AgentCompile](catalog.md#agentcompile) · construction · **review-use restriction** | research-prototype / text, image | generated-artifact dependent |
| [AKG Agents](catalog.md#akg-agents) · construction | generator / general | generated-artifact dependent |
| [FastKernels](catalog.md#fastkernels) · support | verification / text, image, video, audio, multimodal, general | generated-artifact dependent |
| [Helion](catalog.md#helion) · support | compiler / text, general | generated-artifact dependent |
| [KernelAgent](catalog.md#kernelagent) · construction | generator / general | generated-artifact dependent |
| [KernelBench](catalog.md#kernelbench) · support | verification / general | generated-artifact dependent |
| [MetaInfer](catalog.md#metainfer) · construction | generator / text | generated-artifact dependent |
| [Sol-Engine](catalog.md#sol-engine) · construction | optimizer / image, video | generated-artifact dependent, configuration-dependent |
| [Spec-Bench](catalog.md#spec-bench) · support | verification / text | generated-artifact dependent |
| [TileLang](catalog.md#tilelang) · support | compiler / text, image, video, general | generated-artifact dependent |
| [Triton](catalog.md#triton) · support | compiler / text, image, video, general | generated-artifact dependent |

