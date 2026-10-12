# Awesome Inference Specialization · 推理系统专用化

**理解专用推理系统利用了什么条件、如何构建，以及验证和维护它们需要什么代价。**

[English](README.md) · [系统与构建流程](docs/systems.md) · [机制索引](docs/catalog.md) · [能力对照](docs/comparison.md) · [研究问题](docs/research-agenda.md) · [参与维护](CONTRIBUTING.md)

## 为什么建设这个仓库？

**当模型、硬件和工作负载已经确定时，推理系统的哪些部分值得专用化，又应该怎样构建？**

已知条件可以带来不同的执行设计：固定的 MoE 结构、有限的显存、选定的数值格式，或反复出现的生成模式，都可能形成专用化机会。本仓库把这些机会与可检查的系统实现、构建流程联系起来，帮助读者：

- **识别专用化机会：** 从部署约束出发，找到具体的执行、状态管理或数据搬移机制。
- **选择实现边界：** 比较原生运行时、共享引擎中的专用后端、编译生成和智能体辅助构建。
- **评估完整代价：** 同时考察性能、质量、验证工作、集成、迁移和维护成本。

编译器和智能体可能降低专用程序的构建成本；这些节省能否覆盖验证和维护成本，仍需研究。本目录提供系统案例与证据，支持对这一问题的比较和实验。

![从已知约束出发，通过四种构建方式形成专用推理系统，并由共享基础设施、验证和维护支撑](assets/specialization.svg)

## 从专用系统及其构建方式开始

<!-- CATALOG-START -->

**98 个条目：34 专用推理系统 · 9 专用系统的构建流程 · 55 支撑基础设施与参照**

先看系统利用了什么条件，再看它如何构建。完整条目按[三个阅读角色](docs/systems.md)组织，原有八类机制用于交叉检索。

### 专用推理系统

