from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import ai_docs_draft_prs as ai_prs  # noqa: E402
import docs_update_candidates as candidates  # noqa: E402


class MarkdownValidationTests(unittest.TestCase):
    def test_allows_legitimate_ai_page_content(self) -> None:
        original = """---
owner: docs
source_repos:
  - repo: example/ai
source_of_truth:
  - https://example.com
---

# AI Tools

## Overview

Short overview.
"""
        proposed = """---
owner: docs
source_repos:
  - repo: example/ai
source_of_truth:
  - https://example.com
---

# AI Tools

## Overview

Expanded overview for AI tooling.
"""
        self.assertTrue(ai_prs.valid_markdown_update(original, proposed))

    def test_rejects_lost_source_metadata(self) -> None:
        original = """---
owner: docs
source_repos:
  - repo: example/project
source_of_truth:
  - https://example.com
---

# Project

## Overview

Text.
"""
        proposed = """---
owner: docs
source_repos:
  - repo: example/project
---

# Project

## Overview

Text with update.
"""
        self.assertFalse(ai_prs.valid_markdown_update(original, proposed))

    def test_rejects_changed_source_metadata_values(self) -> None:
        original = """---
owner: docs
source_repos:
  - repo: example/project
source_of_truth:
  - https://example.com/project
---

# Project

## Overview

Text.
"""
        proposed = """---
owner: docs
source_repos:
  - repo: example/other
source_of_truth:
  - https://example.com/project
---

# Project

## Overview

Text with update.
"""
        self.assertFalse(ai_prs.valid_markdown_update(original, proposed))

    def test_rejects_invalid_model_response(self) -> None:
        with self.assertRaises(ValueError):
            ai_prs.normalize_model_response({"action": "maybe", "confidence": "high", "summary": "", "uncertainty": "", "proposed_markdown": ""})

    def test_accepts_valid_model_response(self) -> None:
        result = ai_prs.normalize_model_response(
            {
                "action": "needs-human-review",
                "confidence": "medium",
                "summary": "summary",
                "uncertainty": "check",
                "proposed_markdown": "",
            }
        )
        self.assertEqual(result["action"], "needs-human-review")

    def test_rejects_large_destructive_update(self) -> None:
        original = "# Project\n\n" + "\n".join(f"## Section {index}\n\nText." for index in range(8))
        proposed = "# Project\n\nTiny update."
        self.assertFalse(ai_prs.valid_markdown_update(original, proposed))


class CandidateScoringTests(unittest.TestCase):
    def test_page_tokens_include_tags_and_sources(self) -> None:
        page = {
            "page": "docs/dev/scs/page.md",
            "tags": ["Sigmastate Interpreter"],
            "source_repos": [{"repo": "ergoplatform/sigmastate-interpreter"}],
            "source_of_truth": ["https://github.com/ergoplatform/sigmastate-interpreter/releases"],
        }
        tokens = candidates.page_tokens(page)
        self.assertIn("sigmastate", tokens)
        self.assertIn("compiler", tokens)

    def test_weighted_scoring_rejects_body_only_weak_overlap(self) -> None:
        page = {
            "page": "docs/dev/scs/page.md",
            "tags": ["Sigmastate Interpreter"],
            "source_repos": [{"repo": "ergoplatform/sigmastate-interpreter"}],
            "source_of_truth": ["https://github.com/ergoplatform/sigmastate-interpreter"],
        }
        change = {"message": "updated unrelated prose", "severity": "medium", "kind": "commit", "path": "README.md"}
        self.assertFalse(candidates.actionable_change(page, change))

    def test_release_scan_targets_identity_not_every_watched_page(self) -> None:
        release = {
            "message": "Release v6.0.4: Sigma SDK v6.0.4",
            "severity": "medium",
            "kind": "release",
            "repo": "ScorexFoundation/sigmastate-interpreter",
            "path": "release",
        }
        broad_page = {
            "page": "docs/dev/scs/syntax.md",
            "tags": ["Syntax", "ErgoScript"],
            "source_repos": [{"repo": "ScorexFoundation/sigmastate-interpreter"}],
            "source_of_truth": ["https://github.com/ScorexFoundation/sigmastate-interpreter/tree/develop/docs/LangSpec.md"],
        }
        repo_page = {
            "page": "docs/dev/scs/sigmastate-interpreter.md",
            "tags": ["Sigmastate Interpreter"],
            "source_repos": [{"repo": "ScorexFoundation/sigmastate-interpreter"}],
            "source_of_truth": ["https://github.com/ScorexFoundation/sigmastate-interpreter/tree/develop/README.md"],
        }
        release_page = {
            "page": "docs/node/rust-node.md",
            "tags": ["Rust", "Node"],
            "source_repos": [{"repo": "mwaddip/ergo-node-rust"}],
            "source_of_truth": ["https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.9"],
        }
        rust_release = {**release, "repo": "mwaddip/ergo-node-rust", "message": "Release v0.6.9: v0.6.9"}

        self.assertFalse(candidates.actionable_change(broad_page, release))
        self.assertTrue(candidates.actionable_change(repo_page, release))
        self.assertTrue(candidates.actionable_change(release_page, rust_release))


