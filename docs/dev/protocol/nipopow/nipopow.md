---
tags:
  - NIPoPoWs
---
# NIPoPoWs

Ergo implements **NIPoPoWs**, or Non-interactive Proof-of-Proof-of-Work. These are short stand-alone strings that a computer program can inspect to verify that an event happened on a proof-of-work-based blockchain without connecting to the blockchain network and downloading all block headers. For example, these proofs can illustrate that a cryptocurrency payment was made.

## Blocks

In Ergo, just like Bitcoin, Ethereum, and other blockchains, blocks are broken into sections. In Bitcoin, there's simply a block header and the transactions themselves. But in Ergo, we have some **extra sections** that enable new functionality:

* Header
* Transactions
* **Extensions**
* **Proofs of UTXO transformation**

The 'extension' section contains certain mandatory fields (including links for NiPoPoW, once per 1,024 block epoch) and parameters for miner voting, such as current block size. It can also contain arbitrary fields.

**What this means in practice is that different types of nodes and clients can download only those sections of the blocks they need – reducing the demands for storage, bandwidth, and CPU cycles.**








## Literature

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)









