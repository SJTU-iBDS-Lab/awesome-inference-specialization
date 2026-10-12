# Awesome Inference Specialization

**From general-purpose frameworks to model-, hardware-, and workload-specialized inference systems.**

A curated, evidence-aware collection of **purpose-built inference runtimes**, **domain-specific execution systems**, and **tools that generate or optimize them**. Scope: LLMs, image generation, video generation, and adjacent compiler/runtime infrastructure.

[Catalog](#project-catalog) · [Selection criteria](#what-belongs-here) · [Taxonomy](docs/taxonomy.md) · [Research agenda](docs/research-agenda.md) · [Contributing](CONTRIBUTING.md) · [中文](README_CN.md)

> **Research hypothesis, not an established conclusion:** As code generation and adaptation become cheaper, more deployment-specific inference systems may be economically viable. The generality once embedded in a runtime may increasingly move to the **tools that construct, validate, and evolve runtimes**. Whether this improves *total* cost or performance is an open empirical question.

## Why another inference collection?

This is **not** a directory of every LLM serving framework, an optimization-paper bibliography, or a ranking by peak tokens/s. We focus on **where specialization changes execution design**:

- **Model-specific:** leverage a known MoE topology, attention pattern, generation algorithm, or precision format.
- **Hardware/memory-specific:** design around a particular GPU, CPU–GPU combination, SSD, or memory budget.
- **Workload-specific:** restructure prefill/decode, expert routing, block diffusion, streaming, concurrency, or communication.
- **Construction-time specialization:** agent-generated code, compiler-generated execution graphs, or deployment-specific kernel/runtime builds.

A project **does not need to be AI-written**, written from scratch, or limited to one model. Reusing ggml, PyTorch, Triton, FlashAttention, CUDA libraries, etc. is normal. What matters is an identifiable *execution-level design decision* tied to a constrained target.

## What belongs here?

**Core:** An implemented inference runtime or execution stack with substantive specialization, or a system that explicitly builds/optimizes such stacks. **Adjacent:** A specialized backend, compiler, deep runtime fork, or verification platform essential to understanding the phenomenon. **Watchlist:** Interesting but rapidly evolving projects whose exact implementation boundary needs follow-up.

We generally **exclude from the core catalog**:

- teaching/minimal replicas whose principal contribution is small code size;
- API wrappers or model downloaders without meaningful control of execution;
- single isolated kernels that do not define an execution subsystem;
- generic serving engines listed solely because they support many models;
- projects with only a performance headline and no inspectable design description.

See [taxonomy](docs/taxonomy.md), [evidence policy](docs/evidence-policy.md), and [contribution guide](CONTRIBUTING.md). Inclusion **does not imply** production readiness, benchmark superiority, strict model equivalence, open-source licensing, or verified AI authorship.

## Project catalog

These entries are drawn from [`catalog/projects.csv`](catalog/projects.csv). Use `python scripts/update_readme.py` after changing the catalog; `--check` verifies synchronization. `public code` means code is visible, **not** that every artifact is fully open-source or independently audited. `AI disclosed` means a project explicitly states AI-assisted development; `agent-native` means agents are part of the documented method. A missing disclosure is marked `AI use unverified`, not `human-only`.

<!-- CATALOG-START -->

### LLM execution runtimes

| Project | Target | Execution-level specialization | Source / AI | Limitations |
| --- | --- | --- | --- | --- |
| [DwarfStar](https://github.com/antirez/ds4) | Selected DeepSeek / GLM / Qwen models | Narrow native inference and serving paths; hardware-aware memory and KV handling | [public code](https://github.com/antirez/ds4#ai-full-disclosure) · AI disclosed | Authors explicitly disclose substantial AI coding assistance; not a generic GGUF runner. |
| [ExLlamaV3](https://github.com/turboderp-org/exllamav3) | Quantized LLMs on consumer GPUs | EXL3 quantization and dedicated inference, KV, batching, and offload paths | [public code](https://github.com/turboderp-org/exllamav3) · AI use unverified | A precision/hardware-specialized engine, not a single-model runtime. |
| [Flash-MoE](https://github.com/danveloper/flash-moe) | Large MoE on memory-limited Apple hardware | SSD-streamed experts and custom C/Metal execution pipeline | [public code](https://github.com/danveloper/flash-moe) · AI disclosed | Developer documents human–AI work; independently verify routing/model-equivalence claims. |
| [Halogen Flash](https://github.com/peonist-ai/halogen-flash-server) | Qwen MoE on AMD Strix Halo | One model family and one GPU target, with custom execution kernels | [closed core](https://github.com/peonist-ai/halogen-flash-server/blob/main/AGENTS.md) · AI use unverified | Public repository contains deployment/docs, not engine source code. |
| [Magnitude](https://github.com/magnitudedev/magnitude) | Local LLMs on user-owned hardware | Hardware profiling and on-device kernel compilation/tuning | [public code](https://github.com/magnitudedev/magnitude) · AI use unverified | Model coverage is not limited to a single family; optimization extent needs per-backend inspection. |
| [Strata](https://github.com/Niko1221/Strata) | Qwen MoE on consumer hardware | Specialized expert residency, CPU–GPU overlap, and model-specific decoding | [public code](https://github.com/Niko1221/Strata) · AI use unverified | Some modes change computation or output; benchmark equivalence must be checked. |

### Image and diffusion execution

| Project | Target | Execution-level specialization | Source / AI | Limitations |
| --- | --- | --- | --- | --- |
| [Draw Things Community](https://github.com/drawthingsai/draw-things-community) | Image generation application/server stack | Independent public implementation of model, sampler, and execution components | [public code](https://github.com/drawthingsai/draw-things-community) · AI use unverified | Broader application execution stack rather than a narrowly model-specific runtime. |
| [edge-dit.cpp](https://github.com/THU-MIG/edge-dit.cpp) | DiT image/video models on constrained devices | Native C/C++ DiT inference with VRAM-aware placement, precision, and offloading | [public code](https://github.com/THU-MIG/edge-dit.cpp) · AI use unverified | Reuses ggml and other third-party building blocks. |
| [Iris](https://github.com/antirez/iris.c) | FLUX.2 Klein and Z-Image families | Dependency-light C image-generation pipeline including text, denoising, and VAE execution | [public code](https://github.com/antirez/iris.c) · AI use unverified | Supports selected image models; do not generalize to all diffusion architectures. |
| [Nunchaku](https://github.com/nunchux-ai/nunchaku) | Low-bit diffusion models | Co-designed SVDQuant execution; fuses low-bit and low-rank paths | [public code](https://github.com/nunchux-ai/nunchaku) · AI use unverified | Quantized and BF16 models are not numerically identical; separate quality effects. |
| [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) | Native image/video generation | ggml-backed C/C++ execution outside the standard PyTorch pipeline | [public code](https://github.com/leejet/stable-diffusion.cpp) · AI use unverified | A domain-specific native runtime with relatively broad model coverage. |

### Video and diffusion-transformer execution

| Project | Target | Execution-level specialization | Source / AI | Limitations |
| --- | --- | --- | --- | --- |
| [FastVideo](https://github.com/hao-ai-lab/FastVideo) | Accelerated video generation | Video-serving paths alongside sparsity and post-training methods | [public code](https://github.com/hao-ai-lab/FastVideo) · AI use unverified | Joint model/post-training and runtime improvements should be measured separately. |
| [Inferix](https://github.com/alibaba-damo-academy/Inferix) | Block-diffusion/world simulation | Block-oriented generation state, KV handling, and VAE chunking/streaming | [public code](https://github.com/alibaba-damo-academy/Inferix) · AI use unverified | Distinct block-generation and VAE-chunk units; not a generic all-video serving engine. |
| [LightX2V](https://github.com/ModelTC/LightX2V) | Video/image generation model families | Domain runtime spanning caching, quantization, offload, and multi-GPU execution | [public code](https://github.com/ModelTC/LightX2V) · AI use unverified | Broad domain-specific framework; distinguish runtime gains from model changes. |
| [TurboDiffusion](https://github.com/thu-ml/TurboDiffusion) | Accelerated video diffusion | Combination of sparse attention, step distillation, and optimized execution | [public code](https://github.com/thu-ml/TurboDiffusion) · AI use unverified | Reported end-to-end gains combine model/algorithm and runtime effects. |
| [xDiT](https://github.com/xdit-project/xDiT) | Parallel DiT inference | DiT-specific multi-device execution, including parallelism and pipelining | [public code](https://github.com/xdit-project/xDiT) · AI use unverified | A compute-family-specific distributed runtime rather than a single-checkpoint engine. |

### Agent-driven generation and optimization

| Project | Target | Execution-level specialization | Source / AI | Limitations |
| --- | --- | --- | --- | --- |
| [MetaInfer](https://github.com/HuangPuStar/MetaInfer) | Generate purpose-built LLM inference servers | Agent-driven creation, testing, and optimization of model-specific engines | [public code](https://github.com/HuangPuStar/MetaInfer) · agent-native | A generator/toolbox, not itself a specific serving-engine implementation. |
| [Sol-Engine](https://nvlabs.github.io/Sana/Sol-Engine/docs/) | Agent-driven video inference optimization | Agent orchestration of kernel/cache/sparse techniques with quality gates | [documentation](https://nvlabs.github.io/Sana/Sol-Engine/docs/agent-workflow/) · agent-native | Official documentation; do not assume an independently released standalone engine repository. |

### Adjacent infrastructure and watchlist

| Project | Target | Execution-level specialization | Source / AI | Limitations |
| --- | --- | --- | --- | --- |
| [AgentCompile](https://github.com/veneno1213822/AgentCompile) **(Adjacent)** | LLM-guided inference compiler prototype | Bounded kernel selection and contract-checked LLM-generated fusion kernels | [review-only code](https://github.com/veneno1213822/AgentCompile) · agent-native | Anonymous research artifact; review-only licensing, not a production engine. |
| [cache-dit](https://github.com/vipshop/cache-dit) **(Adjacent)** | DiT execution acceleration in PyTorch | Caching, parallelism, quantization, and offload for DiT inference | [public code](https://github.com/vipshop/cache-dit) · AI use unverified | Retains PyTorch as its underlying environment. |
| [FastKernels](https://github.com/Snowflake-AI-Research/fastkernels) **(Adjacent)** | Agent-created/custom kernels in integrated inference | Correctness and performance benchmarking from operator to end-to-end pipeline | [public code](https://github.com/Snowflake-AI-Research/fastkernels) · AI use unverified | Benchmark infrastructure, included for verification rather than as a bespoke engine. |
| [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) **(Adjacent)** | Specialized quantization in a llama.cpp fork | Deep runtime fork emphasizing quantization and performance | [public code](https://github.com/ikawrakow/ik_llama.cpp) · AI use unverified | Evidence that modifying an existing framework may be preferable to a full rewrite. |
| [KTransformers](https://github.com/kvcache-ai/ktransformers) **(Adjacent)** | CPU–GPU heterogeneous MoE | Optimized CPU MoE kernels and heterogeneous expert placement | [public code](https://github.com/kvcache-ai/ktransformers) · AI use unverified | Can integrate with other serving runtimes; specialized backend rather than always a separate engine. |
| [Mirage Persistent Kernel](https://github.com/mirage-project/mirage) **(Adjacent)** | Persistent fused GPU execution for LLMs | Compiler/runtime transforms computation and communication into megakernels | [public code](https://github.com/mirage-project/mirage) · AI use unverified | Compiler-generated execution system; not necessarily AI-generated source code. |
| [TensorFold](https://github.com/ashhart/TensorFold) **(Watchlist)** | Local model memory virtualization | Layer-aware streaming and resident-weight budgeting | [public code](https://github.com/ashhart/TensorFold) · AI use unverified | Architecture is evolving; verify current implementation before detailed comparison. |

<!-- CATALOG-END -->

## Case studies and comparisons

- **[VibeQwen / Baseten](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/):** a reported agent-driven, Qwen-targeted inference optimization case. This is listed as a **case study**, not an audited standalone open-source engine.
- **General-purpose baselines:** [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), [llama.cpp](https://github.com/ggml-org/llama.cpp), and [Diffusers](https://github.com/huggingface/diffusers). Their maturity, interfaces, and ecosystem are part of the economic comparison, not just raw latency.
- **Minimal/educational context:** [nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) and [mini-sglang](https://github.com/sgl-project/mini-sglang) are useful learning references, but **not core evidence** that production-grade systems are becoming cheap to replace.

## What we want to measure, not assume

1. **Abstraction tax:** Which generic interfaces impose measurable memory traffic, synchronization, scheduling constraints, or missed fusion opportunities? Which costs disappear after ordinary plugin/kernel tuning?
2. **True specialization benefit:** For fixed semantics, model weights, precision, hardware, workload, and service targets, how does a bespoke path compare to a fairly tuned general-purpose implementation?
3. **Generation economics:** How much human and machine time is required to build, validate, port, debug, and maintain specialized runtimes?
4. **Correctness and quality:** Are gains exact, tolerance-equivalent, or produced by approximate computation, quantization, expert skipping, or model distillation?
5. **Where generality moves:** Do kernel libraries, compilers, agents, testing frameworks, and orchestration absorb the complexity that monolithic runtimes previously carried?

For methodology and potential systems research directions, see [research agenda](docs/research-agenda.md) and [evidence policy](docs/evidence-policy.md).

## Contributions

Project suggestions, corrections, counterexamples, and independently reproduced benchmarks are welcome. In particular, **negative findings** are valuable: an execution path that does *not* beat a well-tuned general engine, a specialization that breaks correctness, or a case where general infrastructure wins on total cost.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before editing the catalog. The curated list is not an endorsement of a project's claims.

## License

Catalog metadata, original commentary, and scripts in this repository are provided under the [MIT License](LICENSE). Linked third-party projects, models, papers, and assets retain their own licenses.
