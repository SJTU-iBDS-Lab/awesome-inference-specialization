# Device constraints × execution mechanisms / 设备约束 × 执行机制

[Home](../README.md) · [中文首页](../README_CN.md) · [Scope and roles](taxonomy.md) · [Evidence policy](evidence-policy.md) · [中文表格](#chinese)

This is a **cross-cutting reading index**, not a new “mobile frameworks” category, star ranking or additional project inventory. The canonical catalog remains organized by delivered artifact and model domain. A phone is a *device/workload constraint*: the research question is which execution decision changes under its memory, compute and power limits. The links below distinguish **already admitted catalog records** from **official-source routes under review**. The latter are not yet counted, described as independently reproduced, or promoted to core.

## Mechanism crosswalk (English)

| Mobile constraint | Execution-level specialization to inspect | Existing catalog examples (retain their roles) | Official-source comparison routes, **not yet cataloged** | Evidence still required |
| --- | --- | --- | --- | --- |
| ARM CPU ISA, small RAM and variable core topology | Packing / quantized matrix kernels, ISA dispatch, low-memory native runtime | [Cactus](catalog.md#cactus) · [BitNet.cpp](catalog.md#bitnet-cpp) · [llama.cpp](catalog.md#llama-cpp) | [MNN's CPU/C4 execution](#mnn-source-boundary) | Compare on the same handset with identical checkpoints, thread/core affinity, quantization and sustained thermal state |
| Apple ANE versus Metal/CPU | Model partitioning and Core ML compilation, prefill variants, persistent KV versus CPU/GPU fallback | [ANEMLL](catalog.md#anemll) · [CoreML LLM CLI](catalog.md#coreml-llm-cli) · [ane.cpp](catalog.md#ane-cpp) | [ExecuTorch Core ML delegation](#executorch-and-litert-lm-comparators) as a comparison, not an admitted record | Core ML's actual placement, iOS compatibility and model/OS limits; ANE experiments on macOS alone do not prove deployable iPhone execution |
| Snapdragon Hexagon NPU / Qualcomm QNN | AOT graph lowering, quantization contracts, NPU op execution, CPU fallback and SDK dependence | [MLC LLM](catalog.md#mlc-llm) is a mobile compilation precedent, **not** an established QNN/NPU implementation in this catalog | [mllm QNN AOT](#mllm-source-boundary) · [MNN Hexagon](#mnn-source-boundary) · [ExecuTorch QNN](#executorch-and-litert-lm-comparators) | Supported SoC/firmware, runnable graph coverage, proprietary SDK/runtime boundary and CPU/NPU transition costs |
| Mobile GPU and prefill/decode asymmetry | Device-specific Metal/OpenCL/Vulkan kernels, graph fusion, fused low-bit dequantization and phase-specific scheduling | [MLC LLM](catalog.md#mlc-llm) · [Cactus](catalog.md#cactus) · [Draw Things](catalog.md#draw-things) | [MNN's packed C4 and fused operators](#mnn-source-boundary) · [LiteRT-LM orchestration](#executorch-and-litert-lm-comparators) | Separate prefill and decode; distinguish kernel gains, graph export, quantization and GPU occupancy |
| KV residency, context growth and mobile memory pressure | Cache format/layout and page allocation, attention state, load-time budgets | [Cactus](catalog.md#cactus) · [ANEMLL](catalog.md#anemll) · [MLC LLM](catalog.md#mlc-llm) | [MNN Hexagon attention/KV](#mnn-source-boundary) · [LiteRT-LM NPU context execution](#executorch-and-litert-lm-comparators) | Peak RSS, retained KV, context length, reloads, correctness after reset and cross-turn reuse |
| On-device vision/audio + language | Model-specific modality processing and execution orchestration rather than a thin UI/JNI wrapper | [Cactus](catalog.md#cactus) · [Draw Things](catalog.md#draw-things) | [mllm multimodal backend](#mllm-source-boundary) · [LiteRT-LM](#executorch-and-litert-lm-comparators) | End-to-end model variants, transfer/buffering overhead, per-modality quality and OS-memory behavior |

## Official sources and limits

### MNN source boundary

The official [MNN LLM deployment guide](https://github.com/alibaba/MNN/blob/5c22b9f082275dce1cdf82c8a1a0b2a4a1c2976d/docs/transformers/llm.md) describes model conversion and Android Hexagon requirements; the inspected [Hexagon attention implementation](https://github.com/alibaba/MNN/blob/5c22b9f082275dce1cdf82c8a1a0b2a4a1c2976d/source/backend/hexagon/execution/HexagonAttention.cpp) includes fixed workspace/shape constraints and KV pagination. The LLM Hexagon guide requires **symmetric 4-bit weights and Transformer C4 export** for the documented path. The [MNN 3.6.1 author's benchmarks](https://github.com/alibaba/MNN/releases/tag/3.6.1) report, for Qwen3-0.6B W4 on Snapdragon 8 Elite, **NPU prefill 2,667 versus CPU 336 tok/s** but **NPU decode 68.5 versus CPU 94.3 tok/s**. These numbers are *release- and configuration-specific author reports*, not our measurements or a general NPU speed ranking. MNN is a substantive integrated engine; whether it merits a new catalog case requires the normal construction/evidence review, not an automatic promotion of the whole framework.

### mllm source boundary

The canonical research-team repository is [UbiquitousLearning/mllm](https://github.com/UbiquitousLearning/mllm), not the different `acproject/mllm` repository. Its [QNN AOT workflow](https://github.com/UbiquitousLearning/mllm/blob/1d3c3d8e506e3d12e902af82866972623b240ce0/docs/qnn_backend/aot_execute.rst) specifies host-side quantization/export, QNN context compilation, and native on-device execution with **W4A16 weights and uint8 KV**; the [QNN backend implementation](https://github.com/UbiquitousLearning/mllm/blob/1d3c3d8e506e3d12e902af82866972623b240ce0/mllm/backends/qnn/QNNBackend.cpp) provides inspectable operator/backend construction. The official [README](https://github.com/UbiquitousLearning/mllm/blob/1d3c3d8e506e3d12e902af82866972623b240ce0/README.md) also distinguishes newer v2, phone ARM paths and separate Jetson/Ascend additions. QNN toolchain availability, actual NPU coverage, quantization effects and performance remain target-specific; code inspection is not a handset reproduction.

### ExecuTorch and LiteRT-LM comparators

The official [ExecuTorch backend map](https://github.com/pytorch/executorch/blob/24a61164689d5e84a1dcda0e3f619ab629ddd392/docs/source/backends-overview.md) documents target-specific exported programs and CPU fallback; its [Qualcomm partitioner](https://github.com/pytorch/executorch/blob/24a61164689d5e84a1dcda0e3f619ab629ddd392/backends/qualcomm/partition/qnn_partitioner.py) illustrates the supported-subgraph boundary, rather than proving complete NPU execution. [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM/blob/25016d6ef6496d35cec27167a862e5e1f1fdd79c/README.md) is a cross-platform model-execution orchestration route with a [LiteRT executor implementation](https://github.com/google-ai-edge/LiteRT-LM/blob/25016d6ef6496d35cec27167a862e5e1f1fdd79c/runtime/executor/llm_litert_compiled_model_executor.cc); advertised GPU/NPU optimizations are not a blanket claim about all SoCs or checkpoints. These broad frameworks are useful here as **construction/delegation comparisons**, not additional mobile-specific core projects by default.

[PowerInfer-2](https://arxiv.org/abs/2406.06282) motivates neuron-cluster-level CPU/NPU execution and fine-grained I/O overlap on phones, but **this review did not establish an official public implementation**: its paper is a reading lead, not a verified new engine entry. Likewise, no evidence above establishes sustained thermal behavior, tokens/joule, quality parity or independently reproduced performance.

<a id="chinese"></a>

## 中文：设备约束与执行机制横向对照

本表不新增“手机端框架”一级分类，不改变语言／图像／视频／音频／多模态的领域组织，也不按 Star 排名。项目依然按原有产物与执行机制入库；手机端仅作为**硬件与负载约束**横向检索。已入库条目与待审查的官方实现严格区分，后者暂不计入目录数量。

| 端侧约束 | 真正应检查的执行决策 | 已收录的目录入口（保留原分类） | 官方源码候选／对照，**尚未入库** | 必须核实的边界 |
| --- | --- | --- | --- | --- |
| ARM CPU 指令集、有限内存和大小核 | 低比特核、指令集分派、轻量原生运行时 | [Cactus](catalog.md#cactus) · [BitNet.cpp](catalog.md#bitnet-cpp) · [llama.cpp](catalog.md#llama-cpp) | [MNN CPU/C4 路线](#mnn-source-boundary) | 同手机、同模型与量化下比较线程、核绑定及热稳定性 |
| Apple ANE 与 Metal/CPU | Core ML 编译和图切分、预填充变体、KV 状态及回退 | [ANEMLL](catalog.md#anemll) · [CoreML LLM CLI](catalog.md#coreml-llm-cli) · [ane.cpp](catalog.md#ane-cpp) | [ExecuTorch Core ML 委托](#executorch-and-litert-lm-comparators) | 实际算子落点、iOS 和系统版本；macOS ANE 实验不自动证明可在 iPhone 部署 |
| Snapdragon Hexagon / QNN | AOT 子图编译、定点量化约束、NPU 执行与 CPU 回退 | [MLC LLM](catalog.md#mlc-llm) 只作为移动端编译路线对照，**并非已核实的 QNN 实现** | [mllm QNN AOT](#mllm-source-boundary) · [MNN Hexagon](#mnn-source-boundary) · [ExecuTorch QNN](#executorch-and-litert-lm-comparators) | SoC 与 SDK 支持、完整子图覆盖、私有运行库依赖、CPU/NPU 数据搬移 |
| 手机 GPU 与 prefill/decode 差异 | Metal/OpenCL/Vulkan 专用内核、算子融合、低比特反量化融合、分阶段调度 | [MLC LLM](catalog.md#mlc-llm) · [Cactus](catalog.md#cactus) · [Draw Things](catalog.md#draw-things) | [MNN C4 融合算子](#mnn-source-boundary) · [LiteRT-LM](#executorch-and-litert-lm-comparators) | 预填充与解码单独比较，不混淆量化、图导出与实现改动 |
| KV 常驻、长上下文和内存峰值 | KV 格式与页管理、注意力状态、模型加载预算 | [Cactus](catalog.md#cactus) · [ANEMLL](catalog.md#anemll) · [MLC LLM](catalog.md#mlc-llm) | [MNN Hexagon KV](#mnn-source-boundary) · [LiteRT-LM](#executorch-and-litert-lm-comparators) | RSS 峰值、缓存常驻、上下文扩展、会话重置与复用正确性 |
| 视觉／音频／文本本地协同 | 模态组件执行与缓存调度，而不是仅实现 UI/JNI 包装 | [Cactus](catalog.md#cactus) · [Draw Things](catalog.md#draw-things) | [mllm 多模态执行](#mllm-source-boundary) · [LiteRT-LM](#executorch-and-litert-lm-comparators) | 模型子类型、端到端搬移、模态质量与移动系统内存限制 |

**可用于 Survey 的问题。** 移动端优化可能在 prefill 与 decode 之间出现设备最优路径反转；异构 NPU 编译的算子覆盖及闭源 SDK 会影响可维护性；短时 tok/s、持续温升与 tokens/J 之间的关系仍缺少匹配配置的验证。应把这些问题纳入对照设计，而不是把“上 NPU”或“面向移动端”当作性能与成熟度的充分证据。

**证据边界。** 本页是固定到上述源码版本的文档／调用路径审查，不是本维护者的手机测试。MNN、mllm 是值得继续做完整入库审查的实现候选；ExecuTorch、LiteRT-LM 为构建和后端对照；PowerInfer-2 暂仅作为论文线索。正式新增项目仍须更新 canonical catalog、双语简述、必要案例及生成视图，并经过全套测试。
