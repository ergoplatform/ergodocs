---
title: Matrix Pulse
description: Lightweight live monitor for Ergo Matrix input-block activity.
tags:
  - ecosystem
  - tooling
  - monitoring
  - node
owner: docs
last_reviewed: 2026-06-30
source_repos:
  - repo: odiseusme/matrix-pulse
    branch: master
    paths:
      - README.md
source_of_truth:
  - https://github.com/odiseusme/matrix-pulse
---

# Matrix Pulse

[Matrix Pulse](https://github.com/odiseusme/matrix-pulse) is a lightweight live monitor for Ergo Matrix input-block activity. It tails an Ergo Matrix node's systemd journal, parses input-block lifecycle events, and streams a browser view over Server-Sent Events.

## What It Shows

The repository describes a compact status and activity view for:

- node version, network, name, height, sync state, peers, mempool, and mining status from `/info`;
- Matrix sub-blocks per block, current input-block tip, competing forks, best fork depth, and difficulty;
- sub-block arrivals, applied input-block transactions, disconnected-queue churn, fork switches, rollups, frame counts, and gap/stale detection.

## Operator Notes

Matrix Pulse is intentionally small: Python standard library only, no external Python dependencies, and loopback-only by default. The README says the SSE server binds to `127.0.0.1`, exposes only the page and event stream, reads the node journal and `/info`, and does not write to the node.

Use it as operator/debugging tooling for Matrix DevNet-style testing, not as consensus evidence or a production monitoring guarantee.

## Links

- [Repository](https://github.com/odiseusme/matrix-pulse)
- [Rust Node and SANTA](rust-node.md)
- [Matrix DevNet](devnetconf.md)
