---
tags:
  - Merkle
owner: docs
last_reviewed: 2026-09-22
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala
  - repo: ergoplatform/scrypto
    branch: master
    paths:
      - shared/src/main/scala/scorex/crypto/authds/merkle/BatchMerkleProof.scala
      - shared/src/main/scala/scorex/crypto/authds/merkle/MerkleProof.scala
      - shared/src/main/scala/scorex/crypto/authds/merkle/Node.scala
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala
  - https://github.com/ergoplatform/scrypto/tree/master/shared/src/main/scala/scorex/crypto/authds/merkle/BatchMerkleProof.scala
---

# Validation of Merkle Proofs in Ergo

## Overview

Merkle proofs are fundamental to ensuring the integrity of data within a blockchain. By validating a Merkle proof, you can confirm that a specific piece of data, such as a transaction, is included in a block without having to download the entire blockchain. This document outlines the detailed process for validating Merkle proofs in Ergo, using cryptographic hash functions and a structured approach.

## Validation Process

The validation process involves computing a series of hashes based on the provided proof elements and comparing the final result with the expected Merkle root. The steps below describe this process in detail:

### 1. Compute the Leaf Node Hash

Begin by computing the hash of the leaf node, which represents the transaction or data element you want to prove is included in the block. In transaction roots, the leaf data is a 32-byte transaction ID for initial block versions. For later block versions, transaction IDs and witness IDs are both included as separate leaves. A witness ID commits to the serialized spending proofs.

The Merkle implementation uses `Blake2b256` to hash a **1-byte zero prefix** followed by the leaf data. The leaf position is not hashed.

**Code Implementation**: The leaf node hash computation is implemented within the Ergo codebase, primarily found in the `scorex.crypto.authds.merkle` package of the [Scrypto](https://github.com/ergoplatform/scrypto) library, which is used by Ergo.

```scala
val leafData = Base16.decode(txId).get
val leafHash = Blake2b256(0.toByte +: leafData)
```

For node-side transaction roots, use the same block version as the block being verified. From protocol version 6.0 onward, transaction parsing and serialization are performed inside the matching `VersionContext`; proofs built against differently serialized transaction bytes will not validate against the block header root.

### 2. Iterate Through the Proof

The proof consists of multiple levels, each providing information about the position of the node within the Merkle tree and its sibling hash. For each level, the following steps are performed:

- **Check the 1-Byte Side Marker**:
  - If the side marker is `0`, this indicates that the computed hash from the previous step should be on the left side.
  - If the side marker is `1`, this indicates that the computed hash should be on the right side.

- **Compute the Hash for the Next Level**:
  - Use the side marker to order the computed hash and sibling hash. Prepend the internal-node prefix `0x01`, then hash the result using `Blake2b256`. The side marker is not the hash prefix.

**Code Implementation**: The iteration process and validation logic are crucial for verifying the correctness of the Merkle proof. This is implemented in the [MerkleProof.scala](https://github.com/ergoplatform/scrypto/blob/85863595fa2d59cffc207b94d6d7393d3011da6c/shared/src/main/scala/scorex/crypto/authds/merkle/MerkleProof.scala#L26-L37) file in the `scrypto` repository.

The following fragment uses a local example representation: each hex string contains a side byte followed by a sibling digest. This is not the batch-proof wire format.

```scala
val levels = Seq("0139b79af823a92aa72ced2c6d9e7f7f4687de5b5af7fab0ad205d3e54bda3f3ae")
val computedHash = levels.foldLeft(leafHash) { case (hash, level) =>
    val bytes = Base16.decode(level).get
    val side = bytes.head
    val siblingHash = bytes.tail

    val concatenated = if (side == 0.toByte) {
        hash ++ siblingHash
    } else {
        siblingHash ++ hash
    }

    Blake2b256(1.toByte +: concatenated)
}
```

### 3. Compare with Merkle Root

Obtain the expected root from a validated block header or another authenticated source. After iterating through all levels of the proof, the final computed hash should be compared with the expected Merkle root value. If the hashes match, the proof is valid, confirming that the transaction or data element is included in the block.

**Code Implementation**: The comparison of the computed hash with the expected Merkle root is the final step in the validation process. This ensures that the entire proof is correct and that the data has not been tampered with.

```scala
assert(computedHash.sameElements(expectedMerkleRoot))
```

### Flowchart of Merkle Proof Validation

The following flowchart visualizes the Merkle proof validation process described above:

```mermaid
graph TD
        A[Compute Leaf Node Hash] --> B{Check Side Marker}
        B --> |Side is 0| C[Concatenate 0x01, Computed Hash, Sibling Hash]
        B --> |Side is 1| D[Concatenate 0x01, Sibling Hash, Computed Hash]
        C --> E[Hash the Result using Blake2b256]
        D --> E[Hash the Result using Blake2b256]
        E --> F{Next Level?}
        F --> |Yes| B
        F --> |No| G[Compare Final Hash with Merkle Root]
```

## Example: Validating a Transaction's Inclusion in a Block

Here is a concrete example of how to validate a Merkle proof for a transaction included in an Ergo block header:

**Code Implementation**: This example demonstrates how to validate a transaction's inclusion in a block using a Merkle proof. The code is based on the structures and functions provided in the [Scrypto](https://github.com/ergoplatform/scrypto) library and the Ergo codebase.

```scala
import scorex.crypto.authds.merkle.MerkleProof
import scorex.crypto.authds.{LeafData, Side}
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.util.encode.Base16

implicit val hashFn: Blake2b256.type = Blake2b256

val txId = "642c15c62553edd8fd9af9a6f754f3c7a6c03faacd0c9b9d5b7d11052c6c6fe8"
val msgPreimage = Base16.decode("01fb9e35f8a73c128b73e8fde5c108228060d68f11a69359ee0fb9bfd84e7ecde6d19957ccbbe75b075b3baf1cac6126b6e80b5770258f4cec29fbde92337faeec74c851610658a40f5ae74aa3a4babd5751bd827a6ccc1fe069468ef487cb90a8c452f6f90ab0b6c818f19b5d17befd85de199d533893a359eb25e7804c8b5d7514d784c8e0e52dabae6e89a9d6ed9c84388b228e7cdee09462488c636a87931d656eb8b40f82a507008ccacbee05000000").get

val txsRoot = msgPreimage.slice(65, 97)
val leafHash = Blake2b256(0.toByte +: Base16.decode(txId).get)

val levelsEncoded = Seq("0139b79af823a92aa72ced2c6d9e7f7f4687de5b5af7fab0ad205d3e54bda3f3ae")
val levels = levelsEncoded.map { le =>
    val leBytes = Base16.decode(le).get
    val side: Byte = leBytes.head
    val digest = leBytes.tail
    (Digest32 @@ digest, Side @@ side)
}

val merkleProof = MerkleProof[Digest32](LeafData @@ Base16.decode(txId).get, levels)
assert(merkleProof.valid(Digest32 @@ txsRoot))
```

## Conclusion

Validating Merkle proofs is a crucial process that ensures data integrity and enables efficient verification without the need to download the entire blockchain. By understanding and implementing this process in Ergo, you can enhance the security and efficiency of your blockchain applications.

### Source References

- **[Scrypto: Merkle Proofs Implementation](https://github.com/ergoplatform/scrypto)**: This repository contains the core cryptographic components used in Ergo, including the implementation of Merkle proofs.
- **[Ergo: BlockTransactions.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/BlockTransactions.scala)**: Provides the logic for handling transactions within a block, including Merkle Tree construction and proof validation.
