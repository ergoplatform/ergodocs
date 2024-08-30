---
tags:
  - Merkle
---

# Extension Block Merkle Tree in Ergo

## Overview

The Extension Block Merkle Tree in Ergo is crucial in ensuring the integrity and authenticity of additional key-value data stored within the extension section of each block. This data includes miner votes, protocol parameters, and other auxiliary information that extends the functionality of the Ergo protocol beyond the standard transaction data.

By leveraging Merkle Trees, the Ergo blockchain can efficiently and securely verify the integrity of this auxiliary data, ensuring that it has not been tampered with.

## Key Components of the Extension Block Merkle Tree

### 1. Key-Value Data Structure

The Extension Block in Ergo is essentially a key-value storage system. Each block in the blockchain can contain a variety of key-value pairs that represent different types of auxiliary data. This data could include:

- **Miner Votes**: Information on miner preferences or decisions on protocol upgrades.
- **Protocol Parameters**: Configurations or rules that guide the blockchain’s operations.
- **Non-Interactive Proofs**: Cryptographic proofs that can be validated without requiring interaction with other blockchain participants.

Each key-value pair in the Extension Block is encoded as a leaf node in the Merkle Tree. This encoding ensures that even small changes to any key or value will result in a different Merkle Root, making any tampering immediately detectable.

### 2. Construction of the Merkle Tree

The process of constructing the Extension Block Merkle Tree involves organizing the key-value pairs into a binary tree structure, where each leaf node contains a cryptographic hash of the key-value pair, and each non-leaf node contains a hash of its child nodes.

**Code Reference**: The implementation of this Merkle Tree construction process is handled in the [Extension.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/extension/Extension.scala) file within the Ergo codebase. The relevant method for creating the Merkle Tree from key-value pairs is the `merkleTree` method within the `Extension` object.

```scala
def merkleTree: MerkleTree = {
  val leafData = keyValuePairs.map { case (key, value) =>
    hash(key ++ value)
  }
  MerkleTree.fromLeafData(leafData)
}
```

In this code, `keyValuePairs` represent the sequence of key-value data in the Extension Block. The method computes the cryptographic hash for each pair and constructs the Merkle Tree using these hashes.

### 3. Inclusion of the Merkle Root in the Block Header

Once the Merkle Tree is constructed, the root hash (Merkle Root) is included in the block header. This inclusion serves as a cryptographic commitment to the entire set of key-value pairs in the Extension Block, ensuring that the data has not been altered or tampered with after the block was created.

The Merkle Root's presence in the block header allows any participant in the network to validate the integrity of the Extension Block's data by simply verifying the Merkle proof against the root.

### 4. Verifying Key-Value Data Integrity

To verify the integrity of any specific key-value pair within the Extension Block, a Merkle proof can be generated. This proof is a series of hashes that demonstrate the inclusion of the key-value pair in the Merkle Tree, leading up to the Merkle Root in the block header. By verifying this proof, clients can confirm that the data has not been tampered with, even without downloading the entire Extension Block.

### Example: Verifying a Key-Value Pair in the Extension Block

Here's an example of how to verify a key-value pair using a Merkle proof:

```scala
import scorex.crypto.authds.merkle.MerkleProof
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.util.encode.Base16

val key = "someKey".getBytes("UTF-8")
val value = "someValue".getBytes("UTF-8")
val leafHash = Blake2b256(key ++ value)

val proof = MerkleProof[Digest32](leafHash, Seq(...)) // Proof provided in the block
val root = Base16.decode("expectedMerkleRoot").get

assert(proof.valid(Digest32 @@ root))
```

In this example, the proof is validated by comparing the computed root from the proof with the expected Merkle Root stored in the block header.

## Use Cases of the Extension Block Merkle Tree

The Extension Block Merkle Tree serves several critical functions within the Ergo blockchain:

- **Miner Voting**: Securely records and verifies miner votes on protocol changes, ensuring that the results cannot be tampered with.
- **Protocol Upgrades**: Safely stores protocol parameters and upgrades, providing a transparent and immutable record of changes.
- **State Verification**: Enables efficient verification of additional state information or proofs, which can be crucial for off-chain applications or second-layer solutions.
