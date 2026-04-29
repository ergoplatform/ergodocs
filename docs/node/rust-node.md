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
