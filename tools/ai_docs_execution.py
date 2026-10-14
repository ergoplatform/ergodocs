"""Bounded generation and atomic checkpoints shared by docs automation/evaluation."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from contextlib import contextmanager
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import signal
import tempfile
import time
from typing import Any, Callable
from urllib.error import HTTPError, URLError


@contextmanager
def request_deadline(seconds: float):
    """Wall-clock bound around HTTP reads, including slowly arriving response bytes.

    CLI runs on the main thread on macOS/Linux, as do the file-lock operations.
    Restore an enclosing timer rather than cancelling someone else's deadline.
    """
    previous_handler = signal.getsignal(signal.SIGALRM)
    previous_timer = signal.getitimer(signal.ITIMER_REAL)
    started = time.monotonic()

    def expired(*_: Any) -> None:
        raise TimeoutError("HTTP request deadline reached")

    signal.signal(signal.SIGALRM, expired)
    signal.setitimer(
        signal.ITIMER_REAL,
        min(seconds, previous_timer[0]) if previous_timer[0] else seconds,
    )
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
        if previous_timer[0]:
            remaining = max(0.000001, previous_timer[0] - (time.monotonic() - started))
            signal.setitimer(signal.ITIMER_REAL, remaining, previous_timer[1])


def fingerprint(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def classified_error(exc: Exception) -> dict[str, Any]:
    """Do not persist provider bodies, credentials, subprocess output or raw URLs."""
    status = exc.code if isinstance(exc, HTTPError) else None
    if status == 429:
        category = "rate-limit"
    elif status in (408, 500, 502, 503, 504):
        category = "transient-http"
    elif status in (401, 403):
        category = "authentication-or-permission"
    elif status is not None:
        category = "http-error"
    elif isinstance(exc, (TimeoutError, subprocess.TimeoutExpired)) or (
        isinstance(exc, URLError) and isinstance(exc.reason, TimeoutError)
    ):
        category = "timeout"
    elif isinstance(exc, (URLError, ConnectionError)):
        category = "network"
    elif isinstance(exc, (ValueError, KeyError, IndexError, TypeError, AttributeError)):
        category = "malformed-response"
    elif isinstance(exc, subprocess.SubprocessError):
        category = "command-failed"
    else:
        category = "internal-error"
    return {
        "category": category,
        "type": type(exc).__name__,
        "http_status": status,
        "retryable": category in {"rate-limit", "transient-http", "timeout", "network"},
    }


@dataclass(frozen=True)
class Limits:
    max_attempts: int = 3
    max_requests: int = 9
    max_output_tokens: int = 12000
    max_prompt_chars: int = 85000
    request_timeout: float = 60
    page_timeout: float = 180
    run_timeout: float = 600

    def validate(self) -> None:
        if any(
            not math.isfinite(value) or value <= 0 for value in asdict(self).values()
        ):
            raise ValueError("Execution limits must be positive")
        if self.max_attempts > 5:
            raise ValueError("max_attempts must be at most 5")


class GenerationFailure(Exception):
    def __init__(self, error: dict[str, Any]):
        super().__init__(error["category"])
        self.error = error


class Budget:
    def __init__(self, limits: Limits):
        limits.validate()
        self.limits = limits
        self.started = time.monotonic()
        self.requests = 0

    def remaining(self) -> float:
        return max(0.0, self.limits.run_timeout - (time.monotonic() - self.started))


def usage_counts(raw: Any) -> dict[str, int] | None:
    if not isinstance(raw, dict):
        return None
    counts = {
        key: value
        for key, value in raw.items()
        if key in {"prompt_tokens", "completion_tokens", "total_tokens"}
        and type(value) is int
        and value >= 0
    }
    return counts or None


def refresh_metrics(metrics: dict[str, Any]) -> None:
    attempts = metrics["attempts"]
    metrics["elapsed_seconds"] = round(
        sum(item.get("elapsed_seconds", 0) for item in attempts)
        + metrics.get("backoff_seconds", 0),
        3,
    )
    counts: dict[str, int] = {}
    for attempt in attempts:
        for key, value in (attempt.get("usage") or {}).items():
            counts[key] = counts.get(key, 0) + value
    metrics["usage"] = counts or None
    metrics["unreported_usage_attempts"] = sum(
        item.get("usage") is None for item in attempts
    )


def generate(
    prompt: str,
    request: Callable[..., dict[str, Any]],
    decode: Callable[[str], dict[str, Any]],
    budget: Budget,
    metrics: dict[str, Any],
    save: Callable[[], None],
    page_started: float,
) -> dict[str, Any]:
    """Retry only transient transport errors; checkpoint before/after every attempt."""
    limits = budget.limits
    attempts = metrics.setdefault("attempts", [])
    while len(attempts) < limits.max_attempts:
        remaining = min(
            budget.remaining(), limits.page_timeout - (time.monotonic() - page_started)
        )
        if (
            len(prompt) > limits.max_prompt_chars
            or remaining <= 0
            or budget.requests >= limits.max_requests
        ):
            raise GenerationFailure({"category": "execution-limit", "retryable": False})
        # In-flight attempts count even if the process dies before receiving a response.
        attempt: dict[str, Any] = {
            "number": len(attempts) + 1,
            "status": "in-flight",
            "usage": None,
            "error": {"category": "interrupted-or-unknown", "retryable": False},
        }
        attempts.append(attempt)
        budget.requests += 1
        refresh_metrics(metrics)
        save()
        started = time.monotonic()
        try:
            envelope = request(
                timeout=min(limits.request_timeout, remaining),
                max_output_tokens=limits.max_output_tokens,
            )
            attempt["usage"] = usage_counts(envelope.get("usage"))
            attempt["response_model"] = envelope.get("model")
            choice = envelope["choices"][0]
            finish = choice.get("finish_reason")
            attempt["finish_reason"] = finish
            message = choice["message"]
            if finish != "stop" or message.get("refusal"):
                category = (
                    "truncated-response" if finish == "length" else "provider-refusal"
                )
                raise GenerationFailure({"category": category, "retryable": False})
            response = decode(message["content"])
            if time.monotonic() - started > remaining:
                raise GenerationFailure(
                    {"category": "execution-limit", "retryable": False}
                )
            attempt.update(status="completed", error=None)
            metrics["response"] = response
            metrics["response_sha256"] = fingerprint(response)
            return response
        except Exception as exc:
            error = (
                exc.error
                if isinstance(exc, GenerationFailure)
                else classified_error(exc)
            )
            attempt.update(status="failed", error=error)
            if not error["retryable"] or len(attempts) >= limits.max_attempts:
                raise GenerationFailure(error) from exc
        finally:
            attempt["elapsed_seconds"] = round(time.monotonic() - started, 3)
            refresh_metrics(metrics)
            save()
        # Backoff is bounded and included in the run/page deadlines.
        delay = min(2 ** (len(attempts) - 1), 8)
        remaining = min(
            budget.remaining(), limits.page_timeout - (time.monotonic() - page_started)
        )
        if delay >= remaining:
            raise GenerationFailure({"category": "execution-limit", "retryable": False})
        sleep_started = time.monotonic()
        try:
            time.sleep(delay)
        finally:
            metrics["backoff_seconds"] = round(
                metrics.get("backoff_seconds", 0) + time.monotonic() - sleep_started, 3
            )
            refresh_metrics(metrics)
            save()
    raise GenerationFailure({"category": "attempt-limit", "retryable": False})


class Checkpoint:
    """Single writer; interruption leaves either the old or the new complete JSON."""

    def __init__(self, path: Path):
        self.path = path.resolve()
        self.lock = None

    def __enter__(self) -> Checkpoint:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.lock = open(str(self.path) + ".lock", "a", encoding="utf-8")
        try:
            fcntl.flock(self.lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self.lock.close()
            raise ValueError("Checkpoint already has an active writer") from None
        return self

    def __exit__(self, *_: Any) -> None:
        if self.lock:
            self.lock.close()

    def read(self) -> dict[str, Any]:
        data = json.loads(self.path.read_text(encoding="utf-8"))
        if (
            not isinstance(data, dict)
            or data.get("schema_version") != 1
            or not isinstance(data.get("results"), list)
        ):
            raise ValueError("Unsupported or corrupt checkpoint; use a new output path")
        if any(
            not isinstance(item, dict) or not isinstance(item.get("page"), str)
            for item in data["results"]
        ):
            raise ValueError("Corrupt checkpoint results")
        return data

    def save(self, data: dict[str, Any]) -> None:
        fd, name = tempfile.mkstemp(prefix=self.path.name + ".", dir=self.path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as stream:
                json.dump(data, stream, indent=2, ensure_ascii=False)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(name, self.path)
            directory = os.open(self.path.parent, os.O_RDONLY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
        finally:
            if os.path.exists(name):
                os.unlink(name)