class BranchSafetyTests(unittest.TestCase):
    def test_dry_run_does_not_check_branch_ownership(self) -> None:
        result = ai_prs.create_pr(
            "docs/example.md",
            "# Example\n",
            {"action": "needs-human-review"},
            ["docs"],
            "main",
            True,
        )
        self.assertEqual(result["action"], "dry-run-pr")
        self.assertEqual(result["branch"], "ai-docs/example")

    def test_protected_branch_skips_push(self) -> None:
        calls: list[list[str]] = []

        def fake_run(command: list[str], *, check: bool = True):
            calls.append(command)
            if command[:3] == ["git", "ls-remote", "--heads"]:
                return _completed("abc\trefs/heads/ai-docs/example\n")
            if command[:3] == ["git", "log", "-1"] and "--format=%ae" in command:
                return _completed("human@example.com\n")
            if command[:3] == ["git", "log", "-1"] and "--format=%an" in command:
                return _completed("Human\n")
            if command[:3] == ["gh", "pr", "list"]:
                return _completed("https://github.com/ergoplatform/ergodocs/pull/1\n")
            return _completed("")

        with patch.object(ai_prs, "run", side_effect=fake_run):
            result = ai_prs.create_pr("docs/example.md", "# Example\n", {"action": "needs-human-review"}, ["docs"], "main", False)

        self.assertEqual(result["action"], "protected-existing-branch")
        self.assertFalse(any(command[:2] == ["git", "push"] for command in calls))

    def test_invalid_review_markdown_creates_issue(self) -> None:
        with patch.object(ai_prs, "create_or_update_issue") as issue:
            issue.return_value = {"page": "docs/example.md", "action": "created-issue", "url": "https://example.com/1"}
            result = ai_prs.create_review_pr(
                "docs/example.md",
                "# Example\n\n## Existing\n\nText.",
                {"action": "needs-human-review", "proposed_markdown": ""},
                ["docs"],
                "main",
                False,
            )
        self.assertEqual(result["action"], "created-issue")

    def test_existing_issue_lookup_parses_json_in_python(self) -> None:
        with patch.object(
            ai_prs,
            "run",
            return_value=_completed('[{"title":"Other","url":"https://example.com/0"},{"title":"Docs review needed: example.md","url":"https://example.com/1"}]'),
        ) as mocked:
            url = ai_prs.existing_issue_url("Docs review needed: example.md")
        self.assertEqual(url, "https://example.com/1")
        self.assertNotIn("--jq", mocked.call_args.args[0])

    def test_no_diff_updates_existing_pr_body(self) -> None:
        commands: list[list[str]] = []

        def fake_run(command: list[str], *, check: bool = True):
            commands.append(command)
            if command[:3] == ["git", "ls-remote", "--heads"]:
                return _completed("")
            if command[:3] == ["gh", "pr", "list"]:
                return _completed("https://github.com/ergoplatform/ergodocs/pull/1\n")
            if command[:3] == ["git", "diff", "--"]:
                return _completed("")
            return _completed("")

        with (
            patch.object(ai_prs, "run", side_effect=fake_run),
            patch.object(ai_prs, "safe_repo_path", return_value=ROOT / "docs/example.md"),
            patch.object(Path, "write_text", return_value=0),
        ):
            result = ai_prs.create_pr(
                "docs/example.md",
                "# Example\n",
                {"action": "needs-human-review"},
                ["docs"],
                "main",
                False,
            )
        self.assertEqual(result["action"], "updated-pr-body")
        self.assertTrue(any(command[:3] == ["gh", "pr", "edit"] for command in commands))

    def test_generated_pr_runs_checks_before_push(self) -> None:
        commands: list[list[str]] = []

        def fake_run(command: list[str], *, check: bool = True):
            commands.append(command)
            if command[:3] == ["git", "ls-remote", "--heads"]:
                return _completed("")
            if command[:3] == ["gh", "pr", "list"]:
                return _completed("")
            if command[:3] == ["git", "diff", "--"]:
                return _completed("diff")
            if command[:3] == ["gh", "pr", "create"]:
                return _completed("https://github.com/ergoplatform/ergodocs/pull/2\n")
            return _completed("")

        with (
            patch.object(ai_prs, "run", side_effect=fake_run),
            patch.object(ai_prs, "safe_repo_path", return_value=ROOT / "docs/example.md"),
            patch.object(Path, "write_text", return_value=0),
        ):
            result = ai_prs.create_pr(
                "docs/example.md",
                "# Example\n\nUpdated.",
                {"action": "draft-pr-safe"},
                ["docs"],
                "main",
                False,
            )
        self.assertEqual(result["action"], "created-pr")
        check_index = next(index for index, command in enumerate(commands) if command[:3] == ["git", "diff", "--cached"])
        push_index = next(index for index, command in enumerate(commands) if command[:2] == ["git", "push"])
        self.assertLess(check_index, push_index)


def _completed(stdout: str):
    class Completed:
        def __init__(self, value: str) -> None:
            self.stdout = value

    return Completed(stdout)


if __name__ == "__main__":
    unittest.main()
