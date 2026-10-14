"""Offline tests for provenance, repository scope and failure-safe popularity data."""
import copy
import csv
import datetime as dt
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import homepage_metadata as metadata
import refresh_github_stats as refresh
import update_readme as render

TODAY = dt.date(2026, 10, 14)


def snapshot(stars=1200):
    return dict(repository_id=42, full_name='Owner/Engine', stars=stars,
                fetched_on='2026-10-01', last_attempt_on='2026-10-01', status='ok')


class Response:
    headers = {'ETag': '"snapshot"'}
    def __init__(self, payload):
        self.payload = payload
    def read(self, size):
        return json.dumps(self.payload).encode()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False


class MetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = render.load_rows()
        cls.config, cls.cache = metadata.load_bundle(cls.rows)

    def test_every_shortcut_has_previously_reviewed_provenance(self):
        metadata.validate_config(self.config, self.rows, render.load_cases(), (ROOT / 'docs/reading-list.md').read_text())
        bad = copy.deepcopy(self.config)
        bad['links']['seis'][0]['url'] = 'https://example.org/unreviewed-paper'
        with self.assertRaises(ValueError):
            metadata.validate_config(bad, self.rows, render.load_cases(), '')

    def test_repo_scope_and_non_github_entries(self):
        self.assertEqual(metadata.repository_from_url('https://github.com/Owner/Repo'), ('owner/repo', False))
        self.assertEqual(metadata.repository_from_url('https://github.com/Owner/Repo/tree/main/model'), ('owner/repo', True))
        self.assertEqual(metadata.repository_from_url('https://github.com/Owner/Repo#component'), ('owner/repo', True))
        for url in ('https://blog.example.org/foo', 'https://github.com.evil.example/a/b', 'https://evil@github.com/a/b', 'http://github.com/a/b'):
            self.assertIsNone(metadata.repository_from_url(url))

    def test_number_format_and_zero_is_not_missing(self):
        for value, text in [(0,'0'),(999,'999'),(1000,'1k'),(1250,'1.2k'),(12345,'12.3k'),(1000000,'1m')]:
            self.assertEqual(metadata.format_stars(value), text)
        for bad in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                metadata.format_stars(bad)

    def test_parent_totals_are_explicit_in_both_languages(self):
        row={'id':'component','url':'https://github.com/owner/engine/tree/main/component'}
        cache={'schema_version':1,'repositories':{'owner/engine':snapshot()}}
        config={'parent_repository_ids':[],'links':{}}
        self.assertIn('parent repo',metadata.entry_extras(row,config,cache))
        self.assertIn('母仓库',metadata.entry_extras(row,config,cache,True))
        row['url']='https://github.com/owner/engine'
        config['parent_repository_ids']=['component']
        self.assertIn('parent repo',metadata.entry_extras(row,config,cache))

    def test_no_star_placeholder_for_missing_or_blog_entries(self):
        config={'parent_repository_ids':[],'links':{}}
        cache={'schema_version':1,'repositories':{}}
        self.assertEqual(metadata.entry_extras({'id':'x','url':'https://github.com/o/r'},config,cache),'')
        self.assertEqual(metadata.entry_extras({'id':'x','url':'https://blog.example.org/x'},config,cache),'')

    def test_recent_dates_are_not_taken_from_source_review(self):
        text=metadata.recent_line(self.config)
        self.assertIn('Catalog addition dates, not project release dates',text)
        self.assertLessEqual(text.count('](#project-'),5)
        for item in self.config['recent'][:5]:
            self.assertIn(item['added_on'],text)
            self.assertIn(f'#project-{item["id"]}',text)

    def test_regeneration_is_offline_and_preserves_descriptions(self):
        with patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('Network access in renderer')):
            for chinese in (False,True):
                text=render.render_overview(self.rows,chinese)
                notes=render.load_homepage_cn() if chinese else render.load_homepage_en()
                for row in self.rows:
                    self.assertIn(render.md_cell(notes[row['id']]),text)
                self.assertIn('docs/homepage-metadata.md',text)
                self.assertIn('https://arxiv.org/html/2610.04646v1',text)

    def test_snapshot_values_have_dates_and_repository_ids(self):
        metadata.validate_stats(self.cache)
        bad={'schema_version':1,'repositories':{'owner/engine':snapshot(True)}}
        with self.assertRaises(ValueError):
            metadata.validate_stats(bad)


