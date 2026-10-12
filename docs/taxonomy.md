# Taxonomy: inference specialization

The catalog groups projects by **what they change in inference execution**. Domain, constraints, artifact type, semantic effects, and source access are independent dimensions. A project has one editorial primary `family` for navigation and multiple `mechanisms` for its actual implementation. The primary family is neither a quality ranking nor a claim that the project implements only one mechanism.

## Eight navigation families

| ID | Organizing question | Typical mechanisms |
| --- | --- | --- |
| `memory` | What stays close to compute, and when does it move? | Weight/expert/KV residency, paging, offload, prefetch, transfer overlap, memory planning and layouts |
| `precision` | How is each value represented and computed? | Weight/activation/KV quantization, mixed precision, low-bit formats and fused dequantization |
| `selection` | Which computation or state can be omitted? | Sparse attention, token/neuron selection, expert dropping, KV eviction and selective execution |
| `reuse` | Which earlier results can be used again? | Prefix/KV sharing, invariant features, cross-attention caches and diffusion feature reuse |
| `decoding` | How does generation advance? | Draft-and-verify decoding, multi-token proposals, block and parallel generation |
| `serving` | Which request or device executes what, and when? | Batching, chunked prefill, request scheduling, tensor/sequence/context/pipeline parallelism and disaggregation |
| `execution` | How does a graph become an executable? | Compilation, graph/operator fusion, kernel specialization, persistent execution, graph replay and native backends |
| `construction` | How are specialized programs built and checked? | Coding agents, kernel DSLs, configuration search, profiling, differential validation and benchmark infrastructure |

The first seven families describe execution mechanisms. **`construction` contains supporting tools**: a language, agent, or benchmark does not itself establish an inference speedup. Inspect the program it produces or evaluates, its integration, and its validation path. Some projects legitimately span both roles.

The family definitions and navigation examples are stored in [the schema](../catalog/schema.json). The [catalog](catalog.md) exposes the individual records and their evidence.

## Independent dimensions

| Dimension | What it records | What it must not imply |
| --- | --- | --- |
| `domains` | Text, image, video, audio, multimodal, or general-purpose coverage | A domain is not an optimization mechanism; example coverage is not universal support |
| `constraints` | Model structure, hardware, memory capacity, shapes, workload, or deployment assumptions | A narrow model list alone does not establish substantive specialization |
| `mechanisms` | Multiple concrete actions, such as KV offload, fused dequantization, or persistent workers | Membership in the primary family does not exhaust the implementation |
| `artifact_type` | The component delivered by the cataloged project | A kernel library is not automatically a full runtime |
| `semantic_effect` | Changes and assumptions that require evaluation | A tag is not a correctness certificate |
| `source_visibility` | Relevant code access and disclosed restrictions | Public visibility does not establish licensing completeness, correctness, or maturity |

A constraint explains **why** specialization is useful; a mechanism explains **what changes**. For example, limited VRAM is a constraint, while expert offload is a mechanism. Both an LLM and a video denoiser can use fusion, quantization, reuse, and distributed execution, but their state and quality contracts differ.

## Artifact types

- `runtime`: manages integrated execution, state, data movement, or requests for a workload.
- `backend`: implements a substantial execution subsystem used by another runtime.
- `compiler`: transforms graphs or programs into executable artifacts.
- `optimizer`: rewrites or selects configurations for an existing execution stack.
- `kernel-library`: supplies operator or kernel implementations for integration elsewhere.
- `research-prototype`: packages an experimental system whose component boundaries or supported scope remain specific to the demonstrated setup.
- `generator`: constructs source, kernels, graphs, or engines, including agent-driven workflows.
- `verification`: evaluates correctness, quality, or performance of candidate implementations.

