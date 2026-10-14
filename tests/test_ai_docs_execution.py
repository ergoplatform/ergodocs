from __future__ import annotations

import argparse
from dataclasses import asdict
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import ai_docs_draft_prs as ai
from ai_docs_execution import (
    Budget,
    Checkpoint,
    GenerationFailure,
    Limits,
    content_hash,
    fingerprint,
    generate,
)
import docs_update_candidates as candidates

REF = "a" * 40
CHANGE = {"repo": "example/project", "sha": REF, "path": "README.md"}
ORIGINAL = "---\nlast_reviewed: never\nsource_repos:\n  - repo: example/project\n---\n\n# Example\n\n## Usage\n\nRun tool.\n"
PROPOSED = ORIGINAL + "\nThe tool supports --retry.\n"


def available_source(content="+ supports --retry"):
    return {
        "repo": "example/project",
        "ref": REF,
        "paths": ["README.md"],
        "source_id": "source-1",
        "url": f"https://github.com/example/project/commit/{REF}",
        "status": "available",
        "snapshot": {"sha": REF},
        "content_sha256": content_hash(content),
        "content": content,
        "error": None,
    }


def decision(action="draft-pr-safe", proposed=PROPOSED, source=None):
    source = source or available_source()
    return {
        "action": action,
        "confidence": "high",
        "summary": "Document --retry",
        "uncertainty": "Verify behavior",
        "proposed_markdown": proposed,
        "evidence_refs": [
            {
                "source_id": source["source_id"],
                "content_sha256": source["content_sha256"],
            }
        ],
    }


def envelope(response=None, *, usage=None, finish="stop"):
    return {
        "model": "served-model",
        "choices": [
            {
                "finish_reason": finish,
                "message": {"content": json.dumps(response or decision())},
            }
        ],
        "usage": usage,
    }


def completed(stdout=""):
    return subprocess.CompletedProcess([], 0, stdout, "")


