---
tags:
  - Data Structures 
---

# Data Structures

In Ergo, several key data structures are employed to support its blockchain and smart contract functionality. Here's a list of the main data structures used within the Ergo ecosystem:

## 1. **AVL Trees (Authenticated Dynamic Dictionaries)**
   - **Purpose**: AVL Trees in Ergo are used to store and authenticate dynamic sets of data in a compact and efficient manner. They are particularly useful for stateful smart contracts.
   - **Usage**: 
     - In the storage of UTXO states, where efficient verification of state changes is required.
     - In applications like off-chain code and distributed systems managing the Plasma infrastructure, where privacy-preserving transactions need to verify inclusion or exclusion of certain elements without revealing all details.
   - **Documentation Reference**: [AVL Trees in Ergo](avl.md), [Plasma](plasma.md)

## 2. **Merkle Trees**
   - **Purpose**: Merkle Trees are a fundamental data structure in the Ergo blockchain, ensuring the integrity and authenticity of data. They play a crucial role in various blockchain operations, from verifying transactions within blocks to securing additional metadata in the Extension Block.
   - **Usage**:
     - In the construction of the [Transaction Merkle Tree](tx-merkle.md), combining all transactions and their corresponding spending proofs into a single Merkle Tree.
     - In the [Extension Block Merkle Tree](merkle-extension.md), securing key-value data like miner votes and protocol parameters.
     - In creating [Merkle Batch Proofs](merkle-batch-proof.md), allowing efficient verification of multiple data elements within a Merkle Tree.
     - In generating compact proofs of state transitions, enabling lightweight clients to securely participate in the network. An example of how a lite client can check a Merkle-tree-based membership proof is detailed in the [Lite Client Checking Merkle Proof](merkle-light-proof.md) documentation.
   - **Documentation Reference**: [Merkle Trees in Ergo](merkle-tree.md)

## 3. **Sigma Trees (ErgoTree)**
   - **Purpose**: Sigma Trees, also known as ErgoTrees, are specialized data structures that represent logical propositions and cryptographic conditions in the Ergo blockchain. These trees are used in the execution of smart contracts and scripts, encapsulating complex logic and cryptographic proofs.
   - **Usage**:
     - In representing the logic and conditions of ErgoScript smart contracts.
     - In evaluating conditions for spending boxes (UTXOs) by verifying the cryptographic proofs and logic encoded in the ErgoTree.
     - Potential future integration with Merkle Trees (MT) or Sparse Merkle Trees (SMT) to enable working with Ergo transactions and the extension block database directly from ErgoScript.
   - **Documentation Reference**: [ErgoTree](ergotree.md)

## 4. **Context Data Structures**
   - **Purpose**: These structures represent the contextual information that is available during the execution of ErgoScripts. Contexts include details such as the current block height, the transaction being processed, and any additional data inputs.
   - **Usage**:
     - In providing necessary environmental details for smart contract execution.
     - In enabling the contextual flexibility of ErgoScripts.
   - **Documentation Reference**: [Context Data Structures](blockchain-context.md)

## 5. **Proof of Proof-of-Work (PoPow) Data Structures**
   - **Purpose**: These are specialized data structures used to implement PoPow, which allows lightweight nodes to verify the longest chain without downloading the entire blockchain.
   - **Usage**:
     - In creating and verifying interlink vectors, which are crucial for PoPow security.
     - In enabling lightweight clients to participate in the network with minimal data requirements.
   - **Documentation Reference**: [PoPow Data Structures](popow.md)

## 6. **Box Data Structures**
   - **Purpose**: Boxes are the fundamental data structures representing UTXOs in Ergo. Each box contains value, associated tokens, and an ErgoScript that defines spending conditions.
   - **Usage**:
     - In the creation and management of UTXOs.
     - In defining conditions for transaction execution within the blockchain.
   - **Documentation Reference**: [Box Format](box.md)

## 7. **Transaction Data Structures**
   - **Purpose**: These structures represent the transactions within the Ergo blockchain. They include inputs, outputs, data inputs, and other necessary information for executing transactions.
   - **Usage**:
     - In organizing and executing financial transfers, contract calls, and state changes.
     - In ensuring the integrity and validity of transactions through the blockchain.
   - **Documentation Reference**: [Transaction Format](transactions.md)

## 8. **Interlink Vectors**
   - **Purpose**: Used in conjunction with Merkle Trees for PoPow proofs, interlink vectors allow efficient verification of the chain of blocks in the blockchain.
   - **Usage**:
     - In the implementation of PoPow protocols for verifying blockchain headers.
   - **Documentation Reference**: [Interlink Vectors](interlink-vectors.md)

## Potential Additional Data Structures
As the Ergo ecosystem continues to evolve, additional data structures may be introduced, particularly in areas such as privacy-preserving protocols, advanced smart contract functionalities, or optimization of blockchain operations.

## Hash-Based Accumulators

For UTXO-based systems, simpler and well-studied hash-based accumulators are effective. Sparse Merkle Trees are sufficient for UTXO settings, though not the most efficient solution. More efficient alternatives include UTREEXO or the approaches described in [this paper](https://eprint.iacr.org/2021/340.pdf).

## UTREEXO

UTREEXO is a more efficient alternative for representing the UTXO set compared to traditional Merkle Trees. It allows for partially stateless clients, which can be practical in many scenarios. However, fully stateless clients still require archival nodes to store and update client proofs.

## Partially Stateless Clients

Ergo currently employs an approach outlined in [this paper](https://eprint.iacr.org/2016/994.pdf) to support partially stateless clients. This approach balances security and efficiency, as fully stateless clients still depend on archival nodes for storing and updating client proofs.