class RefreshTests(unittest.TestCase):
    def test_failures_preserve_previous_count_and_observation_date(self):
        old=snapshot(4321)
        result=refresh.failed(old,TODAY.isoformat(),'HTTP 404')
        self.assertEqual(result['stars'],4321)
        self.assertEqual(result['fetched_on'],'2026-10-01')
        self.assertEqual(result['last_attempt_on'],'2026-10-14')
        self.assertEqual(old['status'],'ok')
        self.assertIsNone(refresh.failed(None,TODAY.isoformat(),'HTTP 404')['stars'])

    def test_not_modified_revalidates_without_fabricating_a_count(self):
        result=refresh.unchanged(snapshot(0),TODAY.isoformat())
        self.assertEqual(result['stars'],0)
        self.assertEqual(result['fetched_on'],'2026-10-14')
        with self.assertRaises(ValueError):
            refresh.unchanged(None,TODAY.isoformat())

    def test_numeric_and_identity_validation(self):
        payload={'id':42,'full_name':'NewOwner/Engine','stargazers_count':9,'private':False}
        self.assertEqual(refresh.observe(snapshot(),payload,'2026-10-14')['full_name'],'NewOwner/Engine')
        for changes in ({'id':43},{'stargazers_count':True},{'stargazers_count':-1},{'private':True},{'full_name':'../a/b'}):
            with self.assertRaises(ValueError):
                refresh.observe(snapshot(),dict(payload,**changes),'2026-10-14')

    def test_serial_refresh_deduplicates_and_limits_work(self):
        def fetch(req,timeout):
            return Response({'id':42,'full_name':'Owner/Engine','stargazers_count':123,'private':False})
        cache,report=refresh.refresh({'schema_version':1,'repositories':{}},['owner/engine']*3,TODAY,'',fetch=fetch,pause=lambda _:None)
        self.assertEqual(report['requested'],1)
        self.assertEqual(cache['repositories']['owner/engine']['stars'],123)
        _,report=refresh.refresh({'schema_version':1,'repositories':{}},['a/a','a/b'],TODAY,'',limit=1,fetch=fetch,pause=lambda _:None)
        self.assertTrue(report['stopped'])
        self.assertEqual(report['requested'],1)

    def test_rate_limit_stops_and_never_zeroes(self):
        def fetch(req,timeout):
            raise HTTPError(req.full_url,429,'rate limit',{},None)
        original={'schema_version':1,'repositories':{'owner/a':snapshot(77),'owner/b':snapshot(88)}}
        updated,report=refresh.refresh(original,['owner/a','owner/b'],TODAY,'',fetch=fetch,pause=lambda _:None)
        self.assertEqual(report['requested'],1)
        self.assertTrue(report['stopped'])
        self.assertEqual(updated['repositories']['owner/a']['stars'],77)
        self.assertEqual(updated['repositories']['owner/b'],original['repositories']['owner/b'])

    def test_timeout_preserves_prior_snapshot(self):
        def fetch(req,timeout):
            raise URLError('temporary timeout')
        original={'schema_version':1,'repositories':{'owner/engine':snapshot(99)}}
        updated,report=refresh.refresh(original,['owner/engine'],TODAY,'',fetch=fetch,pause=lambda _:None)
        self.assertEqual(updated['repositories']['owner/engine']['stars'],99)
        self.assertEqual(updated['repositories']['owner/engine']['fetched_on'],'2026-10-01')

    def test_fresh_snapshots_are_not_requested(self):
        old=refresh.unchanged(snapshot(),'2026-10-13')
        def fetch(*args,**kwargs):
            self.fail('Fetched a fresh snapshot')
        _,report=refresh.refresh({'schema_version':1,'repositories':{'owner/engine':old}},['owner/engine'],TODAY,'',fetch=fetch)
        self.assertEqual(report['requested'],0)

    def test_auth_is_never_forwarded_to_other_hosts(self):
        from urllib.request import Request
        handler=refresh.GitHubRedirects()
        with self.assertRaises(ValueError):
            handler.redirect_request(Request('https://api.github.com/repos/a/b',headers={'Authorization':'Bearer placeholder'}),None,302,'',{},'https://other.example/collect')

    def test_default_cli_is_dry_run(self):
        path=ROOT/'catalog/github_stats.json'
        before=path.read_bytes()
        with patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('No network allowed')):
            self.assertEqual(refresh.main([]),0)
        self.assertEqual(path.read_bytes(),before)


if __name__=='__main__':
    unittest.main()
