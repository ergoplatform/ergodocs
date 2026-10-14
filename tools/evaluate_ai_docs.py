#!/usr/bin/env python3
"""Repeatable docs policy evaluation; live comparisons require explicit budgets."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import time
from typing import Any

import ai_docs_draft_prs as automation
from ai_docs_execution import (
    Budget,
    Checkpoint,
    GenerationFailure,
    Limits,
    content_hash,
    fingerprint,
    generate,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "tests/fixtures/ai_docs_evaluation.json"


def fixture_inputs(case: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    content = case["source_content"]
    source = {
        "source_id": "fixture-" + fingerprint(case["name"]),
        "repo": "example/project",
        "ref": "fixture",
        "paths": ["README.md"],
        "url": "https://github.com/example/project",
        "snapshot": {"fixture": case["name"]},
        "status": case["source_status"],
        "content": content if case["source_status"] == "available" else "",
        "content_sha256": content_hash(content),
        "error": None,
    }
    response = json.loads(
        json.dumps(case["response"])
        .replace("$SOURCE_ID", source["source_id"])
        .replace("$CONTENT_SHA256", source["content_sha256"])
    )
    return [source], response


def evaluate(
    cases: list[dict[str, Any]],
    *,
    provider: str = "fixture",
    models: list[str] | None = None,
    token: str = "",
    budget: Budget | None = None,
    save=None,
) -> dict[str, Any]:
    """No publication path or source-network requests exist in this harness."""
    output: dict[str, Any] = {
        "schema_version": 1,
        "mode": "live" if budget else "fixture",
        "provider": provider,
        "fixture_sha256": fingerprint(cases),
        "results": [],
        "scope": "Policy/outcome regression only; human reviewers assess factual faithfulness.",
    }
    for model in models or ["recorded-response"]:
        for case in cases:
            sources, raw = fixture_inputs(case)
            row: dict[str, Any] = {
                "page": case["page"],
                "case": case["name"],
                "model": model,
                "expected": case["expected"],
            }
            output["results"].append(row)
            persist = lambda: save(output) if save else None
            metrics = {"provider": provider, "model": model, "attempts": []}
            row["generation"] = metrics
            persist()
            if not automation.evidence_available(sources):
                observed = "unavailable-evidence"
            else:
                if budget:
                    prompt = automation.build_prompt(
                        {"page": case["page"]}, case["original"], sources
                    )
                    try:
                        raw = generate(
                            prompt,
                            lambda **kwargs: automation.chat_completion_request(
                                prompt, token, model, provider, **kwargs
                            ),
                            lambda text: json.loads(automation.strip_json_fence(text)),
                            budget,
                            metrics,
                            persist,
                            time.monotonic(),
                        )
                    except GenerationFailure as exc:
                        row["error"] = exc.error
                        observed = "generation-failure"
                try:
                    if "error" not in row:
                        result, observed = automation.assess_response(
                            raw, case["original"], sources
                        )
                        row["decision"] = result
                except (ValueError, TypeError):
                    observed = "validation-refusal"
            row.update(observed=observed, passed=observed == case["expected"])
            persist()
    by_model = {}
    for model in models or ["recorded-response"]:
        rows = [row for row in output["results"] if row["model"] == model]
        attempts = [
            attempt for row in rows for attempt in row["generation"]["attempts"]
        ]
        reported_tokens = [
            (attempt.get("usage") or {}).get("total_tokens") for attempt in attempts
        ]
        by_model[model] = {
            "passed": sum(row["passed"] for row in rows),
            "total": len(rows),
            "requests": sum(len(row["generation"]["attempts"]) for row in rows),
            "reported_total_tokens": (
                sum(value for value in reported_tokens if value is not None)
                if not attempts or any(value is not None for value in reported_tokens)
                else None
            ),
            "usage_is_complete": all(
                (attempt.get("usage") or {}).get("total_tokens") is not None
                for row in rows
                for attempt in row["generation"]["attempts"]
            ),
        }
    output["summary"] = by_model
    persist()
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--live",
        action="store_true",
        help="Explicitly allow paid model calls; never publishes",
    )
    parser.add_argument(
        "--provider",
        choices=("openai", "openrouter", "github-models"),
        default="openai",
    )
    parser.add_argument(
        "--model",
        action="append",
        help="Required for live mode; repeat to compare models",
    )
    parser.add_argument("--max-cases", type=int, default=3)
    parser.add_argument("--max-requests", type=int)
    parser.add_argument("--max-output-tokens", type=int)
    parser.add_argument("--run-timeout", type=float)
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding="utf-8"))["cases"]
    if args.output and args.output.exists():
        parser.error("Evaluation output already exists; choose a new output path")
    budget = None
    token = ""
    if args.live:
        if (
            not args.model
            or not args.output
            or args.max_requests is None
            or args.max_output_tokens is None
            or args.run_timeout is None
        ):
            parser.error(
                "--live requires --model, --output, --max-requests, --max-output-tokens and --run-timeout"
            )
        if args.max_cases <= 0:
            parser.error("max-cases must be positive")
        try:
            budget = Budget(
                Limits(
                    max_attempts=1,
                    max_requests=args.max_requests,
                    max_output_tokens=args.max_output_tokens,
                    run_timeout=args.run_timeout,
                )
            )
        except ValueError as exc:
            parser.error(str(exc))
        token = {
            "openai": os.environ.get("OPENAI_API_KEY"),
            "openrouter": os.environ.get("OPENROUTER_API_KEY"),
            "github-models": os.environ.get("GITHUB_TOKEN")
            or os.environ.get("GH_TOKEN"),
        }[args.provider] or ""
        if not token:
            parser.error("Live evaluation requires selected provider's token")
        cases = [case for case in cases if case.get("live")][: args.max_cases]
    elif args.model:
        parser.error("--model requires explicit --live mode")
    if args.output:
        with Checkpoint(args.output) as checkpoint:
            if args.output.exists():
                parser.error(
                    "Evaluation output already exists; choose a new output path"
                )
            output = evaluate(
                cases,
                provider=args.provider if budget else "fixture",
                models=args.model,
                token=token,
                budget=budget,
                save=checkpoint.save,
            )
    else:
        output = evaluate(cases)
    print(
        json.dumps(
            {
                "mode": output["mode"],
                "summary": output["summary"],
                "scope": output["scope"],
            },
            indent=2,
        )
    )
    return 0 if all(row["passed"] for row in output["results"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
