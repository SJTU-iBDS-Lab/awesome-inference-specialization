# Awesome Inference Specialization

**Specialized inference execution stacks built for particular models, hardware and workloads—with a focus on whether AI-assisted development and code generation change how they are implemented, optimized and maintained.**

[中文](README_CN.md) · [Core cases](docs/cases.md) · [Construction comparison](docs/comparison.md) · [Survey library](docs/systems.md) · [Research questions](docs/research-agenda.md) · [Contribute](CONTRIBUTING.md)

## Why this repository?

Specialized inference systems are not new. The question is **whether their construction methods, accessibility and economics are changing—and which system designs become practical as a result.**

We study systems that reclaim control of model execution through direct implementation, substantial adaptation or generated code, together with the workflows that build them. This can include the model graph, kernel dispatch, state, data movement or request execution while retaining shared services and lower-level libraries.

The cases help investigate an unproven causal chain:

> AI-assisted coding or code generation may lower implementation and revision costs → some narrowly targeted execution stacks may become worth building → feasible system designs and delivery practices may change.

**A faster engine, a short development period or the use of an agent does not establish that chain.** Record the motivation, reconstruction and reuse boundary, compatibility given up, actual AI participation, disclosed effort, and missing validation or maintenance evidence.

![Known deployment constraints lead to rebuilt execution decisions, construction and validation, then deployment and maintenance, compared with historical routes and shared foundations](assets/specialization.svg)

## Start with the core cases

<!-- CATALOG-START -->

**[Full directory: 99 projects](docs/systems.md) · [Selected analyses: 14 cases](docs/cases.md)**

Follow the construction process to its resulting system, then examine reuse boundaries and missing evidence. These groups guide reading; AI involvement does not imply better results, and missing disclosure does not imply human-only implementation.

### From a construction workflow to an engine

