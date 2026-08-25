---
tags:
  - Vanity GPU
  - Mining
  - Tooling
owner: docs
last_reviewed: 2026-08-25
source_repos:
  - repo: arkadianet/erg-vanity-gpu
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/arkadianet/erg-vanity-gpu
  - https://github.com/arkadianet/erg-vanity-gpu/releases/tag/v0.4.0
---

# Vanity GPU

[erg-vanity-gpu](https://github.com/arkadianet/erg-vanity-gpu) is a GPU-accelerated Ergo vanity address generator. Prefix searches use OpenCL by default, with an optional NVIDIA CUDA backend on Linux; suffix and contains searches remain CPU-only. It supports a desktop GUI, CPU fallback, multi-GPU search, multiple patterns, optional case-insensitive matching, BIP44 derivation at `m/44'/429'/0'/0/{index}`, estimates, benchmarks, and device selection.

The upstream README marks the project as early-development software. It warns that the cryptographic implementations were written from scratch and should not be trusted for significant funds unless the generated mnemonic and address are independently verified with trusted wallet software.

## GPU Vanity Address Generator

[v0.4.0](https://github.com/arkadianet/erg-vanity-gpu/releases/tag/v0.4.0) adds larger default GPU batches and the optional CUDA backend for Linux builds on NVIDIA `sm_75+` GPUs. Set `ERG_BACKEND=cuda` to opt in; OpenCL remains the default and the same kernels are used by both paths.

Current prerequisites for source builds are Rust 2021 stable plus OpenCL runtime/development headers. The CLI can list devices, search specific GPUs or all GPUs, stop after a fixed number of matches, run for a duration, estimate difficulty, and benchmark the GPU pipeline. It rejects impossible mainnet P2PK prefixes before searching.

The upstream RTX 3090 measurements range from roughly `563k` addresses/second at the default `--index 1` to `36.9M` addresses/second at `--index 500`, but higher index counts trade wallet discoverability for throughput. Most wallets stop after roughly 20 unused BIP44 slots, so restore may not find a result at a high slot without manual scanning. Keep the default unless you understand that tradeoff, and treat all benchmark figures as hardware- and driver-specific.

## Related Pages

- [Miner Tooling](miner-tooling.md)
- [Mining Overview](mining-overview.md)
