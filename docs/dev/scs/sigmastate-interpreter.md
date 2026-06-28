---
tags:
  - Sigmastate Interpreter
  - ErgoTree
  - ErgoScript
  - Compiler
  - Interpreter
owner: docs
last_reviewed: 2026-06-27
source_repos:
  - repo: ergoplatform/sigmastate-interpreter
    branch: develop
    paths:
      - README.md
      - docs/sigma-dsl.md
      - interpreter/shared/src/main/scala/sigmastate/interpreter/Interpreter.scala
      - sc/shared/src/main/scala/sigma/compiler/SigmaCompiler.scala
      - sc/shared/src/test/scala/sigmastate/lang
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - ergo-wallet
source_of_truth:
  - https://github.com/ergoplatform/sigmastate-interpreter/releases/tag/v6.0.5
  - https://github.com/ergoplatform/sigmastate-interpreter/tree/develop/README.md
  - https://github.com/ergoplatform/sigmastate-interpreter/tree/develop/docs/sigma-dsl.md
  - https://github.com/ergoplatform/sigmastate-interpreter/tree/develop/interpreter/shared/src/main/scala/sigmastate/interpreter/Interpreter.scala
  - https://github.com/ergoplatform/sigmastate-interpreter/tree/develop/sc/shared/src/main/scala/sigma/compiler/SigmaCompiler.scala
  - https://github.com/ergoplatform/sigmastate-interpreter/tree/develop/sc/shared/src/test/scala/sigmastate/lang
  - https://github.com/ergoplatform/ergo/tree/master/ergo-wallet
---

# Sigmastate Interpreter

## Overview

The [sigmastate-interpreter](https://github.com/ergoplatform/sigmastate-interpreter) repository contains the core implementations of the ErgoScript compiler and ErgoTree Interpreter. These tools are part of a broader framework that supports a family of Sigma-protocol based authentication languages, collectively known as the [*Sigma Language*](sigma-lang.md).

This library is integral to the operation of the [Ergo Node](https://github.com/ergoplatform/ergo) and the [ergo-wallet](https://github.com/ergoplatform/ergo/tree/master/ergo-wallet). It serves as the backbone for processing and validating ErgoScript contracts, ensuring that transactions comply with the defined cryptographic conditions.

## Recent updates

- `Jun 24`: [Sigma SDK v6.0.5](https://github.com/ergoplatform/sigmastate-interpreter/releases/tag/v6.0.5) was released.
- v6.0.5 added regression coverage for `ByIndex` upcasts with non-`Int` indexes, serializer benchmarks, cross-platform `Exponentiate` equivalence checks, subproject module names, TaggedVariable wire-format pinning with Scala-type deprecation, and rejection of negative-id variables in the `ContextExtension` deserializer.
- `May 28`: [Sigma SDK v6.0.4](https://github.com/ergoplatform/sigmastate-interpreter/releases/tag/v6.0.4) was released.
- v6.0.4 added compiler support for `None` expressions, including cases such as `val x: Option[Int] = None`, and included dependency updates and additional tests.
- `Apr 14`: [SigmaState interpreter v6.0.3](https://github.com/ergoplatform/sigmastate-interpreter/releases/tag/v6.0.3) and [sigmastate-js 0.6.1](https://www.npmjs.com/package/sigmastate-js) were released.
- v6.0.3 included compiler support for `Global.serialize`, contract-template deserialization fixes for v6 methods, and broader language-spec coverage.

/// details | DeepWiki Documentation
    {type: info, open: true}
For an alternative and potentially more detailed documentation source generated from the repository, explore the [Sigmastate Interpreter on DeepWiki](https://deepwiki.com/ergoplatform/sigmastate-interpreter/1-overview)
///

### Key Components

- **ErgoScript Compiler**:
  - The [ErgoScript Compiler](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sigmastate/src/main/scala/sigmastate/lang/SigmaCompiler.scala) translates high-level ErgoScript code into low-level ErgoTree bytecode. This bytecode can then be stored in UTXO coins to define spending conditions, akin to how scripts function in Bitcoin but with enhanced flexibility and capabilities.
- **ErgoTree Interpreter**:
  - The [ErgoTree Interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sigmastate/src/main/scala/sigmastate/interpreter/Interpreter.scala) executes the ErgoTree bytecode within a specific blockchain context. It evaluates the scripts against the current state of the blockchain and the spending transaction, ultimately producing a boolean outcome that determines the validity of the transaction.

### Sigma Language Background

In Bitcoin, each coin is secured by a script written in a stack-based language, which is evaluated by the Bitcoin Script interpreter. ErgoScript and the ErgoTree interpreter generalize this concept into an "authentication language" that can express complex spending conditions using Sigma protocols. These protocols allow for sophisticated cryptographic proofs, enabling the creation of contracts that can require multiple signatures, threshold signatures, or even conditions based on external data.

### Prover and Verifier Workflow

The Sigmastate Interpreter involves two primary components in transaction processing:

1. **Prover**:
    - The Prover uses the ErgoTree interpreter to reduce a high-level spending condition (ErgoTree) into a Sigma protocol proposition (SigmaBoolean). This proposition is then converted into a cryptographic proof using the [Fiat-Shamir transformation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/sigma-dsl.md), ensuring that the transaction can only be signed by parties possessing the necessary secrets.
2. **Verifier**:
    - The Verifier also uses the ErgoTree interpreter to independently reduce the ErgoTree into a SigmaBoolean. It then checks the provided proof against this proposition. This process ensures that the transaction is valid and the necessary conditions for spending are met.

### Integration and Usage

While the sigmastate-interpreter library provides the low-level primitives necessary for processing ErgoScript contracts, developers typically interact with these components through higher-level tools.

- **AppKit**:
  - A more accessible alternative for JVM-based development (Java/Scala/Kotlin) is [AppKit](appkit.md), a thin wrapper around the core components provided by the ErgoScript interpreter and Ergo protocol implementations.
- **SigmaJS**:
  - The library is cross-compiled to JavaScript using Scala.js, allowing developers to use these components directly in web applications via the [SigmaJS NPM package](https://www.npmjs.com/package/sigmastate-js).

### Getting Started

To start using the sigmastate-interpreter in your Scala project, add the following dependency to your SBT configuration:

```scala
libraryDependencies += "org.scorexfoundation" %% "sigma-state" % "5.0.14"
```

For more advanced usage and direct interaction with the ErgoTree and Sigma protocols, refer to the detailed [Sigma Language documentation](sigma-lang.md).