| Case | Why study it? |
| --- | --- |
| [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) | An author-reported experiment adapted MetaInfer and reused existing kernels to build a deployment-specific Qwen serving stack. |
| [Sol-Engine](docs/cases.md#sol-engine) | An agent-oriented workflow assembles model-specific video execution paths from reusable optimizations and measured quality constraints. |

### Rebuilding execution around deployment constraints

| Case | Why study it? |
| --- | --- |
| [Flash-MoE](docs/cases.md#flash-moe) | A fixed-model C/Metal prototype streams expert weights from SSD and controls the execution pipeline directly. |
| [DwarfStar](docs/cases.md#dwarfstar) | A native stack integrates selected model paths, state management and local serving around consumer-hardware constraints. |
| [Strata](docs/cases.md#strata) | A Qwen-specific runtime combines GPU-resident work with CPU expert execution and explicit memory budgets. |
| [NInfer](docs/cases.md#ninfer) | Owns model execution, state and serving within a deliberately narrow checkpoint and GPU contract. |
| [Iris](docs/cases.md#iris) | A C image-generation pipeline replaces framework-level execution for selected architectures while retaining platform acceleration. |
| [TensorFold](docs/cases.md#tensorfold) | A Zig server admits explicit model–format–platform combinations and executes their native Metal or CUDA paths. |
| [Halogen Flash](docs/cases.md#halogen-flash) | A distributed binary targets one Qwen family and AMD Strix Halo, with public deployment and quantization descriptions. |
| [ExLlamaV3](docs/cases.md#exllamav3) | A local-inference library couples EXL3 encoding, quantized state and qualified execution paths for consumer GPUs. |

### Specialized backends and generated programs

| Case | Why study it? |
| --- | --- |
| [Magnitude](docs/cases.md#magnitude) | The reviewed Metal path captures typed operations and constructs specialized fused kernels inside MLX’s execution machinery. |
| [KTransformers](docs/cases.md#ktransformers) | A specialized heterogeneous backend uses CPU capacity and instruction sets for MoE experts while retaining GPU serving components. |
| [Nunchaku](docs/cases.md#nunchaku) | A low-bit diffusion backend co-designs packed weights and fused execution so the outlier-correction branch remains affordable. |
| [Mirage MPK](docs/cases.md#mirage) | A compiler/runtime turns an assembled LLM task graph into persistent GPU execution spanning computation and communication. |

### Compare the cases with existing routes

- [Historical and adjacent routes](docs/systems.md#adjacent): ZeRO-Inference, FlexGen, DistServe, S-LoRA and MLC LLM help establish which ideas already exist.
- [Shared foundations and baselines](docs/systems.md#foundation): general engines, compilers, kernels and evaluators reveal what is reused and what a fair comparison requires.

Relevance describes a record’s role in this survey, not its quality, maturity or age. The full [library](docs/systems.md) retains the broader collection.

<details>
<summary>按执行机制检索资料库 / Browse the library by execution mechanism</summary>

[Data residency & movement](docs/catalog.md#memory) · [Numerical representation](docs/catalog.md#precision) · [Selective computation](docs/catalog.md#selection) · [Computation reuse](docs/catalog.md#reuse) · [Generation order](docs/catalog.md#decoding) · [Parallelism & scheduling](docs/catalog.md#serving) · [Compiled & native execution](docs/catalog.md#execution) · [Construction & validation tools](docs/catalog.md#construction)

</details>

<!-- CATALOG-END -->

## Read each case as a construction decision

**Why build another stack → what is rebuilt → what is retained or given up → how it is constructed → how it is validated and maintained.**

For example, [VibeQwen](docs/cases.md#vibeqwen) is an engine outcome; [MetaInfer](docs/catalog.md#metainfer) supplies the construction workflow that was adapted for it. A case card connects them without treating the workflow and its output as the same artifact or duplicating repository counts. Author disclosures, public implementation, validation coverage and unknown effort remain distinct.

The [construction comparison](docs/comparison.md) starts with execution ownership and disclosed effort. Eight [mechanism families](docs/catalog.md) remain secondary search labels for understanding how these designs execute.

## What belongs here?

A **core case** must explain why it illuminates the construction of a specialized execution stack, beyond identifying a deployment constraint and an optimization. Identify the resulting program, the execution decisions it owns, retained dependencies and traceable sources. Unknown construction and maintenance costs are acceptable when explicitly marked unknown.

- **Core cases:** purposeful execution-stack reconstruction, or construction workflows connected to concrete specialized artifacts. Neither a dependency-free implementation nor established AI authorship is required.
- **Historical and adjacent routes:** earlier and contemporary specialized systems, compiler specialization, heterogeneous execution and related construction methods that establish what already exists and what may be changing.
- **Shared foundations and baselines:** general engines, compilers, kernels, optimization components and evaluators that explain reuse and fair comparison.

Relevance and artifact type are independent. Recency, a small codebase, agent use or speed alone does not qualify a core case. Teaching-oriented nano implementations are outside the collection’s scope. See the [classification and inclusion guide](docs/taxonomy.md).

## Evidence and research

This collection reviews sources; it does not independently reproduce project performance. Author results are not independent validation. Separate effects of quantization, approximation and model changes from runtime effects. Establish AI participation through direct disclosure or an inspectable construction workflow, never filenames, coding style or repository size. The [evidence policy](docs/evidence-policy.md) specifies appropriate claim boundaries.

The [research agenda](docs/research-agenda.md) asks what is changing: which general abstractions are worth replacing, which construction steps become automated, whether savings cover verification and maintenance, and what model or hardware changes cost to accommodate. The [historical survey](docs/survey-2026-10-12.md) records the earlier broad search; the [library](docs/systems.md) retains all existing entries.

[Project records](catalog/projects.csv) and [case records](catalog/cases.json) generate the homepage selections, case studies, relevance index, mechanism catalog and comparison. See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance. Metadata, original diagrams, commentary and scripts use the [MIT License](LICENSE); linked projects and models retain their own licenses.