class EvidenceTests(unittest.TestCase):
    def test_fetch_failure_is_structured_and_not_evidence(self):
        with patch.object(
            ai,
            "github_request",
            side_effect=HTTPError("https://api.github.com", 404, "secret", {}, None),
        ):
            sources = ai.source_context([CHANGE], "secret")
        self.assertFalse(ai.evidence_available(sources))
        self.assertEqual(sources[0]["status"], "unavailable")
        self.assertEqual(sources[0]["content"], "")
        self.assertEqual(sources[0]["error"]["http_status"], 404)
        self.assertNotIn("secret", json.dumps(sources))

    def test_commit_snapshot_and_content_hash(self):
        commit = {
            "sha": REF,
            "commit": {"message": "Add retry"},
            "files": [{"filename": "README.md", "patch": "@@ -1 +1 @@\n-old\n+new"}],
        }
        with patch.object(ai, "github_request", return_value=commit):
            sources = ai.source_context([CHANGE, CHANGE], "token")
        self.assertTrue(ai.evidence_available(sources))
        self.assertEqual(len(sources), 1)
        self.assertEqual(sources[0]["snapshot"], {"sha": REF})
        self.assertEqual(
            sources[0]["content_sha256"], content_hash(sources[0]["content"])
        )

    def test_missing_patch_and_unmatched_second_watched_path_block(self):
        commit = {
            "sha": REF,
            "commit": {"message": "Add retry"},
            "files": [{"filename": "README.md"}],
        }
        for changes in ([CHANGE], [CHANGE, {**CHANGE, "path": "src/api.scala"}]):
            with self.subTest(changes=changes), patch.object(
                ai, "github_request", return_value=commit
            ):
                self.assertFalse(
                    ai.evidence_available(ai.source_context(changes, "token"))
                )
        commit["files"][0]["patch"] = "+new"
        with patch.object(ai, "github_request", return_value=commit):
            self.assertFalse(
                ai.evidence_available(
                    ai.source_context(
                        [CHANGE, {**CHANGE, "path": "src/api.scala"}], "token"
                    )
                )
            )

    def test_release_requires_body_and_tracks_snapshot(self):
        release = {
            "id": 3,
            "tag_name": "v1",
            "body": "New retry API",
            "updated_at": "2026-01-01",
            "target_commitish": "main",
        }
        with patch.object(ai, "github_request", return_value=release):
            sources = ai.source_context([{**CHANGE, "sha": "release-v1"}], "token")
        self.assertTrue(ai.evidence_available(sources))
        self.assertEqual(sources[0]["snapshot"]["id"], 3)
        release["body"] = ""
        with patch.object(ai, "github_request", return_value=release):
            self.assertFalse(
                ai.evidence_available(
                    ai.source_context([{**CHANGE, "sha": "release-v1"}], "token")
                )
            )

    def test_pr_race_partial_files_and_file_fetch_failure_block(self):
        pull = {
            "head": {"sha": REF},
            "base": {"sha": "b" * 40},
            "state": "open",
            "updated_at": "today",
            "changed_files": 1,
            "title": "Retry",
            "body": "Retry API",
        }
        files = [{"filename": "README.md", "patch": "+retry"}]
        scenarios = [
            [pull, files, {**pull, "updated_at": "later"}],
            [pull, [], pull],
            [pull, URLError("secret")],
        ]
        for responses in scenarios:
            with self.subTest(responses=responses), patch.object(
                ai, "github_request", side_effect=responses
            ):
                sources = ai.source_context([{**CHANGE, "sha": "pr-12"}], "token")
                self.assertFalse(ai.evidence_available(sources))
                self.assertEqual(sources[0]["content"], "")

    def test_source_limits_cannot_silently_omit_required_evidence(self):
        release = {"id": 3, "tag_name": "v1", "body": "New API"}
        changes = [
            {**CHANGE, "repo": f"example/project{i}", "sha": "release-v1"}
            for i in range(9)
        ]
        with patch.object(ai, "github_request", return_value=release) as fetch:
            sources = ai.source_context(changes, "token")
        self.assertEqual(len(sources), 9)
        self.assertEqual(fetch.call_count, 8)
        self.assertFalse(ai.evidence_available(sources))
        with patch.object(ai, "MAX_SOURCE_CHARS", 2), patch.object(
            ai, "github_request", return_value=release
        ):
            sources = ai.source_context(changes[:1], "token")
        self.assertEqual(sources[0]["status"], "incomplete")
        self.assertEqual(sources[0]["content"], "")

    def test_forged_absent_and_wrong_hash_references_refuse_drafts(self):
        for refs in (
            [],
            [{"source_id": "invented", "content_sha256": "fake"}],
            [{"source_id": "source-1", "content_sha256": "fake"}],
        ):
            with self.subTest(refs=refs):
                raw = {**decision(), "evidence_refs": refs}
                self.assertEqual(
                    ai.assess_response(raw, ORIGINAL, [available_source()])[1],
                    "validation-refusal",
                )
        self.assertEqual(
            ai.assess_response(decision(), ORIGINAL, [available_source()])[1],
            "draft-ready",
        )

    def test_metadata_and_review_date_remain_human_owned(self):
        for replacement in (
            PROPOSED.replace("never", "2026-10-14"),
            PROPOSED.replace("example/project", "example/other"),
        ):
            self.assertFalse(ai.valid_markdown_update(ORIGINAL, replacement))


