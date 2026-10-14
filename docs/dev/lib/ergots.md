---
title: ergots
description: TypeScript Ergo verification and ErgoScript tooling.
tags:
  - TypeScript
  - ErgoScript
  - NiPoPoW
  - libraries
owner: docs
last_reviewed: 2026-10-14
source_repos:
  - repo: mwaddip/ergots
    branch: master
    paths:
      - README.md
      - packages/scorex/package.json
      - packages/nipopow/package.json
      - packages/avltree/package.json
      - packages/ergoscript
      - packages/transaction/package.json
source_of_truth:
  - https://github.com/mwaddip/ergots
  - https://www.npmjs.com/package/@ergots/scorex
  - https://www.npmjs.com/package/@ergots/nipopow
  - https://www.npmjs.com/package/@ergots/avltree
  - https://www.npmjs.com/package/@ergots/ergoscript
  - https://www.npmjs.com/package/@ergots/transaction
---

# ergots

[ergots](https://github.com/mwaddip/ergots) is a TypeScript implementation effort for Ergo verification tooling. It targets browser-compatible code without WASM or Node `Buffer` dependencies, with tests comparing bytes, values, and costs against Rust and JVM reference implementations; the JVM is the consensus authority when they disagree.

## Packages

The repository is organized as a workspace:

- `@ergots/scorex`: Scorex wire codecs, block header types, digest helpers, and Autolykos v2 proof-of-work verification.
- `@ergots/nipopow`: NiPoPoW proof parsing, serialization, verification, comparison, in-memory and demand-loaded proving, continuous-mode verification, and P2P envelope codecs.
- `@ergots/avltree`: Batch AVL+ authenticated-tree verification and proving, including versioned persistent storage and rollback support.
- `@ergots/ergoscript`: ErgoTree parsing, serialization, partial evaluation, sigma-protocol verification, AVL+ integration, and method-handler work.
- `@ergots/transaction`: browser-clean transaction wire codec and validation package.

Current package metadata lists `@ergots/scorex` `0.3.0`, `@ergots/nipopow` `0.4.0`, `@ergots/avltree` `0.7.0`, `@ergots/ergoscript` `0.5.0`, and `@ergots/transaction` `0.1.0`. Check npm and the repository before pinning a package version in an application.

June 2026 team updates marked the first npm publication for the Scorex, AVL tree, NiPoPoW, and ErgoScript packages, followed by Sigma v6 support work. The packages remain useful for differential testing and browser-side verification experiments, not as a standalone consensus authority.

Recent work tightened JVM-alignment and input handling: context-extension ordering, typed context-extension keys, `Context.lastBlockUtxoRootHash`, header/pre-header accessors, v6 type gates, option tags, SBox/ErgoTree deserialization, box equality, collection equality costing, `atLeast` children caps, static signatures for selected methods, and `estimateCryptoCost` for JVM-faithful sigma-verification cost estimates. AVL work added `BatchAVLProver.restoreRoot`, exported node/storage helpers, a storage codec, and a versioned persistent prover. NiPoPoW `0.4.0` added prover entry points and continuous-mode proof handling. The corpus includes JVM-aligned parsing, node-construction checks, Deserialize substitution, storage-rent validation, and cumulative transaction cost. `reduceWith` exposes interpreter reduction with its charges, while transaction validation must preserve the distinction between accumulated entry cost and the returned total.

Important caveat: upstream still describes `ergots` as not yet a consensus-complete kernel. Use it for browser-side research, differential testing, and verification experiments; combine it with sigma-rust or a JVM node before relying on it for binding consensus decisions.

## Verification Scope

NiPoPoW verification checks proof structure, PoW under each header's declared difficulty, and required difficulty-header membership. It does not recompute the network difficulty schedule, enforce the network's hard-fork version schedule, or anchor to a trusted checkpoint. A successful `verifyProof` result alone is therefore not full consensus header validation.

`StrictBatchAVLVerifier` can require a proof to match the prover's canonical bytes. That additional strictness is useful for protocols that require one proof encoding; it is not an Ergo consensus requirement. Check package APIs and the documented scope before turning a fixture result into a consensus decision.

## When To Use It

Use `ergots` as an experimental TypeScript path for Ergo verification, browser-side research, or differential testing against sigma-rust. It is not a replacement for the reference client or sigma-rust in production consensus paths unless the upstream project marks the relevant package stable for that use.

## Links

- [ergots repository](https://github.com/mwaddip/ergots)
- [ErgoScript package](https://github.com/mwaddip/ergots/tree/master/packages/ergoscript)
