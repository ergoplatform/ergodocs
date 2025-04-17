---
tags:
  - Rust
  - SigmaRust
  - Bindings
  - Wasm
  - JavaScript
  - TypeScript
  - Swift
  - iOS
  - Java
  - JVM
  - C
  - Go
  - Ruby
  - Python
---

# Sigma Rust

Rust implementation of [ErgoScript (sigmastate-interpreter)](sigmastate-interpreter.md) cryptocurrency scripting language.


## Crates

[ergo-lib](https://github.com/ergoplatform/sigma-rust/tree/develop/ergo-lib) [![Latest Version](https://img.shields.io/crates/v/ergo-lib.svg)](https://crates.io/crates/ergo-lib) [![Documentation](https://docs.rs/ergo-lib/badge.svg)](https://docs.rs/crate/ergo-lib)

Overarching crate exposing wallet-related features: chain types (transactions, boxes, etc.), JSON serialization, box selection for tx inputs, tx builder and signing. Exports other crates API, probably the only crate you'd need to import.

[ergotree-interpreter](https://github.com/ergoplatform/sigma-rust/tree/develop/ergotree-interpreter) [![Latest Version](https://img.shields.io/crates/v/ergotree-interpreter.svg)](https://crates.io/crates/ergotree-interpreter) [![Documentation](https://docs.rs/ergotree-interpreter/badge.svg)](https://docs.rs/crate/ergotree-interpreter)

ErgoTree interpreter

[ergotree-ir](https://github.com/ergoplatform/sigma-rust/tree/develop/ergotree-ir) [![Latest Version](https://img.shields.io/crates/v/ergotree-ir.svg)](https://crates.io/crates/ergotree-ir) [![Documentation](https://docs.rs/ergotree-ir/badge.svg)](https://docs.rs/crate/ergotree-ir)

ErgoTree IR and serialization.

[ergoscript-compiler](https://github.com/ergoplatform/sigma-rust/tree/develop/ergoscript-compiler) [![Latest Version](https://img.shields.io/crates/v/ergoscript-compiler.svg)](https://crates.io/crates/ergoscript-compiler) [![Documentation](https://docs.rs/ergoscript-compiler/badge.svg)](https://docs.rs/crate/ergoscript-compiler)

ErgoScript compiler.

[sigma-ser](https://github.com/ergoplatform/sigma-rust/tree/develop/sigma-ser) [![Latest Version](https://img.shields.io/crates/v/sigma-ser.svg)](https://crates.io/crates/sigma-ser) [![Documentation](https://docs.rs/sigma-ser/badge.svg)](https://docs.rs/crate/sigma-ser)

Ergo binary serialization primitives.

### Bindings

This section lists available language bindings for `sigma-rust`, allowing developers to interact with the Ergo blockchain using various programming languages.

*   **Wasm:**
    *   Crate: [`ergo-lib-wasm`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm) [![Latest Version](https://img.shields.io/crates/v/ergo-lib-wasm.svg)](https://crates.io/crates/ergo-lib-wasm) [![Documentation](https://docs.rs/ergo-lib-wasm/badge.svg)](https://docs.rs/crate/ergo-lib-wasm)
*   **JavaScript / TypeScript:**
    *   Browser: [`ergo-lib-wasm-browser`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm) [![Latest version](https://img.shields.io/npm/v/ergo-lib-wasm-browser)](https://www.npmjs.com/package/ergo-lib-wasm-browser)
    *   Node.js: [`ergo-lib-wasm-nodejs`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm) [![Latest version](https://img.shields.io/npm/v/ergo-lib-wasm-nodejs)](https://www.npmjs.com/package/ergo-lib-wasm-nodejs)
*   **Swift (iOS):**
    *   Repo: [`ergo-lib-ios`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-ios)
*   **Java / JVM:**
    *   Repo: [`ergo-lib-jni`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-jni) [![Latest Version](https://img.shields.io/crates/v/ergo-lib-jni.svg)](https://crates.io/crates/ergo-lib-jni) [![Documentation](https://docs.rs/ergo-lib-jni/badge.svg)](https://docs.rs/crate/ergo-lib-jni)
*   **C:**
    *   Repo: [`ergo-lib-c`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-c) [![Latest Version](https://img.shields.io/crates/v/ergo-lib-c.svg)](https://crates.io/crates/ergo-lib-c) [![Documentation](https://docs.rs/ergo-lib-c/badge.svg)](https://docs.rs/crate/ergo-lib-c)
*   **Go:**
    *   Repo: [`ergo-lib-go`](https://github.com/ergoplatform/ergo-lib-go) [![Go Reference](https://pkg.go.dev/badge/github.com/ergoplatform/ergo-lib-go.svg)](https://pkg.go.dev/github.com/ergoplatform/ergo-lib-go) *(Note: Community maintained)*
*   **Ruby:**
    *   Repo: [`sigma_rb`](https://github.com/thedlop/sigma_rb) [![Gem Version](https://badge.fury.io/rb/sigma_rb.svg)](https://badge.fury.io/rb/sigma_rb) *(Note: Community maintained)*
*   **Python:**
    *   Package: [`ergo-lib-python`](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-python) [![PyPI version](https://badge.fury.io/py/ergo-lib.svg)](https://badge.fury.io/py/ergo-lib) [![Documentation](https://docs.rs/ergo-lib/badge.svg)](https://docs.rs/crate/ergo-lib) *(Note: Uses ergo-lib crate docs)*
    *   See also: [ergo-lib-python docs](ergo-lib-python.md)

## Usage Examples

To get better understanding on how to use it in your project check out how its being used in the following projects:

Rust:

- [Oracle Core](https://github.com/ergoplatform/oracle-core);
- [Ergo Headless dApp Framework](https://github.com/Emurgo/ergo-headless-dapp-framework);
- [Ergo Node Interface Library](https://github.com/Emurgo/ergo-node-interface);
- [Spectrum Off-Chain Services for Ergo](https://github.com/spectrum-finance/spectrum-offchain-ergo);
- [AgeUSD Stablecoin Protocol](https://github.com/Emurgo/age-usd);
- [ErgoNames SDKs](https://github.com/ergonames/sdk/tree/master/rust)

TS/JS:

- [Ergo SDK](https://github.com/ergolabs/ergo-sdk-js) (Wasm bindings);
- [Yoroi wallet](https://github.com/Emurgo/yoroi-frontend) (Wasm bindings);
- [Ergo Desktop Wallet](https://github.com/ErgoWallet/ergowallet-desktop) (Wasm bindings);

Examples:

- [Create transaction demo](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm/examples/create-transaction-demo) (TS)
- [Address generation demo](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm/examples/address-generation-demo) (TS)

Also take a look at tests where various usage scenarios were implemented.
