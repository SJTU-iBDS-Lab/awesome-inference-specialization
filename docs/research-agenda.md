# Research agenda: from general-purpose runtimes to specialized execution systems

## Central conjecture

As AI-assisted code generation, compiler generation, and systematic verification reduce the marginal cost of specialized implementations, some deployments may favor **purpose-built execution paths** over extending a general runtime. This is a **hypothesis**. The alternatives are equally plausible: a well-designed generic runtime may absorb most specialization behind extensible backends, or the verification/maintenance cost may erase development savings.

## Research questions

**RQ1 — What is the actual abstraction tax?** Identify where generic interfaces constrain execution: graph boundaries, KV/expert state ownership, synchronization, data layout, scheduling, memory lifetime, communication, or inability to fuse across components. Measure costs on the same model/hardware/workload. Compare a generic implementation with its best plugin/kernel tuning, not just default settings.

**RQ2 — What can specialization change?** Map each case to compiler/kernel, execution graph, memory hierarchy, scheduler, data placement, and service interface. Ask which gains are *structural* (could not reasonably be obtained within an existing extension point) versus implementation/parameter tuning.

**RQ3 — What are the economics of bespoke systems?** Record developer-hours, agent/tool cost, GPU profiling/verification cost, porting cost, time-to-correctness, integration defects and maintenance changes. A fast proof of concept is not yet a low-cost service.

**RQ4 — Can specialization be safely repeated?** If the model, workload, or hardware changes, can an implementation be re-specialized while retaining a correctness contract and predictable rollback? What reusable knowledge must be retained outside the generated runtime?

**RQ5 — Where is the right boundary of shared infrastructure?** Contrast monolithic runtimes, specialized backends atop generic serving, compiler-generated megakernels, and end-to-end bespoke engines. Identify workloads where each is preferable.

**RQ6 — Does the pattern hold outside autoregressive LLMs?** Compare diffusion/flow models, block-diffusion video, mixture-of-experts models and distributed inference. The key unit of execution is not universal.

## Practical experiment design

1. Select **three distinct execution patterns** rather than many similar models: e.g., a dense autoregressive LLM, a memory-constrained MoE, and a video diffusion/block-diffusion workload.
2. Specify model weights, precision, hardware, concurrency, input/output distribution, quality requirements and error tolerance *before* optimization.
3. Establish three implementation points: (a) tuned general-purpose engine, (b) best feasible specialized backend in that engine, (c) bespoke runtime/control path.
4. Profile and categorize end-to-end costs: compute, memory traffic, launch/synchronization, offload, scheduling, communication and admission.
5. Change one abstraction boundary at a time where feasible. Measure its incremental effect, *then* evaluate full-stack co-design.
6. Collect time and effort costs from first executable prototype to a verified workload suite, including failures and regressions; not just a single successful optimization run.
7. Test at least one **changed deployment** (e.g., another GPU, quantization, model variant, load distribution) to measure portability and re-specialization cost.

## Distinguishing systems from software-engineering contributions

A **software-engineering** paper may study agent productivity, bug finding, code review, or software lifecycle. A **systems** paper should isolate a performance/correctness bottleneck, propose an execution, memory, scheduling, communication or deployment mechanism, and show why it changes end-to-end behavior. An **architecture** paper should identify and evaluate a hardware execution, storage, or interface implication—not just describe software architecture.

AI coding may be the **method used to explore a system design space** without needing to be the central claimed novelty.

## Open problems

- How to measure *cross-layer* specialization without attributing all gains to one convenient layer.
- Differential testing of stateful KV/expert caches and long-running streaming pipelines.
- Correctness and utility after numerical approximation, distillation or expert skipping.
- Search spaces large enough to include structural execution changes, but constrained enough to admit systematic verification.
- When to stop specializing or fall back to a general engine.
- Ownership, licensing and provenance of generated systems that incorporate existing kernels and runtime code.

See also the [evidence policy](evidence-policy.md) and [reading list](reading-list.md).
