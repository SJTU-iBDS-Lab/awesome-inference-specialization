"""Execute the repository's two generation checks inside the existing CI test job.

The workflow already runs validate_catalog.py, update_readme.py --check,
and unittest discovery. These tests exercise the remaining documented
commands without modifying GitHub Actions or requiring network access.
"""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MaintenanceCommandTests(unittest.TestCase):
    def test_banner_check_command(self):
        subprocess.run([sys.executable, "scripts/generate_banner.py", "--check"],
                       cwd=ROOT, check=True, capture_output=True, text=True)

    def test_generate_catalog_command(self):
        subprocess.run([sys.executable, "scripts/update_readme.py"],
                       cwd=ROOT, check=True, capture_output=True, text=True)
