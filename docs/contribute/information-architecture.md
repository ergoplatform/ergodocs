---
owner: docs
last_reviewed: 2026-05-27
---

# Information Architecture

ErgoDocs has grown from topic pages, ecosystem notes, tutorials, protocol references, and generated API material. That growth is useful, but the repository now needs clearer ownership boundaries so navigation does not become the content model.

## Target Model

Use one canonical home for each page. Other sections should link to that page through curated hub pages, not duplicate the same file in multiple top-level nav surfaces.

| Surface | Job | Canonical content |
| --- | --- | --- |
| Start Here | orientation and first decisions | short guides, glossary, FAQ |
| Use | user jobs and ecosystem use cases | wallets, dApps, tutorials, project pages |
| Learn | concepts and research | protocol concepts, papers, cryptography, scaling |
| Participate | community and contribution | governance, events, docs process, funding |
| Develop | builder references | SDKs, ErgoScript, data model, APIs, examples |
| Deploy | operator runbooks | node, indexers, watchers, pools, infrastructure |

## Current Structural Risks

Run:

```bash
.venv/bin/python tools/structure_audit.py --markdown
```

The audit tracks active docs, nav entries, duplicate targets, cross-surface duplicates, orphans, maximum nav depth, and source-watch coverage by content area.

Current repo shape shows three main risks:

- Same page appears in several top-level surfaces, for example Rosen watcher pages under both `Use` and `Deploy`, and some SDK/tooling pages under multiple developer sections.
- Project pages, conceptual pages, and operational runbooks are mixed in the same folders, especially under `eco/`, `uses/`, and `dev/stack/`.
- Some pages exist as navigation bridges rather than canonical references, making source ownership and update responsibility less clear.

After the second navigation cleanup pass, the audit reports:

- `646` active markdown pages.
- `647` nav entries pointing at `647` unique targets.
- `0` duplicate nav targets, down from `32`.
- `0` cross-surface duplicates, down from `27`.
- `0` active orphan pages outside the nav.
- `1` intentional unlisted legacy page.
- `137` source-watched pages.

## Rules

- A page should have one canonical nav location.
- A page can appear in another journey only through a hub page with a short summary and link.
- `Use` pages should explain user outcomes and risks, not implementation details.
- `Develop` pages should document APIs, libraries, contracts, and source-backed behavior.
- `Deploy` pages should be runbooks: prerequisites, config, operations, failure modes, upgrades.
- `Learn` pages should be stable conceptual references and should not depend on live project status.
- Ecosystem project pages should declare status: active, dormant, prototype, historical, or unknown.
- Source-backed pages should carry `owner`, `last_reviewed`, and `source_repos` frontmatter.
- Replaced, alias, or draft pages should declare `ia_status: legacy`, `ia_status: alias`, or `ia_status: draft` instead of silently becoming orphan debt.

## Migration Plan

1. Pick canonical homes for cross-surface duplicates.
2. Replace duplicate nav entries with hub links.
3. Split mixed pages when they combine concept, runbook, and project status.
4. Move dormant or historical ecosystem pages into a clearly labelled archive path only after redirects exist.
5. Add source-watch metadata to pages that describe changing APIs, contracts, configs, or active repositories.
6. Keep generated API docs separate from authored API guidance.

## High-Value Restructure Candidates

- Rosen watcher docs: canonical home is now `Deploy / Watchers`; `Use / Rosen Bridge` keeps user-facing Rosen concepts and no longer duplicates watcher runbooks.
- Blockchain indexing docs: canonical home is now `Deploy / Blockchain Indexing`; `Develop` keeps API and explorer references without duplicating indexing runbooks.
- Mosaik and legacy frameworks: split active SDK guidance from historical examples.
- Ecosystem directory: continue adding status taxonomy; navigation now separates user/project pages from operator and developer runbooks.
- Node docs: keep generated OpenAPI under `node/swagger/`; keep authored guidance in `node/swagger.md` and `dev/integration/`.
- Remaining work should focus on page quality inside overlarge buckets, especially `Use / Ecosystem / Applications & Utilities`, `Develop / Tooling & Frameworks`, and node operations.

## Review Checklist

- Does this page have one canonical audience?
- Is this page in only one top-level nav surface?
- Does changing source code or config affect this page?
- Is project status explicit?
- Could this page be a hub link instead of a duplicated nav target?
- Would a new contributor know who owns updates?
