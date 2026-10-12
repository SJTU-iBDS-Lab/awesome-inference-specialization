# Systems, construction and supporting infrastructure

> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).

[Home](../README.md) · [中文首页](../README_CN.md) · [Mechanism index](catalog.md) · [Classification](taxonomy.md) · [Research agenda](research-agenda.md)

Read **constraints → execution decisions → artifacts → validation → maintenance**. The roles below explain why an entry is here; they do not rank quality, maturity or importance. Each project has one editorial reading role and retains independent mechanism and artifact labels.

按专用系统、构建流程和支撑基础设施浏览；点击项目进入机制说明、适用边界与直接证据。角色用于组织阅读，不能据此认定系统更快或更成熟。

[Specialized inference systems](#system) · [Ways to construct specialized systems](#construction) · [Supporting infrastructure and references](#support)

<a id="system"></a>

## Specialized inference systems / 专用推理系统 (34)

Integrated runtimes and substantial execution backends organized around concrete model, device or workload constraints.

围绕具体模型、设备或负载约束组织执行的运行时和专用后端。

| Project and evidence | Inspected scope | Artifact |
| --- | --- | --- |
| [AsyncDiff](catalog.md#asyncdiff) | Requires multiple GPUs and temporal hidden-state redundancy, with component count, warmup and stride controlling parallel behavior. | research-prototype |
| [bitnet.cpp](catalog.md#bitnet-cpp) | BitNet-compatible 1.58-bit model layouts and supported ARM/x86 or GPU paths enable specialized arithmetic instead of generic dense matrix multiplication. | runtime |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) | Models exceeding GPU memory and throughput-oriented workloads that tolerate large batches or sequences motivate layerwise offload and transfer/computation overlap. | backend |
| [DistriFusion](catalog.md#distrifusion) | Targets high-resolution diffusion on multiple GPUs with temporal activation redundancy and sufficient work to hide communication. | research-prototype |
| [DistServe](catalog.md#distserve) | Latency-constrained online LLM serving on multiple GPUs | research-prototype |
| [Draw Things Community](catalog.md#draw-things) | Serves local image and video generation across supported macOS and CUDA server deployments. | runtime |
| [DwarfStar](catalog.md#dwarfstar) | Supported model-specific GGUF layouts, backend capabilities and the memory remaining after non-routed weights, graph buffers and KV state determine which experts stay resident. | runtime |
| [edge-dit.cpp](catalog.md#edge-dit) | Prioritizes constrained GPU memory and explicit component placement, with CUDA as the primary optimized backend. | runtime |
| [ExLlamaV3](catalog.md#exllamav3) | EXL3/codebook formats, supported model architectures, CUDA GPU capabilities and small decode shapes determine the available optimized path. | runtime |
| [FastVideo](catalog.md#fastvideo) | Targets supported video architectures with long spatiotemporal sequences; sparse checkpoints and kernels have backend-specific requirements. | runtime |
| [Fiddler](catalog.md#fiddler) | Small-batch local Mixtral-8x7B inference and GPU memory smaller than the unquantized model make activation transfer cheaper than expert-weight transfer. | research-prototype |
| [Flash-MoE](catalog.md#flash-moe) | The implementation targets Qwen3.5-397B-A17B on Apple unified-memory hardware with SSD capacity far exceeding RAM and fixed model geometry. | research-prototype |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) | Throughput-oriented workloads with large effective batches, limited GPU memory and available host/SSD capacity expose the latency–throughput trade-off. | runtime |
| [Halogen Flash](catalog.md#halogen-flash) | One model family and AMD gfx1151 unified-memory machines motivate tensor-specific precision choices and separate budgets for resident weights, KV state and the paged lookup table. | runtime |
| [ik_llama.cpp](catalog.md#ik-llama) | Quantized tensor type, row layout and CPU SIMD or CUDA support determine dispatch, repacking legality and usable offload combinations. | runtime |
| [Inferix](catalog.md#inferix) | Requires block-diffusion or semi-autoregressive world-model execution and must manage long-lived generation state under memory limits. | runtime |
| [Iris](catalog.md#iris) | Targets selected image-model architectures and local machines, with an optimized Apple Silicon path and CPU fallbacks. | runtime |
| [KTransformers / kt-kernel](catalog.md#ktransformers) | CPU AMX/AVX capabilities, NUMA topology, GPU memory and expert precision constrain the heterogeneous placement and execution backend. | backend |
| [LightX2V](catalog.md#lightx2v) | Targets large supported image and video models on memory-constrained accelerators and multi-device systems. | runtime |
| [Magnitude](catalog.md#magnitude) | Encoding, dtype, tensor geometry, layout, numerical contracts and target capabilities constrain kernel composition, while dynamic positions remain operands. | runtime |
| [MFLUX](catalog.md#mflux) | Primarily targets local Apple Silicon execution and explicitly supported MLX model implementations, with documented newer NVIDIA support. | runtime |
| [MoE-Infinity](catalog.md#moe-infinity) | Sparse expert activation, per-model offload stores, GPU-memory budgets and model-specific resident tensors constrain caching and transfer decisions. | runtime |
| [Nunchaku](catalog.md#nunchaku) | Targets supported low-bit diffusion checkpoints and compatible NVIDIA GPU kernels, reducing model memory and repeated activation traffic. | runtime |
| [Petals](catalog.md#petals) | Models distributed across networked user-contributed devices | runtime |
| [PowerInfer](catalog.md#powerinfer) | ReLU-sparse model families, learned predictor weights, activation profiles and a user GPU-memory budget enable neuron-level CPU/GPU partitioning. | runtime |
| [Punica](catalog.md#punica) | Concurrent LoRA requests with shared base weights | backend |
| [S-LoRA](catalog.md#s-lora) | Many LoRA adapters sharing one base model | research-prototype |
| [Sarathi-Serve](catalog.md#sarathi-serve) | Mixed prefill/decode traffic with token-latency targets | research-prototype |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | Targets multiple local CPU and GPU backends and models that fit supported GGUF and execution paths. | runtime |
| [Strata](catalog.md#strata) | The Qwen3.8-Flash-Next model family, supported quantized layouts, consumer GPU VRAM and CPU memory/bandwidth define expert residency and transfer-versus-compute choices. | runtime |
| [TensorFold](catalog.md#tensorfold) | Explicit model–checkpoint-format–platform qualification, quantization group/bit metadata and memory admission restrict which execution paths are accepted. | runtime |
| [TurboDiffusion](catalog.md#turbodiffusion) | Requires supported Wan-family or other integrated model paths and the correct quantized or unquantized checkpoint for the target GPU. | runtime |
| [VideoSys](catalog.md#videosys) | Targets supported video transformers with separable spatial, temporal and cross-modal attention and multi-GPU execution. | runtime |
| [xDiT](catalog.md#xdit) | Targets distributed DiT inference where sequence length, attention-head count and device interconnect determine useful parallel degrees. | runtime |

<a id="construction"></a>

## Ways to construct specialized systems / 专用系统的构建流程 (9)

Concrete model- or deployment-oriented workflows that generate, compile or adapt executable programs.

面向具体模型或部署，生成、编译或改造可执行程序的构建流程。

| Project and evidence | Inspected scope | Artifact |
| --- | --- | --- |
| [AgentCompile](catalog.md#agentcompile) | The documented artifact targets selected models and an A800/SM80-oriented CUDA environment with model-specific fusion contracts. | research-prototype |
| [AKG Agents](catalog.md#akg-agents) | Target backend/DSL, device architecture, reference framework, precision tolerance and concurrent-search budget constrain generated operators. | generator |
| [KernelAgent](catalog.md#kernelagent) | Traceable workload structure, target GPU, shape signatures, reference tensors and search/refinement budgets constrain synthesized code. | generator |
| [MetaInfer](catalog.md#metainfer) | Requested model, hardware, parallelism, precision, API contract and iteration budget define the generated artifact. | generator |
| [Mirage Persistent Kernel](catalog.md#mirage) | NVIDIA GPU architecture, SM worker/scheduler allocation, model graph, batch shape and multi-GPU topology constrain the compiled execution. | compiler |
| [MLC LLM](catalog.md#mlc-llm) | Target device, model architecture, quantization, sequence bounds, tensor parallelism and low-batch workload determine compilation and runtime choices. | runtime |
| [OneDiff](catalog.md#onediff) | Requires a compatible compiler backend, PyTorch/CUDA versions and shape policy, with dynamic shapes trading specialization against recompilation. | compiler |
| [Sol-Engine](catalog.md#sol-engine) | Model pipeline, GPU architecture, tensor shapes, denoising schedule, precision and perceptual-quality thresholds constrain accepted configurations. | optimizer |
| [Stable Fast](catalog.md#stable-fast) | Targets NVIDIA GPU Diffusers pipelines whose repeated execution amortizes tracing and graph-capture costs. | compiler |

<a id="support"></a>

## Supporting infrastructure and references / 支撑基础设施与参照 (55)

General engines, reusable compilers, languages, kernels, mechanism components and evaluation tools.

通用引擎、可复用编译器与语言、内核、机制组件和评测工具。

| Project and evidence | Inspected scope | Artifact |
| --- | --- | --- |
| [AITemplate](catalog.md#aitemplate) | GPU architecture, supported operator templates, FP16-oriented execution and declared shape ranges constrain compilation. | compiler |
| [Apache TVM](catalog.md#tvm) | Compilation targets, tensor shapes, legal operators and schedule rules define the specialization boundary. | compiler |
| [BladeDISC](catalog.md#bladedisc) | Dynamic dimensions, supported fusion patterns, framework integration and CPU/GPU target capabilities constrain generated regions. | compiler |
| [Cache-DiT](catalog.md#cache-dit) | Relies on compatible Diffusers block adapters and user-selected cache thresholds or schedules for repeated denoising. | optimizer |
| [DeepCache](catalog.md#deepcache) | Relies on supported U-Net skip-branch structure and temporal feature redundancy in SD-family pipelines. | optimizer |
| [DeepCompressor](catalog.md#deepcompressor) | Requires calibration data, supported model adapters and a compatible deployment engine such as Nunchaku for actual low-bit acceleration. | optimizer |
| [DeepGEMM](catalog.md#deepgemm) | Supported NVIDIA architectures, precision/scaling formats, alignment and shared expert N/K dimensions determine legal GEMM and grouped-GEMM specializations. | kernel-library |
| [DiTFastAttn](catalog.md#ditfastattn) | Targets supported DiT architectures and calibration settings where spatial, temporal or CFG redundancy is measurable. | research-prototype |
| [EAGLE](catalog.md#eagle) | Autoregressive decoding with compatible EAGLE draft checkpoints | optimizer |
| [ExecuTorch](catalog.md#executorch) | Mobile and embedded device capabilities, delegate operator coverage and bounded memory requirements determine the exported program. | runtime |
| [Fast-dLLM](catalog.md#fast-dllm) | Diffusion language models and supported multimodal derivatives | research-prototype |
| [FastKernels](catalog.md#fastkernels) | Architecture-specific interfaces, captured production shapes, shared weights, task composition and target GPU determine candidate validity. | verification |
| [Flash Linear Attention](catalog.md#flash-linear-attention) | The mixer equations, recurrent-state structure, sequence chunking and backend capabilities define legal execution decompositions. | kernel-library |
| [FlashAttention](catalog.md#flash-attention) | Attention head dimensions, dtype, mask/dropout mode and GPU generation constrain the fused kernel configuration and supported release path. | kernel-library |
| [FlashInfer](catalog.md#flashinfer) | GPU architecture, head dimensions, precision, positional encoding, batch shape and KV layout determine eligible backends and generated kernel modules. | kernel-library |
| [FlashMLA](catalog.md#flashmla) | At the checked HEAD, DeepSeek-V4.1 geometry, NVIDIA SM100/SM103 or Ascend 950, sparse indices and explicit FP8/FP4 KV layouts constrain the available kernels. | kernel-library |
| [Helion](catalog.md#helion) | Input shapes/strides, device backend, traceable operations and autotuning budget constrain each bound kernel. | compiler |
| [Hidet](catalog.md#hidet) | NVIDIA GPU inference, operator coverage, task layouts and tuning-space size constrain the generated execution. | compiler |
| [IREE](catalog.md#iree) | Hardware target, memory lifetime, asynchronous dependencies and the accepted input dialect constrain generated programs. | compiler |
| [IREE Turbine](catalog.md#iree-turbine) | PyTorch exportability, dynamic-shape representation, custom operations and compatible IREE compiler/runtime versions constrain deployment. | compiler |
| [KernelBench](catalog.md#kernelbench) | Specified benchmark tasks, test-input generators, target GPU, numeric tolerances and measured baseline define what a score means. | verification |
| [Learning-to-Cache](catalog.md#learning-to-cache) | Requires architecture- and sampling-schedule-specific router training or released router checkpoints for DiT or U-ViT. | research-prototype |
| [llama.cpp](catalog.md#llama-cpp) | Checkpoint quantization type, tensor layout, matrix geometry, CPU instruction sets and accelerator memory determine eligible kernels and placement. | runtime |
| [LMCache](catalog.md#lmcache) | Repeated or shared LLM context across requests and engines | backend |
| [Lookahead Decoding](catalog.md#lookahead) | Autoregressive decoding with spare parallel compute | optimizer |
| [MagCache](catalog.md#magcache) | Requires a model and denoising-schedule magnitude profile plus threshold and maximum-reuse settings. | optimizer |
| [Marlin](catalog.md#marlin) | Weight-only INT4 formats, compatible group/shape alignment and NVIDIA tensor-core hardware enable its inference-oriented memory/compute pipeline. | kernel-library |
| [Medusa](catalog.md#medusa) | Autoregressive LLMs with trained auxiliary prediction heads | research-prototype |
| [MInference](catalog.md#minference) | Long prompts, per-layer/head sparse-pattern configurations and supported attention layouts make selective attention computation useful. | optimizer |
| [Mooncake](catalog.md#mooncake) | Disaggregated inference and distributed KV storage | backend |
| [NIXL](catalog.md#nixl) | Inference data transfers across heterogeneous memory and storage | backend |
| [NVIDIA TensorRT](catalog.md#tensorrt) | NVIDIA devices, supported operators, precision contracts and min/opt/max input-shape profiles define an engine build. | compiler |
| [ONNX Runtime GenAI](catalog.md#onnxruntime-genai) | ONNX model contracts, execution-provider policy, attention/convolution structure and KV quantization determine the state-management path. | runtime |
| [OpenVINO GenAI](catalog.md#openvino-genai) | OpenVINO-supported CPU/GPU/NPU devices, model export format, cache precision and per-device feature support constrain execution. | runtime |
| [ParaAttention](catalog.md#para-attention) | Requires compatible Diffusers adapters; distributed speed depends on communication, while cache behavior depends on a residual threshold. | optimizer |
| [QTIP](catalog.md#qtip) | Trellis/codebook parameters, tile dimensions and the supported 2/3/4-bit HYB encoding determine which quantized artifact has a fast inference path. | optimizer |
| [SageAttention](catalog.md#sageattention) | Targets supported NVIDIA architectures, layouts and head dimensions, with precision choice constrained by model sensitivity. | kernel-library |
| [SGLang](catalog.md#sglang) | Shared token prefixes within compatible cache namespaces, finite device memory and request arrivals make prefix matching and cache-aware batching effective. | runtime |
| [SnapKV](catalog.md#snapkv) | A bounded KV budget and the assumption that prompt-end attention predicts useful historical positions enable head-specific cache selection. | optimizer |
| [SpargeAttention](catalog.md#spargeattn) | Requires supported head dimensions and block layouts, with top-k or threshold settings controlling sparse work and approximation. | kernel-library |
| [Sparse VideoGen](catalog.md#sparse-videogen) | Requires supported video-model attention adapters and enough sequence length for sparse selection and layout transformations to amortize their overhead. | research-prototype |
| [Spec-Bench](catalog.md#spec-bench) | Comparing speculative decoding under matched devices and workloads | verification |
| [SwiftTransformer](catalog.md#swifttransformer) | C++/CUDA execution substrate used by DistServe and FastServe | backend |
| [T-GATE](catalog.md#t-gate) | Targets text-conditioned diffusion pipelines whose attention contributions vary across denoising phases. | optimizer |
| [T-MAC](catalog.md#t-mac) | Weight bit width, group size, matrix dimensions and CPU vector/lookup capabilities parameterize the generated layout and schedule. | kernel-library |
| [TaylorSeer](catalog.md#taylorseer) | Assumes sufficiently smooth feature evolution across denoising steps and requires a refresh schedule and Taylor order. | research-prototype |
| [TeaCache](catalog.md#teacache) | Benefits from redundancy across denoising iterations and requires model-specific rescaling coefficients and thresholds. | optimizer |
| [TensorRT-LLM](catalog.md#tensorrt-llm) | NVIDIA GPU architecture, model/attention structure, batch-token budgets, KV capacity and precision modes drive execution choices. | runtime |
| [TileLang](catalog.md#tilelang) | Device architecture, tile shapes, tensor-memory features, data precision and supported backend passes constrain generated kernels. | compiler |
| [tinygrad](catalog.md#tinygrad) | Tensor metadata, chosen device backend and available schedule actions determine the captured and optimized execution. | compiler |
| [ToMe for Stable Diffusion](catalog.md#tomesd) | Targets supported Stable Diffusion transformer blocks, with merge ratio and spatial partition parameters controlling saved work. | optimizer |
| [Torch-TensorRT](catalog.md#torch-tensorrt) | NVIDIA target hardware, TensorRT converter coverage, shape profiles and partition size constrain the delegated graph. | backend |
| [Triton](catalog.md#triton) | Target architecture, pointer/value signatures, compile-time constants, warp/stage counts and autotuning keys determine kernel variants. | compiler |
| [vAttention](catalog.md#vattention) | Growing KV state with contiguous virtual address requirements | backend |
| [vLLM](catalog.md#vllm) | Variable request lengths, overlapping prompts, finite KV capacity and layer-specific attention/state layouts determine block ownership and admission. | runtime |

