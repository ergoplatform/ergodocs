#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
  echo "Missing .venv. Create it with: python -m venv .venv && .venv/bin/python -m pip install -r requirements.txt" >&2
  exit 1
fi

source ".venv/bin/activate"

if [ -f ".env" ]; then
  set -a
  source ".env"
  set +a
fi

mkdocs serve
