import unittest
from classify_changes import recipe_ci_required


class Routing(unittest.TestCase):
    def test_owned_documentation_and_ci_support(self):
        self.assertFalse(recipe_ci_required(["AGENTS.md", "docs/fair-bioheaders/ci.md", ".github/workflows/PR.yml", "scripts/fair_bioheaders/check_docs.py"]))

    def test_recipe_or_global_or_unknown_changes_keep_upstream_ci(self):
        for path in ["recipes/example/meta.yaml", "recipes/example/run_test.sh", "config.yml", "scripts/other.py", "README.md", ".github/workflows/master.yml"]:
            with self.subTest(path=path):
                self.assertTrue(recipe_ci_required(["AGENTS.md", path]))

    def test_empty_diff_is_conservative(self):
        self.assertTrue(recipe_ci_required([]))
