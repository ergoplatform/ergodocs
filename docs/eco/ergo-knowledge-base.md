---
tags:
  - Knowledge Base
  - Transcripts
  - Documentation
  - Community
owner: docs
last_reviewed: 2026-05-30
source_repos:
  - repo: cannonQ/ergo-transcripts
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/cannonQ/ergo-transcripts
  - https://ergo-transcripts.vercel.app/
  - https://ergo-transcripts.vercel.app/mcp
---

# Ergo Knowledge Base and Transcripts

## Overview

Ergo Knowledge Base and Ergo Transcripts make Ergo community knowledge searchable and machine-readable. The public transcripts site indexes long-form ecosystem material such as community calls, AMAs, technical discussions, conference talks, and chat exports.

## Recent updates

- `Jan 28`: Ergo Knowledge Base work started to transcribe videos and spaces into searchable knowledge.
- `Feb 4`: Ergo Transcripts added 37 more calls and reached 58+ hours of indexed content.
- `Feb 11`: another 50 calls brought the archive to 88+ hours, with Twitter Spaces and Reddit AMA workflows planned.
- `Mar 6`: Telegram general/developer channel exports were archived by week/month, producing 153 monthly summaries and 556 weekly segments.

## Ergo Transcripts

[Ergo Transcripts](https://ergo-transcripts.vercel.app/) indexes calls, Twitter Spaces, AMAs, technical discussions, and conference talks. Source is available at [cannonQ/ergo-transcripts](https://github.com/cannonQ/ergo-transcripts).

The project turns long-form ecosystem material into searchable text for humans and structured context for agents. Current work includes fuzzy search, decision and commitment tracking, speaker/topic browsing, Telegram/forum/blog ingestion, correction workflows, and an MCP endpoint for tool use.

- The transcripts MCP is available at [ergo-transcripts.vercel.app/mcp](https://ergo-transcripts.vercel.app/mcp).
- The repository describes the archive as transcript coverage for Ergo Platform videos, community chats, and related ecosystem material.
- The README describes MCP tools for semantic conversation search, full video summaries, Telegram summaries, forum-topic retrieval, cross-source timelines, and content browsing.

## Ergo Knowledge Base

[Ergo Knowledge Base](https://ergo-knowledge-base.vercel.app/) is a related public knowledge interface for curated summaries and project context.

Ergo Knowledge Base transcribes and organizes ecosystem videos, community calls, AMAs, technical discussions, Telegram exports, and public ErgoScript contract summaries.

Planned work includes:

- Reddit AMA and Twitter Spaces ingestion workflows.
- KPI/dashboard views for tracking content coverage.
- Public contract summaries and project-context pages for reuse by docs, agents, and contributors.

## Ergo Book

The Ergo Book effort was converted to mdBook in February 2026. It organizes the ideological, philosophical, and technical foundation of the Ergo movement. A Reddit AMA with contributors was also planned around the book structure.
