# Execution-stack discovery audit · 2026-10-12

## Question and preregistered scope

Which missing projects reconstruct a substantive inference execution path for a specific model, device or workload, and what can their public artifacts establish about how that path was built?

This is a project-oriented discovery audit using backward references and forward adoption/fork tracing, supplemented by independent keyword searches. It adapts the snowball workflow to software repositories; it is not a complete paper citation review and does not guarantee exhaustive coverage.

- **Include as core:** an integrated native runtime, substantial specialized fork/backend, or construction workflow tied to a concrete specialized executable. Inspect actual execution ownership and retained components; AI involvement and recent publication are not prerequisites.
- **Include as adjacent:** a relevant earlier or neighboring construction route with a different scope. Preserve the distinction from direct cases of the current phenomenon.
- **Do not add:** teaching-only nano implementations, thin interfaces/installers, unmodified mirrors, repeated model variants in one repository, unsupported performance claims without identifiable artifacts, or generic infrastructure already represented in the catalog.
- **Evidence:** official repositories, design/development documents, source files and author reports; use immutable revisions where practical. Do not infer AI authorship from agent instruction files. Source review does not establish successful builds or independent reproduction.
- **Coverage:** no publication-year or venue cutoff; English and Chinese sources; Apple, NVIDIA, AMD, CPU/edge, model-specialized multimodal systems and construction workflows. Preserve the 102 pre-existing project records.
- **Seeds:** Splash, Gufo, NInfer, Iris, MetaInfer, Mirage and llama.cpp. These span device-specific stacks, multimodal execution, agent/compiler construction and a general-engine reference.
- **Expansion:** trace credited dependencies/references backward and named adopters, substantive forks and comparisons forward. Expand newly admitted projects in both directions; record unavailable links rather than pretending a citation graph is complete.
- **Stopping rule:** continue expansion until the final complete frontier adds zero new eligible projects, or fewer than 5% of newly screened candidates. Report the observed frontier and remaining blind spots, not a claim that no other project exists.

## What changed / 本轮结果

本轮新增 **59 个项目记录**，为 **4 个已收录系统**补充构建分析并调整为核心案例。目录从 102 增至 **161 条**，核心案例从 17 增至 **63 个**。既有 102 条记录全部保留；仓库保持私有。

This is a source-audited expansion, not a speed leaderboard. A project count is not a count of independent inventions: substantial forks retain explicit upstream lineage, and one repository with multiple models is counted once. Case notes connect construction processes with artifacts and do not add another repository count.

**Status:** this bounded update is complete, but the global discovery frontier has **not converged**. Apple and multimodal tracing still exposes candidates requiring source inspection. The originally stated zero/<5% stopping criterion was not reached across all branches; no claim of an exhaustive systematic review is made. Unresolved candidates are retained below rather than silently excluded.

[按模型领域查找 / Model domains](domains.md) · [全部核心案例 / Cases](cases.md) · [构建方式对照 / Comparison](comparison.md) · [Machine-readable audit](../catalog/discovery-2026-10-12.json)

### Additions by reviewed scope / 新增覆盖

Counts overlap because one project can execute several modalities. These tags do not replace construction boundaries. Video generation, restoration and understanding remain distinct in each project description.

| Scope | New project records | New core records |
| --- | ---: | ---: |
| text | 39 | 27 |
| multimodal | 22 | 18 |
| image | 13 | 9 |
| video | 8 | 6 |
| audio | 19 | 14 |
| general | 1 | 0 |

### Why the multimodal routes matter / 多模态部分看什么

- **Vision-language and edge execution:** inspect the visual encoder, embedding insertion, language state and device qualification; Cactus, zLLM and FastFlowLM expose different native/compiled and source/binary boundaries.
- **Image generation:** distinguish a reconstructed conditioning → denoising → VAE pipeline from a single fast kernel or a UI calling an existing engine.
- **Video generation:** inspect temporally persistent state, rolling or block generation, weight residency and distributed execution. Video restoration (for example SeedVR2 in zLLM) is explicitly not labeled video generation.
- **Speech and action:** ASR, TTS, audio diffusion and vision-language-action runtimes illustrate model-specific state and scheduling beyond text token generation.
- **Existing systems revisited:** core status follows the inspected construction boundary, not novelty or release date. Framework reuse does not disqualify a case, but a feature list alone does not qualify it.

### Fork and reuse lineage / 继承与复用关系

