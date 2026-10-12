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
from validate_catalog import validate, validate_cases, validate_showcase, validate_homepage_cn


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
        self.assertEqual(validate_cases(render.load_cases(), self.rows), [])
        self.assertEqual(validate_showcase(render.load_showcase(), render.load_cases(), self.rows), [])

    def test_core_case_requires_linked_project_and_explicit_evidence(self):
        cases = copy.deepcopy(render.load_cases())
        cases[0]['project_ids'] = ['missing-project']
        cases[0]['cost'] = ''
        self.assertTrue(validate_cases(cases, self.rows))
        cases = copy.deepcopy(render.load_cases())
        cases[0]['evidence_urls'] = [cases[0]['evidence_urls'][0]]
        self.assertTrue(any('evidence pointers' in e for e in validate_cases(cases, self.rows)))

    def test_core_selection_cannot_silently_include_adjacent_work(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r['id'] == 'zero-inference')['survey_role'] = 'core'
        self.assertTrue(any('lacks a construction case' in e for e in validate_cases(render.load_cases(), rows)))

    def test_relevance_does_not_replace_artifact_role(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['survey_role'] = 'system'
        self.assertTrue(any('unsupported survey_role' in e for e in validate(rows)))

    def test_case_can_link_a_foundation_without_promoting_it(self):
        cases = copy.deepcopy(render.load_cases())
        cases[0]['project_ids'].append('vllm')
        self.assertEqual(validate_cases(cases, self.rows), [])

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

    def test_role_index_keeps_every_record_once(self):
        text = render.render_systems(self.rows)
        links = re.findall(r'\]\(catalog.md#([a-z0-9-]+)\)', text)
        self.assertCountEqual(links, [r['id'] for r in self.rows])
        self.assertEqual(len(links), len(set(links)))

    def test_homepage_separates_roles_and_links_complete_case_index(self):
        expected = {c['id'] for c in render.load_cases()}
        for chinese in (False, True):
            text = render.render_overview(self.rows, chinese)
            links = re.findall(r'\]\(docs/cases.md#([a-z0-9-]+)\)', text)
            self.assertTrue(set(links) <= expected)
            self.assertEqual(len(links), len(set(links)))
            for target in ('docs/cases.md', 'docs/systems.md#system', 'docs/systems.md#construction',
                           'docs/validation.md#numerical', 'docs/benchmarks.md', 'docs/resources.md#diagnostics',
                           'docs/resources.md#knowledge'):
                self.assertIn(f']({target})', text)
            self.assertEqual(text.count('<details>'), text.count('</details>'))
        case_index = render.render_cases(self.rows)
        self.assertTrue(expected <= anchors(case_index))

    def test_specialized_resource_indices_cover_primary_roles_without_duplicates(self):
        for renderer, role in [(render.render_benchmarks, 'benchmark'), (render.render_resources, 'support')]:
            text = renderer(self.rows)
            pattern = r'^\| \[[^\]]+\]\(catalog.md#([a-z0-9-]+)\)' if role == 'support' else r'\]\(catalog.md#([a-z0-9-]+)\)'
            links = re.findall(pattern, text, flags=re.M)
            members = {r['id'] for r in self.rows if r['catalog_role'] == role}
            for id in members:
                self.assertEqual(links.count(id), 1)
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r['id'] == 'fastkernels')['catalog_role'] = 'validation'
        self.assertTrue(any('Benchmark index must cover' in e for e in validate(rows)))

    def test_domain_index_retains_each_overlapping_membership(self):
        text = render.render_domains(self.rows)
        links = re.findall(r'\]\(catalog.md#([a-z0-9-]+)\)', text)
        expected = [r['id'] for r in self.rows for _ in r['domains'].split(';')]
        self.assertCountEqual(links, expected)
        for domain in render.SCHEMA['domains']:
            self.assertIn(domain, anchors(text))

    def test_support_example_cannot_silently_become_a_system(self):
        rows = copy.deepcopy(self.rows)
        example = render.SCHEMA['support_groups'][0]['examples'][0]
        next(r for r in rows if r['id'] == example)['catalog_role'] = 'system'
        self.assertTrue(any('Support list must point to a supporting entry' in e for e in validate(rows)))
        next(r for r in rows if r['id'] == example)['catalog_role'] = 'unknown'
        self.assertTrue(any('unsupported catalog_role' in e for e in validate(rows)))

    def test_showcase_requires_existing_cases_bilingual_text_and_linked_projects(self):
        for field, replacement, expected in [
            ('case_id', 'missing-case', 'missing case'),
            ('project_id', 'vllm', 'must belong'),
            ('scope_cn', '', 'nonempty bilingual'),
        ]:
            choices = copy.deepcopy(render.load_showcase())
            choices[0][field] = replacement
            self.assertTrue(any(expected in e for e in validate_showcase(choices, render.load_cases(), self.rows)))
        choices = render.load_showcase()
        self.assertTrue(any('Duplicate' in e for e in validate_showcase(choices + [choices[0]], render.load_cases(), self.rows)))
        self.assertTrue(validate_showcase([], render.load_cases(), self.rows))

    def test_homepages_share_exact_reasoned_selection(self):
        choices = render.load_showcase()
        expected = [entry['case_id'] for entry in choices]
        self.assertTrue(10 <= len(expected) <= 15)
        for chinese in (False, True):
            text = render.render_overview(self.rows, chinese)
            links = re.findall(r'\]\(docs/cases.md#([a-z0-9-]+)\)', text)
            self.assertEqual(links, expected)
            for entry in choices:
                self.assertIn(render.md_cell(entry['why_cn' if chinese else 'why']), text)

    def test_compact_matrix_retains_source_scope_reuse_and_validation(self):
        text = render.render_representative_comparison(self.rows)
        cases = {c['id']: c for c in render.load_cases()}
        rows = {r['id']: r for r in self.rows}
        self.assertIn('not a popularity, performance or maturity ranking', text)
        self.assertIn('not a complete current support list', text)
        for entry in render.load_showcase():
            self.assertIn(f"[upstream]({rows[entry['project_id']]['url']})", text)
            self.assertIn(f"[source]({cases[entry['case_id']]['evidence_urls'][0]})", text)
            for field in ('scope', 'boundary', 'reuse', 'validation'):
                for suffix in ('', '_cn'):
                    self.assertIn(render.md_cell(entry[field + suffix]), text)
        full = render.render_comparison(self.rows)
        for case in cases.values():
            self.assertIn(f"(cases.md#{case['id']})", full)
            self.assertIn(render.md_cell(case['cost']), full)

    def test_homepages_list_every_project_once_with_direct_upstream_links(self):
        for chinese in (False, True):
            text = render.render_overview(self.rows, chinese)
            ids = re.findall(r'<a id="project-([a-z0-9-]+)"></a>', text)
            self.assertCountEqual(ids, [r['id'] for r in self.rows])
            self.assertEqual(len(ids), len(set(ids)))
            external = re.findall(r'\]\((https://[^)]+)\)', text)
            for row in self.rows:
                self.assertEqual(external.count(row['url']), 1, row['id'])
                if not chinese:
                    self.assertIn(render.md_cell(row['mechanism']), text)
                self.assertIn(f"(docs/catalog.md#{row['id']})", text)
            # Complete entries are ordinary expanded Markdown, never hidden panels.
            self.assertNotIn('<details>', text)
            self.assertLess(text.index('project-'), text.index('id="featured-reading"'))

    def test_homepage_expands_every_functional_section_and_validation_contract(self):
        for chinese in (False, True):
            text = render.render_overview(self.rows, chinese)
            for role in render.SCHEMA['roles']:
                self.assertIn(f'(#homepage-{role["id"]})', text)
                self.assertIn(f'<a id="homepage-{role["id"]}"></a>', text)
            for id, en, cn, explanation, explanation_cn, methods in render.HOMEPAGE_VALIDATION:
                self.assertIn(f'id="homepage-validation-{id}"', text)
                self.assertIn(explanation_cn if chinese else explanation, text)
                for project_id, label, note, note_cn in methods:
                    self.assertIn(f'[{label}](#project-{project_id})', text)
                    self.assertIn(note_cn if chinese else note, text)
            self.assertNotIn('### Continue by task', text)

    def test_chinese_homepage_descriptions_cover_all_records(self):
        notes = render.load_homepage_cn()
        self.assertEqual(validate_homepage_cn(notes, self.rows), [])
        self.assertTrue(validate_homepage_cn({}, self.rows))
        broken = dict(notes)
        broken[self.rows[0]['id']] = ''
        self.assertTrue(validate_homepage_cn(broken, self.rows))
        text = render.render_overview(self.rows, True)
        for note in notes.values():
            self.assertIn(render.md_cell(note), text)

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
