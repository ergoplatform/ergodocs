---
tags:
  - Block
  - Data Model
---

# Understanding Blocks in Ergo

*(Back to: [Data Model Overview](data-model.md))*

In blockchain technology, a **block** is a fundamental unit of data that groups together a set of [transactions](transactions.md). These blocks are linked together chronologically to form a "blockchain," serving as a secure and transparent record of all transactions.

[Proof-of-Work (PoW)](autolykos.md) is a consensus mechanism that requires [miners](mining-overview.md) to solve complex mathematical problems to add new blocks to the blockchain. This process, known as "[mining](mining-overview.md)," involves significant computational effort, ensuring the security and immutability of the blockchain.

Ergo, like other Proof-of-Work (PoW) blockchains such as Bitcoin, uses blocks to record transactions and ensure the integrity of the network. However, Ergo's block structure is more sophisticated, offering enhanced functionality and efficiency.

In Ergo, a new block is created approximately every **two minutes**. Initially, each block rewarded miners with 75 ERG, which were distributed among them and the [Ergo Foundation Treasury](ef-treasury.md). This [emission schedule](emission.md) applied for the first two years of the network's operation. You can find more details in the [emission section](emission.md).


## Ergo Block Structure

Ergo's blocks are divided into distinct sections to optimize organization and functionality:

1. [**Header**](block-header.md): The header acts as a summary of the block's content. It includes metadata (block version, timestamp, etc.), hashes linking to other block sections, and the Proof-of-Work solution.

2. [**Block Transactions**](block-transactions.md): This section contains the core data of the block – a list of all transactions included within it. These transactions define how [tokens](tokens.md) and assets are transferred on the Ergo blockchain.

3. [**ADProofs**](block-adproofs.md): These cryptographic proofs, short for Authenticated Data Proofs, allow [light clients](modes.md) ([nodes](install.md) with limited storage) to verify transactions without downloading the entire block or the full [UTXO set](eutxo.md).

4. [**Extension**](extension-section.md): This section provides a flexible space to store additional data that doesn't fit into the other sections. It includes interlinks for [NiPoPoWs](nipopows.md) (efficient proof-of-work verification) and system parameters (e.g., block size).

This structured approach enhances efficiency and allows for greater flexibility in incorporating new features and upgrades into the Ergo blockchain.

## Related Concepts

* **Ergo Modifiers:** In Ergo's [peer-to-peer network protocol](p2p-protocol-overview.md), blocks and transactions are referred to as "[modifiers](modifiers.md)." These modifiers are exchanged between nodes to keep the network synchronized. [More details](modifiers.md)
* **Superblock Clients:** Ergo supports "superblock clients," which provide an additional layer of efficiency and flexibility for specific use cases, related to [logarithmic space mining](log_space.md). [More details](log_space.md).
