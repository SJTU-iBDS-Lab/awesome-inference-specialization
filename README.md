<a id="top"></a>

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/header-dark-compact.svg">
  <source media="(max-width: 600px)" srcset="assets/header-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="1120" alt="Known models, hardware and workloads guide the construction, optimization and validation of a purpose-built inference stack.">
</picture>

<div align="center">

# Awesome Inference Specialization

**Specialized execution. Shared foundations.**

Purpose-built runtimes, forks and backends for specific models, hardware and workloads. Exploring whether **AI-assisted programming** changes which specialized systems are worth building.

</div>

<!-- CATALOG-START -->

<p align="center">
<sub>126 projects · 91 engines · 14 build workflows · 3 benchmarks · 18 resources</sub>
</p>

<div align="center">

[Engines](#homepage-system) · [Build](#homepage-construction) · [Validate](#homepage-validation) · [Benchmarks](#homepage-benchmark) · [Resources](#homepage-support) · [Reading](#further-reading) · [中文](README_CN.md)

<sub>By domain: [Language](#homepage-system-text) · [Image](#homepage-system-image) · [Video](#homepage-system-video) · [Audio](#homepage-system-audio) · [Multimodal](#homepage-system-multimodal)</sub>

</div>

<sub title="Catalog addition dates, not project release dates"><b>Recently added</b> · 2026-10-14 · [VibeServe / VibeSys](#project-vibesys) · [AutoMegaKernel](#project-automegakernel) · [Infire](#project-infire) · [KIE](#project-kie) · [SEIS](#project-seis) · [Updates](docs/updates.md)</sub>

<a id="featured-reading"></a>
<a id="start-here"></a>
<a id="从这里开始"></a>

## Six ways to specialize

<!-- STARTER-GRID-START -->
<table align="center">
<tr>
<td width="33%" valign="top">
<sub>01 / Agent-built engine</sub>

**[Vibe<wbr>Qwen](docs/cases.md#vibeqwen)**<br>
<sub title="Connect an agent workflow to a reported deployed engine">Workflow to model server.</sub>

</td>
<td width="33%" valign="top">
<sub>02 / Native runtime</sub>

**[Splash](docs/cases.md#splash)**<br>
<sub title="Inspect model-shaped kernels, draft execution and serving together">Metal kernels, state and serving.</sub>

</td>
<td width="33%" valign="top">
<sub>03 / Deep fork</sub>

**[llam<wbr>Ampere](docs/cases.md#llamampere)**<br>
<sub title="See what a deep fork changes and what upstream still supplies">Reuse the server. Rebuild execution.</sub>

</td>
</tr>
<tr>
<td width="33%" valign="top">
<sub>04 / Specialized backend</sub>

**[Nun<wbr>chaku](docs/cases.md#nunchaku)**<br>
<sub title="Trace packed checkpoints into fused diffusion execution">Low-bit weights meet fused execution.</sub>

</td>
<td width="33%" valign="top">
<sub>05 / Compiled execution</sub>

**[Mirage MPK](docs/cases.md#mirage)**<br>
<sub title="Follow an explicit task graph into persistent GPU execution">Task graph to persistent GPU program.</sub>

</td>
<td width="33%" valign="top">
<sub>06 / Video workflow</sub>

**[Sol-Engine](docs/cases.md#sol-engine)**<br>
<sub title="See how optimization choices are accepted and composed">Search, check and compose.</sub>

</td>
</tr>
</table>
<!-- STARTER-GRID-END -->

<sub>[Compare 12 cases](docs/representative-comparison.md) · [Cross-case synthesis](docs/synthesis.md) · Reading examples, not a ranking.</sub>

<a id="homepage-system"></a>

## Inference engines

<sub>All projects expanded; names link upstream. [Execution boundaries](docs/systems.md#system) · [Overlapping domains](docs/domains.md) · [★ Repository star snapshots · 2026-10-14](docs/homepage-metadata.md)</sub>

<a id="homepage-system-text"></a>

### Language models <sub>· 51</sub>

- <a id="project-ane-lm"></a>**[ANE-LM](https://github.com/johnmai-dev/ANE-LM)** <sub title="johnmai-dev/ANE-LM: 144 repository stars; observed 2026-10-14">★&nbsp;144</sub> — A direct predecessor to ane.cpp, connecting Qwen ANE kernels and CPU operations through a compile cache; constrained by private interfaces and limited model coverage. <sub>[Details](docs/catalog.md#ane-lm)</sub>
- <a id="project-ane-cpp"></a>**[ane.cpp](https://github.com/skyfallsin/ane.cpp)** <sub title="skyfallsin/ane.cpp: 6 repository stars; observed 2026-10-14">★&nbsp;6</sub> — Compiles Qwen convolution programs for ANE while the CPU handles normalization, attention and KV state, informed by hardware probes and kept/discarded experiments. <sub>[Details](docs/catalog.md#ane-cpp)</sub>
- <a id="project-anemll-flash-llama"></a>**[ANEMLL Flash llama.cpp](https://github.com/Anemll/anemll-flash-llama.cpp)** <sub title="Anemll/anemll-flash-llama.cpp: 135 repository stars; observed 2026-10-14">★&nbsp;135</sub> — A llama.cpp fork with expert sidecars, slot mapping and layer-major prefill. Optional reduced top-k and shared-expert-only modes change model computation. <sub>[Details](docs/catalog.md#anemll-flash-llama)</sub>
- <a id="project-basert"></a>**[BaseRT](https://github.com/basecompute/baseRT)** <sub title="basecompute/baseRT: 231 repository stars; observed 2026-10-14">★&nbsp;231</sub> — Public conversion tools, C APIs and bindings around a proprietary native engine. The closed execution core limits kernel and performance evidence to author documentation. <sub>Multimodal · [Details](docs/catalog.md#basert)</sub>
- <a id="project-bitnet-cpp"></a>**[bitnet.cpp](https://github.com/microsoft/BitNet)** <sub title="microsoft/BitNet: 41,140 repository stars; observed 2026-10-14">★&nbsp;41.1k</sub> — An engine for compatible ternary models using packed kernels, lookup tables and shape specialization. Losslessness concerns the existing ternary representation, not arbitrary floating-point models. <sub>[Details](docs/catalog.md#bitnet-cpp)</sub>
- <a id="project-needle"></a>**[Cactus Needle](https://github.com/cactus-compute/needle)** <sub title="cactus-compute/needle: 13,915 repository stars; observed 2026-10-14">★&nbsp;13.9k</sub> — Pairs sliceable-attention models and quantized weights with platform-native engines. Model and packaging code is public, but the distributed C++ engine implementation is not. <sub>Audio · [Details](docs/catalog.md#needle)</sub>
- <a id="project-ciru-runtime"></a>**[CIRU runtime](https://github.com/ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4)** <sub title="ciru-ai/Qwen3.8-Flash-CIRU-STRIX-IU4: 20 repository stars; observed 2026-10-14">★&nbsp;20</sub> — A llama.cpp-derived runtime coupling expert paging, specialized kernels, sparse attention and speculative-state fixes to specific model formats and release builds. <sub>Multimodal · [Details](docs/catalog.md#ciru-runtime)</sub>
- <a id="project-infire"></a>**[Cloudflare Infire](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/)** <sub title="Reviewed sources">[Blog](https://blog.cloudflare.com/high-performance-llms/)</sub> — A proprietary Rust serving stack built for Cloudflare nodes, combining model-specific kernel compilation, batching and paged state with later multi-GPU support. Official engineering reports describe the design; deployment conditions differ across comparisons, and AI-assisted construction is not established. <sub>[Details](docs/catalog.md#infire)</sub>
- <a id="project-coreml-llm-cli"></a>**[CoreML LLM CLI](https://github.com/smpanaro/coreml-llm-cli)** <sub title="smpanaro/coreml-llm-cli: 131 repository stars; observed 2026-10-14">★&nbsp;131</sub> — A Llama 2 host runtime orchestrating chunked Core ML execution, KV state and IOSurface buffers; a compiled-model integration precedent to ANEMLL. <sub>[Details](docs/catalog.md#coreml-llm-cli)</sub>
- <a id="project-zero-inference"></a>**[DeepSpeed ZeRO-Inference](https://github.com/deepspeedai/DeepSpeedExamples)** <sub title="deepspeedai/DeepSpeedExamples: 6,847 repository stars; observed 2026-10-14">★&nbsp;6.8k&nbsp;(parent repo) · [Blog](https://www.deepspeed.ai/2022/09/09/zero-inference.html)</sub> — Streams CPU/NVMe weights to the GPU layer by layer, amortizing transfers with prefetch and large batches. A throughput-oriented offload precedent predating recent coding agents. <sub>[Details](docs/catalog.md#zero-inference)</sub>
- <a id="project-dwarfstar"></a>**[DwarfStar](https://github.com/antirez/ds4)** <sub title="antirez/ds4: 23,840 repository stars; observed 2026-10-14">★&nbsp;23.8k</sub> — An explicitly AI-assisted native runtime for selected models, combining resident non-routed state with bounded SSD expert caching; model and backend support is deliberately limited. <sub>[Details](docs/catalog.md#dwarfstar)</sub>
- <a id="project-exllamav3"></a>**[ExLlamaV3](https://github.com/turboderp-org/exllamav3)** <sub title="turboderp-org/exllamav3: 1,661 repository stars; observed 2026-10-14">★&nbsp;1.7k</sub> — An EXL3-centered runtime coupling low-bit execution, quantized paged KV and shape-qualified decode paths; numerical behavior and coverage depend on configuration. <sub>[Details](docs/catalog.md#exllamav3)</sub>
- <a id="project-fiddler"></a>**[Fiddler](https://github.com/efeslab/fiddler)** <sub title="efeslab/fiddler: 268 repository stars; observed 2026-10-14">★&nbsp;268</sub> — A small-batch Mixtral prototype that computes nonresident experts on the CPU and transfers activations, illustrating the alternative to moving expert weights. <sub>[Details](docs/catalog.md#fiddler)</sub>
- <a id="project-flash-moe"></a>**[Flash-MoE](https://github.com/danveloper/flash-moe)** <sub title="danveloper/flash-moe: 4,248 repository stars; observed 2026-10-14">★&nbsp;4.2k</sub> — An AI-assisted Qwen/Metal implementation that streams quantized experts from SSD. It reduces active experts from 10 to 4, so its execution is approximate. <sub>[Details](docs/catalog.md#flash-moe)</sub>
- <a id="project-flexllmgen"></a>**[FlexLLMGen (FlexGen)](https://github.com/FMInference/FlexLLMGen)** <sub title="FMInference/FlexLLMGen: 9,346 repository stars; observed 2026-10-14">★&nbsp;9.3k</sub> — An OPT throughput runtime using GPU/CPU/disk placement, cross-microbatch weight reuse and overlapped transfers; not a general low-latency serving result. <sub>[Details](docs/catalog.md#flexllmgen)</sub>
- <a id="project-gufo-rdma"></a>**[Gufo RDMA](https://github.com/neuhaus/gufo)** <sub title="neuhaus/gufo: 11 repository stars; observed 2026-10-14">★&nbsp;11</sub> — Extends Gufo across two Strix Halo hosts, using tensor partitioning, RDMA collectives and mirrored requests to synchronize execution and speculative state. <sub>Multimodal · [Details](docs/catalog.md#gufo-rdma)</sub>
- <a id="project-halogen-flash"></a>**[Halogen Flash](https://github.com/peonist-ai/halogen-flash-server)** <sub title="peonist-ai/halogen-flash-server: 964 repository stars; observed 2026-10-14">★&nbsp;964</sub> — A model-and-chip-specific Qwen binary with mixed precision, paged n-gram lookup and dedicated expert execution. Its closed core limits implementation inspection. <sub>[Details](docs/catalog.md#halogen-flash)</sub>
- <a id="project-hilum-engine"></a>**[Hilum LLM Engine](https://github.com/hilum-labs/hilum-local-llm-engine)** <sub title="hilum-labs/hilum-local-llm-engine: 1 repository stars; observed 2026-10-14">★&nbsp;1</sub> — A llama.cpp/GGML mobile integration for Adreno/Vulkan and Metal, adjusting shader dispatch, allocation and device parameters. <sub>Multimodal · [Details](docs/catalog.md#hilum-engine)</sub>
- <a id="project-hipengine"></a>**[hipEngine](https://github.com/shisa-ai/hipEngine)** <sub title="shisa-ai/hipEngine: 88 repository stars; observed 2026-10-14">★&nbsp;88</sub> — A selected-AMD execution stack with a Python host, HIP/C++ model kernels, shared KV and continuous batching, without PyTorch in the inference path. <sub>Audio · Multimodal · [Details](docs/catalog.md#hipengine)</sub>
- <a id="project-hybrimoe"></a>**[HybriMoE](https://github.com/PKU-SEC-Lab/HybriMoE)** <sub title="PKU-SEC-Lab/HybriMoE: 123 repository stars; observed 2026-10-14">★&nbsp;123</sub> — A KTransformers-based combination of CPU/GPU expert scheduling, prefetch and caching; a precedent for placement and movement in models exceeding VRAM. <sub>[Details](docs/catalog.md#hybrimoe)</sub>
- <a id="project-ik-llama"></a>**[ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)** <sub title="ikawrakow/ik_llama.cpp: 3,300 repository stars; observed 2026-10-14">★&nbsp;3.3k</sub> — A deep llama.cpp fork extending packed formats, CPU IQK kernels and CUDA dispatch while retaining general-engine compatibility. <sub>[Details](docs/catalog.md#ik-llama)</sub>
- <a id="project-imp"></a>**[imp](https://github.com/kekzl/imp)** <sub title="kekzl/imp: 44 repository stars; observed 2026-10-14">★&nbsp;44</sub> — A C++/CUDA engine for RTX 5090-class devices, owning model execution, paged KV, graph scheduling and serving. The author explicitly discloses end-to-end coding-agent implementation. <sub>Multimodal · [Details](docs/catalog.md#imp)</sub>
- <a id="project-infernix"></a>**[Infernix](https://github.com/wallawalla47/infernix)** <sub title="Wallawalla47/Infernix: 111 repository stars; observed 2026-10-14">★&nbsp;111</sub> — An explicitly AI-assisted NInfer fork combining GPU hot-expert caching, CPU miss computation, overlapped PCIe transfers and NVMe storage. <sub>Multimodal · [Details](docs/catalog.md#infernix)</sub>
- <a id="project-kipp"></a>**[Kipp](https://github.com/Polished-Snow/Kipp)** <sub title="Polished-Snow/Kipp: 1 repository stars; observed 2026-10-14">★&nbsp;1</sub> — A C11 stack owning strict checkpoint loading, tokenization, model execution, paged KV and batched serving through isolated Metal/CUDA backends. <sub>[Details](docs/catalog.md#kipp)</sub>
- <a id="project-kie"></a>**[Kog Inference Engine (KIE)](https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/)** <sub title="Reviewed sources">[Blog](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/)</sub> — A vendor-described low-latency monokernel co-designing execution, weight streaming, sampling and multi-GPU communication. The reviewed FP16 preview uses Laneformer/DTP and eight MI300X GPUs; public engine source is not established, and these are not unchanged-model speedup results. <sub>[Details](docs/catalog.md#kie)</sub>
- <a id="project-ktransformers"></a>**[KTransformers / kt-kernel](https://github.com/kvcache-ai/ktransformers)** <sub title="kvcache-ai/ktransformers: 19,604 repository stars; observed 2026-10-14">★&nbsp;19.6k</sub> — A heterogeneous MoE backend that uses ISA-specific CPU kernels and NUMA placement for memory-heavy experts while retaining shared GPU serving infrastructure. <sub>[Details](docs/catalog.md#ktransformers)</sub>
- <a id="project-lily"></a>**[Lily](https://github.com/perplexityai/pplx-garden/tree/main/lily)** <sub title="perplexityai/pplx-garden: 942 repository stars; observed 2026-10-14">★&nbsp;942&nbsp;(parent repo)</sub> — A Rust/Metal runtime for one quantized Qwen checkpoint, owning prefill/decode and prefix caching. Its text-only, greedy, nonstreaming interface makes the compatibility trade-off explicit. <sub>[Details](docs/catalog.md#lily)</sub>
- <a id="project-lithos-metal"></a>**[Lithos Metal](https://github.com/lithos-ai/lithos-metal)** <sub title="lithos-ai/lithos-metal: 210 repository stars; observed 2026-10-14">★&nbsp;210</sub> — Compiles typed model graphs into layer-fused and conventional kernels, using Metal indirect commands and GPU-resident draft state; backend coverage and fused numerics remain qualified. <sub>[Details](docs/catalog.md#lithos-metal)</sub>
- <a id="project-llamampere"></a>**[llamAmpere](https://github.com/JakeATX/llamAmpere)** <sub title="JakeATX/llamAmpere: 172 repository stars; observed 2026-10-14">★&nbsp;172</sub> — A deep llama.cpp fork combining Ampere verification kernels, MTP drafts and compressed KV while retaining shared serving. Separate post-trained models and quantization from engine contributions. <sub>[Details](docs/catalog.md#llamampere)</sub>
- <a id="project-llaminar"></a>**[Llaminar](https://github.com/Llaminar/llaminar)** <sub title="Llaminar/llaminar: 45 repository stars; observed 2026-10-14">★&nbsp;45</sub> — Builds native model graphs and device plans, placing stages and experts across CPU/NVIDIA/AMD devices with explicit heterogeneous communication. <sub>[Details](docs/catalog.md#llaminar)</sub>
- <a id="project-magnitude"></a>**[Magnitude](https://github.com/magnitudedev/magnitude)** <sub title="magnitudedev/magnitude: 6,719 repository stars; observed 2026-10-14">★&nbsp;6.7k</sub> — The reviewed Metal/MLX path maps typed operations to compatible kernel plans and emits specialized fused entry points. This evidence does not cover other backends. <sub>[Details](docs/catalog.md#magnitude)</sub>
- <a id="project-memra"></a>**[memra](https://github.com/avifenesh/memra)** <sub title="avifenesh/memra: 2 repository stars; observed 2026-10-14">★&nbsp;2</sub> — A Rust host connecting ahead-of-time CUDA kernels and model-specific programs, explicitly managing quantization, KV and multi-GPU placement with model/device-specific numerical checks. <sub>Multimodal · [Details](docs/catalog.md#memra)</sub>
- <a id="project-metalchat"></a>**[MetalChat](https://github.com/ybubnov/metalchat)** <sub title="ybubnov/metalchat: 23 repository stars; observed 2026-10-14">★&nbsp;23</sub> — A C++/Metal native generation path built from tensor, layer and model abstractions; an adjacent reusable-framework example whose generation tests do not establish full quality coverage. <sub>[Details](docs/catalog.md#metalchat)</sub>
- <a id="project-moe-infinity"></a>**[MoE-Infinity](https://github.com/EfficientMoE/MoE-Infinity)** <sub title="EfficientMoE/MoE-Infinity: 370 repository stars; observed 2026-10-14">★&nbsp;370</sub> — Offloads experts across memory tiers with activation-aware caching and trace-based prefetch. A residency-policy precedent; the public implementation differs from the paper system. <sub>[Details](docs/catalog.md#moe-infinity)</sub>
- <a id="project-ninfer"></a>**[NInfer](https://github.com/Neroued/ninfer)** <sub title="Neroued/ninfer: 2,990 repository stars; observed 2026-10-14">★&nbsp;3k</sub> — A native selected-Qwen runtime for one RTX 5090, owning execution, KV/CUDA graphs and request/cache management. Agent instruction files do not establish AI authorship. <sub>Multimodal · [Details](docs/catalog.md#ninfer)</sub>
- <a id="project-ninfer-3090"></a>**[NInfer-3090](https://github.com/ashalliants/ninfer-3090)** <sub title="ashalliants/ninfer-3090: 49 repository stars; observed 2026-10-14">★&nbsp;49</sub> — An NInfer fork adapted to a 24 GB RTX 3090 through new SM86 quantized kernels, memory planning and replay state, beyond a compile-target change. <sub>Multimodal · [Details](docs/catalog.md#ninfer-3090)</sub>
- <a id="project-powerinfer"></a>**[PowerInfer](https://github.com/Tiiny-AI/PowerInfer)** <sub title="Tiiny-AI/PowerInfer: 9,826 repository stars; observed 2026-10-14">★&nbsp;9.8k</sub> — A CPU/GPU runtime placing frequently activated neurons on GPU and using predictors for sparse execution. Requires compatible sparse models, not arbitrary dense weights. <sub>[Details](docs/catalog.md#powerinfer)</sub>
- <a id="project-rocmfpx"></a>**[ROCmFPX](https://github.com/ROCmFPX/ROCmFPX)** <sub title="ROCmFPX/ROCmFPX: 48 repository stars; observed 2026-10-14">★&nbsp;48</sub> — A llama.cpp downstream co-designing AMD quantization blocks, conversion policies and matching kernels; accuracy must be qualified per recipe. <sub>[Details](docs/catalog.md#rocmfpx)</sub>
- <a id="project-saragossa"></a>**[Saragossa](https://github.com/azerozero/saragossa)** <sub title="azerozero/saragossa: 8 repository stars; observed 2026-10-14">★&nbsp;8</sub> — A single-user Apple Silicon runtime for selected text/speech models, with Rust/Metal execution, resident decode state, buffers and prefix snapshots backed by regression comparisons. <sub>Audio · [Details](docs/catalog.md#saragossa)</sub>
- <a id="project-splash"></a>**[Splash](https://github.com/incoai/splash)** <sub title="incoai/splash: 1,421 repository stars; observed 2026-10-14">★&nbsp;1.4k · [Blog](https://inco.ai/blog/splash/)</sub> — A native Apple Silicon serving stack with model-specific Metal kernels, draft verification and prefix reuse. Disclosed agent assistance concerns kernels, not authorship of the entire engine. <sub>Multimodal · [Details](docs/catalog.md#splash)</sub>
- <a id="project-strata"></a>**[Strata](https://github.com/Niko1221/Strata)** <sub title="Niko1221/Strata: 23,943 repository stars; observed 2026-10-14">★&nbsp;23.9k</sub> — A selected-Qwen CPU/GPU engine combining hot-expert residency with tiered KV management. Some paths use approximate expert skipping; AI authorship is not established. <sub>[Details](docs/catalog.md#strata)</sub>
- <a id="project-strix-llama-cpp"></a>**[strix-llama.cpp](https://github.com/halo-box/strix-llama.cpp)** <sub title="halo-box/strix-llama.cpp: 231 repository stars; observed 2026-10-14">★&nbsp;231</sub> — A llama.cpp fork with Strix Halo fusion kernels and speculative-state management. Optional speculative prefill is approximate; accepting agent contributions does not establish AI authorship. <sub>Multimodal · [Details](docs/catalog.md#strix-llama-cpp)</sub>
- <a id="project-swiftlet"></a>**[Swiftlet](https://github.com/leonickson1/Swiftlet)** <sub title="leonickson1/Swiftlet: 659 repository stars; observed 2026-10-14">★&nbsp;659</sub> — An explicitly AI-assisted Swift/Metal reconstruction of selected Qwen hybrid-MoE paths, combining expert containers, caching and native state with documented reference checks. <sub>[Details](docs/catalog.md#swiftlet)</sub>
- <a id="project-swiftlm"></a>**[SwiftLM](https://github.com/SharpAI/SwiftLM)** <sub title="SharpAI/SwiftLM: 780 repository stars; observed 2026-10-14">★&nbsp;780</sub> — Reworks expert reads, asynchronous I/O and generation synchronization in MLX Swift and maintained forks to explicitly stream oversized MoE models from SSD. <sub>Multimodal · [Details](docs/catalog.md#swiftlm)</sub>
- <a id="project-tensorfold"></a>**[TensorFold](https://github.com/ashhart/TensorFold)** <sub title="ashhart/TensorFold: 1,314 repository stars; observed 2026-10-14">★&nbsp;1.3k</sub> — A native Zig runtime for qualified models and formats, using packed-layout contracts and Metal/CUDA paths; projection fusion requires compatible packing. <sub>[Details](docs/catalog.md#tensorfold)</sub>
- <a id="project-tuff"></a>**[TUFF](https://github.com/rexmhall09/TUFF)** <sub title="rexmhall09/TUFF: 52 repository stars; observed 2026-10-14">★&nbsp;52</sub> — A Swift/Metal streaming-runtime fork adding model-specific forward paths, bounded expert loading and a separate service, illustrating adaptation across MoE families. <sub>Multimodal · [Details](docs/catalog.md#tuff)</sub>
- <a id="project-turbo-fieldfare"></a>**[TurboFieldfare](https://github.com/drumih/turbo-fieldfare)** <sub title="drumih/turbo-fieldfare: 6,923 repository stars; observed 2026-10-14">★&nbsp;6.9k</sub> — A Gemma runtime for memory-limited Apple Silicon using bounded expert-read slots and chunked prefill, with documented accepted and discarded construction experiments. <sub>Multimodal · [Details](docs/catalog.md#turbo-fieldfare)</sub>
- <a id="project-uzu"></a>**[Uzu](https://github.com/trymirai/uzu)** <sub title="trymirai/uzu: 2,298 repository stars; observed 2026-10-14">★&nbsp;2.3k</sub> — A reusable edge engine combining Rust model blocks, native Metal dispatch, model conversion and generated bindings. Source availability alone does not establish AI authorship. <sub>[Details](docs/catalog.md#uzu)</sub>
- <a id="project-vllm-radiance"></a>**[vLLM Radiance](https://github.com/magiccodingman/vllm-radiance)** <sub title="magiccodingman/vllm-radiance: 116 repository stars; observed 2026-10-14">★&nbsp;116</sub> — Retains vLLM serving while rebuilding RDNA4 paths with pinned patches and HIP kernels; low-bit arithmetic and speculative execution require separate equivalence checks. <sub>Multimodal · [Details](docs/catalog.md#vllm-radiance)</sub>
- <a id="project-vte"></a>**[VTE](https://github.com/kyuubyN/VTE)** <sub title="kyuubyN/VTE: 0 repository stars; observed 2026-10-14">★&nbsp;0</sub> — A consumer-RDNA3 stack owning GGUF parsing, template-generated HIP kernels, VRAM management and decode-graph replay around memory and driver constraints. <sub>[Details](docs/catalog.md#vte)</sub>
- <a id="project-zinc"></a>**[ZINC](https://github.com/zolotukhin/zinc)** <sub title="zolotukhin/zinc: 521 repository stars; observed 2026-10-14">★&nbsp;521</sub> — A Zig runtime owning model loading, forward graphs, KV and serving over native Vulkan/HIP and other backends; each device path needs separate qualification. <sub>[Details](docs/catalog.md#zinc)</sub>

<sub>[↑ Engines](#homepage-system)</sub>

<a id="homepage-system-image"></a>

### Image generation and processing <sub>· 12</sub>

- <a id="project-brodiffusion"></a>**[brodiffusion](https://github.com/wlejon/brodiffusion)** <sub title="wlejon/brodiffusion: 1 repository stars; observed 2026-10-14">★&nbsp;1</sub> — A C++ image runtime owning loading, diffusion pipelines and samplers, with shape/state-qualified denoising-graph replay over a reused brotensor backend. <sub>[Details](docs/catalog.md#brodiffusion)</sub>
- <a id="project-diffusion-rs"></a>**[diffusion-rs](https://github.com/EricLBuehler/diffusion-rs)** <sub title="EricLBuehler/diffusion-rs: 130 repository stars; observed 2026-10-14">★&nbsp;130</sub> — FLUX loading, sampling, quantization and residency on a reusable Rust tensor layer; a reuse/offload reference without inferred coding-agent authorship. <sub>[Details](docs/catalog.md#diffusion-rs)</sub>
- <a id="project-draw-things"></a>**[Draw Things Community](https://github.com/drawthingsai/draw-things-community)** <sub title="drawthingsai/draw-things-community: 587 repository stars; observed 2026-10-14">★&nbsp;587</sub> — Public Swift model graphs, samplers and hardware execution components for local generation, including approximate TeaCache reuse. Their availability does not establish that the entire product is open source. <sub>Video · [Details](docs/catalog.md#draw-things)</sub>
- <a id="project-edge-dit"></a>**[edge-dit.cpp](https://github.com/THU-MIG/edge-dit.cpp)** <sub title="THU-MIG/edge-dit.cpp: 52 repository stars; observed 2026-10-14">★&nbsp;52</sub> — A ggml-based DiT runtime owning graphs, component residency and staged offload, with quantization and tiled VAE execution for constrained memory. Cache and backend support vary by model. <sub>Video · [Details](docs/catalog.md#edge-dit)</sub>
- <a id="project-hearth"></a>**[Hearth](https://github.com/jeff-hiner/hearth)** <sub title="jeff-hiner/hearth: 2 repository stars; observed 2026-10-14">★&nbsp;2</sub> — A Rust SD pipeline owning model graphs, samplers and dependency-ordered execution while reusing CubeCL/wgpu kernels and device access. <sub>[Details](docs/catalog.md#hearth)</sub>
- <a id="project-iris"></a>**[Iris](https://github.com/antirez/iris.c)** <sub title="antirez/iris.c: 1,996 repository stars; observed 2026-10-14">★&nbsp;2k</sub> — A native image pipeline in C with Metal/CPU kernels, mapped weights and text-encoder release after conditioning, illustrating ownership of the graph and its execution. <sub>[Details](docs/catalog.md#iris)</sub>
- <a id="project-mflux"></a>**[MFLUX](https://github.com/mflux-community/mflux)** <sub title="mflux-community/mflux: 2,480 repository stars; observed 2026-10-14">★&nbsp;2.5k</sub> — Native selected-image-model implementations on MLX, with load-time quantization and adapter merging; a useful contrast between framework-level ports and deeper execution redesign. <sub>[Details](docs/catalog.md#mflux)</sub>
- <a id="project-nunchaku"></a>**[Nunchaku](https://github.com/nunchux-ai/nunchaku)** <sub title="nunchux-ai/nunchaku: 3,959 repository stars; observed 2026-10-14">★&nbsp;4k</sub> — A diffusion backend that fuses SVDQuant low-bit matrix multiplication with low-rank branches. Quantization, offload and cache gains require separate attribution. <sub>[Details](docs/catalog.md#nunchaku)</sub>
- <a id="project-saient-quartz"></a>**[Quartz](https://github.com/SaientAI/saient-quartz)** <sub title="SaientAI/saient-quartz: 7 repository stars; observed 2026-10-14">★&nbsp;7</sub> — Image generation on a custom Rust tensor backend with native Wan work in progress. Demonstrated mobile Wan uses a separate C++ companion, not the native Rust path. <sub>Language · Video · [Details](docs/catalog.md#saient-quartz)</sub>
- <a id="project-stable-diffusion-cpp"></a>**[stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)** <sub title="leejet/stable-diffusion.cpp: 7,670 repository stars; observed 2026-10-14">★&nbsp;7.7k</sub> — Native ggml-based image/video loading, conditioning, sampling and component placement, with quantization and VAE tiling. Optional approximate caching is separate from the native rewrite. <sub>Video · [Details](docs/catalog.md#stable-diffusion-cpp)</sub>
- <a id="project-stable-diffusion-rs"></a>**[stable-diffusion.rs](https://github.com/andreinknv/stable-diffusion.rs)** <sub title="andreinknv/stable-diffusion.rs: 1 repository stars; observed 2026-10-14">★&nbsp;1</sub> — Rust diffusion models and samplers with documented Candle-to-MLX migration and reference checks; agent task instructions do not establish AI authorship. <sub>[Details](docs/catalog.md#stable-diffusion-rs)</sub>
- <a id="project-streamdiffusion"></a>**[StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion)** <sub title="cumulo-autumn/StreamDiffusion: 10,822 repository stars; observed 2026-10-14">★&nbsp;10.8k</sub> — Reorganizes Diffusers into StreamBatch with residual guidance, input filtering and optional compilation; approximate guidance and skipped frames change outputs or workload. <sub>Video · [Details](docs/catalog.md#streamdiffusion)</sub>

<sub>[↑ Engines](#homepage-system)</sub>

<a id="homepage-system-video"></a>

### Video generation and streaming <sub>· 10</sub>

- <a id="project-fastvideo"></a>**[FastVideo](https://github.com/hao-ai-lab/FastVideo)** <sub title="hao-ai-lab/FastVideo: 4,601 repository stars; observed 2026-10-14">★&nbsp;4.6k</sub> — An integrated video runtime owning model implementations, loading and staged denoising, with optional sparsity, parallelism and offload. Sparse or distilled paths may change the model. <sub>Audio · [Details](docs/catalog.md#fastvideo)</sub>
- <a id="project-inferix"></a>**[Inferix](https://github.com/alibaba-damo-academy/Inferix)** <sub title="alibaba-damo-academy/Inferix: 140 repository stars; observed 2026-10-14">★&nbsp;140 · [Paper](https://arxiv.org/abs/2511.20714)</sub> — A semi-autoregressive world-model runtime separating persistent generation KV, VAE chunking and streamed video output. This execution redesign does not establish AI-assisted construction. <sub>[Details](docs/catalog.md#inferix)</sub>
- <a id="project-lightx2v"></a>**[LightX2V](https://github.com/ModelTC/LightX2V)** <sub title="ModelTC/LightX2V: 2,903 repository stars; observed 2026-10-14">★&nbsp;2.9k</sub> — A video execution stack combining model-specific paths, storage contracts and double-buffered weight loading. Attribute quantization, distilled weights and lightweight VAE changes separately. <sub>Image · Audio · [Details](docs/catalog.md#lightx2v)</sub>
- <a id="project-minimax-h3-mlx"></a>**[MiniMax-H3 MLX](https://github.com/PipeNetwork/minimax-h3-mlx)** <sub title="PipeNetwork/minimax-h3-mlx: 83 repository stars; observed 2026-10-14">★&nbsp;83</sub> — An MLX reconstruction of joint MiniMax-H3 audio/video diffusion, precomputing timestep conditioning and staging component residency; quantization mainly affects capacity. <sub>Audio · [Details](docs/catalog.md#minimax-h3-mlx)</sub>
- <a id="project-streamdiffusion-v2"></a>**[StreamDiffusionV2](https://github.com/chenfengxu714/StreamDiffusionV2)** <sub title="chenfengxu714/StreamDiffusionV2: 580 repository stars; observed 2026-10-14">★&nbsp;580</sub> — Reorganizes causal Wan chunked denoising, stage scheduling and distributed KV ownership. Causal/distilled checkpoints and optional lightweight decoding change the comparison target. <sub>[Details](docs/catalog.md#streamdiffusion-v2)</sub>
- <a id="project-telefuser"></a>**[TeleFuser](https://github.com/Tele-AI/TeleFuser)** <sub title="Tele-AI/TeleFuser: 32 repository stars; observed 2026-10-14">★&nbsp;32</sub> — Co-designs generation stages and streaming scheduling, separating resident session state from GPU execution leases with backpressure. Optional cache, sparsity and precision modes change semantics. <sub>Image · Audio · Multimodal · [Details](docs/catalog.md#telefuser)</sub>
- <a id="project-turbodiffusion"></a>**[TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)** <sub title="thu-ml/TurboDiffusion: 3,855 repository stars; observed 2026-10-14">★&nbsp;3.9k</sub> — A video stack combining low-precision/sparse attention, timestep-distilled weights and optional quantized layers. Separate model and step-count changes from implementation gains. <sub>[Details](docs/catalog.md#turbodiffusion)</sub>
- <a id="project-vidax"></a>**[Vidax](https://github.com/FlyingGiraffe/vidax)** <sub title="FlyingGiraffe/vidax: 21 repository stars; observed 2026-10-14">★&nbsp;21</sub> — Ports video graphs and checkpoint layouts to JAX/Flax TPU meshes, explicitly composing tensor/sequence sharding, attention kernels and component placement. <sub>[Details](docs/catalog.md#vidax)</sub>
- <a id="project-videosys"></a>**[VideoSys](https://github.com/NUS-HPC-AI-Lab/VideoSys)** <sub title="NUS-HPC-AI-Lab/VideoSys: 2,025 repository stars; observed 2026-10-14">★&nbsp;2k</sub> — An integrated video execution reference combining type-specific attention reuse with dynamic sequence parallelism. Attention broadcast is approximate and model support is bounded. <sub>[Details](docs/catalog.md#videosys)</sub>
- <a id="project-xdit"></a>**[xDiT](https://github.com/xdit-project/xDiT)** <sub title="xdit-project/xDiT: 2,737 repository stars; observed 2026-10-14">★&nbsp;2.7k · [Paper](https://arxiv.org/abs/2411.01738)</sub> — A distributed DiT framework combining sequence-parallel schemes and patch pipelines. Earlier-step feature reuse differs from exact synchronous execution; supported combinations are constrained. <sub>Image · [Details](docs/catalog.md#xdit)</sub>

<sub>[↑ Engines](#homepage-system)</sub>

<a id="homepage-system-audio"></a>

### Speech and audio <sub>· 9</sub>

- <a id="project-aria"></a>**[Aria](https://github.com/matteospanio/aria)** <sub title="matteospanio/aria: 10 repository stars; observed 2026-10-14">★&nbsp;10</sub> — A C Stable Audio 3 pipeline owning conditioning, diffusion, sampling and audio decoding, with disclosed LLM assistance and controlled reference tests; construction cost remains unknown. <sub>[Details](docs/catalog.md#aria)</sub>
- <a id="project-parakeet-axiom"></a>**[parakeet.cpp (axiom)](https://github.com/Frikallo/parakeet.cpp)** <sub title="Frikallo/parakeet.cpp: 306 repository stars; observed 2026-10-14">★&nbsp;306</sub> — A C++ Parakeet reconstruction on axiom, owning encoder/decoder and streaming caches while reusing CPU/MPSGraph tensor backends; local checks are not end-to-end results. <sub>[Details](docs/catalog.md#parakeet-axiom)</sub>
- <a id="project-parakeet-ggml"></a>**[parakeet.cpp (ggml)](https://github.com/mudler/parakeet.cpp)** <sub title="mudler/parakeet.cpp: 840 repository stars; observed 2026-10-14">★&nbsp;840</sub> — Ports NeMo speech features, encoder/decoder graphs and cache-aware streaming sessions to C++/ggml, with GGUF conversion and reference-parity fixtures. <sub>[Details](docs/catalog.md#parakeet-ggml)</sub>
- <a id="project-qingming-qwen3-tts"></a>**[Qingming Qwen3-TTS](https://github.com/uulong950/qingming-qwen3-tts)** <sub title="uulong950/qingming-qwen3-tts: 6 repository stars; observed 2026-10-14">★&nbsp;6</sub> — Separate native Qwen3-TTS paths for 24 GB RX 7900 XTX and RTX 4090 devices, explicitly partitioning resident generation and streaming-decoder resources. <sub>[Details](docs/catalog.md#qingming-qwen3-tts)</sub>
- <a id="project-qwen-asr-c"></a>**[Qwen-ASR (C)](https://github.com/antirez/qwen-asr)** <sub title="antirez/qwen-asr: 623 repository stars; observed 2026-10-14">★&nbsp;623</sub> — A C reconstruction of Qwen3-ASR preprocessing, encoder, autoregressive decoding and chunked streaming state, with explicit CPU and optional GPU responsibilities. <sub>[Details](docs/catalog.md#qwen-asr-c)</sub>
- <a id="project-qwen3-tts-c"></a>**[Qwen3-TTS (C)](https://github.com/gabriele-mastrapasqua/qwen3-tts)** <sub title="gabriele-mastrapasqua/qwen3-tts: 116 repository stars; observed 2026-10-14">★&nbsp;116</sub> — Rebuilds the Qwen3-TTS talker, code predictor and waveform decoder in C, with reference checks and measurement corrections; engineering task files do not establish AI authorship. <sub>[Details](docs/catalog.md#qwen3-tts-c)</sub>
- <a id="project-voxgen"></a>**[VoxGen](https://github.com/NullMagic2/VoxGen)** <sub title="NullMagic2/VoxGen: 7 repository stars; observed 2026-10-14">★&nbsp;7</sub> — A Rust VoxCPM2 reconstruction with direct Vulkan buffer/shader management and incremental PCM state; RDNA3 configurations have separate tuning and qualification scopes. <sub>[Details](docs/catalog.md#voxgen)</sub>
- <a id="project-whisper-cpp"></a>**[whisper.cpp](https://github.com/ggml-org/whisper.cpp)** <sub title="ggml-org/whisper.cpp: 54,359 repository stars; observed 2026-10-14">★&nbsp;54.4k</sub> — An established native Whisper/ggml speech runtime with converted weights and multiple backends; a historical reference, not evidence of recent AI-driven construction savings. <sub>[Details](docs/catalog.md#whisper-cpp)</sub>
- <a id="project-whisperkit"></a>**[WhisperKit](https://github.com/argmaxinc/argmax-oss-swift)** <sub title="argmaxinc/argmax-oss-swift: 6,405 repository stars; observed 2026-10-14">★&nbsp;6.4k</sub> — Swift orchestration of Core ML speech preprocessing, encoder/decoder, caches and segmentation, illustrating the execution boundary between compiled models and their host runtime. <sub>[Details](docs/catalog.md#whisperkit)</sub>

<sub>[↑ Engines](#homepage-system)</sub>

<a id="homepage-system-multimodal"></a>

### Multimodal and cross-domain <sub>· 9</sub>

- <a id="project-brain"></a>**[BRaiN](https://github.com/swedishembedded/brain)** <sub title="swedishembedded/brain: 41 repository stars; observed 2026-10-14">★&nbsp;41</sub> — Rust model implementations sharing a WGSL backend, including vision-language/video component-residency decisions; a model list does not establish full validation of every path. <sub>Language · Image · Video · Audio · [Details](docs/catalog.md#brain)</sub>
- <a id="project-cactus"></a>**[Cactus](https://github.com/cactus-compute/cactus)** <sub title="cactus-compute/cactus: 6,123 repository stars; observed 2026-10-14">★&nbsp;6.1k</sub> — A mobile runtime lowering supported model components into its own graph operations, ARM/Metal kernels and quantized state; general conversion coverage remains limited. <sub>Language · Image · Audio · [Details](docs/catalog.md#cactus)</sub>
- <a id="project-colibri"></a>**[Colibri](https://github.com/JustVugg/colibri)** <sub title="JustVugg/colibri: 41,799 repository stars; observed 2026-10-14">★&nbsp;41.8k</sub> — Architecture-specific C engines sharing selected components, with resident dense state and streamed experts. Backend, quantization and approximation choices need per-engine qualification. <sub>Language · Image · [Details](docs/catalog.md#colibri)</sub>
- <a id="project-fastflowlm"></a>**[FastFlowLM](https://github.com/ROCm/FastFlowLM)** <sub title="ROCm/FastFlowLM: 1,953 repository stars; observed 2026-10-14">★&nbsp;2k</sub> — Model-family host runtimes managing AMD NPU tensors, weights and decode streams with shape-matched kernels; original flm engines ship as prebuilt libraries. <sub>Language · Image · Audio · [Details](docs/catalog.md#fastflowlm)</sub>
- <a id="project-gufo"></a>**[Gufo](https://github.com/gufo-org/gufo)** <sub title="gufo-org/gufo: 734 repository stars; observed 2026-10-14">★&nbsp;734</sub> — A selected-model C++/HIP stack for AMD Strix Halo, owning kernels, batching and continuation caching while reusing upstream components; quality qualification is model-specific. <sub>Language · Image · Video · Audio · [Details](docs/catalog.md#gufo)</sub>
- <a id="project-pmetal"></a>**[PMetal](https://github.com/Epistates/pmetal)** <sub title="Epistates/pmetal: 327 repository stars; observed 2026-10-14">★&nbsp;327</sub> — An Apple Silicon training/inference SDK combining model implementations, native inference bridges and device operators, illustrating specialized execution within a broader ecosystem. <sub>General · [Details](docs/catalog.md#pmetal)</sub>
- <a id="project-tensorrt-edge-llm"></a>**[TensorRT Edge-LLM](https://github.com/NVIDIA/TensorRT-Edge-LLM)** <sub title="NVIDIA/TensorRT-Edge-LLM: 588 repository stars; observed 2026-10-14">★&nbsp;588</sub> — An edge-deployment reference combining ONNX export and TensorRT compilation with C++ decoding, KV and multimodal embedding management. <sub>Language · Image · Audio · [Details](docs/catalog.md#tensorrt-edge-llm)</sub>
- <a id="project-vla-simd"></a>**[vla.simd](https://github.com/cair-vinuni/vla.simd)** <sub title="cair-vinuni/vla.simd: 24 repository stars; observed 2026-10-14">★&nbsp;24</sub> — Native C++/CPU-SIMD operators, GGUF loading and action inference for selected vision-language-action policies. Throughput and numerical tests do not establish closed-loop safety. <sub>[Details](docs/catalog.md#vla-simd)</sub>
- <a id="project-zllm"></a>**[zLLM](https://github.com/zllm-lab/zllm)** <sub title="zllm-lab/zllm: 11 repository stars; observed 2026-10-14">★&nbsp;11</sub> — Rust model/backend-specific loading, execution and state management covering vision-language, image generation and video restoration; each combination has its own support boundary. <sub>Language · Image · Video · Audio · [Details](docs/catalog.md#zllm)</sub>

<sub>[↑ Engines](#homepage-system)</sub>

<a id="homepage-construction"></a>

## Build and optimize

Group workflows by what they produce. Compiler and agent involvement describe the method; they do not turn a generated kernel into a complete engine.

[Construction boundaries and sources](docs/systems.md#construction)

<a id="homepage-construction-execution"></a>
<a id="homepage-construction-construction"></a>

<a id="homepage-construction-kernels"></a>

### Operator kernels (2)

Emits or migrates individual accelerator kernels.

- <a id="project-akg-agents"></a>**[AKG Agents](https://github.com/mindspore-ai/akg)** <sub title="mindspore-ai/akg: 262 repository stars; observed 2026-10-14">★&nbsp;262&nbsp;(parent repo)</sub> — Builds and migrates accelerator operators through multi-agent search, code generation, backend validation and profiling; a kernel-construction workflow, not a complete inference engine. <sub>General · [Details](docs/catalog.md#akg-agents)</sub>
- <a id="project-atrex-kernel-agent"></a>**[Atrex Kernel Agent (AKA)](https://github.com/alibaba/atrex-kernel-agent)** <sub title="alibaba/atrex-kernel-agent: 177 repository stars; observed 2026-10-14">★&nbsp;177</sub> — Runs coding agents in isolated worktrees to generate operator kernels, applying numerical/performance gates and revising with profiler feedback and retrieved knowledge; not a complete engine. <sub>General · [Details](docs/catalog.md#atrex-kernel-agent)</sub>

<a id="homepage-construction-programs"></a>

### Model programs and compiled artifacts (7)

Emits composed forward programs, compiled model packages or executable graphs; hosting responsibilities differ.

- <a id="project-anemll"></a>**[ANEMLL](https://github.com/Anemll/Anemll)** <sub title="Anemll/Anemll: 1,693 repository stars; observed 2026-10-14">★&nbsp;1.7k</sub> — Splits, quantizes and converts models into stateful Core ML packages with Swift/Python orchestration; actual ANE placement remains a Core ML decision. <sub>Language · [Details](docs/catalog.md#anemll)</sub>
- <a id="project-automegakernel"></a>**[AutoMegaKernel](https://github.com/RightNow-AI/AutoMegaKernel)** <sub title="RightNow-AI/AutoMegaKernel: 151 repository stars; observed 2026-10-14">★&nbsp;151 · [Paper](https://arxiv.org/html/2606.09682v1)</sub> — A Llama-family compiler and agent harness that emits one CUDA megakernel per forward pass through a checked schedule IR. The host still drives decoding. Static checks are not a whole-stack proof, and reported W8A16 wins use precision-asymmetric baselines. <sub>Language · [Details](docs/catalog.md#automegakernel)</sub>
- <a id="project-kernelagent"></a>**[KernelAgent](https://github.com/meta-pytorch/KernelAgent)** <sub title="meta-pytorch/KernelAgent: 587 repository stars; observed 2026-10-14">★&nbsp;587</sub> — Partitions PyTorch programs into fusible subgraphs, generates Triton kernels and composes forward execution using correctness and hardware feedback. Finite tests do not prove general correctness. <sub>General · [Details](docs/catalog.md#kernelagent)</sub>
- <a id="project-mirage"></a>**[Mirage Persistent Kernel](https://github.com/mirage-project/mirage)** <sub title="mirage-project/mirage: 2,551 repository stars; observed 2026-10-14">★&nbsp;2.6k</sub> — Compiles an explicitly assembled LLM task graph into persistent CUDA execution with GPU workers scheduling computation and communication across decode steps; coverage depends on implemented graphs and tasks. <sub>Language · [Details](docs/catalog.md#mirage)</sub>
- <a id="project-mlc-llm"></a>**[MLC LLM](https://github.com/mlc-ai/mlc-llm)** <sub title="mlc-ai/mlc-llm: 23,239 repository stars; observed 2026-10-14">★&nbsp;23.2k</sub> — A TVM-based model compiler and MLCEngine runtime, fusing operations and specializing small-batch computation and KV kernels; illustrates portability trade-offs in compiled deployment. <sub>Language · [Details](docs/catalog.md#mlc-llm)</sub>
- <a id="project-onediff"></a>**[OneDiff](https://github.com/siliconflow/onediff)** <sub title="siliconflow/onediff: 1,961 repository stars; observed 2026-10-14">★&nbsp;2k</sub> — Adapts diffusion components to OneFlow/Nexfort compilation and graph reuse. Public adapter code does not establish visibility of every compiler core. <sub>Image · Video · [Details](docs/catalog.md#onediff)</sub>
- <a id="project-stable-fast"></a>**[Stable Fast](https://github.com/chengzeyi/stable-fast)** <sub title="chengzeyi/stable-fast: 1,305 repository stars; observed 2026-10-14">★&nbsp;1.3k</sub> — Incrementally specializes Diffusers through TorchScript tracing, fused operators and optional CUDA graphs; numerical behavior and graph compatibility require workload-specific checks. <sub>Image · Video · [Details](docs/catalog.md#stable-fast)</sub>

<a id="homepage-construction-stacks"></a>

### Runtime construction and integrated optimization (5)

Builds a server or integrates changes into a model runtime. Kernel generation, configuration search and whole-engine construction are distinct scopes.

- <a id="project-agentcompile"></a>**[AgentCompile](https://github.com/veneno1213822/AgentCompile)** <sub title="veneno1213822/AgentCompile: 7 repository stars; observed 2026-10-14">★&nbsp;7</sub> — Uses an LLM to select bounded CUDA templates and generate fused kernels for a runtime. Reviewed generic verification/timing paths contain skipped checks and placeholders. <sub>Language · Image · [Details](docs/catalog.md#agentcompile)</sub>
- <a id="project-metainfer"></a>**[MetaInfer](https://github.com/MetaInfer/MetaInfer)** <sub title="HuangPuStar/MetaInfer: 113 repository stars; observed 2026-10-14">★&nbsp;113 · [Paper](https://arxiv.org/abs/2607.12875) · [Case report](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/)</sub> — Orchestrates coding agents to construct deployment-specific servers and checks fixed correctness/performance contracts, connecting to VibeQwen. Finite prompt checks do not establish numerical equivalence. <sub>Language · [Details](docs/catalog.md#metainfer)</sub>
- <a id="project-seis"></a>**[SEIS: Self-Evolving Inference Systems](https://github.com/smth-fun/self-evolving-inference-system)** <sub title="smth-fun/self-evolving-inference-system: 0 repository stars; observed 2026-10-14">★&nbsp;0 · [Paper](https://arxiv.org/html/2610.04646v1) · [Blog](https://github.com/smth-fun/self-evolving-inference-system/blob/bf2ddc5c5882a2573756b744c0e88c1b154739fa/posts/post-2-evolve.md)</sub> — A fixed coding agent repeatedly refactors mini-sglang through inherited code and reports, coordinating kernels, runtime and decoding. Quantization changes numerics; the H100 paper results and the public ten-trial Blackwell example are distinct artifacts. <sub>Language · [Details](docs/catalog.md#seis)</sub>
- <a id="project-sol-engine"></a>**[Sol-Engine](https://github.com/NVlabs/Sana/tree/sol-engine)** <sub title="NVlabs/Sana: 9,293 repository stars; observed 2026-10-14">★&nbsp;9.3k&nbsp;(parent repo)</sub> — An agent-guided video optimization workflow integrating model-specific fusion, state reuse, approximate caches and sparse attention with visual checks; each change needs separate validation and attribution. <sub>Image · Video · [Details](docs/catalog.md#sol-engine)</sub>
- <a id="project-vibesys"></a>**[VibeServe / VibeSys](https://github.com/uw-syfi/vibesys)** <sub title="uw-syfi/vibesys: 114 repository stars; observed 2026-10-14">★&nbsp;114 · [Paper](https://arxiv.org/html/2605.06068v1) · [Blog](https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/)</sub> — An agent framework for model-, hardware- and workload-specific serving stacks, with design search, implementation and framework-owned evaluation. The VibeServe paper and current VibeSys code are different revisions; generated systems remain scenario- and contract-specific. <sub>Language · Audio · Multimodal · [Details](docs/catalog.md#vibesys)</sub>

<a id="homepage-validation"></a>

## Validation: coverage and gaps

Four contracts, with six source-inspected method entries. Checks embedded in a project are linked below without counting another repository. These methods were not executed here.

| Object | Available methods and observed coverage | Remaining gap |
| --- | --- | --- |
| <a id="homepage-validation-numerical"></a>[Operator / subgraph numerics](docs/validation.md#numerical) | Compare reference outputs under explicit shapes, dtypes and tolerances.<br>[KernelBench](#project-kernelbench): Reference and evaluator-integrity checks.<br>[FastKernels](#project-fastkernels): Kernel-to-pipeline replacement checks; coverage depends on the task.<br>[Atrex-Bench](#project-atrex-bench): Output structure, numerical errors and mutation checks. | Finite tested inputs; not automatic coverage of every model, device or persistent state. |
| <a id="homepage-validation-model-state"></a>[Composed model and state](docs/validation.md#model-state) | Check the assembled forward program separately from persistent engine state.<br>[KernelAgent composition](#project-kernelagent): Optional --verify reference self-test of the composed forward program. | The listed composition check does not cover KV isolation, resets, batching or long trajectories; these need separate tests. |
| <a id="homepage-validation-quality"></a>[Generated-output quality](docs/validation.md#quality) | Compare admitted approximations against a specified reference and quality threshold.<br>[Sol-Engine LPIPS and visual review](#project-sol-engine): Sampled-frame perceptual comparisons and visual checks. | Sampled frames do not fully assess temporal consistency; unequal lengths may compare only a common prefix. Unavailable scoring is not a pass. |
| <a id="homepage-validation-service"></a>[Service and integration](docs/validation.md#service) | Exercise startup, requests, responses and the intended candidate.<br>[MetaInfer inference-framework oracle](#project-metainfer): Runs serve.sh and judges configured prompts using an LLM or heuristic fallback. | Plausible responses do not prove tensor parity or concurrency safety; prompt judging is not numerical equivalence. |

Validation cost includes reference execution, candidate compilation, device/judge calls and human review. Compare costs under the same acceptance contract; a weaker check is not an equivalent efficiency improvement.

[Implementation evidence and validation design](docs/validation.md)

<a id="homepage-benchmark"></a>

## Benchmarks

Tasks and comparison protocols complement the checks above. Match model, device, precision, workload, state and quality before comparing results.

- <a id="project-atrex-bench"></a>**[Atrex-Bench](https://github.com/alibaba/atrex-bench)** <sub title="alibaba/atrex-bench: 36 repository stars; observed 2026-10-14">★&nbsp;36</sub> — Production-sourced operator tasks, reference programs and shape generators with separate agent-visible inputs and evaluator metadata; checks compilation/numerics/timing, not whole-stack acceleration. <sub>General · [Details](docs/catalog.md#atrex-bench)</sub>
- <a id="project-fastkernels"></a>**[FastKernels](https://github.com/Snowflake-AI-Research/fastkernels)** <sub title="Snowflake-AI-Research/fastkernels: 7 repository stars; observed 2026-10-14">★&nbsp;7 · [Paper](https://arxiv.org/abs/2605.23215)</sub> — Integrates candidate operators into deployment-shaped pipelines, checking kernel numerics/timing and end-to-end outputs/latency; separates local tolerance tests from model behavior. <sub>Language · Image · Video · Audio · Multimodal · General · [Details](docs/catalog.md#fastkernels)</sub>
- <a id="project-kernelbench"></a>**[KernelBench](https://github.com/ScalingIntelligence/KernelBench)** <sub title="ScalingIntelligence/KernelBench: 1,290 repository stars; observed 2026-10-14">★&nbsp;1.3k</sub> — Compiles generated kernels, compares randomized inputs against PyTorch references and times passing candidates; evaluates construction tasks, not deployed-engine gains. <sub>General · [Details](docs/catalog.md#kernelbench)</sub>

[Benchmark scope and comparison protocols](docs/benchmarks.md)

<a id="homepage-support"></a>

## Companion resources

Selected resources with a concrete construction, reuse or comparison relationship to an included system—not a general GPU-tool directory.

<a id="homepage-support-diagnostics"></a>

### Performance diagnosis

- <a id="project-ncu-report-skill"></a>**[ncu-report-skill](https://github.com/mit-han-lab/ncu-report-skill)** <sub title="mit-han-lab/ncu-report-skill: 255 repository stars; observed 2026-10-14">★&nbsp;255</sub> — Extracts Nsight Compute metrics and source-level stalls to connect measured bottlenecks with candidate optimizations; a diagnosis workflow, not an inference engine. <sub>General · [Details](docs/catalog.md#ncu-report-skill)</sub>

[Relationships and sources](docs/resources.md#diagnostics)

<a id="homepage-support-knowledge"></a>

### Construction knowledge and experience

- <a id="project-kernelwiki"></a>**[KernelWiki](https://github.com/mit-han-lab/KernelWiki)** <sub title="mit-han-lab/KernelWiki: 509 repository stars; observed 2026-10-14">★&nbsp;509</sub> — Indexes kernel optimization experience, documents and upstream changes by hardware and symptom, retaining artifact provenance; a searchable knowledge resource, not a runtime. <sub>General · [Details](docs/catalog.md#kernelwiki)</sub>
- <a id="project-ane-field-guide"></a>**[Apple Neural Engine Field Guide](https://github.com/skyfallsin/apple-neural-engine-field-guide)** <sub title="skyfallsin/apple-neural-engine-field-guide: 3 repository stars; observed 2026-10-14">★&nbsp;3</sub> — MIL/ANE probes and CPU-reference checks recording kept/discarded M3 Max experiments whose findings inform ane.cpp; a knowledge resource, not another engine. <sub>Language · [Details](docs/catalog.md#ane-field-guide)</sub>

[Relationships and sources](docs/resources.md#knowledge)

<a id="homepage-support-engine-baselines"></a>

### General-engine baselines

- <a id="project-vllm"></a>**[vLLM](https://github.com/vllm-project/vllm)** <sub title="vllm-project/vllm: 93,743 repository stars; observed 2026-10-14">★&nbsp;93.7k</sub> — A general-engine comparison for VibeQwen and a serving foundation reused by Radiance, with paged KV, prefix sharing and continuous batching. <sub>Language · [Details](docs/catalog.md#vllm)</sub>
- <a id="project-sglang"></a>**[SGLang](https://github.com/sgl-project/sglang)** <sub title="sgl-project/sglang: 37,110 repository stars; observed 2026-10-14">★&nbsp;37.1k</sub> — A shared serving foundation for systems such as KTransformers, with radix-prefix KV reuse and cache-aware scheduling. Reuse depends on compatible prefixes and configuration. <sub>Language · [Details](docs/catalog.md#sglang)</sub>
- <a id="project-tensorrt-llm"></a>**[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)** <sub title="NVIDIA/TensorRT-LLM: 14,807 repository stars; observed 2026-10-14">★&nbsp;14.8k</sub> — A general-engine reference for VibeQwen combining NVIDIA kernels, chunked-context scheduling, dynamic batching and paged KV; comparisons must match precision and workload. <sub>Language · Multimodal · [Details](docs/catalog.md#tensorrt-llm)</sub>
- <a id="project-llama-cpp"></a>**[llama.cpp](https://github.com/ggml-org/llama.cpp)** <sub title="ggml-org/llama.cpp: 131,111 repository stars; observed 2026-10-14">★&nbsp;131.1k</sub> — A shared native foundation for specialized forks, with GGUF loading, GGML graphs and backend quantized kernels; useful for distinguishing inherited infrastructure from execution changes. <sub>Language · [Details](docs/catalog.md#llama-cpp)</sub>

[Relationships and sources](docs/resources.md#engine-baselines)

<a id="homepage-support-compilers"></a>

### Compilers and kernel languages

- <a id="project-tvm"></a>**[Apache TVM](https://github.com/apache/tvm)** <sub title="apache/tvm: 13,830 repository stars; observed 2026-10-14">★&nbsp;13.8k</sub> — The compiler foundation beneath MLC LLM, providing graph transformations, tensor scheduling and target code generation. Model and serving policies remain higher-level responsibilities. <sub>Language · General · [Details](docs/catalog.md#tvm)</sub>
- <a id="project-tensorrt"></a>**[NVIDIA TensorRT](https://github.com/NVIDIA/TensorRT)** <sub title="NVIDIA/TensorRT: 13,406 repository stars; observed 2026-10-14">★&nbsp;13.4k</sub> — Builds NVIDIA engines around shape profiles and kernel tactics and underlies Edge-LLM. The public repository exposes plugins/examples, not the complete optimizer and runtime core. <sub>Language · Image · General · [Details](docs/catalog.md#tensorrt)</sub>
- <a id="project-triton"></a>**[Triton](https://github.com/triton-lang/triton)** <sub title="triton-lang/triton: 20,369 repository stars; observed 2026-10-14">★&nbsp;20.4k</sub> — A code-generation foundation for KernelAgent and others, specializing tiled kernels and launch configurations by target/signature/constants; it does not own model loading or service validation. <sub>Language · Image · Video · General · [Details](docs/catalog.md#triton)</sub>
- <a id="project-tilelang"></a>**[TileLang](https://github.com/tile-ai/tilelang)** <sub title="tile-ai/tilelang: 8,598 repository stars; observed 2026-10-14">★&nbsp;8.6k</sub> — A kernel language used by Atrex, compiling tiled programs through target layouts and software pipelining. Its generated kernels are distinct from a complete model runtime. <sub>Language · Image · Video · General · [Details](docs/catalog.md#tilelang)</sub>

[Relationships and sources](docs/resources.md#compilers)

<a id="homepage-support-components"></a>

### Reusable execution and model preparation

- <a id="project-deepcompressor"></a>**[DeepCompressor](https://github.com/nunchux-ai/deepcompressor)** <sub title="nunchux-ai/deepcompressor: 802 repository stars; observed 2026-10-14">★&nbsp;802</sub> — Calibrates low-bit quantization and SVDQuant decompositions and exports weights for backends such as Nunchaku. Model preparation and simulated evaluation are distinct from runtime acceleration. <sub>Language · Image · [Details](docs/catalog.md#deepcompressor)</sub>
- <a id="project-qtip"></a>**[QTIP](https://github.com/Cornell-RelaxML/qtip)** <sub title="Cornell-RelaxML/qtip: 195 repository stars; observed 2026-10-14">★&nbsp;195</sub> — Trellis-coded weights with matching matrix-vector kernels, referenced by ExLlamaV3. The public interactive path lacks fusion used for the main reported timings. <sub>Language · [Details](docs/catalog.md#qtip)</sub>
- <a id="project-marlin"></a>**[Marlin](https://github.com/IST-DASLab/marlin)** <sub title="IST-DASLab/marlin: 1,162 repository stars; observed 2026-10-14">★&nbsp;1.2k</sub> — An INT4 execution component referenced by ExLlamaV3, combining offline repacking with load/dequantization/matmul pipelining; not a complete inference service. <sub>Language · [Details](docs/catalog.md#marlin)</sub>
- <a id="project-flash-linear-attention"></a>**[Flash Linear Attention](https://github.com/fla-org/flash-linear-attention)** <sub title="fla-org/flash-linear-attention: 5,859 repository stars; observed 2026-10-14">★&nbsp;5.9k</sub> — Linear-attention and recurrent-state kernels reused by ExLlamaV3, with chunked prefill and state updates for compatible architectures; not equivalent replacements for arbitrary softmax attention. <sub>Language · [Details](docs/catalog.md#flash-linear-attention)</sub>
- <a id="project-flash-attention"></a>**[FlashAttention](https://github.com/Dao-AILab/flash-attention)** <sub title="Dao-AILab/flash-attention: 25,132 repository stars; observed 2026-10-14">★&nbsp;25.1k</sub> — Reusable IO-aware attention kernels with fused reductions and KV-update interfaces. Exact mathematical attention does not imply bitwise identity or whole-system speedup. <sub>Language · [Details](docs/catalog.md#flash-attention)</sub>
- <a id="project-sageattention"></a>**[SageAttention](https://github.com/thu-ml/SageAttention)** <sub title="thu-ml/SageAttention: 3,967 repository stars; observed 2026-10-14">★&nbsp;4k</sub> — Reusable attention kernels combining outlier smoothing with hardware-specific INT8/FP8 paths. Operator speed and quality checks do not substitute for full video-pipeline validation. <sub>Language · Image · Video · [Details](docs/catalog.md#sageattention)</sub>
- <a id="project-flashinfer"></a>**[FlashInfer](https://github.com/flashinfer-ai/flashinfer)** <sub title="flashinfer-ai/flashinfer: 6,613 repository stars; observed 2026-10-14">★&nbsp;6.6k</sub> — Selects or generates kernels by precision, head geometry and cache layout, including paths reused by MoE-Infinity; not a standalone inference server. <sub>Language · [Details](docs/catalog.md#flashinfer)</sub>

[Relationships and sources](docs/resources.md#components)

**Embedded knowledge:** Atrex GPU Wiki connects optimization traces and retrieved experience to later construction attempts; it remains part of Atrex. [How it is used](docs/resources.md#embedded-knowledge).

<a id="further-reading"></a>

## Further reading

Additional cases extend the six starting routes into hardware constraints, memory movement, audio, model porting and action inference.

| Case | Reading benefit |
| --- | --- |
| [Gufo](docs/cases.md#gufo) | Study a device-focused stack with explicit per-model quality limits |
| [Flash-MoE](docs/cases.md#flash-moe) | Separate SSD streaming from changes to the model computation |
| [LightX2V](docs/cases.md#lightx2v) | Inspect explicit asynchronous weight-storage contracts |
| [Vidax](docs/cases.md#vidax) | Follow model conversion and numerical debugging across devices |
| [Aria](docs/cases.md#aria) | Read an AI disclosure beside an inspectable parity harness |
| [vla.simd](docs/cases.md#vla-simd) | Distinguish native action inference from robot task success |

**Mechanism index:** <a id="homepage-system-memory"></a>[Data residency & movement](docs/catalog.md#memory) · <a id="homepage-system-precision"></a>[Numerical representation](docs/catalog.md#precision) · <a id="homepage-system-selection"></a>[Selective computation](docs/catalog.md#selection) · <a id="homepage-system-reuse"></a>[Computation reuse](docs/catalog.md#reuse) · <a id="homepage-system-decoding"></a>[Generation order](docs/catalog.md#decoding) · <a id="homepage-system-serving"></a>[Parallelism & scheduling](docs/catalog.md#serving) · <a id="homepage-system-execution"></a>[Compiled & native execution](docs/catalog.md#execution)

[All cases](docs/cases.md) · [Full comparison](docs/comparison.md) · [Mechanism index](docs/catalog.md) · [Research questions](docs/research-agenda.md) · [Latest updates](docs/updates.md)

<!-- CATALOG-END -->

<a id="what-belongs-here"></a>
<a id="read-the-evidence"></a>

## Scope and evidence

A record needs a documented relationship to **building or validating a specialized execution stack**. General frameworks, libraries and historical systems provide concrete reuse relationships and comparison points; a thin wrapper or a generic optimization alone is insufficient. [Inclusion rules](docs/taxonomy.md).

Descriptions summarize reviewed public sources, not independently reproduced benchmarks. Keep runtime improvements separate from quantization, omitted computation and changed models. AI participation requires direct disclosure or an inspectable workflow; it does not by itself establish lower lifecycle cost. [Evidence policy](docs/evidence-policy.md).

[Contribute or correct a record](CONTRIBUTING.md) · [Maintain the bilingual homepage](docs/homepage-maintenance.md) · [Visual map](assets/specialization.svg)

Project identities and domain coverage come from the [catalog](catalog/projects.csv); concise descriptions are maintained in matching [English](catalog/homepage_en.json) and [Chinese](catalog/homepage_cn.json) records. Original metadata, diagrams, commentary and scripts use [MIT](LICENSE); linked projects and models retain their own licenses.

<sub>[Layout and banner maintenance](docs/homepage-visual-design.md) · [↑ Back to top](#top)</sub>
