---
tags:
  - Go
  - Ergo
---

# Ergo Platform and Go

Go developers can interact with the Ergo blockchain primarily through bindings to the core `sigma-rust` library. See the main [sigma-rust bindings list](sigma-rust.md#bindings) for details.

The resources for integrating Ergo using the Go programming language are currently limited compared to some other languages. However, there are key projects available:

## Ergo-Golang

The [*ergo-golang*](https://github.com/azhiganov/ergo-golang) project is a promising tool for integrating with Ergo. At present, the project is in its initial stages and may be considered as under development. This implies that while it offers basic functionalities to interact with the Ergo Blockchain, it may not have extensive features and may not be fully tested or optimized.

As an open-source project, *ergo-golang* offers a fantastic opportunity for Go developers to contribute to its development by providing enhancements, fixes, and new features.

Please note that if you come across any issues or require more detailed instructions, you can always connect with the Ergo community. The [`#development` Discord channel](https://discord.gg/kj7s7nb) is an excellent platform to receive support from seasoned Ergo developers and community members.

### Ergo-lib-go

[*ergo-lib-go*](https://github.com/sigmaspace-io/ergo-lib-go/tree/main) is a Go wrapper around C bindings for ErgoLib from sigma-rust. This library provides Go developers with the ability to interact with the Ergo blockchain using the robust functionalities of ErgoLib, which is originally written in Rust.
