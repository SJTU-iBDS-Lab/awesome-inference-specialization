# Awesome Inference Specialization · 专用推理系统

**找到专用推理引擎，理解它们怎样构建，并选择适合其产出的验证方法。**

[English](README.md) · [找引擎](docs/systems.md#system) · [构建流程](docs/systems.md#construction) · [验证方法](docs/validation.md) · [快速对照](docs/representative-comparison.md#chinese) · [最近更新](docs/updates.md)

当模型、设备与负载已知，可以围绕这些条件重新组织执行栈。先从下面的阅读入口开始，对比实际模型／设备和复用边界，再深入上游实现。范围覆盖语言、多模态、图像、视频与音频。

**最近更新，2026-10-12：**新增 [12 案例速查](docs/representative-comparison.md#chinese)和[跨案例综合](docs/synthesis.md)，方便使用已有源码审查记录。[本次变化与检查范围](docs/updates.md)。

## 从这里开始

<!-- CATALOG-START -->

### 12 个起点：读完能学到什么

按执行控制、复用方式、构建路径和验证边界选例，覆盖引擎、编译与 Agent 工作流。这是阅读路线，不按星标、速度或成熟度排名。

| 案例 | 阅读收益 |
| --- | --- |
| [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) | 把 Agent 工作流与报告中的引擎产物连接起来 |
| [Sol-Engine](docs/cases.md#sol-engine) | 了解优化配置怎样验收并组合 |
| [Mirage MPK](docs/cases.md#mirage) | 沿显式任务图理解持久 GPU 执行 |
| [Splash](docs/cases.md#splash) | 一起查看模型专用内核、草稿执行与服务 |
| [Gufo](docs/cases.md#gufo) | 研究设备专用栈及逐模型列明的质量边界 |
| [Flash-MoE](docs/cases.md#flash-moe) | 区分 SSD 流式读取与模型计算本身的改变 |
| [llamAmpere](docs/cases.md#llamampere) | 了解深度分叉改了什么，又保留了哪些上游能力 |
| [Nunchaku](docs/cases.md#nunchaku) | 从打包权重追到融合扩散执行 |
| [LightX2V](docs/cases.md#lightx2v) | 查看明确的异步权重存储契约 |
| [Vidax](docs/cases.md#vidax) | 追踪跨设备的模型转换与数值调试 |
| [Aria](docs/cases.md#aria) | 对照 AI 开发披露与可检查的一致性测试 |
| [vla.simd](docs/cases.md#vla-simd) | 区分原生动作推理与机器人任务成功 |

[12 案例速查：模型／设备、产物、复用与验证](docs/representative-comparison.md#chinese) · [完整对照](docs/comparison.md) · [全部案例](docs/cases.md)

### 按任务继续找

- **找引擎：**[全部引擎](docs/systems.md#system)，再按下方模型领域筛选。
- **构建或优化：**[工作流索引](docs/systems.md#construction)区分内核、模型前向程序和完整服务；[内嵌构建知识](docs/resources.md#embedded-knowledge)连接优化经验与后续尝试。
- **验证结果：**[数值](docs/validation.md#numerical)、[模型／状态](docs/validation.md#model-state)、[生成质量](docs/validation.md#quality)、[服务行为](docs/validation.md#service)是不同契约；[基准](docs/benchmarks.md)提供任务和比较协议。
- **找配套工具：**[性能诊断](docs/resources.md#diagnostics)、[构建知识](docs/resources.md#knowledge)和[复用组件](docs/resources.md#components)。

[多模态理解与交互](docs/domains.md#multimodal) · [图像生成与处理](docs/domains.md#image) · [视频生成与处理](docs/domains.md#video) · [语音与音频](docs/domains.md#audio) · [语言模型](docs/domains.md#text) · [跨模态基础设施](docs/domains.md#general)

完整资料：121 个项目、63 个构建案例。按[执行机制](docs/catalog.md)查找，或读[跨案例结论](docs/synthesis.md)。

<!-- CATALOG-END -->

## 什么值得收录？

记录必须与**专用执行栈的构建或验证有直接、可追溯的联系**：实质性引擎／后端、构建工作流、验证、评测及有明确用途的配套资源。通用引擎和库需要具体的复用或对照关系；简单封装、泛化优化或仅面向教学的 nano 复现不能单独构成收录理由。[纳入标准与分类](docs/taxonomy.md)。

## 怎样读证据

沿着**为什么另建 → 控制什么 → 复用与取舍 → 怎样构建 → 如何验证和维护**阅读。内核、模型前向程序和完整服务是不同产物。[完整案例](docs/cases.md)保留构建过程、AI 参与、投入、验证与维护证据。

本仓库核查公开来源，未独立复现项目性能。AI 参与需要直接披露或可检查的工作流；报告速度提升或使用 Agent，均不足以证明全生命周期成本下降。执行优化须与量化、近似和模型改变分开讨论。[证据规范](docs/evidence-policy.md) · [研究问题](docs/research-agenda.md) · [资源核查](docs/resources-audit-2026-10-12.md)。

<details>
<summary>展开资料结构图</summary>

![引擎、构建方案与验证方法为核心；评测基准与配套资源支持比较](assets/specialization.svg)

</details>

[贡献或更正条目](CONTRIBUTING.md)。目录由[项目数据](catalog/projects.csv)、[案例数据](catalog/cases.json)及[阅读选例](catalog/showcase.json)生成。元数据、原创图示、评论与脚本采用 [MIT](LICENSE)；链接项目及模型保留各自许可。
