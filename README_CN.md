# Awesome Inference Specialization · 推理系统专用化

**收录并分析面向特定模型、硬件和负载构建的专用推理执行栈，重点观察 AI 辅助开发与代码生成是否改变了这些系统的实现、优化和维护方式。**

[English](README.md) · [核心案例](docs/cases.md) · [构建方式对照](docs/comparison.md) · [主题资料库](docs/systems.md) · [研究问题](docs/research-agenda.md) · [参与维护](CONTRIBUTING.md)

## 为什么建设这个仓库？

专用推理系统并不新。值得调查的是：**构建专用执行栈的方式、可获得性和经济性是否正在变化，这种变化又释放了哪些系统设计空间？**

我们关注通过直接实现、深度改造或生成代码，重新掌握模型执行路径的系统，以及构建这些系统的方法。它们可能重新组织模型计算图、内核分派、状态管理、数据搬移或请求执行；也可以保留通用框架的服务层和已有底层库。

本仓库用具体案例检验一条尚待验证的因果链：

> AI 辅助编码或代码生成可能降低实现与修改成本 → 某些面向少数模型和设备的执行栈可能更值得构建 → 可行的系统设计与交付方式可能随之变化。

**性能提升、开发时间短、使用了 Agent，分别都不足以证明这条因果链。** 我们同时记录重构动机、复用边界、放弃的兼容性、AI 的实际参与、构建投入，以及验证和维护的证据缺口。

![围绕已知部署条件重建执行路径，追踪构建验证与部署维护，并以历史路线和共享基础作为对照](assets/specialization.svg)

## 先看核心案例

<!-- CATALOG-START -->

先看构建过程与产出系统，再比较复用边界和证据缺口。以下分组只是阅读顺序；AI 参与不代表效果更好，未披露也不代表纯人工实现。

### 构建流程实际产出了什么

| 案例 | 为什么研究它 |
| --- | --- |
| [VibeQwen](docs/cases.md#vibeqwen) | 一个改造智能体工作流、复用现有内核来构建专用执行栈的实验案例。 |
| [Sol-Engine](docs/cases.md#sol-engine) | 以智能体工作流组合模型专用优化，并以延迟和图像质量约束筛选配置。 |

### 围绕部署条件重建执行栈

| 案例 | 为什么研究它 |
| --- | --- |
| [Flash-MoE](docs/cases.md#flash-moe) | 围绕固定模型和苹果统一内存机器，直接组织 SSD 专家读取与 C/Metal 执行。 |
| [DwarfStar](docs/cases.md#dwarfstar) | 以少数模型和消费级硬件为边界，联合构建原生执行、状态管理与本地服务。 |
| [Strata](docs/cases.md#strata) | 针对普通游戏电脑，将 GPU 热专家、CPU 冷专家和状态存储组合成模型专用运行时。 |
| [Iris](docs/cases.md#iris) | 用 C 接管选定图像模型的完整推理流程，同时复用系统数学库和 GPU 能力。 |
| [TensorFold](docs/cases.md#tensorfold) | 以模型、权重格式和平台的资格表限定支持范围，再提供原生 Zig 服务与专用执行。 |
| [Halogen Flash](docs/cases.md#halogen-flash) | 以一个模型家族和一类芯片为边界发布专用二进制，公开部署与量化说明。 |
| [ExLlamaV3](docs/cases.md#exllamav3) | 将 EXL3 编码、低比特状态与专用执行路径配套，服务消费级 GPU 本地推理。 |

### 专用后端与编译生成的执行程序

| 案例 | 为什么研究它 |
| --- | --- |
| [Magnitude](docs/cases.md#magnitude) | 在 MLX 执行体系内捕获带类型的运算，按数值契约与张量布局构造专用融合内核。 |
| [KTransformers](docs/cases.md#ktransformers) | 将面向 CPU 指令集与 NUMA 的专家执行后端接入 GPU 服务路径。 |
| [Nunchaku](docs/cases.md#nunchaku) | 围绕 SVDQuant 权重与低秩修正分支，联合设计低比特布局和融合执行。 |
| [Mirage MPK](docs/cases.md#mirage) | 将显式组装的 LLM 任务图编译为覆盖计算与通信的持久 GPU 执行程序。 |

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

[研究议程](docs/research-agenda.md)围绕“变化在哪里”展开：哪些通用抽象值得替换、哪些构建步骤被自动化、节省能否覆盖验证与维护，以及模型或硬件改变后要付出多少重新适配成本。[历史检索记录](docs/survey-2026-10-12.md)保留早期广泛搜集的过程；[主题资料库](docs/systems.md)保留全部既有条目。

[项目数据](catalog/projects.csv)与[案例数据](catalog/cases.json)统一生成首页精选、案例卡片、主题索引、机制目录和对照页。维护方法见[贡献指南](CONTRIBUTING.md)。元数据、原创图示、评述与脚本使用 [MIT License](LICENSE)，第三方项目与模型保留各自许可。
