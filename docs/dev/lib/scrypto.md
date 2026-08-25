---
tags:
  - Scrypto
  - Cryptography
  - Toolkit
  - Library
owner: docs
last_reviewed: 2026-08-25
source_repos:
  - repo: ergoplatform/scrypto
    branch: master
    release_watch: true
    paths:
      - README.md
source_of_truth:
  - https://github.com/ergoplatform/scrypto
  - https://github.com/ergoplatform/scrypto/releases/tag/v3.1.1
---

# Scrypto

[Scrypto](https://github.com/ergoplatform/scrypto) is a public-domain cryptographic toolkit for Scala. Ergo's SigmaState stack uses it for cryptographic primitives and authenticated data structures.

## Install

Scrypto 3.1.1 is published on Maven Central for Scala 2.11, 2.12, 2.13, and 3. Scala.js artifacts are available for Scala 2.13 and 3.

For the JVM:

```scala
libraryDependencies += "org.scorexfoundation" %% "scrypto" % "3.1.1"
```

For Scala.js:

```scala
libraryDependencies += "org.scorexfoundation" %%% "scrypto" % "3.1.1"
```

## Current Release

[v3.1.1](https://github.com/ergoplatform/scrypto/releases/tag/v3.1.1) updates Bouncy Castle and other dependencies, hardens serialization, fixes slicing, and fixes Merkle proofs when a tree contains duplicate leaf values.

## Main Features

- Authenticated AVL+ trees with batched operations, compressed proofs, and verifier work bounds.
- Blake2b, Keccak, SHA, Whirlpool, Skein, and Stribog hash functions.
- Base16, Base58, and Base64 encoding.
- Curve25519 and Ed25519 signing support through the upstream Curve25519 Java implementation.
- JVM and Scala.js builds.

Scrypto was extracted from [Scorex](https://github.com/ScorexProject/Scorex-Lagonaki). For APIs, examples, build instructions, and security notes, use the [upstream README](https://github.com/ergoplatform/scrypto#readme).
