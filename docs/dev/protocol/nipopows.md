---
tags:
  - NIPoPoWs
---
# NIPoPoWs

Ergo implements **NIPoPoWs**, or Non-interactive Proof-of-Proof-of-Work. These are short stand-alone strings that a computer program can inspect to verify that an event happened on a proof-of-work-based blockchain without connecting to the blockchain network and downloading all block headers. For example, these proofs can illustrate that a cryptocurrency payment was made.

## Blocks

In Ergo, blocks are broken into sections, just like Bitcoin, Ethereum, and other blockchains. In Bitcoin, there is simply a block header and the transactions themselves. However, in Ergo, we have some **extra sections** that enable new functionality:

* Header
* Transactions
* **Extensions**
* **Proofs of UTXO transformation**

The 'extension' section contains certain mandatory fields (including links for NiPoPoW, once per 1,024 block epoch) and parameters for miner voting, such as current block size. It can also contain arbitrary fields.

**What this means in practice is that different types of nodes and clients can download only those sections of the blocks they need – reducing the demands for storage, bandwidth, and CPU cycles.**

One application of NIPoPoWs described in a previous article deals with [logarithmic space mining](https://www.youtube.com/watch?v=s05ypkSC7gk). Logarithmic space mining allows for "light miners." Light miners can bootstrap with block headers like light clients without downloading the whole blockchain. It is also possible to store just a few necessary blocks to verify the whole blockchain in a blockchain, and this eradicates the need for miners to store all of the blockchains. Integrating logarithmic space mining in Ergo is possible via velvet (soft) forks, preventing the need for painful hard forks.



Another application of NIPoPoWs was proposed in the first [ErgoHack](ergohack.md) by a team called SmartPools. SmartPools' proposal aims to increase the **Nakamoto Coefficient**, a metric for calculating the decentralisation of the given network. In our case, the proposal aims to increase the decentralisation of the Ergo Platform by bootstrapping mining entities with collateralised smart contracts. The purpose here is to provide returns for non-miner investors and prevent big GPU farms from taking control of the system.



The most well-known example of NIPoPoWs is the implementation of the second layer blockchain. The second layers help interact with different blockchains by increasing scalability and creating private sidechains for enterprise-grade applications. The second layers create blockchains on top of the primary blockchain for different use cases. Because transactions can happen on these second layers without constant synchronous updates, we can lower the network load substantially by keeping everything on the main chain all the time.

**The Ergo blockchain has supported NIPoPoWs since its genesis, yet their use cases are still in their infancy. We continue to develop this field of research with our partners at [IOHK](https://iohk.io/) and [EMURGO](https://emurgo.io/), and we expect their application to increase with continued contributions from the community developers.**

## Literature

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)