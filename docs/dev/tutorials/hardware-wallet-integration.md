---
tags:
  - hardware wallet
  - sigma-rust
  - no_std
  - embedded
  - keystone
  - ledger
  - rust
  - cryptography
  - secp256k1
  - k256
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/sigma-rust
    branch: develop
    paths:
      - ergo-lib/Cargo.toml
      - ergo-lib/src/lib.rs
  - repo: arobsn/ledger-ergo-js
    branch: master
    paths:
      - README.md
  - repo: ergoplatform/ledger-app-ergo
    branch: main
    paths:
      - README.md
      - doc
  - repo: arobsn/keystone-ergo-js
    branch: master
    paths:
      - README.md
  - repo: KeystoneHQ/keystone-sdk-base
    branch: master
    paths:
      - packages/ur-registry-ergo/README.md
      - packages/ur-registry-ergo
source_of_truth:
  - https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/Cargo.toml
  - https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/lib.rs
  - https://github.com/arobsn/ledger-ergo-js
  - https://github.com/arobsn/ledger-ergo-js/releases/tag/v0.2.0
  - https://github.com/arobsn/ledger-ergo-js/releases/tag/v0.2.1
  - https://github.com/ergoplatform/ledger-app-ergo
  - https://github.com/arobsn/keystone-ergo-js
  - https://github.com/ergoplatform/sigma-rust/pull/834
  - https://github.com/KeystoneHQ/keystone-sdk-base/tree/master/packages/ur-registry-ergo
  - https://github.com/KeystoneHQ/keystone-sdk-rust/pull/105
  - https://github.com/KeystoneHQ/keystone3-firmware/pull/1427
---

# Hardware Wallet Integration with sigma-rust

## Introduction

Integrating Ergo support into hardware wallets (like Ledger, Trezor, Keystone, etc.) presents unique challenges due to the resource-constrained nature of these devices (limited memory, processing power, and no standard library/OS). The default `ergo-lib` configuration in [`sigma-rust`](sigma-rust.md) enables Rust's standard library (`std`), but upstream also has a `no_std` configuration. Device integration still requires checking dependencies, allocation, and the target's signing interface.

This guide provides developers with pointers and strategies for adapting `sigma-rust` functionality for hardware wallet integration, based on community discussions and efforts.

## Key Challenges

* **No `std`:** Hardware wallets typically run bare-metal or on a minimal RTOS, lacking Rust's standard library (`std`). Code must be compatible with `no_std`.
* **Limited Resources:** Memory (RAM and flash) and CPU cycles are scarce. Libraries and cryptographic operations must be efficient.
* **Dependency Bloat:** Large dependencies can quickly exceed storage limits.
* **Cryptographic Primitives:** Hardware wallets often have optimized, built-in implementations of core cryptographic primitives (like secp256k1) that should ideally be leveraged instead of pulling in separate library implementations.

## Adapting `sigma-rust`: Strategies and Tools

### 1. Using `sigma-rust-mini` and `no_std`

Upstream `ergo-lib` uses `#![cfg_attr(not(feature = "std"), no_std)]`. Disable its default features with `default-features = false`; there is no upstream feature named `no_std` to enable. The defaults enable `std`, `json`, `nipopow`, and `merkle`. Select compatible features for the version and target you use: the current library has an explicit compile-time guard rejecting `nipopow` or `merkle` without `std`.

