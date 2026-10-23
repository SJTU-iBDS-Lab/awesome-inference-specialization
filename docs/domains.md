# Browse by model domain / 按模型领域查找

> Generated from [projects.csv](../catalog/projects.csv). Domain labels overlap; counts below must not be summed as unique projects.

[Home](../README.md) · [中文首页](../README_CN.md) · [Core cases](cases.md) · [Survey roles](systems.md) · [Execution mechanisms](catalog.md)

Use these facets to find relevant workloads, then inspect what the system actually rebuilds. Image/video processing includes generation, restoration and perception; the row describes which task is implemented. A multimodal label does not mean every input/output combination is supported.

模态标签可重叠，数量不能相加。图像和视频包含生成、修复与感知，具体能力以条目为准；多模态标签不表示支持所有输入输出组合。先列核心与相邻系统，再折叠共享基础。

[Multimodal understanding & interaction](domains.md#multimodal) · [Image generation & processing](domains.md#image) · [Video generation & processing](domains.md#video) · [Speech & audio](domains.md#audio) · [Language models](domains.md#text) · [Cross-domain infrastructure](domains.md#general)

<a id="multimodal"></a>

## Multimodal understanding & interaction / 多模态理解与交互

27 core/adjacent entries; 2 shared foundations. Counts reflect reviewed scope, not identical capability or maturity.

| Project | Survey role | Inspected execution scope |
| --- | --- | --- |
| [Cactus](catalog.md#cactus) | core | Mobile and wearable deployments; model bundles tested on selected Liquid, Gemma, Qwen and speech families. |
| [CIRU runtime](catalog.md#ciru-runtime) | core | Qwen3.8 Flash model artifacts, paged embeddings and Strix Halo unified memory require coordinated quantization, sparse attention and speculative-state paths. |
| [Colibri](catalog.md#colibri) | core | Models much larger than RAM, with architecture-specific C engines and optional device-specific backends. |
| [FastFlowLM](catalog.md#fastflowlm) | core | AMD XDNA2 client NPUs, including supported Ryzen AI platforms; selected language, vision and audio models. |
| [FreeVideo](catalog.md#freevideo) | core | VDN-H3 eight-step MiniMax H3 video generation on qualified consumer NVIDIA GPUs; Apple-Silicon support is a separately qualified preview. |
| [Gufo](catalog.md#gufo) | core | Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit. |
| [Gufo RDMA](catalog.md#gufo-rdma) | core | Two Strix Halo machines can jointly host higher-precision Qwen Flash-Next weights, but request state, tensors and speculative execution must remain synchronized across hosts. |
| [hipEngine](catalog.md#hipengine) | core | RDNA3 gfx1100 and Strix Halo gfx1151 need native model kernels, recurrent-state handling and request scheduling qualified for their memory and execution geometry. |
| [imp](catalog.md#imp) | core | A single RTX 5090-class sm_120a target and local agent workloads motivate native FP4 arithmetic, memory planning and low-overhead concurrent serving. |
| [Infernix](catalog.md#infernix) | core | Qwen Flash-Next experts and n-gram embeddings exceed a single RTX 5090’s memory, while local agent sessions demand prefix reuse and bounded concurrency. |
| [memra](catalog.md#memra) | core | Per-card Blackwell execution, limited device memory and low-concurrency or large-model workloads motivate native model programs and explicit state placement. |
| [NInfer](catalog.md#ninfer) | core | Selected Qwen Dense/MoE checkpoints on Linux and one RTX 5090 (sm_120a), with one resident model and one to eight startup-fixed execution lanes. |
| [NInfer-3090](catalog.md#ninfer-3090) | core | Qwen dense/MoE serving on a 24 GB RTX 3090 requires SM86-compatible kernels and a smaller memory budget than upstream consumer Blackwell. |
| [Splash](catalog.md#splash) | core | Selected Qwen3.8-27B and Qwen3.6-35B-A3B checkpoints, plus compatible Ternary Bonsai 2, on Apple M3 or newer and macOS 26.4+; text and vision. |
| [strix-llama.cpp](catalog.md#strix-llama-cpp) | core | Strix Halo gfx1151 shares limited bandwidth between CPU and GPU and exhibits device/driver-specific Vulkan and HIP behavior. |
| [SwiftLM](catalog.md#swiftlm) | core | Oversized MoE checkpoints on Apple Silicon with explicit SSD streaming alongside selected speculative and memory controls. |
| [TeleFuser](catalog.md#telefuser) | core | Streaming generative/world-model workloads with per-session state, bounded queues and GPU resource groups. |
| [TUFF](catalog.md#tuff) | core | Selected MoE families on Apple Silicon Macs with limited unified memory and SSD capacity. |
| [TurboFieldfare](catalog.md#turbo-fieldfare) | core | Gemma 4 26B-A4B on memory-constrained Apple Silicon, with separate optional vision support. |
| [VibeServe / VibeSys](catalog.md#vibesys) | core | The VibeServe initiative studies target-specific language serving, streaming ASR, constrained output, multimodal workloads and Apple Silicon. The current VibeSys repository also serves non-inference domains, which are outside this record. |
| [vla.simd](catalog.md#vla-simd) | core | Selected vision-language-action policies on x86 AVX2 and ARM NEON/Apple CPU paths. |
| [vLLM Radiance](catalog.md#vllm-radiance) | core | Dual Radeon AI PRO R9700 gfx1201 serving exposes missing efficient RDNA4 attention, recurrent, low-bit and collective paths in a general framework. |
| [zLLM](catalog.md#zllm) | core | Selected model/backend pairs across Metal, CUDA, ROCm and CPU; experimental Snapdragon HTP paths. |
| [BaseRT](catalog.md#basert) | adjacent | Selected Apple Silicon and NVIDIA GB10 deployments with an engine-specific .base format and device-specific quantization profiles. |
| [BRaiN](catalog.md#brain) | adjacent | Multiple native model ports across CPU and GPU/WebGPU; support is architecture- and action-specific. |
| [Hilum LLM Engine](catalog.md#hilum-engine) | adjacent | Android Adreno/Vulkan and Apple Metal mobile deployments with GGUF models. |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) | adjacent | Supported Jetson, DRIVE and other qualified NVIDIA platforms; model and precision support follow the release matrix. |

<details>
<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>

[FastKernels](catalog.md#fastkernels) · [TensorRT-LLM](catalog.md#tensorrt-llm)

</details>

<a id="image"></a>

## Image generation & processing / 图像生成与处理

26 core/adjacent entries; 6 shared foundations. Counts reflect reviewed scope, not identical capability or maturity.

| Project | Survey role | Inspected execution scope |
| --- | --- | --- |
| [brodiffusion](catalog.md#brodiffusion) | core | Selected diffusion image families on CPU and brotensor CUDA/Metal/Vulkan paths. |
| [Cactus](catalog.md#cactus) | core | Mobile and wearable deployments; model bundles tested on selected Liquid, Gemma, Qwen and speech families. |
| [Colibri](catalog.md#colibri) | core | Models much larger than RAM, with architecture-specific C engines and optional device-specific backends. |
| [edge-dit.cpp](catalog.md#edge-dit) | core | Prioritizes constrained GPU memory and explicit component placement, with CUDA as the primary optimized backend. |
| [FastFlowLM](catalog.md#fastflowlm) | core | AMD XDNA2 client NPUs, including supported Ryzen AI platforms; selected language, vision and audio models. |
| [Gufo](catalog.md#gufo) | core | Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit. |
| [Hearth](catalog.md#hearth) | core | SD1.5/SDXL on GPUs reachable through CubeCL/wgpu Vulkan execution. |
| [Iris](catalog.md#iris) | core | Targets selected image-model architectures and local machines, with an optimized Apple Silicon path and CPU fallbacks. |
| [LightX2V](catalog.md#lightx2v) | core | Targets large supported image and video models on memory-constrained accelerators and multi-device systems. |
| [Nunchaku](catalog.md#nunchaku) | core | Targets supported low-bit diffusion checkpoints and compatible NVIDIA GPU kernels, reducing model memory and repeated activation traffic. |
| [Quartz](catalog.md#saient-quartz) | core | Native Rust local inference with SD1.5/SDXL and an evolving Wan path on CPU/CUDA/Vulkan. |
| [Sol-Engine](catalog.md#sol-engine) | core | Model pipeline, GPU architecture, tensor shapes, denoising schedule, precision and perceptual-quality thresholds constrain accepted configurations. |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | core | Targets multiple local CPU and GPU backends and models that fit supported GGUF and execution paths. |
| [stable-diffusion.rs](catalog.md#stable-diffusion-rs) | core | Selected diffusion models on Apple MLX, with an explicit Rust model/backend boundary. |
| [TeleFuser](catalog.md#telefuser) | core | Streaming generative/world-model workloads with per-session state, bounded queues and GPU resource groups. |
| [zLLM](catalog.md#zllm) | core | Selected model/backend pairs across Metal, CUDA, ROCm and CPU; experimental Snapdragon HTP paths. |
| [AgentCompile](catalog.md#agentcompile) | adjacent | The documented artifact targets selected models and an A800/SM80-oriented CUDA environment with model-specific fusion contracts. |
| [BRaiN](catalog.md#brain) | adjacent | Multiple native model ports across CPU and GPU/WebGPU; support is architecture- and action-specific. |
| [diffusion-rs](catalog.md#diffusion-rs) | adjacent | FLUX image generation through Rust tensor operations and optional component offload. |
| [Draw Things Community](catalog.md#draw-things) | adjacent | Serves local image and video generation across supported macOS and CUDA server deployments. |
| [MFLUX](catalog.md#mflux) | adjacent | Primarily targets local Apple Silicon execution and explicitly supported MLX model implementations, with documented newer NVIDIA support. |
| [OneDiff](catalog.md#onediff) | adjacent | Requires a compatible compiler backend, PyTorch/CUDA versions and shape policy, with dynamic shapes trading specialization against recompilation. |
| [Stable Fast](catalog.md#stable-fast) | adjacent | Targets NVIDIA GPU Diffusers pipelines whose repeated execution amortizes tracing and graph-capture costs. |
| [StreamDiffusion](catalog.md#streamdiffusion) | adjacent | Interactive SD/LCM image streams with overlapping denoising steps. |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) | adjacent | Supported Jetson, DRIVE and other qualified NVIDIA platforms; model and precision support follow the release matrix. |
| [xDiT](catalog.md#xdit) | adjacent | Targets distributed DiT inference where sequence length, attention-head count and device interconnect determine useful parallel degrees. |

<details>
<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>

[DeepCompressor](catalog.md#deepcompressor) · [FastKernels](catalog.md#fastkernels) · [NVIDIA TensorRT](catalog.md#tensorrt) · [SageAttention](catalog.md#sageattention) · [TileLang](catalog.md#tilelang) · [Triton](catalog.md#triton)

</details>

<a id="video"></a>

## Video generation & processing / 视频生成与处理

22 core/adjacent entries; 4 shared foundations. Counts reflect reviewed scope, not identical capability or maturity.

| Project | Survey role | Inspected execution scope |
| --- | --- | --- |
| [edge-dit.cpp](catalog.md#edge-dit) | core | Prioritizes constrained GPU memory and explicit component placement, with CUDA as the primary optimized backend. |
| [FastVideo](catalog.md#fastvideo) | core | Supported video and audio-video architectures on qualified backends; ordinary dense and accelerated model paths have distinct checkpoint and precision requirements. |
| [FreeVideo](catalog.md#freevideo) | core | VDN-H3 eight-step MiniMax H3 video generation on qualified consumer NVIDIA GPUs; Apple-Silicon support is a separately qualified preview. |
| [Gufo](catalog.md#gufo) | core | Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit. |
| [LightX2V](catalog.md#lightx2v) | core | Targets large supported image and video models on memory-constrained accelerators and multi-device systems. |
| [MiniMax-H3 MLX](catalog.md#minimax-h3-mlx) | core | MiniMax-H3 joint video/audio diffusion on Apple Silicon with large unified memory. |
| [Quartz](catalog.md#saient-quartz) | core | Native Rust local inference with SD1.5/SDXL and an evolving Wan path on CPU/CUDA/Vulkan. |
| [Sol-Engine](catalog.md#sol-engine) | core | Model pipeline, GPU architecture, tensor shapes, denoising schedule, precision and perceptual-quality thresholds constrain accepted configurations. |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | core | Targets multiple local CPU and GPU backends and models that fit supported GGUF and execution paths. |
| [StreamDiffusionV2](catalog.md#streamdiffusion-v2) | core | Causal Wan video generation with low-latency streaming and single/multiple GPU execution. |
| [TeleFuser](catalog.md#telefuser) | core | Streaming generative/world-model workloads with per-session state, bounded queues and GPU resource groups. |
| [Vidax](catalog.md#vidax) | core | Selected video-generation models on JAX/Flax TPU meshes. |
| [zLLM](catalog.md#zllm) | core | Selected model/backend pairs across Metal, CUDA, ROCm and CPU; experimental Snapdragon HTP paths. |
| [BRaiN](catalog.md#brain) | adjacent | Multiple native model ports across CPU and GPU/WebGPU; support is architecture- and action-specific. |
| [Draw Things Community](catalog.md#draw-things) | adjacent | Serves local image and video generation across supported macOS and CUDA server deployments. |
| [Inferix](catalog.md#inferix) | adjacent | Requires block-diffusion or semi-autoregressive world-model execution and must manage long-lived generation state under memory limits. |
| [OneDiff](catalog.md#onediff) | adjacent | Requires a compatible compiler backend, PyTorch/CUDA versions and shape policy, with dynamic shapes trading specialization against recompilation. |
| [Stable Fast](catalog.md#stable-fast) | adjacent | Targets NVIDIA GPU Diffusers pipelines whose repeated execution amortizes tracing and graph-capture costs. |
| [StreamDiffusion](catalog.md#streamdiffusion) | adjacent | Interactive SD/LCM image streams with overlapping denoising steps. |
| [TurboDiffusion](catalog.md#turbodiffusion) | adjacent | Requires supported Wan-family or other integrated model paths and the correct quantized or unquantized checkpoint for the target GPU. |
| [VideoSys](catalog.md#videosys) | adjacent | Targets supported video transformers with separable spatial, temporal and cross-modal attention and multi-GPU execution. |
| [xDiT](catalog.md#xdit) | adjacent | Targets distributed DiT inference where sequence length, attention-head count and device interconnect determine useful parallel degrees. |

<details>
<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>

[FastKernels](catalog.md#fastkernels) · [SageAttention](catalog.md#sageattention) · [TileLang](catalog.md#tilelang) · [Triton](catalog.md#triton)

</details>

<a id="audio"></a>

## Speech & audio / 语音与音频

23 core/adjacent entries; 1 shared foundations. Counts reflect reviewed scope, not identical capability or maturity.

| Project | Survey role | Inspected execution scope |
| --- | --- | --- |
| [Aria](catalog.md#aria) | core | Stable Audio 3 small/medium local text-to-audio diffusion on CPU and optional CUDA. |
| [Cactus](catalog.md#cactus) | core | Mobile and wearable deployments; model bundles tested on selected Liquid, Gemma, Qwen and speech families. |
| [FastFlowLM](catalog.md#fastflowlm) | core | AMD XDNA2 client NPUs, including supported Ryzen AI platforms; selected language, vision and audio models. |
| [FastVideo](catalog.md#fastvideo) | core | Supported video and audio-video architectures on qualified backends; ordinary dense and accelerated model paths have distinct checkpoint and precision requirements. |
| [Gufo](catalog.md#gufo) | core | Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit. |
| [hipEngine](catalog.md#hipengine) | core | RDNA3 gfx1100 and Strix Halo gfx1151 need native model kernels, recurrent-state handling and request scheduling qualified for their memory and execution geometry. |
| [LightX2V](catalog.md#lightx2v) | core | Targets large supported image and video models on memory-constrained accelerators and multi-device systems. |
| [MiniMax-H3 MLX](catalog.md#minimax-h3-mlx) | core | MiniMax-H3 joint video/audio diffusion on Apple Silicon with large unified memory. |
| [parakeet.cpp (axiom)](catalog.md#parakeet-axiom) | core | Parakeet ASR on CPU and Apple Metal/MPSGraph through the axiom tensor library. |
| [parakeet.cpp (ggml)](catalog.md#parakeet-ggml) | core | NeMo FastConformer CTC/RNNT/TDT families, including cache-aware streaming, on ggml backends. |
| [Qingming Qwen3-TTS](catalog.md#qingming-qwen3-tts) | core | Qwen3-TTS on AMD RX 7900 XTX 24GB and NVIDIA RTX 4090 24GB. |
| [Qwen-ASR (C)](catalog.md#qwen-asr-c) | core | Qwen3-ASR 0.6B/1.7B on local CPU and optional CUDA/ROCm devices. |
| [Qwen3-TTS (C)](catalog.md#qwen3-tts-c) | core | Qwen3-TTS 0.6B/1.7B speech synthesis on CPU and supported CUDA/Metal paths. |
| [Saragossa](catalog.md#saragossa) | core | Single-user local latency on Apple Silicon for selected text and speech architectures with MLX affine integer weights. |
| [TeleFuser](catalog.md#telefuser) | core | Streaming generative/world-model workloads with per-session state, bounded queues and GPU resource groups. |
| [VibeServe / VibeSys](catalog.md#vibesys) | core | The VibeServe initiative studies target-specific language serving, streaming ASR, constrained output, multimodal workloads and Apple Silicon. The current VibeSys repository also serves non-inference domains, which are outside this record. |
| [VoxGen](catalog.md#voxgen) | core | VoxCPM2 speech synthesis with Vulkan, including a tuned AMD RDNA3 profile. |
| [zLLM](catalog.md#zllm) | core | Selected model/backend pairs across Metal, CUDA, ROCm and CPU; experimental Snapdragon HTP paths. |
| [BRaiN](catalog.md#brain) | adjacent | Multiple native model ports across CPU and GPU/WebGPU; support is architecture- and action-specific. |
| [Cactus Needle](catalog.md#needle) | adjacent | Small automation models across desktop, mobile, embedded and browser targets; current source generation is Needle 3. |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) | adjacent | Supported Jetson, DRIVE and other qualified NVIDIA platforms; model and precision support follow the release matrix. |
| [whisper.cpp](catalog.md#whisper-cpp) | adjacent | Whisper ASR on local CPU and diverse accelerator backends. |
| [WhisperKit](catalog.md#whisperkit) | adjacent | Apple Silicon speech recognition through compiled Core ML model components. |

<details>
<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>

[FastKernels](catalog.md#fastkernels)

</details>

<a id="text"></a>

## Language models / 语言模型

71 core/adjacent entries; 17 shared foundations. Counts reflect reviewed scope, not identical capability or maturity.

| Project | Survey role | Inspected execution scope |
| --- | --- | --- |
| [ane.cpp](catalog.md#ane-cpp) | core | Dense Qwen3/Qwen3.5 text inference through private ANE APIs, with M3 Max-specific empirical constraints. |
| [ANEMLL Flash llama.cpp](catalog.md#anemll-flash-llama) | core | Selected GGUF MoE architectures on Apple Silicon with sidecar expert storage and bounded slot-bank memory. |
| [AutoMegaKernel](catalog.md#automegakernel) | core | Supported HuggingFace Llama-family graphs on CUDA, principally batch-one decode. Paper speed sweeps at position zero use synthetic weights at real model shapes; real-checkpoint quality tests have a separate scope. |
| [Cactus](catalog.md#cactus) | core | Mobile and wearable deployments; model bundles tested on selected Liquid, Gemma, Qwen and speech families. |
| [CIRU runtime](catalog.md#ciru-runtime) | core | Qwen3.8 Flash model artifacts, paged embeddings and Strix Halo unified memory require coordinated quantization, sparse attention and speculative-state paths. |
| [Cloudflare Infire](catalog.md#infire) | core | Cloudflare distributed inference nodes with constrained host CPU, startup and isolation requirements. The initial Hopper-focused report and later large-model/multi-GPU update describe different deployment stages. |
| [Colibri](catalog.md#colibri) | core | Models much larger than RAM, with architecture-specific C engines and optional device-specific backends. |
| [dInfer](catalog.md#dinfer) | core | LLaDA 8B, LLaDA-MoE 7B and LLaDA2 mini/flash families on qualified NVIDIA multi-GPU paths. |
| [DwarfStar](catalog.md#dwarfstar) | core | Supported model-specific GGUF layouts, backend capabilities and the memory remaining after non-routed weights, graph buffers and KV state determine which experts stay resident. |
| [ExLlamaV3](catalog.md#exllamav3) | core | EXL3/codebook formats, supported model architectures, CUDA GPU capabilities and small decode shapes determine the available optimized path. |
| [FastFlowLM](catalog.md#fastflowlm) | core | AMD XDNA2 client NPUs, including supported Ryzen AI platforms; selected language, vision and audio models. |
| [Flash-MoE](catalog.md#flash-moe) | core | The implementation targets Qwen3.5-397B-A17B on Apple unified-memory hardware with SSD capacity far exceeding RAM and fixed model geometry. |
| [Gufo](catalog.md#gufo) | core | Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit. |
| [Gufo RDMA](catalog.md#gufo-rdma) | core | Two Strix Halo machines can jointly host higher-precision Qwen Flash-Next weights, but request state, tensors and speculative execution must remain synchronized across hosts. |
| [Halogen Flash](catalog.md#halogen-flash) | core | One model family and AMD gfx1151 unified-memory machines motivate tensor-specific precision choices and separate budgets for resident weights, KV state and the paged lookup table. |
| [hipEngine](catalog.md#hipengine) | core | RDNA3 gfx1100 and Strix Halo gfx1151 need native model kernels, recurrent-state handling and request scheduling qualified for their memory and execution geometry. |
| [Ignis](catalog.md#ignis) | core | Single SM120a Blackwell GPU (RTX 5090 / RTX PRO 6000), selected Qwen3.8-27B NVFP4 and Flash-Next MoE text paths; image/vision features are advertised but not audited here. |
| [imp](catalog.md#imp) | core | A single RTX 5090-class sm_120a target and local agent workloads motivate native FP4 arithmetic, memory planning and low-overhead concurrent serving. |
| [Infernix](catalog.md#infernix) | core | Qwen Flash-Next experts and n-gram embeddings exceed a single RTX 5090’s memory, while local agent sessions demand prefix reuse and bounded concurrency. |
| [Kipp](catalog.md#kipp) | core | A pinned Qwen3 checkpoint registry and small native runtime motivate explicit model contracts and hardware-checked CPU/Metal/CUDA paths. |
| [Kog Inference Engine (KIE)](catalog.md#kie) | core | The reviewed low-latency preview uses an FP16 approximately 2B Laneformer model, batch one and eight AMD MI300X GPUs; the companion announcement also reports an eight-H200 configuration. |
| [KTransformers / kt-kernel](catalog.md#ktransformers) | core | CPU AMX/AVX capabilities, NUMA topology, GPU memory and expert precision constrain the heterogeneous placement and execution backend. |
| [Lily](catalog.md#lily) | core | One exact Qwen3.6-35B-A3B MLX-affine Q4 checkpoint, group size 64, on Apple GPU family 10+ and macOS 26+. |
| [Lithos Metal](catalog.md#lithos-metal) | core | Registered Apple chip backends and selected Qwen target/draft checkpoints, with explicit recipe, format and context constraints. |
| [llamAmpere](catalog.md#llamampere) | core | Qwen3.8-27B with an MTP head, primarily single-stream inference on Ampere RTX 3090/3090 Ti, where verification width and long-context state compete for compute and VRAM. |
| [Llaminar](catalog.md#llaminar) | core | A selected mixture of x86 CPUs, SM86 NVIDIA GPUs and gfx906 AMD GPUs requires explicit placement and communication across vendor-specific execution stacks. |
| [Mach X](catalog.md#machx) | core | Intel Arc, built/tuned on Arc Pro B70; inspected Qwen 27B and 35B-A3B text decode paths. Other advertised architectures and video are outside this focused review. |
| [Magnitude](catalog.md#magnitude) | core | Encoding, dtype, tensor geometry, layout, numerical contracts and target capabilities constrain kernel composition, while dynamic positions remain operands. |
| [memra](catalog.md#memra) | core | Per-card Blackwell execution, limited device memory and low-concurrency or large-model workloads motivate native model programs and explicit state placement. |
| [MetaInfer](catalog.md#metainfer) | core | Requested model, hardware, parallelism, precision, API contract and iteration budget define the generated artifact. |
| [Mirage Persistent Kernel](catalog.md#mirage) | core | NVIDIA GPU architecture, SM worker/scheduler allocation, model graph, batch shape and multi-GPU topology constrain the compiled execution. |
| [NInfer](catalog.md#ninfer) | core | Selected Qwen Dense/MoE checkpoints on Linux and one RTX 5090 (sm_120a), with one resident model and one to eight startup-fixed execution lanes. |
| [NInfer-3090](catalog.md#ninfer-3090) | core | Qwen dense/MoE serving on a 24 GB RTX 3090 requires SM86-compatible kernels and a smaller memory budget than upstream consumer Blackwell. |
| [peregrine](catalog.md#peregrine) | core | GLM-5.2 744B-style int4 MoE streaming on Linux with NVMe, CPU and optional NVIDIA CUDA expert execution. |
| [Quartz](catalog.md#saient-quartz) | core | Native Rust local inference with SD1.5/SDXL and an evolving Wan path on CPU/CUDA/Vulkan. |
| [Saragossa](catalog.md#saragossa) | core | Single-user local latency on Apple Silicon for selected text and speech architectures with MLX affine integer weights. |
| [SEIS: Self-Evolving Inference Systems](catalog.md#seis) | core | The paper centers on Qwen3-0.6B on one H100 with single-request greedy decoding, with supplementary Llama-3.2-1B experiments. The linked public ten-trial example uses RTX PRO 6000 Blackwell and is a separate configuration. |
| [Splash](catalog.md#splash) | core | Selected Qwen3.8-27B and Qwen3.6-35B-A3B checkpoints, plus compatible Ternary Bonsai 2, on Apple M3 or newer and macOS 26.4+; text and vision. |
| [Strata](catalog.md#strata) | core | The Qwen3.8-Flash-Next model family, supported quantized layouts, consumer GPU VRAM and CPU memory/bandwidth define expert residency and transfer-versus-compute choices. |
| [strix-llama.cpp](catalog.md#strix-llama-cpp) | core | Strix Halo gfx1151 shares limited bandwidth between CPU and GPU and exhibits device/driver-specific Vulkan and HIP behavior. |
| [Swiftlet](catalog.md#swiftlet) | core | Selected Qwen hybrid MoE architectures on macOS/iOS, using qpack containers and bounded resident memory. |
| [SwiftLM](catalog.md#swiftlm) | core | Oversized MoE checkpoints on Apple Silicon with explicit SSD streaming alongside selected speculative and memory controls. |
| [TensorFold](catalog.md#tensorfold) | core | Explicit model–checkpoint-format–platform qualification, quantization group/bit metadata and memory admission restrict which execution paths are accepted. |
| [TUFF](catalog.md#tuff) | core | Selected MoE families on Apple Silicon Macs with limited unified memory and SSD capacity. |
| [TurboFieldfare](catalog.md#turbo-fieldfare) | core | Gemma 4 26B-A4B on memory-constrained Apple Silicon, with separate optional vision support. |
| [VibeServe / VibeSys](catalog.md#vibesys) | core | The VibeServe initiative studies target-specific language serving, streaming ASR, constrained output, multimodal workloads and Apple Silicon. The current VibeSys repository also serves non-inference domains, which are outside this record. |
| [vLLM Radiance](catalog.md#vllm-radiance) | core | Dual Radeon AI PRO R9700 gfx1201 serving exposes missing efficient RDNA4 attention, recurrent, low-bit and collective paths in a general framework. |
| [VTE](catalog.md#vte) | core | Consumer RDNA3 GPUs, especially RX 7600 with 8 GB VRAM and Windows driver constraints, motivate direct control of memory and dispatch. |
| [ZINC](catalog.md#zinc) | core | Local consumer GPUs motivate explicit memory ownership and native per-backend execution for a selected GGUF model catalog. |
| [zLLM](catalog.md#zllm) | core | Selected model/backend pairs across Metal, CUDA, ROCm and CPU; experimental Snapdragon HTP paths. |
| [AgentCompile](catalog.md#agentcompile) | adjacent | The documented artifact targets selected models and an A800/SM80-oriented CUDA environment with model-specific fusion contracts. |
| [ANE-LM](catalog.md#ane-lm) | adjacent | Dense Qwen3 and Qwen3.5 text execution using private Apple Neural Engine APIs. |
| [ANEMLL](catalog.md#anemll) | adjacent | Selected LLM architectures converted to CoreML for Apple Neural Engine, with size, shape, context and quantization restrictions. |
| [BaseRT](catalog.md#basert) | adjacent | Selected Apple Silicon and NVIDIA GB10 deployments with an engine-specific .base format and device-specific quantization profiles. |
| [bitnet.cpp](catalog.md#bitnet-cpp) | adjacent | BitNet-compatible 1.58-bit model layouts and supported ARM/x86 or GPU paths enable specialized arithmetic instead of generic dense matrix multiplication. |
| [BRaiN](catalog.md#brain) | adjacent | Multiple native model ports across CPU and GPU/WebGPU; support is architecture- and action-specific. |
| [Cactus Needle](catalog.md#needle) | adjacent | Small automation models across desktop, mobile, embedded and browser targets; current source generation is Needle 3. |
| [CoreML LLM CLI](catalog.md#coreml-llm-cli) | adjacent | CoreML-converted Llama 2 on ANE with fixed chunking and IOSurface-backed buffers. |
| [DeepSpeed ZeRO-Inference](catalog.md#zero-inference) | adjacent | Models exceeding GPU memory and throughput-oriented workloads that tolerate large batches or sequences motivate layerwise offload and transfer/computation overlap. |
| [Fiddler](catalog.md#fiddler) | adjacent | Small-batch local Mixtral-8x7B inference and GPU memory smaller than the unquantized model make activation transfer cheaper than expert-weight transfer. |
| [FlexLLMGen (FlexGen)](catalog.md#flexllmgen) | adjacent | Throughput-oriented workloads with large effective batches, limited GPU memory and available host/SSD capacity expose the latency–throughput trade-off. |
| [Hilum LLM Engine](catalog.md#hilum-engine) | adjacent | Android Adreno/Vulkan and Apple Metal mobile deployments with GGUF models. |
| [HybriMoE](catalog.md#hybrimoe) | adjacent | MoE models exceeding GPU memory incur on-demand expert-loading latency and unbalanced CPU/GPU use. |
| [ik_llama.cpp](catalog.md#ik-llama) | adjacent | Quantized tensor type, row layout and CPU SIMD or CUDA support determine dispatch, repacking legality and usable offload combinations. |
| [MetalChat](catalog.md#metalchat) | adjacent | Selected Llama/Gemma-family models on Apple Silicon through a native C++/Metal library. |
| [MLC LLM](catalog.md#mlc-llm) | adjacent | Target device, model architecture, quantization, sequence bounds, tensor parallelism and low-batch workload determine compilation and runtime choices. |
| [MoE-Infinity](catalog.md#moe-infinity) | adjacent | Sparse expert activation, per-model offload stores, GPU-memory budgets and model-specific resident tensors constrain caching and transfer decisions. |
| [PowerInfer](catalog.md#powerinfer) | adjacent | ReLU-sparse model families, learned predictor weights, activation profiles and a user GPU-memory budget enable neuron-level CPU/GPU partitioning. |
| [ROCmFPX](catalog.md#rocmfpx) | adjacent | AMD RDNA execution motivates compact weight blocks with explicit disk contracts and matching CPU, Vulkan and HIP arithmetic. |
| [TensorRT Edge-LLM](catalog.md#tensorrt-edge-llm) | adjacent | Supported Jetson, DRIVE and other qualified NVIDIA platforms; model and precision support follow the release matrix. |
| [Uzu](catalog.md#uzu) | adjacent | On-device Apple deployment using its supported configurations, converted model format and native Metal backend. |

<details>
<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>

[Apache TVM](catalog.md#tvm) · [Apple Neural Engine Field Guide](catalog.md#ane-field-guide) · [DeepCompressor](catalog.md#deepcompressor) · [FastKernels](catalog.md#fastkernels) · [Flash Linear Attention](catalog.md#flash-linear-attention) · [FlashAttention](catalog.md#flash-attention) · [FlashInfer](catalog.md#flashinfer) · [llama.cpp](catalog.md#llama-cpp) · [Marlin](catalog.md#marlin) · [NVIDIA TensorRT](catalog.md#tensorrt) · [QTIP](catalog.md#qtip) · [SageAttention](catalog.md#sageattention) · [SGLang](catalog.md#sglang) · [TensorRT-LLM](catalog.md#tensorrt-llm) · [TileLang](catalog.md#tilelang) · [Triton](catalog.md#triton) · [vLLM](catalog.md#vllm)

</details>

<a id="general"></a>

## Cross-domain infrastructure / 跨模态基础设施

4 core/adjacent entries; 9 shared foundations. Counts reflect reviewed scope, not identical capability or maturity.

| Project | Survey role | Inspected execution scope |
| --- | --- | --- |
| [AKG Agents](catalog.md#akg-agents) | adjacent | Target backend/DSL, device architecture, reference framework, precision tolerance and concurrent-search budget constrain generated operators. |
| [Atrex Kernel Agent (AKA)](catalog.md#atrex-kernel-agent) | adjacent | Evaluator-owned GPU operator tasks, target DSL/device and fixed optimization budgets constrain candidate search and acceptance. |
| [KernelAgent](catalog.md#kernelagent) | adjacent | Traceable workload structure, target GPU, shape signatures, reference tensors and search/refinement budgets constrain synthesized code. |
| [PMetal](catalog.md#pmetal) | adjacent | Apple Silicon training and inference across MLX, native Metal and ANE-oriented components. |

<details>
<summary>Shared foundations and comparison components / 共享基础与对照组件</summary>

[Apache TVM](catalog.md#tvm) · [Atrex-Bench](catalog.md#atrex-bench) · [FastKernels](catalog.md#fastkernels) · [KernelBench](catalog.md#kernelbench) · [KernelWiki](catalog.md#kernelwiki) · [ncu-report-skill](catalog.md#ncu-report-skill) · [NVIDIA TensorRT](catalog.md#tensorrt) · [TileLang](catalog.md#tilelang) · [Triton](catalog.md#triton)

</details>

