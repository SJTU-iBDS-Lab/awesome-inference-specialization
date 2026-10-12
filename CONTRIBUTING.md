# Contributing

Contribute a specialized system, a concrete construction workflow, or infrastructure that supports their implementation and comparison. Connect a known constraint to an inspectable execution decision and explain its boundary. Corrections and independent negative results are as useful as additions.

## Add or correct a project

1. Read the [inclusion criteria](README.md#what-belongs-here), [taxonomy](docs/taxonomy.md) and [evidence policy](docs/evidence-policy.md).
2. Edit **`catalog/projects.csv`**. Use the canonical upstream repository; do not count renamed repositories, integration wrappers or multiple methods in the same repository twice.
3. Choose a `catalog_role` (`system`, `construction`, `support`) for the main reading order, then one primary `family` for secondary mechanism browsing. Keep modality, artifact type, mechanism tags and semantic effects independent. This is an editorial grouping, not a quality ranking.
4. Supply at least two distinct official evidence pointers, ideally a design/README plus a relevant implementation file. For closed cores, identify the public interface or documentation boundary. Two links alone do not establish correctness.
5. State a concrete scope and caveat. Note quantization, omitted work, stale state, changed models, unsupported configurations and incomplete verification where relevant.
6. Mark AI involvement only from direct disclosure or the implemented construction method. An `AGENTS.md` or `CLAUDE.md` filename alone establishes neither.
7. Set `checked_on` to the date you inspected the sources. Prefer commit-pinned evidence for version-sensitive claims. Summarize the inspection depth and discovery path in the PR.
8. Regenerate and validate the five views:

```sh
python scripts/update_readme.py
python scripts/validate_catalog.py
python scripts/update_readme.py --check
python -m unittest discover -s tests
```

Do not edit generated sections of either README, `docs/systems.md`, `docs/catalog.md`, or `docs/comparison.md` directly. The hand-written README introductions and guides can be edited normally. Use `catalog/schema.json` for controlled facets, system showcases, construction routes and supporting examples. The routes can overlap; distinguish generated kernels, composed model programs and complete servers. Update both homepages and the diagrams when changing the classification.

## Data dictionary

Schema version: **3**. `catalog_role` separates systems, concrete construction workflows and supporting infrastructure. The former `category`, `tier`, `axes` and single `evidence_url` fields have been replaced; no high/low inclusion tier remains.

| Field | Meaning |
| --- | --- |
| `id`, `project` | Stable identifier and display name; preserve identifiers when renaming |
| `catalog_role` | Main reading role: system, construction workflow or supporting infrastructure; not a quality tier |
| `family` | One of eight secondary mechanism browsing families in `schema.json` |
| `domains` | Semicolon-separated inspected modalities: text, image, video, audio, multimodal, general |
| `artifact_type` | Runtime, backend, compiler, optimizer, kernel library, research prototype, generator or verification tool |
| `constraints` | Semicolon-separated concise tags for the known deployment assumptions |
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

The dated survey is a historical account. Do not silently rewrite its counts when adding later records; add a dated follow-up when appropriate.

## Comparisons and attribution

Report model/checkpoint, precision, hardware, software revision, workload, cache conditions, tuned baseline and quality criterion. Separate runtime improvements from distillation, reduced steps, expert dropping and quantization. Public code does not automatically imply an OSI-compatible license or a complete shipping product.

Original diagrams explain mechanisms, not measured speedups. Cite upstream material rather than copying a project's figures or performance claims without context. Do not submit credentials, non-public benchmark assets or third-party material without permission.
