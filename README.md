# Ergo Platform documentation

[docs.ergoplatform.com](https://docs.ergoplatform.com/)

ErgoDocs is a docs-as-code site built with MkDocs Material. The repository keeps content, navigation, build tooling, and deployment workflow together so docs changes can be reviewed and shipped like product code.

## Contributing

Please submit a pull request. For larger docs changes, read:

- [Contributing to the documentation](docs/contribute/docs.md)
- [Content standards](docs/contribute/content-standards.md)
- [Documentation lifecycle](docs/contribute/docs-lifecycle.md)

## Running locally

Install required packages

```bash
python -m pip install -r requirements.txt
```

Start local preview:

```bash
mkdocs serve
```

Build static site:

```bash
mkdocs build
```

Audit navigation coverage:

```bash
python tools/nav_audit.py
```

Run AI-assisted docs review prompt:

```bash
cat tools/ai_docs_review_prompt.md
```

Validate source-linked docs metadata:

```bash
python tools/source_watch.py scan --strict
```

Scan selected source repos for possible stale docs:

```bash
GITHUB_TOKEN=... python tools/source_watch.py scan --github --since 2026-01-01 --repo ergoplatform/sigma-rust --max-queries 50
```

JSON report:

```bash
python tools/source_watch.py scan --github --format json --output source-watch.json
```
