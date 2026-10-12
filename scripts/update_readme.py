#!/usr/bin/env python3
"""Render the project catalog section of README.md from catalog/projects.csv."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'catalog' / 'projects.csv'
README_PATH = ROOT / 'README.md'
START = '<!-- CATALOG-START -->'
END = '<!-- CATALOG-END -->'
CATEGORIES = [
    ('LLM runtime', 'LLM execution runtimes'),
    ('Image / diffusion runtime', 'Image and diffusion execution'),
    ('Video / DiT runtime', 'Video and diffusion-transformer execution'),
    ('Engine generation / agents', 'Agent-driven generation and optimization'),
    ('Adjacent infrastructure', 'Adjacent infrastructure and watchlist'),
]
SOURCES = {
    'public-code': 'public code',
    'closed-core': 'closed core',
    'documentation-only': 'documentation',
    'review-only': 'review-only code',
}
AI = {
    'intrinsic': 'agent-native',
    'disclosed': 'AI disclosed',
    'not-established': 'AI use unverified',
}


def md_cell(value: str) -> str:
    return str(value).replace('|', '&#124;').replace('\n', ' ').strip()


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(encoding='utf-8', newline='') as fp:
        return list(csv.DictReader(fp))


def render_catalog(rows: list[dict[str, str]]) -> str:
    groups: list[str] = []
    for category, heading in CATEGORIES:
        these = sorted((r for r in rows if r['category'] == category), key=lambda r: r['project'].lower())
        if not these:
            continue
        table = [
            f'### {heading}',
            '',
            '| Project | Target | Execution-level specialization | Source / AI | Limitations |',
            '| --- | --- | --- | --- | --- |',
        ]
        for r in these:
            proj = f"[{md_cell(r['project'])}]({r['url']})"
            evidence = f"[{SOURCES[r['source_visibility']]}]({r['evidence_url']}) · {AI[r['ai_involvement']]}"
            tag = '' if r['tier'] == 'Core' else f" **({r['tier']})**"
            table.append('| ' + ' | '.join([
                proj+tag,
                md_cell(r['target']),
                md_cell(r['mechanism']),
                evidence,
                md_cell(r['caveat']),
            ]) + ' |')
        groups.append('\n'.join(table))
    return '\n\n'.join(groups)


def updated_text(before: str, rows: list[dict[str, str]]) -> str:
    if before.count(START) != 1 or before.count(END) != 1:
        raise ValueError('Expected exactly one start and one end catalog marker')
    prefix, after_start = before.split(START, 1)
    _, suffix = after_start.split(END, 1)
    return prefix + START + '\n\n' + render_catalog(rows) + '\n\n' + END + suffix


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--check', action='store_true', help='Fail if README generated catalog is out of date')
    args = p.parse_args()
    rows = load_rows()
    before = README_PATH.read_text(encoding='utf-8')
    after = updated_text(before, rows)
    if args.check:
        if after != before:
            print('README.md catalog is out of date; run python scripts/update_readme.py', file=sys.stderr)
            return 1
        print(f'README catalog in sync ({len(rows)} entries)')
    else:
        README_PATH.write_text(after, encoding='utf-8')
        print(f'Updated README catalog ({len(rows)} entries)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
