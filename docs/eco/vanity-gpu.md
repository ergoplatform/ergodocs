---
tags:
  - Vanity GPU
  - Mining
  - Tooling
owner: docs
last_reviewed: 2026-05-30
source_repos:
  - repo: arkadianet/erg-vanity-gpu
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/arkadianet/erg-vanity-gpu
---

# Vanity GPU

[erg-vanity-gpu](https://github.com/arkadianet/erg-vanity-gpu) is a GPU-accelerated Ergo vanity address generator using OpenCL. It supports multi-GPU search, multiple patterns, optional case-insensitive matching, BIP44 derivation at `m/44'/429'/0'/0/{index}`, benchmark mode, and device selection.

The upstream README marks the project as early-development software. It warns that the cryptographic implementations were written from scratch and should not be trusted for significant funds unless the generated mnemonic and address are independently verified with trusted wallet software.

## GPU Vanity Address Generator

Early benchmarks reported roughly `790k/sec` on `7x 3060 Ti`, roughly `1.3M/sec` across all GPUs, and later about `320k addresses/sec` on an RTX 3080 Ti. The build notes also called out nightly Rust requirements for the OpenCL path.

Current prerequisites are Rust 2021 stable plus OpenCL runtime/development headers. The CLI can list devices, search specific GPUs or all GPUs, stop after a fixed number of matches, run for a duration, and benchmark the GPU pipeline.

## Related Pages

- [Miner Tooling](miner-tooling.md)
- [Mining Overview](mining-overview.md)
