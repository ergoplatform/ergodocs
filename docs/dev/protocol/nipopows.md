---
tags:
  - NIPoPoWs
---

# Non-interactive Proof-of-Proof-of-Work (NIPoPoWs)


The Ergo Blockchain incorporates a powerful feature known as NIPoPoWs, or Non-interactive Proof-of-Proof-of-Work. NIPoPoWs are compact data structures that validate blockchain events using proof-of-work, without the need to connect to the blockchain network or download all block headers. This feature is particularly useful for confirming cryptocurrency transactions.

## Overview

Ergo's blocks go beyond the standard block header and transaction format found in systems like Bitcoin. They offer additional sections for expanded functionality. The 'extension' section, for instance, holds mandatory fields, including NIPoPoWs links updated every 1,024 block epochs, and parameters for miner voting, such as the current block size. It is also designed to store arbitrary fields.

This unique structure enables various types of nodes and clients to selectively download only the necessary block sections, optimizing storage space, bandwidth, and CPU usage.

## Applications

NIPoPoWs have found innovative applications within the Ergo ecosystem:

1. Light Clients: [Learn more](nipopow_nodes.md)
2. Light Miners: [Learn more](logspace.md)
3. Sidechains: [Learn more](nipopow-sidechains.md)

NIPoPoWs have been a fundamental part of the Ergo Blockchain since its inception. We are committed to continuously exploring their potential, expanding this research area in collaboration with our partners at IOHK. We look forward to increased use of NIPoPoWs with ongoing contributions from our vibrant developer community.

## Logarithmic Space Mining

One notable application of NIPoPoWs is logarithmic space mining. This technology enables "light miners" to start with block headers, similar to light clients, without the need to download the entire blockchain. By keeping only a select few important blocks, light miners can validate the entire blockchain, eliminating the need to store the complete set of blockchains. This approach can be integrated with Ergo through velvet (soft) forks, avoiding the complexities of hard forks.

## Enhancing Decentralization

Another exciting application of NIPoPoWs was proposed by a team named SmartPools during the inaugural ErgoHack. Their method aims to improve the Nakamoto Coefficient, a measure used to estimate a network's decentralization. The team seeks to boost Ergo's decentralization by empowering mining entities with collateralized smart contracts, providing returns for non-miner investors, and preventing large GPU farms from dominating the system.

## Implementing Second-layer Blockchains

Perhaps the most significant application of NIPoPoWs is in developing second-layer blockchains. These secondary layers interact with various blockchains to improve scalability and create private sidechains for enterprise-grade applications. They generate blockchains on top of the primary one for diversified use cases. As transactions on these secondary layers do not require constant synchronous updates, we can significantly reduce network load by maintaining everything on the main chain at all times.

## Additional Resources

For those wishing to delve deeper into NIPoPoWs, here are some recommended resources:

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)