---
tags:
- NIPoPoWs
---

# Light Clients and NIPoPoWs in Ergo

**Light Clients** play a crucial role in enhancing the accessibility and scalability of blockchain networks. They address the challenges associated with running a full node, which requires substantial computational resources, electricity, and storage space to maintain the entire blockchain.

Ergo leverages Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) to facilitate the creation of efficient light clients. Here's how NIPoPoWs contribute to Ergo's ecosystem:

## Simplified Payment Verification (SPV) Client

NIPoPoWs enable Ergo to build a mobile [SPV client](light-spv-node.md) that requires only around 100KB of block headers to be downloaded. This significantly simplifies the process of verifying whether a transaction has occurred on the blockchain. As a result, users can interact with the Ergo blockchain using more efficient and convenient mobile wallets.

## Pruned Full-Node

NIPoPoWs can also be used to create a [Pruned Full-Node](pruned-full-node.md) using UTXO Set Snapshots. This approach allows for a more storage-efficient full node that maintains the necessary data for transaction verification without storing the entire blockchain history.

By leveraging NIPoPoWs, Ergo ensures that users can interact with its blockchain network efficiently, regardless of their device's computational capabilities or storage capacity.