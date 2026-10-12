"""Regression checks for data integrity, generated navigation and local links."""
import copy
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import update_readme as render
from validate_catalog import validate


def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    seen = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, flags=re.M):
        title = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', title)
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        suffix = seen.get(slug, 0)
        seen[slug] = suffix + 1
        result.add(slug + (f'-{suffix}' if suffix else ''))
    return result


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = render.load_rows()

    def test_catalog_valid(self):
        self.assertEqual(validate(self.rows), [])

    def test_duplicates_rejected(self):
        errors = validate(self.rows + [self.rows[0]])
        self.assertTrue(any('duplicate id' in e for e in errors))
        self.assertTrue(any('duplicate project URL' in e for e in errors))

    def test_bad_facet_and_missing_evidence_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['domains'] = 'not-a-modality'
        rows[0]['evidence_urls'] = rows[0]['url']
        errors = validate(rows)
        self.assertTrue(any('unknown domains' in e for e in errors))
        self.assertTrue(any('evidence pointers' in e for e in errors))

    def test_markers_must_be_ordered_and_unique(self):
        for text in ['', render.START + render.START + render.END, render.END + render.START]:
            with self.assertRaises(ValueError):
                render.updated_text(text, 'generated')
        self.assertEqual(render.updated_text('prefix' + render.START + 'old' + render.END + 'suffix', 'new'),
                         'prefix' + render.START + '\n\nnew\n\n' + render.END + 'suffix')

    def test_markdown_cells_do_not_inject_table_or_html(self):
        self.assertEqual(render.md_cell('<script>|two\nlines'), '&lt;script&gt;&#124;two lines')

    def test_generated_views_are_current(self):
        for path, content in render.generated_files(self.rows).items():
            with self.subTest(path=path.name):
                self.assertEqual(path.read_text(encoding='utf-8'), content)

    def test_every_project_has_unique_navigation_target(self):
        full = render.render_catalog(self.rows)
        ids = re.findall(r'<a id="([^"]+)"></a>', full)
        self.assertEqual(len(ids), len(set(ids)))
        for row in self.rows:
            self.assertIn(row['id'], ids)

    def test_local_links_and_anchors(self):
        paths = [*ROOT.glob('*.md'), *ROOT.glob('docs/*.md')]
        for path in paths:
            content = path.read_text(encoding='utf-8')
            for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', content):
                u = urlsplit(target)
                if u.scheme or u.netloc:
                    continue
                dest = (path.parent / unquote(u.path)).resolve() if u.path else path
                with self.subTest(source=path.name, link=target):
                    self.assertTrue(dest.exists(), f'Missing {dest}')
                    if u.fragment and dest.suffix == '.md' and dest.exists():
                        self.assertIn(unquote(u.fragment), anchors(dest.read_text(encoding='utf-8')))

    def test_svg_assets_are_self_contained_and_accessible(self):
        for path in (ROOT / 'assets').glob('*.svg'):
            tree = ET.parse(path)
            tags = {element.tag.rsplit('}', 1)[-1] for element in tree.iter()}
            with self.subTest(path=path.name):
                self.assertIn('title', tags)
                self.assertIn('desc', tags)
                self.assertNotIn('script', tags)
                self.assertNotIn('image', tags)
                self.assertNotIn('foreignObject', tags)


if __name__ == '__main__':
    unittest.main()
