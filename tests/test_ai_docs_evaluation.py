from __future__ import annotations
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import evaluate_ai_docs as evaluation
from ai_docs_execution import Budget, Limits


class EvaluationTests(unittest.TestCase):
    def test_manual_workflow_defaults_and_resume_budget_contract(self):
        root = Path(__file__).resolve().parents[1]
        workflow = yaml.safe_load(
            (root / ".github/workflows/ai-docs-draft-prs.yml").read_text()
        )
        triggers = workflow.get("on", workflow.get(True))
        self.assertEqual(set(triggers), {"workflow_dispatch"})
        self.assertEqual(
            triggers["workflow_dispatch"]["inputs"]["dry_run"]["default"], "true"
        )
        job = workflow["jobs"]["draft"]
        self.assertEqual(job["permissions"]["actions"], "read")
        self.assertNotIn("OPENAI_API_KEY", job["env"])
        steps = job["steps"]
        restore_index = next(
            i
            for i, step in enumerate(steps)
            if step["name"] == "Restore prior checkpoint"
        )
        generation_index = next(
            i
            for i, step in enumerate(steps)
            if step["name"] == "Create AI-assisted draft PRs"
        )
        self.assertLess(restore_index, generation_index)
        self.assertIn('--repo "$GITHUB_REPOSITORY"', steps[restore_index]["run"])
        generation = steps[generation_index]
        self.assertIn("EXTRA_ARGS+=(--resume)", generation["run"])
        for flag in ("--max-requests", "--max-output-tokens", "--run-timeout"):
            self.assertIn(flag, generation["run"])
        self.assertIn("OPENAI_API_KEY", generation["env"])

    def setUp(self):
        self.cases = json.loads(evaluation.DEFAULT_CASES.read_text())["cases"]

    def test_recorded_regression_cases_pass_without_network_or_publication(self):
        with patch.object(
            evaluation.automation, "chat_completion_request"
        ) as model, patch.object(evaluation.automation, "create_pr") as publish:
            result = evaluation.evaluate(self.cases)
        model.assert_not_called()
        publish.assert_not_called()
        self.assertEqual(result["summary"]["recorded-response"]["total"], 12)
        self.assertTrue(all(row["passed"] for row in result["results"]))

    def test_live_comparison_uses_one_shared_request_budget(self):
        cases = [case for case in self.cases if case.get("live")]
        with patch.object(
            evaluation.automation,
            "chat_completion_request",
            return_value={
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {
                            "content": '{"action":"no-doc-change","confidence":"high"}'
                        },
                    }
                ]
            },
        ) as model:
            result = evaluation.evaluate(
                cases,
                provider="openai",
                models=["model-a", "model-b"],
                token="fake",
                budget=Budget(
                    Limits(max_attempts=1, max_requests=1, max_output_tokens=200)
                ),
            )
        self.assertEqual(model.call_count, 1)
        self.assertEqual(model.call_args.kwargs["max_output_tokens"], 200)
        self.assertFalse(result["summary"]["model-a"]["usage_is_complete"])
        self.assertEqual(result["summary"]["model-b"]["requests"], 0)
        self.assertTrue(
            any(
                row.get("error", {}).get("category") == "execution-limit"
                for row in result["results"]
            )
        )

    def test_live_requires_explicit_model_and_budget_before_any_call(self):
        with patch.object(sys, "argv", ["evaluate_ai_docs.py", "--live"]), patch.object(
            evaluation.automation, "chat_completion_request"
        ) as model, patch("sys.stderr"), self.assertRaises(SystemExit) as exit:
            evaluation.main()
        self.assertEqual(exit.exception.code, 2)
        model.assert_not_called()


if __name__ == "__main__":
    unittest.main()
