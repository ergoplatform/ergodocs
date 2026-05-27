---
tags:
  - Merkle Tree
  - Data Structures
  - Cryptography
owner: docs
last_reviewed: 2026-05-26
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala
      - ergo-core/src/main/scala/org/ergoplatform/modifiers/history/extension/Extension.scala
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala
  - https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/extension/Extension.scala
---

# Merkle Trees in Ergo

*(Back to: [Data Model Overview](data-model.md))*

## Overview

**Merkle Trees** are a fundamental [data structure](data-structures.md) in the Ergo blockchain, ensuring the integrity and authenticity of data. They play a crucial role in various blockchain operations, from verifying [transactions](transactions.md) within [blocks](block.md) to securing additional metadata in the [Extension Block](extension-section.md). For current non-initial block versions, Ergo commits to both transaction IDs and witness IDs in the transaction Merkle tree, so the block header root covers transaction bodies and their [spending proofs](signing.md).

The Merkle Tree format in Ergo follows a specific structure and encoding scheme that is essential for developers working with Merkle proofs and validating data inclusion. For detailed information on the Merkle Tree format, leaf nodes, internal nodes, and the process of validating Merkle proofs, refer to the [Merkle Tree Format](merkle-format.md) and [Merkle Tree Validation](merkle-validation.md) sections.

## Key Characteristics

- **Binary Tree Structure**: Ergo employs a binary structure for its Merkle Trees, where each node has two children. Leaf nodes contain hashes of transaction data or proofs, while internal nodes contain hashes of their child nodes.
- **Cryptographic Security**: The cryptographic hashes ensure that any alteration in the underlying data is reflected in the **Merkle Root**, making the tree tamper-evident.
- **Deterministic Byte Representation**: The byte representation of transactions in Ergo is deterministic, allowing consistent restoration and verification of Merkle Tree roots, even if transactions are serialized in different formats, such as JSON.
- **Pregenesis State**: Ergo's deterministic pregenesis state, configured at the blockchain's inception, facilitates seamless restoration and verification of state transitions by comparing them with the hashes stored in the [block header](block-header.md).

## Core Applications of Merkle Trees in Ergo

### Transaction Merkle Tree

The [Transaction Merkle Tree](tx-merkle.md) is a core component of Ergo. In the initial block version, it is built from transaction IDs. In later versions, it is built from transaction IDs followed by witness IDs, where witness IDs commit to serialized spending proofs. This provides a cryptographic guarantee that transaction data and authorization proofs have not been tampered with. The Merkle Root is included in the [block header](block-header.md), ensuring that any change to a committed transaction or proof changes the root.

**Code Reference**: The implementation can be found in the [BlockTransactions.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala) file.

### Extension Block Merkle Tree

The [Extension Block Merkle Tree](merkle-extension.md) secures key-value data like [miner votes](governance.md) and [protocol parameters](governance.md). It organizes this data into a binary Merkle Tree, with leaf nodes containing key-value pair hashes and non-leaf nodes containing child node hashes. The root hash is included in the block header, cryptographically committing to the [Extension Block](extension-section.md) data. Merkle proofs allow efficient verification of specific key-value pairs without downloading the entire block. This tree ensures data integrity and enables secure storage of auxiliary blockchain information.

**Code Reference**: The implementation can be found in the [Extension.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/extension/Extension.scala) file.

### Merkle Batch Proofs

[Merkle Batch Proofs](merkle-batch-proof.md) are an advanced application that allows for efficient verification of multiple data elements within a Merkle Tree, reducing computational overhead. These proofs build on the foundational Merkle Trees used in transactions and the Extension Block.

### State Proofs

Merkle Trees are also used to create compact proofs of state transitions (related to [AD Proofs](block-adproofs.md)). These proofs allow for efficient verification of the blockchain state without requiring a [full node](archival-node.md), which is crucial for [lightweight clients](light-spv-node.md) to securely participate in the network. An example of how a lite client can check a Merkle-tree-based membership proof is detailed in the [Lite Client Checking Merkle Proof](merkle-light-proof.md) documentation.
