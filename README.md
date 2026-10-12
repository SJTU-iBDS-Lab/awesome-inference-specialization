# Awesome Inference Specialization

**Find specialized inference engines, understand how they are built, and choose the checks their outputs need.**

[中文](README_CN.md) · [Find engines](docs/systems.md#system) · [Build workflows](docs/systems.md#construction) · [Validate](docs/validation.md) · [Quick comparison](docs/representative-comparison.md) · [Latest updates](docs/updates.md)

Known models, devices and workloads allow different execution stacks. Start with the reading choices below, compare their actual model/device and reuse boundaries, then inspect the upstream implementation. Language, multimodal, image, video and audio workloads are covered.

**Latest, 2026-10-12:** a [12-case comparison](docs/representative-comparison.md) and [cross-case synthesis](docs/synthesis.md) make the existing source reviews easier to use. [What changed and what was checked](docs/updates.md).

## Start here

<!-- CATALOG-START -->

### 12 starting points: what you can learn

Chosen to contrast execution control, reuse, construction routes and validation across engines, compilation and agent workflows. This is a reading route, not a star, speed or maturity ranking.

| Case | Read it to understand |
| --- | --- |
| [MetaInfer → VibeQwen](docs/cases.md#vibeqwen) | Connect an agent workflow to a reported deployed engine |
| [Sol-Engine](docs/cases.md#sol-engine) | See how optimization choices are accepted and composed |
| [Mirage MPK](docs/cases.md#mirage) | Follow an explicit task graph into persistent GPU execution |
| [Splash](docs/cases.md#splash) | Inspect model-shaped kernels, draft execution and serving together |
| [Gufo](docs/cases.md#gufo) | Study a device-focused stack with explicit per-model quality limits |
| [Flash-MoE](docs/cases.md#flash-moe) | Separate SSD streaming from changes to the model computation |
| [llamAmpere](docs/cases.md#llamampere) | See what a deep fork changes and what upstream still supplies |
| [Nunchaku](docs/cases.md#nunchaku) | Trace packed checkpoints into fused diffusion execution |
| [LightX2V](docs/cases.md#lightx2v) | Inspect explicit asynchronous weight-storage contracts |
| [Vidax](docs/cases.md#vidax) | Follow model conversion and numerical debugging across devices |
| [Aria](docs/cases.md#aria) | Read an AI disclosure beside an inspectable parity harness |
| [vla.simd](docs/cases.md#vla-simd) | Distinguish native action inference from robot task success |

[12-case matrix: model/device, artifact, reuse and checks](docs/representative-comparison.md) · [Full comparison](docs/comparison.md) · [All cases](docs/cases.md)

### Continue by task

- **Find an engine:** open [all engines](docs/systems.md#system), then use the model-domain links below.
- **Build or optimize:** the [workflow index](docs/systems.md#construction) distinguishes kernels, model forward programs and full services; [embedded knowledge](docs/resources.md#embedded-knowledge) connects optimization experience to later attempts.
- **Validate results:** [numerics](docs/validation.md#numerical), [model/state](docs/validation.md#model-state), [output quality](docs/validation.md#quality) and [service behavior](docs/validation.md#service) are different contracts; [benchmarks](docs/benchmarks.md) supply tasks and comparison protocols.
- **Find supporting tools:** [diagnostics](docs/resources.md#diagnostics), [construction knowledge](docs/resources.md#knowledge) and [reusable components](docs/resources.md#components).

[Multimodal understanding & interaction](docs/domains.md#multimodal) · [Image generation & processing](docs/domains.md#image) · [Video generation & processing](docs/domains.md#video) · [Speech & audio](docs/domains.md#audio) · [Language models](docs/domains.md#text) · [Cross-domain infrastructure](docs/domains.md#general)

Full collection: 121 projects, 63 construction cases. Browse [execution mechanisms](docs/catalog.md) or read the [cross-case synthesis](docs/synthesis.md).

<!-- CATALOG-END -->

## What belongs here?

A record needs a direct, documented relationship to **building or validating a specialized execution stack**: substantive engines/backends, construction workflows, validation, benchmarks or concrete supporting resources. General engines and libraries need a reuse or comparison relationship; a thin wrapper, generic optimization or teaching-only nano reproduction is insufficient. [Inclusion rules and taxonomy](docs/taxonomy.md).

## Read the evidence

Ask **why another execution path → what it controls → what it reuses or gives up → how it was built → how it is validated and maintained**. A kernel, model forward program and complete service are different artifacts. [Full case notes](docs/cases.md) retain construction, AI participation, cost, validation and maintenance evidence.

This collection reviews public sources; it has not independently reproduced project performance. AI participation requires direct disclosure or an inspectable workflow. Reported speedups and agent use alone do not establish lower lifecycle cost. Keep runtime changes separate from quantization, approximations and changed models. [Evidence policy](docs/evidence-policy.md) · [Research questions](docs/research-agenda.md) · [Resource audit](docs/resources-audit-2026-10-12.md).

<details>
<summary>Visual map of the collection</summary>

![Engines, construction workflows and validation methods; benchmarks and companion resources support their comparison](assets/specialization.svg)

</details>

[Contribute or correct a record](CONTRIBUTING.md). Directories are generated from [projects](catalog/projects.csv), [cases](catalog/cases.json) and [reading selections](catalog/showcase.json). Metadata, original diagrams, commentary and scripts use [MIT](LICENSE); linked projects and models retain their own licenses.
