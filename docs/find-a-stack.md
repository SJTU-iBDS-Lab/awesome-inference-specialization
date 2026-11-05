# Find a stack / 按硬件与模型查找

> Generated from [discovery.json](../catalog/discovery.json) and [projects.csv](../catalog/projects.csv).

[Home](../README.md#find-a-stack) · [中文首页](../README_CN.md#find-a-stack) · [Complete catalog / 全目录](catalog.md) · [Mobile execution constraints / 移动端约束](device-execution-matrix.md)

Curated entry points into existing records, not an exhaustive support matrix or a recommendation ranking. A project may appear in multiple routes and is still counted once. Scope is copied verbatim from its reviewed catalog record; follow Details for precision, model changes, source evidence and benchmark limits. No benchmarks were independently reproduced here.

这些入口指向现有记录，不是完整兼容性表或性能推荐。跨组重复引用不增加项目数；具体范围原样取自已核查记录。设备名称不意味着支持该系列所有型号，模型家族也不意味着支持所有检查点。详情保留量化、模型改动、源码与基准限制；本仓库未独立复现性能。

<a id="hardware"></a>

## By hardware / 按硬件

[RTX 5090 / Blackwell](#blackwell) · [DGX Spark](#spark) · [Strix Halo / 395](#strix-halo) · [Apple Silicon](#apple) · [Intel Arc](#intel-arc) · [RTX 3090 / Ampere](#ampere) · [BC-250](#bc250) · [Mobile / NPU / 手机 / NPU](#mobile)

<a id="blackwell"></a>

### RTX 5090 / Blackwell

Consumer/workstation Blackwell paths; memory budgets and supported checkpoints differ. DGX Spark has a separate route below.

桌面／工作站 Blackwell 路径，显存预算与检查点各不相同；DGX Spark 另列。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [NInfer](catalog.md#ninfer) | Selected Qwen Dense/MoE checkpoints on Linux and one RTX 5090 (sm_120a), with one resident model and one to eight startup-fixed execution lanes. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#ninfer) |
| [Ignis](catalog.md#ignis) | Single SM120a Blackwell GPU (RTX 5090 / RTX PRO 6000), selected Qwen3.8-27B NVFP4 and Flash-Next MoE text paths; image/vision features are advertised but not audited here. | `public-code` · 2026-10-23 · [Details / 详情](catalog.md#ignis) |
| [imp](catalog.md#imp) | A single RTX 5090-class sm_120a target and local agent workloads motivate native FP4 arithmetic, memory planning and low-overhead concurrent serving. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#imp) |
| [Basalt](catalog.md#basalt) | Qwen3.8-Flash-Next on Linux/Windows x64 with NVIDIA Blackwell sm_120 and CPU RAM; optional peer GPU tier. Text expert/verify and NVFP4 prefill paths inspected; vision not qualified here. | `public-code` · 2026-11-05 · [Details / 详情](catalog.md#basalt) |

[↑ By hardware / 按硬件](#hardware)

<a id="spark"></a>

### DGX Spark

Separate single-node Qwen dispatch from the reviewed multi-node full-GLM stack. Advertised additional model paths are not automatically qualified.

区分单节点 Qwen 调用链与已查多节点完整 GLM 栈；宣传中的其他模型路径不自动视为已核查。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Spark Engine](catalog.md#spark-engine) | NVIDIA DGX Spark / GB10 sm_121, Linux aarch64. Qwen3.8-Flash-Next text path on one node and N-way RDMA substrate inspected; GLM/DeepSeek multi-node and vision paths are advertised but not fully audited here. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#spark-engine) |
| [gr8](catalog.md#gr8) | Full GLM-5.3 on three to six DGX Spark / GB10 sm_121a nodes with RoCE v2. Review covers the GLM trellis, S2 and KV-store substrate; newer GLM-Flash and DeepSeek paths are not fully qualified here. | `public-code` · 2026-11-05 · [Details / 详情](catalog.md#gr8) |

[↑ By hardware / 按硬件](#hardware)

<a id="strix-halo"></a>

### Strix Halo / 395

gfx1151 unified-memory systems. Matching weight files alone does not match quantization, speculation, caching or sampling behavior; Halogen has a closed core.

gfx1151 统一内存设备。同一权重文件不足以统一量化、投机、缓存与采样行为；Halogen 核心闭源。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Halogen Flash](catalog.md#halogen-flash) | One model family and AMD gfx1151 unified-memory machines motivate tensor-specific precision choices and separate budgets for resident weights, KV state and the paged lookup table. | `closed-core` · 2026-11-03 · [Details / 详情](catalog.md#halogen-flash) |
| [Qwenox](catalog.md#qwenox) | Qwen3.8-Flash-Next on AMD Ryzen AI Max+ 395 / gfx1151 with 128 GB unified memory; Linux and Windows. Text execution reviewed; advertised vision paths not audited. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#qwenox) |
| [Crucible](catalog.md#crucible) | Qwen3.8-Flash-Next EXL3 packs on one Linux AMD Ryzen AI Max+ 395 / gfx1151 with 128 GB unified memory; text execution reviewed. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#crucible) |
| [Strixite](catalog.md#strixite) | Qwen3.8-Flash-Next on one Linux AMD Strix Halo / gfx1151 machine with 128 GB unified memory; text paths inspected, vision not qualified here. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#strixite) |
| [Gufo](catalog.md#gufo) | Selected models on Linux x86-64 AMD Strix Halo (gfx1151), optimized for 128 GiB unified-memory systems; smaller memory configurations are conditional on model fit. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#gufo) |

[↑ By hardware / 按硬件](#hardware)

<a id="apple"></a>

### Apple Silicon

Metal-native execution, SSD expert streaming and ANE compilation are different paths. Chip generations, OS versions and model modifications matter.

Metal 原生执行、SSD 专家流式加载与 ANE 编译是不同路线；须匹配芯片、系统版本与模型改动。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Splash](catalog.md#splash) | Selected Qwen3.8-27B and Qwen3.6-35B-A3B checkpoints, plus compatible Ternary Bonsai 2, on Apple M3 or newer and macOS 26.4+; text and vision. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#splash) |
| [Lily](catalog.md#lily) | One exact Qwen3.6-35B-A3B MLX-affine Q4 checkpoint, group size 64, on Apple GPU family 10+ and macOS 26+. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#lily) |
| [Swiftlet](catalog.md#swiftlet) | Selected Qwen hybrid MoE architectures on macOS/iOS, using qpack containers and bounded resident memory. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#swiftlet) |
| [Flash-MoE](catalog.md#flash-moe) | The implementation targets Qwen3.5-397B-A17B on Apple unified-memory hardware with SSD capacity far exceeding RAM and fixed model geometry. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#flash-moe) |
| [ANEMLL](catalog.md#anemll) | Selected LLM architectures converted to CoreML for Apple Neural Engine, with size, shape, context and quantization restrictions. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#anemll) |
| [ane.cpp](catalog.md#ane-cpp) | Dense Qwen3/Qwen3.5 text inference through private ANE APIs, with M3 Max-specific empirical constraints. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#ane-cpp) |

[↑ By hardware / 按硬件](#hardware)

<a id="intel-arc"></a>

### Intel Arc

The reviewed path is tuned on Arc Pro B70; this is not qualification of every Arc device or advertised architecture.

已查路径以 Arc Pro B70 调优为基础，不代表所有 Arc 设备和宣传架构均已核查。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Mach X](catalog.md#machx) | Intel Arc, built/tuned on Arc Pro B70; inspected Qwen 27B and 35B-A3B text decode paths. Other advertised architectures and video are outside this focused review. | `public-code` · 2026-10-23 · [Details / 详情](catalog.md#machx) |

[↑ By hardware / 按硬件](#hardware)

<a id="ampere"></a>

### RTX 3090 / Ampere

Device-specific forks with different model and memory contracts; neither is just an upstream compile-target switch.

两者都有实际执行改造，但模型和显存契约不同，并非仅切换上游编译目标。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [llamAmpere](catalog.md#llamampere) | Qwen3.8-27B with an MTP head, primarily single-stream inference on Ampere RTX 3090/3090 Ti, where verification width and long-context state compete for compute and VRAM. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#llamampere) |
| [NInfer-3090](catalog.md#ninfer-3090) | Qwen dense/MoE serving on a 24 GB RTX 3090 requires SM86-compatible kernels and a smaller memory budget than upstream consumer Blackwell. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#ninfer-3090) |

[↑ By hardware / 按硬件](#hardware)

<a id="bc250"></a>

### BC-250

A 16 GiB unified-memory offload path. Its default profile drops experts; storage misses remain on the critical path.

16 GiB 统一内存卸载路径；默认配置削减专家，存储未命中仍会阻塞执行。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [N3komata](catalog.md#n3komata) | AMD BC-250, 16 GiB unified memory, Linux/Mesa RADV Vulkan and SSD-backed Qwen3.8-Flash-Next IQ3_XXS GGUF shards. | `public-code` · 2026-11-05 · [Details / 详情](catalog.md#n3komata) |

[↑ By hardware / 按硬件](#hardware)

<a id="mobile"></a>

### Mobile / NPU / 手机 / NPU

CPU, mobile GPU and Hexagon paths have distinct deployment boundaries. Follow the mobile cross-index for reviewed comparisons and platform limitations.

CPU、手机 GPU 和 Hexagon 路径的部署边界不同；移动端交叉索引保留具体对照与平台限制。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Cactus](catalog.md#cactus) | Mobile and wearable deployments; model bundles tested on selected Liquid, Gemma, Qwen and speech families. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#cactus) |
| [MobiInfer Android](catalog.md#mobiinfer-android) | Selected 30B/35B-A3B MoE text paths on Snapdragon Android devices using Hexagon HTP/HVX/HMX and external expert packs; advertised multimodal and MOSS-Image paths are outside this review. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#mobiinfer-android) |
| [Hilum LLM Engine](catalog.md#hilum-engine) | Android Adreno/Vulkan and Apple Metal mobile deployments with GGUF models. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#hilum-engine) |

[↑ By hardware / 按硬件](#hardware)

<a id="models"></a>

## By model / 按模型

[Flash-Next](#flash-next) · [Other Qwen / 其他 Qwen](#qwen) · [GLM-5.3](#glm) · [Image / video / 图像 / 视频](#diffusion) · [Speech / 语音](#speech)

<a id="flash-next"></a>

### Flash-Next

Selected Qwen3.8-Flash-Next paths across devices. Formats, reduced precision, cache modes and optional expert/routing changes prevent a speed-only comparison.

跨设备的指定 Qwen3.8-Flash-Next 路径；权重格式、低精度、缓存模式和可选专家／路由改动需单独比较。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Halogen Flash](catalog.md#halogen-flash) | One model family and AMD gfx1151 unified-memory machines motivate tensor-specific precision choices and separate budgets for resident weights, KV state and the paged lookup table. | `closed-core` · 2026-11-03 · [Details / 详情](catalog.md#halogen-flash) |
| [Qwenox](catalog.md#qwenox) | Qwen3.8-Flash-Next on AMD Ryzen AI Max+ 395 / gfx1151 with 128 GB unified memory; Linux and Windows. Text execution reviewed; advertised vision paths not audited. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#qwenox) |
| [Crucible](catalog.md#crucible) | Qwen3.8-Flash-Next EXL3 packs on one Linux AMD Ryzen AI Max+ 395 / gfx1151 with 128 GB unified memory; text execution reviewed. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#crucible) |
| [Strixite](catalog.md#strixite) | Qwen3.8-Flash-Next on one Linux AMD Strix Halo / gfx1151 machine with 128 GB unified memory; text paths inspected, vision not qualified here. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#strixite) |
| [Spark Engine](catalog.md#spark-engine) | NVIDIA DGX Spark / GB10 sm_121, Linux aarch64. Qwen3.8-Flash-Next text path on one node and N-way RDMA substrate inspected; GLM/DeepSeek multi-node and vision paths are advertised but not fully audited here. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#spark-engine) |
| [Ignis](catalog.md#ignis) | Single SM120a Blackwell GPU (RTX 5090 / RTX PRO 6000), selected Qwen3.8-27B NVFP4 and Flash-Next MoE text paths; image/vision features are advertised but not audited here. | `public-code` · 2026-10-23 · [Details / 详情](catalog.md#ignis) |
| [Basalt](catalog.md#basalt) | Qwen3.8-Flash-Next on Linux/Windows x64 with NVIDIA Blackwell sm_120 and CPU RAM; optional peer GPU tier. Text expert/verify and NVFP4 prefill paths inspected; vision not qualified here. | `public-code` · 2026-11-05 · [Details / 详情](catalog.md#basalt) |
| [N3komata](catalog.md#n3komata) | AMD BC-250, 16 GiB unified memory, Linux/Mesa RADV Vulkan and SSD-backed Qwen3.8-Flash-Next IQ3_XXS GGUF shards. | `public-code` · 2026-11-05 · [Details / 详情](catalog.md#n3komata) |

[↑ By model / 按模型](#models)

<a id="qwen"></a>

### Other Qwen / 其他 Qwen

Selected dense and hybrid-MoE checkpoints; family names do not imply interchangeable architectures or unrestricted model loading. Some engines also appear under Flash-Next.

指定稠密与混合 MoE 检查点；家族名称不意味着架构可互换或任意权重可加载，部分引擎也列入 Flash-Next。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Splash](catalog.md#splash) | Selected Qwen3.8-27B and Qwen3.6-35B-A3B checkpoints, plus compatible Ternary Bonsai 2, on Apple M3 or newer and macOS 26.4+; text and vision. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#splash) |
| [Lily](catalog.md#lily) | One exact Qwen3.6-35B-A3B MLX-affine Q4 checkpoint, group size 64, on Apple GPU family 10+ and macOS 26+. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#lily) |
| [Swiftlet](catalog.md#swiftlet) | Selected Qwen hybrid MoE architectures on macOS/iOS, using qpack containers and bounded resident memory. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#swiftlet) |
| [NInfer](catalog.md#ninfer) | Selected Qwen Dense/MoE checkpoints on Linux and one RTX 5090 (sm_120a), with one resident model and one to eight startup-fixed execution lanes. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#ninfer) |
| [NInfer-3090](catalog.md#ninfer-3090) | Qwen dense/MoE serving on a 24 GB RTX 3090 requires SM86-compatible kernels and a smaller memory budget than upstream consumer Blackwell. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#ninfer-3090) |
| [llamAmpere](catalog.md#llamampere) | Qwen3.8-27B with an MTP head, primarily single-stream inference on Ampere RTX 3090/3090 Ti, where verification width and long-context state compete for compute and VRAM. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#llamampere) |
| [Mach X](catalog.md#machx) | Intel Arc, built/tuned on Arc Pro B70; inspected Qwen 27B and 35B-A3B text decode paths. Other advertised architectures and video are outside this focused review. | `public-code` · 2026-10-23 · [Details / 详情](catalog.md#machx) |
| [Ignis](catalog.md#ignis) | Single SM120a Blackwell GPU (RTX 5090 / RTX PRO 6000), selected Qwen3.8-27B NVFP4 and Flash-Next MoE text paths; image/vision features are advertised but not audited here. | `public-code` · 2026-10-23 · [Details / 详情](catalog.md#ignis) |

[↑ By model / 按模型](#models)

<a id="glm"></a>

### GLM-5.3

The source-reviewed full-GLM cluster path. Newer advertised GLM-Flash and DeepSeek paths are outside this focused review.

已做源码核查的完整 GLM 集群路径；新增宣传的 GLM-Flash 和 DeepSeek 路径未纳入本次完整核查。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [gr8](catalog.md#gr8) | Full GLM-5.3 on three to six DGX Spark / GB10 sm_121a nodes with RoCE v2. Review covers the GLM trellis, S2 and KV-store substrate; newer GLM-Flash and DeepSeek paths are not fully qualified here. | `public-code` · 2026-11-05 · [Details / 详情](catalog.md#gr8) |

[↑ By model / 按模型](#models)

<a id="diffusion"></a>

### Image / video / 图像 / 视频

Different diffusion model families and runtime boundaries. Verify the exact checkpoint, denoising steps, VAE and approximate cache settings in each record.

不同扩散模型家族与运行时边界；应逐项核对检查点、去噪步数、VAE 和近似缓存设置。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Nunchaku](catalog.md#nunchaku) | Targets supported low-bit diffusion checkpoints and compatible NVIDIA GPU kernels, reducing model memory and repeated activation traffic. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#nunchaku) |
| [LightX2V](catalog.md#lightx2v) | Targets large supported image and video models on memory-constrained accelerators and multi-device systems. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#lightx2v) |
| [FreeVideo](catalog.md#freevideo) | VDN-H3 eight-step MiniMax H3 video generation on qualified consumer NVIDIA GPUs; Apple-Silicon support is a separately qualified preview. | `public-code` · 2026-10-16 · [Details / 详情](catalog.md#freevideo) |
| [stable-diffusion.cpp](catalog.md#stable-diffusion-cpp) | Targets multiple local CPU and GPU backends and models that fit supported GGUF and execution paths. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#stable-diffusion-cpp) |

[↑ By model / 按模型](#models)

<a id="speech"></a>

### Speech / 语音

Separate speech recognition from synthesis and streaming service behavior. Model families and state ownership are not interchangeable.

区分语音识别、语音合成与流式服务；不同模型家族和状态管理方式不能直接互换。

| Project / 项目 | Reviewed scope / 已查范围 | Source review / 来源审查 |
| --- | --- | --- |
| [Qwen-ASR (C)](catalog.md#qwen-asr-c) | Qwen3-ASR 0.6B/1.7B on local CPU and optional CUDA/ROCm devices. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#qwen-asr-c) |
| [Qwen3-TTS (C)](catalog.md#qwen3-tts-c) | Qwen3-TTS 0.6B/1.7B speech synthesis on CPU and supported CUDA/Metal paths. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#qwen3-tts-c) |
| [Qingming Qwen3-TTS](catalog.md#qingming-qwen3-tts) | Qwen3-TTS on AMD RX 7900 XTX 24GB and NVIDIA RTX 4090 24GB. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#qingming-qwen3-tts) |
| [whisper.cpp](catalog.md#whisper-cpp) | Whisper ASR on local CPU and diverse accelerator backends. | `public-code` · 2026-10-12 · [Details / 详情](catalog.md#whisper-cpp) |
| [Maya2 Native / Maya3](catalog.md#maya2-native) | Maya3 speech checkpoint with a Qwen3-derived backbone, depth decoder and Mimi codec on NVIDIA CUDA GPUs; author qualification includes H100 and RTX 4090. | `public-code` · 2026-11-03 · [Details / 详情](catalog.md#maya2-native) |

[↑ By model / 按模型](#models)
