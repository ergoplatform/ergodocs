---
tags:
    - Merkle
---

# Example: Lite Client Checking Merkle Proof

In the Ergo blockchain, Merkle Trees are utilized for efficient and secure verification of transactions within a block. This capability is especially useful in scenarios where a lightweight client, such as a decentralized pool, needs to verify that a specific transaction is included in a block without having to download the entire blockchain.

This page provides a comprehensive example of how a lite client can check a Merkle-tree-based membership proof against an incomplete header, which lacks a full proof-of-work (PoW) solution. This method can be particularly valuable for decentralized mining pools with collateral, where the pool checks shares from miners to ensure that a corresponding block contains a specific transaction, such as one that pays out to the pool.

### Use Case

Consider a scenario where a miner submits a share to a decentralized pool. The share includes:

- A block header without a PoW solution
- A partial PoW solution
- A Merkle proof demonstrating that a transaction is included in the block

The pool needs to verify the following:

1. The header, when combined with the partial PoW solution, meets the required difficulty level.
2. The Merkle proof accurately proves that the transaction is included in the block.

### Steps to Verify a Merkle Proof

The following steps outline the process a lite client (such as a decentralized pool) would use to verify a share submitted by a miner:

1. **Transaction Creation**:
     - The miner creates a transaction that pays out to the pool and includes it in a block candidate.

2. **Mining Process**:
     - The miner attempts to mine the block. If successful, the miner posts the transaction to the network. If the miner's partial PoW solution does not meet the full difficulty for a block but is sufficient for a share, the miner can submit the share to the pool.

3. **Share Components**:
     - The share submitted to the pool consists of:
         - The block header without the PoW solution (`msgPreimage`).
         - The partial PoW solution.
         - The Merkle proof that the transaction is included in the block.

4. **Verification by the Pool**:
     - The pool verifies the validity of the share by:
         1. Checking that the combination of `msgPreimage` and the partial PoW solution forms a valid block header with sufficient difficulty.
         2. Using the Merkle proof to verify that the transaction is indeed included in the block.

### Example Code

The following code demonstrates how to perform step 4b: verifying that a transaction is included in the block header using a Merkle proof.

```scala
package org.ergoplatform.examples

import org.ergoplatform.utils.ErgoPropertyTest
import scorex.crypto.authds.merkle.MerkleProof
import scorex.crypto.authds.{LeafData, Side}
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.util.encode.Base16

class LiteClientExamples extends ErgoPropertyTest {

    property("Example client code for tx proof") {
        implicit val hashFn: Blake2b256.type = Blake2b256

        // The msgPreimage is the block header without the PoW solution
        val msgPreimageBase16 = "01fb9e35f8a73c128b73e8fde5c108228060d68f11a69359ee0fb9bfd84e7ecde6d19957ccbbe75b075b3baf1cac6126b6e80b5770258f4cec29fbde92337faeec74c851610658a40f5ae74aa3a4babd5751bd827a6ccc1fe069468ef487cb90a8c452f6f90ab0b6c818f19b5d17befd85de199d533893a359eb25e7804c8b5d7514d784c8e0e52dabae6e89a9d6ed9c84388b228e7cdee09462488c636a87931d656eb8b40f82a507008ccacbee05000000"
        val msgPreimage = Base16.decode(msgPreimageBase16).get

        // The hash of msgPreimage should be equal to the msg value
        val msg = "6cb37d0a202bc2984f43de003cbc5558804db45798d0fc8faae7390b96d42d15"
        assert(Base16.encode(hashFn(msgPreimage)) == msg)

        // Extract the transactions Merkle root from the msgPreimage
        val txsRoot = msgPreimage.slice(65, 97)

        // The txId represents the leaf node in the Merkle tree
        val txId = "642c15c62553edd8fd9af9a6f754f3c7a6c03faacd0c9b9d5b7d11052c6c6fe8"

        // Merkle proof encoded as a sequence of bytes
        val levelsEncoded = Seq("0139b79af823a92aa72ced2c6d9e7f7f4687de5b5af7fab0ad205d3e54bda3f3ae")
        val levels = levelsEncoded.map { le =>
            val leBytes = Base16.decode(le).get
            val side: Byte = leBytes.head
            val digest = leBytes.tail
            (Digest32 @@ digest, Side @@ side)
        }

        // Construct the Merkle proof using the leaf data and levels
        val merkleProof = MerkleProof[Digest32](LeafData @@ Base16.decode(txId).get, levels)

        // Validate the Merkle proof against the transactions root
        assert(merkleProof.valid(Digest32 @@ txsRoot))
    }
}
```

### Explanation of the Code

- **msgPreimage**: The block header without the PoW solution is called `msgPreimage`. The header hash (`msg`) is computed from `msgPreimage`.
- **txsRoot**: The Merkle root of the transactions included in the block is extracted from `msgPreimage`.
- **txId**: This represents the transaction ID that needs to be verified.
- **Merkle Proof Levels**: The proof consists of the `txId` and the hashes of the intermediate nodes in the Merkle Tree (`levels`). Each level indicates whether the computed value is on the left or right of the sibling node.
- **Verification**: The proof is validated by recalculating the Merkle root from the `txId` and comparing it with `txsRoot`.

### Conclusion

This example demonstrates how to verify that a specific transaction is included in a block using a Merkle proof in the context of a lite client. By following the steps outlined above, decentralized mining pools or other lightweight clients can efficiently validate transactions without downloading the entire blockchain. This approach not only reduces the computational burden but also ensures the integrity and security of the blockchain.

For further details, explore the [LiteClientExamples.scala](https://github.com/ergoplatform/ergo/blob/85dfd1a39700ef4ff6a45766fc103e624873f652/src/test/scala/org/ergoplatform/examples/LiteClientExamples.scala#L11) in the Ergo GitHub repository.