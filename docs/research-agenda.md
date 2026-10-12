# Research agenda: building specialized inference systems

## Purpose and reading order

This catalog supports a concrete systems question: **when a model, device or workload offers stable constraints, how should those constraints be turned into a deployable inference system, and how can that system be checked and maintained?** The object of study is the connection between the constraint and the resulting execution decisions, not optimization in the abstract.

The [systems and construction guide](systems.md) therefore foregrounds integrated systems and specialized backends, then concrete construction workflows. General engines, compilers, DSLs, kernel libraries, mechanism components and evaluators provide reference points and reusable infrastructure. These are display roles (`system`, `construction`, `support`), not quality levels. The seven execution-mechanism families and one construction-tool family remain a second layer for finding related techniques; they do not define the main research question.

The value of collecting these projects is to make implementation choices comparable: what the system assumes, which decisions it fixes or changes, what artifact it delivers, and which obligations remain after deployment. A constrained-memory MoE runtime, a fixed-device video pipeline and a generated model library may rely on different mechanisms, but each should expose this chain:

**Constraint → changed execution decision → deployable artifact → validation and maintenance.**

Neither a narrow model list nor a faster isolated kernel establishes a complete specialization account. A reusable component can still be valuable without claiming to be an integrated system. All existing catalog records remain useful for tracing these relationships; the display order highlights the systems and construction questions.

## Construction paths to compare

| Path | Decisions to examine | Artifact and evaluation boundary |
| --- | --- | --- |
| Direct native implementation | Explicit state layout, kernel boundaries, memory movement, launch/synchronization and scheduling | An integrated runtime or native execution path; include its dependencies and service integration |
| Specialized backend within an existing engine | Which decisions the backend controls, which remain owned by the host engine, and where extension interfaces constrain it | A backend plus the hosting engine; measure both local behavior and the full service |
| Model/deployment compilation and search | Which model, shape, precision and hardware assumptions become fixed; which transformations/configurations are searched | An executable graph, model library or engine; include compilation, tuning, cache invalidation and rebuild cost |
| Agent-assisted construction | Which design/code changes are proposed, what tools the agent can use, and how candidates are accepted or rejected | Generated kernels, backends or runtimes; execute the actual candidate and account for failed attempts and verification cost |

These paths can be combined. Direct implementation can reuse a compiler; a backend can contain generated kernels; an agent can call established profiling and compilation tools. The comparison should isolate what each step contributes. AI participation is a construction choice to evaluate, not a premise that it improves performance, correctness or engineering cost.

## Research questions

**RQ1 — Which constraints justify which decisions?** Identify properties stable enough to exploit: model topology, expert structure, device memory hierarchy, bounded shapes, repeated state or a known request distribution. Trace each property to a concrete decision such as placement, state ownership, fusion, launch strategy or scheduling. Specify when the assumption becomes false and what the implementation then does. A generic optimization flag or a workload label alone is not a sufficient explanation.

**RQ2 — Where does a general engine leave avoidable cost?** On the same model, hardware and workload, compare the tuned general engine, its best feasible specialized backend, and a purpose-built execution path. Examine graph boundaries, state ownership, layout conversions, synchronization, memory lifetime, communication and scheduling. Determine whether a gain requires changing an interface or can be obtained within existing extension points. Do not assume that a new runtime is necessary or that every overhead is inherent to generality.

**RQ3 — Which construction path can reliably reach the needed design?** Compare direct native work, backend integration, compiler/search workflows and agent-assisted workflows on a specified design task. Record the decisions each path can express, the artifacts it produces, validation coverage, time to a valid integrated result and unsuccessful attempts. Separate the usefulness of a design from the method that discovered or implemented it.

**RQ4 — What must be validated after specialization?** Establish the contract before optimization: numerical tolerance, greedy output behavior, sampling behavior, acceptable approximation or task/perceptual quality. Test stateful caches, long trajectories, concurrent requests, rejection paths and device-specific corner cases where relevant. Check that the acceptance gate invokes the actual candidate and that failures prevent promotion. A local kernel check and an integrated model/service check answer different questions.

