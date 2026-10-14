# Homepage visual design / 首页视觉维护

[Home](../README.md) · [中文首页](../README_CN.md) · [Content maintenance](homepage-maintenance.md)

## Presentation, not a new taxonomy

The homepage keeps the complete project list and its domain-first organization. The visual layer supplies a compact theme-aware banner, one primary navigation row, a domain shortcut row and six reading cards. Project names link upstream; details link to the existing evidence records. The cards are examples of construction approaches, not a performance or maturity ranking.

The introductory copy is maintained outside the generated markers in each README. `scripts/homepage_layout.py` generates the counts, navigation, cards and catalog. Long-form case explanations remain in the case collection and comparison; cards use a short label with the full reading rationale available as a tooltip and in the linked comparison.

保留全量项目、按领域组织的引擎目录及既有证据。视觉层只负责头图、导航、六个阅读入口和信息主次，不新建分类，也不把清单改为折叠面板。

## Components

| Component | Rule |
| --- | --- |
| Banner | Four self-contained SVGs: light/dark × wide/compact. A conceptual diagram, not a performance claim. |
| Navigation | One main row and one domain row. No repeated table of contents. |
| Six cards | A two-row, three-column HTML table; short copy, relative case links and no per-card images. |
| Project entries | Keep every source-backed description, important limitation and upstream link. Do not repeat the section's domain; retain additional domains as secondary text. |
| Mechanisms | Keep the full mechanism index and legacy anchors in further reading. |
| Counts | Generated from the catalog, not manually updated numbers in image assets. |

GitHub-compatible markup is intentional: no scripts, inline CSS, custom classes, external fonts or remote image services. Native Markdown remains the body format. Responsive `<picture>` sources supply compact diagrams on narrow screens; the default image is the light wide variant. The original conceptual diagrams remain available.

## Regenerate and check

```sh
python scripts/generate_banner.py
python scripts/update_readme.py
python scripts/generate_banner.py --check
python scripts/validate_catalog.py
python scripts/update_readme.py --check
python -m unittest discover -s tests
```

The banner generator uses only the Python standard library. Its generated assets are checked by `tests/test_homepage_visual.py`, so normal catalog CI also detects stale diagrams. Homepage tests preserve complete, unique project coverage, description text, source links, evidence boundaries and the six selected cases.

检查应同时覆盖中英文、浅色／深色及窄屏。特别检查图片回退、卡片文字换行、目录锚点和额外领域标签。不要以“美化”为由删除专家缩减、闭源核心或验证占位等关键限制。

## Review boundary

The 2026-10-13 presentation update was checked with local Chromium previews using GitHub-like Markdown typography at desktop and narrow widths. These are local layout checks, not screenshots captured from a signed-in GitHub session and not a claim that all clients render identically. GitHub remains responsible for final HTML sanitization and platform styling. No upstream engine benchmarks were run, and source-review dates were not changed.

本次排版检查不等于重新审查所有上游项目，也不代表重新复现引擎性能。来源日期、项目内容、案例数据与许可保持原有边界。

## 2026-10-14 metadata refinement

Project names now carry compact repository-star text and selected Paper / Blog / Case report shortcuts. Subproject counts are explicitly parent-repository totals. A single recent-additions line uses admission dates rather than release dates. See [metadata rules](homepage-metadata.md). No remote badges or new visual framework are introduced; the six reading cards and original descriptions are unchanged.
