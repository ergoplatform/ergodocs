---
tags:
  - Node
  - Rust
  - Infrastructure
  - Experimental
owner: docs
last_reviewed: 2026-08-20
source_repos:
  - repo: mwaddip/ergo-node-rust
    branch: master
    release_watch: true
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
  - repo: mwaddip/santa-blitzen
    branch: master
    paths:
      - README.md
  - repo: mwaddip/santa-vixen
    branch: master
    paths:
      - README.md
  - repo: mwaddip/santa-donner
    branch: main
    paths:
      - README.md
  - repo: arkadianet/ergo
    branch: main
    release_watch: true
    paths:
      - README.md
source_of_truth:
  - https://github.com/mwaddip/ergo-node-rust
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.8.1
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.8.0
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.11
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.10
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.9
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.8
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.7
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.6
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.5
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.4
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.3
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.2
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.1
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.0
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.9
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.8
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.7
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.6
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.4
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.2
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.4.4
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.4.3
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.3.1
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.3.0
  - https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.1.0
  - https://github.com/Luivatra/ergo-rust-node
  - https://github.com/odiseusme/ergo-rust-sync-dashboard
  - https://github.com/mwaddip/santa
  - https://github.com/mwaddip/santa-blitzen
  - https://github.com/mwaddip/santa-vixen
  - https://github.com/mwaddip/santa-donner
  - https://github.com/arkadianet/ergo
  - https://github.com/arkadianet/ergo/releases/tag/v0.5.3
---

# Ergo Rust Node

## Overview