| Upstream or retained system | Added case or family | What must be compared |
| --- | --- | --- |
| [NInfer](catalog.md#ninfer) | [NInfer-3090](catalog.md#ninfer-3090), [Infernix](catalog.md#infernix) | Retargeted kernels, state and heterogeneous placement; do not count repeated model/build variants as independent stacks. |
| [Gufo](catalog.md#gufo) | [Gufo RDMA](catalog.md#gufo-rdma) | Two-host tensor parallelism and transport; single-host results do not measure the added path. |
| [llama.cpp](catalog.md#llama-cpp) | [CIRU](catalog.md#ciru-runtime), [Strix fork](catalog.md#strix-llama-cpp), [ANEMLL Flash fork](catalog.md#anemll-flash-llama) | Specialized graph, kernel, format or residency changes over retained general-engine code. |
| [TurboFieldfare](catalog.md#turbo-fieldfare) | [TUFF](catalog.md#tuff) | Additional stateful model paths and qualification, not just a different interface. |
| MLX / MLX-LM | [SwiftLM](catalog.md#swiftlm) | Modified expert streaming and slot synchronization within a retained framework. |
| [vLLM](catalog.md#vllm) | [Radiance](catalog.md#vllm-radiance) | Device-critical backend changes while retaining serving and cache abstractions. |

## Candidate ledger

The audit contains **151 screening/relationship records**. These are not all unique repositories: cross-branch discoveries, upstream relationships and already-included records are retained for provenance. The project CSV is deduplicated. `deferred` means unresolved; it is not an exclusion or a zero-yield proof.

| Branch / round | Candidate | Found from / direction | Decision | Reason and evidence |
| --- | --- | --- | --- | --- |
| apple / 1 | [Lily](https://github.com/perplexityai/pplx-garden/tree/main/lily) | Keyword cross-check from Splash/Apple-Metal engines / keyword | core | A deliberately single-checkpoint execution stack makes the compatibility cost of reconstruction explicit. Greedy, text-only, non-streaming API; unsupported checkpoints and sampling options are rejected. Published comparisons do not establish independent reproduction. [1](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/README.md) [2](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/src/config.rs) [3](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/src/model.rs) [4](https://github.com/perplexityai/pplx-garden/blob/1ed972ed3f0bd5616c997c9507c25616c63394fc/lily/CONTRIBUTING.md) |
| apple / 1 | [Lithos Metal](https://github.com/lithos-ai/lithos-metal) | Keyword cross-check from Splash/Apple-Metal engines / keyword | core | Connects a graph compiler and chip-specific recipes to a concrete standalone inference runtime. Some chip backends are unmeasured, hybrid MoE integration is experimental, and default normalization fusion changes BF16 rounding; target-compute projections exclude draft and verification overhead. [1](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/README.md) [2](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/docs/design/design.md) [3](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/docs/design/extensions.md) [4](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/monolith/runtime/engine.py) [5](https://github.com/lithos-ai/lithos-metal/blob/08d9d53067eab538e3ad8435a6a5b50b80088554/CONTRIBUTING.md) |
| apple / 1 | [Saragossa](https://github.com/azerozero/saragossa) | Keyword cross-check for native Apple engines / keyword | core | Replaces array-framework execution with an explicitly owned local runtime and regression oracles. Model and precision coverage is explicit; the single-user serving design and configuration-dependent KV precision do not imply general multi-tenant performance. [1](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/README.md) [2](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/decode_resident.rs) [3](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/decode_resident/attention.rs) [4](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/src/runtime_flags.rs) [5](https://github.com/azerozero/saragossa/blob/57f409b76925dfa810b279a128f4028704299cae/tests/golden/README.md) |
| apple / 2 | [TurboFieldfare](https://github.com/drumih/turbo-fieldfare) | TUFF README explicitly credits the original fork source / backward | core | A single-model native runtime publishes a detailed sequence of accepted and rejected construction experiments. Research system with a narrow architecture contract; reported footprint excludes the full disk checkpoint and throughput depends on cache warmth, context and hardware. [1](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/README.md) [2](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/SYSTEM_DESIGN.md) [3](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/OPTIMIZATION_JOURNEY.md) [4](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/experiments/EXPERIMENT_INVENTORY.md) [5](https://github.com/drumih/turbo-fieldfare/blob/77e8f9c02ec5345f4d9b633961c938bbafefb757/docs/IMPLEMENTATION_REFERENCES.md) |
| apple / 1 | [TUFF](https://github.com/rexmhall09/TUFF) | Keyword cross-check for native Apple engines / keyword | core | A disclosed substantial fork shows how a narrow streaming runtime is adapted into several qualified model paths. Author testing centers on a 16 GB M2; model capability, vision support and performance differ by machine. A UI feature comparison is not a speed benchmark. [1](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/README.md) [2](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/CONTRIBUTING.md) [3](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/docs/HOW_TUFF_WORKS.md) [4](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/Sources/TUFFEngine/Infrastructure/Streaming/PreadExpertStreamer.swift) [5](https://github.com/rexmhall09/TUFF/blob/0dd6dd7bacbd335edf59a5c46e06f3cc2da0de71/Sources/TUFFEngine/Runtime/Inference/RealForwardRunner.swift) |
| apple / 2 | [Colibri](https://github.com/JustVugg/colibri) | TUFF README names Colibri in its feature comparison / comparison | core | Exposes the alternative of several small architecture-specific execution programs sharing selected components. Backend maturity, numerical formats and speculative/approximate options vary per engine; synthetic oracle agreement does not establish every advertised model/backend combination. [1](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/README.md) [2](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/c/qwen36.c) [3](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/docs/qwen36.md) [4](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/CONTRIBUTING.md) [5](https://github.com/JustVugg/colibri/blob/bf2442915d6e3dd4cdfd2eb9c2a3d2aa44a25850/THIRD_PARTY_NOTICES.md) |
| apple / 1 | [ane.cpp](https://github.com/skyfallsin/ane.cpp) | Independent ANE runtime search / keyword | core | Connects hardware probes and a documented keep/discard workflow to concrete changes in a specialized execution stack. Private APIs can change; tested ANE paths do not move every operator off CPU, and measured speculative variants have been slower than baseline. [1](https://github.com/skyfallsin/ane.cpp/blob/b87bf57356c26025853a60cddfe4b58784ee4fda/README.md) [2](https://github.com/skyfallsin/ane.cpp/blob/b87bf57356c26025853a60cddfe4b58784ee4fda/core/ane_runtime.cpp) [3](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/README.md) [4](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/program.md) [5](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/83e73eb94051dc67431829d0f3d3eb67db0b8e9b/results.tsv) |
| apple / 3 | [Swiftlet](https://github.com/leonickson1/Swiftlet) | Colibri THIRD_PARTY_NOTICES documents adapted Swiftlet kernels and format / backward | core | Links explicit AI-assisted authorship to a model-family-specific runtime and documented reference-based validation. The public roadmap notes expensive long-prompt prefill and limited phone throughput; quantization tiers have different quality behavior. [1](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/README.md) [2](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Sources/SwiftletCore/ExpertCache.swift) [3](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Sources/SwiftletCore/QwenCPUModel.swift) [4](https://github.com/leonickson1/Swiftlet/blob/de1a942241f65ac43290cecffc85d69ea5b52310/Tests/SwiftletCoreTests/IncrementalDecodeTests.swift) |
| apple / 3 | [SwiftLM](https://github.com/SharpAI/SwiftLM) | TurboFieldfare implementation-reference ledger credits SSD-streaming design / backward | core | Shows substantial backend reconstruction while retaining the MLX ecosystem and serving integration. Streaming and speculative verification can multiply I/O; upstream synchronization broke quantized streaming in earlier releases, and fixed-version results must not be generalized. [1](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/README.md) [2](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/Package.swift) [3](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/docs/moe_ssd_streaming_architecture.md) [4](https://github.com/SharpAI/SwiftLM/blob/b1ae6cc44e308986d8a10638d9a0410cd039b876/Sources/MLXInferenceCore/SSDStreamingRecovery.swift) [5](https://github.com/SharpAI/mlx-swift-lm/blob/4f1fdaabeb490d3e97b0ff71fc0132bca4078fa2/Libraries/MLXLMCommon/SwitchLayers.swift) |
| apple / 3 | [ANEMLL Flash llama.cpp](https://github.com/Anemll/anemll-flash-llama.cpp) | ANEMLL official organization lists the slot-bank llama.cpp fork / forward | core | A substantial fork exposes exactly which graph/runtime boundary must change to support explicit expert residency. Model maturity varies; optional top-k reductions and shared-only diagnostics change computation and must not be compared as exact execution. [1](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/README.md) [2](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/src/llama-context.cpp) [3](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/native-slot-bank-porting.md) [4](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/flashmoe-layer-major-dedup-single-sidecar.md) [5](https://github.com/Anemll/anemll-flash-llama.cpp/blob/a809594fd2035979ad2b7ef23398127c1d07e891/docs/moe-bank-modeling-workflow.md) |
| apple / 1 | [Uzu](https://github.com/trymirai/uzu) | Keyword cross-check for native Apple engines / keyword | adjacent | A broader on-device engine and model-conversion ecosystem provides a reference for reusable native construction. Its broad SDK scope differs from a single deployment-specific case; source inspection does not establish performance or AI authorship. [1](https://github.com/trymirai/uzu/blob/bd374af567221e281538de47987ce35429f91376/README.md) [2](https://github.com/trymirai/uzu/blob/bd374af567221e281538de47987ce35429f91376/crates/uzu-engine/src/encodable_block/decoder.rs) [3](https://github.com/trymirai/uzu/blob/bd374af567221e281538de47987ce35429f91376/crates/uzu-engine/build/metal/bindgen/specialize.rs) [4](https://github.com/trymirai/lalamo/blob/831accb8252a6b6606c378048caeb44178f1a050/README.md) |
| apple / 1 | [PMetal](https://github.com/Epistates/pmetal) | Keyword cross-check for native Apple engines / keyword | adjacent | A training-and-inference platform is an adjacent route for studying when specialized paths live inside a reusable ecosystem. The inspection covers a Qwen native forward path and cached-decode tests, not every advertised model or ANE capability. [1](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/README.md) [2](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/CONTRIBUTING.md) [3](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/crates/pmetal-bridge/src/qwen3_native/forward.rs) [4](https://github.com/Epistates/pmetal/blob/b469853656d3587dfb84ba083d8cca59c77dad7d/crates/pmetal-models/tests/cached_decode.rs) |
| apple / 1 | [MetalChat](https://github.com/ybubnov/metalchat) | Keyword cross-check for native Apple engines / keyword | adjacent | An adjacent native framework illustrates reusable model abstractions rather than a narrowly documented reconstruction experiment. The API is explicitly unstable and the inspected integration test demonstrates generation without a comprehensive quality gate. [1](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/README.md) [2](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/src/gemma.cc) [3](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/test/test_gemma.cc) [4](https://github.com/ybubnov/metalchat/blob/be9f19a7cdc9559f3f814ad25a1ce77f7e7cc466/documentation/guides/getting_started.rst) |
| apple / 1 | [BaseRT](https://github.com/basecompute/baseRT) | Keyword cross-check for native Metal engines / keyword | adjacent | Provides a contrasting delivery model: public format/conversion tooling around a closed specialized engine. The execution core is not in the public repository; kernel mechanisms and performance rely on author documentation rather than source verification. [1](https://github.com/basecompute/baseRT/blob/24badc8dd173e4111b64996a718d0e056405ea62/README.md) [2](https://github.com/basecompute/baseRT/blob/24badc8dd173e4111b64996a718d0e056405ea62/CONTRIBUTING.md) [3](https://github.com/basecompute/baseRT/blob/24badc8dd173e4111b64996a718d0e056405ea62/base-convert/FORMAT.md) |
| apple / 1 | [ANEMLL](https://github.com/Anemll/Anemll) | Independent ANE runtime search / keyword | adjacent | An existing converter-plus-runtime route helps distinguish compiler-mediated specialization from direct native reconstruction. CoreML chooses actual placement; unsupported operators, OS versions, package sizing and quantization require target-specific verification. [1](https://github.com/Anemll/Anemll/blob/f4ad26d061dc2e426faa19f81c367343bdeb9f0d/README.md) [2](https://github.com/Anemll/Anemll/blob/f4ad26d061dc2e426faa19f81c367343bdeb9f0d/docs/ANE_converter.md) [3](https://github.com/Anemll/Anemll/blob/f4ad26d061dc2e426faa19f81c367343bdeb9f0d/anemll/ane_converter/llama_converter.py) |
| apple / 2 | [ANE-LM](https://github.com/johnmai-dev/ANE-LM) | ane.cpp README explicitly identifies its upstream / backward | adjacent | The direct precursor of ane.cpp anchors what the later measurement-driven fork actually changed. Private API dependence and narrow model support limit portability; public generation examples do not establish broad quality qualification. [1](https://github.com/johnmai-dev/ANE-LM/blob/04b1af12aa30b3f280f511d286398469764b4326/README.md) [2](https://github.com/johnmai-dev/ANE-LM/blob/04b1af12aa30b3f280f511d286398469764b4326/models/llm/qwen3.cpp) [3](https://github.com/johnmai-dev/ANE-LM/blob/04b1af12aa30b3f280f511d286398469764b4326/core/ane_runtime.cpp) |
| apple / 2 | [CoreML LLM CLI](https://github.com/smpanaro/coreml-llm-cli) | ANEMLL README credits CoreML LLM CLI / backward | adjacent | A cited predecessor of ANEMLL makes earlier compiled-model and host-runtime specialization visible. Demonstration-focused scope with a small model/device matrix; the compiled model and runtime must be evaluated together. [1](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/README.md) [2](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/Sources/Kit/ModelPipeline.swift) [3](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/Sources/Kit/KVCacheProcessor.swift) [4](https://github.com/smpanaro/coreml-llm-cli/blob/9d141fc6a5182c0ce8befb2711284205cc928e10/Sources/Kit/MultiArrayStore.swift) |
| apple / 1 | [Splash](https://github.com/incoai/splash) | Seed / seed | already-included | Retained seed; model-specific runtime already present. [1](https://github.com/incoai/splash) |
| apple / 1 | [Iris](https://github.com/antirez/iris.c) | Seed / seed | already-included | Retained image runtime seed; its cited FLUX implementation is model/reference material, not another engine. [1](https://github.com/antirez/iris.c) |
| apple / 1 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Seed and cited execution reference / backward | already-included | Shared general-engine reference already present. [1](https://github.com/ggml-org/llama.cpp) |
| apple / 1 | [Lily Engine fork](https://github.com/RavenXAILabs/lily-engine) | Apple Metal engine query / keyword | deferred | Claims model-agnostic generalization but carries upstream Lily benchmark numbers; distinct supported paths and validation were not sufficiently established in this audit. [1](https://github.com/RavenXAILabs/lily-engine) |
| apple / 2 | [Lalamo](https://github.com/trymirai/lalamo) | Uzu README model-format exporter / backward | excluded | Recorded as Uzu construction evidence; model adaptation tooling is not counted again as a separate specialized execution stack. [1](https://github.com/trymirai/lalamo) |
| apple / 2 | [Anemll Server](https://github.com/alexgusevski/anemll-server) | ANEMLL README named adopter / forward | excluded | API wrapper around included ANEMLL inference; no substantial new execution ownership established. [1](https://github.com/alexgusevski/anemll-server) |
| apple / 2 | [ANE](https://github.com/maderix/ANE) | ane.cpp and ANE-LM acknowledgments / backward | deferred | Training/reverse-engineering dependency; checkout encountered missing git-lfs. No execution-stack record is inferred from incomplete inspection. [1](https://github.com/maderix/ANE) |
| apple / 2 | [ANE field guide](https://github.com/skyfallsin/apple-neural-engine-field-guide) | ane.cpp companion research project / backward | excluded | Probes and autonomous-workflow record linked directly to the ane.cpp case, not counted as another runtime. [1](https://github.com/skyfallsin/apple-neural-engine-field-guide) |
| apple / 2 | [BaseRT 4D component](https://github.com/miyako/BaseRT) | BaseRT forward search / forward | excluded | Lifecycle and launcher integration around BaseRT, without another substantive execution path. [1](https://github.com/miyako/BaseRT) |
| apple / 2 | [BaseRT mirror fork](https://github.com/hunter-arton/basert) | BaseRT forward search / forward | excluded | No independent runtime contribution established; canonical BaseRT is used. [1](https://github.com/hunter-arton/basert) |
| apple / 3 | [Flash-MoE](https://github.com/danveloper/flash-moe) | TurboFieldfare implementation references / backward | already-included | Native streaming seed already included. [1](https://github.com/danveloper/flash-moe) |
| apple / 3 | [ANEMLL Flash-MoE fork](https://github.com/Anemll/flash-moe) | TurboFieldfare implementation references / backward | deferred | Quantized kernels and I/O fanout are substantive modifications; distinction from the existing Flash-MoE case needs a dedicated lineage and validation audit before separate counting. [1](https://github.com/Anemll/flash-moe) |
| apple / 3 | [MLX](https://github.com/ml-explore/mlx) | Uzu/Swiftlet/SwiftLM/TurboFieldfare references / backward | excluded | Shared framework dependency recorded in case reuse fields; this branch of the audit focuses additions on execution systems rather than expanding every foundation. [1](https://github.com/ml-explore/mlx) |
| apple / 3 | [vLLM Metal](https://github.com/vllm-project/vllm-metal) | TurboFieldfare kernel-reference ledger / backward | deferred | Reusable backend named as a reference; no separate construction-boundary audit performed. [1](https://github.com/vllm-project/vllm-metal) |
| apple / 3 | [Colibri Qwen fork](https://github.com/czemar/colibri-qwen3.6-35B-A3B) | Colibri forward fork search / forward | excluded | Qwen model-family variant overlaps the canonical Colibri Qwen path; distinct current execution contribution not established. [1](https://github.com/czemar/colibri-qwen3.6-35B-A3B) |
| apple / 3 | [TurboFieldfare uncensored fork](https://github.com/Lookoff-AIMLAPI/turbo-fieldfare-uncensored) | TurboFieldfare forward fork search / forward | excluded | Model-policy variant does not by itself establish a distinct execution-stack construction case. [1](https://github.com/Lookoff-AIMLAPI/turbo-fieldfare-uncensored) |
| apple / 4 | [Priv AI application](https://github.com/leonickson1/localLLM) | Swiftlet README names embedding app / forward | excluded | Deployment adopter of the same SwiftletCore runtime, not another engine. [1](https://github.com/leonickson1/localLLM) |
| apple / 4 | [Retort](https://github.com/adrianco/retort) | Swiftlet forward search; docs/future-experiments.md / forward | excluded | Backend integration/benchmark setup; its own note separates built adapter from an unperformed smoke test. [1](https://github.com/adrianco/retort) |
| apple / 4 | [Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | SwiftLM adoption discussion #1150 / forward | deferred | Maintainer reports model-limited disk streaming; the implementation and current repository identity require source verification before inclusion. [1](https://github.com/raullenchai/Rapid-MLX) |
| apple / 4 | [Melix](https://github.com/Keith-CY/melix) | SwiftLM reference issue #1394 / forward | deferred | Issue proposes explicit SSD streaming; an issue alone is not evidence of a completed execution subsystem. [1](https://github.com/Keith-CY/melix) |
| apple / 4 | [Crossfire](https://github.com/Murai-Labs/Crossfire) | ANEMLL Flash llama.cpp forward reference search / forward | deferred | Search exposed a staged experiment plan; completed multi-device integration and validation were not established. [1](https://github.com/Murai-Labs/Crossfire) |
| apple / 4 | [Hypura](https://github.com/t8/hypura) | scasella/gemma4-m4-pro references Hypura and ANEMLL Flash llama.cpp / backward | deferred | Strong candidate: custom GGML NVMe buffer and tier placement are documented, but source/quality audit remains incomplete. [1](https://github.com/t8/hypura) |
| apple / 4 | [Gemma4 M4 Pro tuning](https://github.com/scasella/gemma4-m4-pro) | ANEMLL Flash llama.cpp forward search / forward | deferred | Reproducible tuning/workflow candidate; requires checking whether changes exceed configuration and measurement of Hypura. [1](https://github.com/scasella/gemma4-m4-pro) |
| apple / 4 | [Rustane](https://github.com/ncdrone/rustane) | ANEMLL Flash-MoE credits page-aligned pread fanout / backward | deferred | Training-focused ANE/Metal engine now documents checkpoint inference; contradictory planned/current status in README requires actual path verification. [1](https://github.com/ncdrone/rustane) |
| apple / 4 | [rapidAI](https://github.com/muharremyurtsever/rapidAI) | Independent disk-stream search during final frontier / keyword | deferred | Disk-backed MoE implementation and measurement archive appear relevant; not fully source-audited in this round. [1](https://github.com/muharremyurtsever/rapidAI) |
| apple / 4 | [LlamaOnDisk](https://github.com/DumbGreenFish/LlamaOnDisk) | Independent disk-stream search during final frontier / keyword | deferred | llama.cpp expert-streaming derivative; substantive delta and parity evidence need inspection. [1](https://github.com/DumbGreenFish/LlamaOnDisk) |
| apple / 4 | [Hipfire](https://github.com/warpfront/hipfire) | Rustane search exposed credited architecture transfer / forward | deferred | Cross-device candidate relayed to the GPU branch of the audit; no duplicate Apple record created. [1](https://github.com/warpfront/hipfire) |
| apple / 1 | [NPUMoE](https://arxiv.org/abs/2604.18788) | Independent ANE runtime search / keyword | deferred | Paper describes static expert tiers and ANE offload, but a source artifact was not located and the full paper was not audited; abstract claims alone are insufficient. [1](https://arxiv.org/abs/2604.18788) |
| gpu / 1 | [hipEngine](https://github.com/shisa-ai/hipEngine) | gufo README Reference Projects / backward | core | Native AMD reconstruction with explicit model/device qualification; Gufo cites this runtime as a design reference. [1](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/README.md) [2](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/hipengine/runtime/qwen35_gguf_runner.py) [3](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/hipengine/generation/batch_scheduler.py) [4](https://github.com/shisa-ai/hipEngine/blob/3621f3a672f9a151f36a02ad2aea7e2049323054/docs/RDNA3-TUNING-GUIDE.md) |
| gpu / 1 | [VTE](https://github.com/kyuubyN/VTE) | independent AMD from-scratch runtime search / keyword | core | Integrated consumer-GPU runtime with public profiling and bug-history evidence explaining why it was rebuilt. [1](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/README.md) [2](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/docs/ARCHITECTURE.md) [3](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/docs/PERFORMANCE.md) [4](https://github.com/kyuubyN/VTE/blob/07e1396f6e071698171e285cc03d1ca29cd62220/vte/core/model.py) |
| gpu / 1 | [ZINC](https://github.com/zolotukhin/zinc) | independent keyword search / keyword | core | Consumer-hardware execution-stack reconstruction with inspectable native model paths and backend-specific measurements. [1](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/README.md) [2](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/src/compute/forward.zig) [3](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/src/rocm/rocm_shim.c) [4](https://github.com/zolotukhin/zinc/blob/29bc350ac4cbf9f110ec628b9e177ea04ac816fb/docs/DEVELOPMENT.md) |
| gpu / 1 | [imp](https://github.com/kekzl/imp) | independent keyword search / keyword | core | Explicit single-architecture reconstruction plus a direct author disclosure of end-to-end coding-agent implementation. [1](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/README.md) [2](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/CONTRIBUTING.md) [3](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/src/runtime/engine.cpp) [4](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/src/runtime/engine_scheduler.cpp) [5](https://github.com/kekzl/imp/blob/e583b0ac6f181d760b62cfd20fecd51d013656ad/docs/MISSION_JOURNAL.md) |
| gpu / 1 | [memra](https://github.com/avifenesh/memra) | independent keyword search / keyword | core | Native runtime with per-model/device exactness gates and explicit evidence of the maintenance and qualification burden. [1](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/README.md) [2](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/ARCHITECTURE.md) [3](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/crates/memra-engine/src/forward.rs) [4](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/crates/memra-engine/THIRD-PARTY.md) [5](https://github.com/avifenesh/memra/blob/89b749cae9f32b286358b6ce09170408027f13ab/docs/TESTING.md) |
| gpu / 1 | [Kipp](https://github.com/Polished-Snow/Kipp) | independent keyword search / keyword | core | Model-family reconstruction with explicit checkpoint rejection and native serving, beyond a teaching-only forward-pass example. [1](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/README.md) [2](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/docs/ARCHITECTURE.md) [3](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/docs/ROADMAP.md) [4](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/src/kipp.c) [5](https://github.com/Polished-Snow/Kipp/blob/0b8c1246d756ae72031eb71e1b2b86309a969ed4/src/cuda/kipp_cuda.cu) |
| gpu / 1 | [vLLM Radiance](https://github.com/magiccodingman/vllm-radiance) | independent keyword search / keyword | core | Substantial specialized backend/distribution: preserves vLLM services while replacing device-critical execution and explicitly managing upstream patch dependencies. [1](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/README.md) [2](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/radiance_r4d_attn.py) [3](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/radiance_mxfp4.py) [4](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/docs/maintenance/ARCHITECTURE.md) [5](https://github.com/magiccodingman/vllm-radiance/blob/d5c07c52d2121901654b203da3e44553172a1a46/docs/NUMERICAL_CORRECTIONS.md) |
| gpu / 2 | [NInfer-3090](https://github.com/ashalliants/ninfer-3090) | NInfer forward port search → Don-Chad/ninfer-3090 → ashalliants continuation / forward | core | Concrete retargeting case: kernel and memory-program changes beyond changing a CUDA architecture flag; one representative records the 3090 fork family. [1](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/README.md) [2](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/src/ops/linear/ggml/ggml_mmq.cuh) [3](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/src/models/qwen3_5/program/transactions/replay.cpp) [4](https://github.com/ashalliants/ninfer-3090/blob/62545c49f8c7c81729cc20e01495c3e3cd917a9c/RELEASE_NOTES_0.11.0.md) |
| gpu / 2 | [Infernix](https://github.com/wallawalla47/infernix) | NInfer-3090 README upstream/adapted-source credit; also forward Strata comparison / backward | core | Substantial descendant reconstructing heterogeneous execution for a model too large for GPU memory, with direct AI-development disclosure. [1](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/README.md) [2](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/src/ops/offloaded_sparse_moe/cpu/miss_service.cpp) [3](https://github.com/wallawalla47/infernix/blob/bbc2771c4b79ba70b8f61f7002ba490c4e77e853/src/models/qwen4_exp/execution/expert_stream.cpp) |
| gpu / 2 | [CIRU runtime](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4) | Gufo/hipEngine Strix ecosystem follow-up; Halogen/pwilkin reference integration / forward | core | Model/hardware-specific deep integration with traceable borrowed kernels, artifact compatibility work and release qualification. [1](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/README.md) [2](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/docs/PROVENANCE.md) [3](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/ggml/src/ggml-cuda/qsa.cu) [4](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4/blob/bac7ad8c314bcc59505a3b76f0b18ad4618557ea/docs/QSA_BACKPORT_STATUS.md) |
| gpu / 2 | [Gufo RDMA](https://github.com/neuhaus/gufo) | gufo README named RDMA variant / forward | core | Substantive deployment reconstruction from one unified-memory machine to two synchronized hosts, not merely another binary package. [1](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/README.md) [2](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/docs/models/qwen3.8-flash-next/TP2.md) [3](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/src/models/qwen38_flash_next/distributed/tp_partition.cpp) [4](https://github.com/neuhaus/gufo/blob/2accddbb01bb6cc97df2938d7715d29fa5a13484/src/cli/serve/tp_executor.cpp) |
| gpu / 2 | [Llaminar](https://github.com/Llaminar/llaminar) | independent SM86/ROCm native-engine search / keyword | core | Native mixed-hardware construction route: owns model graphs, execution plans and cross-vendor coordination rather than wrapping existing engines. [1](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/README.md) [2](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/execution/local_execution/engine/ForwardExecutionEngine.cpp) [3](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/collective/backends/HeterogeneousBackend.cpp) [4](https://github.com/Llaminar/llaminar/blob/454741b1b2228bc6874e46ade75bbf523a8385d5/src/v2/planning/AutomaticOrchestrationPlanner.cpp) |
| gpu / 2 | [strix-llama.cpp](https://github.com/halo-box/strix-llama.cpp) | Gufo credited Strix forks → community consolidation named in Lemonade discussion 3585 / forward | core | Hardware-specialized fork with substantial kernel/state changes and a documented upstream/staging boundary; represents the overlapping Strix llama.cpp fork family. [1](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/README.md) [2](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/ggml/src/ggml-cuda/gated_delta_net.cu) [3](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/ggml/src/ggml-vulkan/ggml-vulkan.cpp) [4](https://github.com/halo-box/strix-llama.cpp/blob/6aa81b88e14aa753c1c7e1a9ff27c9d50fd3c673/CONTRIBUTING.md) |
| gpu / 2 | [ROCmFPX](https://github.com/ROCmFPX/ROCmFPX) | hipEngine external survey → q38rocm; halo-box credited ROCmFPX / backward | adjacent | Adjacent format/backend construction route used by specialized Strix forks; separate from a new complete model execution stack. [1](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/README.md) [2](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/docs/rocmfpx/README.md) [3](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/ggml/rocmfpx/rocmfpx_mmq_rdna3.cuh) [4](https://github.com/ROCmFPX/ROCmFPX/blob/c4aa38b1987ee9cd390f56fb393ba93ac472769b/docs/rocmfpx/UPSTREAM-MAINTENANCE.md) |
| gpu / 2 | [HybriMoE](https://github.com/PKU-SEC-Lab/HybriMoE) | Colibri README references supplied by Apple survey; KTransformers lineage / backward | adjacent | Historical/adjacent heterogeneous MoE route directly referenced by newer native systems; establishes prior art for expert placement and movement. [1](https://github.com/PKU-SEC-Lab/HybriMoE/blob/508a85b9a43dff37124370d8816e411e74827803/README.md) [2](https://github.com/PKU-SEC-Lab/HybriMoE/blob/508a85b9a43dff37124370d8816e411e74827803/ktransformers/operators/experts.py) [3](https://github.com/PKU-SEC-Lab/HybriMoE/blob/508a85b9a43dff37124370d8816e411e74827803/ktransformers/ktransformers_ext/operators/llamafile/moe.cpp) |
| gpu / 1 | [Gufo](https://github.com/gufo-org/gufo) | seed / seed | already-included | Existing core seed; followed named origins and Windows/RDMA descendants. [1](https://github.com/gufo-org/gufo/blob/956f3d62386a80d327aea9610310fef105c31b95/README.md) |
| gpu / 1 | [NInfer](https://github.com/Neroued/ninfer) | seed / seed | already-included | Existing core seed; traced nontrivial retargeting and derivative systems. [1](https://github.com/Neroued/ninfer/blob/81c8ce093b2c1646a87566a8e59d807fcf0ec95c/README.md) |
| gpu / 1 | [Strata](https://github.com/Niko1221/Strata) | seed / seed | already-included | Existing core seed; new Infernix comparison closes a forward relation. [1](https://github.com/Niko1221/Strata/blob/7695859aa13afb248bdb4d36f9b2e95707db079d/README.md) |
| gpu / 1 | [llamAmpere](https://github.com/JakeATX/llamAmpere) | seed / seed | already-included | Existing SM86 core seed; the older llama-cpp-qwen-ampere name is not another case. [1](https://github.com/JakeATX/llamAmpere/blob/3e670a8ecfc3d6f2c382e038180a0029eb47a8be/README.md) |
| gpu / 1 | [Zynfer](https://github.com/SinAnima/zynfer) | NInfer inspiration cited in README / forward | deferred | Intended RDNA4 target is waiting for hardware; current staged/educational implementation is mainly Metal. Defer until deployment and AMD execution boundary can be qualified. [1](https://github.com/SinAnima/zynfer/blob/77cc6067f4d1006a97a36d19c562a2d4132c733d/README.md) |
| gpu / 1 | [NInfer Studio](https://github.com/giveen/ninfer-studio) | NInfer forward search / forward | excluded | Desktop control plane; explicitly launches a separately supplied ninfer-serve engine. [1](https://github.com/giveen/ninfer-studio) |
| gpu / 1 | [qwen600 ROCm](https://github.com/Ramshankar07/qwen600-ROCm-inference) | AMD from-scratch keyword search / keyword | excluded | Explicit educational CUDA exercise with HIP performance still pending; teaching-only implementation is outside the collection boundary. [1](https://github.com/Ramshankar07/qwen600-ROCm-inference) |
| gpu / 1 | [inferd](https://github.com/likhith-v1/inferd) | RTX5090 from-scratch keyword search / keyword | deferred | Paused pre-release stack; README identifies persistent paged KV in live decode and fused paged attention as unfinished. Revisit when execution ownership and integrated serving path are clearer. [1](https://github.com/likhith-v1/inferd/blob/929472b4598d225acc6149f10607dba9a6d450a6/README.md) |
| gpu / 1 | [InferSpore](https://github.com/m0dulo/InferSpore) | CUDA inference-engine topic search / keyword | deferred | Public code but minimal one-sentence documentation; intended specialization, construction motive and validation boundary cannot be established reliably. [1](https://github.com/m0dulo/InferSpore/blob/6f8b7e7979a3a130ef38ca3364afd973c37e1079/README.md) |
| gpu / 2 | [Gufo Windows port](https://github.com/pixmaate/gufo) | Gufo named variant / forward | excluded | Platform port in the same engine family; no separate execution mechanism established beyond the represented Gufo case. [1](https://github.com/pixmaate/gufo/blob/2eb0778ac15d9e1c18c5b2f9e5dbbecc19e20ec2/README.md) |
| gpu / 2 | [NInfer-3090 original port](https://github.com/Don-Chad/ninfer-3090) | NInfer forward search / forward | excluded | Retain lineage credit within one NInfer-3090 family record; the selected continuation includes later SM86 kernel and state work, so avoid duplicating the same port. [1](https://github.com/Don-Chad/ninfer-3090/blob/d7277e88cc3a56d2967d5d533f148bed36e97df5/README.md) |
| gpu / 2 | [q38rocm](https://github.com/julianmb/q38rocm) | hipEngine external Strix survey / backward | excluded | Model-specific recipes, measurements and delivery over ROCmFPX; original execution family is recorded instead of treating every checkpoint bundle as another engine. [1](https://github.com/julianmb/q38rocm/blob/1d88ab50a5c00221a153f459f7af3eb15eb3af74/README.md) |
| gpu / 2 | [Nathan Strix toolbox](https://github.com/Nathanw1014/strix-halo-llamacpp) | Gufo Reference Projects / backward | excluded | Substantive older kernel patches acknowledged, but record the consolidated halo-box fork as representative rather than duplicating overlapping Strix variants. [1](https://github.com/Nathanw1014/strix-halo-llamacpp/blob/84036cc8b7536eb67bb3f1f60f5a955dab322872/README.md) |
| gpu / 2 | [Gaetan Strix fork](https://github.com/gaetan-puleo/llama-cpp-strix-halo) | Gufo Reference Projects / backward | deferred | Fetched source retains generic upstream README; distinct current execution boundary and incremental contribution not clearly documented in reviewed entry points. [1](https://github.com/gaetan-puleo/llama-cpp-strix-halo/blob/860c828363988d3e4b3d5c2b701dcba3d7b9f26c/README.md) |
| gpu / 2 | [Laurent Strix fork](https://github.com/LaurentZuijdwijk/llama.cpp) | Gufo Reference Projects / hipEngine comparison / backward | deferred | Referenced upstream returned 404 during API inspection; keep discovery provenance, do not infer deleted/private status or implementation. [1](https://github.com/LaurentZuijdwijk/llama.cpp) |
| gpu / 2 | [Ciru ROCmFPX](https://github.com/ciru-ai/ROCmFPX) | halo-box imported format attribution / backward | excluded | Related format/runtime research lineage recorded in ROCmFPX and the concrete CIRU runtime case; no extra family count for each release/format branch. [1](https://github.com/ciru-ai/ROCmFPX/blob/efd1ef5a17db576168d849831e1ef3346582881e/README.md) |
| gpu / 3 | [NInfer Jetson Orin port](https://forums.developer.nvidia.com/t/ninfer-jetson-orin-optimized-port-jp6-2-and-jp7-2/384440) | NInfer-3090 forward hardware migration search / forward | deferred | Named SM87 migration discovered through NVIDIA forum; not independently source-audited in this pass and not counted as another variant. [1](https://forums.developer.nvidia.com/t/ninfer-jetson-orin-optimized-port-jp6-2-and-jp7-2/384440) |
| gpu / 3 | [ZINC-X](https://github.com/Maxritz/zinc-x) | ZINC forward fork search / forward | excluded | Fork retains upstream ZINC description and clone instructions; no independently evidenced execution increment was identified. [1](https://github.com/Maxritz/zinc-x) |
| gpu / 3 | [HaloFPX](https://github.com/julianmb/halofpx) | q38rocm named successor / forward | excluded | Model management, presets and server delivery around the already represented ROCmFPX/llama.cpp execution family; no separate native runtime established. [1](https://github.com/julianmb/halofpx/blob/d9ec975b059a5895224fdedfe451cdf270a598d9/README.md) |
| gpu / 3 | [ROCmFPX Builder](https://github.com/Heretek-AI/ROCmFPX-BUILDER) | ROCmFPX downstream search / forward | excluded | Build/distribution automation for several existing runtime variants, not another execution stack. [1](https://github.com/Heretek-AI/ROCmFPX-BUILDER) |
| gpu / 3 | [ROCmFPX Windows recipes](https://github.com/daimonionnn/amd-rocmfpx-for-win) | ROCmFPX downstream search / forward | excluded | Deployment, benchmark and LM Studio integration scripts; preserve engine attribution rather than counting packaging as a new system. [1](https://github.com/daimonionnn/amd-rocmfpx-for-win) |
| gpu / 3 | [darklanes](https://github.com/avifenesh/darklanes) | memra README cross-reference / backward | deferred | Official repository link returned 404 during inspection; no source-derived classification possible. [1](https://github.com/avifenesh/darklanes) |
| gpu / 3 | [Aetheris Blackbox VTE integration](https://github.com/AMD-DEV-CONTEST/Radeon-hackathon-2026-07) | VTE downstream adoption search / forward | excluded | Agent application adopts VTE; useful adoption evidence, but it is not a second independent inference engine. [1](https://github.com/AMD-DEV-CONTEST/Radeon-hackathon-2026-07) [2](https://github.com/AMD-DEV-CONTEST/Radeon-hackathon-2026-07/pull/42) |
| gpu / 3 | [VTE Lemonade integration](https://github.com/lemonade-sdk/lemonade) | VTE forward integration search / forward | excluded | Integration request is adoption evidence, not another specialized runtime. [1](https://github.com/lemonade-sdk/lemonade) [2](https://github.com/lemonade-sdk/lemonade/issues/2679) |
| gpu / 3 | [StillDeadcode Radiance](https://codeberg.org/StillDeadcode/vllm-radiance) | vLLM Radiance explicit upstream attribution / backward | deferred | Codeberg source access failed in this tool session; preserve authorship and dependency relation in the reviewed GitHub continuation, without claiming independent audit of all upstream code. [1](https://codeberg.org/StillDeadcode/vllm-radiance) |
| gpu / 3 | [libr4d](https://codeberg.org/StillDeadcode/libr4d) | vLLM Radiance explicit upstream attribution / backward | deferred | Codeberg source access failed in this tool session; preserve authorship and dependency relation in the reviewed GitHub continuation, without claiming independent audit of all upstream code. [1](https://codeberg.org/StillDeadcode/libr4d) |
| gpu / 3 | [ggz14 Radiance MXFP4](https://codeberg.org/ggz14/radiance-vllm-mxfp4) | vLLM Radiance explicit upstream attribution / backward | deferred | Codeberg source access failed in this tool session; preserve authorship and dependency relation in the reviewed GitHub continuation, without claiming independent audit of all upstream code. [1](https://codeberg.org/ggz14/radiance-vllm-mxfp4) |
| root / 1 | [Cactus](https://github.com/cactus-compute/cactus) | CPU/edge/NPU or native multimodal keyword search / keyword | core | Connects model graph capture and lowering to a native mobile execution stack with its own quantized state and kernels. [1](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/README.md) [2](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/python/cactus/transpile/capture_pytorch.py) [3](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/python/cactus/transpile/lower.py) [4](https://github.com/cactus-compute/cactus/blob/2cfcdb8568eb9192323b27fd0012a834517b4419/cactus-engine/src/model.cpp) |
| root / 1 | [FastFlowLM](https://github.com/ROCm/FastFlowLM) | CPU/edge/NPU or native multimodal keyword search / keyword | core | Shows device-specific NPU execution built from model-family host runtimes and compiled kernel providers, with a visible source/binary boundary. [1](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/README.md) [2](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/src/common/models/README.md) [3](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/src/common/AutoModel/model_backend.cpp) [4](https://github.com/ROCm/FastFlowLM/blob/e5e33d9f64388f4e239eb6584493c76ef5a07231/flm_story.md) |
| root / 1 | [zLLM](https://github.com/zllm-lab/zllm) | CPU/edge/NPU or native multimodal keyword search / keyword | core | A growing collection of native model/device execution paths, including vision-language, image generation and video restoration, with explicit per-backend capability limits. [1](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/README.md) [2](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/deepseek_v4/vision.rs) [3](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/flux2_klein/rocm.rs) [4](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/seedvr2/rocm_pipeline.rs) [5](https://github.com/zllm-lab/zllm/blob/9a9d1ef0b55b09e1c41589ff83c407d3549f2b67/src/runtime/minicpm5/qnn.rs) |
| root / 2 | [Cactus Needle](https://github.com/cactus-compute/needle) | Cactus official README / backward | adjacent | A model/runtime co-design and deployment-packaging reference; public model/export code is more inspectable than the distributed native engine. [1](https://github.com/cactus-compute/needle/blob/3da4261073199444f2e070800854436fbc31fb6a/README.md) [2](https://github.com/cactus-compute/needle/blob/3da4261073199444f2e070800854436fbc31fb6a/needle/model/run.py) [3](https://github.com/cactus-compute/needle/blob/3da4261073199444f2e070800854436fbc31fb6a/needle/agent/fetch.py) |
| root / 1 | [TensorRT Edge-LLM](https://github.com/NVIDIA/TensorRT-Edge-LLM) | CPU/edge/NPU or native multimodal keyword search / keyword | adjacent | A compiler-based edge deployment reference linking exported model graphs, hardware-specific engine plans and a native multimodal runtime. [1](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/README.md) [2](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/docs/source/developer_guide/software-design/engine-builder.md) [3](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/0f52705723abfa8c6702654bfdcc082a728ed353/docs/source/developer_guide/software-design/llm-inference-runtime.md) |
| root / 1 | [BRaiN](https://github.com/swedishembedded/brain) | CPU/edge/NPU or native multimodal keyword search / keyword | adjacent | A broader native training/inference framework provides a contrast to narrowly scoped stacks, including explicit limitations for individual multimodal ports. [1](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/README.md) [2](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/docs/models/qwen3vl.md) [3](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/crates/wan/src/pipeline.rs) [4](https://github.com/swedishembedded/brain/blob/6626e37fc57d7b3a5a6d79944f008fac976e2681/docs/models/ltxv.md) |
| root / 1 | [Hilum LLM Engine](https://github.com/hilum-labs/hilum-local-llm-engine) | CPU/edge/NPU or native multimodal keyword search / keyword | adjacent | A mobile-focused llama.cpp fork illustrates continued subsystem porting and device adaptation while retaining the general engine. [1](https://github.com/hilum-labs/hilum-local-llm-engine/blob/dacf8c60173c05331970b16fcbaf15efbc755f73/README.md) [2](https://github.com/hilum-labs/hilum-local-llm-engine/blob/dacf8c60173c05331970b16fcbaf15efbc755f73/ggml/src/ggml-vulkan/CMakeLists.txt) |
| root / 1 | [Reame / nucleo](https://github.com/swellweb/reame) | CPU engine keyword search / keyword | deferred | Server adapter references an external nucleo-dev build directory, but the reviewed tree does not contain that engine. The guessed public nucleo repository returned 404; native-core provenance needs resolution. [1](https://github.com/swellweb/reame/blob/32d558bb78f41f345bd79cb861cb1a7f7bde1b14/README.md) [2](https://github.com/swellweb/reame/blob/32d558bb78f41f345bd79cb861cb1a7f7bde1b14/src/core/nucleo_backend.cpp) [3](https://github.com/swellweb/reame/blob/32d558bb78f41f345bd79cb861cb1a7f7bde1b14/CMakeLists.txt) |
| root / 1 | [SnapLLM](https://github.com/Zrald1/Snap-llm-phone) | Snapdragon engine keyword search / keyword | deferred | Live inference delegates to llama_decode; advertised batching includes simulation/stub logic in the inspected scheduler. Need a source-qualified execution delta before adding as a specialized system. [1](https://github.com/Zrald1/Snap-llm-phone/blob/e43c7d5d25a52b71764f678007ba0079c021a37d/README.md) [2](https://github.com/Zrald1/Snap-llm-phone/blob/e43c7d5d25a52b71764f678007ba0079c021a37d/src/engine.cpp) [3](https://github.com/Zrald1/Snap-llm-phone/blob/e43c7d5d25a52b71764f678007ba0079c021a37d/src/batch_scheduler.cpp) |
| root / 2 | [Lemonade FastFlowLM integration](https://developer.amd.com/playbooks/lemonade-getting-started/) | FastFlowLM adoption search / forward | excluded | Adoption evidence for FastFlowLM; this integration routes to an existing engine and is not counted again as the constructed NPU execution stack. [1](https://developer.amd.com/playbooks/lemonade-getting-started/) |
| root / 2 | [Jetson AI Lab Edge-LLM tutorial](https://github.com/NVIDIA-AI-IOT/jetson-ai-lab/blob/main/src/content/tutorials/model-optimization/tensorrt-edge-llm.mdx) | TensorRT Edge-LLM downstream deployment search / forward | excluded | Worked VLM/LLM deployment confirms use of the same engine construction workflow; a tutorial is not a separate engine record. [1](https://github.com/NVIDIA-AI-IOT/jetson-ai-lab/blob/main/src/content/tutorials/model-optimization/tensorrt-edge-llm.mdx) |
| root / 2 | [Original Needle model announcement](https://cactuscompute.com/blog/needle) | Cactus / Needle lineage search / backward | excluded | Earlier model generation remains history for one project. Current Needle 3 packaging was inspected separately; do not duplicate generations or copy old architecture claims. [1](https://cactuscompute.com/blog/needle) |
| root / 2 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Reviewed edge runtimes: retained dependencies / backward | already-included | Shared dependency is already cataloged; no duplicate engine record. [1](https://github.com/ggml-org/llama.cpp) |
| root / 2 | [TensorRT](https://github.com/NVIDIA/TensorRT) | Reviewed edge runtimes: retained dependencies / backward | already-included | Shared dependency is already cataloged; no duplicate engine record. [1](https://github.com/NVIDIA/TensorRT) |
| root / 3 | [NobodyWho](https://github.com/nobodywho-ooo/nobodywho) | Cactus comparison/adoption search / forward | excluded | Reviewed official description identifies llama.cpp as the inference engine; SDK integrations are not counted as another reconstructed execution stack in this pass. [1](https://github.com/nobodywho-ooo/nobodywho) |
| root / 3 | [Needle exporter/runtime compatibility reports](https://github.com/cactus-compute/needle/issues/58) | Needle deployment/forward search / forward | excluded | Packaging compatibility and quantization reports qualify the existing Needle record; they are not new projects. [1](https://github.com/cactus-compute/needle/issues/58) [2](https://github.com/cactus-compute/needle/issues/91) |
| construction / 1 | [Qwen-ASR (C)](https://github.com/antirez/qwen-asr) | Iris / native-model keyword search / keyword | core | Reconstructs Qwen3-ASR from waveform preprocessing through autoregressive transcription in C, making streaming context policy and CPU/GPU execution responsibilities directly inspectable. [1](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/README.md) [2](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/qwen_asr.c) [3](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/qwen_asr_encoder.c) [4](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/asr_regression.py) [5](https://github.com/antirez/qwen-asr/blob/924694251d9e0f18e5d86bbd06aa3ab5f870002d/MODEL.md) |
| construction / 2 | [Qwen3-TTS (C)](https://github.com/gabriele-mastrapasqua/qwen3-tts) | Qwen-ASR references and Qwen3-TTS comparison search / backward | core | Rebuilds the Qwen3-TTS talker, code predictor and waveform decoder as one native path; published engineering records connect implementation choices to reference checks and measurement corrections. [1](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/README.md) [2](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/qwen_tts_talker.c) [3](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/docs/pipeline.md) [4](https://github.com/gabriele-mastrapasqua/qwen3-tts/blob/ef339be58a778b062e1c14382347964552eae007/docs/ENGINEERING-METHOD.md) |
| construction / 1 | [Qingming Qwen3-TTS](https://github.com/uulong950/qingming-qwen3-tts) | independent Qwen3-TTS C++/native-engine search / keyword | core | Tests the narrowest device-specialization boundary: separate native synthesis paths for two fixed 24GB GPUs, including their memory capacities and generation/decoder concurrency contracts. [1](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/README.md) [2](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/CONTRACT.md) [3](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/devices/rtx4090-24g/qwen3_tts_0_6b.cu) [4](https://github.com/uulong950/qingming-qwen3-tts/blob/66b85b1e3b1d2cf6f927c6c8c8b23e48ed66e2ac/devices/rtx4090-24g/benchmark.cpp) |
| construction / 1 | [VoxGen](https://github.com/NullMagic2/VoxGen) | independent speech native GPU search / keyword | core | Reconstructs VoxCPM2 speech synthesis in Rust while directly controlling Vulkan buffers, shaders and incremental PCM state, including a separately tuned RDNA3 device profile. [1](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/README.md) [2](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/src/runtime.rs) [3](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/src/vulkan.rs) [4](https://github.com/NullMagic2/VoxGen/blob/7b4f78b060f8a4c41e87f8e282c92e53893c53ce/build_linux/smoke_pipeline_f16.sh) |
| construction / 1 | [parakeet.cpp (ggml)](https://github.com/mudler/parakeet.cpp) | independent Whisper/C++ inference-engine search / keyword | core | Ports NeMo speech graphs and cache-aware transcription semantics into C++/ggml, exposing the conversion, streaming-state and parity work needed to build a portable native ASR stack. [1](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/README.md) [2](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/src/model.cpp) [3](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/docs/parity.md) [4](https://github.com/mudler/parakeet.cpp/blob/5c9b0fbbd8e611d88e47d7e1ebae9bca9b447e8f/docs/batching.md) |
| construction / 2 | [parakeet.cpp (axiom)](https://github.com/Frikallo/parakeet.cpp) | parakeet.cpp comparison search / forward | core | An independent Parakeet reconstruction uses axiom/MPSGraph instead of ggml; it exposes how model and streaming ownership can be retained while reusing a different tensor backend. [1](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/README.md) [2](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/src/models/encoder.cpp) [3](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/src/models/streaming_encoder.cpp) [4](https://github.com/Frikallo/parakeet.cpp/blob/a212eea694ab2de39d4dd1dc601806fed9ce8b19/tests/test_all.cpp) |
| construction / 3 | [Aria](https://github.com/matteospanio/aria) | independent diffusion native-runtime search / keyword | core | Links an explicit author disclosure of LLM-assisted development to a complete native Stable Audio 3 artifact and controlled reference tests, without assuming lower total construction cost. [1](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/README.md) [2](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/src/aria_model_sa3.c) [3](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/src/aria_sampler.c) [4](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/tests/test_e2e.c) [5](https://github.com/matteospanio/aria/blob/8af80a7f900cff1d71aaecfa2929452dc46b520a/BENCHMARKS.md) |
| construction / 2 | [vla.simd](https://github.com/cair-vinuni/vla.simd) | vla.cpp / parent VLA lead and vla.simd search / keyword | core | Rebuilds selected robot-policy model paths around CPU SIMD operators and model adapters, exposing action preprocessing and numerical-porting obligations beyond a language-model runtime. [1](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/README.md) [2](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/src/hal/arch.h) [3](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/src/nn/linear.cpp) [4](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/docs/development.md) [5](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/docs/benchmark/intel-core-ultra-9-285k.md) [6](https://github.com/cair-vinuni/vla.simd/blob/75791daf47ca5e62564ca797e83ea555b17b8940/tools/check_model_parity.py) |
| construction / 1 | [Hearth](https://github.com/jeff-hiner/hearth) | Iris / independent Rust CUDA diffusion-engine search / keyword | core | Reconstructs SD-family model graphs, samplers and dependency-ordered execution in Rust over CubeCL/wgpu, illustrating native pipeline ownership without rebuilding the entire GPU layer. [1](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/README.md) [2](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/src/unet/model.rs) [3](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/src/node/executor.rs) [4](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/Cargo.toml) [5](https://github.com/jeff-hiner/hearth/blob/7e6170228626a7be533d4f931fc5a0d87b086371/tests/tensor_ops.rs) |
| construction / 1 | [brodiffusion](https://github.com/wlejon/brodiffusion) | Iris / independent C++ diffusion-engine search / keyword | core | Owns C++ image-model pipelines and denoiser capture/replay policy over a reused tensor backend, making the boundary between model reconstruction and lower-level reuse explicit. [1](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/README.md) [2](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/src/pipeline_step_graph.cpp) [3](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/src/pipeline_qwenimage21.cpp) [4](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/scripts/qwenimage21_pipeline_parity.sh) [5](https://github.com/wlejon/brodiffusion/blob/2ac6f400314817f73df2857c2f7962684c43c403/tests/test_device_parity.cpp) |
| construction / 1 | [stable-diffusion.rs](https://github.com/andreinknv/stable-diffusion.rs) | independent native Rust diffusion search / keyword | core | Documents a native Rust diffusion implementation and its Candle-to-MLX migration, exposing which model/backend boundaries can survive a device-stack change and which require new parity checks. [1](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/README.md) [2](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/backends.md) [3](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/seam.md) [4](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/docs/agent-tasks/README.md) [5](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/xtask/golden/README.md) [6](https://github.com/andreinknv/stable-diffusion.rs/blob/930c48e2e7c962e856a12bc01b98cc95f27c990c/crates/sd-models/src/mlx/flux.rs) |
| construction / 1 | [MiniMax-H3 MLX](https://github.com/PipeNetwork/minimax-h3-mlx) | independent video native MLX search / keyword | core | Reconstructs a complete joint video/audio diffusion model on MLX, including packed modality geometry and invariant AdaLN precomputation; distinguishes making a model fit from making it fast. [1](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/README.md) [2](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/minimax_h3_mlx/pipeline.py) [3](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/minimax_h3_mlx/adaln.py) [4](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/tests/test_dit_parity.py) [5](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/tests/test_text_encoder_parity.py) [6](https://github.com/PipeNetwork/minimax-h3-mlx/blob/b2f7e4d2b7861cefe68b75e4b59ab81cc4e7c318/reference/README.md) |
| construction / 3 | [Vidax](https://github.com/FlyingGiraffe/vidax) | independent video inference runtime TPU search / keyword | core | Ports video model graphs and checkpoint layouts onto TPU meshes with explicit JAX sharding and numerical-debugging records, making hardware migration a concrete construction case. [1](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/README.md) [2](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/core/attention.py) [3](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/core/sharding.py) [4](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/src/vidax/models/wan/wan2_1/dit.py) [5](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/docs/lessons/wan2_1_debugging.md) [6](https://github.com/FlyingGiraffe/vidax/blob/3f03da2a41b03dad47064674b68cc2b2ede21912/docs/benchmarking.md) |
| construction / 3 | [TeleFuser](https://github.com/Tele-AI/TeleFuser) | independent video inference engine search / keyword | core | Builds model-specific generation stages together with bounded streaming dataflow, retained session state and execution leases, connecting model execution ownership to an interactive serving workload. [1](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/README.md) [2](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/docs/en/stream_scheduler.md) [3](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/telefuser/pipelines/wan_video/single_dit_denoising.py) [4](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/telefuser/pipelines/wan_video/wan21_video.py) [5](https://github.com/Tele-AI/TeleFuser/blob/f21457a92e92f4a7570f0cb6b445ee334f1072b0/benchmarks/telefuser_aiperf/README.md) |
| construction / 3 | [StreamDiffusionV2](https://github.com/chenfengxu714/StreamDiffusionV2) | streaming video engine references / StreamDiffusionV2 search / backward | core | Reconstructs causal video execution around chunked denoising and distributed KV ownership; concrete source and adopter evidence connect a specialized schedule to an integrated streaming artifact. [1](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/README.md) [2](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamdiffusionv2/pipeline.py) [3](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamv2v/inference_pipe.py) [4](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/streamv2v/communication/kv_cache_manager.py) [5](https://github.com/chenfengxu714/StreamDiffusionV2/blob/6961a5cf2045d1dda05a04ef229698bdc04e873a/tools/eval_video_metrics.py) |
| construction / 3 | [Quartz](https://github.com/SaientAI/saient-quartz) | independent Wan Rust native search / keyword | core | Exposes native Rust image generation and an evolving native Wan path, while a separate C++ video companion provides a concrete case for auditing claimed versus actual execution boundaries. [1](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/README.md) [2](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/src/sdxl_pipeline.rs) [3](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/src/wan_pipeline.rs) [4](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/reference/README.md) [5](https://github.com/SaientAI/saient-quartz/blob/5a2a82387b9548c6c165eb50880a5f49c54ef1ff/Cargo.toml) |
| construction / 1 | [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | independent speech-engine search / keyword | adjacent | Established native speech-model route: a historical control for what purpose-built runtimes and cross-backend maintenance already required. [1](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/README.md) [2](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/src/whisper.cpp) [3](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/CMakeLists.txt) [4](https://github.com/ggml-org/whisper.cpp/blob/0c7be696371069e0baa2515ed7aa08d5a5473aa6/tests/CMakeLists.txt) |
| construction / 1 | [WhisperKit](https://github.com/argmaxinc/argmax-oss-swift) | independent WhisperKit Swift inference search / keyword | adjacent | Compiler-backed speech deployment provides a comparison for how much execution control remains in the runtime versus compiled platform artifacts. [1](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/README.md) [2](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/Sources/WhisperKit/Core/WhisperKit.swift) [3](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/Sources/WhisperKit/Core/TextDecoder.swift) [4](https://github.com/argmaxinc/argmax-oss-swift/blob/9f99b5cb6a907730543823ad271b82532782a899/Tests/WhisperKitTests/UnitTests.swift) |
| construction / 1 | [diffusion-rs](https://github.com/EricLBuehler/diffusion-rs) | independent diffusion Rust CUDA engine search / keyword | adjacent | A neighboring Rust model-port route provides a component-reuse and offload comparison; it is not evidence of agent-generated construction. [1](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/README.md) [2](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/Cargo.toml) [3](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/diffusion_rs_core/src/pipelines/flux/mod.rs) [4](https://github.com/EricLBuehler/diffusion-rs/blob/d977e05ad19075f87bed8c0888ae42e63c456729/diffusion_rs_core/src/pipelines/flux/sampling.rs) |
| construction / 3 | [StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion) | StreamDiffusionV2 predecessor / backward | adjacent | Earlier workload-specific pipeline reconstruction is a comparison for newer causal video engines; most model components remain supplied by Diffusers. [1](https://github.com/cumulo-autumn/StreamDiffusion/blob/b623251dc055e1fd858d53509aa43e09dfc5cdc0/README.md) [2](https://github.com/cumulo-autumn/StreamDiffusion/blob/b623251dc055e1fd858d53509aa43e09dfc5cdc0/src/streamdiffusion/pipeline.py) |
| construction / 3 | [edge-dit.cpp](https://github.com/THU-MIG/edge-dit.cpp) | existing image/video catalog execution-boundary re-audit / backward | already-included | Recommend adjacent → core on inspected execution ownership; not a new repository. Core by execution ownership: native DiT graphs and model-component residency, graph segmentation and staged offload reconstruct the integrated constrained-memory path. [1](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/README.md) [2](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/docs/optimization/memory-efficient-execution.md) [3](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/src/core/backend/ggml/cuda/ed_async_offload.cu) [4](https://github.com/THU-MIG/edge-dit.cpp/blob/97cc585d9dbd9ac5e30b78ef2e2c4a0d8bfbe9f2/benchmark/README.md) |
| construction / 3 | [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) | existing image/video catalog execution-boundary re-audit / backward | already-included | Recommend adjacent → core on inspected execution ownership; not a new repository. Core by construction boundary: the native image/video model implementation owns loading, conditioning, sampling and component placement over reusable ggml backends. [1](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/README.md) [2](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/src/pipeline/diffusion_engine.cpp) [3](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/src/pipeline/video.cpp) [4](https://github.com/leejet/stable-diffusion.cpp/blob/2988060a4338a5dcd94721c964a8e87003c1ac8b/docs/caching.md) |
| construction / 3 | [LightX2V](https://github.com/ModelTC/LightX2V) | existing image/video catalog execution-boundary re-audit / backward | already-included | Recommend adjacent → core on inspected execution ownership; not a new repository. Core by substantive backend reconstruction: model inference, operator storage contracts and two-slot weight transfer expose owned execution and memory decisions within a shared framework. [1](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/README.md) [2](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/lightx2v/common/offload/manager.py) [3](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/lightx2v/common/offload/block_loader.py) [4](https://github.com/ModelTC/LightX2V/blob/94f0f19459e66f61a723db7690f1707f308599ef/docs/EN/source/getting_started/benchmark.md) |
| construction / 3 | [FastVideo](https://github.com/hao-ai-lab/FastVideo) | existing image/video catalog execution-boundary re-audit / backward | already-included | Recommend adjacent → core on inspected execution ownership; not a new repository. Core by integrated model execution: its own model implementations, registries, component loaders and denoising stages reconstruct inference, beyond the separately cataloged sparse/distillation methods. [1](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/README.md) [2](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/docs/inference/architecture.md) [3](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/fastvideo/pipelines/stages/denoising.py) [4](https://github.com/hao-ai-lab/FastVideo/blob/d5253fd71055927f12aa6c4aa679b93a00238851/docs/contributing/performance_benchmarks.md) |
| construction / 2 | [vla.cpp](https://fai-modelopt-tech.github.io/vla-cpp.github.io/) | parent VLA lead / keyword | deferred | Official page describes a native VLA runtime but says code and paper links are coming soon; inspectable execution source was not established. [1](https://fai-modelopt-tech.github.io/vla-cpp.github.io/) |
| construction / 1 | [Aurora Rust Engine](https://github.com/lecyberbill/aurora-rust-engine) | native Rust diffusion search / keyword | deferred | Promising native FLUX/model paths inspected, but advertised multimodal breadth and construction/validation boundary require a complete follow-up audit; not rejected as a wrapper. [1](https://github.com/lecyberbill/aurora-rust-engine/blob/2a653e462f68cbd3fefe819217e8f7fa35bf4b26/README.md) [2](https://github.com/lecyberbill/aurora-rust-engine/blob/2a653e462f68cbd3fefe819217e8f7fa35bf4b26/docs/KREA2_CANDLE_SPEC.md) |
| construction / 3 | [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | independent image/video inference search / keyword | deferred | Official source tree and overview identify substantial model pipelines; execution ownership and inference-versus-training scope have not yet been audited sufficiently for this pass. [1](https://github.com/modelscope/DiffSynth-Studio/blob/acf2ad29c65f436633f57beec1caaa1296760331/README.md) |
| construction / 2 | [ced.cpp](https://github.com/localai-org/ced.cpp) | parakeet/LocalAI speech ecosystem / backward | deferred | Native sound-event classification is a plausible adjacent route; only metadata/overview were checked, so do not assume end-to-end coverage or equivalence. [1](https://github.com/localai-org/ced.cpp/blob/736a4ee46a31d4ff38b41add65ce0f2cf1aaa05f/README.md) |
| construction / 2 | [speech.cpp](https://github.com/NairoDorian/speech.cpp) | speech native-runtime expansion / keyword | deferred | Modular ggml speech runtime surfaced; model execution and build/validation source have not yet been audited. [1](https://github.com/NairoDorian/speech.cpp) |
| construction / 2 | [Qwen3-TTS-ncnn](https://github.com/Krystal579-max/Qwen3-TTS-ncnn) | Qwen3-TTS native alternatives / forward | deferred | A converter/ncnn-backed synthesis route surfaced; further inspection must distinguish owned decoding from reused compiled artifacts. [1](https://github.com/Krystal579-max/Qwen3-TTS-ncnn) |
| construction / 2 | [Qwen3-TTS (darkautism)](https://github.com/darkautism/qwen3-tts) | Qwen3-TTS native alternatives / forward | deferred | Advertised Rust/SBC execution path requires source and validation-boundary audit before inclusion. [1](https://github.com/darkautism/qwen3-tts) |
| construction / 3 | [mlx_diffuser](https://github.com/amirhossein-razlighi/mlx_diffuser) | MLX image/video alternatives / keyword | deferred | Image and video model paths surfaced; source ownership and implemented streaming scope remain unverified. [1](https://github.com/amirhossein-razlighi/mlx_diffuser) |
| construction / 4 | [LCM-Dreamshaper-V7-rs](https://github.com/darkautism/LCM-Dreamshaper-V7-rs) | stable-diffusion.rs forward/neighbor search / forward | deferred | RK3588 NPU image-generation route surfaced in the final expansion; source audit was handed to the parent CPU/NPU strand. [1](https://github.com/darkautism/LCM-Dreamshaper-V7-rs) |
| construction / 2 | [ArgusAgent](https://github.com/microsoft/ArgusAgent) | Sol-Engine forward search / forward | excluded | General research-agent workflow; reviewed results material proposes Sol-engine work but did not establish an additional concrete specialized engine artifact. [1](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/ARGUS_IMPRESSIVE_RESULTS.md) |
| construction / 4 | [Scope](https://github.com/daydreamlive/scope) | StreamDiffusionV2 adopter search / forward | excluded | Confirms adoption/integration of StreamDiffusionV2; no separate newly audited execution-stack reconstruction was established for another engine record. [1](https://github.com/daydreamlive/scope/blob/main/src/scope/core/pipelines/streamdiffusionv2/docs/usage.md) [2](https://github.com/daydreamlive/scope/blob/main/README.md) |
| construction / 2 | [LocalAI](https://github.com/mudler/LocalAI) | parakeet.cpp adopter search / forward | excluded | Adopter/integration evidence for parakeet.cpp rather than an additional model-specific reconstruction established by this audit. [1](https://pkg.go.dev/github.com/mudler/LocalAI@v1.40.1-0.20260928194146-84a2b209a052/core/gallery/importers) |
| construction / 4 | [MiniMax-H3 MLX quantized checkpoints](https://huggingface.co/pipenetwork/MiniMax-H3-MLX-4bit) | MiniMax-H3 MLX forward search / forward | excluded | Same engine with converted precision variants; preserve provenance but do not count checkpoints as separate execution stacks. [1](https://huggingface.co/pipenetwork/MiniMax-H3-MLX-4bit) [2](https://huggingface.co/pipenetwork/MiniMax-H3-MLX-8bit) |
| construction / 1 | [stable-diffusion-flux.cpp](https://github.com/robolamp/stable-diffusion-flux.cpp) | native diffusion search / keyword | excluded | Search evidence pointed to stable-diffusion.cpp-derived material; no substantial independently audited execution change established for a distinct entry. [1](https://github.com/robolamp/stable-diffusion-flux.cpp) |
| construction / 1 | [iris.c-contrib](https://github.com/FHult/iris.c-contrib) | Iris alternative search / forward | excluded | Derivative material without an established distinct construction boundary in this audit; retain Iris as the primary case. [1](https://github.com/FHult/iris.c-contrib) |
| construction / 4 | [TeleFuser-p](https://github.com/yJader/TeleFuser-p) | TeleFuser forward search / forward | excluded | A derivative repository surfaced; no separately demonstrated execution reconstruction beyond TeleFuser established. [1](https://github.com/yJader/TeleFuser-p) |
| construction / 2 | [VibeQwen](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/) | MetaInfer forward/generated-engine search / forward | already-included | Already represented by the MetaInfer → VibeQwen case; do not count generated-engine mention as a duplicate project. [1](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/) |
| construction / 2 | [Sol-Engine](https://github.com/NVlabs/Sana/tree/sol-engine) | seed construction workflow / backward | already-included | Concrete video optimization workflow already included; new image/video cases should link execution ownership, not add every reused kernel. [1](https://github.com/NVlabs/Sana/tree/sol-engine) |
| construction / 2 | [MetaInfer](https://github.com/MetaInfer/MetaInfer) | seed construction workflow / forward | already-included | Already included with generated-engine linkage; no independent new qualified workflow established by expansion. [1](https://github.com/MetaInfer/MetaInfer) |
| construction / 2 | [Mirage](https://github.com/mirage-project/mirage) | seed compiler construction route / backward | already-included | Already included compiler-generated execution route; shared compiler/kernel dependencies are not automatically separate core cases. [1](https://github.com/mirage-project/mirage) |
| construction / 3 | [xDiT](https://github.com/xdit-project/xDiT) | existing video route re-audit / backward | already-included | Retain adjacent as the distributed diffusion-framework comparison in this pass; no new case-level construction audit justifies promotion here. [1](https://github.com/xdit-project/xDiT/blob/81dc33d5de7aab0b444af05882dbc55591f3059a/README.md) |
| construction / 3 | [TurboDiffusion](https://github.com/thu-ml/TurboDiffusion) | existing video route re-audit / backward | already-included | Retain adjacent model/optimization co-design route; distinguish sparse/quantized/distilled model effects from an independently reconstructed runtime. [1](https://github.com/thu-ml/TurboDiffusion/blob/e3d61360b0eeab60c5cd09ff7d6c1020cccc80b2/README.md) |
| construction / 3 | [CausVid / Self-Forcing model references](https://github.com/guandeh17/Self-Forcing) | StreamDiffusionV2 credited components / backward | excluded | Training/model-generation references support the causal checkpoint lineage; they are not separately audited execution stacks in this pass. [1](https://github.com/guandeh17/Self-Forcing) |
| construction / 2 | [Shared tensor/compiler/kernel dependencies](https://github.com/ml-explore/mlx) | native diffusion/audio/VLA README and build references / backward | excluded | MLX, ggml, CubeCL, JAX and device libraries explain reuse; this pass does not indiscriminately add generic dependencies as core inference systems. [1](https://github.com/ml-explore/mlx) [2](https://github.com/ggml-org/ggml) [3](https://github.com/tracel-ai/cubecl) [4](https://github.com/jax-ml/jax) |

## Round log

Round 0 fixed the question, inclusion rules and seeds before new searches. The four parallel branches use local round numbers; they are not synchronized waves. Counts below describe ledger records, not unseen search results.

| Branch / round | Recorded screens | Newly admitted records | Deferred records |
| --- | ---: | ---: | ---: |
| apple / 1 | 15 | 10 | 2 |
| apple / 2 | 10 | 4 | 1 |
| apple / 3 | 9 | 3 | 2 |
| apple / 4 | 11 | 0 | 9 |
| gpu / 1 | 16 | 7 | 3 |
| gpu / 2 | 15 | 8 | 2 |
| gpu / 3 | 11 | 0 | 5 |
| root / 1 | 8 | 6 | 2 |
| root / 2 | 6 | 1 | 0 |
| root / 3 | 2 | 0 | 0 |
| construction / 1 | 14 | 11 | 1 |
| construction / 2 | 15 | 3 | 5 |
| construction / 3 | 15 | 6 | 2 |
| construction / 4 | 4 | 0 | 1 |

### apple · round 1

Independent English keyword expansion and seed README/reference screening. Retrieved official repositories; indexed secondary reports were used only to find primary artifacts. The Perplexity blog could not be opened, so source and dated repository reports anchor Lily.

**Expanded:** splash, iris, llama-cpp.

<details>
<summary>Search queries / 检索式</summary>

- github Apple Silicon inference engine uzu Lily Metal LLM
- github splash incoai inference engine references
- github Iris inference Apple Silicon engine antirez
- Perplexity Lily inference engine github official
- BaseRT inference github Apple Metal
- NPUMoE github inference runtime
- ANE inference engine ANEMLL github Apple Neural Engine

</details>

### apple · round 2

Followed explicit upstreams, exporters, named adopters and comparisons. Some broad or quoted-site queries returned irrelevant material; corrected domain queries were run. GitHub anonymous API rate limit was reached, then read-only shallow source checkouts continued inspection. Found TurboFieldfare, Colibri, ANE-LM and CoreML LLM CLI.

**Expanded:** lily, lithos-metal, uzu, saragossa, tuff, basert, anemll, ane-cpp, pmetal, metalchat.

<details>
<summary>Search queries / 检索式</summary>

- "lithos-metal" "fork" inference
- "lily" "inference" "Apple" github engine -site:reddit.com
- "uzu" "inference" "fork" -site:reddit.com
- "saragossa" inference "fork" github
- "TUFF" "turbo-fieldfare" "colibri"
- "ane.cpp" github inference engine fork
- "NPUMoE" github
- "site:github.com" "colibri" "inference"
- "turbo-fieldfare" inference
- "site:github.com" "saragossa" "inference"
- "site:github.com" "NPUMoE"
- site:github.com "saragossa" "inference"
- site:github.com "uzu" "inference" engine -trymirai/uzu
- site:github.com "NPUMoE"
- site:github.com "BaseRT" "inference" -basecompute/baseRT

</details>

### apple · round 3

Source-level backward expansion found Swiftlet through Colibri provenance and SwiftLM through TurboFieldfare references; official ANEMLL project listing exposed the substantial llama.cpp sidecar/slot-bank fork. Model-only forks and thin adopters were not counted separately.

**Expanded:** turbo-fieldfare, colibri, ane-lm, coreml-llm-cli, lalamo, anemll-server.

<details>
<summary>Search queries / 检索式</summary>

- site:github.com "turbo-fieldfare" "fork" -Lookoff -drumih
- site:github.com "colibri" "inference" "fork"
- site:github.com "ANE-LM" "fork"
- site:github.com "anemll" "inference" "fork"

</details>

### apple · round 4

Final observed frontier still produced unaudited candidates (Hypura, Rapid-MLX, Rustane and others). They are deferred with reasons. This branch has NOT met a zero-yield convergence criterion and makes no exhaustiveness claim; further same-family expansion was stopped for synthesis while preserving the open frontier.

**Expanded:** swiftlet, swiftlm, anemll-flash-llama, anemll-flash-moe.

<details>
<summary>Search queries / 检索式</summary>

- site:github.com "Swiftlet" "inference" -leonickson1/Swiftlet -JustVugg
- site:github.com "SwiftLM" "stream" "fork" -SharpAI
- site:github.com "anemll-flash-llama.cpp" -Anemll
- site:github.com "Lily" "lithos-metal" "inference"
- site:github.com Hypura inference engine
- site:github.com Rapid-MLX disk-stream expert streaming
- site:github.com "ncdrone/rustane" inference

</details>

### gpu · round 1

Read seed README/source lists, extracted explicit credits and searched independent GPU/native-engine terms; identified seven immediately eligible native/backend candidates.

**Expanded:** gufo, ninfer, strata, llamampere, ktransformers.

<details>
<summary>Search queries / 检索式</summary>

- github hipEngine inference
- github vllm-radiance
- github Gufo inference Strix
- github NInfer llamAmpere
- Strix Halo inference engine github -site:reddit.com
- RTX 5090 inference engine github -site:reddit.com
- inference engine from scratch AMD github Qwen
- site:github.com inference engine RTX 5090 from scratch
- site:github.com CIRU Runtime
- site:github.com ZINC inference Vulkan
- site:github.com Qwen native inference H100 engine

</details>

### gpu · round 2

Expanded admitted systems using README credits, architecture/maintenance references and named downstreams. Added six further core cases and two adjacent routes; inspected pinned source for all additions. NInfer-3090 and Strix forks represented by one distinct continuation each.

**Expanded:** hipengine, vte, zinc, imp, memra, kipp, vllm-radiance, gufo, ninfer.

<details>
<summary>Search queries / 检索式</summary>

- hipEngine vllm-radiance gufo inference
- imp inference engine kekzl fork
- memra inference fork
- ZINC inference engine github -zolotukhin -site:reddit.com
- CIRU Runtime github
- vllm-radiance inference github -site:reddit.com
- hipEngine inference github -site:reddit.com
- Qwen inference engine SM86
- ninfer-3090 github
- llama-cpp-strix-halo ROCmFPX
- Llaminar github inference
- vllm-radiance libr4d
- site:github.com ROCmFPX lmcoleman
- site:github.com Llaminar inspired
- site:github.com VTE kyuubyN inference engine fork
- site:github.com Kipp inference engine fork

</details>

### gpu · round 3

Final observed frontier: newly screened downstreams were wrappers, duplicate fork families, inaccessible references or insufficiently qualified variants; zero further admitted entries. Infernix points back to existing NInfer/Strata and is already credited by the selected 3090 continuation. This is closure of reviewed references/search results, not enumeration of every GitHub fork.

**Expanded:** ninfer-3090, infernix, ciru-runtime, gufo-rdma, llaminar, strix-llama-cpp, rocmfpx, hybrimoe.

<details>
<summary>Search queries / 检索式</summary>

- site:github.com ROCmFPX fork inference
- site:github.com HybriMoE inference -PKU-SEC-Lab -awesome
- site:github.com Llaminar inference -Llaminar/llaminar
- site:github.com Gufo RDMA
- Infernix inference github -wallawalla47 -site:reddit.com
- Gufo RDMA github -neuhaus -site:reddit.com
- strix-llama.cpp fork -site:reddit.com -site:github.locker
- HybriMoE Colibri github

</details>

### root · round 1

Cross-hardware and multimodal keyword expansion; official pinned README and implementation paths checked for admitted entries.

**Expanded:** cactus, fastflowlm, tensorrt-edge-llm, zllm, brain, hilum-engine, reame, snapllm.

<details>
<summary>Search queries / 检索式</summary>

- Cactus inference engine CPU native github ARM
- FastFlowLM github AMD NPU inference engine
- NVIDIA TensorRT Edge LLM github Jetson runtime
- specialized inference engine CPU from scratch model github 2026
- CPU specialized inference runtime mobile engine ARM github
- site:github.com zllm-lab/zllm vision inference
- site:github.com swedishembedded/brain inference

</details>

### root · round 2

Backward model/engine and dependency tracing plus forward integration searches. Needle is an additional adjacent record; wrappers/tutorials and repeated generations are not new stacks.

**Expanded:** needle, lemonade, jetson-lab, needle-v1, llama-cpp, tensorrt.

<details>
<summary>Search queries / 检索式</summary>

- Cactus Needle inference engine runtime adoption
- FastFlowLM Lemonade engine NPU
- TensorRT-Edge-LLM Jetson tutorial
- zllm inference fork
- Cactus inference engine built on

</details>

### root · round 3

Observed follow-up results returned existing projects, deployment issues and a llama.cpp-backed SDK. No further eligible entry was established on this frontier; this does not resolve deferred native-core provenance or enumerate all forks.

**Expanded:** needle, zllm, brain, nobodywho.

<details>
<summary>Search queries / 检索式</summary>

- site:github.com cactus-compute/needle engine -cactus-compute -awesome
- site:github.com zllm-lab/zllm -zllm-lab -awesome
- site:github.com swedishembedded/brain fork -swedishembedded -awesome
- site:github.com NobodyWho llama.cpp

</details>

### construction · round 1

Independent modality-specific keywords supplement the construction seeds; repository metadata, fixed commits, READMEs, source paths and selected design/validation artifacts were retrieved. Source reading only; no upstream code execution.

**Expanded:** iris, metainfer, sol-engine, mirage, hearth, brodiffusion, voxgen, qwen-asr-c, qingming-qwen3-tts, parakeet-ggml, stable-diffusion-rs, minimax-h3-mlx.

<details>
<summary>Search queries / 检索式</summary>

- github diffusion inference "pure C" FLUX runtime -llama
- github specialized inference "whisper" C++ inference engine
- github "agent" "inference engine" "generated" model 2026
- github "diffusion" "from scratch" "Metal" inference
- github "MetaInfer" "engine" -site:reddit.com
- github "Sol-Engine" inference references
- github diffusion inference "Rust" "CUDA" engine standalone
- github "WhisperKit" "Qwen3-TTS.cpp"
- site:github.com "inference engine" "agent" "generated" "model" -MetaInfer -llama -awesome -rag
- site:github.com "Qwen3-TTS" "C++" "inference"
- site:github.com "video" "inference" "native" "MLX" minimax
- site:github.com "WhisperKit" "Swift" inference

</details>

### construction · round 2

Backward inspection used official README/build/design references; forward queries found distinct axiom Parakeet, LocalAI adoption and model/checkpoint variants. Agent task files were not treated as evidence of AI authorship. Generic reused libraries were screened as dependencies, not automatically added.

**Expanded:** qwen-asr-c, qwen3-tts-c, parakeet-ggml, parakeet-axiom, vla-simd, voxgen, hearth, brodiffusion, metainfer, sol-engine.

<details>
<summary>Search queries / 检索式</summary>

- "vla.simd" github
- "MetaInfer" "VibeQwen" "engine" github generated
- "Sol-Engine" "ArgusAgent" inference
- site:github.com "Hearth" "diffusion" "Vulkan" "inspired"
- site:github.com "VoxGen" "VoxCPM" "credits"
- site:github.com "brodiffusion" "validation"
- site:github.com "vla.simd" inference
- "parakeet.cpp" inference engine -site:reddit.com -site:github.com/mudler/parakeet.cpp
- "VoxGen" "inference" -site:reddit.com -site:github.com/NullMagic2/VoxGen
- "qingming-qwen3-tts" -site:github.com/uulong950/qingming-qwen3-tts
- "hearth" "diffusion" "jeff-hiner" -site:github.com/jeff-hiner/hearth

</details>

### construction · round 3

Expanded image/video beyond Apple and text-engine terminology. Native Rust image/video, TPU model ports and stateful GPU streaming runtimes were source-inspected. Four existing entries receive proposed core reclassification based on execution ownership, not new record counts.

**Expanded:** vidax, telefuser, streamdiffusion-v2, streamdiffusion, aria, saient-quartz, edge-dit, stable-diffusion-cpp, lightx2v, fastvideo, turbodiffusion, xdit.

<details>
<summary>Search queries / 检索式</summary>

- 视频生成 推理 引擎 专用 github native CUDA engine
- "video" "inference engine" github -awesome -vllm -tensorrt -rag -MetaInfer -llama -CUDA-Graphs
- "diffusion" "inference engine" "C++" github -stable-diffusion.cpp -robolamp
- "Wan" "inference" "Rust" github native
- "vidax" "github.com"
- "TeleFuser" "LightX2V" "runtime"
- "video generation" "inference runtime" "GitHub" "TPU"
- "video generation" "inference engine" -site:reddit.com -site:arxiv.org -site:github.locker -site:wikipedia.org -site:deepwiki.com
- "StreamDiffusionV2" github
- "diffusion" "native runtime" github -llama -gufo -quartz -awesome
- "图像生成" "推理引擎" "GitHub" -ComfyUI -ollama -天数 -芯片

</details>

### construction · round 4

Forward checks identified Scope adoption, same-engine quantized weights, mirrors and another RK3588 image route. This frontier is INCOMPLETE: unresolved strong candidates remain and not every new engine has a complete adopter/citation trace. No convergence or exhaustive-coverage claim is made.

**Expanded:** vidax, telefuser, streamdiffusion-v2, brodiffusion, aria, saient-quartz, minimax-h3-mlx, stable-diffusion-rs.

<details>
<summary>Search queries / 检索式</summary>

- "vidax" "inference" "comparison" -site:pypi.org -site:arxiv.org -site:twstalker.com
- "TeleFuser" "github" -site:github.com/Tele-AI -site:deepwiki.com -site:github.mosekj.com
- "brodiffusion" "Hearth" "engine"
- "StreamDiffusionV2" "Scope" github engine
- "matteospanio/aria" "audio" -site:reddit.com -site:github.com/matteospanio/aria
- "SaientAI/saient-quartz" "inference" -site:github.com/SaientAI
- "minimax-h3-mlx" "inference" -site:github.com/PipeNetwork
- "stable-diffusion.rs" "andreinknv" -site:github.com/andreinknv

</details>

## Source review and coverage limits

Official repositories, pinned source files and author documentation establish implementation boundaries; no upstream model was downloaded, no engine was executed and no performance was independently reproduced. Link availability is separate from source correctness or numerical validation.

Cross-review sampled substantial forks and multimodal paths. It corrected TurboFieldfare from “model designed” to “runtime designed”, tightened Saragossa’s AI attribution, made TUFF’s execution delta explicit, and aligned FastVideo’s record with its dense as well as optional sparse/distilled runtime paths. TeleFuser scheduling claims are limited to the inspected LingBot service. The catalog preserves closed-core, license and paused-development caveats where relevant.

**apple**

- Project references and forward adopters are an informal software relation graph, not a complete citation graph. Search ranking and repository indexing omit obscure projects.
- The final frontier was not exhausted: Hypura, Rapid-MLX, Rustane, rapidAI, LlamaOnDisk and some substantive forks need source/quality audits.
- No upstream model, benchmark, installer or test suite was executed. Pinned code inspection is not build verification, numerical reproduction or a safety audit.
- English keyword searches were used in this Apple branch; Chinese-only projects and unindexed author posts remain a coverage gap.
- BaseRT has a proprietary runtime. Public converter/binding code cannot establish implementation details of the engine.
- Individual field guides and author logs establish disclosed workflows, not total development cost or a causal benefit from AI coding.

**gpu**

- No upstream binaries or GPU code were executed; source and author reports are not independent reproduction.
- Keyword indexing and named-fork references are incomplete; GitHub fork API was not exhaustively enumerated.
- Codeberg upstreams were inaccessible; GitHub Radiance continuation source was inspected and original authorship retained.
- Some public README links returned 404 (Laurent fork, darklanes); no inaccessible-source claims were inferred.
- NInfer hardware ports and overlapping Strix/ROCmFPX branches were recorded without making every port, model recipe or package a new case.
- Fields marked AI not-established do not assert absence of AI; agent files and contribution policies alone were not treated as authorship evidence.

**root**

- Project link graphs are incomplete and search may omit small or Chinese-language repositories.
- Reame native-core source provenance and Snapdragon wrapper execution deltas remain unresolved.
- The last pass is a bounded discovery update, not a certified exhaustive closure of every repository fork or model port.

**construction**

- This discovery strand has not reached the preregistered convergence threshold. Deferred strong candidates are unresolved, not exclusions or zero-growth evidence.
- Aurora Rust Engine, DiffSynth-Studio, speech.cpp, ncnn/SBC TTS variants and mlx_diffuser require additional source/design/validation inspection. The final RK3588 image lead was handed to the parent NPU strand.
- No upstream inference, build, GPU/TPU experiment or robot trial was executed. Fixed-commit source inspection and author reports do not establish reproducibility or performance superiority.
- Newer low-visibility repositories, unindexed Chinese sources, closed implementations and unreleased code are under-observed. Search absence is not evidence that no related engine exists.
- AI involvement is marked disclosed only for explicit author statements such as Aria. Agent-oriented instructions, source style and repository age are not authorship evidence.
- Construction and maintenance economics remain mostly unknown. Code size, runtime speed and AI involvement do not measure total engineering cost.
- Video quality, speech perception and robot closed-loop task success require task-specific evaluation beyond numerical fixture agreement; optional quantization, cache, sparse attention and distilled models need separate attribution.
- VLM-only zllm/brain, CPU/NPU LCM-Dreamshaper and general Apple/text systems are covered or pending in other strands; this output does not duplicate their records.

The next discovery pass should start from the deferred frontier, especially non-Apple image/video engines, hardware-specific multimodal paths and unresolved native-core sources. It should not restart from star counts or infer eligibility from an “AI-written” label alone.
