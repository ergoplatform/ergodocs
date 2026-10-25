from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import external_link_audit as audit  # noqa: E402


class ExternalLinkCollectionTests(unittest.TestCase):
    def test_collects_sources_and_excludes_local_examples(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "nested").mkdir()
            (site / "index.html").write_text(
                """
                <a href="https://example.com/page#section">Example</a>
                <a href="http://localhost:9053/info">Local</a>
                <a href="http://192.168.0.10:9053/info">LAN</a>
                <a href="https://example.com/{address}">Placeholder</a>
                <link rel="preconnect" href="https://fonts.gstatic.com">
                <a href="https://fonts.gstatic.com">Font host link</a>
                """,
                encoding="utf-8",
            )
            (site / "nested" / "index.html").write_text(
                '<a href="https://example.com/page">Again</a>', encoding="utf-8"
            )

            sources, excluded, page_count = audit.collect_urls(site)

        self.assertEqual(page_count, 2)
        self.assertEqual(
            sources["https://example.com/page"], ["index.html", "nested/index.html"]
        )
        self.assertEqual(sources["https://fonts.gstatic.com"], ["index.html"])
        reasons = {(item["url"], item["reason"]) for item in excluded}
        self.assertIn(("http://localhost:9053/info", "local example host"), reasons)
        self.assertIn(
            ("http://192.168.0.10:9053/info", "private or local example address"),
            reasons,
        )
        self.assertIn(("https://example.com/{address}", "placeholder URL"), reasons)
        self.assertIn(("https://fonts.gstatic.com", "font preconnect"), reasons)

    def test_collects_scheme_relative_urls_and_keeps_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text(
                '<a href="//example.com/page#section">External</a>'
                '<a href="HTTPS://example.com/upper">Uppercase</a>'
                '<a href="//localhost/example">Local</a>'
                '<a href="/relative">Relative</a>', encoding="utf-8"
            )
            sources, excluded, _ = audit.collect_urls(site)
        self.assertEqual(set(sources), {
            "https://example.com/page", "https://example.com/upper"
        })
        self.assertEqual(excluded[0]["reason"], "local example host")

    def test_requires_rendered_html(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "No HTML files"):
                audit.collect_urls(Path(directory))


