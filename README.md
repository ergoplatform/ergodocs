# ErgoDocs

[ErgoDocs](https://docs.ergoplatform.com/) is the public documentation site for
the Ergo Platform. It is built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and maintained as
a docs-as-code project: content, navigation, review tooling, and deployment
configuration live in one repository so changes can be reviewed and shipped with
the same discipline as product code.

Use this README for local setup and contributor orientation. Maintainers should
also read [`docs/start_here.md`](docs/start_here.md).

## Quick Start

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
./run.sh
```

Then open the local MkDocs URL printed by `mkdocs serve`.

Build once without serving:

```bash
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

## What This Repo Contains

- `docs/`: published Markdown documentation and maintainer guides.
- `mkdocs.yml`: site configuration, navigation, theme options, plugins, and hooks.
- `tools/`: documentation audits, source-watch tooling, review prompts, and helpers.
- `overrides/`: MkDocs Material theme overrides used by `mkdocs.yml`.
- `.github/workflows/`: build, audit, source-watch, and deploy workflows.

## Common Workflows

| Task | Start here |
| --- | --- |
| Make a content change | Edit the relevant file under `docs/`, then run the checks below. |
| Add or move a page | Update `mkdocs.yml`, add cross-links from related pages, then run nav and structure audits. |
| Update source-backed docs | Check upstream repos first, update the page naturally, then validate `source_repos`. |
| Review site structure | Use [`docs/contribute/information-architecture.md`](docs/contribute/information-architecture.md). |
| Maintain tooling | Use [`docs/contribute/tools.md`](docs/contribute/tools.md). |
| Run a source-watch pass | Use [`docs/contribute/source-watch-playbook.md`](docs/contribute/source-watch-playbook.md). |

## Local Development

Use the repository virtualenv. Do not rely on a global MkDocs install.

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Preview the site:

```bash
./run.sh
```

Or run MkDocs directly through the repo environment:

```bash
.venv/bin/mkdocs serve
```

Build the static site:

```bash
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

## Definition of Done

A docs change is not complete until the affected page reads naturally, links to
nearby relevant pages, and passes the narrowest relevant checks.

For normal docs or tooling changes, run:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

- `source_watch.py`: validates source-linked page metadata.
- `nav_audit.py`: catches missing nav targets, duplicate nav entries, and orphan docs.
- `structure_audit.py`: checks section structure, nav coverage, duplicate surfaces, and source-watch coverage.
- `git diff --check`: catches whitespace errors before commit.
- `mkdocs build`: verifies the site renders.

If you changed only copy on an unsourced page, a full source-watch run may be
unnecessary. If you changed navigation, run both nav audits and a build.

## Contributing

Use pull requests for documentation and tooling changes.

Good docs changes are:

- focused: one topic or workflow per change where possible.
- sourced: behavior claims point to durable repositories, issues, releases, EIPs, or maintainer-confirmed references.
- connected: new pages link from relevant existing pages and are reachable through navigation.
- readable: content is written for users, not as a changelog of how it was discovered.
- checked: commands, links, and examples changed in the PR were verified.

Useful maintainer pages:

- [Contributing to the documentation](docs/contribute/docs.md)
- [Content standards](docs/contribute/content-standards.md)
- [Documentation lifecycle](docs/contribute/docs-lifecycle.md)
- [Information architecture](docs/contribute/information-architecture.md)
- [Documentation tools](docs/contribute/tools.md)
- [Source Watch](docs/contribute/source-watch.md)
- [Source Watch Playbook](docs/contribute/source-watch-playbook.md)

## Source-Linked Documentation

Some pages include `source_repos` frontmatter so maintainers can compare docs
against upstream repositories. Use strict validation after changing source
metadata:

```bash
.venv/bin/python tools/source_watch.py scan --strict
```

For GitHub-backed review runs, provide a token and scope the scan:

```bash
GITHUB_TOKEN=... .venv/bin/python tools/source_watch.py scan --github --new-only --repo ergoplatform/ergo --max-queries 120 --no-fail-on-changes --format markdown --output /tmp/source-watch-ergo.md
```

Discord or chat exports are review leads only. Public docs should be updated
from repositories, issues, releases, EIPs, or maintainer-confirmed sources.

Do not add “scan found this” or internal review notes to public pages. Fold
verified changes into the page in normal documentation prose.

## Deployment

Pull requests touching docs or tooling are checked by
`.github/workflows/docs-quality.yml`. Main-branch deployment is handled by
`.github/workflows/ci.yml`. The manual `tools/deploy.sh` helper is legacy; prefer
GitHub Actions unless a maintainer explicitly asks for manual deployment.

## Repository Hygiene

Do not commit generated site output, local caches, virtualenv files, secrets, or
local scan state. In particular, keep these out of commits:

- `site/`
- `.venv/`
- `.env`
- `__pycache__/`
- `.DS_Store`
- `tools/state/`
- `tools/discord_dev_digest/state/`
