---
tags:
  - Node
  - Rust
  - Infrastructure
  - Experimental
owner: docs
last_reviewed: 2026-06-08
source_repos:
  - repo: mwaddip/ergo-node-rust
    branch: master
    paths:
      - README.md
  - repo: Luivatra/ergo-rust-node
    branch: main
    paths:
      - README.md
  - repo: odiseusme/ergo-rust-sync-dashboard
    branch: main
    paths:
      - README.md
  - repo: mwaddip/santa
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/mwaddip/ergo-node-rust
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.9
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.8
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.7
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.6
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.4
  - https://github.com/Luivatra/ergo-rust-node
  - https://github.com/odiseusme/ergo-rust-sync-dashboard
  - https://github.com/mwaddip/santa
---

# Ergo Rust Node

## Overview

[Ergo Rust Node](https://github.com/mwaddip/ergo-node-rust) is an experimental Rust implementation of an Ergo node. It is not the reference client; use the Scala [Ergo reference client](install.md) for production unless a release explicitly says otherwise.

## Current State

The project has moved beyond early header-sync testing into API compatibility, indexer, pruning, and validation-harness work. It remains experimental, but recent releases show active alignment with the JVM node API surface.

Related Rust-node references include [Luivatra/ergo-rust-node](https://github.com/Luivatra/ergo-rust-node), an earlier experimental implementation, and [ergo-rust-sync-dashboard](https://github.com/odiseusme/ergo-rust-sync-dashboard), a small Tkinter sync display for `mwaddip/ergo-node-rust`.

[SANTA](https://github.com/mwaddip/santa) is a related cross-implementation conformance suite for Ergo consensus behavior. It keeps shared test vectors and runner contracts so independent implementations can compare wire, evaluation, transaction, block, and chain behavior against canonical expected outputs.

Recent release highlights:

- [v0.6.9](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.9) added consensus-behavior fixes from sigma-rust for mixed-width numeric arithmetic and rejection of flat N-ary tuples during deserialization.
- [v0.6.8](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.8) tightened JIT cost accounting for empty and packed collections and added an indexer health endpoint at `/api/v1/health`.
- [v0.6.7](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.7) addressed validation-harness gridlock by moving heavy API work to blocking threads, adding single-flight block-transaction fetching in the indexer, and relaxing bogus peer-address handling so normal NAT gossip is filtered without banning the gossiper.
- [v0.6.6](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.6) aligned several REST responses with the JVM node, including `/peers/connected`, `/mining/rewardAddress`, and error response shapes. It also fixed an indexer reorg-detection blind spot that could surface as duplicate transaction IDs during mid-sync reorgs.
- [v0.6.4](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.4) added `blocks_to_keep` pruning for non-header block sections, plus validation-oriented endpoints for canonical block fragments and indexed box bytes.
- Earlier `v0.4.x` work reduced at-tip memory use and exposed peer-request behavior that could trigger bans when malformed or repeated requests were sent.

Current development areas include mining endpoint support, NiPoPoW bootstrapping, RequestModifiers serving, mempool/API work, peer penalties, indexer behavior, API parity, and validation against JVM behavior.

## Implementation notes

- Mainnet validation work exposed sigma-rust edge cases around context-extension ordering, v6 opcode parsing, JIT costing, lazy constant resolution, and pre-JIT compatibility paths.
- The peer-penalty system was designed to integrate with `fail2ban`, but repeated or malformed request behavior still needed tuning during April testing.
- Memory work focused on reducing database cache pressure after the node reaches tip. The `v0.4.0` release reopened the runtime AVL state database with a smaller redb cache once chain sync completed.
- NiPoPoW work included bootstrapping and proof-serving gaps. One noted difference was that the sigma-rust `NipopowProof` structure lacked a `continuous` field present in the JVM node.
- Use the Rust node for testing, differential validation, and implementation research unless release notes explicitly mark a version as production-ready.
