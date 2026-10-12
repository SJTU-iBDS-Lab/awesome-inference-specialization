# Evidence and comparison policy

Every project record should explain **what mechanism is implemented, under which constraints, and where it can be inspected**. Selected cases additionally explain why a distinct execution path was built, what it reuses or gives up, how construction was performed, and which cost and maintenance claims remain unknown. Source access, implementation inspection, validation, performance reproduction, and deployment readiness are separate claims. This catalog records source-based findings; an evidence link does not mean that the maintainers independently reproduced the advertised result.

## Match the claim to the evidence

| Evidence available | Appropriate claim | What it does not establish |
| --- | --- | --- |
| Official README or design documentation | “Describes …” or “Reports … under the stated setup” | That the relevant implementation is public, complete, or exercised by the example |
| Inspected implementation and call path | “Implements … in this path/configuration” | Correctness for all inputs, support on all devices, or a measured speedup |
| Author-provided evaluation procedure and results | “Reports … with these models, settings, baselines and metrics” | Independent reproduction or portability to another workload |
| Independent reproduction under documented conditions | “Independently reproduced … for this setup” | Universal performance or quality guarantees |

Do not turn repository existence into implementation evidence or author benchmarks into independent validation. An inspected file may establish a mechanism while leaving its integration unverified. Record that limit explicitly.

## Evidence for construction, availability and economics

A visible specialized stack is evidence that a particular artifact exists. It does not establish that such stacks have become cheaper, easier for more teams to obtain, or more economical to maintain. A collection of successful recent examples also cannot establish that AI caused a change: selection, model simplicity, hardware access, prior code, team expertise and unreported failed attempts can affect the result.

| Claim | Evidence to seek | Boundary to retain |
| --- | --- | --- |
| Why a separate path was built | Direct rationale plus the execution decisions or extension constraints visible in the implementation | A motivation statement does not prove that a tuned existing engine could not satisfy the need |
| What was reused or abandoned | Dependency and integration paths, supported configurations and explicit omissions | Few lines of new code do not mean little inherited engineering; missing features are not automatically intended trade-offs |
| What construction or AI actually did | Workflow/code, disclosed human interventions, prompts or task logs where available, emitted artifacts and acceptance decisions | AI-authorship claims and an agent construction method are different evidence; neither establishes saved effort |
| Who can obtain and use the result | Access/license, released artifacts, hardware requirements, setup procedure and external execution evidence | Public code alone does not establish reproducible deployment or accessibility to teams with different resources |
| Total construction and operating cost | Human effort, tool and compute spending, failed candidates, validation, integration, serving and change/maintenance costs with a stated horizon | Prototype elapsed time, agent tokens or steady-state speed alone are not total cost |
| AI reduced total cost | Comparable target contracts and resources, an explicit non-AI or alternative-workflow counterfactual, complete cost accounting and uncertainty | Before/after anecdotes or selected successes support a hypothesis, not causal attribution |

Record missing evidence as **unknown**, not as zero cost or evidence of failure. Distinguish measured costs, author-reported costs, inferred trade-offs and unmeasured obligations. A core case can be valuable for exposing these gaps without establishing economic success.

Case records may link a construction workflow and a reported generated output. Keep those sources distinct and do not count the output as another repository without an independently identified upstream project. In particular, link VibeQwen-related claims to the MetaInfer workflow and the relevant Baseten output report; evidence for one side of that relationship does not automatically verify the other.

## Inspect the path that is actually used

For a substantive mechanism claim, trace the relevant dispatch, implementation, configuration, and fallback. For a validation claim, check whether the candidate is actually invoked, what reference it is compared against, which inputs are tested, and whether failure propagates to the acceptance decision. A directory called `verifier` or a test named “correctness” is not sufficient evidence.

Concrete examples from source inspection illustrate the distinction:

