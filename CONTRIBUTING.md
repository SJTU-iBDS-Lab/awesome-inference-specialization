# Contributing

Thanks for helping maintain an evidence-aware index of inference specialization.

## Suggest or add a project

Before opening a PR, check the [inclusion criteria](README.md#what-belongs-here), [taxonomy](docs/taxonomy.md), and [evidence policy](docs/evidence-policy.md). We prioritize concrete execution-level mechanisms over small code size, a single impressive benchmark number, or a large star count.

For a project addition or correction:

1. Edit **`catalog/projects.csv`** (UTF-8) with an official project URL, a technical description of what is specialized, an explicit caveat and evidence link. Do not directly edit the generated catalog section in `README.md`.
2. Choose `Core`, `Adjacent`, or `Watchlist` based on the actual implementation boundary. Use documented axes separated by `;`.
3. Set source visibility accurately: `public-code`, `closed-core`, `documentation-only`, or `review-only`.
4. Mark `ai_involvement=disclosed` only when maintainers explicitly disclose use of agents; `intrinsic` only if agent/LLM work is part of the system itself; otherwise use `not-established`.
5. Update `checked_on` to the date you checked the *direct source*; do not guess model names, supported backends, license or production readiness.
6. Run `python scripts/update_readme.py` and `python scripts/validate_catalog.py`.
7. In the PR description, explain why the project belongs and identify the exact mechanism beyond a general framework/configuration layer.

For research and benchmark submissions, provide model revision, quantization/precision, hardware, software versions, workload and baseline optimization, plus any approximate-computation/quality changes. **Independent negative results are welcome.**

## Editorial policy

- Describe verifiable implementation details, not promotional superlatives.
- Do not conflate end-to-end speedups with changes from distillation, quantization, sparse computation or reduced algorithmic work.
- We do not claim that code was AI-generated based solely on filenames such as `CLAUDE.md`.
- Avoid treating `public-code` as synonymous with OSI-compatible licensing.
- Do not list pedagogical minimal engine replicas as core evidence.
- Do not post credentials, non-public benchmark assets, or material that violates upstream licensing.

## Data dictionary

| Field | Meaning |
| --- | --- |
| `id`, `project` | Stable unique identifier and display name |
| `category`, `tier` | Presentation grouping and inclusion strength |
| `axes` | Semicolon-separated specialization axes from taxonomy |
| `target` | Concrete model/hardware/workload scope |
| `mechanism` | What changes in the execution or construction system |
| `source_visibility` | Public code vs. closed/review/docs-only |
| `ai_involvement` | `intrinsic`, `disclosed`, or `not-established` |
| `url`, `evidence_url` | Public landing page and direct source of the described mechanism |
| `caveat` | Limits, equivalence risks, or scope qualifications |
| `checked_on` | Last source-check date, ISO YYYY-MM-DD |
