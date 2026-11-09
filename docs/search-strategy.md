# Discovery vocabulary and search workflow / 关键词库与检索方法

[Home](../README.md) · [中文首页](../README_CN.md) · [Contributing](../CONTRIBUTING.md) · [Latest pass](discovery-2026-11-08.md)

The maintained [keyword bank](../catalog/search_keywords.json) supplies search terms, device/model variants and query templates. [Run records](../catalog/search_runs/) preserve what was actually queried and returned. Neither file is an admission list: [projects.csv](../catalog/projects.csv) remains the catalog authority.

`catalog/discovery.json` serves a different purpose: it routes readers to **already admitted** projects by hardware/model. Do not put unreviewed search hits in those homepage routes.

## Vocabulary structure

| Group | Example terms | What to check after a hit |
| --- | --- | --- |
| Engine identity / 专用定位 | specialized inference, native inference, fixed-shape execution | Which computation is specialized, and for which target? |
| System synthesis / 系统构建 | engine construction harness, generated inference engine, SkySynth | Is the output a kernel, model program or serving engine? |
| Agent optimization / 优化循环 | self-evolving inference, candidate acceptance, optimization workbench | Who edits the candidate and who controls acceptance? |
| Kernel execution / 内核执行 | megakernel, persistent decode, device-side scheduling | Does model dispatch actually invoke the implementation? |
| Expert residency / 专家驻留 | CPU-GPU co-execution, bandwidth-adaptive, expert cache | Is work computed elsewhere, moved, cached or omitted? |
| State / 状态 | GDN state, semantic anchor, state rollback | Are state ownership and repeated execution checked? |
| Speculation / 投机 | DFlash2, MTP, tree verification | What target/reference and sampling contract are preserved? |
| Representation / 数值表示 | FTW, NVFP4, W4A8, scale bias packing | Which changes affect precision or model behavior? |
| Workloads / 服务负载 | dual ubatch, decode lanes, AI-SQL, query-aware inference | Which latency, throughput and concurrency conditions apply, and are reused input tokens counted? |
| Validation / 验证 | teacher forcing, source fingerprint, mutation testing | What finite acceptance rule is actually enforced? |
| Other domains / 其他模型领域 | DiT compiler, streaming TTS engine, VLA inference | Separate model/step changes from runtime improvements |

The bank also carries **hardware terms** such as R9700/gfx1201, Strix Halo/gfx1151, RK3588/RKNPU2, DGX Spark/GB10, Apple/Metal/ANE and Ascend, and **model terms** such as Flash-Next, LFM2.5, Flint, H3 and Qwen3-TTS. Grouping helps retrieval; it does not make two chips, model versions or checkpoints equivalent.

## How to query

Start with one artifact/construction phrase and one mechanism, model or device. Run small independent queries; do not require every synonym at once. The JSON templates use `{since}`, `{model}`, `{hardware}`, `{mechanism}` and `{seed}` placeholders; replace them before sending a query.

Examples for GitHub repository search:

```text
"specialized inference" in:name,description,readme pushed:>={since} archived:false
"inference engine" "coding agents" in:name,description,readme archived:false
"expert cache" "RK3588" in:name,description,readme archived:false
"inference" "Metal" fork:only pushed:>={since}
```

For web search, use ordinary phrases and `site:github.com` when useful; do not copy GitHub-only qualifiers into a web query. For known projects, fetch the official repository and inspect its references directly rather than relying on search ranking.

Broad `synthesis` retrieves speech and image synthesis; broad `RSI` retrieves general agents. Narrow the construction query with engine/model/harness terms. Keep separate audio/video searches rather than globally excluding TTS or diffusion. Stars, language, AI claims and “from scratch” branding are not filters for admission.

## A repeatable pass

1. **Establish the baseline.** Record the target catalog commit and current admitted URLs/IDs.
2. **Search complementary windows.** Use a recent-push pass for active work, a creation-date pass for newly created repositories, and an undated pass for dependencies and missed older work. Record the actual date interval; repository creation is not release time.
3. **Vary the route.** Include construction, execution mechanisms, at least one non-LLM domain and a fork-only pass. Rotate less-covered hardware/model combinations. A recurring schedule is not implied or configured by this guide.
4. **Follow relationships.** Inspect acknowledgements, VENDORED/NOTICE, benchmark baselines, generated-output links and relevant author organizations. Record the exact relation; a cited algorithm is not automatically shared code.
5. **Triage and normalize.** Resolve canonical repository identity; separate renamed repos, packages and substantial forks. Record inspected commit, source files, status and remaining checks. Leave unknowns unknown.
6. **Apply existing admission rules.** Trace actual execution/construction and its upstream reuse, numerical/model changes and verification limits before editing the bilingual catalog. A search hit or source file inventory alone does not pass this gate.

## Record the search, including misses

Run records use `searched_on` for retrieval, distinct from a project's technical `checked_on`. Save exact query/surface, page, result cap, returned repository names, inspected revisions and remaining work. A full page means the sample may be capped; it does not reveal the total number of hits. If a known seed is absent, split the query, query it directly or follow a source relationship. No result is not evidence that no implementation exists.

The [November 8 record](../catalog/search_runs/2026-11-08.json) retains broad/noisy probes as observations. Its 20 GitHub queries each returned 20 names; only seven selected leads received bounded source inspection. Subsequent passes can record more pages or different ordering, but must label their coverage accurately.

Maintain the vocabulary when a source introduces a useful synonym or a query repeatedly misses relevant work. Keep observed productive phrases, narrow ambiguous combinations, and retire stale template choices only with a reason. Do not turn the raw hit log into a second “awesome” list or automatically promote a candidate.

## Query-aware follow-up — 2026-11-09

The [Quail source review](source-review-2026-11-09.md) adds eight workload/accounting terms and two query templates: **139 terms in 11 groups and 22 templates**. These cover AI-SQL, semantic filters/joins, query-aware inference and KV regret. Distinguish SQL invoking a model from NL2SQL. This targeted source review does not replay or alter the November 8 search record; the new templates are vocabulary for subsequent searches, not claims of executed queries.

## 中文维护约定

词表负责“怎样找”，运行记录负责“实际找了什么”，正式目录负责“哪些已经通过收录核查”。三者分开维护，避免检索日期冒充源码核查日期，也避免生成器、生成产物、同仓库多个模型与上游派生重复计数。关键词更新应以本轮命中和漏检为依据，保留对既有框架之上的实质改造，不以是否 Python／MLX、是否有 Star 或是否宣称 AI 编写作简单筛选。
