# Homepage stars and source links / 首页 Star 与来源入口

[Home](../README.md) · [中文首页](../README_CN.md) · [Content maintenance](homepage-maintenance.md)

## What the number means

`★` is the upstream **repository's** GitHub `stargazers_count`, not a project-quality, correctness, production-readiness or performance score. The catalog remains domain-first and alphabetic within sections; stars neither rank entries nor decide inclusion. Values are compacted for display (for example, `1.2k`); the exact count, stable repository ID, canonical name and observation date remain in [github_stats.json](../catalog/github_stats.json). Hover text provides the exact count and date as a convenience, not as the only record.

A directory, branch or component within a larger repository is explicitly labeled **parent repo / 母仓库**. URL-based detection covers Lily and Sol-Engine; explicit editorial overrides cover root-linked subprojects such as AKG Agents and DeepSpeed ZeRO-Inference. A parent repository's stars are not attributed to its subproject. Infire and KIE have no confirmed independent public engine repository here, so they receive no star number. Neither an absent repository nor a failed fetch is displayed as zero.

These are **weekly snapshots, not live counters**. Each repository has its own `fetched_on` and `last_attempt_on`. A failed refresh retains the last successful count and date, marks it `cached / 缓存`, and records the error. A repository with no successful observation omits the star mark. The displayed date range covers only actual observations; it does not claim that missing repositories were checked successfully. Snapshot dates never replace the catalog's technical `checked_on` dates.

Star 数量仅表示上游仓库的关注度，保留发现小众项目的能力，不按 Star 排名或设收录门槛。母仓库数量单独标明；无公开仓库不补零。读取失败保留原数值和原观测日期，首次失败则不显示数值。技术核查日期与关注度采集日期相互独立。

## Refresh during weekly maintenance

```sh
# Inspect the due set without network access or file changes.
python scripts/refresh_github_stats.py

# Optional GITHUB_TOKEN or GH_TOKEN must be provided securely by the environment.
# No token, credential or private repository data is written to the snapshot.
python scripts/refresh_github_stats.py --refresh --max-repositories 160
python scripts/update_readme.py
python scripts/generate_banner.py --check
python scripts/validate_catalog.py
python scripts/update_readme.py --check
python -m unittest discover -s tests
```

The updater uses the official [repository metadata endpoint](https://docs.github.com/en/rest/repos/repos#get-a-repository), serial capped requests, seven-day freshness and conditional ETags. It stops on authentication/rate-limit responses rather than retrying aggressively, follows redirects only within `api.github.com`, and refuses a changed repository ID. Access failure is not a reason to remove an entry. `--strict` makes an incomplete refresh fail the command; either mode preserves valid cached values. Check the printed partial-refresh report before describing coverage. No new scheduled GitHub workflow is installed: use the existing weekly maintenance task. Ordinary README generation and CI remain completely offline.

## Paper and blog shortcuts

[homepage_metadata.json](../catalog/homepage_metadata.json) contains editorially selected source links with explicit provenance. They must already occur in that project's reviewed record or primary case, or in the reviewed reading list. Missing papers or blogs have no placeholder. A case report about a generated engine is labeled **Case report**, not represented as the generator's implementation or paper. The full evidence record remains authoritative; shortcuts do not imply a fresh source audit.

Both homepages use the same URLs and localized labels. Do not guess a paper from a similar project name, automatically label any external page a blog, or copy links from unrelated dependencies. Add newly discovered sources to their evidence records first.

## Recently added

The compact recent line shows up to five explicitly recorded additions. `added_on` is the date of addition to this catalog, **not** a project's publication date, release date or source-review date. The initial dates refer to the SEIS and literature additions recorded in [updates](updates.md). A metadata refresh alone never makes an old entry newly added. Append new project IDs when they are actually admitted; do not infer dates from `checked_on`.

## Presentation boundary

Stars are text, not remote badges. No remote image service, custom CSS, JavaScript, font or new website is needed. Keep the existing banners, reading cards, unique upstream links, complete expanded listing, domain order and all source-backed descriptions. This change adds discovery information; it does not recertify any engine's claims.
