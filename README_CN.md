# Awesome Inference Specialization · 专用推理系统

**收录并分析专用推理引擎、构建这些引擎的方案，以及验证它们的方案。**

[English](README.md) · [专用推理引擎](docs/systems.md#system) · [构建方案](docs/systems.md#construction) · [验证方案](docs/validation.md) · [评测基准](docs/benchmarks.md) · [配套资源](docs/resources.md)

## 为什么建设这个仓库？

当模型、硬件和负载已知时，开发者可以围绕这些条件重新构建部分执行栈。我们关注：**它们重构了什么，如何构建出可用的引擎，又如何确认引擎确实有效**。范围涵盖语言、多模态、图像、视频和音频模型。

专用推理系统并不新。值得研究的是，AI 辅助开发与代码生成是否改变了它们的构建、获取和维护成本，让更多面向特定条件的系统设计变得可行。使用了 Agent 或报告了性能提升，都不足以单独证明这一变化。

本仓库连接三类证据：

- **专用推理引擎：**掌握了哪些执行决策，复用了什么，放弃了哪些兼容性。
- **构建方案：**原生实现、深度分叉、模型到程序的编译、Agent 工作流，以及实际产出的范围。
- **验证方案：**数值、状态、生成质量和服务行为的检查，以及覆盖范围、验证开销和失效边界。

[评测基准](docs/benchmarks.md)单独提供任务与比较协议。[性能诊断、构建知识和可复用组件](docs/resources.md)作为配套资源，需能说明与具体引擎或构建流程的联系。

![专用推理引擎、构建方案与验证方案构成三个核心对象；评测基准提供任务和协议，性能诊断、构建知识与组件提供配套支持](assets/specialization.svg)

## 从这里开始

<!-- CATALOG-START -->

### 专用推理引擎

从执行栈重建方式入手，再按模型、设备和机制筛选。下面是阅读入口，完整引擎索引和案例分析另页列出。

| 执行栈阅读路线 | 代表案例 |
| --- | --- |
| 围绕指定模型与设备重建原生运行时 | [Splash](docs/cases.md#splash) · [Gufo](docs/cases.md#gufo) · [NInfer](docs/cases.md#ninfer) |
| 围绕内存与专家驻留重建执行 | [Flash-MoE](docs/cases.md#flash-moe) · [Strata](docs/cases.md#strata) · [Swiftlet](docs/cases.md#swiftlet) |
| 通过深度分叉与专用后端改变执行 | [llamAmpere](docs/cases.md#llamampere) · [vLLM Radiance](docs/cases.md#vllm-radiance) · [ANEMLL Flash llama.cpp](docs/cases.md#anemll-flash-llama) |
| 重建图像生成流水线 | [Iris](docs/cases.md#iris) · [stable-diffusion.cpp](docs/cases.md#stable-diffusion-cpp) · [Nunchaku](docs/cases.md#nunchaku) |
| 视频执行、设备移植与连续生成 | [LightX2V](docs/cases.md#lightx2v) · [Vidax](docs/cases.md#vidax) · [TeleFuser](docs/cases.md#telefuser) |
| 语音、音频扩散与动作模型运行时 | [Aria](docs/cases.md#aria) · [Qwen-ASR](docs/cases.md#qwen-asr-c) · [vla.simd](docs/cases.md#vla-simd) |

[全部引擎](docs/systems.md#system) · [全部构建案例](docs/cases.md) · [重构边界对照](docs/comparison.md)

[多模态理解与交互](docs/domains.md#multimodal) · [图像生成与处理](docs/domains.md#image) · [视频生成与处理](docs/domains.md#video) · [语音与音频](docs/domains.md#audio) · [语言模型](docs/domains.md#text) · [跨模态基础设施](docs/domains.md#general)

### 构建与优化方案

把构建流程与生成产物连起来。内核、模型前向程序和完整服务是不同的产出范围。

| 方案 | 实际产出范围 |
| --- | --- |
| [MetaInfer](docs/catalog.md#metainfer) | 模型／服务构建；关联 VibeQwen 产出案例 |
| [Sol-Engine](docs/catalog.md#sol-engine) | 模型专用视频执行与质量约束优化 |
| [Mirage Persistent Kernel](docs/catalog.md#mirage) | 任务图编译与持久 GPU 执行 |
| [KernelAgent](docs/catalog.md#kernelagent) | 生成内核并重新组合模型前向程序 |
| [Atrex Kernel Agent (AKA)](docs/catalog.md#atrex-kernel-agent) | 性能反馈驱动的内核构建与验收流程 |

[全部构建方案](docs/systems.md#construction) · [MetaInfer → VibeQwen 案例链](docs/cases.md#vibeqwen)

### 正确性与质量验证方案

| 检验对象 | 方案入口 |
| --- | --- |
| 数值与算子组合 | [参考实现差分、组合后复检](docs/validation.md#numerical) |
| 模型组合与状态覆盖 | [模型组合检查与状态覆盖要求](docs/validation.md#model-state) |
| 图像／视频质量 | [感知质量与误差约束](docs/validation.md#quality) |
| 服务接口与功能 | [接口测试、判定器及其覆盖边界](docs/validation.md#service) |

验证器可以内嵌在引擎或构建框架中；这里索引方案，不重复计算仓库。数值检查、感知质量和功能测试不能相互替代。

### 评测基准与任务集

| 基准 | 比较的问题 |
| --- | --- |
| [FastKernels](docs/benchmarks.md#fastkernels) | 候选内核的收益能否在模型集成后保留？ |
| [Atrex-Bench](docs/benchmarks.md#atrex-bench) | 生成算子能否编译、通过数值检查并有效利用目标硬件？ |
| [KernelBench](docs/benchmarks.md#kernelbench) | 在指定评测协议下，生成实现与可执行参考程序相比如何？ |

基准提供任务、参考程序和比较协议；通过算子评测不等于完成整个引擎的验收。[查看评测范围与限制](docs/benchmarks.md)。

### 配套资源

| 用途 | 精选入口 |
| --- | --- |
| [性能诊断](docs/resources.md#diagnostics) | [ncu-report-skill](docs/catalog.md#ncu-report-skill) |
| [构建知识与优化经验](docs/resources.md#knowledge) | [KernelWiki](docs/catalog.md#kernelwiki), [Apple Neural Engine Field Guide](docs/catalog.md#ane-field-guide) |
| [通用引擎参照](docs/resources.md#engine-baselines) | [vLLM](docs/catalog.md#vllm), [SGLang](docs/catalog.md#sglang), [TensorRT-LLM](docs/catalog.md#tensorrt-llm), [llama.cpp](docs/catalog.md#llama-cpp) |
| [编译器与内核语言](docs/resources.md#compilers) | [Apache TVM](docs/catalog.md#tvm), [NVIDIA TensorRT](docs/catalog.md#tensorrt), [Triton](docs/catalog.md#triton), [TileLang](docs/catalog.md#tilelang) |
| [可复用执行组件与模型准备](docs/resources.md#components) | [DeepCompressor](docs/catalog.md#deepcompressor), [QTIP](docs/catalog.md#qtip), [Marlin](docs/catalog.md#marlin), [Flash Linear Attention](docs/catalog.md#flash-linear-attention) |

[Atrex GPU Wiki：优化轨迹 → 可复用经验](docs/resources.md#embedded-knowledge)。配套资源必须说明服务于哪个构建、验证或比较过程。

当前目录：121 个项目、63 个构建案例。按[项目角色](docs/systems.md)、[执行机制](docs/catalog.md)或[模型领域](docs/domains.md)继续查找。

<!-- CATALOG-END -->

## 沿着构建过程读案例

**为什么另做执行路径 → 掌握了什么 → 复用与取舍 → 如何构建 → 如何验证和维护。**

例如，[MetaInfer → VibeQwen](docs/cases.md#vibeqwen)将构建工作流与作者报告的引擎产物连在一起；[Sol-Engine](docs/cases.md#sol-engine)连接视频模型专用优化和质量检查。生成一个内核、组合一个模型前向程序、交付完整推理服务，是不同范围的产出，案例需要分别说明。

[案例分析](docs/cases.md)和[构建方式对照](docs/comparison.md)沿着这条主线展开。[模型领域](docs/domains.md)和[执行机制](docs/catalog.md)是可重叠的二级检索维度。

## 什么值得收录？

每条记录都需要说明与**专用执行栈的构建或验证之间的直接联系**。收录对象包括实质性的原生引擎与专用后端、构建流程、相关验证方法、评测基准，以及在这一过程中有明确用途的配套资源。

通用引擎、编译器和内核库需要有具体的复用或对照关系。泛化的推理优化、简单封装、面向教学的 nano 实现，不能仅凭与推理有关就被收录。详见[分类与纳入标准](docs/taxonomy.md)。

## 证据与开放问题

本仓库核查公开来源，没有独立复现项目性能。作者报告与源码检查分别标注；运行时收益与量化、近似或模型改变分别讨论。AI 参与需要直接披露或可检查的工作流；未披露应记为未知。详见[证据规范](docs/evidence-policy.md)及[本轮资源核查](docs/resources-audit-2026-10-12.md)。

[研究议程](docs/research-agenda.md)进一步追问：构建节省能否覆盖验证、集成和维护成本？模型、硬件或负载变化后需要重做什么？未知成本与覆盖缺口应始终可见。

[项目数据](catalog/projects.csv)和[案例数据](catalog/cases.json)生成目录与对照页面，维护方式见[贡献规范](CONTRIBUTING.md)。元数据、原创图示、评论与脚本采用 [MIT License](LICENSE)；链接项目及模型遵循各自许可。
