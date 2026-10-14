"""Apply the locally tested metadata layer to the pinned catalog; never publish main."""
from pathlib import Path
import json
import shutil
import subprocess
import sys

BASE = '6ce2f0bf2f358a85939bac57c40c9a82f761997e'
ROOT = Path.cwd()
HELPER = Path(__file__).resolve().parents[1]
NEW = ['catalog/homepage_metadata.json', 'catalog/github_stats.json', 'scripts/homepage_metadata.py',
       'scripts/refresh_github_stats.py', 'tests/test_homepage_metadata.py', 'docs/homepage-metadata.md']
EDITED = ['scripts/homepage_layout.py', 'docs/homepage-maintenance.md', 'docs/homepage-visual-design.md', 'docs/updates.md']
ALLOWED = set(NEW + EDITED + ['README.md', 'README_CN.md'])

def replace_once(text, old, new):
    assert text.count(old) == 1, f'Unexpected base context: {old[:100]}'
    return text.replace(old, new)

if '--verify' in sys.argv:
    changed = set(subprocess.check_output(['git', 'diff', '--name-only', BASE], text=True).splitlines())
    untracked = set(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())
    assert changed <= ALLOWED and untracked == set(NEW), (changed, untracked)
    # All existing tracked data, descriptions, cases, diagrams and tests outside the allowlist are byte-identical.
    for path in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE], text=True).splitlines():
        if path not in ALLOWED:
            original = subprocess.check_output(['git', 'show', f'{BASE}:{path}'])
            assert (ROOT / path).read_bytes() == original, path
    cache = json.loads((ROOT / 'catalog/github_stats.json').read_text())
    valid = sum(type(item.get('stars')) is int for item in cache['repositories'].values())
    assert valid > 0, 'No observed star counts; do not publish an empty feature'
    config = json.loads((ROOT / 'catalog/homepage_metadata.json').read_text())
    print(f'Observed snapshots: {valid}; direct source links: {sum(map(len, config["links"].values()))}')
    print('Preserved all original project records, review dates, cases, descriptions, assets, tests and workflows.')
    raise SystemExit(0)

assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == BASE
assert not subprocess.check_output(['git', 'status', '--porcelain'], text=True).strip()
for path in NEW:
    assert not (ROOT / path).exists(), path
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HELPER / path, ROOT / path)

p = ROOT / 'scripts/homepage_layout.py'
s = p.read_text()
s = replace_once(s, 'import html\n', 'import html\n\nfrom homepage_metadata import load_bundle, entry_extras, recent_line, snapshot_note\n')
s = replace_once(s, '    notes = notes_cn if chinese else notes_en\n', '    notes = notes_cn if chinese else notes_en\n    metadata_config, star_cache = load_bundle(rows)\n')
s = replace_once(s, '**[{cell(row["project"])}]({row["url"]})** — ', '**[{cell(row["project"])}]({row["url"]})**{entry_extras(row, metadata_config, star_cache, chinese)} — ')
s = replace_once(s, "domain_navigation + '</sub>', '', '</div>', '',\n        '<a id=\"featured-reading\"></a>'", "domain_navigation + '</sub>', '', '</div>', '',\n        recent_line(metadata_config, chinese), '',\n        '<a id=\"featured-reading\"></a>'")
s = replace_once(s, "'全部项目展开，名称直达上游。[执行边界](docs/systems.md#system) · [跨领域索引](docs/domains.md)') + '</sub>', '']", "'全部项目展开，名称直达上游。[执行边界](docs/systems.md#system) · [跨领域索引](docs/domains.md)') + ' · ' + snapshot_note(rows, star_cache, chinese) + '</sub>', '']")
p.write_text(s)

p = ROOT / 'docs/homepage-maintenance.md'
s = p.read_text()
s += '''
## Weekly popularity snapshots and source shortcuts

Run `python scripts/refresh_github_stats.py --refresh` during the existing weekly maintenance task, before regenerating the README. Review partial-fetch results; never replace failed counts with zero or modify technical `checked_on` dates. Keep direct source links and actual catalog-addition dates in `catalog/homepage_metadata.json`. See [metadata rules](homepage-metadata.md) for parent repositories, cached values, source provenance and offline CI.

每周维护先更新关注度快照，再生成首页；失败保留原数值及日期。论文／博客入口只来自已核实材料，近期收录日期不等于发布日期。
'''
p.write_text(s)
p = ROOT / 'docs/homepage-visual-design.md'
s = p.read_text()
s += '''
## 2026-10-14 metadata refinement

Project names now carry compact repository-star text and selected Paper / Blog / Case report shortcuts. Subproject counts are explicitly parent-repository totals. A single recent-additions line uses admission dates rather than release dates. See [metadata rules](homepage-metadata.md). No remote badges or new visual framework are introduced; the six reading cards and original descriptions are unchanged.
'''
p.write_text(s)
p = ROOT / 'docs/updates.md'
s = p.read_text()
pos = s.index('\n## ')
s = s[:pos] + '''
## 2026-10-14 — Star snapshots and direct sources / 关注度快照与来源直达

- Added compact GitHub repository-star snapshots beside project names, with observation dates, explicit parent-repository labels and failure-safe cached values. Stars do not change order or inclusion.
- Promoted selected already-reviewed Paper / Blog / Case report links into the bilingual entries. Added a small recent-additions line whose dates mean catalog admission, not upstream release.
- Added an opt-in, bounded metadata refresher and offline regression tests. Kept all 126 project records, 68 cases, technical review dates, descriptions, source evidence, banners and starter cards unchanged.
- [Metadata and maintenance rules](homepage-metadata.md) explain cache age, missing numbers, parent repositories and the existing weekly maintenance path. This is a presentation/metadata change, not another source audit or engine benchmark.

新增紧凑 Star 快照、已核实来源入口与近期收录提示。母仓库不冒充子项目，缺失或获取失败不记为零；关注度更新时间与技术核查日期分离。布局、条目与原有测试保持不变，普通生成和 CI 不联网。
''' + s[pos:]
p.write_text(s)
print('Applied metadata presentation only; ready for live star collection and existing checks.')
