import tempfile
import unittest
from pathlib import Path
from tools.internal_link_audit import audit


class InternalLinkAuditTest(unittest.TestCase):
    def run_audit(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            return audit(root)

    def test_resolves_cards_images_root_links_and_encoded_anchors(self):
        count, issues = self.run_audit(
            {
                "index.html": '<a href="guide/?q=1#caf%C3%A9">Card</a><img src="images/a%20b.svg"><a href="/#home">Home</a><h1 id="home">Home</h1>',
                "guide/index.html": '<a name="café"></a><a href="../#home:~:text=Home">Back</a>',
                "images/a b.svg": "<svg></svg>",
            }
        )
        self.assertEqual(count, 2)
        self.assertEqual(issues, [])

    def test_reports_case_mismatch_missing_anchor_and_escaping_path(self):
        _, issues = self.run_audit(
            {
                "index.html": '<a href="guide/">Bad case</a><a href="Guide/#missing">Bad anchor</a><img src="absent.png"><a href="../secret">Escape</a>',
                "Guide/index.html": '<h1 id="exists">Guide</h1>',
            }
        )
        self.assertEqual(len(issues), 4)
        self.assertIn("path escapes site", [i.reason for i in issues])
        self.assertIn("missing anchor #missing", [i.reason for i in issues])

    def test_ignores_external_links_and_text_only_fragments(self):
        _, issues = self.run_audit(
            {
                "index.html": '<a href="https://example.com/bad">External</a><a href="//example.com">External</a><a href="mailto:docs@example.com">Email</a><a href="#:~:text=example">Text</a>'
            }
        )
        self.assertEqual(issues, [])

    def test_same_site_absolute_urls_use_the_local_build(self):
        _, issues = self.run_audit(
            {
                "index.html": '<a href="https://docs.ergoplatform.com/guide/#ok">Good</a><a href="https://docs.ergoplatform.org/absent/">Bad</a><a href="//docs.ergoplatform.com/guide/#missing">Bad anchor</a>',
                "guide/index.html": '<h1 id="ok">Guide</h1><a href="https://docs.ergoplatform.com">Home</a>',
            }
        )
        self.assertEqual(len(issues), 2)
        self.assertIn("missing anchor #missing", [i.reason for i in issues])

    def test_empty_directory_has_no_pages(self):
        self.assertEqual(self.run_audit({}), (0, []))


if __name__ == "__main__":
    unittest.main()