These are component descriptions, not a maturity ladder. Choose the type of the component being cataloged and describe other roles in the mechanism summary or caveat. A project may evolve: for example, FastKernels has both evaluation machinery and a documented [minimal serving framework](https://github.com/Snowflake-AI-Research/fastkernels/blob/HEAD/docs/serving-framework-guide.md). Its evaluation role and serving coverage should be stated separately.

<a id="semantic-effects"></a>

## Semantic effects: what must be evaluated

`semantic_effect` is multi-valued. It describes evaluation obligations, rather than declaring an implementation exact or safe.

| Value | Meaning | Required attention |
| --- | --- | --- |
| `layout-scheduling` | Changes placement, layout, scheduling, fusion, or execution order while intending to preserve the computation | Indexing, state transitions, synchronization, numerical reduction order, and supported shapes |
| `reduced-precision` | Changes the representation or arithmetic precision of weights, activations, or state | Formats, calibration, accumulation precision, error and task quality |
| `selective-approximation` | Omits work or state that the reference computation would use | Selection policy, budgets, fallback behavior and workload-dependent quality |
| `stale-state` | Reuses an earlier result, or predicts a current result from earlier states | Refresh policy, accumulated drift, failure cases and quality across trajectories |
| `verified-proposals` | Generates candidates whose acceptance is checked by a target or verifier | Acceptance/rejection and correction rules, target distribution or output contract, and verifier implementation |
| `trained-model` | Uses changed, trained, or distilled model components or weights | Model identity, training assumptions, and attribution of speed/quality changes |
| `configurable` | Different enabled modes have materially different effects | The exact active configuration; add the specific applicable effect tags where known |
| `tool-dependent` | Effects depend on the program generated, selected, or tested by a tool | The emitted artifact, integration, validation coverage and measured configuration |

Exact prefix reuse, under valid cache keys and compatible model state, is not the same as substituting an earlier diffusion residual. The latter needs a stale-state quality assessment. This tag also covers history-based feature prediction: TaylorSeer extrapolates features rather than simply returning a cached value. Similarly, a draft-and-verify interface does not by itself prove distribution preservation: the acceptance and correction implementation matters. A trained draft model and a trained replacement target also have different implications; record which component changed.

## Cross-domain examples and classification boundaries

| Situation | Classification and boundary |
| --- | --- |
| MoE experts do not fit in VRAM | Residency and offload are `memory`. Skipping routed experts is `selection`; it introduces a different evaluation obligation. Ordinary model-defined routing is not automatically an additional approximation. |
| An LLM changes its KV handling | Offload is `memory`, low-bit KV is `precision`, compatible prefix reuse is `reuse`, and retaining only selected KV entries is `selection`. These may coexist. |
| Low-bit LLM matmul and low-bit diffusion layers | Both can combine `precision` with fused `execution`. Quantization formats, accumulation and model quality must be checked separately for each implementation. |
| A video generator reuses denoising features | Cross-step substitution belongs to `reuse`, often with `stale-state`. Changing block-generation order belongs to `decoding`; VAE chunking may instead concern `memory` and `execution`. |
| A system uses persistent GPU workers and tensor parallelism | Persistent workers concern `execution`; distributing tensor work concerns `serving`. Neither mechanism should hide the other. Mirage exposes a concrete [persistent-kernel implementation](https://github.com/mirage-project/mirage/blob/mpk/include/mirage/persistent_kernel/persistent_kernel.cuh). |
| A compiler lowers models while a DSL builds kernels | A model-to-executable path can use `execution` as its primary family; a reusable language can use `construction`. MLC-LLM's [compiler pipeline](https://github.com/mlc-ai/mlc-llm/blob/HEAD/python/mlc_llm/compiler_pass/pipeline.py) names concrete fusion, dequantization and dispatch passes. The word “compiler” alone does not specify their effects. |
| An agent produces an inference engine | The generator is `construction`; the emitted engine has its own mechanisms and validation obligations. MetaInfer, KernelAgent and Sol-Engine expose different construction scopes. A generated kernel does not establish a complete serving system. |

Broad projects can reasonably fit several navigation groups. Sol-Engine, for example, exposes an agent workflow and concrete model runtimes; placing its record under `construction` emphasizes how it builds specialized engines, while its mechanism tags must retain the runtime's fusion, caching, attention and precision behavior. A future record focused only on one deployed runtime could have a different primary family without contradicting this classification.

## Assigning a primary family

1. Identify the cataloged component and its deployed or generated artifact.
2. Read the implementation path for the mechanism, including dispatch and fallback conditions.
3. Choose the family that best answers the component's central specialization question.
4. Preserve other substantive mechanisms, constraints and semantic effects as separate tags and prose.
5. Explain ambiguous boundaries in the caveat; revise the assignment when the project's scope changes.

Counts by primary family describe this catalog's editorial organization. They do not measure research importance, prevalence, quality, or mutually exclusive technical populations. Follow the [evidence policy](evidence-policy.md) when converting source observations into claims.
