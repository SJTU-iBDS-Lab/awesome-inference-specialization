# Taxonomy: inference specialization

This taxonomy distinguishes **the *target* of specialization** from **how an implementation is created**, **how much of execution it controls**, and **how strong the evidence is**. A project can belong to multiple dimensions.

## Specialization axes

| Axis | Typical constraint | System-level consequences |
| --- | --- | --- |
| `model` | Fixed model family, MoE routing, MTP, hybrid attention | Tailored execution sequence, state layout, operator boundaries |
| `hardware` | Particular GPU generation, CPU ISA, unified-memory machine | Explicit placement, launch strategy, native kernels |
| `memory` | Limited VRAM, SSD-backed weights, expert residency | Cache, offload, prefetch, overlap, state virtualization |
| `precision` | Quantization format or mixed precision | Fused quantized kernels, different layout and bandwidth requirements |
| `workload` | Online latency, batch throughput, long context, streaming | Scheduling, batching, state reuse, pipeline organization |
| `domain` | LLM, image diffusion, video diffusion, world models | Domain-specific graph, decoding and serving structure |
| `algorithm` | Distillation, block generation, sparse attention | May change numerical semantics, model, or iteration count |
| `execution` | Cross-operator and whole-graph implementation | Fusion, dataflow, resident kernels, synchronization elimination |
| `parallelism` | Multi-GPU, multiple nodes, CPU/GPU | Partitioning, collective communication, pipelining |
| `builder` | Compiler or coding agent constructs a runtime | Shifts generality to build-time generation and validation |
| `verification` | Contracts, differential tests, benchmarks | Enables safe selection and rejection of generated candidates |

## Implementation depth

1. **Full or domain runtime:** Owns enough of execution, data movement, state, or scheduling for end-to-end specialized behavior. It may reuse established lower-level libraries.
2. **Specialized backend or deep fork:** Controls a significant execution subsystem and integrates with an existing runtime. Not equivalent to a full independent engine.
3. **Compiler / engine generator:** Produces kernels, graphs, or runtime code. The generated artifact may be deployed under another serving system.
4. **Benchmark / correctness infrastructure:** Helps test and compare specialized implementations; generally `Adjacent`.
5. **Case study / deployment-only:** Useful evidence of a trend, but insufficient to inspect a complete implementation. Disclose source limitations.

## Core versus adjacent

`Core` requires a **substantive inference execution system** or an explicit **inference-engine construction workflow**. `Adjacent` captures reusable specialized components, compilers, deep forks, and benchmarking methodology that illuminate the design space. `Watchlist` identifies promising but rapidly changing implementations needing follow-up.

A narrow model set alone is **not sufficient**. We ask *what changed* in memory layout, execution ordering, kernel boundaries, placement, scheduling, or code generation. Conversely, supporting many models does **not** disqualify an otherwise domain-specialized execution stack.

## Agent involvement is independent

- `intrinsic`: the documented system is *defined* by agentic or LLM-based construction/optimization.
- `disclosed`: project maintainers explicitly state that AI agents substantially participated in development.
- `not-established`: no sufficiently direct attribution was established by the catalog maintainers. **Not** a claim of human-only authorship.

A `CLAUDE.md` or `.agents` directory is not, by itself, sufficient attribution for an engine's design. Do not infer performance benefits from AI participation without a controlled study.
