#!/usr/bin/env python3
"""Opt-in, bounded HTTP spot checks; never a recursive catalog audit.

Preview: python scripts/check_external_links.py
Check:   python scripts/check_external_links.py docs/catalog.md --check --strict

Only --check makes requests. Fragments are removed: HTTP cannot validate anchors.
No dependencies, recursive traversal, response-body reads, or repairs are used.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from html import unescape
from http.client import HTTPException
from pathlib import Path
import re
import socket
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = [ROOT / 'README.md', ROOT / 'README_CN.md',
                 ROOT / 'docs' / 'representative-comparison.md']


def extract_urls(text: str) -> list[str]:
    """Find HTTP(S) URLs in Markdown links, references, HTML and plain text."""
    urls = []
    for raw in re.findall(r'https?://[^\s<>"\'`]+', text, flags=re.I):
        raw = unescape(raw).rstrip('.,;')
        # Emphasis can surround the entire Markdown link: **[name](url)**.
        for marker in ('**', '__', '~~', '*', '_'):
            if raw.endswith(')' + marker):
                raw = raw[:-len(marker)]
                break
        # Remove Markdown delimiters, preserving balanced parentheses in URLs.
        while raw and raw[-1] in ')]}':
            opening = {')': '(', ']': '[', '}': '{'}[raw[-1]]
            if raw.count(raw[-1]) <= raw.count(opening):
                break
            raw = raw[:-1]
        try:
            parts = urlsplit(raw)
            if parts.hostname and not parts.username and not parts.password:
                urls.append(urlunsplit(parts._replace(fragment='')))
        except ValueError:
            continue
    return urls


def select_urls(paths: list[Path], limit: int) -> tuple[list[str], int]:
    """Deduplicate before applying the cap, retaining document order."""
    unique = dict.fromkeys(url for path in paths
                           for url in extract_urls(path.read_text(encoding='utf-8')))
    return list(unique)[:limit], len(unique)


@dataclass(frozen=True)
class Result:
    category: str
    detail: str


def classify(status: int) -> str:
    if 200 <= status < 300:
        return 'reachable'
    if status in (404, 410):
        return 'missing'
    if status in (401, 403):
        return 'access-restricted'
    if status == 429:
        return 'rate-limited'
    if status >= 500:
        return 'server-error'
    return 'inconclusive'


def check_url(url: str, timeout: float) -> Result:
    """HEAD first; confirm missing responses or unsupported HEAD with one GET."""
    for method in ('HEAD', 'GET'):
        headers = {'User-Agent': 'InferenceCatalogLinkCheck/1.0'}
        if method == 'GET':
            headers['Range'] = 'bytes=0-0'
        try:
            try:
                with urlopen(Request(url, headers=headers, method=method), timeout=timeout) as response:
                    status = response.status
                    # Do not read the body, even if the server ignores Range.
            except HTTPError as error:
                status = error.code
                error.close()
            if method == 'HEAD' and status in (404, 405, 410, 501):
                continue
            return Result(classify(status), f'{method} HTTP {status}')
        except (TimeoutError, socket.timeout):
            return Result('timeout', f'{method} timed out')
        except URLError as error:
            if isinstance(error.reason, (TimeoutError, socket.timeout)):
                return Result('timeout', f'{method} timed out')
            return Result('network-error', f'{method}: {error.reason}')
        except HTTPException as error:
            return Result('network-error', f'{method}: {error}')
        except (OSError, ValueError) as error:
            return Result('inconclusive', f'{method}: {error}')
    raise AssertionError('GET must produce a result')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('paths', nargs='*', type=Path,
                        help='Markdown files (default: README pair and docs/representative-comparison.md)')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Opt in to HTTP requests')
    mode.add_argument('--dry-run', action='store_true', help='List targets without requests (the default)')
    parser.add_argument('--strict', action='store_true', help='With --check, exit 1 only on GET HTTP 404/410')
    parser.add_argument('--max-links', type=int, default=25, help='Maximum unique URLs to check, 1–100 (default: 25)')
    parser.add_argument('--timeout', type=float, default=5, help='Socket timeout in seconds, >0 to 30 (default: 5)')
    args = parser.parse_args(argv)
    if not 1 <= args.max_links <= 100:
        parser.error('--max-links must be between 1 and 100')
    if not 0 < args.timeout <= 30:
        parser.error('--timeout must be greater than 0 and at most 30 seconds')
    if args.strict and not args.check:
        parser.error('--strict requires --check')
    paths = args.paths or DEFAULT_PATHS
    if any(path.suffix.lower() not in ('.md', '.markdown') for path in paths):
        parser.error('Only explicit Markdown files are supported; directories are not traversed')
    try:
        urls, total = select_urls(paths, args.max_links)
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    print(f'Selected {len(urls)} of {total} unique HTTP(S) URLs; fragments are not checked.')
    if total > len(urls):
        print(f'{total - len(urls)} URLs omitted by the cap. Select narrower Markdown files to focus a check.')
    if not args.check:
        print('Dry run: no network requests. Use --check to opt in.')
        for url in urls:
            print(url)
        return 0
    counts: Counter[str] = Counter()
    for url in urls:
        result = check_url(url, args.timeout)
        counts[result.category] += 1
        print(f'{result.category}: {url} ({result.detail})', flush=True)
    print('Summary: ' + (', '.join(f'{key}={value}' for key, value in sorted(counts.items())) or 'no URLs selected'))
    print('Only GET HTTP 404/410 is reported as missing. Restricted, rate-limited, timeout and other errors need review.')
    return int(args.strict and counts['missing'] > 0)


if __name__ == '__main__':
    raise SystemExit(main())
