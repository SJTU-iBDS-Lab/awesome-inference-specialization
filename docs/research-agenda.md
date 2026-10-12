# Research agenda: construction and economics of specialized execution stacks

## Central question

**Are the ways specialized inference stacks are built, who can obtain and maintain them, and their economics changing?** Known model, device and workload constraints have long motivated specialized execution. The research question is whether current construction methods change the feasible choices: which teams can produce a useful artifact, how much control they can obtain, and what it costs across validation, integration, operation and later changes.

The [selected cases](cases.md) are the starting point. Each should explain why another execution path was built, which decisions it controls, what it reuses and gives up, how construction was performed, and which costs remain unknown. [Historical and adjacent routes](systems.md) establish alternatives and continuity; shared compilers, libraries, engines and evaluators provide foundations and comparison baselines. These `survey_role` values are independent of the `catalog_role` describing the delivered software. The seven execution-mechanism families and one tool family remain secondary discovery aids.

The survey does not require systems to be new, AI-built or implemented from scratch. Existing libraries and serving infrastructure may be essential to an economical specialized stack. Conversely, a newly published engine, a small codebase or an AI-authorship statement does not establish a change in economics. Teaching-oriented “nano” reproductions of standard engines are outside scope; a small implementation with substantive execution choices is assessed by the same case questions as any other.

## A causal hypothesis, not a premise

**Hypothesis:** for a specified deployment contract, AI-assisted construction can reduce the total cost of obtaining and maintaining a useful specialized execution stack relative to an appropriate alternative construction workflow.

The claim requires more than a generated artifact or a fast prototype. Total cost includes human work, tools and compute, failed attempts, verification, integration, operation, porting and maintenance over an explicit horizon. A construction method could save coding time while increasing verification or future repair cost. A narrower feature set or a different quality contract could also explain an apparent saving. These alternatives must remain visible.

Availability is a separate outcome: source access, released artifacts, deployment instructions, required expertise, hardware access and successful use by another team determine who can obtain a working system. Public code alone does not establish broad accessibility. Greater availability can be valuable even where lower total cost has not been demonstrated.

## What each core case should answer

| Question | Evidence sought |
| --- | --- |
| Why build another path? | The deployment need and stated reason existing systems or extension points did not provide the desired control |
| Which decisions are owned? | Graph structure, state ownership, memory placement, scheduling, kernel boundaries, synchronization or service behavior controlled by the implementation |
| What is reused and given up? | Dependencies and inherited infrastructure; compatibility, dynamism, portability or service features that are restricted or absent |
| How was it constructed? | Direct implementation, backend adaptation, compilation/search and agent work traced to specific decisions and artifacts |
| What did AI actually do? | Documented tasks, human interventions, candidate generation, testing and acceptance; separate these from general authorship disclosures |
| What remains unknown? | Effort, unsuccessful attempts, validation coverage, integration cost, rebuild cost and observed maintenance history |

The case chain is **reason to build → controlled execution decisions → reuse and trade-offs → construction and artifact → validation and lifecycle cost**. Repository records supply inspectable components; a case can connect a workflow with reported outputs without adding duplicate repositories. Unknowns belong in the case, rather than being silently converted into zero cost or established failure.

## Construction paths to compare

| Path | Decisions to examine | Artifact and evaluation boundary |
| --- | --- | --- |
| Direct native implementation | Explicit state layout, kernel boundaries, memory movement, launch/synchronization and scheduling | An integrated runtime or native execution path; include inherited dependencies and service integration |
| Specialized backend within an existing engine | Which decisions the backend controls, which remain owned by the host, and where extension interfaces constrain it | A backend plus the hosting engine; measure both local behavior and the full service |
| Model/deployment compilation and search | Which model, shape, precision and hardware assumptions become fixed; which transformations/configurations are searched | An executable graph, model library or engine; include compilation, tuning, invalidation and rebuild cost |
| Agent-assisted construction | Which design/code changes are proposed, available tools, human intervention, and candidate acceptance/rejection | Generated kernels, backends or runtimes; execute the actual candidate and account for failed attempts and verification cost |

These paths can be combined. Direct implementation can reuse a compiler; a backend can contain generated kernels; an agent can call established profiling and compilation tools. “Native” describes an implementation boundary, not whether a human or agent wrote it. The output can be one subsystem rather than a complete server.

## Research questions

**RQ1 — Why construct a distinct execution path?** Identify a constraint stable enough to exploit and trace it to decisions an existing implementation does not expose or does not handle well in the target setting. Compare with tuning or extending that implementation. Distinguish a documented motivation from evidence that a separate runtime was necessary.

**RQ2 — Which control produces which integrated effect?** Compare state ownership, layout, fusion, scheduling, movement and synchronization decisions under the same model, hardware, workload and quality contract. Identify the boundary changed and the infrastructure still reused. Separate execution effects from quantization, distillation, skipped work and changed model components.

