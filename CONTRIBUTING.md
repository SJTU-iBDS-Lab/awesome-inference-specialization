# Contributing

Contribute evidence about **how specialized execution stacks are built, who can obtain and maintain them, and what they cost**. A core case should explain why another execution path was built, the decisions it controls, what it reuses or gives up, actual construction and AI participation, and unresolved validation and maintenance costs. Corrections, failed attempts and independent negative results are as useful as successful cases.

The survey does not require a new project, AI involvement or an implementation from scratch. General engines, compilers, libraries and evaluators remain as shared foundations and comparison points. Teaching-oriented “nano” reproductions of standard engines are outside scope; small size alone does not exclude a substantive execution system. Adding entries or maximizing counts is not the objective.

## Add or correct a project

1. Read the [scope](README.md#what-belongs-here), [taxonomy](docs/taxonomy.md), [selected cases](docs/cases.md) and [evidence policy](docs/evidence-policy.md).
2. Edit **`catalog/projects.csv`** for repository-level facts. Use the canonical upstream repository; do not count renamed repositories, integration wrappers or multiple methods in the same repository twice. Keep the existing inventory when changing editorial focus.
3. Assign `survey_role` (`core`, `adjacent`, `foundation`) and a concise English `relevance_note` explaining why the project belongs in this survey. This describes its relation to the research question, not quality, age or AI authorship. A `core` project must be associated with a selected case.
4. Independently choose `catalog_role` (`system`, `construction`, `support`) for the delivered software, then one primary `family` for secondary mechanism browsing. Keep modality, artifact type, mechanisms and semantic effects independent.
5. Supply at least two distinct official evidence pointers, ideally a design/README plus a relevant implementation file. For closed cores, identify the public interface or documentation boundary. Two links alone do not establish correctness.
6. State concrete scope and caveats: quantization, omitted work, stale state, changed models, unsupported configurations and incomplete verification where relevant. Do not infer that a kernel generator delivers a complete engine.
7. Mark AI involvement only from direct disclosure or an inspected construction method. Name the actual work and human intervention where known; an `AGENTS.md` or `CLAUDE.md` filename alone establishes neither authorship nor saved cost.
8. Set `checked_on` to the direct source-review date. Prefer commit-pinned evidence for sensitive or version-dependent claims. Summarize inspection depth and discovery path in the PR.
9. Add or update the associated selected case when the change affects a core project's construction account. Regenerate and validate all six views using the commands below.

## Add or correct a selected case

Edit **`catalog/cases.json`**, a top-level array, rather than the generated `docs/cases.md`. Cases answer the construction question and link to repository records through `project_ids`; they are not extra repository entries. Preserve stable identifiers and distinguish workflow evidence from evidence about a reported output.

For example, VibeQwen belongs in a case linking the MetaInfer project and the relevant Baseten output report. Do not add a duplicate VibeQwen repository row without an independently identified upstream project. A named output or blog report is not itself evidence that a separate public repository exists.

Write concise English case prose and a Chinese `summary_cn`. Unknown effort or maintenance data should be stated explicitly. Do not fill gaps with inferred numbers or convert a reported build time into total cost.

| Case field | Required content |
| --- | --- |
| `id`, `title` | Stable case identifier and descriptive title |
| `project_ids` | List of existing project identifiers involved in the case |
| `summary`, `summary_cn` | Concise English and Chinese accounts of why this is a useful case |
| `motivation` | Why another execution path was built; distinguish stated rationale from an established limitation of alternatives |
| `boundary` | Execution decisions controlled and the actual artifact/integration boundary |
| `reuse` | Existing frameworks, libraries, runtimes, kernels or models retained |
| `tradeoff` | Generality, compatibility, dynamism, portability or features restricted by the choice; distinguish observed omissions from stated intent |
| `construction` | Concrete implementation, adaptation, compilation/search or agent workflow and its output |
| `ai_role` | Specific disclosed or inspected AI participation and limits of attribution |
| `cost` | Measured or reported construction/operating costs and unknown items; include the accounting boundary |
| `validation` | Reference, acceptance criteria, inspected checks, reproduction status and coverage gaps |
| `maintenance` | Known update/rebuild obligations, observed maintenance evidence and unknown costs |
| `evidence_urls` | List of direct official evidence links supporting the case's separate claims |
| `checked_on` | ISO date of source inspection |

Every `core` project needs a case association. A case may also reference an adjacent project or foundation where needed to explain its construction or counterfactual. Do not promote all dependencies to core merely because a case uses them.

## Regenerate and validate

```sh
python scripts/update_readme.py
python scripts/validate_catalog.py
python scripts/update_readme.py --check
python -m unittest discover -s tests
```

The six generated views are the catalog sections of `README.md` and `README_CN.md`, plus `docs/cases.md`, `docs/systems.md`, `docs/catalog.md` and `docs/comparison.md`. Do not edit those outputs directly. Hand-written README introductions and guides can be edited normally.

Use `catalog/schema.json` for controlled facets and navigation configuration, `catalog/projects.csv` for project records, and `catalog/cases.json` for selected-case narratives. Keep both homepages and original diagrams consistent with classification changes. Construction routes can overlap; distinguish generated kernels, composed model programs and complete servers. The homepage should foreground cases and research questions rather than entry totals.

## Project data dictionary

Schema version: **4**. `survey_role` describes relevance to the survey; `catalog_role` describes the software's role. Neither is a quality tier, and neither replaces `artifact_type` or mechanism families. The former `category`, `tier`, `axes` and single `evidence_url` fields remain superseded.

| Field | Meaning |
| --- | --- |
| `id`, `project` | Stable identifier and display name; preserve identifiers when renaming |
| `survey_role` | `core` case, `adjacent` historical/neighboring route, or `foundation` infrastructure/reference |
| `relevance_note` | Required concise English explanation of why the project belongs in this survey |
| `catalog_role` | Delivered-software role: system, construction workflow or supporting infrastructure |
| `family` | One of eight secondary mechanism/tool browsing families in `schema.json` |
| `domains` | Semicolon-separated inspected modalities: text, image, video, audio, multimodal, general |
| `artifact_type` | Runtime, backend, compiler, optimizer, kernel library, research prototype, generator or verification tool |
| `constraints` | Semicolon-separated concise tags for known deployment assumptions |
| `mechanisms` | Multiple kebab-case mechanism tags; primary family is not an exclusive boundary |
| `target` | Specific model, hardware, shape or workload scope in prose |
| `mechanism` | A concrete execution/construction decision and its implementation |
| `semantic_effect` | One or more evaluation considerations from the taxonomy; not a correctness certificate |
| `source_visibility` | Public code, closed core, documentation only or review-use restriction |
| `ai_involvement` | `intrinsic`, `disclosed`, `not-established`; the last does not mean human-only |
| `url` | Canonical official project landing page |
| `evidence_urls` | Semicolon-separated direct official evidence links |
| `caveat` | Important scope limits, semantic changes or evidence gaps |
| `checked_on` | ISO date of direct source review |
| `discovery` | `initial` (original 25), `keyword`, or `dependency` expansion; not an evidence score |

The dated survey is a historical account. Do not silently rewrite its counts when adding later records or changing focus; add a dated follow-up when appropriate.

## Comparisons and attribution

Report model/checkpoint, precision, hardware, software revision, workload, cache conditions, tuned baseline and quality criterion. Separate runtime improvements from distillation, reduced steps, expert dropping and quantization. Public code does not automatically imply an OSI-compatible license or a complete shipping product.

“AI reduced total cost” requires an explicit comparable alternative and accounting for human effort, tools/compute, unsuccessful attempts, verification, integration, operation and maintenance over a stated horizon. Otherwise describe the observation and the missing evidence. Successful selected cases alone do not establish a historical trend or a causal effect.

Original diagrams explain mechanisms and research hypotheses, not measured speedups. Cite upstream material rather than copying figures or performance claims without context. Do not submit credentials, non-public benchmark assets or third-party material without permission.
