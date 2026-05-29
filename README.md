<div align="center">

# ErgoDocs

**The public documentation site for the Ergo Platform.**

[![Docs](https://img.shields.io/badge/docs-docs.ergoplatform.com-red?style=for-the-badge)](https://docs.ergoplatform.com/)
[![Docs quality](https://img.shields.io/github/actions/workflow/status/ergoplatform/ergodocs/docs-quality.yml?branch=main&label=docs%20quality&style=for-the-badge)](https://github.com/ergoplatform/ergodocs/actions/workflows/docs-quality.yml)
[![Deploy](https://img.shields.io/github/actions/workflow/status/ergoplatform/ergodocs/ci.yml?branch=main&label=deploy&style=for-the-badge)](https://github.com/ergoplatform/ergodocs/actions/workflows/ci.yml)
[![Source Watch](https://img.shields.io/github/actions/workflow/status/ergoplatform/ergodocs/source-watch.yml?branch=main&label=source%20watch&style=for-the-badge)](https://github.com/ergoplatform/ergodocs/actions/workflows/source-watch.yml)

[Visit the docs](https://docs.ergoplatform.com/) ·
[Contribute](docs/contribute/docs.md) ·
[Automation](docs/contribute/automation.md) ·
[Source Watch](docs/contribute/source-watch.md) ·
[Maintainer Start Here](docs/start_here.md)

</div>

---

ErgoDocs is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and maintained as a docs-as-code project. Content, navigation, review tooling, source monitoring, and deployment configuration live together so documentation changes can be reviewed and shipped with the same discipline as product code.

## What Lives Here

| Path | Purpose |
| --- | --- |
| [`docs/`](docs/) | Public Markdown documentation and maintainer guides. |
| [`mkdocs.yml`](mkdocs.yml) | Site configuration, navigation, theme settings, plugins, and hooks. |
| [`tools/`](tools/) | Audits, Source Watch, Discord lead review, prompts, and maintenance helpers. |
| [`overrides/`](overrides/) | MkDocs Material theme overrides used by the live site. |
| [`.github/workflows/`](.github/workflows/) | Quality checks, source scans, weekly docs leads, and deployment. |

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

## Common Tasks

| Task | Start here |
| --- | --- |
| Make a docs edit | [Contributing to the Documentation](docs/contribute/docs.md) |
| Understand docs standards | [Content Standards](docs/contribute/content-standards.md) |
| Add, move, or reorganize pages | [Information Architecture](docs/contribute/information-architecture.md) |
| Keep source-backed pages current | [Source Watch](docs/contribute/source-watch.md) |
| Run the weekly review workflow manually | [Source Watch Playbook](docs/contribute/source-watch-playbook.md) |
| Understand checks and automation | [Documentation Automation](docs/contribute/automation.md) |
| Maintain repo tooling | [Documentation Tools](docs/contribute/tools.md) |

## Quality Checks

For normal docs or tooling changes, run:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

These checks validate source metadata, navigation coverage, section structure, whitespace, and the final MkDocs build.

## Source-Linked Docs

Pages that describe active software, APIs, contracts, configs, EIPs, or ecosystem projects can declare upstream sources in frontmatter. Source Watch compares those pages against watched GitHub paths and helps maintainers decide what needs review.

```bash
GITHUB_TOKEN=... .venv/bin/python tools/source_watch.py scan \
  --github \
  --new-only \
  --repo ergoplatform/ergo \
  --max-queries 120 \
  --no-fail-on-changes \
  --format markdown \
  --output /tmp/source-watch-ergo.md
```

Discord and chat exports are leads only. Public docs should be updated from durable sources such as repositories, issues, releases, EIPs, or maintainer-confirmed references.

## Automation

ErgoDocs uses GitHub Actions for:

- pull-request builds and audits
- weekly Source Watch scans
- weekly docs review packages combining Discord leads and a full watched-source scan
- optional AI-assisted draft PR creation from Source Watch candidates
- main-branch deployment to the live site

The weekly docs workflow does two separate checks: it exports recent Discord discussion for review leads, and it scans all source-linked docs repositories for watched changes even when those repos were not mentioned in Discord that week. Manual runs can use `full`, `discord-only`, or `source-only` mode. The workflow labels tracking and per-page issues, writes a run summary, closes stale weekly tracking issues, and opens per-page review issues only when a source-linked page may need attention. If everything is already reviewed or low-signal, it comments on the tracking issue and closes it automatically.

The AI draft PR workflow is manual. It uses GitHub Models to propose draft documentation PRs from Source Watch candidates, labels them for human review, and never auto-merges. Configure `DOCS_BOT_TOKEN` if those generated PRs should trigger normal pull request workflows.

Read the full overview in [Documentation Automation](docs/contribute/automation.md).

## Contributing

Good documentation changes are:

- focused: one topic or workflow per change where practical
- sourced: technical claims point to durable references
- connected: pages are reachable through navigation and linked from relevant nearby pages
- readable: written as public documentation, not as internal review notes
- checked: commands, links, examples, and affected pages were verified

Use pull requests for documentation and tooling changes. If you are unsure where a change belongs, start with [Contributing to the Documentation](docs/contribute/docs.md).

## Deployment

Pull requests touching docs or tooling run the docs quality workflow. Main branch deploys through [Deploy and verify live site](https://github.com/ergoplatform/ergodocs/actions/workflows/ci.yml).

The deploy workflow syncs the checked-out repository to the server and builds on Linux, so only committed files are deployed and path casing matters.

## Repository Hygiene

Do not commit generated output, secrets, local caches, virtualenvs, or scan state:

- `site/`
- `.venv/`
- `.env`
- `__pycache__/`
- `.DS_Store`
- `tools/state/`
- `tools/discord_dev_digest/state/`
