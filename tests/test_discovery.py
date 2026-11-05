"""Protect curated routing integrity and the canonical scope boundary."""
import copy
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import discovery
import update_readme


class DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = update_readme.load_rows()
        cls.routes = discovery.load_routes(cls.rows)

    def test_bad_references_and_duplicate_navigation_are_rejected(self):
        for field, value in [('projects', ['missing-project']), ('projects', []),
                             ('label_cn', ''), ('homepage', 'yes'), ('id', 'invalid anchor')]:
            broken = copy.deepcopy(self.routes)
            broken['hardware'][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                discovery.validate_routes(broken, self.rows)
        for field in ('projects', 'id'):
            broken = copy.deepcopy(self.routes)
            if field == 'projects':
                broken['hardware'][0][field] *= 2
            else:
                broken['models'][0][field] = broken['hardware'][0][field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                discovery.validate_routes(broken, self.rows)

    def test_every_shortcut_reaches_scope_copied_from_catalog(self):
        guide = discovery.render_guide(self.rows)
        by_id = {r['id']: r for r in self.rows}
        for groups in self.routes.values():
            for group in groups:
                self.assertIn(f'id="{group["id"]}"', guide)
                for id in group['projects']:
                    self.assertIn(discovery.cell(by_id[id]['target']), guide)
                    self.assertIn(by_id[id]['checked_on'], guide)
                    self.assertIn(by_id[id]['source_visibility'], guide)
                for chinese in (False, True):
                    shortcuts = '\n'.join(discovery.render_shortcuts(self.rows, chinese))
                    self.assertEqual(f'(docs/find-a-stack.md#{group["id"]})' in shortcuts,
                                     group['homepage'])

    def test_source_scope_change_propagates_without_editing_routes(self):
        changed = copy.deepcopy(self.rows)
        id = self.routes['hardware'][0]['projects'][0]
        next(r for r in changed if r['id'] == id)['target'] = 'Changed reviewed scope | <limit>'
        self.assertIn('Changed reviewed scope &#124; &lt;limit&gt;', discovery.render_guide(changed))


if __name__ == '__main__':
    unittest.main()
