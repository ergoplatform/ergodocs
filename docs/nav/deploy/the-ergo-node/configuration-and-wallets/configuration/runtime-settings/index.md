---
tags:
  - deploy
  - runtime-settings
  - navigation
owner: docs
last_reviewed: '2026-05-31'
---

# Runtime Settings

Runtime Settings groups related pages inside Deploy. Runtime, cache, mailbox, Akka, Scorex, and dispatcher settings.

The table links to the next useful page or sub-hub, keeping the sidebar staged instead of fully expanded.

## Map

| Page | What you'll find |
| --- | --- |
| [Cache Settings](conf-cache.md) | The cache configuration specifies what data to keep in memory to optimize the performance of the system. |
| [Bounded Mailbox](conf-bounded.md) | The bounded-mailbox configuration specifies the settings for the bounded mailbox type, which limits the maximum number of messages that can be stored in an actor's mailbo... |
| [Akka](conf-akka.md) | The akka configuration settings manage how the application uses the Akka framework, which handles concurrency and actor-based programming in the system. |
| [Scorex](conf-scorex.md) | The scorex.network section allows you to configure settings related to the P2P network. |
| [Critical Dispatcher](conf-crit.md) | The critical-dispatcher is a dedicated actor dispatcher, utilized exclusively by the block candidate generator and NodeViewHolder actors within the system. |
| [API Dispatcher](conf-api.md) | The api-dispatcher configuration controls the dispatcher responsible for managing API-related actors. |
