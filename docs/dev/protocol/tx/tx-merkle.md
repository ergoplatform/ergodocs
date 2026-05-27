---
tags:
  - Merkle
owner: docs
last_reviewed: 2026-05-26
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala
      - ergo-core/src/main/scala/org/ergoplatform/modifiers/history/header/Header.scala
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala
  - https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/header/Header.scala
---

# Transaction Merkle Tree

## Overview

In the Ergo blockchain, the Transaction Merkle Tree is a vital data structure that ensures the integrity and authenticity of transactions within a block. This mechanism is similar to the Merkle Tree implementation in Bitcoin, where trees are constructed for block transactions and transaction witnesses (introduced with the SegWit upgrade). However, in Ergo, the process is adapted and extended to combine both transactions and their corresponding spending proofs into a single Merkle Tree.

### **Merkle Tree Structure**

A Merkle Tree is a binary tree where each node contains a cryptographic hash. Leaf nodes represent the hash of individual data elements, such as transactions and their spending proofs, while non-leaf nodes represent the hash of their child nodes. The topmost node, known as the Merkle Root, serves as a cryptographic commitment to the entire dataset. This structure allows for efficient verification of data integrity, ensuring that even if only a small portion of the data is checked, the entire dataset can be trusted.

The Merkle Tree format in Ergo follows a specific structure and encoding scheme that is essential for developers working with Merkle proofs and validating data inclusion. For detailed information on the Merkle Tree format, leaf nodes, internal nodes, and the process of validating Merkle proofs, refer to the [Merkle Tree Format](merkle-format.md) and [Merkle Tree Validation](merkle-validation.md) sections.

## Construction of the Transaction Merkle Tree

### **Leaf Node Structure**

In current Ergo node code, the transaction root is version-dependent:

- For the initial block version, the tree is built from transaction IDs only.
- For later block versions, the tree is built from transaction IDs followed by witness IDs, where each witness ID commits to the serialized spending proofs.

This means newer blocks commit to both transaction bodies and authorization proofs in the same transaction root, but the implementation stores them as separate 32-byte leaves rather than one paired 64-byte leaf per transaction.

Each leaf is constructed as:

  ```
  hash(0 || pos || data)
  ```

  where `pos` is the position of the leaf in the tree and `data` is a 32-byte transaction ID or witness ID. A prefix of `0` is used for domain separation.

### **Internal Node Structure**

- **Node Construction**: Internal nodes in the Merkle Tree are constructed by hashing the concatenation of their child nodes:

  ```
  hash(1 || left_child || right_child)
  ```

  where `1` is a prefix added for domain separation. If both children are empty, the node is considered empty (`null`).

### **Merkle Root**

The Merkle Root is derived by recursively hashing the tree from the leaf nodes up to the root. This root serves as a cryptographic summary of all the transactions and their proofs within a block.

- **Root Calculation**: The root of the tree is derived by recursively hashing the tree from the leaf nodes up to the root. If the root hash is `null`, it is replaced with a string of zeros of the same length as the hash function output (typically 256 bits).

### **Code Implementation**

The core implementation of the Transaction Merkle Tree can be found in the Ergo codebase:

- **[BlockTransactions.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala)**: This file contains the logic for constructing the Transaction Merkle Tree, including the methods to calculate the Merkle Root and verify transactions within a block.

`BlockTransactions` serialization is also version-aware. For block versions greater than 1, the serializer writes a version marker as `10,000,000 + blockVersion` before the transaction count, so older records without that marker can still be read without a database rescan. From protocol version 6.0 onward, transaction parsing and serialization run inside the matching `VersionContext`.

## Inclusion in Block Header

The Merkle Root, calculated from the Transaction Merkle Tree, is included in the block header. This inclusion ensures that the integrity of the entire block's transactions can be verified by simply verifying the root hash. If any transaction or its corresponding proofs are altered, the Merkle Root will change, and this discrepancy can be detected by nodes in the network.

### **Code Implementation**

- **[Header.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/header/Header.scala)**: This file manages the block header structure, including the Merkle Root, which is crucial for the block's validity.

## Efficiency and Security

### **Efficiency**

The Transaction Merkle Tree structure allows for efficient verification of individual transactions. A lightweight client can verify that a particular transaction is included in a block by downloading only a small portion of the tree, rather than the entire block.

### **Security**

The combined use of transaction identifiers and spending proofs within the Merkle Tree enhances the security of the Ergo blockchain. It ensures that both the transaction data and the corresponding authorization (spending proofs) are protected against tampering.

## Use Cases in Ergo

### **Block Validation**

Nodes use the Merkle Root to verify the integrity of transactions within newly received blocks. If the Merkle Root doesn't match the expected value, the block is rejected.

### **Lightweight Client Verification**

Clients that do not store the full blockchain can still verify the inclusion of transactions by using Merkle proofs. This allows them to trust the blockchain without needing to download and store all transaction data.

### **Fraud Proofs**

If a node detects an invalid transaction, it can create a fraud proof by providing a Merkle proof that demonstrates the inclusion of the transaction in the block. This mechanism is essential for maintaining the security and trustworthiness of the blockchain.

## Performance Considerations

The Transaction Merkle Tree in Ergo is designed with efficiency in mind, allowing for fast verification and compact representation of transactions and proofs. However, there are some performance considerations to keep in mind:

1. **Tree Construction Time**: Building the Merkle Tree for a block can be computationally intensive, especially for blocks with a large number of transactions. This process needs to be optimized for efficient block mining and validation.

2. **Memory Usage**: Storing the entire Merkle Tree in memory can be memory-intensive, especially for large blocks. Efficient data structures and caching mechanisms should be employed to minimize memory usage.

3. **Proof Generation and Verification**: While Merkle proofs are compact and efficient for verifying individual transactions, generating and verifying these proofs can still be computationally expensive, especially for large blocks or when dealing with a high volume of transactions.

### **Practical Example**

To address these performance considerations, the Ergo codebase employs various optimization techniques and data structures. Here's a practical example of constructing a Transaction Merkle Tree using the Ergo codebase:

- **Example Code Reference**: Detailed examples of constructing and verifying Transaction Merkle Trees can be found in the Ergo codebase within the [`BlockTransactions.scala`](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala) file.