**RQ5 — When do construction and maintenance costs pay off?** Measure developer effort, tool/agent cost, profiling and validation compute, integration work and ongoing regressions alongside steady-state latency, throughput and memory. Evaluate the deployment volume and lifetime needed to amortize build and maintenance cost. Include a case in which specialization is not worthwhile; a fast prototype does not establish a low-cost service.

**RQ6 — How can a system be rebuilt when its assumptions change?** Change a model revision, shape range, precision mode, device or workload distribution. Identify which assumptions invalidate generated code, caches, schedules or quality checks. Measure diagnosis and re-specialization effort, test reuse and rollback/fallback behavior. Ask what knowledge should live in reusable specifications and tooling rather than only in the final implementation.

**RQ7 — What should remain shared across systems and modalities?** Compare the boundary between shared serving infrastructure and specialized execution, and between reusable compilers/kernels and model-specific coordination. Autoregressive text, memory-constrained MoE and iterative or block-based video generation have different state and progress units. Determine which construction and validation practices transfer, and which depend on those units. Do not infer cross-modal gains from a common mechanism name.

## Practical experiment design

The following is a proposed design, not a report of completed experiments.

1. Select **three distinct execution patterns**, such as a dense autoregressive LLM, a constrained-memory MoE and a video diffusion/block-generation workload. Select them for identifiable constraints and measurable execution decisions.
2. Specify model weights, precision, hardware, shape/workload distribution, concurrency, quality requirements and error tolerance before optimization. Record the supported deployment envelope and required fallback.
3. Establish implementation points where feasible: a tuned general engine, a specialized backend within that engine, and a purpose-built runtime/control path. Explain unavailable comparisons rather than substituting an intentionally weak baseline.
4. Profile end-to-end costs: compute, memory traffic, launch/synchronization, offload, scheduling, communication and relevant pre/post-processing. Tie each proposed change to an observed cost or an explicit capacity constraint.
5. Change one decision or interface boundary at a time where feasible; then evaluate interactions in the integrated system. Separate model/algorithm changes from execution changes.
6. Compare construction methods on the same target contract. Preserve accepted and rejected candidates, actual verification results, time and resource costs, and integration failures. If only one method is used, avoid claims that it is superior to the others.
7. Test at least one changed deployment to measure invalidation, portability and maintenance. Include warm/cold behavior and construction cost amortization where they affect the intended use.
8. Report a per-case chain from constraint to decision, artifact and evidence. State unsupported configurations and negative results. Do not aggregate unrelated speedups into a single ranking.

## Contribution boundaries

A systems contribution should identify an execution, memory, scheduling, communication or deployment problem and show how the proposed decisions change integrated behavior under a stated contract. A software-engineering contribution may instead study productivity, defects, review or maintenance; these outcomes can complement a systems result but do not substitute for it. A hardware-architecture claim requires an evaluated hardware execution, storage or interface implication.

A construction workflow can be a substantive contribution when it makes a meaningful system design space reachable, enforces useful acceptance conditions, or reduces demonstrated re-specialization effort. It does not need to be agent-driven. Conversely, an agent that writes working code does not by itself establish a new system mechanism, a performance gain or lower total cost.

## Open problems

- Specifications that capture model/device/workload assumptions and make their invalidation detectable.
- Search spaces that include state ownership, scheduling and cross-operator decisions, with validation that remains tractable.
- Testing stateful KV/expert caches, concurrent services and long-running generation beyond short isolated cases.
- Separating the contributions of precision, selection, reuse, model changes and execution coordination in a combined system.
- Reusing validation evidence after a model, device, backend or generated artifact changes without assuming unchanged behavior.
- Deciding when to stop specialization, reuse a backend, or fall back to a general engine.
- Maintaining provenance, licensing obligations and dependency updates for manually assembled and generated systems alike.

See the [taxonomy](taxonomy.md), [evidence policy](evidence-policy.md) and [reading list](reading-list.md) for classification, claim boundaries and supporting material. Historical survey documents record their original inspection scope; the current navigation does not rewrite those records.
