"""Regression checks for README visuals without browser or network dependencies."""
import csv
import json
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import homepage_layout as layout
import generate_banner


class ImageSources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []
        self.images = []

    def handle_starttag(self, tag, attributes):
        if tag == 'source':
            self.sources.append(dict(attributes))
        elif tag == 'img':
            self.images.append(dict(attributes))


class HomepageVisualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / 'catalog/projects.csv').open(encoding='utf-8', newline='') as fp:
            cls.rows = list(csv.DictReader(fp))
        cls.pages = [(False, ROOT / 'README.md'), (True, ROOT / 'README_CN.md')]

    def test_banners_are_current_and_accessible(self):
        assets = generate_banner.generated_assets()
        self.assertEqual(len(assets), 4)
        for path, content in assets.items():
            with self.subTest(path=path.name):
                self.assertEqual(path.read_text(encoding='utf-8'), content)
                svg = ET.fromstring(content)
                tags = {e.tag.rsplit('}', 1)[-1] for e in svg.iter()}
                self.assertTrue({'title', 'desc'} <= tags)
                self.assertFalse({'script', 'foreignObject', 'image', 'style'} & tags)
                self.assertEqual(svg.get('role'), 'img')
                for element in svg.iter():
                    self.assertFalse(any(k.lower().startswith('on') for k in element.attrib))
                    self.assertNotIn('href', element.attrib)

    def test_picture_fallbacks_and_media_order(self):
        for chinese, path in self.pages:
            parser = ImageSources()
            parser.feed(path.read_text(encoding='utf-8'))
            self.assertEqual([s['srcset'] for s in parser.sources], [
                'assets/header-dark-compact.svg', 'assets/header-light-compact.svg',
                'assets/header-dark.svg'])
            self.assertIn('max-width: 600px', parser.sources[0]['media'])
            self.assertIn('prefers-color-scheme: dark', parser.sources[0]['media'])
            self.assertEqual(parser.images[0]['src'], 'assets/header-light.svg')
            self.assertTrue(parser.images[0]['alt'])
            for entry in parser.sources + parser.images:
                self.assertTrue((ROOT / entry.get('srcset', entry.get('src'))).is_file())

    def test_cards_are_six_unique_linked_examples(self):
        for chinese, path in self.pages:
            text = path.read_text(encoding='utf-8')
            grid = text.split('<!-- STARTER-GRID-START -->', 1)[1].split('<!-- STARTER-GRID-END -->', 1)[0]
            self.assertEqual(grid.count('<tr>'), 2)
            self.assertEqual(grid.count('<td '), 6)
            self.assertEqual(grid.count('</td>'), 6)
            self.assertEqual(re.findall(r'\]\(docs/cases.md#([^)]+)\)', grid), list(layout.STARTER_CASE_IDS))
            self.assertNotRegex(grid, r'<(?:script|style|img)\b|\bstyle=|\bclass=')
            self.assertIn('title=', grid)

    def test_no_duplicate_toc_or_hidden_catalog(self):
        for chinese, path in self.pages:
            text = path.read_text(encoding='utf-8')
            self.assertNotRegex(text, re.compile(r'^## (?:Contents|目录)$', re.M))
            self.assertNotIn('<details>', text)
            self.assertLess(text.index('STARTER-GRID-START'), text.index('id="project-'))
            generated = text.split('<!-- CATALOG-START -->', 1)[1].split('<!-- CATALOG-END -->', 1)[0]
            for role in ('system', 'construction', 'validation', 'benchmark', 'support'):
                self.assertIn(f'(#homepage-{role})', generated)

    def test_complete_entries_and_descriptions_are_unchanged(self):
        for chinese, path in self.pages:
            text = path.read_text(encoding='utf-8')
            notes_path = ROOT / 'catalog' / ('homepage_cn.json' if chinese else 'homepage_en.json')
            notes = json.loads(notes_path.read_text(encoding='utf-8'))
            ids = re.findall(r'<a id="project-([^\"]+)"></a>', text)
            self.assertCountEqual(ids, [r['id'] for r in self.rows])
            self.assertEqual(len(ids), len(set(ids)))
            for row in self.rows:
                self.assertIn(layout.cell(notes[row['id']]), text)
                self.assertEqual(text.count(f']({row["url"]})'), 1)
                self.assertIn(f'(docs/catalog.md#{row["id"]})', text)

    def test_redundant_domain_tags_are_removed_but_other_facets_remain(self):
        for chinese, path in self.pages:
            text = path.read_text(encoding='utf-8')
            labels = {id: cn if chinese else en for id, en, cn in layout.SHORT_DOMAINS}
            for row in self.rows:
                if row['catalog_role'] != 'system':
                    continue
                line = next(line for line in text.splitlines() if f'id="project-{row["id"]}"' in line)
                metadata = line.split('<sub>', 1)[1].split('</sub>', 1)[0]
                tokens = metadata.split(' · ')
                primary = layout.primary_domain(row)
                self.assertNotIn(labels[primary], tokens)
                for domain in set(row['domains'].split(';')) - {primary}:
                    self.assertIn(labels[domain], tokens)

    def test_wide_and_compact_banners_match_in_dimensions_across_themes(self):
        for compact in (False, True):
            light = ET.fromstring(generate_banner.banner('light', compact))
            dark = ET.fromstring(generate_banner.banner('dark', compact))
            self.assertEqual(light.get('viewBox'), dark.get('viewBox'))
            self.assertEqual(light.get('height'), dark.get('height'))
            self.assertLessEqual(int(light.get('height')), 168)

    def test_critical_limits_are_still_visible(self):
        for chinese, path in self.pages:
            text = path.read_text(encoding='utf-8')
            for token in (('十个激活专家缩减为四个', '专家跳过', '闭源', '占位') if chinese else
                          ('from 10 to 4', 'expert skipping', 'closed core', 'placeholders')):
                self.assertIn(token, text)


if __name__ == '__main__':
    unittest.main()
