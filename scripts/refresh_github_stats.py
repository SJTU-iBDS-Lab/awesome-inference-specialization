#!/usr/bin/env python3
"""Refresh only repository popularity snapshots; never change technical review dates.

Default: dry run. Network I/O occurs only with --refresh; CI rendering is offline.
Uses GitHub's repository metadata API, conditional requests and bounded serial I/O.
"""
from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import json
import os
from pathlib import Path
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from homepage_metadata import ROOT, REPOSITORY, repository_from_url, validate_stats


class GitHubRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        u = urlsplit(newurl)
        if u.scheme != 'https' or u.netloc.lower() != 'api.github.com':
            raise ValueError('Refused redirect outside the GitHub API')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def observe(old: dict | None, payload: dict, today: str, etag: str | None = None) -> dict:
    if not isinstance(payload, dict):
        raise ValueError('Expected a repository metadata object')
    stars, repo_id, full_name = payload.get('stargazers_count'), payload.get('id'), payload.get('full_name')
    if type(stars) is not int or stars < 0 or type(repo_id) is not int or repo_id < 1:
        raise ValueError('Malformed repository star response')
    if not isinstance(full_name, str) or not REPOSITORY.fullmatch(full_name) or payload.get('private') is not False:
        raise ValueError('Expected public GitHub repository metadata')
    if old and old.get('repository_id') is not None and old['repository_id'] != repo_id:
        raise ValueError('Repository identity changed; review the upstream URL')
    result = {'repository_id': repo_id, 'full_name': full_name, 'stars': stars,
              'fetched_on': today, 'last_attempt_on': today, 'status': 'ok'}
    if etag:
        result['etag'] = etag
    return result


def failed(old: dict | None, today: str, error: str) -> dict:
    result = copy.deepcopy(old) if old else {'stars': None, 'fetched_on': None}
    result.update(last_attempt_on=today, status='unavailable', error=error)
    return result


def unchanged(old: dict | None, today: str) -> dict:
    if not old or type(old.get('stars')) is not int:
        raise ValueError('304 received without a valid previous snapshot')
    result = dict(old)
    result.update(fetched_on=today, last_attempt_on=today, status='ok')
    result.pop('error', None)
    return result


def due(old: dict | None, today: dt.date, age: int) -> bool:
    return (not old or old.get('status') != 'ok' or
            (today - dt.date.fromisoformat(old['fetched_on'])).days >= age)


def refresh(cache: dict, repos: list[str], today: dt.date, token: str,
            limit: int = 160, age: int = 7, fetch=None, pause=time.sleep) -> tuple[dict, dict]:
    result = copy.deepcopy(cache)
    report = {'requested': 0, 'updated': 0, 'unavailable': [], 'stopped': False}
    opener = build_opener(GitHubRedirects())
    fetch = fetch or opener.open
    day = today.isoformat()
    for repo in sorted(set(repos)):
        if not REPOSITORY.fullmatch(repo):
            raise ValueError('Invalid repository identifier')
        old = result['repositories'].get(repo)
        if not due(old, today, age):
            continue
        if report['requested'] >= limit:
            report['stopped'] = True
            break
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'awesome-inference-specialization-metadata',
                   'X-GitHub-Api-Version': '2026-03-10'}
        if token:
            headers['Authorization'] = 'Bearer ' + token
        if old and old.get('etag'):
            headers['If-None-Match'] = old['etag']
        req = Request(f'https://api.github.com/repos/{repo}', headers=headers)
        report['requested'] += 1
        try:
            with fetch(req, timeout=15) as response:
                payload = json.loads(response.read(2_000_000))
                result['repositories'][repo] = observe(old, payload, day, response.headers.get('ETag'))
                report['updated'] += 1
        except HTTPError as error:
            if error.code == 304:
                result['repositories'][repo] = unchanged(old, day)
                report['updated'] += 1
            else:
                result['repositories'][repo] = failed(old, day, f'HTTP {error.code}')
                report['unavailable'].append(repo)
                if error.code in {401, 403, 429}:
                    report['stopped'] = True
                    break
        except (URLError, TimeoutError, OSError, ValueError, KeyError) as error:
            result['repositories'][repo] = failed(old, day, type(error).__name__)
            report['unavailable'].append(repo)
        pause(0.1)
    validate_stats(result)
    return result, report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Explicitly allow bounded GitHub API reads')
    parser.add_argument('--max-repositories', type=int, default=160)
    parser.add_argument('--min-age-days', type=int, default=7)
    parser.add_argument('--strict', action='store_true', help='Return nonzero on incomplete refresh; preserve old values regardless')
    args = parser.parse_args(argv)
    if not 1 <= args.max_repositories <= 500 or args.min_age_days < 0:
        parser.error('Use 1–500 repositories and a nonnegative age')
    path = ROOT / 'catalog/github_stats.json'
    cache = json.loads(path.read_text(encoding='utf-8'))
    validate_stats(cache)
    with (ROOT / 'catalog/projects.csv').open(encoding='utf-8', newline='') as stream:
        repos = sorted({p[0] for row in csv.DictReader(stream) if (p := repository_from_url(row['url']))})
    today = dt.datetime.now(dt.timezone.utc).date()
    pending = sum(due(cache['repositories'].get(repo), today, args.min_age_days) for repo in repos)
    print(f'{len(repos)} unique GitHub repositories; {pending} snapshots due. Technical checked_on dates are untouched.')
    if not args.refresh:
        print('Dry run: pass --refresh to read GitHub. No network calls or writes performed.')
        return 0
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN') or ''
    if not token and pending > 50:
        print('Warning: unauthenticated rate limits may prevent a full refresh.', file=sys.stderr)
    updated, report = refresh(cache, repos, today, token, args.max_repositories, args.min_age_days)
    text = json.dumps(updated, ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    if text != path.read_text(encoding='utf-8'):
        temp = path.with_suffix('.json.tmp')
        temp.write_text(text, encoding='utf-8')
        temp.replace(path)
    print(json.dumps(report, ensure_ascii=False))
    current = sum(updated['repositories'].get(repo, {}).get('status') == 'ok' for repo in repos)
    print(f'{current}/{len(repos)} repository snapshots currently have successful status; failed fetches are never zeroed.')
    return 1 if args.strict and (report['unavailable'] or report['stopped']) else 0


if __name__ == '__main__':
    raise SystemExit(main())