- MetaInfer's [correctness oracle](https://github.com/MetaInfer/MetaInfer/blob/HEAD/metainfer/tasks/gen_infer_framework/orchestrator/oracles/correctness.py) starts the generated service and tests an API using prescribed prompts, with judge or heuristic paths. This is evidence of service-level checks, not a proof of numerical equivalence across all model inputs.
- In the inspected AgentCompile revision, the generic [benchmark selector](https://github.com/veneno1213822/AgentCompile/blob/043e454f55f69355e483920fa6292ff5731ecf41/benchmark/selector.py#L104-L114) times a proxy operation, and the generic [verifier](https://github.com/veneno1213822/AgentCompile/blob/043e454f55f69355e483920fa6292ff5731ecf41/verifier/verifier.py#L89-L93) can return success when the CUDA compiler is unavailable. These paths require a concrete caveat despite the README's validation language. This observation does not establish that every dedicated fusion path has the same limitation.
- Sol-Engine has visible [model runtime code](https://github.com/NVlabs/Sana/blob/sol-engine/models/wan22_ti2v_5b/optimized/wan_kernel_runtime.py) and a [perceptual image judge](https://github.com/NVlabs/Sana/blob/sol-engine/tools/vision/lpips_judge.py). A documentation-only label would miss the implementation; perceptual similarity checks should still not be described as bitwise equivalence.
- The public [TensorRT repository](https://github.com/NVIDIA/TensorRT) exposes components such as plugins, parsers and samples, rather than the complete optimizer/runtime core. Public examples support claims about those interfaces, not inspection claims about the closed implementation.

Pin a commit for a consequential negative or rapidly changing implementation finding. A current-branch link is useful for navigation, but it can move after the recorded inspection date.

## Semantic effects determine the evaluation contract

The [semantic-effect tags](taxonomy.md#semantic-effects-what-must-be-evaluated) identify changes to assess; they are not correctness certificates. Multiple tags can apply to one configuration.

| Effect | Minimum evaluation questions |
| --- | --- |
| `layout-scheduling` | Are shapes, indexing, synchronization, state ownership and numerical tolerances preserved? Are stateful and concurrent paths exercised? |
| `reduced-precision` | Which values and accumulators change precision? What calibration and quality tests support the chosen format? |
| `selective-approximation` | What work or state is removed? How does error change with selection budgets and difficult inputs? |
| `stale-state` | When is cached state refreshed? How is drift measured over the full generation trajectory? |
| `verified-proposals` | What verifies acceptance? Are rejection/correction paths implemented, and which target distribution or output contract is intended? |
| `trained-model` | Which weights or components changed? How much of the result comes from the model change rather than its execution system? |
| `configurable` | Which modes were enabled in the reported run, and which specific effects apply to them? |
| `tool-dependent` | Was the generated or selected candidate executed and checked after integration? What does the tool's acceptance gate actually cover? |

Identical greedy tokens on a test set, close tensor outputs, acceptable perceptual quality, and preservation of a sampling distribution are different contracts. Report the one actually tested. A successful verifier run has meaning only within its tested reference, tolerances, inputs and failure handling.

## Fair comparisons

- **Model and algorithm:** checkpoint, tokenizer, architecture, routing, draft/target identity, quantization, denoising steps, distillation, and other changed components.
- **Numerical and quality contract:** reference behavior, tolerance, approximate paths, calibration, and task or perceptual quality criteria.
- **Hardware and software:** accelerator type/count, host CPU, memory capacity, storage, interconnect, drivers, compiler and dependency versions.
- **Workload:** input/output lengths, concurrency, batching, cache hit rate, warm/cold state, image resolution, video frame count and other modality-specific dimensions.
- **Baselines:** relevant optimized systems with disclosed tuning, compatible models, quality settings, resources and timing boundaries.
- **Timing scope:** model load, compilation/search, warm-up, transfers, pre/post-processing and steady-state inference; state which are included.
- **Construction and maintenance:** human effort, tools, profiling/validation compute, rejected attempts, integration work, model/device updates, deployment horizon and amortization assumptions.
- **Metrics:** TTFT, per-token latency, throughput, tail latency and memory for serving; full-generation latency, throughput and quality for image/video; construction cost and amortization when compilation or agents are involved.

LLM prefill throughput and decode latency answer different questions. A faster video denoiser does not automatically imply the same end-to-end gain after text encoding, VAE decoding and transfers. A compiler or agent can improve steady-state execution while adding substantial build/search cost. Keep these boundaries visible rather than averaging incomparable results.

Do not compute an average speedup across projects with different models, hardware, precision, quality budgets, or timing scopes. Cross-project tables should compare disclosed mechanisms and assumptions unless a controlled measurement supports direct performance comparison.

## Kernel checks and integrated checks

A kernel benchmark can establish behavior for its supplied tensor cases without exercising model state, decoding, cache lifetime, batching, or a service interface. For example, [KernelBench's evaluator](https://github.com/ScalingIntelligence/KernelBench/blob/HEAD/src/kernelbench/eval.py) tests candidate implementations within a benchmark harness. Its coverage should not be presented as complete model-serving validation.

Integrated checks have their own scope. [FastKernels' model evaluator](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/fastkernels/eval.py) checks generated tokens for an enabled end-to-end configuration. Such a check supplements operator tests; it does not prove equivalence for every prompt, decoding policy, precision or hardware target. Record both the local and integrated validation evidence when available.

## Source visibility and access

- `public-code`: relevant source is publicly inspectable. This does not establish an OSI-approved license, license completeness, independent correctness, or production readiness.
- `closed-core`: public interfaces, examples or components are available while the relevant engine core is not fully inspectable.
- `documentation-only`: official documentation is available, but the relevant implementation was not located or inspected. Recheck this label when a linked branch or repository becomes available.
- `review-only`: source access or use is restricted to review. This is an access/licensing attribute, not a verdict on the implementation's validation quality.

Inspect the actual license and its scope. A README's licensing statement and a missing referenced license file should be reported as a gap rather than replaced with an assumed license. The catalog's license does not relicense linked projects. Validation placeholders belong in a mechanism-specific caveat, independently of a `review-only` label.

## Agent involvement is independent

`intrinsic` means that the documented system uses agents or LLMs as part of its construction or optimization method. `disclosed` means that maintainers explicitly report AI participation in development. `not-established` means that the catalog has not established sufficiently direct attribution; it does not mean human-only authorship.

A `CLAUDE.md`, an agents directory, coding style, or repository size does not establish how an engine was built. Report the specific AI task and the human decisions or interventions disclosed; do not collapse all forms of participation into autonomous construction. A compiler is not necessarily agent-driven. Use explicit maintainer statements or an inspected generation workflow, and do not attribute performance gains to AI participation without a controlled comparison.

## Updating a record

Keep canonical project URLs, direct evidence pointers, an inspection date, and a concrete caveat. Preserve the distinction between repository records in `catalog/projects.csv` and selected case accounts in `catalog/cases.json`; `survey_role` describes research relevance, while `catalog_role` and `artifact_type` describe the delivered software. Prefer an implementation pointer alongside documentation for mechanism claims. Preserve a pinned revision for findings whose interpretation depends on exact code.

The inspection date records when the source was checked, not the software release date or a promise of future validity. When a repository adds code, serving support, a new backend or a different validation path, update source visibility, artifact scope and caveats together. Keep mechanism observations, semantic effects and evaluation results distinct; explicitly label inference, untested paths, source inspection and independent reproduction.
