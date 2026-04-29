---
tags:
  - Node
  - Rust
  - Infrastructure
  - Experimental
---

# Ergo Rust Node

## Overview

[Ergo Rust Node](https://github.com/mwaddip/ergo-node-rust) is an experimental Rust implementation of an Ergo node. It is not the reference client; use the Scala [Ergo reference client](install.md) for production unless a release explicitly says otherwise.

## Recent updates

- `Jan-Feb`: early header sync was working, with mainnet header heights above 400,000 and later above 1,130,000 reported in the development log.
- `Apr 9`: [v0.1.0](https://github.com/mwaddip/ergo-node-rust/releases) was published, with mainnet support under test and peer-penalty / fail2ban work added.
- `Apr 16`: `v0.3.0` reduced mainnet sync peak RSS from about `14.95 GB` to `9.5 GB`.
- `Apr 16`: `v0.3.1` validated to tip and fixed mainnet sync stalls around the voting boundary and sigma-rust v6 opcode parsing.
- `Apr 24`: proxy fallback was removed after it forwarded too many modifiers and caused peer bans.
- `Apr 26`: `v0.4.0` reduced at-tip steady-state RSS from about `7.3 GB` to `1.35 GB`; later testing reported `v0.4.2` at tip with about `0.70 GB` RSS.

Current development areas include mining endpoint support, NiPoPoW bootstrapping, RequestModifiers serving, mempool/API work, peer penalties, and reducing accidental bans from malformed or repeated requests.

## Implementation notes

- Mainnet validation work exposed sigma-rust edge cases. The log records consensus/compatibility fixes around context-extension ordering, v6 opcode parsing, JIT costing, lazy constant resolution, and pre-JIT compatibility paths.
- The peer-penalty system was designed to integrate with `fail2ban`, but repeated or malformed request behavior still needed tuning during April testing.
- Memory work focused on reducing database cache pressure after the node reaches tip. The `v0.4.0` release reopened the runtime AVL state database with a smaller redb cache once chain sync completed.
- NiPoPoW work included bootstrapping and proof-serving gaps. One noted difference was that the sigma-rust `NipopowProof` structure lacked a `continuous` field present in the JVM node.
- The node remained experimental through the log period. Use it for testing, differential validation, and implementation research unless later release notes say otherwise.
