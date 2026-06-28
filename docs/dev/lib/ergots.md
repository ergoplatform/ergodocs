---
title: ergots
description: TypeScript Ergo verification and ErgoScript tooling.
tags:
  - TypeScript
  - ErgoScript
  - NiPoPoW
  - libraries
owner: docs
last_reviewed: 2026-06-27
source_repos:
  - repo: mwaddip/ergots
    branch: master
    paths:
      - README.md
      - packages/ergoscript
source_of_truth:
  - https://github.com/mwaddip/ergots
---

# ergots

[ergots](https://github.com/mwaddip/ergots) is a TypeScript implementation effort for Ergo verification tooling. It targets browser-compatible code without WASM or Node `Buffer` dependencies, with tests comparing output against Rust reference implementations.

## Packages

The repository is organized as a workspace:

- `@ergots/scorex`: Scorex wire codecs, block header types, digest helpers, and Autolykos v2 proof-of-work verification.
- `@ergots/nipopow`: NiPoPoW proof parsing, serialization, verification, comparison, and P2P envelope codecs.
- `@ergots/avltree`: Batch AVL+ authenticated-tree verification.
- `@ergots/ergoscript`: ErgoTree parsing, serialization, partial evaluation, sigma-protocol verification, AVL+ integration, and method-handler work.

The upstream README lists published package versions as `@ergots/scorex` `0.3.0`, `@ergots/nipopow` `0.2.0`, `@ergots/avltree` `0.2.0`, and `@ergots/ergoscript` `0.3.0`; later repository release commits include `@ergots/ergoscript` `0.5.0` and `@ergots/transaction` `0.1.0`. Check npm and the repository before pinning a package version in an application.

Recent work tightened JVM-alignment and input handling: context-extension ordering, typed context-extension keys, `Context.lastBlockUtxoRootHash`, header/pre-header accessors, v6 type gates, option tags, SBox/ErgoTree deserialization, box equality, collection equality costing, `atLeast` children caps, static signatures for selected methods, and `estimateCryptoCost` for JVM-faithful sigma-verification cost estimates. The README reports `7028` tests passing across packages under both `node` and `jsdom`.

Important caveat: upstream still describes `ergots` as not yet a consensus-complete kernel. Use it for browser-side research, differential testing, and verification experiments; combine it with sigma-rust or a JVM node before relying on it for binding consensus decisions.

## When To Use It

Use `ergots` as an experimental TypeScript path for Ergo verification, browser-side research, or differential testing against sigma-rust. It is not a replacement for the reference client or sigma-rust in production consensus paths unless the upstream project marks the relevant package stable for that use.

## Links

- [ergots repository](https://github.com/mwaddip/ergots)
- [ErgoScript package](https://github.com/mwaddip/ergots/tree/master/packages/ergoscript)