The historical [sigma-rust-mini fork](https://github.com/Alesfatalis/sigma-rust-mini/tree/no_std) is additional integration context. A successful `no_std` build alone does not establish that an application fits a device's memory limits or uses its secure key storage correctly.

### 2. Replacing Cryptographic Backends (k256 vs. secp256k1)

Upstream `sigma-rust` depends on [`k256`](https://crates.io/crates/k256). A device may expose its own cryptographic primitives through an SDK, but replacing a Rust dependency does not by itself integrate secure-element keys or Ergo's Sigma-protocol signing flow. An adapter must preserve key derivation, scalar/group encodings, nonce handling, and the protocol's signing semantics.

The [Ledger Ergo app](https://github.com/ergoplatform/ledger-app-ergo) is a C application built with the Ledger SDK. Treat its device-side implementation and the host-side JavaScript bindings as separate parts of the signing boundary. Generic ECDSA APIs or `secp256k1` crate methods are not a substitute for that Ergo-specific protocol.

### 3. Minimizing Dependencies

Carefully review the dependency tree of the `sigma-rust` components you intend to use. Remove or replace dependencies that are too large or rely on `std`. This might involve:

* Using feature flags to disable unused functionality.
* Replacing crates with lighter-weight or `no_std` alternatives where possible.
* Potentially re-implementing certain non-cryptographic helper functions if their dependencies are problematic.

## Core Functionality to Port

The essential functions needed for basic hardware wallet support typically include:

* **Key Derivation:** Deriving child keys from a master seed according to [EIP-3](eip3.md).
* **Address Generation:** Generating Ergo addresses from public keys.
* **Transaction Parsing:** Securely parsing transaction details for display and user confirmation.
* **Transaction Signing:** Signing the transaction digest using the derived private key. This is the most critical part and must use the hardware wallet's secure key storage and signing mechanism.
* **ErgoTree Serialization/Hashing:** Potentially needed for constructing parts of the transaction message to be signed.

## Ledger Reference Stack

For Ledger-specific Ergo integration, the active JavaScript binding layer is [ledger-ergo-js](https://github.com/arobsn/ledger-ergo-js). Its February 2025 `v0.2.x` releases added OS-level device helpers such as `openApp()`, `closeApp()`, and `getCurrentAppInfo()`, which are useful when orchestrating app-selection and signing flows from desktop or browser-adjacent tools.

The hardware app itself lives in [ergoplatform/ledger-app-ergo](https://github.com/ergoplatform/ledger-app-ergo). Upstream documentation describes the current build flow, API docs, and automated test setup, including Ragger-based functional tests for Nano S+, Nano X, Stax, and Flex.

For the narrower wallet-facing notes page, see [Ledger](ledger.md).

## Keystone Serialization Work

[keystone-ergo-js](https://github.com/arobsn/keystone-ergo-js) is an experimental JavaScript reference for Ergo transaction serialization in Keystone-style hardware-wallet flows. Treat it as integration reference material, not a complete wallet standard.

July 2025 dev updates said `keystone-ergo-js` `v0.1.0` had shipped with a custom serialization schema, later adding reduced-transaction custom serialization. The Keystone/Nautilus path also depended on sigma-rust JSON serialization for reduced transactions, exposed for JS bindings in [sigma-rust#834](https://github.com/ergoplatform/sigma-rust/pull/834).

Keystone's upstream SDK also includes [`@keystonehq/bc-ur-registry-ergo`](https://github.com/KeystoneHQ/keystone-sdk-base/tree/master/packages/ur-registry-ergo), an Ergo extension for `bc-ur-registry` used by Keystone-style UR signing flows. Use it when comparing Ergo sign-request encoding against Keystone's registry packages.

The broader Keystone integration spans multiple upstream components. The Rust SDK [Ergo support PR](https://github.com/KeystoneHQ/keystone-sdk-rust/pull/105) was closed unmerged after review, while the Keystone3 firmware [Ergo support PR](https://github.com/KeystoneHQ/keystone3-firmware/pull/1427) remains the reference firmware integration work and links back to the Rust and JavaScript SDK PRs. Treat these PRs as implementation context until support is merged and released by Keystone.

August 2025 wallet updates described the Nautilus integration as close to review, with one final sigma-rust prerequisite merged and remaining work around Keystone firmware cleanup plus physical-device integration testing. Treat that as development status, not a shipped hardware-wallet path.

## Conclusion

Integrating Ergo with hardware wallets requires careful adaptation of existing libraries like `sigma-rust`. Leveraging `no_std` compatible forks/versions, replacing cryptographic backends to use the device's optimized implementations (like `secp256k1`), and minimizing dependencies are key strategies. This is a complex task often requiring deep knowledge of both the Ergo protocol and embedded Rust development. Collaboration within the developer community is crucial for advancing hardware wallet support.
