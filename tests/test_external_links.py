"""Offline regression tests: no HTTP request may leave this test suite."""
from contextlib import redirect_stderr, redirect_stdout
import io
from http.client import BadStatusLine
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_external_links as links


def response(status):
    result = MagicMock()
    result.__enter__.return_value.status = status
    return result


def http_error(status):
    return HTTPError('https://example.test/a', status, 'test response', {}, None)


class ExternalLinkTests(unittest.TestCase):
    def test_extract_markdown_and_drop_fragments(self):
        text = '''[a](https://example.test/a#one)
        [b](https://example.test/topic_(one) "title")
        [reference]: https://example.test/ref
        <https://example.test/auto> <a href="https://example.test/?a=1&amp;b=2">
        [local](docs/catalog.md) [email](mailto:someone@example.test)
        https://user:password@example.test/private'''
        self.assertEqual(links.extract_urls(text), [
            'https://example.test/a', 'https://example.test/topic_(one)',
            'https://example.test/ref', 'https://example.test/auto',
            'https://example.test/?a=1&b=2'])

    def test_deduplicate_across_files_before_cap(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / 'a.md', Path(directory) / 'b.md'
            a.write_text('[a](https://example.test/a#one) [a](https://example.test/a#two)', encoding='utf-8')
            b.write_text('[a](https://example.test/a) [b](https://example.test/b) [c](https://example.test/c)', encoding='utf-8')
            self.assertEqual(links.select_urls([a, b], 2),
                             (['https://example.test/a', 'https://example.test/b'], 3))

    @patch.object(links, 'urlopen')
    def test_head_success_does_not_read_body_or_retry(self, opened):
        opened.return_value = response(200)
        self.assertEqual(links.check_url('https://example.test/a', 3).category, 'reachable')
        self.assertEqual(opened.call_count, 1)
        self.assertEqual(opened.call_args.args[0].method, 'HEAD')
        self.assertEqual(opened.call_args.kwargs['timeout'], 3)
        opened.return_value.__enter__.return_value.read.assert_not_called()

    @patch.object(links, 'urlopen')
    def test_head_fallback_is_bounded_and_missing_requires_get(self, opened):
        for head_status in (404, 405, 410, 501):
            for get_status, category in ((200, 'reachable'), (404, 'missing'), (410, 'missing'), (403, 'access-restricted')):
                with self.subTest(head=head_status, get=get_status):
                    opened.reset_mock()
                    opened.side_effect = [http_error(head_status),
                                          response(get_status) if get_status == 200 else http_error(get_status)]
                    result = links.check_url('https://example.test/a', 2)
                    self.assertEqual(result.category, category)
                    self.assertEqual(opened.call_count, 2)
                    request = opened.call_args.args[0]
                    self.assertEqual(request.method, 'GET')
                    self.assertEqual(request.get_header('Range'), 'bytes=0-0')

    @patch.object(links, 'urlopen')
    def test_failed_get_confirmation_does_not_preserve_head_missing(self, opened):
        opened.side_effect = [http_error(404), socket.timeout()]
        self.assertEqual(links.check_url('https://example.test/a', 1).category, 'timeout')
        self.assertEqual(opened.call_count, 2)

    @patch.object(links, 'urlopen')
    def test_access_and_transient_errors_are_not_missing(self, opened):
        for status, category in ((401, 'access-restricted'), (403, 'access-restricted'),
                                 (429, 'rate-limited'), (503, 'server-error'), (302, 'inconclusive')):
            with self.subTest(status=status):
                opened.reset_mock()
                opened.side_effect = http_error(status)
                self.assertEqual(links.check_url('https://example.test/a', 1).category, category)
                self.assertEqual(opened.call_count, 1)

    @patch.object(links, 'urlopen')
    def test_timeout_and_network_failures_are_not_missing(self, opened):
        for error, category in ((socket.timeout(), 'timeout'), (URLError(socket.timeout()), 'timeout'),
                                (URLError('DNS failure'), 'network-error'), (BadStatusLine('bad'), 'network-error')):
            with self.subTest(error=error):
                opened.side_effect = error
                self.assertEqual(links.check_url('https://example.test/a', 1).category, category)

    @patch.object(links, 'urlopen', side_effect=AssertionError('Network forbidden in dry run'))
    def test_default_and_explicit_dry_runs_are_offline(self, opened):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'README.md'
            path.write_text('[sample](https://example.test/a)', encoding='utf-8')
            with patch.object(links, 'DEFAULT_PATHS', [path]), redirect_stdout(io.StringIO()):
                self.assertEqual(links.main([]), 0)
                self.assertEqual(links.main(['--dry-run']), 0)
        opened.assert_not_called()

    @patch.object(links, 'check_url', return_value=links.Result('reachable', 'mocked'))
    def test_check_obeys_default_cap(self, checked):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.md'
            path.write_text('\n'.join(f'[link](https://example.test/{n})' for n in range(40)), encoding='utf-8')
            with redirect_stdout(io.StringIO()):
                self.assertEqual(links.main([str(path), '--check']), 0)
            self.assertEqual(checked.call_count, 25)

    @patch.object(links, 'select_urls', return_value=(['https://example.test/a'], 1))
    @patch.object(links, 'check_url')
    def test_strict_exit_code_only_for_missing(self, checked, selected):
        for category in ('reachable', 'missing', 'access-restricted', 'rate-limited', 'timeout', 'network-error'):
            checked.return_value = links.Result(category, 'test')
            with redirect_stdout(io.StringIO()):
                self.assertEqual(links.main(['--check', '--strict']), int(category == 'missing'))
                self.assertEqual(links.main(['--check']), 0)

    def test_invalid_limits_and_modes_fail_before_requests(self):
        for args in (['--max-links', '0'], ['--max-links', '101'], ['--timeout', '0'],
                     ['--timeout', 'nan'], ['--timeout', '31'], ['--strict'],
                     ['--check', '--dry-run'], ['catalog/projects.csv']):
            with self.subTest(args=args), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                links.main(args)
            self.assertEqual(error.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
