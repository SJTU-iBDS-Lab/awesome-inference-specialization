# Reading list and case studies

This list is intentionally selective and **not** an exhaustive survey. Entries are included because they help distinguish inference optimization, domain-specific execution, and automatic construction.

## Inference-system surveys and baselines

- [xDiT: an Inference Engine for Diffusion Transformers with Massive Parallelism](https://arxiv.org/abs/2411.01738) — a DiT-domain system, not merely an LLM runtime port.

## Engine generation, testing, and evidence

- [SEIS: Self-Evolving Inference Systems](https://arxiv.org/abs/2610.04646) — sustained whole-engine optimization through inherited code and reports; [case and artifact boundaries](cases.md#seis), [public scaffold](https://github.com/smth-fun/self-evolving-inference-system).
- [MetaInfer paper](https://arxiv.org/abs/2607.12875) and [implementation](https://github.com/MetaInfer/MetaInfer) — explicit inference engine generation objective.
- [Baseten's VibeQwen case study](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/) — reported agent-built targeted runtime; treat reported speedups as author claims.
- [Sol-Engine agent workflow](https://nvlabs.github.io/Sana/Sol-Engine/docs/agent-workflow/) — agent-guided video inference optimization and quality gates.
- [FastKernels: Benchmarking GPU Kernel Generation in Production](https://arxiv.org/abs/2605.23215) — why isolated kernel gains may fail to survive end-to-end integration.

## Specialization beyond autoregressive LLMs

- [Inferix: A Block-Diffusion based Next-Generation Inference Engine for World Simulation](https://arxiv.org/abs/2511.20714) — block-level video execution semantics.
- [Nunchaku / SVDQuant](https://github.com/nunchux-ai/nunchaku) — precision-algorithm co-design changes fusion boundaries.
- [Iris](https://github.com/antirez/iris.c) — an independently implemented image synthesis pipeline.
- [DwarfStar's software-delivery rationale](https://github.com/antirez/ds4) — a project that directly discusses AI-modifiable, intentionally narrow runtimes.

## Important counterexamples

- General-purpose engines continue to have strong value through [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), and [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM).
- [KTransformers](https://github.com/kvcache-ai/ktransformers) suggests that specialized execution can coexist with a shared serving runtime.
- [Mirage](https://github.com/mirage-project/mirage) suggests that compiler-generated execution is another path to specialization without hand-maintained per-model engines.

**Interpretation note:** More specialized projects on GitHub alone do not establish a causal trend attributable to AI coding, a decrease in demand for general runtimes, or superior lifecycle economics. Those require longitudinal and controlled measurements.