**RQ3 — Which construction method can reach and validate the design?** Compare direct native work, backend integration, compiler/search and agent-assisted workflows on a specified target. Record the decisions each can express, emitted artifacts, time to a valid integrated result, validation coverage and unsuccessful attempts. The usefulness of a design and the method that found it are distinct claims.

**RQ4 — Does AI reduce total cost, and through which steps?** Define a counterfactual workflow with comparable expertise, resources, scope and acceptance conditions. Measure coding, exploration, diagnosis, verification and integration separately, then track their combined cost through an explicit deployment and maintenance period. Account for pre-existing code, human rescue, selected successes and repeated attempts. Without a credible comparison, report a case observation rather than a causal effect.

**RQ5 — Does construction become accessible to more teams?** Examine source and artifact access, licensing, hardware and expertise requirements, deployment instructions, time to first valid run and use by teams other than the creators. Identify which capability becomes available and which prerequisite remains. Do not use publication date, code size or repository popularity as a substitute.

**RQ6 — What survives a changed deployment?** Change a model revision, shape range, precision mode, device or workload distribution. Identify invalidated code, state, schedules or quality assumptions. Measure diagnosis, rebuild and revalidation effort, test reuse and rollback/fallback behavior. Determine what knowledge belongs in reusable specifications and tooling rather than only in the final artifact.

**RQ7 — When is a shared engine or backend the better choice?** Compare a tuned general engine, a specialized extension and a separate execution stack over the intended volume and lifetime. Include service features, dependency updates and maintenance ownership. Test cases where specialization does not repay its cost. Historical and adjacent systems help distinguish longstanding mechanisms from changes in construction or availability.

## Practical experiment design

The following is a proposed design, not a report of completed experiments.

1. Select distinct execution patterns, such as a dense autoregressive LLM, a constrained-memory MoE and a video diffusion/block-generation workload. Require identifiable constraints and concrete execution decisions rather than selecting only visible successes.
2. Fix model/checkpoint, precision, hardware, shape/workload distribution, concurrency, quality contract, required service features and deployment horizon before comparison. Record supported conditions and fallback requirements.
3. Establish appropriate implementation alternatives: a tuned general engine, its best feasible specialized backend and a separate execution path. Explain unavailable comparisons rather than choosing an intentionally weak baseline.
4. Trace what each alternative controls, inherits and omits. Profile end-to-end compute, memory traffic, transfers, launch/synchronization, scheduling, communication and relevant pre/post-processing.
5. Isolate changed decisions where feasible, then evaluate their interactions after integration. A local kernel improvement and a full-service improvement are different outcomes.
6. Compare construction workflows on the same acceptance contract. For the AI hypothesis, define the counterfactual and record human interventions, tools, failed and accepted candidates, time, compute and validation outcomes. Preserve negative results.
7. Have another team or clean environment attempt deployment when studying availability. Report missing prerequisites, modifications and time to a valid result rather than treating code release as successful transfer.
8. Test at least one changed deployment and account for revalidation and maintenance. Report measured, author-reported and unknown costs separately; give an amortization range when a break-even conclusion depends on uncertain usage or lifetime.
9. Present per-case evidence and limits. Do not turn a selected case collection into a population trend or average unrelated speedups into a ranking.

## Contribution boundaries

A systems contribution should identify an execution, memory, scheduling, communication or deployment problem and show how proposed decisions change integrated behavior under a stated contract. A construction contribution can make a meaningful design space reachable, enforce useful acceptance conditions, improve demonstrated accessibility or reduce measured lifecycle cost. Neither requires implementing all infrastructure from scratch or using agents.

Productivity, defects, review and maintenance are legitimate software-engineering outcomes. They can complement a systems result, but a shorter coding session does not establish a better inference system or a cheaper lifecycle. A hardware-architecture claim requires an evaluated hardware execution, storage or interface implication.

## Open problems

- Specifications that expose the assumptions behind specialized decisions and make invalidation detectable.
- Design/search spaces that include state ownership and cross-component coordination while keeping validation tractable.
- Checking stateful caches, concurrent services and long generation trajectories beyond short local examples.
- Cost accounting that includes failed construction attempts, human interventions and inherited engineering.
- Reusing validation evidence after model, device, backend or generated-artifact changes without assuming unchanged behavior.
- Deciding when to stop specialization, reuse a backend or fall back to a shared engine.
- Maintaining provenance, licensing obligations and dependency updates for directly assembled and generated systems alike.

See the [taxonomy](taxonomy.md), [evidence policy](evidence-policy.md) and [reading list](reading-list.md). The current collection follows the focused inclusion boundary; source evidence lives with retained project and case records.