class ExternalLinkClassificationTests(unittest.TestCase):
    def test_retries_and_classifies_final_results(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            site.joinpath("index.html").write_text(
                """
                <a href="https://fixed.example">Fixed</a>
                <a href="https://missing.example">Missing</a>
                <a href="https://timeout.example">Timeout</a>
                <a href="https://blocked.example">Blocked</a>
                """,
                encoding="utf-8",
            )
            calls: dict[str, int] = {}

            def fake_check(
                url: str, _connect: float, _read: float, browser_headers: bool
            ) -> dict:
                calls[url] = calls.get(url, 0) + 1
                if url == "https://fixed.example" and calls[url] > 1:
                    self.assertTrue(browser_headers)
                    return {"status": 200, "final_url": url, "error": None}
                if url == "https://fixed.example" or url == "https://missing.example":
                    return {"status": 404, "final_url": url, "error": None}
                if url == "https://blocked.example":
                    return {"status": 403, "final_url": url, "error": None}
                return {
                    "status": None,
                    "final_url": None,
                    "error": "read-timeout",
                    "detail": "slow",
                }

            report = audit.audit_site(
                site,
                workers=1,
                retry_workers=1,
                retries=1,
                retry_delay=0,
                progress_every=0,
                check_fn=fake_check,
            )

        results = {item["url"]: item for item in report["results"]}
        self.assertEqual(results["https://fixed.example"]["outcome"], "ok")
        self.assertEqual(results["https://missing.example"]["outcome"], "actionable")
        self.assertEqual(results["https://timeout.example"]["outcome"], "warning")
        self.assertEqual(results["https://blocked.example"]["outcome"], "warning")
        self.assertEqual(report["summary"], {"ok": 1, "warning": 2, "actionable": 1})
        self.assertEqual(calls["https://missing.example"], 2)
        self.assertEqual(calls["https://blocked.example"], 1)

    def test_invalid_url_is_actionable_without_retry(self) -> None:
        attempt = audit.check_url("https://example.com:bad", 1, 1)
        self.assertEqual(attempt["error"], "invalid-url")
        self.assertFalse(audit.needs_retry(attempt))
        self.assertEqual(audit.classify_attempt(attempt)[0], "actionable")

    def test_dns_detection_is_narrower_than_generic_connection_error(self) -> None:
        self.assertEqual(audit.connection_error_kind("Failed to resolve host"), "dns")
        self.assertEqual(
            audit.connection_error_kind("Connection reset by peer"), "connection"
        )


class ExternalLinkReportTests(unittest.TestCase):
    def sample_report(self, actionable: int = 1) -> dict:
        items = []
        if actionable:
            items.append(
                {
                    "url": "https://missing.example",
                    "pages": ["guide/index.html"],
                    "outcome": "actionable",
                    "reason": "HTTP 404 after retry",
                }
            )
        return {
            "generated": "2026-09-08T00:00:00+00:00",
            "html_pages": 1,
            "unique_external_urls": len(items),
            "checked_urls": len(items),
            "excluded_urls": 0,
            "summary": {"ok": 0, "warning": 0, "actionable": actionable},
            "results": items,
            "excluded": [],
        }

    def test_markdown_contains_actionable_source(self) -> None:
        markdown = audit.render_markdown(self.sample_report())
        self.assertIn("https://missing.example", markdown)
        self.assertIn("`guide/index.html`", markdown)

    def test_sync_issue_updates_one_and_closes_duplicate(self) -> None:
        calls: list[tuple[str, str, dict | None]] = []
        existing = [
            {
                "number": 10,
                "title": audit.ISSUE_TITLE,
                "url": "https://api.github.test/issues/10",
                "html_url": "https://github.test/issues/10",
                "comments_url": "https://api.github.test/issues/10/comments",
            },
            {
                "number": 11,
                "title": audit.ISSUE_TITLE,
                "url": "https://api.github.test/issues/11",
                "html_url": "https://github.test/issues/11",
                "comments_url": "https://api.github.test/issues/11/comments",
            },
        ]

        def fake_request(
            method: str, url: str, _token: str, payload: dict | None = None
        ):
            calls.append((method, url, payload))
            if method == "GET":
                return {"items": existing}
            if method == "PATCH" and url.endswith("/10"):
                return existing[0]
            return {}

        with patch.object(audit, "github_request", side_effect=fake_request):
            result = audit.sync_issue(
                self.sample_report(), "org/repo", "token", "https://run.test"
            )

        self.assertEqual(result["action"], "updated")
        self.assertEqual(result["closed_duplicates"], 1)
        self.assertTrue(
            any(
                method == "PATCH"
                and url.endswith("/11")
                and payload == {"state": "closed"}
                for method, url, payload in calls
            )
        )

    def test_sync_issue_closes_existing_when_clean(self) -> None:
        issue = {
            "number": 10,
            "title": audit.ISSUE_TITLE,
            "url": "https://api.github.test/issues/10",
            "html_url": "https://github.test/issues/10",
            "comments_url": "https://api.github.test/issues/10/comments",
        }

        def fake_request(
            method: str, url: str, _token: str, payload: dict | None = None
        ):
            if method == "GET":
                return {"items": [issue]}
            return {}

        with patch.object(audit, "github_request", side_effect=fake_request) as request:
            result = audit.sync_issue(
                self.sample_report(actionable=0), "org/repo", "token", ""
            )

        self.assertEqual(result["action"], "closed")
        request.assert_any_call("PATCH", issue["url"], "token", {"state": "closed"})


if __name__ == "__main__":
    unittest.main()
