---
tags:
  - Node
  - Protocol
  - P2P
  - Validation
  - Processing
  - Modifiers
---

# Ergo Node Protocol

## Overview

*(Back to: [Node Overview](install.md))*

The Node Protocol section provides a comprehensive overview of the core operational aspects of the Ergo network. It covers the following key areas:

## Recent updates

- `Jan 23`: Ergo reference client [v6.0.2](https://github.com/ergoplatform/ergo/releases/tag/v6.0.2) was released, and 6.1.2 was also published for the related line.
- `Jan-Apr`: the release stream included P2P, fork, sync, cache-growth, DoS, miner-candidate, and memory-exhaustion fixes, alongside subblock/input-block work.
- `Apr 20`: the 6.0.3 candidate was finalized in [PR #2291](https://github.com/ergoplatform/ergo/pull/2291), and [v6.0.2.1](https://github.com/ergoplatform/ergo/releases/tag/v6.0.2.1) was published as a pre-release jar identical to 6.0.3 for public testnet operators and miners needing the new API methods.
- Wallet-related fixes included duplicate-address restore work in [PR #2244](https://github.com/ergoplatform/ergo/pull/2244) and the USE node-wallet decimal display issue in [issue #2289](https://github.com/ergoplatform/ergo/issues/2289).
- Token minting caveat: indexers or explorers that assume all minted supply is emitted into one output can display a wrong emission amount for non-standard multi-output mints.

Release-stream details:

- The log distinguishes the Scala reference client release line from Matrix test builds. Subblock/input-block work was merged with the 6.0.3 candidate line for testing, but production activation still depended on review, release notes, and later rollout steps.
- `v6.0.2.1` was described as a 6.0.3-compatible pre-release jar for public testnet operators and miners needing the new Matrix/miner API work before the final release.
- Additional post-6.0.3 work was expected for compiler, memory-exhaustion, and JIT-costing fixes.
- Duplicate transaction IDs and mempool invalidation were under investigation after DEX transactions sat pending and were cleared slowly.

- **Processing Algorithm**: This section explains the algorithm used for processing Ergo [modifiers](modifiers-processing.md). It is applicable across all [security modes](modes.md) within the Ergo network, ensuring consistent data processing.

- **Validation Rules**: This part outlines the consensus-critical [validation rules](modifiers-validation.md). These rules are mandatory for every [node](install.md) in the Ergo network to maintain network integrity and security. They ensure that all [transactions](transactions.md) and [blocks](block.md) adhere to the established network standards.

- **P2P Protocol**: The [P2P Protocol](p2p-protocol-overview.md) section delves into the [peer-to-peer](p2p-protocol-overview.md) protocol used in the Ergo network. It provides insights into how nodes communicate and share information, facilitating efficient data exchange within the network.

- **Peer Management**: The [peer management](peer-management.md) section discusses the strategies nodes in the Ergo network employ to manage their peers. It includes information about peer discovery, connection, and disconnection, providing a clear understanding of how nodes maintain network connectivity.

By understanding these aspects, you can gain a deeper insight into how the Ergo network operates, ensuring its security and efficiency.
