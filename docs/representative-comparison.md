# Representative comparison / 代表案例速查

> Generated from [showcase.json](../catalog/showcase.json), [cases.json](../catalog/cases.json) and [projects.csv](../catalog/projects.csv).

[Home](../README.md) · [中文表格](#chinese) · [Full comparison](comparison.md) · [Case synthesis](synthesis.md) · [Validation guide](validation.md)

12 deliberately different reading examples: native runtimes, a deep fork, memory/representation-driven execution, compilation, agent workflows and model ports. Selection balances construction and validation lessons across model domains; it is not a popularity, performance or maturity ranking.

Scope means the reviewed configuration, not a complete current support list. Where a record does not enumerate model names or devices, the table says so rather than guessing. Open the case for the selection lesson, construction/AI evidence, effort and maintenance, and the source for exact version limits.

These are source-review summaries, not reproduced benchmarks. Unknown lifecycle costs remain in the full cases; absence of disclosure is not zero cost. [Evidence policy](evidence-policy.md).

| Case / source | Reviewed model & device | Artifact & execution control | Retained components | Validation boundary |
| --- | --- | --- | --- | --- |
| [MetaInfer → VibeQwen](cases.md#vibeqwen) · [upstream](https://github.com/MetaInfer/MetaInfer) · [source](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/) | Qwen-3.6-35B-A3B NVFP4; one B200 | Reported model + serving stack; engine source not established | vLLM / TensorRT-LLM kernels; adapted MetaInfer | Author performance/accuracy checks; experimental, no independent reproduction |
| [Sol-Engine](cases.md#sol-engine) · [upstream](https://github.com/NVlabs/Sana/tree/sol-engine) · [source](https://github.com/NVlabs/Sana/blob/sol-engine/README.md) | Inspected Wan2.2-TI2V-5B path; GPU, shape and quality constraints per configuration | Video codebase + configuration workflow; cache / sparsity / fusion | SGLang multimodal_gen; model pipelines and kernels | LPIPS, visual review, engagement checks; no equivalence proof |
| [Mirage MPK](cases.md#mirage) · [upstream](https://github.com/mirage-project/mirage) · [source](https://github.com/mirage-project/mirage/blob/mpk/README.md) | Supported LLM task graphs; NVIDIA GPU / SM allocation / topology constraints | Compiled persistent program; computation + communication scheduling | PyTorch tensors, CUDA, NVSHMEM, supported fused operations | Demos and profiling inspected; arbitrary model support not implied |
| [Splash](cases.md#splash) · [upstream](https://github.com/incoai/splash) · [source](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/README.md) | Selected Qwen3.8-27B / Qwen3.6-35B-A3B / compatible Bonsai 2; Apple M3+, macOS 26.4+ | C++/Metal runtime + HTTP frontend; target/draft, state, memory policy | Checkpoints, tokenizers, Apple runtimes, llama.cpp-derived material | Numerical/model/HTTP tests inspected, not run; kernel AI disclosure is narrower than whole-engine authorship |
| [Gufo](cases.md#gufo) · [upstream](https://github.com/gufo-org/gufo) · [source](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/README.md) | Selected models, including reviewed Qwen3.8 Flash-Next / Qwen-Image 2.1 / H3 paths; Linux gfx1151, typically 128 GiB | C++/HIP execution, kernels, sessions and local serving | ROCm/HIP, BLAS, llama.cpp/ggml and attributed model code | Vision parity failure; small image coverage; full-video quality unqualified |
| [Flash-MoE](cases.md#flash-moe) · [upstream](https://github.com/danveloper/flash-moe) · [source](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/README.md) | Qwen3.5-397B-A17B; Apple unified memory + SSD (reported 48 GB MacBook target) | C/Metal prototype; expert routing, I/O and execution | Metal, Accelerate, dispatch, OS page cache, pretrained weights | K=4 versus model top-10; 2-bit JSON failures; no equivalent headline-speed comparison |
| [llamAmpere](cases.md#llamampere) · [upstream](https://github.com/JakeATX/llamAmpere) · [source](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN_AMPERE.md) | Qwen3.8-27B + MTP; chiefly single-stream RTX 3090 / 3090 Ti | llama.cpp fork; SM86 kernels, MTP verification and KV state | GGML/GGUF, llama.cpp server/model support, TurboQuant/MTP | Separate Swift checkpoint and KV changes; parallel-8 startup failure remains |
| [Nunchaku](cases.md#nunchaku) · [upstream](https://github.com/nunchux-ai/nunchaku) · [source](https://github.com/nunchux-ai/nunchaku/blob/main/README.md) | Supported low-bit diffusion checkpoints; compatible NVIDIA GPU kernels; model names not enumerated in this record | Diffusion backend + adapters; low-bit / low-rank fused operations | DeepCompressor checkpoints; PyTorch/Diffusers integrations | Quantization changes numerics; separate offload/cache/checkpoint effects |
| [LightX2V](cases.md#lightx2v) · [upstream](https://github.com/ModelTC/LightX2V) · [source](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/README.md) | Supported image/video models; memory-constrained accelerators and multi-device systems; models not enumerated here | Model runtime; layout planning, prefetch streams and two-slot buffers | PyTorch/stream facilities, checkpoints, selectable kernels | Contiguous offload rejects graph capture/cache/multi-rank combinations; no execution here |
| [Vidax](cases.md#vidax) · [upstream](https://github.com/FlyingGiraffe/vidax) · [source](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/README.md) | Selected video models, including the reviewed Wan2.1 path; JAX/Flax TPU meshes | Model port; checkpoint translation, samplers and sharding | JAX/Flax, Pallas, original checkpoints and references | Precision bugs documented; benchmark/configuration-specific evidence; TPUs not run here |
| [Aria](cases.md#aria) · [upstream](https://github.com/matteospanio/aria) · [source](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/README.md) | Stable Audio 3 small/medium; CPU, optional CUDA | Complete C audio pipeline; conditioning, diffusion, sampling, decoding | Released weights, vector/OpenMP facilities, optional CUDA libraries | Controlled reference/noise parity tests inspected, not run; quantized/steered modes need separate checks |
| [vla.simd](cases.md#vla-simd) · [upstream](https://github.com/cair-vinuni/vla.simd) · [source](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/README.md) | Selected vision-language-action policies; x86 AVX2 and ARM NEON / Apple CPU | Native operators, model adapters and actions; Python robot integration outside | Pretrained weights, GGUF conventions, architecture libraries | Fixed-input checks; action throughput is not closed-loop frequency or robot safety |

<a id="chinese"></a>

## 中文速查

这 12 个例子覆盖原生运行时、深度分叉、内存与表示驱动的执行、编译、Agent 工作流和模型移植。选例依据是构建与验证的阅读价值，不是星标、速度或成熟度。范围只代表已检查的配置，不是完整支持列表；记录未列明的模型／设备不会补猜。全部记录均未在本仓库独立复现性能，完整案例保留投入与维护的未知项。

| 案例／来源 | 已查模型与设备 | 产物与执行控制 | 保留的组件 | 验证边界 |
| --- | --- | --- | --- | --- |
| [MetaInfer → VibeQwen](cases.md#vibeqwen) · [upstream](https://github.com/MetaInfer/MetaInfer) · [source](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/) | Qwen-3.6-35B-A3B NVFP4；单张 B200 | 报告中的模型执行与服务栈；未确认引擎源码公开 | vLLM／TensorRT-LLM 内核；改造 MetaInfer | 作者性能／准确率检查；实验性质，未独立复现 |
| [Sol-Engine](cases.md#sol-engine) · [upstream](https://github.com/NVlabs/Sana/tree/sol-engine) · [source](https://github.com/NVlabs/Sana/blob/sol-engine/README.md) | 已检查 Wan2.2-TI2V-5B 路径；GPU、形状与质量条件随配置限定 | 视频代码与配置工作流；缓存／稀疏／融合 | SGLang multimodal_gen；模型流水线与内核 | LPIPS、视觉复核与优化生效检查；不是等价性证明 |
| [Mirage MPK](cases.md#mirage) · [upstream](https://github.com/mirage-project/mirage) · [source](https://github.com/mirage-project/mirage/blob/mpk/README.md) | 受支持的 LLM 任务图；NVIDIA GPU／SM 分配／拓扑约束 | 编译后的持久执行程序；计算与通信调度 | PyTorch 张量、CUDA、NVSHMEM 与受支持的融合算子 | 检查了示例与性能接口；不代表支持任意模型 |
| [Splash](cases.md#splash) · [upstream](https://github.com/incoai/splash) · [source](https://github.com/incoai/splash/blob/8cd9fb0ea768042153f2490d4201296b483a45dd/README.md) | 选定 Qwen3.8-27B／Qwen3.6-35B-A3B／兼容 Bonsai 2；Apple M3+、macOS 26.4+ | C++/Metal 运行时与 HTTP 前端；目标／草稿执行、状态和内存策略 | 检查点、分词器、Apple 运行时及源于 llama.cpp 的组件 | 检查但未运行数值／模型／HTTP 测试；AI 内核披露不等于整个引擎由 AI 编写 |
| [Gufo](cases.md#gufo) · [upstream](https://github.com/gufo-org/gufo) · [source](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/README.md) | 选定模型，包括已查 Qwen3.8 Flash-Next／Qwen-Image 2.1／H3 路径；Linux gfx1151，通常 128 GiB | C++/HIP 执行、内核、会话与本地服务 | ROCm/HIP、BLAS、llama.cpp/ggml 与注明来源的模型代码 | 视觉一致性仍有失败；图像覆盖小；完整视频质量未完成验收 |
| [Flash-MoE](cases.md#flash-moe) · [upstream](https://github.com/danveloper/flash-moe) · [source](https://github.com/danveloper/flash-moe/blob/3601d41882a346d85041f7955c66429d248e8cd9/README.md) | Qwen3.5-397B-A17B；Apple 统一内存与 SSD（报告目标为 48 GB MacBook） | C/Metal 原型；专家路由、I/O 与执行 | Metal、Accelerate、dispatch、系统页缓存与预训练权重 | K=4 与模型 top-10 不同；2-bit JSON 失败；头条速度不能视为等价比较 |
| [llamAmpere](cases.md#llamampere) · [upstream](https://github.com/JakeATX/llamAmpere) · [source](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/QWEN_AMPERE.md) | Qwen3.8-27B 与 MTP；主要为单流 RTX 3090／3090 Ti | llama.cpp 分叉；SM86 内核、MTP 验证与 KV 状态 | GGML/GGUF、llama.cpp 服务／模型支持、TurboQuant/MTP | 需区分 Swift 检查点及 KV 改变；parallel-8 启动失败仍在 |
| [Nunchaku](cases.md#nunchaku) · [upstream](https://github.com/nunchux-ai/nunchaku) · [source](https://github.com/nunchux-ai/nunchaku/blob/main/README.md) | 受支持的低比特扩散检查点与兼容 NVIDIA GPU 内核；本条记录未逐一列出模型名 | 扩散后端与适配器；低比特／低秩融合算子 | DeepCompressor 检查点；PyTorch/Diffusers 集成 | 量化改变数值；需分离卸载、缓存及检查点的影响 |
| [LightX2V](cases.md#lightx2v) · [upstream](https://github.com/ModelTC/LightX2V) · [source](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/README.md) | 受支持的图像／视频模型；显存受限加速器与多设备系统；此处未逐一列出模型 | 模型运行时；布局规划、预取流与双槽缓冲 | PyTorch／流机制、检查点与可选内核 | 连续卸载不支持图捕获／缓存／多 rank 的相关组合；本仓库未执行 |
| [Vidax](cases.md#vidax) · [upstream](https://github.com/FlyingGiraffe/vidax) · [source](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/README.md) | 选定视频模型，包括已查 Wan2.1 路径；JAX/Flax TPU 网格 | 模型移植；检查点转换、采样器与切分 | JAX/Flax、Pallas、原始检查点与参考实现 | 记录了精度错误；证据限于配置与评测；本仓库未运行 TPU |
| [Aria](cases.md#aria) · [upstream](https://github.com/matteospanio/aria) · [source](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/README.md) | Stable Audio 3 small/medium；CPU 与可选 CUDA | 完整 C 音频流水线；条件编码、扩散、采样与解码 | 公开权重、向量／OpenMP 机制与可选 CUDA 库 | 检查但未运行受控参考／噪声一致性测试；量化／引导模式需另验 |
| [vla.simd](cases.md#vla-simd) · [upstream](https://github.com/cair-vinuni/vla.simd) · [source](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/README.md) | 选定视觉语言动作策略；x86 AVX2 与 ARM NEON／Apple CPU | 原生算子、模型适配与动作计算；Python 机器人集成在边界之外 | 预训练权重、GGUF 约定与架构库 | 固定输入检查；动作吞吐不等于闭环频率或机器人安全 |

## Why these cases? / 为什么选这些案例

| Case / 案例 | Reading benefit / 阅读收益 |
| --- | --- |
| [MetaInfer → VibeQwen](cases.md#vibeqwen) | Connect an agent workflow to a reported deployed engine / 把 Agent 工作流与报告中的引擎产物连接起来 |
| [Sol-Engine](cases.md#sol-engine) | See how optimization choices are accepted and composed / 了解优化配置怎样验收并组合 |
| [Mirage MPK](cases.md#mirage) | Follow an explicit task graph into persistent GPU execution / 沿显式任务图理解持久 GPU 执行 |
| [Splash](cases.md#splash) | Inspect model-shaped kernels, draft execution and serving together / 一起查看模型专用内核、草稿执行与服务 |
| [Gufo](cases.md#gufo) | Study a device-focused stack with explicit per-model quality limits / 研究设备专用栈及逐模型列明的质量边界 |
| [Flash-MoE](cases.md#flash-moe) | Separate SSD streaming from changes to the model computation / 区分 SSD 流式读取与模型计算本身的改变 |
| [llamAmpere](cases.md#llamampere) | See what a deep fork changes and what upstream still supplies / 了解深度分叉改了什么，又保留了哪些上游能力 |
| [Nunchaku](cases.md#nunchaku) | Trace packed checkpoints into fused diffusion execution / 从打包权重追到融合扩散执行 |
| [LightX2V](cases.md#lightx2v) | Inspect explicit asynchronous weight-storage contracts / 查看明确的异步权重存储契约 |
| [Vidax](cases.md#vidax) | Follow model conversion and numerical debugging across devices / 追踪跨设备的模型转换与数值调试 |
| [Aria](cases.md#aria) | Read an AI disclosure beside an inspectable parity harness / 对照 AI 开发披露与可检查的一致性测试 |
| [vla.simd](cases.md#vla-simd) | Distinguish native action inference from robot task success / 区分原生动作推理与机器人任务成功 |

For all cases and disclosed construction effort, use the [full comparison](comparison.md). For references, trade-offs and maintenance details, use the [case collection](cases.md). / 全量边界与投入见完整对照，具体来源、取舍及维护见案例全文。
