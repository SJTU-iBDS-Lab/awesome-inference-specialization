# Maintaining the bilingual homepage / 双语首页维护

[Home](../README.md) · [中文首页](../README_CN.md) · [Contributing](../CONTRIBUTING.md)

## Content sources

Project identity, upstream URL, role and domain coverage remain in [projects.csv](../catalog/projects.csv). Detailed mechanisms and evidence stay in the catalog and case records. Neither homepage is a replacement for those records.

Maintain [English summaries](../catalog/homepage_en.json) and [Chinese summaries](../catalog/homepage_cn.json) together. They must cover exactly the same project identifiers, with nonempty text. Describe the target and artifact first, then the distinctive execution decision. Keep English summaries within 60 words. The two versions need equivalent facts, not word-for-word syntax.

Preserve consequential limits in both languages: changed expert counts, approximation, a closed execution core, or incomplete verification. Generic caveats belong in the shared evidence statement rather than every sentence. New descriptions must be supported by existing records or an explicitly recorded source review.

项目身份、上游链接、角色和领域仍以 CSV 为准；首页简述不是新的源码审计。英文和中文说明须同步维护，逐项对应目标范围、产物、执行区别及关键限制。不能只在一种语言中披露专家缩减、核心闭源或验证占位。

## Layout policy

[scripts/homepage_layout.py](../scripts/homepage_layout.py) renders the reader-facing layout. [scripts/update_readme.py](../scripts/update_readme.py) calls it and retains the detailed catalog, case, domain and comparison generators.

Engine placement uses a primary model domain; all recorded domains remain short tags, and the overlapping domain index is unchanged. `ENGINE_DOMAIN_OVERRIDES` documents editorial placement for cross-domain engines. Mechanism families remain independent catalog facets; their previous homepage anchors are preserved as links to that index.

Construction groups identify the output boundary: operator kernels, model programs, or runtime construction/integrated optimization. Add a new construction project to the appropriate `CONSTRUCTION_GROUPS` entry. The generator rejects missing or duplicated membership rather than silently hiding a project.

Six `STARTER_CASE_IDS` are drawn from the canonical showcase, with the remaining selections shown under further reading. Changing a starter requires an existing showcase and case record; it is not a quality ranking. All project entries stay expanded and link upstream exactly once.

首页按主要模型领域组织引擎，机制分类继续服务于深入分析；多领域信息保留为短标签与交叉索引。构建流程按实际产物分组。首页保留全量展开，精选入口只负责导读，不替代完整清单。

## Checks

```sh
python scripts/validate_catalog.py
python scripts/update_readme.py
python scripts/update_readme.py --check
python -m unittest discover -s tests
```

The generator verifies complete bilingual coverage. Regression tests check unique project/upstream links, primary-domain navigation, all showcase reasons, validation coverage and gaps, critical bilingual caveats, local anchors and generated-view consistency.

These checks validate repository data and presentation. They do not run model engines, reproduce upstream speedups or certify the correctness of the indexed implementations. Keep source-review dates unchanged when only editing presentation.

## Weekly popularity snapshots and source shortcuts

Run `python scripts/refresh_github_stats.py --refresh` during the existing weekly maintenance task, before regenerating the README. Review partial-fetch results; never replace failed counts with zero or modify technical `checked_on` dates. Keep direct source links and actual catalog-addition dates in `catalog/homepage_metadata.json`. See [metadata rules](homepage-metadata.md) for parent repositories, cached values, source provenance and offline CI.

每周维护先更新关注度快照，再生成首页；失败保留原数值及日期。论文／博客入口只来自已核实材料，近期收录日期不等于发布日期。
