---
tags:
  - Libraries
  - Development
  - SDKs
  - Bindings
---

# Libraries & SDKs

Ergo offers a rich ecosystem of Software Development Kits (SDKs), libraries, and language bindings to help developers build applications on the blockchain. These tools provide abstractions and utilities for interacting with nodes, creating and signing transactions, working with ErgoScript, and more.

## Primary SDKs

These are the main SDKs recommended for most dApp development use cases:

- 🥇 **[AppKit](https://github.com/ergoplatform/ergo-appkit)**: Java/Scala SDK for building Ergo apps, suitable for JVM environments and Android development. [`Java`, `Scala`]
- 🥇 **[Fleet SDK](https://fleet-sdk.github.io/docs/)**: A pure JS/TS library designed for effortless Ergo transaction creation in web-based dApps and Node.js environments. [GitHub Org](https://github.com/fleet-sdk) [`JS/TS`]
- 🥇 **[Sigma-Rust](https://github.com/ergoplatform/sigma-rust/)**: Rust implementation of ErgoTree types, core primitives, and serialization, forming the basis for many other libraries and bindings. [`Rust`]

## Core Libraries

These libraries form the foundation of Ergo's core logic and cryptography:

- 🥇 **[Sigmastate Interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter)**: The reference implementation of the ErgoTree interpreter and ErgoScript language. [`Scala`, `ErgoScript`]
- [Scrypto](https://github.com/input-output-hk/scrypto/): Cryptographic primitives library used by the Sigmastate Interpreter. [`Scala`]
- [Scorex Util](https://github.com/ScorexFoundation/scorex-util): Utility classes for Scorex projects. [`Scala`]
- [Debox](https://github.com/ScorexFoundation/debox): Efficient primitive type Boxes for Scala. [`Scala`]

## Language Bindings (via Sigma-Rust)

Sigma-Rust provides bindings for various languages, allowing developers to leverage its core functionality:

- 🥇 **[ErgoLib](https://github.com/ergoplatform/sigma-rust/tree/develop/ergo-lib)**: High-level Rust abstractions built on top of `sigma-rust`. [Docs](https://docs.rs/ergo-lib/) [`Rust`]
- 🥇 **[ergo-lib-wasm](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm)**: WASM bindings for JavaScript/TypeScript (Browser & Node.js). [NPM (Browser)](https://www.npmjs.com/package/ergo-lib-wasm-browser) | [NPM (NodeJS)](https://www.npmjs.com/package/ergo-lib-wasm-nodejs) [`JS/TS`, `Rust`]
- [ergo-lib-jni](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-jni): JNI bindings for JVM languages (Java, Scala, Kotlin). [Docs](https://docs.rs/ergo-lib-jni/) [`Java`, `Rust`]
- 🥇 **[ergo-lib-python](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-python)**: Python bindings. [PyPI](https://pypi.org/project/ergo-lib/) [`Python`, `Rust`]
- *Note: Bindings for C and Go also exist.*

## Specific Library Documentation

The following pages provide more detailed documentation on specific libraries within the ecosystem:

::cards::

[
  {
    "title": "GetBlok Plasma",
    "url": "lib/plasma.md"
  },
  {
    "title": "Scrypto",
    "url": "lib/scrypto.md"
  },
  {
    "title": "EIP12-Types",
    "url": "lib/eip12-types.md"
  },
  {
    "title": "SigmaJS",
    "url": "lib/sigmajs.md"
  }

]

::/cards::