class BoundedGenerationTests(unittest.TestCase):
    def test_http_wall_clock_deadline_interrupts_slow_response_reads(self):
        class SlowResponse:
            finished = False

            def __enter__(self):
                return self

            def __exit__(self, *_):
                pass

            def read(self):
                time.sleep(0.2)
                self.finished = True
                return b"{}"

        response = SlowResponse()
        with patch.object(ai, "urlopen", return_value=response), self.assertRaises(
            TimeoutError
        ):
            ai.github_request("https://api.github.com/example", "fake", timeout=0.015)
        self.assertFalse(response.finished)

    def test_provider_adapters_preserve_usage_and_enforce_request_output_caps(self):
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_):
                pass

            def read(self):
                return json.dumps(envelope(usage={"total_tokens": 10})).encode()

        for provider in ("openai", "openrouter", "github-models"):
            with self.subTest(provider=provider), patch.object(
                ai, "urlopen", return_value=Response()
            ) as request:
                raw = ai.chat_completion_request(
                    "prompt", "fake", "model", provider, timeout=2, max_output_tokens=50
                )
            self.assertEqual(raw["usage"], {"total_tokens": 10})
            payload = json.loads(request.call_args.args[0].data)
            self.assertEqual(
                payload[
                    "max_completion_tokens" if provider == "openai" else "max_tokens"
                ],
                50,
            )
            self.assertEqual(request.call_args.kwargs["timeout"], 2)

    def invoke(self, request, limits=None, metrics=None):
        metrics = (
            metrics
            if metrics is not None
            else {"provider": "openai", "model": "requested-model", "attempts": []}
        )
        budget = Budget(limits or Limits())
        return (
            generate(
                "prompt",
                request,
                json.loads,
                budget,
                metrics,
                lambda: None,
                time.monotonic(),
            ),
            metrics,
        )

    def test_transient_retry_usage_and_elapsed_retained(self):
        request = unittest.mock.Mock(
            side_effect=[
                HTTPError("url", 503, "hidden", {}, None),
                envelope(
                    usage={
                        "prompt_tokens": 10,
                        "completion_tokens": 20,
                        "total_tokens": 30,
                    }
                ),
            ]
        )
        with patch("ai_docs_execution.time.sleep"):
            response, metrics = self.invoke(request)
        self.assertEqual(response["action"], "draft-pr-safe")
        self.assertEqual(len(metrics["attempts"]), 2)
        self.assertEqual(metrics["attempts"][0]["error"]["category"], "transient-http")
        self.assertEqual(metrics["usage"]["total_tokens"], 30)
        self.assertEqual(metrics["unreported_usage_attempts"], 1)
        self.assertEqual(metrics["attempts"][1]["response_model"], "served-model")
        self.assertGreaterEqual(metrics["elapsed_seconds"], 0)
        self.assertLessEqual(request.call_args.kwargs["timeout"], 60)
        self.assertEqual(request.call_args.kwargs["max_output_tokens"], 12000)

    def test_auth_and_malformed_responses_never_retry(self):
        for error in (HTTPError("url", 401, "secret", {}, None), {"choices": []}):
            request = unittest.mock.Mock(
                side_effect=error if isinstance(error, Exception) else None,
                return_value=error if isinstance(error, dict) else None,
            )
            with self.subTest(error=error), self.assertRaises(GenerationFailure):
                self.invoke(request)
            self.assertEqual(request.call_count, 1)

    def test_attempt_and_request_caps_enforced(self):
        request = unittest.mock.Mock(side_effect=URLError("secret"))
        for limits, expected_calls in (
            (Limits(max_attempts=2), 2),
            (Limits(max_requests=1), 1),
        ):
            request.reset_mock()
            with self.subTest(limits=limits), patch(
                "ai_docs_execution.time.sleep"
            ), self.assertRaises(GenerationFailure):
                self.invoke(request, limits)
            self.assertEqual(request.call_count, expected_calls)

    def test_prompt_and_elapsed_limits_prevent_calls(self):
        request = unittest.mock.Mock()
        with self.assertRaises(GenerationFailure):
            self.invoke(request, Limits(max_prompt_chars=2))
        request.assert_not_called()
        budget = Budget(Limits(run_timeout=1))
        budget.started -= 2
        with self.assertRaises(GenerationFailure):
            generate(
                "prompt",
                request,
                json.loads,
                budget,
                {"attempts": []},
                lambda: None,
                time.monotonic(),
            )
        request.assert_not_called()

    def test_truncation_and_bad_json_preserve_reported_usage(self):
        for response in (
            envelope(usage={"total_tokens": 12}, finish="length"),
            {
                "usage": {"total_tokens": 12},
                "choices": [
                    {"finish_reason": "stop", "message": {"content": "broken"}}
                ],
            },
        ):
            metrics = {"attempts": []}
            with self.subTest(response=response), self.assertRaises(GenerationFailure):
                self.invoke(unittest.mock.Mock(return_value=response), metrics=metrics)
            self.assertEqual(metrics["usage"], {"total_tokens": 12})
            self.assertEqual(len(metrics["attempts"]), 1)

    def test_successful_raw_response_checkpointed_before_normalization(self):
        metrics = {"attempts": []}
        snapshots = []
        generate(
            "prompt",
            lambda **_: envelope(),
            json.loads,
            Budget(Limits()),
            metrics,
            lambda: snapshots.append(json.loads(json.dumps(metrics))),
            time.monotonic(),
        )
        self.assertEqual(snapshots[-1]["response_sha256"], fingerprint(decision()))
        self.assertEqual(snapshots[0]["attempts"][0]["status"], "in-flight")


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        self.items = []
        for name in ("first", "second"):
            page = f"docs/{name}.md"
            (self.root / page).write_text(ORIGINAL)
            self.items.append(
                candidates.Candidate({"page": page}, page, name, name, [CHANGE], "test")
            )
        self.args = argparse.Namespace(
            output=self.root / "state/result.json",
            dry_run=True,
            resume=False,
            provider="openai",
            repo="example/docs",
            base_branch="main",
            max_pages=2,
        )
        self.root_patch = patch.object(ai, "ROOT", self.root)
        self.root_patch.start()
        self.config_patch = patch.object(
            ai,
            "configuration_fingerprint",
            side_effect=lambda args, model, limits: fingerprint(
                [model, asdict(limits)]
            ),
        )
        self.config_patch.start()
        self.sources_patch = patch.object(
            ai, "source_context", return_value=[available_source()]
        )
        self.fetch = self.sources_patch.start()
        self.run_patch = patch.object(ai, "run", return_value=completed())
        self.run_patch.start()

    def tearDown(self):
        self.sources_patch.stop()
        self.run_patch.stop()
        self.config_patch.stop()
        self.root_patch.stop()
        self.tmp.cleanup()

    def execute(self, limits=None):
        with Checkpoint(self.args.output) as checkpoint:
            return ai.execute_candidates(
                self.args,
                self.items,
                [],
                "model",
                "source-token",
                "model-token",
                checkpoint,
                limits or Limits(),
            )

    def read(self):
        return json.loads(self.args.output.read_text())

    def test_missing_evidence_blocks_generation_and_drafting(self):
        self.fetch.return_value = [
            {
                **available_source(),
                "status": "unavailable",
                "content": "",
                "content_sha256": None,
            }
        ]
        with patch.object(ai, "chat_completion_request") as model, patch.object(
            ai, "create_pr"
        ) as publish:
            output = self.execute()
        model.assert_not_called()
        publish.assert_not_called()
        self.assertTrue(
            all(
                row["outcome"] == "unavailable-evidence"
                and row["action"] == "dry-run-issue"
                for row in output["results"]
            )
        )

    def test_oversized_page_is_refused_before_generation(self):
        (self.root / "docs/first.md").write_text(ORIGINAL + "x" * ai.MAX_PAGE_CHARS)
        self.items = self.items[:1]
        with patch.object(ai, "chat_completion_request") as model:
            output = self.execute()
        model.assert_not_called()
        self.assertEqual(output["results"][0]["outcome"], "validation-refusal")
        self.assertEqual(
            output["results"][0]["error"]["category"], "page-content-limit"
        )

    def test_interruption_preserves_completed_page_and_resumes_pending_attempt(self):
        with patch.object(
            ai, "chat_completion_request", side_effect=[envelope(), KeyboardInterrupt()]
        ):
            with self.assertRaises(KeyboardInterrupt):
                self.execute()
        saved = self.read()
        self.assertEqual(saved["run_status"], "interrupted")
        self.assertEqual(saved["results"][0]["stage"], "complete")
        self.assertEqual(
            saved["results"][1]["generation"]["attempts"][0]["status"], "in-flight"
        )
        self.args.resume = True
        with patch.object(
            ai, "chat_completion_request", return_value=envelope()
        ) as model:
            output = self.execute()
        self.assertEqual(model.call_count, 1)
        self.assertEqual(self.fetch.call_count, 4)
        second = next(
            row for row in output["results"] if row["page"] == "docs/second.md"
        )
        self.assertEqual(len(second["generation"]["attempts"]), 2)

    def test_changed_page_source_configuration_or_candidate_invalidates_reuse(self):
        for change in ("page", "source", "configuration", "candidate"):
            with self.subTest(change=change):
                self.args.resume = False
                (self.root / "docs/first.md").write_text(ORIGINAL)
                self.fetch.return_value = [available_source()]
                self.items[0].changes = [CHANGE]
                with patch.object(
                    ai, "chat_completion_request", return_value=envelope()
                ):
                    self.execute()
                self.args.resume = True
                limits = Limits()
                if change == "page":
                    (self.root / "docs/first.md").write_text(
                        ORIGINAL + "\nExisting note.\n"
                    )
                elif change == "source":
                    self.fetch.return_value = [available_source("+new snapshot")]
                elif change == "configuration":
                    limits = Limits(max_output_tokens=300)
                else:
                    self.items[0].changes = [{**CHANGE, "date": "2026-10-14"}]
                with patch.object(
                    ai, "chat_completion_request", return_value=envelope()
                ) as model:
                    self.execute(limits)
                self.assertEqual(
                    model.call_count, 2 if change in {"source", "configuration"} else 1
                )

    def test_outage_on_resume_cannot_reuse_previous_success(self):
        with patch.object(ai, "chat_completion_request", return_value=envelope()):
            self.execute()
        self.args.resume = True
        self.fetch.return_value = [
            {**available_source(), "status": "unavailable", "content": ""}
        ]
        with patch.object(ai, "chat_completion_request") as model:
            output = self.execute()
        model.assert_not_called()
        self.assertTrue(
            all(row["outcome"] == "unavailable-evidence" for row in output["results"])
        )

    def test_later_model_failure_preserves_first_and_reports_nonzero_kind(self):
        with patch.object(
            ai,
            "chat_completion_request",
            side_effect=[envelope(), HTTPError("url", 401, "secret", {}, None)],
        ):
            output = self.execute()
        first, second = output["results"]
        self.assertEqual(first["action"], "dry-run-pr")
        self.assertEqual(second["outcome"], "generation-failure")
        self.assertEqual(second["error"]["category"], "authentication-or-permission")
        self.assertNotIn("secret", self.args.output.read_text())

    def test_validation_refusal_never_publishes_markdown(self):
        bad = {**decision(), "evidence_refs": []}
        with patch.object(
            ai, "chat_completion_request", return_value=envelope(bad)
        ), patch.object(ai, "create_pr") as publish:
            output = self.execute()
        publish.assert_not_called()
        self.assertTrue(
            all(row["outcome"] == "validation-refusal" for row in output["results"])
        )
        self.assertTrue(
            all(
                row["error"]["category"] == "evidence-reference-refusal"
                for row in output["results"]
            )
        )

    def test_publish_failure_saved_separately_and_resume_does_not_regenerate(self):
        self.args.dry_run = False

        def failed_publish(*args, **kwargs):
            saved = self.read()["results"][-1]
            self.assertEqual(saved["stage"], "publishing")
            self.assertIn("decision", saved)
            raise RuntimeError("publish service failed")

        with patch.object(ai, "assert_repository"), patch.object(
            ai, "assert_clean_checkout"
        ), patch.object(ai, "ensure_labels"), patch.object(
            ai, "chat_completion_request", return_value=envelope()
        ) as model, patch.object(
            ai, "create_pr", side_effect=failed_publish
        ) as publish:
            output = self.execute()
        self.assertEqual(model.call_count, 2)
        self.assertEqual(publish.call_count, 2)
        self.assertTrue(
            all(row["outcome"] == "publishing-failure" for row in output["results"])
        )
        self.args.resume = True
        with patch.object(ai, "assert_repository"), patch.object(
            ai, "ensure_labels"
        ), patch.object(ai, "chat_completion_request") as model, patch.object(
            ai,
            "create_pr",
            side_effect=lambda page, *_: {
                "page": page,
                "action": "updated-pr-branch",
                "url": "https://example/pr",
            },
        ):
            output = self.execute()
        model.assert_not_called()
        self.assertTrue(
            all(row["action"] == "updated-pr-branch" for row in output["results"])
        )

    def test_repository_integrity_error_stops_later_pages(self):
        self.args.dry_run = False
        with patch.object(ai, "assert_repository"), patch.object(
            ai, "ensure_labels"
        ), patch.object(
            ai, "chat_completion_request", return_value=envelope()
        ) as model, patch.object(
            ai, "create_pr", side_effect=ai.RepositoryIntegrityError("checkout damaged")
        ):
            with self.assertRaises(ai.RepositoryIntegrityError):
                self.execute()
        self.assertEqual(model.call_count, 1)
        self.assertEqual(self.read()["run_status"], "stopped")
        self.assertEqual(self.read()["error"]["category"], "repository-integrity")
        self.assertEqual(self.read()["results"][0]["outcome"], "publishing-failure")

    def test_tampered_checkpoint_decision_is_not_reused(self):
        with patch.object(ai, "chat_completion_request", return_value=envelope()):
            self.execute()
        saved = self.read()
        saved["results"][0]["decision"]["proposed_markdown"] = "# Destroyed\n"
        saved["results"][0]["generation"].pop("response", None)
        self.args.output.write_text(json.dumps(saved))
        self.args.resume = True
        with patch.object(
            ai, "chat_completion_request", return_value=envelope()
        ) as model:
            self.execute()
        self.assertEqual(model.call_count, 1)

    def test_failed_atomic_replace_keeps_previous_json(self):
        with Checkpoint(self.args.output) as checkpoint:
            checkpoint.save({"schema_version": 1, "results": []})
            previous = self.args.output.read_bytes()
            with patch(
                "ai_docs_execution.os.replace", side_effect=OSError("interrupted")
            ), self.assertRaises(OSError):
                checkpoint.save({"schema_version": 1, "results": [{"page": "new"}]})
            self.assertEqual(self.args.output.read_bytes(), previous)
            with self.assertRaises(ValueError):
                with Checkpoint(self.args.output):
                    pass

    def test_resume_revalidates_saved_generated_response_without_extra_call(self):
        with patch.object(ai, "chat_completion_request", return_value=envelope()):
            self.execute()
        saved = self.read()
        for row in saved["results"]:
            row.pop("decision")
            row.pop("decision_sha256")
            row["stage"] = "generating"
        self.args.output.write_text(json.dumps(saved))
        self.args.resume = True
        with patch.object(ai, "chat_completion_request") as model:
            self.execute()
        model.assert_not_called()

    def test_dry_run_generation_failure_returns_nonzero_exit(self):
        report = self.root / "report.json"
        report.write_text('{"pages": []}')
        argv = [
            "ai_docs_draft_prs.py",
            "--report",
            str(report),
            "--output",
            str(self.args.output),
            "--dry-run",
        ]
        with patch.object(sys, "argv", argv), patch.dict(
            os.environ, {"GITHUB_TOKEN": "fake", "OPENAI_API_KEY": "fake"}
        ), patch.object(
            ai.candidates, "build_candidates", return_value=(self.items, [])
        ), patch.object(
            ai,
            "chat_completion_request",
            side_effect=HTTPError("url", 401, "hidden", {}, None),
        ), patch(
            "sys.stdout"
        ):
            self.assertEqual(ai.main(), 1)
        self.assertEqual(self.read()["results"][0]["outcome"], "generation-failure")

    def test_no_change_is_saved_and_reused_without_publishing(self):
        with patch.object(
            ai,
            "chat_completion_request",
            return_value=envelope(decision("no-doc-change", "")),
        ), patch.object(ai, "create_pr") as pr, patch.object(
            ai, "create_or_update_issue"
        ) as issue:
            output = self.execute()
        pr.assert_not_called()
        issue.assert_not_called()
        self.assertTrue(
            all(
                row["outcome"] == "no-change" and row["action"] == "no-doc-change"
                for row in output["results"]
            )
        )
        self.args.resume = True
        with patch.object(ai, "chat_completion_request") as model:
            self.execute()
        model.assert_not_called()

    def test_permanent_generation_failure_is_not_retried_on_resume(self):
        with patch.object(
            ai,
            "chat_completion_request",
            side_effect=HTTPError("url", 403, "hidden", {}, None),
        ):
            self.execute()
        self.args.resume = True
        with patch.object(ai, "chat_completion_request") as model:
            self.execute()
        model.assert_not_called()


