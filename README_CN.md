# Awesome Inference Specialization · 推理系统专用化

**收录并分析面向特定模型、硬件和负载构建的专用推理执行栈，重点观察 AI 辅助开发与代码生成是否改变了这些系统的实现、优化和维护方式。**

[English](README.md) · [核心案例](docs/cases.md) · [构建方式对照](docs/comparison.md) · [主题资料库](docs/systems.md) · [按模型领域](docs/domains.md) · [研究问题](docs/research-agenda.md) · [参与维护](CONTRIBUTING.md)

## 为什么建设这个仓库？

专用推理系统并不新。值得调查的是：**构建专用执行栈的方式、可获得性和经济性是否正在变化，这种变化又释放了哪些系统设计空间？**

我们关注通过直接实现、深度改造或生成代码，重新掌握模型执行路径的系统，以及构建这些系统的方法。它们可能重新组织模型计算图、内核分派、状态管理、数据搬移或请求执行；也可以保留通用框架的服务层和已有底层库。

本仓库用具体案例检验一条尚待验证的因果链：

> AI 辅助编码或代码生成可能降低实现与修改成本 → 某些面向少数模型和设备的执行栈可能更值得构建 → 可行的系统设计与交付方式可能随之变化。

**性能提升、开发时间短、使用了 Agent，分别都不足以证明这条因果链。** 我们同时记录重构动机、复用边界、放弃的兼容性、AI 的实际参与、构建投入，以及验证和维护的证据缺口。

![围绕已知部署条件重建执行路径，追踪构建验证与部署维护，并以历史路线和共享基础作为对照](assets/specialization.svg)

## 先看核心案例

<!-- CATALOG-START -->

**[完整目录：161 个项目](docs/systems.md) · [精选分析：63 个案例](docs/cases.md)**

先看构建过程与产出系统，再比较复用边界和证据缺口。以下分组只是阅读顺序；AI 参与不代表效果更好，未披露也不代表纯人工实现。

