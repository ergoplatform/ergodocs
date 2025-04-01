---
tags:
  - ADProofs
  - Authenticated Data Proofs
  - Block
  - Data Model
---

# ADProofs (Authenticated Data Proofs)

*(Back to: [Block Overview](block.md))*

**ADProofs**, short for Authenticated Data Proofs, are a crucial component of Ergo's [block structure](block.md) that allows for efficient and secure [validation](validation.md) of [transactions](transactions.md) without requiring full blockchain download. They are particularly beneficial for "[light clients](modes.md)" – [wallets](wallets.md) or [nodes](install.md) that don't store the entire blockchain.

**Function:**

* **Efficient Transaction Validation:** ADProofs enable light clients to verify the validity of transactions within a block by proving they are included in the [Merkle tree](merkle-tree.md) of the [UTXO set](eutxo.md). This eliminates the need to download and process the entire UTXO set or the full block.
* **State Verification:** Light clients can use ADProofs to calculate the new [state root](block-header.md) (a cryptographic summary of the UTXO set) after applying the transactions in a block. This allows them to stay synchronized with the blockchain without storing the complete state.
* **Security:** ADProofs are cryptographically secure, ensuring that any tampering with the transactions or the UTXO set will be detected during validation.

**Structure:**

The `ADProofs` class in [ADProofs.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/ADProofs.scala) defines the structure of ADProofs. It contains the following key elements:

* **headerId:** The ID of the [block header](block-header.md) to which these proofs correspond.
* **proofBytes:** The serialized cryptographic proof that allows for verification of the state changes.

**Verification Process:**

1. **Initialization:** A light client receives the block header, the ADProofs, and the list of [transactions](block-transactions.md).
2. **Proof Application:** The client uses the `ADProofs` to construct a `BatchAVLVerifier`. This verifier utilizes the provided proof to validate the changes made to the UTXO set by the transactions.
3. **State Root Calculation:** The verifier calculates the new state root after applying the transactions. This calculated root is then compared against the state root declared in the block header.
4. **Verification Result:** If the calculated state root matches the one in the header, the transactions and the state transition are considered valid.

**Key Concepts:**

* **[Merkle Tree](merkle-tree.md):** A tree-like data structure where each leaf node represents a piece of data (in this case, a transaction or a [box](box.md)) and each non-leaf node is a hash of its child nodes. This structure allows for efficient verification of data inclusion.
* **[AVL+ Tree](avl.md):** A self-balancing binary search tree used in Ergo to represent the UTXO set. It enables efficient lookups and updates while maintaining a verifiable structure.
* **Batch Verification:** The process of verifying multiple operations (transaction additions or removals) within the UTXO set simultaneously, optimizing efficiency.

**Benefits:**

* **Reduced Bandwidth:** Light clients can avoid downloading full blocks and the entire UTXO set, saving significant bandwidth.
* **Increased Efficiency:** ADProofs streamline the validation process, making it faster and less resource-intensive for light clients.
* **Enhanced Scalability:** By enabling lightweight participation, ADProofs contribute to the overall scalability of the Ergo blockchain.
