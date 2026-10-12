# Awesome Inference Specialization · 推理系统专用化

**从执行机制理解推理系统：数据怎样放、计算怎样省、程序怎样构建。**

[English](README.md) · [完整目录](docs/catalog.md) · [能力对照](docs/comparison.md) · [分类依据](docs/taxonomy.md) · [本轮调研](docs/survey-2026-10-12.md) · [参与维护](CONTRIBUTING.md)

![八类机制地图：数据驻留、精度、选择性计算、复用、生成顺序、调度、编译与构建工具](assets/landscape.svg)

从具体执行决策进入目录：**搬什么、怎样表示、跳过什么、复用什么、怎样生成、怎样调度、怎样编译？** LLM、图像和视频作为交叉标签。每个项目都注明实际机制、产物形态、直接证据及适用边界。

## 按机制浏览

<!-- CATALOG-START -->

**98 个项目 · 8 个机制入口 · 最近核查 2026-10-12**

每个项目选一个主要入口；模态、产物类型和具体机制另外标注。构建与验证工具单独标识，数量不代表质量排名。

| 机制入口 | 改变了什么 | 从这些项目开始 |
| --- | --- | --- |
| [数据驻留与搬移 (11)](docs/catalog.md#memory) | 权重、专家和 KV 的驻留、分页、预取与卸载。 | [KTransformers / kt-kernel](docs/catalog.md#ktransformers), [vAttention](docs/catalog.md#vattention), [Mooncake](docs/catalog.md#mooncake) |
| [数值表示与低比特执行 (9)](docs/catalog.md#precision) | 联合设计低比特格式、布局和执行内核。 | [ExLlamaV3](docs/catalog.md#exllamav3), [Nunchaku](docs/catalog.md#nunchaku), [T-MAC](docs/catalog.md#t-mac) |
| [选择性计算 (8)](docs/catalog.md#selection) | 选择神经元、token 或注意力块，并明确近似条件。 | [MInference](docs/catalog.md#minference), [SnapKV](docs/catalog.md#snapkv), [Sparse VideoGen](docs/catalog.md#sparse-videogen) |
| [计算复用 (10)](docs/catalog.md#reuse) | 复用请求前缀、特征或跨时间步注意力结果。 | [LMCache](docs/catalog.md#lmcache), [TeaCache](docs/catalog.md#teacache), [TaylorSeer](docs/catalog.md#taylorseer) |
| [生成顺序 (5)](docs/catalog.md#decoding) | 候选生成与验证，或重新组织块生成流程。 | [EAGLE](docs/catalog.md#eagle), [Lookahead Decoding](docs/catalog.md#lookahead), [Inferix](docs/catalog.md#inferix) |
| [并行与调度 (12)](docs/catalog.md#serving) | 围绕负载约束安排阶段、设备与请求。 | [DistServe](docs/catalog.md#distserve), [Sarathi-Serve](docs/catalog.md#sarathi-serve), [xDiT](docs/catalog.md#xdit) |
| [编译与原生执行 (32)](docs/catalog.md#execution) | 融合、降低抽象层级、专用化及分派原生内核。 | [Mirage Persistent Kernel](docs/catalog.md#mirage), [FlashAttention](docs/catalog.md#flash-attention), [MLC LLM](docs/catalog.md#mlc-llm) |
| [构建与验证工具 (11)](docs/catalog.md#construction) | 智能体、内核语言和评测基础设施。 | [MetaInfer](docs/catalog.md#metainfer), [Sol-Engine](docs/catalog.md#sol-engine), [KernelBench](docs/catalog.md#kernelbench) |

<!-- CATALOG-END -->

## 三种机制，三种不同的检验条件

![数据搬移、状态复用和候选验证的三条执行路径](assets/mechanisms.svg)

- **数据与计算放置：** [KTransformers](docs/catalog.md#ktransformers) 把部分 MoE 专家计算放在 CPU；[MoE-Infinity](docs/catalog.md#moe-infinity) 把专家权重搬入并缓存在 GPU。约束相似，执行选择不同。
- **状态复用：** [LMCache](docs/catalog.md#lmcache) 可以复用匹配前缀的 KV；[TeaCache](docs/catalog.md#teacache) 复用较早去噪步骤的残差。两者需要满足不同的有效性条件。
- **候选验证：** [EAGLE](docs/catalog.md#eagle) 提出候选 token，再由目标模型检查；[Medusa](docs/catalog.md#medusa) 同样使用候选树，但训练方式和接受规则需要单独判断。

[分类文档](docs/taxonomy.md)进一步解释各机制的边界，以及同时属于多个方向的项目如何归类。

## 收录什么？

项目需要有可辨认的约束，并据此改变**执行、数据搬移、数值表示、调度或程序构建**。运行时、后端、内核库、编译器与验证工具分别标注，不设 Core / Adjacent 高低层级。能解释完整子系统机制的内核库也有收录价值。

仅有 API 包装、部署配方或论文性能标题不足以确认机制。[vLLM](docs/catalog.md#vllm)、[SGLang](docs/catalog.md#sglang)、[TensorRT-LLM](docs/catalog.md#tensorrt-llm) 等通用引擎同样纳入具体机制比较；教学项目和 [Diffusers](https://github.com/huggingface/diffusers) 则提供背景与生态参照。

**证据边界：** 本目录核查了公开来源，没有独立复现各项目性能。代码可见不代表许可开放、正确性通过或生产可用。低精度、近似计算、模型训练与执行实现的变化分别说明。[证据标准 →](docs/evidence-policy.md)

## 研究与维护

构建专用系统的成本降低后，部署是否会更多采用专用执行路径？共享运行时能否吸收大部分收益？这些仍是待验证的问题。参见[研究议程](docs/research-agenda.md)、[延伸阅读](docs/reading-list.md)及[本轮检索记录与修正](docs/survey-2026-10-12.md)。

[CSV 目录](catalog/projects.csv)统一生成中英首页导航、完整项目目录和对照页。欢迎补充项目、纠正机制描述、提交独立验证与负面结果；维护方法见[贡献指南](CONTRIBUTING.md)。

目录元数据、原创图示、评述与脚本使用 [MIT License](LICENSE)；第三方项目、模型及材料保留各自许可。
