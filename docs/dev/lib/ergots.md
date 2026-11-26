---
title: ergots
description: TypeScript Ergo verification and ErgoScript tooling.
tags:
  - TypeScript
  - ErgoScript
  - NiPoPoW
  - libraries
owner: docs
last_reviewed: 2026-11-26
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
  - https://github.com/mwaddip/ergots/commit/a33e07adaf98
  - https://github.com/mwaddip/ergots/commit/32e6f9f8de85
  - https://github.com/mwaddip/ergots/commit/7e2a895148c8
  - https://github.com/mwaddip/ergots/commit/563768014d70
  - https://github.com/mwaddip/ergots/commit/55495c621839
  - https://github.com/mwaddip/ergots/commit/fb2e1aed30a9
  - https://github.com/mwaddip/ergots/commit/d34db6642461
  - https://github.com/mwaddip/ergots/commit/63f9b69e9b77
  - https://github.com/mwaddip/ergots/commit/b9065327d4d1
  - https://github.com/mwaddip/ergots/commit/721f9a5834d9
  - https://github.com/mwaddip/ergots/commit/6b80cad53a66
  - https://github.com/mwaddip/ergots/commit/cb3ae086c168
  - https://github.com/mwaddip/ergots/commit/6c54141a640c
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

### Recent ErgoScript alignment work

The upstream package documentation and commits from 2026-11-18 to 2026-11-20 add several JVM-alignment details that are easy to miss when reading the high-level package list:

- `tupleColl(items)` is exported from the package root. It builds the `Coll[Any]` that the JVM data reader gives for a tuple of any arity other than two; a pair stays a `{ kind: 'Tuple' }` value. The element type is identity-sensitive (`SANY_JVM`), so a structural `SAny` object is not treated as a tuple collection by the writer or the lambda-applying collection arms. Callers binding a non-pair tuple at a register or extension position should use this builder. See [a33e07a](https://github.com/mwaddip/ergots/commit/a33e07adaf98), [32e6f9f](https://github.com/mwaddip/ergots/commit/32e6f9f8de85) and [7e2a895](https://github.com/mwaddip/ergots/commit/7e2a895148c8).
- Collection values carry their JVM runtime class (`cls` and array class). Operations that cast or store elements reject with `coll-class-cast` or `coll-array-store` where the JVM would throw `ClassCastException` or `ArrayStoreException`. An empty `map` or `flatMap` whose mapper range ergots types as `SAny` may carry the `unknown` class marker; readers follow the JVM's empty-receiver rule for it. See [5637680](https://github.com/mwaddip/ergots/commit/563768014d70) and [55495c6](https://github.com/mwaddip/ergots/commit/55495c621839).
- `SigmaAnd` and `SigmaOr` refuse a node with no items, `XorOf` behaves as exclusive-or at every tree version, and `BoolToSigmaProp` passes a `SigmaProp` through below activated version 2. See [fb2e1ae](https://github.com/mwaddip/ergots/commit/fb2e1aed30a9), [d34db66](https://github.com/mwaddip/ergots/commit/d34db6642461), [63f9b69](https://github.com/mwaddip/ergots/commit/63f9b69e9b77) and [b906532](https://github.com/mwaddip/ergots/commit/b9065327d4d1).
- `TaggedVariable` (`0x71`), `TrueLeaf` (`0x7f`), `FalseLeaf` (`0x80`), `ModQ` (`0xe7`), `PlusModQ` (`0xe8`) and `MinusModQ` (`0xe9`) parse and round-trip because the JVM parses them. The Boolean leaves become the constants `true` and `false` (written back in constant form); the arithmetic and tagged variants reject at evaluation with `unsupported-eval-node`, charging nothing and evaluating no operand. See [721f9a5](https://github.com/mwaddip/ergots/commit/721f9a5834d9), [6b80cad](https://github.com/mwaddip/ergots/commit/6b80cad53a66) and [cb3ae08](https://github.com/mwaddip/ergots/commit/cb3ae086c168).
- `@ergots/ergoscript` now depends on the workspace `@ergots/avltree` `0.7.0`. The root README table still lists `0.6.0`, so use `packages/*/package.json` for exact versions before pinning an application. See [6c54141](https://github.com/mwaddip/ergots/commit/6c54141a640c).

Important caveat: upstream still describes `ergots` as not yet a consensus-complete kernel. Use it for browser-side research, differential testing, and verification experiments; combine it with sigma-rust or a JVM node before relying on it for binding consensus decisions.

## Verification Scope

NiPoPoW verification checks proof structure, PoW under each header's declared difficulty, and required difficulty-header membership. It does not recompute the network difficulty schedule, enforce the network's hard-fork version schedule, or anchor to a trusted checkpoint. A successful `verifyProof` result alone is therefore not full consensus header validation.

`StrictBatchAVLVerifier` can require a proof to match the prover's canonical bytes. That additional strictness is useful for protocols that require one proof encoding; it is not an Ergo consensus requirement. Check package APIs and the documented scope before turning a fixture result into a consensus decision.

## When To Use It

Use `ergots` as an experimental TypeScript path for Ergo verification, browser-side research, or differential testing against sigma-rust. It is not a replacement for the reference client or sigma-rust in production consensus paths unless the upstream project marks the relevant package stable for that use.

## Links

- [ergots repository](https://github.com/mwaddip/ergots)
- [ErgoScript package](https://github.com/mwaddip/ergots/tree/master/packages/ergoscript)
