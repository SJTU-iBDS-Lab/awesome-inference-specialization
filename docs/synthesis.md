# Cross-case synthesis / 跨案例综合

[Home](../README.md) · [中文首页](../README_CN.md) · [Full case records / 完整案例](cases.md) · [Project records / 项目记录](catalog.md)

What do the selected cases show about obtaining control over inference execution? These five patterns synthesize the source reviews recorded on **2026-10-12** in [cases.json](../catalog/cases.json) and [projects.csv](../catalog/projects.csv). They connect examples across construction routes and model domains; they are not a new benchmark or a ranking.

精选案例如何说明推理执行控制权的获得方式？以下五个模式综合了 **2026-10-12** 的已有源码审查记录，连接不同构建路线与模型领域；本页不提供新基准测试或排名。每个案例链接均通向完整记录及其上游证据。

## 1. Execution ownership can coexist with substantial reuse / 控制执行并不排斥大量复用

- [Splash](cases.md#splash) owns target/draft execution, scheduling and state in C++/Metal while retaining checkpoints, tokenizers and attributed llama.cpp-derived material. [Gufo](cases.md#gufo) similarly owns per-model execution and local serving on Strix Halo while using ROCm/HIP, BLAS and adapted upstream components.
- [llamAmpere](cases.md#llamampere) reaches a different boundary: it retains llama.cpp server and GGML/GGUF infrastructure while changing speculative verification, compressed KV state and Ampere kernels. Its fork is a substantive construction route, not evidence of a from-scratch runtime.

These cases make “which decisions are controlled?” more informative than “how much was rewritten?” Native runtime, deep fork and specialized backend are different ways to obtain that control, with different inherited responsibilities.

- [Splash](cases.md#splash) 在 C++/Metal 中控制目标模型与草稿模型执行、调度及状态，同时复用权重、分词器和注明来源的 llama.cpp 组件。[Gufo](cases.md#gufo) 围绕 Strix Halo 控制逐模型执行及本地服务，同时使用 ROCm/HIP、BLAS 和改造的上游代码。
- [llamAmpere](cases.md#llamampere) 保留 llama.cpp 服务与 GGML/GGUF 基础设施，改造推测验证、压缩 KV 状态及 Ampere 内核。深度分叉本身就是一种构建路线，不能据此称为从零实现。

因此，阅读重点是“具体掌握哪些执行决策”。原生运行时、深度分叉与专用后端各有控制边界，也各自继承依赖与维护责任。

## 2. Memory and representation choices shape the integrated path / 内存与表示选择塑造完整执行路径

- [Flash-MoE](cases.md#flash-moe) coordinates SSD expert reads and Metal execution for a fixed model. [LightX2V](cases.md#lightx2v) controls weight-storage contracts, prefetch streams and two-slot device buffers inside a shared tensor framework. Both expose placement and movement as runtime decisions.
- [Nunchaku](cases.md#nunchaku) couples SVDQuant checkpoints with low-bit/low-rank fused execution to address extra activation traffic. Its checkpoint format, kernels and Python model adapters form a connected specialization boundary.

Trace storage → movement → computation before interpreting a speed claim. Flash-MoE's executable also reduces active experts from the model's ten to four; that is an approximation distinct from SSD streaming. LightX2V's offload likewise needs separate attribution from quantization, caching or changed model components.

- [Flash-MoE](cases.md#flash-moe) 为固定模型协调 SSD 专家读取与 Metal 执行；[LightX2V](cases.md#lightx2v) 在共享张量框架内控制权重存储契约、预取流及双槽设备缓冲。二者都把驻留与搬运落实为运行时决策。
- [Nunchaku](cases.md#nunchaku) 将 SVDQuant 权重与低比特、低秩融合执行结合，处理修正分支带来的额外激活读写。权重格式、内核和 Python 模型适配层共同构成专用路径。

解读速度之前，应先追踪“存储 → 搬运 → 计算”。Flash-MoE 还把模型的十个活跃专家减为四个，这是独立于 SSD 流式读取的近似；LightX2V 的卸载也须与量化、缓存和模型组件变化分别归因。

## 3. Construction automation and engine behavior are separate evidence / 构建自动化与引擎行为需要分别取证

- [MetaInfer → VibeQwen](cases.md#vibeqwen) links an adapted agent workflow to an author-reported serving artifact that reused existing kernels. The public workflow is not the VibeQwen engine source. [Sol-Engine](cases.md#sol-engine) exposes agent-guided configuration exploration and integration alongside inspectable video runtime code.
- [Mirage MPK](cases.md#mirage) instead compiles an explicitly assembled graph and worker configuration into persistent GPU execution. Compiler automation does not establish coding-agent participation. [Aria](cases.md#aria) discloses LLM-assisted development with human-led ideas, testing and debugging; [Splash](cases.md#splash) specifically discloses agent-created kernels.

Keep three questions separate: what construction process is visible, what artifact it produces, and what the artifact controls. An authorship disclosure, a generation workflow and a runtime mechanism answer different questions.

- [MetaInfer → VibeQwen](cases.md#vibeqwen) 将改造的智能体流程与作者报告的服务产物联系起来，后者复用了现有内核；公开流程不等于 VibeQwen 引擎源码。[Sol-Engine](cases.md#sol-engine) 同时提供智能体引导的配置探索、集成流程和可检查的视频运行时代码。
- [Mirage MPK](cases.md#mirage) 将显式组装的图与工作线程配置编译为持久 GPU 执行；编译自动化本身不能证明编码智能体参与。[Aria](cases.md#aria) 披露了人主导构思、测试和调试的 LLM 辅助开发；[Splash](cases.md#splash) 则具体披露了智能体生成内核。

应分别回答：看到了什么构建过程、产生什么产物、产物控制什么执行决策。作者披露、生成流程与运行时机制不能互相替代。

## 4. The changed behavior determines the validation contract / 改变了什么，就需要验证什么

- [Aria](cases.md#aria) uses reference tensors, controlled conditioning/noise and latent/audio comparisons for selected paths. [Sol-Engine](cases.md#sol-engine) uses perceptual checks and visual review while admitting cache, sparsity and precision changes. These checks address different acceptance contracts.
- [Vidax](cases.md#vidax) records precision-handling failures and fixes during JAX/TPU porting, showing why similar-looking mathematics still needs numerical checks. [vla.simd](cases.md#vla-simd) has fixed-input numerical checks, but action throughput does not establish closed-loop robot behavior.

Ask what the reference is, which configuration actually ran, and which failures the check can detect. Kernel numerics, composed state, generated-output quality and service behavior require distinct evidence; see the [validation guide](validation.md).

- [Aria](cases.md#aria) 用参考张量、受控条件与噪声、潜变量及音频比较检查特定路径。[Sol-Engine](cases.md#sol-engine) 在允许缓存、稀疏和精度变化的前提下进行感知指标与视觉检查。两者采用的验收契约不同。
- [Vidax](cases.md#vidax) 记录了 JAX/TPU 移植中的精度问题及修复，说明表面相似的数学仍需数值核对。[vla.simd](cases.md#vla-simd) 提供固定输入的数值检查，但动作吞吐不能证明闭环机器人表现。

应追问参考实现是什么、实际运行哪个配置、检查能发现哪些失败。内核数值、组合状态、生成质量和服务行为分别需要证据，详见[验证指南](validation.md)。

## 5. A specialization boundary also defines requalification work / 专用化边界也界定了重新验证的工作

- [llamAmpere](cases.md#llamampere) documents upstream merges and cache-restoration/build regressions, plus an unresolved parallel-8 failure. [Gufo](cases.md#gufo) keeps model-specific quality records and separates hosted CPU/repository CI from GPU qualification.
- [LightX2V](cases.md#lightx2v) explicitly rejects some combinations in its contiguous-offload path. [Mirage MPK](cases.md#mirage) requires supported tasks and graph assembly for new models; [Vidax](cases.md#vidax) requires checkpoint translation and device-mesh qualification.

These records make evolution concrete: a new model, state format, backend combination or device is a reason to revisit particular assumptions. A useful comparison should preserve those boundaries rather than treating one passing configuration as permanent coverage.

- [llamAmpere](cases.md#llamampere) 记录了上游合并、缓存恢复及构建回归，还保留未解决的 parallel-8 失败。[Gufo](cases.md#gufo) 按模型维护质量记录，并区分托管 CPU/仓库 CI 与 GPU 验证。
- [LightX2V](cases.md#lightx2v) 的连续卸载路径明确拒绝部分配置组合。[Mirage MPK](cases.md#mirage) 为新模型要求受支持的任务实现与图组装；[Vidax](cases.md#vidax) 需要权重转换及设备网格验证。

这些记录把演进工作具体化：模型、状态格式、后端组合或设备变化，都可能使原先假设失效。比较时应保留这些边界，不能把单个通过的配置当作永久覆盖。

## Limits and deeper reading / 边界与深入阅读

This is a synthesis of recorded source evidence, not independent execution or a causal study. Selected successes do not establish prevalence, production readiness or AI-driven savings. Reported prototype time, token use and device-hours are partial observations; comparable lifecycle accounting and counterfactuals are still needed. Missing evidence remains unknown.

本页综合已有源码证据，没有新增独立运行或因果实验。精选成功案例不能证明普遍程度、生产就绪或 AI 带来的节省。原型时间、token 用量与设备时数只是局部观察；仍需可比的全生命周期核算及反事实。缺失证据保留为未知。

- [Evidence policy / 证据规则](evidence-policy.md): claim strength, comparison conditions and source-access boundaries.
- [Research agenda / 研究议程](research-agenda.md): construction alternatives, causal questions and lifecycle accounting.
- [Taxonomy / 分类框架](taxonomy.md): execution ownership, artifact roles and semantic effects.
- [Validation / 验证方法](validation.md): references, acceptance rules, coverage and checking cost.
