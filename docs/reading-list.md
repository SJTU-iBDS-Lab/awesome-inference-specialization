# Reading list and case studies

This list is intentionally selective and **not** an exhaustive survey. Entries are included because they help distinguish inference optimization, domain-specific execution, and automatic construction.

## Inference-system surveys and baselines

- [xDiT: an Inference Engine for Diffusion Transformers with Massive Parallelism](https://arxiv.org/abs/2411.01738) — a DiT-domain system, not merely an LLM runtime port.

## Engine generation, testing, and evidence

- [VibeServe paper](https://arxiv.org/abs/2605.06068) and [current VibeSys framework](https://github.com/uw-syfi/vibesys) — target-specific serving-stack construction; keep the paper and later implementation revisions separate. [Case](cases.md#vibeserve).
- [AutoMegaKernel](https://arxiv.org/abs/2606.09682) — model-level persistent execution generated through a restricted schedule IR and trusted VM; static checks are not a whole-stack proof. [Case](cases.md#automegakernel).
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

## Model-level generation: paper evidence

- [ForgeMegakernel](https://arxiv.org/html/2609.12379v1) — milestone-guided decode megakernel generation with reference KV/logit and functional checks, followed by SGLang integration. Reviewed as a paper; an official implementation was not established by this search. It is not currently counted as an independently verified software project. [Review and next check](source-review-2026-10-14.md).

## Industrial execution-stack design

- [Cloudflare Infire](cases.md#infire) — proprietary Rust execution tailored to deployment constraints; [initial design](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/) and [later multi-GPU development](https://blog.cloudflare.com/high-performance-llms/) provide separate stages of evidence.
- [Kog Inference Engine](cases.md#kie) — vendor-described persistent execution and model/device co-design. Read the [implementation discussion](https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/) with the [preview's model and eight-GPU conditions](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/), not as an unchanged-model generic speedup.

## Perspectives on construction and abstraction

- [Retire the Abstractions](https://hazyresearch.stanford.edu/blog/2026-08-05-retire-the-abstractions), Hazy Research, August 5, 2026 — a first-party account arguing that agents can replace some implementation scaffolding while references, tests and domain knowledge remain necessary. This is a perspective grounded in one team's experience, not causal evidence that general runtimes are obsolete.

## Important counterexamples

- General-purpose engines continue to have strong value through [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), and [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM).
- [KTransformers](https://github.com/kvcache-ai/ktransformers) suggests that specialized execution can coexist with a shared serving runtime.
- [Mirage](https://github.com/mirage-project/mirage) suggests that compiler-generated execution is another path to specialization without hand-maintained per-model engines.

**Interpretation note:** More specialized projects on GitHub alone do not establish a causal trend attributable to AI coding, a decrease in demand for general runtimes, or superior lifecycle economics. Those require longitudinal and controlled measurements.
