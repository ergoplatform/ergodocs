#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -x ".venv/bin/python" ]; then
  if command -v python3 >/dev/null 2>&1; then
    python3 -m venv .venv
  else
    python -m venv .venv
  fi
fi

PIP_CACHE_DIR="${PIP_CACHE_DIR:-$PWD/.venv/pip-cache}" \
  ".venv/bin/python" -m pip install --quiet --disable-pip-version-check -r requirements.txt

if [ -f ".env" ]; then
  set -a
  source ".env"
  set +a
fi

exec ".venv/bin/python" -m mkdocs serve "$@"
