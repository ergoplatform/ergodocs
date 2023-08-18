---
tags:
  - NIPoPoWs
---

# Non-interactive Proof-of-Proof-of-Work (NIPoPoWs)

The Ergo Blockchain integrates a robust feature known as NIPoPoWs, or Non-interactive Proof-of-Proof-of-Work. NIPoPoWs are efficient data structures that authenticate blockchain events using proof-of-work, eliminating the need for a direct connection to the blockchain network or downloading all block headers. This feature is especially beneficial for verifying cryptocurrency transactions.

## Overview

Ergo's block structure goes beyond the traditional block header and transaction format seen in systems like Bitcoin. It includes additional sections for improved functionality. One such section is the 'extension' section. This section houses mandatory fields such as NIPoPoWs links, which are updated every 1,024 block epochs, and parameters for miner voting, including the current block size. The 'extension' section is also capable of storing miscellaneous fields.

This unique structure provides flexibility to different types of nodes and clients. They can choose to download only the block sections they need, thereby optimizing their storage space, bandwidth, and CPU usage.

## Applications

NIPoPoWs have been utilized innovatively within the Ergo ecosystem:

1. **[Light Clients](nipopow_nodes.md)**: Light Clients play a crucial role in enhancing the accessibility and scalability of blockchain networks. They address the challenges associated with running a full node, which requires substantial computational resources, electricity, and storage space to maintain the entire blockchain. Ergo leverages Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) to facilitate the creation of efficient light clients.
2. **[Light Miners](logspace.md)**: A significant application of NIPoPoWs is logarithmic space mining. This technology allows "light miners" to begin with block headers, similar to light clients, without the need to download the entire blockchain. By retaining only a select few important blocks, light miners can validate the entire blockchain, eliminating the need to store the complete set of blockchains. This approach can be integrated with Ergo through velvet (soft) forks, avoiding the complexities of hard forks.
3. **[Sidechains](nipopow-sidechains.md)**: Non-Interactive Proofs of Proof-of-Work (NiPoPoWs) are a novel technology that enables trustless sidechains. They leverage Simplified Payment Verification (SPV) proofs to provide resistance against potential attacks, while maintaining a small enough size for efficient network transmission.

NIPoPoWs have been a crucial part of the Ergo Blockchain since its inception. We are dedicated to continually exploring their potential, expanding this research area in collaboration with our partners at IOHK. We anticipate increased use of NIPoPoWs with ongoing contributions from our active developer community.

<!--TODO: Remove?
## Enhancing Decentralization

Another intriguing application of NIPoPoWs was proposed by a team named SmartPools during the inaugural ErgoHack. Their method aims to enhance the Nakamoto Coefficient, a measure used to estimate a network's decentralization. The team strives to boost Ergo's decentralization by empowering mining entities with collateralized smart contracts, providing returns for non-miner investors, and preventing large GPU farms from dominating the system.

## Implementing Second-layer Blockchains

Perhaps the most impactful application of NIPoPoWs is in developing second-layer blockchains. These secondary layers interact with various blockchains to improve scalability and create private sidechains for enterprise-grade applications. They generate blockchains on top of the primary one for diversified use cases. As transactions on these secondary layers do not require constant synchronous updates, we can significantly reduce network load by maintaining everything on the main chain at all times.
-->
## Additional Resources

For those interested in exploring NIPoPoWs further, here are some recommended resources:

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)