# Evidence and comparison policy

The purpose of this catalog is to aid research, not aggregate marketing claims. Every catalog row must include a public source and an evidence link. We verify **the existence of the source and what it documents**, not automatically the advertised speedup.

## Claim strength

| Level | Evidence | Appropriate language |
| --- | --- | --- |
| E0 — assertion | Marketing text, demo only, undocumented number | “Claims …”; no comparative conclusion |
| E1 — disclosed implementation | Public code or sufficiently detailed design docs | “Implements / describes …” |
| E2 — reproducible procedure | Hardware, models, quantization, prompts, scripts, baseline and quality criterion documented | “Reports X under Y conditions …” |
| E3 — independent reproduction | Repeated under comparable conditions by independent party | “Independently reproduced for …” |

`E1` does not imply `E2`, and a public repository does not necessarily include the underlying engine source. Do not assign E3 to an author's self-benchmark.

## Minimum fair-comparison checklist

- **Model identity:** weights/checkpoint, MoE routing, layer count, quantization, MTP, tokenizer, and software versions.
- **Semantic contract:** exact execution, numerical tolerance, approximate inference, expert dropping, speculative verification, or a retrained/distilled model. State which one.
- **Hardware:** accelerator and count, host CPU, RAM/VRAM capacity, storage bandwidth, interconnect, driver/compiler versions.
- **Workload:** input/output length distribution, concurrency, batching, cache hit rate, warm/cold state, modality-specific dimensions.
- **Metrics:** LLM TTFT, TPOT, throughput, tail latency and memory; image/video latency, throughput and generated quality; amortized total service cost where relevant.
- **Strong baselines:** a *well-tuned* general engine, an optimized plugin/backend, and a focused implementation when available.
- **End-to-end attribution:** distinguish changes to **execution system** from quantization, sparsity, timestep distillation, and other model/algorithm changes.
- **Correctness:** differential output/shape tests; quality metrics for approximate paths; stateful and concurrent workloads; model- and hardware-specific corner cases.

Do not compute average speedup across projects that use different model weights, quantization, or hardware.

## Source visibility

- `public-code`: relevant source can be inspected publicly; this says nothing about independent correctness, licensing of all dependencies, or production quality.
- `closed-core`: the repository may expose deployment/configuration while the actual engine remains proprietary.
- `documentation-only`: an official documentation entry is available but should not be presented as a distinct open-source engine repository.
- `review-only`: source is visible under a review-use restriction and is **not** equivalent to a standard open-source license.

## Updating a record

Each row has `checked_on`, `url`, `evidence_url`, `caveat`, `source_visibility`, and `ai_involvement`. Preserve uncertainty rather than converting a self-report into a verified fact. Review fast-changing projects regularly; the date indicates when the record was last checked, not a promise of current validity.