class PublishingSafetyTests(unittest.TestCase):
    def test_local_human_branch_is_not_reset(self):
        commands = []

        def fake(command, **kwargs):
            commands.append(command)
            if command[:3] == ["git", "rev-parse", "ai-docs/example"]:
                return completed("human-commit")
            if "--format=%ae" in command:
                return completed("human@example.com")
            if "--format=%an" in command:
                return completed("Human")
            return completed()

        with patch.object(ai, "run", side_effect=fake):
            self.assertFalse(ai.branch_owned_by_automation("ai-docs/example"))
        self.assertFalse(
            any(command[:3] == ["git", "checkout", "-B"] for command in commands)
        )

    def test_dirty_checkout_and_mismatched_remote_stop(self):
        with patch.object(
            ai, "run", return_value=completed("docs/local.md\n")
        ), self.assertRaises(ai.RepositoryIntegrityError):
            ai.assert_clean_checkout(Path("tools/state/result.json"))

        def repository_command(command, **kwargs):
            return completed(
                str(ai.ROOT)
                if "--show-toplevel" in command
                else "https://github.com/other/repo.git"
            )

        with patch.object(ai, "run", side_effect=repository_command), self.assertRaises(
            ai.RepositoryIntegrityError
        ):
            ai.assert_repository("example/docs", Path("tools/state/result.json"))

    def test_duplicate_lookup_failure_never_creates_new_issue(self):
        with patch.object(
            ai,
            "run",
            side_effect=subprocess.CalledProcessError(1, ["gh", "issue", "list"]),
        ) as run:
            with self.assertRaises(subprocess.CalledProcessError):
                ai.create_or_update_issue(
                    "docs/example.md", decision(), ["docs"], False
                )
        self.assertEqual(run.call_count, 1)

    def test_existing_ready_pr_is_never_pushed(self):
        commands = []

        def fake(command, **kwargs):
            commands.append(command)
            if command[:3] == ["gh", "pr", "list"]:
                return completed("https://github.com/example/docs/pull/1")
            if command[:3] == ["gh", "pr", "view"]:
                return completed('{"isDraft": false}')
            return completed()

        with patch.object(ai, "run", side_effect=fake), self.assertRaises(
            ai.RepositoryIntegrityError
        ):
            ai.create_pr(
                "docs/example.md", PROPOSED, decision(), ["docs"], "main", False
            )
        self.assertFalse(any(command[:2] == ["git", "push"] for command in commands))
        self.assertFalse(
            any(command[:3] == ["git", "checkout", "-B"] for command in commands)
        )


if __name__ == "__main__":
    unittest.main()
