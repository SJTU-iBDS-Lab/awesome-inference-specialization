# Source review: construction workflows and industrial execution

Reviewed on **2026-10-14**, starting from `7dd83ff`. This is a focused follow-up on six named candidates, not an exhaustive survey or independent performance reproduction.

[Home](../README.md) · [Reading list](reading-list.md) · [Updates](updates.md)

## Decisions

| Work | Decision | Evidence boundary |
| --- | --- | --- |
| VibeServe / VibeSys | Add one construction record and the VibeServe case | May paper and lab blog; separately pinned current README and evaluation wiring. Do not duplicate the renamed repository or include unrelated VibeSys tasks. |
| AutoMegaKernel | Add a model-program construction record and case | Paper, agent harness and schedule-IR implementation. Restricted schedule generation is not unconstrained whole-runtime synthesis. |
| Cloudflare Infire | Add an industrial runtime record and case | Two official engineering reports; proprietary core, no source-level verification. Initial and later multi-GPU stages are distinct. |
| Kog Inference Engine | Add an industrial co-design record and case | Technical article plus matching preview report; engine source not established. Preserve the Laneformer/DTP, FP16, batch-one and eight-GPU conditions. |
| ForgeMegakernel | Add to reading and validation discussion; no separate software record yet | Paper reviewed. Exact-name GitHub and web searches did not establish an official implementation. This is a retrieval limitation, not proof that code does not exist. |
| Retire the Abstractions | Add as a perspective in the reading list | First-party Hazy Research account, not a software project or controlled cost study. |

## What the review changes

**Construction has different output boundaries.** VibeServe targets serving stacks. AutoMegaKernel emits a per-forward program through a fixed VM/IR and separate instruction/schedule loops. The ForgeMegakernel paper describes per-model decode generation integrated with SGLang. These should not be counted as the same kind of artifact.

**Checks must retain their actual scope.** AutoMegaKernel's inspected validator has task-count-capped data-hazard checks and assumes its supported IR and trusted VM. ForgeMegakernel describes reference KV/logit checks and functional probes, not a mechanized correctness proof. Its public implementation remains unverified in this review.

**Industrial specialization is not automatically evidence of AI authorship.** Infire supplies a platform-focused reconstruction example; KIE supplies model/runtime/device co-design. Operational performance does not establish lower construction cost. No AI-development attribution was established for either from the reviewed reports.

## Discovery and follow-up

Use papers and citations, author/lab blogs and vendor engineering reports as discovery routes, then follow canonical code and implementation evidence. News is a lead, not the final authority. Do not filter candidates by stars or require the term “inference engine” in a title. Conversely, a promising title or related dependency is insufficient for inclusion.

For ForgeMegakernel, recheck the authors' paper landing page and any subsequently linked repository before changing artifact status. Do not treat the arXiv abstract and HTML rendering as two independent implementation sources. For the admitted records, retain the exact reviewed revisions and distinguish later maintenance from historical paper results.

## Reviewed primary sources

- VibeServe: [paper](https://arxiv.org/html/2605.06068v1), [SyFI lab report](https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/), [current VibeSys README](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/README.md), [host evaluation wiring](https://github.com/uw-syfi/vibesys/blob/140baf9df1d16238c13143f84bb67526525b9baf/src/vibesys/core_wiring.py).
- AutoMegaKernel: [paper](https://arxiv.org/html/2606.09682v1), [agent integration contract](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/HARNESS.md), [schedule IR and validator](https://github.com/RightNow-AI/AutoMegaKernel/blob/884534c4d2dbed4381576f81a79ae97feca53c34/schedule/ir.py).
- Infire: [initial design report](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/), [later large-model and multi-GPU work](https://blog.cloudflare.com/high-performance-llms/).
- KIE: [monokernel design](https://blog.kog.ai/building-a-single-kernel-latency-optimized-llm-inference-engine-on-amd-mi300x-gpus/), [preview conditions](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/).
- ForgeMegakernel: [paper](https://arxiv.org/html/2609.12379v1).
- Perspective: [Retire the Abstractions](https://hazyresearch.stanford.edu/blog/2026-08-05-retire-the-abstractions).

## 中文结论

本轮新增四项有明确边界的记录及案例：VibeServe/VibeSys、AutoMegaKernel、Infire、KIE。前两项分别是服务栈构建和模型级执行生成；后两项是工业平台特化与软硬件协同设计，不推定 AI 作者身份。ForgeMegakernel 已纳入文献及验证讨论，但未找到可确认的官方代码，不标作开源工具；Hazy Research 文章作为观点材料，不增加项目计数。检索范围限于这六项及其直接来源，未运行上游引擎、付费 Agent 或 GPU 实验，也未重新审查整个既有目录。