[多模态理解与交互](docs/domains.md#multimodal) · [图像生成与处理](docs/domains.md#image) · [视频生成与处理](docs/domains.md#video) · [语音与音频](docs/domains.md#audio) · [语言模型](docs/domains.md#text) · [跨模态基础设施](docs/domains.md#general)

模态是交叉检索标签，不替代构建分类；每组先展示三个入口，其余案例可展开，全部保留在案例索引。

### 构建流程与生成的执行程序

| 案例 | 为什么研究它 |
| --- | --- |
| [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) | 一个改造智能体工作流、复用现有内核来构建专用执行栈的实验案例。 |
| [Sol-Engine](docs/cases.md#sol-engine) | 以智能体工作流组合模型专用优化，并以延迟和图像质量约束筛选配置。 |
| [Mirage MPK](docs/cases.md#mirage) | 将显式组装的 LLM 任务图编译为覆盖计算与通信的持久 GPU 执行程序。 |

<details>
<summary>展开本组其余 2 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [Lithos Metal](docs/cases.md#lithos-metal) | 把模型图、芯片配置和生成状态共同编译为 Apple 专用执行程序。 |
| [Magnitude](docs/cases.md#magnitude) | 在 MLX 执行体系内捕获带类型的运算，按数值契约与张量布局构造专用融合内核。 |

</details>

### 围绕指定模型与设备重建原生运行时

| 案例 | 为什么研究它 |
| --- | --- |
| [Splash](docs/cases.md#splash) | 围绕选定模型和 Apple 芯片，把专用草稿、内核与内存策略整合为本地执行栈，并披露由智能体生成专用内核。 |
| [Gufo](docs/cases.md#gufo) | 围绕 Strix Halo 和选定模型重建原生 C++/HIP 执行、状态管理与服务，并复用已有组件。 |
| [zLLM](docs/cases.md#zllm) | 原生重建视觉语言、图像生成与视频处理路径，用模型和设备资格表限制支持范围。 |

<details>
<summary>展开本组其余 16 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [NInfer](docs/cases.md#ninfer) | 围绕选定 Qwen 模型和 RTX 5090，自行组织模型计算、状态管理与请求服务。 |
| [Lily](docs/cases.md#lily) | 为单一检查点重建 Rust/Metal 执行路径，并明确舍弃通用兼容性。 |
| [hipEngine](docs/cases.md#hipengine) | 围绕选定 Radeon 架构重建模型执行、共享 KV 与服务调度。 |
| [imp](docs/cases.md#imp) | 面向单类 Blackwell 芯片重建执行栈，并公开披露编码智能体参与。 |
| [VTE](docs/cases.md#vte) | 为消费级 RDNA3 直接实现 GGUF、HIP 内核生成、显存管理和执行图。 |
| [ZINC](docs/cases.md#zinc) | 用 Zig 与原生后端重建模型执行，分别核对 ROCm、Vulkan 等路径。 |
| [memra](docs/cases.md#memra) | 以 Rust/CUDA 实现并逐型号核验执行路径，同时保留开发暂停和维护边界。 |
| [Kipp](docs/cases.md#kipp) | 以固定检查点注册表限定兼容性，完整实现 C11 Qwen 执行与服务。 |
| [Saragossa](docs/cases.md#saragossa) | 用 Rust/Metal 原生模型路径管理驻留状态，面向本地低延迟推理。 |
| [TensorFold](docs/cases.md#tensorfold) | 以模型、权重格式和平台的资格表限定支持范围，再提供原生 Zig 服务与专用执行。 |
| [Halogen Flash](docs/cases.md#halogen-flash) | 以一个模型家族和一类芯片为边界发布专用二进制，公开部署与量化说明。 |
| [ExLlamaV3](docs/cases.md#exllamav3) | 将 EXL3 编码、低比特状态与专用执行路径配套，服务消费级 GPU 本地推理。 |
| [Llaminar](docs/cases.md#llaminar) | 为 CPU、NVIDIA 与 AMD 混合硬件构建原生模型图和通信执行计划。 |
| [ane.cpp](docs/cases.md#ane-cpp) | 将 ANE 探针实验的结果落实为融合、分块与调度修改。 |
| [Cactus](docs/cases.md#cactus) | 将模型组件捕获与图降低连接到移动端原生运行时，自行管理量化、状态与执行。 |
| [FastFlowLM](docs/cases.md#fastflowlm) | 围绕 AMD NPU 组织模型运行时、内核提供方与设备适配，并明确源码和二进制边界。 |

</details>

### 围绕内存与专家驻留重建执行

| 案例 | 为什么研究它 |
| --- | --- |
| [Flash-MoE](docs/cases.md#flash-moe) | 围绕固定模型和苹果统一内存机器，直接组织 SSD 专家读取与 C/Metal 执行。 |
| [Strata](docs/cases.md#strata) | 针对普通游戏电脑，将 GPU 热专家、CPU 冷专家和状态存储组合成模型专用运行时。 |
| [Swiftlet](docs/cases.md#swiftlet) | 为 Mac 与 iPhone 重建 Qwen 混合 MoE 执行路径，作者明确披露 Claude Code 辅助。 |

<details>
<summary>展开本组其余 6 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [DwarfStar](docs/cases.md#dwarfstar) | 以少数模型和消费级硬件为边界，联合构建原生执行、状态管理与本地服务。 |
| [TurboFieldfare](docs/cases.md#turbo-fieldfare) | 围绕 8 GB 内存限制联合重建 Gemma 的专家存储、调度和执行路径。 |
| [TUFF](docs/cases.md#tuff) | 从 TurboFieldfare 深度分叉，保留有界专家流式机制并扩展模型执行路径。 |
| [SwiftLM](docs/cases.md#swiftlm) | 保留 MLX，并通过维护分叉重构超内存 MoE 的专家 I/O、同步和故障处理。 |
| [Colibri](docs/cases.md#colibri) | 按模型族实现独立 C 执行器，共享专家流式与可选设备后端。 |
| [KTransformers](docs/cases.md#ktransformers) | 将面向 CPU 指令集与 NUMA 的专家执行后端接入 GPU 服务路径。 |

</details>

### 通过深度分叉与专用后端改变执行

| 案例 | 为什么研究它 |
| --- | --- |
| [llamAmpere](docs/cases.md#llamampere) | 深度改造 llama.cpp，将 MTP 验证、压缩 KV 和 SM86 执行路径整合为面向本地长上下文 Qwen 推理的系统。 |
| [vLLM Radiance](docs/cases.md#vllm-radiance) | 保留 vLLM 服务体系，替换 RDNA4 关键执行路径并管理版本耦合。 |
| [ANEMLL Flash llama.cpp](docs/cases.md#anemll-flash-llama) | 保留 llama.cpp，将专家存储、slot 映射和 prefill 执行顺序改成专用路径。 |

<details>
<summary>展开本组其余 5 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [NInfer-3090](docs/cases.md#ninfer-3090) | 以实际内核和内存规划修改把 NInfer 迁移到 24 GB Ampere。 |
| [Infernix](docs/cases.md#infernix) | 为放不进显存的模型重构专家缓存、CPU 计算和 NVMe 数据读取。 |
| [CIRU runtime](docs/cases.md#ciru-runtime) | 围绕特定模型制品集成 Strix Halo 内核、嵌入分页和投机状态。 |
| [Gufo RDMA](docs/cases.md#gufo-rdma) | 将单机 Gufo 扩展为模型专用的双机张量并行与请求状态同步。 |
| [strix-llama.cpp](docs/cases.md#strix-llama-cpp) | 以架构守卫和实测核验维护 Strix Halo 专用内核与状态路径。 |

</details>

### 重建图像生成流水线

| 案例 | 为什么研究它 |
| --- | --- |
| [Iris](docs/cases.md#iris) | 用 C 接管选定图像模型的完整推理流程，同时复用系统数学库和 GPU 能力。 |
| [stable-diffusion.cpp](docs/cases.md#stable-diffusion-cpp) | 通过 C/C++ 模型实现掌握图像/视频扩散的加载、条件编码、采样与组件放置。 |
| [Nunchaku](docs/cases.md#nunchaku) | 围绕 SVDQuant 权重与低秩修正分支，联合设计低比特布局和融合执行。 |

<details>
<summary>展开本组其余 5 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [edge-dit.cpp](docs/cases.md#edge-dit) | 在复用 ggml 的基础上，重建完整 DiT 图执行和分组件、分图段的显存安排。 |
| [Hearth](docs/cases.md#hearth) | 在 CubeCL/wgpu 基础上自行实现模型图与节点执行，形成 Rust 图像生成栈。 |
| [brodiffusion](docs/cases.md#brodiffusion) | 通过 C++ 模型流水线掌握采样与去噪图重放，同时复用底层张量库。 |
| [stable-diffusion.rs](docs/cases.md#stable-diffusion-rs) | 通过 Rust 原生模型实现及后端迁移记录，观察哪些抽象可以保留、哪些数值路径必须重验。 |
| [Quartz](docs/cases.md#saient-quartz) | 区分 Rust 原生图像执行、开发中的 Wan 路径，以及移动端演示使用的独立视频后端。 |

</details>

### 视频执行、设备移植与连续生成

| 案例 | 为什么研究它 |
| --- | --- |
| [LightX2V](docs/cases.md#lightx2v) | 保留张量框架，重建模型推理、权重存储契约与异步双槽搬运。 |
| [Vidax](docs/cases.md#vidax) | 将视频模型及其权重布局、并行安排迁入 JAX/TPU，并记录移植中的数值问题。 |
| [TeleFuser](docs/cases.md#telefuser) | 将模型专用去噪流水线与有界队列、会话状态和执行资源调度连接起来。 |

<details>
<summary>展开本组其余 3 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [FastVideo](docs/cases.md#fastvideo) | 自有模型实现、加载与去噪执行形成完整运行时，稀疏化和蒸馏是另行归因的选项。 |
| [MiniMax-H3 MLX](docs/cases.md#minimax-h3-mlx) | 完整移植音视频联合扩散流水线，区分不变量预计算、容量收益与稠密注意力瓶颈。 |
| [StreamDiffusionV2](docs/cases.md#streamdiffusion-v2) | 面向因果视频生成重组分块去噪与跨设备 KV 状态管理。 |

</details>

### 语音、音频扩散与动作模型运行时

| 案例 | 为什么研究它 |
| --- | --- |
| [Aria](docs/cases.md#aria) | 作者明确披露 LLM 辅助开发，并提供可检查的 C 音频扩散执行路径与一致性测试。 |
| [Qwen-ASR](docs/cases.md#qwen-asr-c) | 围绕 Qwen3-ASR 重建音频预处理、编码、解码和流式状态管理。 |
| [vla.simd](docs/cases.md#vla-simd) | 面向机器人动作模型重建 CPU SIMD 执行路径，区分模型吞吐与闭环控制效果。 |

<details>
<summary>展开本组其余 5 个案例</summary>

| 案例 | 为什么研究它 |
| --- | --- |
| [Qwen3-TTS](docs/cases.md#qwen3-tts-c) | 将语音 token 生成和声码器连接成原生执行路径，并公开构建与测量约束。 |
| [Qingming Qwen3-TTS](docs/cases.md#qingming-qwen3-tts) | 为两种 24GB 消费级 GPU 分别确定原生语音执行路径、容量与并发边界。 |
| [VoxGen](docs/cases.md#voxgen) | 在 Rust 中重建 VoxCPM2 的完整语音生成流程，并直接管理 Vulkan 资源和调度。 |
| [parakeet.cpp (ggml)](docs/cases.md#parakeet-ggml) | 将 NeMo 声学模型和流式状态迁入 C++/ggml，并明确参考一致性的覆盖范围。 |
| [parakeet.cpp (axiom)](docs/cases.md#parakeet-axiom) | 另一条独立的 Parakeet 原生移植路线复用 axiom/MPSGraph，并自行实现模型与缓存状态。 |

</details>

### 把案例放回已有路线中比较

- [历史与相邻路线](docs/systems.md#adjacent)：ZeRO-Inference、FlexGen、DistServe、S-LoRA、MLC LLM 等，帮助判断哪些设计早已有之。
- [共享基础与对照](docs/systems.md#foundation)：通用引擎、编译器、内核和评测工具，说明系统复用了什么、应该与什么比较。

相关性是这些材料在本 Survey 中的作用，不是质量、成熟度或年代排名。完整[资料库](docs/systems.md)保留既有收录。

<details>
<summary>按执行机制检索资料库 / Browse the library by execution mechanism</summary>

[数据驻留与搬移](docs/catalog.md#memory) · [数值表示与低比特执行](docs/catalog.md#precision) · [选择性计算](docs/catalog.md#selection) · [计算复用](docs/catalog.md#reuse) · [生成顺序](docs/catalog.md#decoding) · [并行与调度](docs/catalog.md#serving) · [编译与原生执行](docs/catalog.md#execution) · [构建与验证工具](docs/catalog.md#construction)

</details>

<!-- CATALOG-END -->

## 怎样阅读一个案例？

**为什么另建 → 重构了多少 → 复用与舍弃了什么 → 怎样构建 → 怎样验证和维护。**

例如，[VibeQwen](docs/cases.md#vibeqwen) 是产出的引擎案例，[MetaInfer](docs/catalog.md#metainfer) 是其采用并调整的构建流程来源。两者通过案例卡片连接，不把一个流程及其产物混为同一项目，也不增加重复仓库计数。卡片明确区分作者披露、公开实现、验证覆盖与尚未知晓的成本。

[构建方式对照](docs/comparison.md)先比较执行栈边界和构建投入。八类[执行机制](docs/catalog.md)作为二级检索标签，帮助解释这些设计怎样运行。

## 收录什么？

一个**核心案例**除了说明部署约束和执行机制，还应回答：为什么它能说明“专用执行栈如何被构建”这一研究对象？必须明确产出什么程序、控制哪些执行决策、保留哪些依赖，并提供可追溯来源。构建与维护成本未知可以收录，但必须写明未知。

- **核心案例：** 有目的的执行栈重建，或与具体专用产物相连的构建流程。无需全栈从零实现，也不要求已经确证 AI 参与。
- **历史与相邻路线：** 传统及当代专用系统、编译特化、异构执行与相关构建方法，用来判断哪些早已有之、哪些可能变化。
- **共享基础与对照：** 通用引擎、编译器、内核、优化组件和评测工具，用来解释复用关系与公平比较条件。

相关性与产物类型是独立维度；新近发布、代码少、使用 Agent 或跑得更快，都不是进入核心层的充分条件。以教学为目的的 nano 实现不在本仓库收录范围内。详见[分类与纳入标准](docs/taxonomy.md)。

## 证据与研究

这是基于来源核查的资料库，没有独立复现各项目性能。作者结果不能当作独立验证；量化、近似或模型变化的收益需要与运行时收益分开。AI 参与的判断需要直接披露或可检查的构建流程，不能从文件名、代码风格或项目规模推断。[证据标准](docs/evidence-policy.md)说明各类结论需要什么支撑。

[研究议程](docs/research-agenda.md)围绕“变化在哪里”展开：哪些通用抽象值得替换、哪些构建步骤被自动化、节省能否覆盖验证与维护，以及模型或硬件改变后要付出多少重新适配成本。[本轮系统检索](docs/discovery-2026-10-12.md)记录来源追溯、收录依据和待核实线索；[历史检索记录](docs/survey-2026-10-12.md)保留早期广泛搜集的过程；[主题资料库](docs/systems.md)保留全部既有条目。

[项目数据](catalog/projects.csv)与[案例数据](catalog/cases.json)统一生成首页精选、案例卡片、主题索引、模态入口、机制目录和对照页。维护方法见[贡献指南](CONTRIBUTING.md)。元数据、原创图示、评述与脚本使用 [MIT License](LICENSE)，第三方项目与模型保留各自许可。