| 专用化机会 | 代表系统 | 关注的执行改变 |
| --- | --- | --- |
| 已知模型结构 | [DwarfStar](docs/catalog.md#dwarfstar), [Iris](docs/catalog.md#iris), [Inferix](docs/catalog.md#inferix) | 针对选定架构组织模型执行与生成状态。 |
| 设备与内存约束 | [KTransformers / kt-kernel](docs/catalog.md#ktransformers), [Strata](docs/catalog.md#strata) | 决定专家驻留在哪个设备、由哪个设备执行。 |
| 选定数值格式 | [ExLlamaV3](docs/catalog.md#exllamav3), [Nunchaku](docs/catalog.md#nunchaku) | 联合设计量化表示及其实际执行路径。 |
| 已知负载结构 | [DistServe](docs/catalog.md#distserve), [xDiT](docs/catalog.md#xdit) | 围绕预填充/解码阶段或 DiT 计算组织跨设备执行。 |

### 四种构建方式

| 构建方式 | 构建什么、怎样构建 | 案例 |
| --- | --- | --- |
| 原生实现 | 实现选定模型的计算图和运行策略，按需复用底层库。 | [DwarfStar](docs/catalog.md#dwarfstar), [Iris](docs/catalog.md#iris) |
| 专用后端集成 | 保留共享框架服务，替换关键执行子系统。 | [KTransformers / kt-kernel](docs/catalog.md#ktransformers), [Nunchaku](docs/catalog.md#nunchaku) |
| 编译生成执行程序 | 把模型或任务图编译为面向目标设备的程序与执行安排。 | [Mirage Persistent Kernel](docs/catalog.md#mirage), [MLC LLM](docs/catalog.md#mlc-llm) |
| 智能体辅助构建 | 生成或修改内核及服务程序，检查产物的验证与集成。 | [MetaInfer](docs/catalog.md#metainfer), [Sol-Engine](docs/catalog.md#sol-engine), [KernelAgent](docs/catalog.md#kernelagent) |

这些方式可以组合；使用智能体不说明产物必然更快，测试通过也只覆盖相应验证条件。

### 支撑基础设施与参照

以下项目提供复用组件、比较基线和评测条件，帮助构建和评价前面的专用系统。

- **通用引擎参照:** [vLLM](docs/catalog.md#vllm), [SGLang](docs/catalog.md#sglang), [TensorRT-LLM](docs/catalog.md#tensorrt-llm), [llama.cpp](docs/catalog.md#llama-cpp).
- **编译器与语言:** [Apache TVM](docs/catalog.md#tvm), [IREE](docs/catalog.md#iree), [Triton](docs/catalog.md#triton), [TileLang](docs/catalog.md#tilelang).
- **可复用内核与组件:** [FlashAttention](docs/catalog.md#flash-attention), [FlashInfer](docs/catalog.md#flashinfer), [LMCache](docs/catalog.md#lmcache).
- **评测与集成检查:** [KernelBench](docs/catalog.md#kernelbench), [FastKernels](docs/catalog.md#fastkernels), [Spec-Bench](docs/catalog.md#spec-bench).

### 按机制继续查找

[数据驻留与搬移 (11)](docs/catalog.md#memory) · [数值表示与低比特执行 (9)](docs/catalog.md#precision) · [选择性计算 (8)](docs/catalog.md#selection) · [计算复用 (10)](docs/catalog.md#reuse) · [生成顺序 (5)](docs/catalog.md#decoding) · [并行与调度 (12)](docs/catalog.md#serving) · [编译与原生执行 (32)](docs/catalog.md#execution) · [构建与验证工具 (11)](docs/catalog.md#construction)

来源核查日期：2026-10-12。精选案例属于阅读入口，不代表性能或成熟度排名。

<!-- CATALOG-END -->

## 怎样阅读一个项目？

**约束 → 执行改变 → 部署或生成的产物 → 验证 → 维护成本。**

例如，同样面对显存不足，[KTransformers](docs/catalog.md#ktransformers) 可以把未驻留专家的计算放在 CPU；[MoE-Infinity](docs/catalog.md#moe-infinity) 则搬移并缓存专家权重。约束相同，执行位置和数据搬移方式不同。比较这些选择时，需要固定模型、质量目标、硬件与负载，并计入集成和运行成本。

[机制指南](docs/taxonomy.md)用领域地图和执行路径图解释八类二级检索入口。模态、产物类型、语义变化和源码状态分别标注。量化、缓存或编译是否体现专用化，需要落实到明确的部署假设与执行改变。

## 收录什么？

主要研究对象是**专用推理系统，以及构建这些系统的具体流程**。系统条目应说明利用了什么约束、控制哪部分执行、交付什么产物；构建条目应说明输入是什么、生成或改造什么程序，以及验证覆盖到哪里。

通用引擎、编译器、内核库、优化组件和评测工具提供参照与可复用基础，帮助解释专用系统如何组装和比较。三个阅读角色不代表质量或成熟度排名；专用后端无需实现完整服务器，也可以成为重点案例。

所有条目保留直接来源和适用边界。本目录基于公开来源核查，没有独立复现各项目性能，也不据此建立跨项目速度排名。参见[证据标准](docs/evidence-policy.md)与[检索记录](docs/survey-2026-10-12.md)。

## 研究与维护

[研究议程](docs/research-agenda.md)关注专用化何时划算、应采用哪种构建方式，以及模型、设备或负载变化后哪些设计仍然有效；[延伸阅读](docs/reading-list.md)提供背景材料。欢迎补充系统案例、纠正机制描述，以及提交独立验证和负面结果。

[CSV 目录](catalog/projects.csv)统一生成角色索引、机制目录、对照页和中英文首页精选入口，维护方法见[贡献指南](CONTRIBUTING.md)。元数据、原创图示、评述与脚本使用 [MIT License](LICENSE)，第三方项目和模型保留各自许可。
