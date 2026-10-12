# Awesome Inference Specialization

**A map of how inference systems specialize computation, memory and execution.**

[中文](README_CN.md) · [All projects](docs/catalog.md) · [Compare](docs/comparison.md) · [Classification](docs/taxonomy.md) · [Survey notes](docs/survey-2026-10-12.md) · [Contribute](CONTRIBUTING.md)

![Eight mechanism families, from data placement to program construction](assets/landscape.svg)

Start with the execution decision: **what is moved, represented, skipped, reused, generated, scheduled or compiled?** Text, image and video are cross-cutting tags. Each record identifies a concrete mechanism, its implementation role, direct sources and an important limitation.

## Explore by mechanism

<!-- CATALOG-START -->

**98 projects · 8 mechanism families · Last source review 2026-10-12**

One primary home per project; modality, artifact type and mechanism tags remain independent. Construction tools support execution rather than being another runtime class.

| Mechanism family | What changes | Start with |
| --- | --- | --- |
| [Data residency & movement (11)](docs/catalog.md#memory) | Place, page, prefetch or offload weights, experts and KV state. | [KTransformers / kt-kernel](docs/catalog.md#ktransformers), [vAttention](docs/catalog.md#vattention), [Mooncake](docs/catalog.md#mooncake) |
| [Numerical representation (9)](docs/catalog.md#precision) | Co-design low-bit formats, layouts and execution kernels. | [ExLlamaV3](docs/catalog.md#exllamav3), [Nunchaku](docs/catalog.md#nunchaku), [T-MAC](docs/catalog.md#t-mac) |
| [Selective computation (8)](docs/catalog.md#selection) | Select neurons, tokens or attention blocks; expose approximation. | [MInference](docs/catalog.md#minference), [SnapKV](docs/catalog.md#snapkv), [Sparse VideoGen](docs/catalog.md#sparse-videogen) |
| [Computation reuse (10)](docs/catalog.md#reuse) | Reuse request prefixes, features or attention across steps. | [LMCache](docs/catalog.md#lmcache), [TeaCache](docs/catalog.md#teacache), [TaylorSeer](docs/catalog.md#taylorseer) |
| [Generation order (5)](docs/catalog.md#decoding) | Draft and verify tokens, or reorganize block generation. | [EAGLE](docs/catalog.md#eagle), [Lookahead Decoding](docs/catalog.md#lookahead), [Inferix](docs/catalog.md#inferix) |
| [Parallelism & scheduling (12)](docs/catalog.md#serving) | Partition stages, devices and requests around workload constraints. | [DistServe](docs/catalog.md#distserve), [Sarathi-Serve](docs/catalog.md#sarathi-serve), [xDiT](docs/catalog.md#xdit) |
| [Compiled & native execution (32)](docs/catalog.md#execution) | Fuse, lower, specialize and dispatch graphs or native kernels. | [Mirage Persistent Kernel](docs/catalog.md#mirage), [FlashAttention](docs/catalog.md#flash-attention), [MLC LLM](docs/catalog.md#mlc-llm) |
| [Construction & validation tools (11)](docs/catalog.md#construction) | Agents, kernel languages and evaluation infrastructure. | [MetaInfer](docs/catalog.md#metainfer), [Sol-Engine](docs/catalog.md#sol-engine), [KernelBench](docs/catalog.md#kernelbench) |

<!-- CATALOG-END -->

## Three mechanisms, different contracts

![Data movement, state reuse and candidate verification illustrated as distinct execution paths](assets/mechanisms.svg)

- **Place data and compute:** [KTransformers](docs/catalog.md#ktransformers) runs selected MoE work on CPU; [MoE-Infinity](docs/catalog.md#moe-infinity) transfers and caches expert weights. Both address memory limits through different execution decisions.
- **Reuse state:** [LMCache](docs/catalog.md#lmcache) can reuse matching KV prefixes; [TeaCache](docs/catalog.md#teacache) reuses earlier denoising residuals. Their validity conditions differ.
- **Propose and verify:** [EAGLE](docs/catalog.md#eagle) drafts candidate tokens and checks them with the target model. [Medusa](docs/catalog.md#medusa) also uses candidate trees, but training and acceptance modes need separate scrutiny.

See [taxonomy and semantic effects](docs/taxonomy.md) for all eight families and overlapping cases.

## What belongs here?

Include a project when a known constraint changes **execution, data movement, numerical representation, scheduling or program construction**. Full runtimes, backends, kernel libraries, compilers and evaluation tools have distinct roles; none is automatically a higher tier. A focused kernel subsystem can be relevant without being a complete server.

API wrappers, deployment recipes and paper-only performance headlines do not establish a mechanism. Educational engines and [Diffusers](https://github.com/huggingface/diffusers) remain useful context. General engines such as [vLLM](docs/catalog.md#vllm), [SGLang](docs/catalog.md#sglang) and [TensorRT-LLM](docs/catalog.md#tensorrt-llm) are included where a concrete design is documented.

**Evidence boundary:** this is a source-reviewed directory, not a benchmark leaderboard. Publicly visible code does not imply open licensing, correctness or production readiness. Approximation, reduced precision and model changes are stated alongside implementation changes. [Evidence policy →](docs/evidence-policy.md)

## Research and maintenance

Can cheaper construction make deployment-specific systems economical, or will shared runtimes absorb most useful specialization? This remains a research question. Explore the [research agenda](docs/research-agenda.md), [reading list](docs/reading-list.md) and [survey method and corrections](docs/survey-2026-10-12.md).

The [CSV catalog](catalog/projects.csv) is the source of truth for both homepages, the complete catalog and comparison view. Corrections, missing mechanisms and independent negative results are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

Catalog metadata, original diagrams, commentary and scripts use the [MIT License](LICENSE). Linked projects, models and third-party material retain their own licenses.
