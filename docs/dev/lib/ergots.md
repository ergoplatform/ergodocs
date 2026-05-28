---
title: ergots
description: TypeScript Ergo verification and ErgoScript tooling.
tags:
  - TypeScript
  - ErgoScript
  - NiPoPoW
  - libraries
owner: docs
last_reviewed: 2026-05-27
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

## When To Use It

Use `ergots` as an experimental TypeScript path for Ergo verification, browser-side research, or differential testing against sigma-rust. It is not a replacement for the reference client or sigma-rust in production consensus paths unless the upstream project marks the relevant package stable for that use.

## Links

- [ergots repository](https://github.com/mwaddip/ergots)
- [ErgoScript package](https://github.com/mwaddip/ergots/tree/master/packages/ergoscript)
