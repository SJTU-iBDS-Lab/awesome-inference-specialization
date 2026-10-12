# Benchmarks and task suites / 评测基准与任务集

> Generated from [projects.csv](../catalog/projects.csv) and [schema.json](../catalog/schema.json).

[Home](../README.md) · [中文首页](../README_CN.md) · [Validation methods](validation.md) · [Construction workflows](systems.md#construction)

A benchmark defines tasks, executable references, inputs and a comparison protocol. A validation method checks a contract; one benchmark may incorporate several methods. Keep these roles distinct even when both live in the same project.

评测基准规定任务、参考程序、输入和比较协议；验证方案判断某项契约是否满足。包含数值检查的基准仍按主要用途列在这里，不重复计数。

<a id="fastkernels"></a>

## FastKernels

**Scope / 范围:** Kernel → fused operation → block → end-to-end model pipeline / 内核 → 融合算子 → 模块 → 端到端模型流水线

**Question / 比较问题:** Do candidate-kernel gains survive model integration? / 候选内核的收益能否在模型集成后保留？

Replaces candidate operators in production-shaped model pipelines and evaluates both kernel-level numerics/timing and end-to-end token outputs, throughput and latency.

**Limits / 边界:** FastKernels also exposes a minimal serving path, but its primary distinction here is integrated evaluation; kernel-level tolerance checks and exact greedy-token tests cover different contracts.

[Project record and inspected sources / 项目记录与已核来源](catalog.md#fastkernels) · [Upstream / 上游](https://github.com/Snowflake-AI-Research/fastkernels)

<a id="atrex-bench"></a>

## Atrex-Bench

**Scope / 范围:** Production-trace operator generation / 生产执行轨迹中的算子生成

**Question / 比较问题:** Does a generated operator compile, meet numerical checks and use the target hardware effectively? / 生成算子能否编译、通过数值检查并有效利用目标硬件？

Packages reference programs and input/shape generators, separates agent-visible tasks from evaluator metadata, and checks compilation, numerical outputs/input mutations and forward timing against a roofline estimate.

**Limits / 边界:** End-to-end refers to operator generation and evaluation, not a complete serving stack; correctness uses finite inputs and tolerances, and roofline efficiency is not an application-level speedup.

[Project record and inspected sources / 项目记录与已核来源](catalog.md#atrex-bench) · [Upstream / 上游](https://github.com/alibaba/atrex-bench)

<a id="kernelbench"></a>

## KernelBench

**Scope / 范围:** Operator, fusion and model-program generation tasks / 算子、融合与模型程序生成任务

**Question / 比较问题:** How do generated implementations compare with executable references under a stated evaluation protocol? / 在指定评测协议下，生成实现与可执行参考程序相比如何？

Compiles generated kernel implementations, compares them against PyTorch reference programs on randomized inputs and times only candidates that pass correctness checks.

**Limits / 边界:** This is an evaluation environment, not an inference runtime; finite task-level success or speedup does not establish deployment-level gains.

[Project record and inspected sources / 项目记录与已核来源](catalog.md#kernelbench) · [Upstream / 上游](https://github.com/ScalingIntelligence/KernelBench)

## What a complete-engine comparison still needs / 完整引擎还需要比较什么

Record the model/checkpoint, device, precision, input distribution, state/cache conditions, concurrency, software revisions and quality criterion. Measure end-to-end latency/throughput and memory under the same workload; disclose fallback and unsupported cases.

The listed suites do not by themselves establish the cost or reliability of constructing an entire engine. Construction comparisons also need human effort, agent/tool/GPU budgets, failed attempts, validation and integration effort, plus adaptation and maintenance over a stated horizon.

上述基准不能单独证明整个引擎的构建成本或可靠性。构建方式的比较还须记录人工投入、Agent／工具／GPU 预算、失败尝试、验证集成成本与后续维护。

