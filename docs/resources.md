# Companion resources / 配套资源

> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).

[Home](../README.md) · [中文首页](../README_CN.md) · [Construction](systems.md#construction) · [Validation](validation.md) · [Benchmarks](benchmarks.md)

Resources belong here through a concrete connection to building, checking or comparing an included execution stack. This is a selected dependency and knowledge map, not a general GPU-tool directory.

只收录与执行栈构建、验证或比较有具体联系的资源。性能诊断和构建知识服务于构建流程，通用组件须写明复用关系。

<a id="diagnostics"></a>

## Performance diagnosis / 性能诊断

Turn measured hardware behavior into actionable optimization feedback; not a correctness certificate.

把硬件测量转成可执行的优化反馈；诊断本身不证明正确性。

| Resource | Concrete role in this collection |
| --- | --- |
| [ncu-report-skill](catalog.md#ncu-report-skill) | Diagnostic companion for connecting measured kernel bottlenecks to an agent-guided optimization decision. |

<a id="knowledge"></a>

## Construction knowledge and experience / 构建知识与优化经验

Traceable optimization knowledge and hardware experiments that can inform another construction attempt.

有来源的优化知识与硬件实验，用于后续构建复用。

| Resource | Concrete role in this collection |
| --- | --- |
| [KernelWiki](catalog.md#kernelwiki) | Retrievable hardware and kernel experience connects prior engineering work with subsequent specialized implementation decisions. |
| [Apple Neural Engine Field Guide](catalog.md#ane-field-guide) | Concrete hardware-investigation knowledge and accepted/rejected experiments feed the separately cataloged ane.cpp engine. |

<a id="engine-baselines"></a>

## General-engine baselines / 通用引擎参照

Shared services, fork origins and comparison points for included specialized stacks.

收录执行栈的共享服务、分叉来源与比较对象。

| Resource | Concrete role in this collection |
| --- | --- |
| [vLLM](catalog.md#vllm) | General-engine reference for the VibeQwen construction case and upstream serving infrastructure retained by the Radiance specialized backend. |
| [SGLang](catalog.md#sglang) | Shared serving infrastructure used alongside KTransformers and model components reused by Sol-Engine; separates specialized execution from shared services. |
| [TensorRT-LLM](catalog.md#tensorrt-llm) | General-engine comparison point in the VibeQwen case; record matching model, hardware, precision and workload before comparing the specialized result. |
| [llama.cpp](catalog.md#llama-cpp) | Upstream execution stack for the llamAmpere, CIRU, Strix and ANEMLL Flash forks; makes inherited code and changed execution paths comparable. |

<a id="compilers"></a>

## Compilers and kernel languages / 编译器与内核语言

Compilation dependencies and output languages of included construction workflows.

收录构建流程实际使用的编译依赖与输出语言。

| Resource | Concrete role in this collection |
| --- | --- |
| [Apache TVM](catalog.md#tvm) | Compiler infrastructure underlying the included MLC LLM model-to-runtime construction route. |
| [NVIDIA TensorRT](catalog.md#tensorrt) | Model-compilation and execution foundation for the included TensorRT Edge-LLM deployment route. |
| [Triton](catalog.md#triton) | Kernel language emitted or optimized by KernelAgent and Atrex Kernel Agent, linking generated programs to their compilation and validation boundary. |
| [TileLang](catalog.md#tilelang) | Kernel language supported by the included Atrex Kernel Agent campaigns; a generated kernel remains distinct from a complete model runtime. |

<a id="components"></a>

## Reusable execution and model preparation / 可复用执行组件与模型准备

Selected dependencies used in the engine cases; model preparation remains distinct from runtime execution.

引擎案例中使用的精选依赖；模型准备与运行时执行分开记录。

| Resource | Concrete role in this collection |
| --- | --- |
| [DeepCompressor](catalog.md#deepcompressor) | Model preparation used for the Nunchaku/SVDQuant execution path; calibration and exported weights must be distinguished from runtime gains. |
| [QTIP](catalog.md#qtip) | Trellis quantization and matching execution provide a representation-design reference credited in the ExLlamaV3 case, rather than a second complete engine. |
| [Marlin](catalog.md#marlin) | Quantized linear-kernel and packing reference used in the ExLlamaV3 construction account; separates reusable low-level work from engine ownership. |
| [Flash Linear Attention](catalog.md#flash-linear-attention) | Reusable recurrent and linear-attention kernels in the ExLlamaV3 execution stack; state semantics must survive integration. |
| [FlashAttention](catalog.md#flash-attention) | Attention implementation reused by included model runtimes such as ExLlamaV3; an optimized component does not establish an end-to-end gain. |
| [SageAttention](catalog.md#sageattention) | Low-precision attention component integrated into the included FastVideo/video execution paths, with a separate quality-validation obligation. |
| [FlashInfer](catalog.md#flashinfer) | Optional standard paged-attention backend used by MoE-Infinity where supported; preserves the distinction between reusable kernels and the reconstructed engine. |

<a id="embedded-knowledge"></a>

## Knowledge inside a construction workflow / 构建流程中的知识模块

The [Atrex Kernel Agent](catalog.md#atrex-kernel-agent) includes [GPU Wiki](https://github.com/alibaba/atrex-kernel-agent/blob/main/gpu-wiki/README.md): optimization traces and agent sessions feed candidate knowledge, provenance/scope checks gate admission, and later optimization episodes retrieve it. It remains part of the parent project rather than a second repository record.

Atrex 的 GPU Wiki 把优化轨迹和 Agent 会话转成候选知识，检查来源与适用范围后再供后续优化检索；它属于构建框架内部模块，不单独增加仓库数量。公开工作流不等于已经证明总开发成本下降。

The [ANE field guide](catalog.md#ane-field-guide) links hardware experiments to [ane.cpp](catalog.md#ane-cpp). Read kept and discarded findings together and retain the tested hardware boundary.