[Ergo Rust Node](https://github.com/mwaddip/ergo-node-rust) is an experimental Rust implementation of an Ergo node. It is not the reference client; use the Scala [Ergo reference client](install.md) for production unless a release explicitly says otherwise.

## Current State

The project has moved beyond early header-sync testing into API compatibility, indexer, pruning, and validation-harness work. It remains experimental, but recent releases show active alignment with the JVM node API surface.

Related Rust-node references include [Luivatra/ergo-rust-node](https://github.com/Luivatra/ergo-rust-node), an earlier experimental implementation, [arkadianet/ergo](https://github.com/arkadianet/ergo), an independent Rust full-node implementation targeting strict consensus parity with the Scala reference, and [ergo-rust-sync-dashboard](https://github.com/odiseusme/ergo-rust-sync-dashboard), a small Tkinter sync display for `mwaddip/ergo-node-rust`.

[SANTA](https://github.com/mwaddip/santa) is a related cross-implementation conformance suite for Ergo consensus behavior. It keeps shared test vectors and runner contracts so independent implementations can compare wire, evaluation, transaction, block, and chain behavior against canonical expected outputs. Related runners include [Blitzen](https://github.com/mwaddip/santa-blitzen) for `sigma-rust`, [Vixen](https://github.com/mwaddip/santa-vixen) for the `arkadianet/ergo` Rust node, and [Donner](https://github.com/mwaddip/santa-donner) for block-tier validation in `mwaddip/ergo-node-rust`.

Recent release highlights:

- [v0.8.1](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.8.1) aligned `CONTEXT.headers` with the reference node's nine preceding headers and allowed missing-parent requests to resume after the unknown-parent request budget had been exhausted.
- [v0.8.0](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.8.0) removed deferred script evaluation, introduced derived memory-budget and split-cache settings, moved Debian configuration into `/etc/ergo-node/conf.d/`, and fixed external-miner candidates, at-tip candidate serving, and mempool admission. UTXO mode now refuses to start below a 3 GiB memory ceiling unless the operator explicitly overrides the floor.
- [v0.7.11](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.11) fixed a reorg header-index overwrite and fast-sync cold-start gap, and added offline state compaction. Operators whose `v0.7.5`–`v0.7.10` index is already clobbered still need a resync.
- [v0.7.10](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.10) stopped unbounded `state.redb` growth; it does not reclaim existing unreachable rows. [v0.7.9](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.9), [v0.7.8](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.8), and [v0.7.7](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.7) fixed P2P frame sizing and several restart/at-tip proof-digest failures.
- [v0.7.6](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.6) fixed an AVL-tree persistence bug that could omit rebalanced internal nodes and later cause resolver-miss panics at the chain tip. The release notes require operators upgrading from an earlier version to delete the node's local `state.redb` and resync because existing state may already be incomplete.
- [v0.7.5](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.5) added the missing proof-digest consensus check after block application, fixed genesis/proof-generation ordering needed for canonical proofs, and decoupled validation sweeps from download progress. The release notes say SANTA isolated a live testnet divergence; this reinforces the node's experimental status.
- [v0.7.4](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.4) fixed a mining-serve state-root mismatch at tip by building a fresh prover from storage rather than sharing mutable prover tree state.
- [v0.7.3](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.3) improved mining-serve JVM compatibility, fixed candidate height handling, rebased the sigma-rust pin, and added further JVM-compatibility fixes around type checking, sized-ErgoTree handling, constant type-code rejection, and block-cost units.
- [v0.7.2](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.2) focused on JVM-exactness in chain validation: header vote-field checks, fork-vote gating, soft-fork vote lifecycle behavior, validation-settings parsing/serialization, rollback error handling, and sigma-rust pin updates.
- [v0.7.1](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.1) and [v0.7.0](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.7.0) continued the same validation/conformance release line.
- [v0.6.9](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.9) added consensus-behavior fixes from sigma-rust for mixed-width numeric arithmetic and rejection of flat N-ary tuples during deserialization.
- [v0.6.8](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.8) tightened JIT cost accounting for empty and packed collections and added an indexer health endpoint at `/api/v1/health`.
- [v0.6.7](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.7) addressed validation-harness gridlock by moving heavy API work to blocking threads, adding single-flight block-transaction fetching in the indexer, and relaxing bogus peer-address handling so normal NAT gossip is filtered without banning the gossiper.
- [v0.6.6](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.6) aligned several REST responses with the JVM node, including `/peers/connected`, `/mining/rewardAddress`, and error response shapes. It also fixed an indexer reorg-detection blind spot that could surface as duplicate transaction IDs during mid-sync reorgs.
- [v0.6.4](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.6.4) added `blocks_to_keep` pruning for non-header block sections, plus validation-oriented endpoints for canonical block fragments and indexed box bytes.
- Earlier `v0.6.2` and `v0.4.x` testing focused on at-tip recovery and storage behavior, including `apply_state` retry / missing-UTXO-key recovery after unclean stops, seed-list fixes for Ubuntu package installs, and reduced at-tip memory use.
- [v0.3.1](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.3.1) unblocked mainnet sync stalls around a voting-epoch boundary and a sigma-rust v6 parse-time type check. [v0.3.0](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.3.0) reduced observed peak RSS during mainnet sync from about `14.95 GB` to about `9.5 GB`.
- [v0.1.0](https://github.com/mwaddip/ergo-node-rust/releases/tag/v0.1.0) was the first public release after early P2P, sync, NiPoPoW, and mining-endpoint work. Treat these early releases as historical implementation milestones, not stable-node recommendations.

The independent [arkadianet/ergo v0.5.3](https://github.com/arkadianet/ergo/releases/tag/v0.5.3) release added configurable mining extension fields and digest-mode ADProofs scheduling, while fixing storage-rent candidate construction, mempool orphan eviction, sync bounds, snapshot authentication, and several consensus-parity issues. It remains pre-1.0 alpha software; verify results against the Scala reference node.

Current development areas include mining endpoint support, NiPoPoW bootstrapping, RequestModifiers serving, mempool/API work, peer penalties, indexer behavior, API parity, and validation against JVM behavior.

## Implementation notes

- Mainnet validation work exposed sigma-rust edge cases around context-extension ordering, v6 opcode parsing, JIT costing, lazy constant resolution, and pre-JIT compatibility paths.
- SANTA and independent `ergots` validation both exposed a sigma-rust under-charging divergence in May 2026. That kind of cross-runner failure is useful evidence for conformance work, but the Scala node remains the consensus authority.
- SANTA's August AuthDS review retired three AVL operations that are unreachable from current ErgoScript/node paths. On the remaining reachable corpus, its JVM and `ergots` runners agreed on all 37 verifier fixtures; this is scoped conformance evidence, not a general production-readiness claim.
- The independent `arkadianet/ergo` node now separates Scala-compatible API documentation at `/swagger` from its native Rust API family at `/swagger/native`.
- The peer-penalty system was designed to integrate with `fail2ban`, but repeated or malformed request behavior still needed tuning during April testing.
- Memory work focused on reducing database cache pressure after the node reaches tip. The `v0.4.0` release reopened the runtime AVL state database with a smaller redb cache once chain sync completed.
- NiPoPoW work included bootstrapping and proof-serving gaps. One noted difference was that the sigma-rust `NipopowProof` structure lacked a `continuous` field present in the JVM node.
- Use the Rust node for testing, differential validation, and implementation research unless release notes explicitly mark a version as production-ready. SANTA runner results are useful evidence for implementation parity, but they do not by themselves turn an experimental node into a production reference client.
