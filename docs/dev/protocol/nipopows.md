---
tags:
  - NIPoPoWs
---

# Exploring NIPoPoWs in the Ergo Blockchain

Ergo Blockchain leverages a robust feature known as **NIPoPoWs**, an acronym for Non-interactive Proof-of-Proof-of-Work. NIPoPoWs are concise, self-sufficient data structures that allow a computer program to verify an event's occurrence on a proof-of-work-based blockchain without the need to connect to the blockchain network or download all block headers. A real-world implementation of this feature can include verifying the occurrence of a cryptocurrency transaction.

In the Bitcoin ecosystem, you'd commonly encounter a block header accompanied by the transactions. However, Ergo's [blocks](block.md) introduce **several additional sections**, opening avenues for new capabilities. For example, the 'extension' section contains mandatory fields (inclusive of NIPoPoWs links, refreshed every 1,024 block epochs) and parameters for miner voting like the present block size. It also has the capacity to hold arbitrary fields.

**This distinctive structure allows various types of nodes and clients to selectively download the block sections they need, thereby optimizing storage, bandwidth, and CPU utilization.**

## Applications

Each of the following application pages presents a unique use case for NIPoPoWs within the Ergo ecosystem:

- [Light Clients](nipopow_nodes.md)
- [Light Miners](logspace.md)
- [Sidechains](nipopow-sidechains.md)

**NIPoPoWs have been a fundamental part of the Ergo Blockchain since its foundation. Yet, we're continuously exploring the full spectrum of their potential. We're devoted to broadening this research field, in collaboration with our partners at [IOHK](https://iohk.io/), and eagerly anticipate an increased application of NIPoPoWs with ongoing contributions from the developer community.**

## For Further Exploration

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)


<!--TODO: Reorg 

One of the remarkable applications of NIPoPoWs, as discussed in an earlier article, is [logarithmic space mining](https://www.youtube.com/watch?v=s05ypkSC7gk). This mechanism facilitates "light miners" who can initialize with block headers like light clients, without needing to download the entire blockchain. What's more, you can store only a handful of crucial blocks to validate the entire blockchain, thereby eliminating the need for miners to store all blockchains. Integrating logarithmic space mining with Ergo is feasible through velvet (soft) forks, averting the complications of hard forks.

Another exciting application of NIPoPoWs came from a team called SmartPools during the inaugural [ErgoHack](ergohack.md). They proposed a method to enhance the **Nakamoto Coefficient** — a measure used to estimate a network's decentralization. The team's goal is to boost Ergo's decentralization by bootstrapping mining entities with collateralized smart contracts. The intent is to yield returns for non-miner investors and prevent large GPU farms from dominating the system.

Perhaps, the most notable use of NIPoPoWs lies in implementing second-layer blockchains. These secondary layers interact with various blockchains, augment scalability, and develop private sidechains for enterprise-grade applications. They generate blockchains on top of the primary one for diversified use cases. Since transactions on these secondary layers do not necessitate constant synchronous updates, we can substantially reduce network load by maintaining everything on the main chain at all times.
-->

