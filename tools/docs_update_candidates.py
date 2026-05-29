#!/usr/bin/env python3
"""Build page-aware documentation update candidates from Source Watch reports."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


NOISE_RE = re.compile(
    r"\b("
    r"refactor|cleanup|clean up|format|formatting|typo|test|tests|testing|spec test|ci|"
    r"chore|merge|bump|dependency|dependencies|candidate for .*release|release candidate|"
    r"case-class wrappers|case class wrappers|compiler helper"
    r")\b",
    re.IGNORECASE,
)
DOC_SIGNAL_RE = re.compile(
    r"\b("
    r"add|added|support|supports|enable|enabled|implement|implemented|introduce|introduced|"
    r"new|remove|removed|deprecate|deprecated|rename|renamed|change|changed|update|updated|"
    r"endpoint|api|swagger|openapi|config|configuration|parameter|option|setting|wallet|"
    r"address|transaction|token|contract|oracle|miner|mining|release|upgrade|migration|"
    r"breaking|security|protocol|feature|mode|command|sdk"
    r")\b",
    re.IGNORECASE,
)
GENERIC_TOKENS = {
    "docs",
    "doc",
    "dev",
    "eco",
    "uses",
    "node",
    "ergo",
    "ergoplatform",
    "src",
    "main",
    "scala",
    "rs",
    "js",
    "ts",
    "md",
    "readme",
    "release",
    "pr",
}
USER_FACING_RE = re.compile(
    r"\b("
    r"endpoint|api|swagger|openapi|config|configuration|parameter|option|setting|wallet scan|"
    r"getblocktemplate|primitive|syntax|language|ergoscript|sdk|release|migration|breaking|"
    r"security|protocol|command|address|transaction signing|sign endpoint|check endpoint"
    r")\b",
    re.IGNORECASE,
)
SYNONYMS = {
    "swagger": {"api", "endpoint", "openapi"},
    "openapi": {"api", "endpoint", "swagger"},
    "wallet": {"wif", "address", "sign", "mnemonic", "scan"},
    "mining": {"miner", "pool", "stratum", "getblocktemplate"},
    "sigmastate": {"sigma", "ergoscript", "compiler", "sdk"},
    "interpreter": {"sigma", "ergoscript", "compiler", "sdk"},
    "sigma": {"sigmastate", "ergoscript", "compiler", "sdk"},
    "oracles": {"oracle"},
    "oracle": {"oracles"},
}


@dataclass
class Candidate:
    page: dict[str, Any]
    page_path: str
    subject: str
    title: str
    changes: list[dict[str, Any]]
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "page": self.page_path,
            "subject": self.subject,
            "title": self.title,
            "reason": self.reason,
            "changes": self.changes,
        }


def page_changes(page: dict[str, Any]) -> list[dict[str, Any]]:
    return [change for change in page.get("changes", []) if isinstance(change, dict)]


def change_date(change: dict[str, Any]) -> datetime | None:
    raw = str(change.get("date", ""))
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def reviewed_date(page: dict[str, Any]) -> datetime | None:
    raw = str(page.get("last_reviewed", ""))
    if not raw or raw.lower() == "never":
        return None
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def latest_change_date(changes: list[dict[str, Any]]) -> datetime | None:
    dates = [date for date in (change_date(change) for change in changes) if date is not None]
    return max(dates) if dates else None


def already_reviewed(page: dict[str, Any]) -> bool:
    reviewed = reviewed_date(page)
    latest = latest_change_date(page_changes(page))
    if reviewed is None or latest is None:
        return False
    return reviewed.date() >= latest.date()


def low_only(changes: list[dict[str, Any]]) -> bool:
    return bool(changes) and all(str(change.get("severity", "")) == "low" for change in changes)


def words(value: str) -> set[str]:
    return {part.lower() for part in re.findall(r"[A-Za-z][A-Za-z0-9]{2,}", value)}


def meaningful(tokens: set[str]) -> set[str]:
    return {token for token in tokens if token not in GENERIC_TOKENS}


def expand_tokens(tokens: set[str]) -> set[str]:
    expanded = set(tokens)
    for token in tokens:
        expanded.update(SYNONYMS.get(token, set()))
    return expanded


def page_tokens(page: dict[str, Any]) -> set[str]:
    path = str(page.get("page", ""))
    tokens = meaningful(words(path.replace("/", " ").replace("-", " ").replace("_", " ")))
    return expand_tokens(tokens)


def message_tokens(change: dict[str, Any]) -> set[str]:
    message = str(change.get("message", ""))
    tokens = meaningful(words(message.replace("/", " ").replace("-", " ").replace("_", " ")))
    return expand_tokens(tokens)


def source_tokens(change: dict[str, Any]) -> set[str]:
    text = " ".join([str(change.get("message", "")), str(change.get("path", "")), str(change.get("repo", ""))])
    tokens = meaningful(words(text.replace("/", " ").replace("-", " ").replace("_", " ")))
    return expand_tokens(tokens)


def issue_subject(changes: list[dict[str, Any]]) -> str:
    for change in changes:
        message = str(change.get("message", "")).strip()
        message = re.sub(r"^PR #\d+:\s*", "", message)
        message = re.sub(r"^Release [^:]+:\s*", "", message)
        message = re.sub(
            r"^(add|added|support|supports|enable|enabled|implement|implemented|introduce|introduced|update|updated)\s+",
            "",
            message,
            flags=re.IGNORECASE,
        )
        message = message.rstrip(".")
        if message:
            return message[:90]
    return "source-backed documentation update"


def page_text(page_path: str) -> str:
    path = ROOT / page_path
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def already_covered(page_path: str, subject: str) -> bool:
    text = page_text(page_path).lower()
    if not text:
        return False
    normalized = re.sub(r"\s+", " ", subject.lower()).strip()
    if normalized and normalized in text:
        return True
    terms = meaningful(words(subject))
    important = [term for term in terms if len(term) >= 4]
    if len(important) < 3:
        return False
    return sum(1 for term in important if term in text) >= min(len(important), 4)


def actionable_change(page: dict[str, Any], change: dict[str, Any]) -> bool:
    message = str(change.get("message", ""))
    kind = str(change.get("kind", ""))
    severity = str(change.get("severity", ""))
    msg_overlap = page_tokens(page) & message_tokens(change)

    if severity == "low":
        return False
    if re.search(r"\bprimitive wallet messages\b|\bcase-class wrappers\b|\bcase class wrappers\b", message, re.IGNORECASE):
        return False
    if re.search(r"\bcandidate for .*release\b|\brelease candidate\b", message, re.IGNORECASE):
        return False
    if not DOC_SIGNAL_RE.search(message):
        return False
    if NOISE_RE.search(message) and not USER_FACING_RE.search(message):
        return False
    if "/test/" in str(change.get("path", "")) and not USER_FACING_RE.search(message):
        return False
    if kind == "release":
        return bool(msg_overlap) and "release" in words(message)
    if NOISE_RE.search(message) and not msg_overlap:
        return False
    return bool(msg_overlap)


def unique_changes(changes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    for change in changes:
        key = (str(change.get("repo", "")), str(change.get("sha", "")))
        entry = grouped.setdefault(key, {**change, "paths": []})
        path = str(change.get("path", ""))
        if path and path not in entry["paths"]:
            entry["paths"].append(path)
    return sorted(grouped.values(), key=lambda item: (item.get("date", ""), item.get("repo", ""), item.get("sha", "")))


def build_candidates(
    report: dict[str, Any],
    *,
    include_reviewed: bool = False,
    include_low_only: bool = False,
    include_not_actionable: bool = False,
    skip_covered: bool = True,
) -> tuple[list[Candidate], list[dict[str, str]]]:
    candidates: list[Candidate] = []
    skipped: list[dict[str, str]] = []
    for page in report.get("pages", []):
        page_path = str(page.get("page", ""))
        changes = page_changes(page)
        if not page_path or not changes:
            continue
        base_title = f"Docs review needed: {page_path}"
        if already_reviewed(page) and not include_reviewed:
            skipped.append({"title": base_title, "action": "skipped-reviewed", "url": ""})
            continue
        if low_only(changes) and not include_low_only:
            skipped.append({"title": base_title, "action": "skipped-low-only", "url": ""})
            continue

        filtered = [change for change in changes if actionable_change(page, change)]
        if not filtered and not include_not_actionable:
            skipped.append({"title": base_title, "action": "skipped-not-actionable", "url": ""})
            continue
        candidate_changes = unique_changes(filtered or changes)
        subject = issue_subject(candidate_changes)
        if skip_covered and already_covered(page_path, subject):
            skipped.append({"title": f"Add info on {subject}: {page_path}", "action": "skipped-covered", "url": ""})
            continue

        candidates.append(
            Candidate(
                page=page,
                page_path=page_path,
                subject=subject,
                title=f"Add info on {subject}: {page_path}",
                changes=candidate_changes,
                reason="source change appears relevant to this page and is not already obvious in the page text",
            )
        )
    return candidates, skipped
