# Awesome Inference Specialization

**Specialized inference engines, the workflows that build them, and the methods that validate them.**

[中文](README_CN.md) · [Engines](docs/systems.md#system) · [Construction](docs/systems.md#construction) · [Validation](docs/validation.md) · [Benchmarks](docs/benchmarks.md) · [Supporting resources](docs/resources.md)

## Why this repository?

When models, hardware and workloads are known, developers can rebuild parts of the execution stack around those conditions. This repository studies **what they rebuild, how they obtain the resulting engine, and how they establish that it works**—across language, multimodal, image, video and audio models.

Specialized systems are not new. The research question is whether AI-assisted development and code generation change their construction, availability and maintenance costs, making more narrowly targeted designs practical. Agent use or a reported speedup alone does not answer that question.

We connect three kinds of evidence:

- **Engines:** the execution decisions they control, the components they reuse and the compatibility they give up.
- **Construction methods:** direct implementation, substantial forks, model-to-program compilation and agent workflows, with the actual scope of their outputs.
- **Validation methods:** numerical, state, output-quality and service checks, including their coverage, cost and failure limits.

[Benchmarks](docs/benchmarks.md) provide separate tasks and comparison protocols. [Diagnostics, construction knowledge and reusable components](docs/resources.md) support this work when their relationship to an engine or construction workflow is explicit.

![Three connected subjects: specialized inference engines, construction methods and validation methods; benchmarks supply evaluation protocols, while diagnostics, knowledge and components provide support](assets/specialization.svg)

## Explore the collection

<!-- CATALOG-START -->

### Specialized inference engines

Start with how execution is rebuilt, then filter by model, device and mechanism. These are entry points into the full engine index and case analyses.

| Execution-stack reading route | Selected cases |
| --- | --- |
| Native runtimes for qualified models and devices | [Splash](docs/cases.md#splash) · [Gufo](docs/cases.md#gufo) · [NInfer](docs/cases.md#ninfer) |
| Rebuilding around memory and expert placement | [Flash-MoE](docs/cases.md#flash-moe) · [Strata](docs/cases.md#strata) · [Swiftlet](docs/cases.md#swiftlet) |
| Substantial forks and specialized backends | [llamAmpere](docs/cases.md#llamampere) · [vLLM Radiance](docs/cases.md#vllm-radiance) · [ANEMLL Flash llama.cpp](docs/cases.md#anemll-flash-llama) |
| Reconstructing image-generation pipelines | [Iris](docs/cases.md#iris) · [stable-diffusion.cpp](docs/cases.md#stable-diffusion-cpp) · [Nunchaku](docs/cases.md#nunchaku) |
| Video execution, device migration and streaming | [LightX2V](docs/cases.md#lightx2v) · [Vidax](docs/cases.md#vidax) · [TeleFuser](docs/cases.md#telefuser) |
| Speech, audio diffusion and action-model runtimes | [Aria](docs/cases.md#aria) · [Qwen-ASR](docs/cases.md#qwen-asr-c) · [vla.simd](docs/cases.md#vla-simd) |

[All engines](docs/systems.md#system) · [All construction cases](docs/cases.md) · [Compare reconstruction boundaries](docs/comparison.md)

[Multimodal understanding & interaction](docs/domains.md#multimodal) · [Image generation & processing](docs/domains.md#image) · [Video generation & processing](docs/domains.md#video) · [Speech & audio](docs/domains.md#audio) · [Language models](docs/domains.md#text) · [Cross-domain infrastructure](docs/domains.md#general)

### Construction and optimization

Connect each workflow to its output. A kernel, model forward program and complete serving stack have different scopes.

| Workflow | Output scope |
| --- | --- |
| [MetaInfer](docs/catalog.md#metainfer) | Model/server construction; see the linked VibeQwen case |
| [Sol-Engine](docs/catalog.md#sol-engine) | Model-specific video execution and quality-constrained optimization |
| [Mirage Persistent Kernel](docs/catalog.md#mirage) | Compiled task graphs and persistent GPU execution |
| [KernelAgent](docs/catalog.md#kernelagent) | Generated kernels and recomposed model forward programs |
| [Atrex Kernel Agent (AKA)](docs/catalog.md#atrex-kernel-agent) | Profile-guided kernel construction with acceptance gates |

[All construction workflows](docs/systems.md#construction) · [MetaInfer → VibeQwen case chain](docs/cases.md#vibeqwen)

### Correctness and quality validation

| Contract to check | Method entry point |
| --- | --- |
| Numerics and operator composition | [Reference comparisons and recomposition checks](docs/validation.md#numerical) |
| Model composition and state coverage | [Composed-forward checks and state coverage](docs/validation.md#model-state) |
| Image / video quality | [Perceptual quality and error constraints](docs/validation.md#quality) |
| Service interfaces and function | [Interface tests, judges and coverage limits](docs/validation.md#service) |

A validator can live inside an engine or construction framework; methods are indexed without duplicating repositories. Numerical, perceptual and functional checks are distinct contracts.

### Benchmarks and task suites

| Benchmark | Comparison question |
| --- | --- |
| [FastKernels](docs/benchmarks.md#fastkernels) | Do candidate-kernel gains survive model integration? |
| [Atrex-Bench](docs/benchmarks.md#atrex-bench) | Does a generated operator compile, meet numerical checks and use the target hardware effectively? |
| [KernelBench](docs/benchmarks.md#kernelbench) | How do generated implementations compare with executable references under a stated evaluation protocol? |

Benchmarks supply tasks, references and comparison protocols. Passing operator tasks does not validate a complete engine. [Read evaluation scopes and limits](docs/benchmarks.md).

### Companion resources

| Purpose | Selected resources |
| --- | --- |
| [Performance diagnosis](docs/resources.md#diagnostics) | [ncu-report-skill](docs/catalog.md#ncu-report-skill) |
| [Construction knowledge and experience](docs/resources.md#knowledge) | [KernelWiki](docs/catalog.md#kernelwiki), [Apple Neural Engine Field Guide](docs/catalog.md#ane-field-guide) |
| [General-engine baselines](docs/resources.md#engine-baselines) | [vLLM](docs/catalog.md#vllm), [SGLang](docs/catalog.md#sglang), [TensorRT-LLM](docs/catalog.md#tensorrt-llm), [llama.cpp](docs/catalog.md#llama-cpp) |
| [Compilers and kernel languages](docs/resources.md#compilers) | [Apache TVM](docs/catalog.md#tvm), [NVIDIA TensorRT](docs/catalog.md#tensorrt), [Triton](docs/catalog.md#triton), [TileLang](docs/catalog.md#tilelang) |
| [Reusable execution and model preparation](docs/resources.md#components) | [DeepCompressor](docs/catalog.md#deepcompressor), [QTIP](docs/catalog.md#qtip), [Marlin](docs/catalog.md#marlin), [Flash Linear Attention](docs/catalog.md#flash-linear-attention) |

[Atrex GPU Wiki: optimization traces → reusable experience](docs/resources.md#embedded-knowledge). Each companion resource must identify the construction, validation or comparison it supports.

Current collection: 121 projects and 63 construction cases. Browse by [project role](docs/systems.md), [execution mechanism](docs/catalog.md) or [model domain](docs/domains.md).

<!-- CATALOG-END -->

## Read a case from motivation to evidence

**Why build another path → what it controls → what it reuses or gives up → how it is built → how it is validated and maintained.**

For example, [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) connects a construction workflow with an author-reported engine outcome. [Sol-Engine](docs/cases.md#sol-engine) connects model-specific video optimization with quality checks. A generated kernel, a composed forward pass and a complete inference service are different outputs; a case must identify its boundary.

Use the [case notes](docs/cases.md) and [construction comparison](docs/comparison.md) for this analysis. [Model domains](docs/domains.md) and [execution mechanisms](docs/catalog.md) are secondary, overlapping search dimensions—not the repository's top-level identity.

## What belongs here?

A record must have a **direct, documented relationship to building or validating a specialized execution stack**. We include substantive native engines and backends, construction workflows, relevant validation methods, benchmarks, and supporting resources with an identifiable use in that process.

General engines, compilers and kernel libraries qualify only through a concrete reuse or comparison relationship. A generic inference optimization, a thin wrapper, or a teaching-oriented nano implementation does not qualify by itself. Unrelated entries are removed from the maintained collection rather than retained in a backup directory. See the [classification and inclusion guide](docs/taxonomy.md).

## Evidence and open questions

This is a source-reviewed collection, not an independent performance reproduction. Separate author reports from inspected implementation, and runtime changes from quantization, approximation or changed models. AI participation requires direct disclosure or an inspectable workflow; missing disclosure means unknown. See the [evidence policy](docs/evidence-policy.md) and [latest resource audit](docs/resources-audit-2026-10-12.md).

The [research agenda](docs/research-agenda.md) asks whether construction savings survive verification, integration and maintenance, and what happens when the model, hardware or workload changes. Unknown costs and incomplete coverage remain visible.

[Project records](catalog/projects.csv) and [case records](catalog/cases.json) generate the directories and comparisons. Follow [CONTRIBUTING.md](CONTRIBUTING.md) to maintain them. Metadata, original diagrams, commentary and scripts use the [MIT License](LICENSE); linked projects and models retain their own licenses.
