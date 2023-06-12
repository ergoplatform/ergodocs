---
tags:
  - NIPoPoWs
---

# Non-interactive Proof-of-Proof-of-Work

The Ergo Blockchain incorporates a powerful feature known as **NIPoPoWs**, or Non-interactive Proof-of-Proof-of-Work. Simply put, NIPoPoWs are compact data structures that validate the occurrence of events on a blockchain using proof-of-work, without needing to connect to the blockchain network or download all block headers. This feature can be used practically to confirm a cryptocurrency transaction.

Ergo's [blocks](block.md) go beyond the standard block header and transaction format you might encounter in systems like Bitcoin, offering **additional sections** for expanded functionality. The 'extension' section, for instance, holds mandatory fields (including NIPoPoWs links updated every 1,024 block epochs) and parameters for miner voting like the current block size. It's also designed to store arbitrary fields.

**This unique structure enables various types of nodes and clients to selectively download only the necessary block sections, optimizing storage space, bandwidth, and CPU usage.**

## Applications

Here are some innovative applications of NIPoPoWs within the Ergo ecosystem:

- [Light Clients](nipopow_nodes.md)
- [Light Miners](logspace.md)
- [Sidechains](nipopow-sidechains.md)

**NIPoPoWs have been a fundamental part of the Ergo Blockchain since its inception. We're committed to continuously exploring the potential of NIPoPoWs, expanding this research area in collaboration with our partners at [IOHK](https://iohk.io/). We look forward to seeing an increased use of NIPoPoWs with ongoing contributions from our vibrant developer community.**

## Logarithmic Space Mining

One notable application of NIPoPoWs is [logarithmic space mining](https://www.youtube.com/watch?v=s05ypkSC7gk). This technology enables "light miners" to start with block headers like light clients, without the need to download the entire blockchain. In fact, you can keep only a select few important blocks to validate the whole blockchain, removing the need for miners to store the complete set of blockchains. This approach can be integrated with Ergo through velvet (soft) forks, avoiding the complexities of hard forks.

## Enhancing Decentralization

Another exciting application of NIPoPoWs was proposed by a team named SmartPools during the inaugural [ErgoHack](ergohack.md). Their method aims to improve the **Nakamoto Coefficient**, a measure used to estimate a network's decentralization. The team seeks to boost Ergo's decentralization by empowering mining entities with collateralized smart contracts, intending to provide returns for non-miner investors and prevent large GPU farms from dominating the system.

## Implementing Second-layer Blockchains

Perhaps, the most significant application of NIPoPoWs is in developing second-layer blockchains. These secondary layers interact with various blockchains to improve scalability and create private sidechains for enterprise-grade applications. They generate blockchains on top of the primary one for diversified use cases. As transactions on these secondary layers do not require constant synchronous updates, we can significantly reduce network load by maintaining everything on the main chain at all times.

## Additional Resources

For those wishing to delve deeper into NIPoPoWs:

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)