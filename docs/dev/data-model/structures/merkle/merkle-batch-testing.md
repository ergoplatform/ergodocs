---
tags:
  - Merkle
---

# Testing Merkle Batch Proofs

Testing Merkle Batch Proofs is crucial to ensure the correctness of their implementation in the Ergo blockchain. This section provides examples of how to write tests for Merkle Batch Proofs using both Rust (`sigma-rust`) and Scala (`scrypto`). These tests cover the creation, verification, serialization, and deserialization of batch Merkle proofs.

### Rust (`sigma-rust`) Testing

In Rust, the `sigma-rust` library provides the necessary tools to create and test Merkle Batch Proofs. Below is a series of tests written using the Rust testing framework.

```rust
#[cfg(test)]
mod tests {
    use sigma_merkle_tree::merkletree::MerkleTree;
    use sigma_merkle_tree::MerkleNode;
    use sigma_merkle_tree::batchmerkleproof::BatchMerkleProof;
    use sigma_ser::ScorexSerializable;
    use blake2::Blake2b256;

    #[test]
    fn test_merkle_tree_creation() {
        let data_1 = [1u8; 32];
        let data_2 = [2u8; 32];
        let data_3 = [3u8; 32];

        let node_1 = MerkleNode::from_bytes(data_1);
        let node_2 = MerkleNode::from_bytes(data_2);
        let node_3 = MerkleNode::from_bytes(data_3);

        let tree = MerkleTree::new(vec![node_1, node_2, node_3]);
        assert!(tree.root_hash().is_some(), "Merkle tree root hash should be generated");
    }

    #[test]
    fn test_batch_merkle_proof_generation() {
        let data_1 = [1u8; 32];
        let data_2 = [2u8; 32];
        let data_3 = [3u8; 32];

        let node_1 = MerkleNode::from_bytes(data_1);
        let node_2 = MerkleNode::from_bytes(data_2);
        let node_3 = MerkleNode::from_bytes(data_3);

        let tree = MerkleTree::new(vec![node_1, node_2, node_3]);
        let proof = tree.proof_by_indices(&[0, 2]).unwrap();

        assert_eq!(proof.indices.len(), 2, "Batch proof should include two indices");
    }

    #[test]
    fn test_batch_merkle_proof_verification() {
        let data_1 = [1u8; 32];
        let data_2 = [2u8; 32];
        let data_3 = [3u8; 32];

        let node_1 = MerkleNode::from_bytes(data_1);
        let node_2 = MerkleNode::from_bytes(data_2);
        let node_3 = MerkleNode::from_bytes(data_3);

        let tree = MerkleTree::new(vec![node_1, node_2, node_3]);
        let proof = tree.proof_by_indices(&[0, 2]).unwrap();

        assert!(proof.valid(tree.root_hash().as_ref()), "Merkle proof should be valid");
    }

    #[test]
    fn test_batch_merkle_proof_serialization_deserialization() {
        let data_1 = [1u8; 32];
        let data_2 = [2u8; 32];
        let data_3 = [3u8; 32];

        let node_1 = MerkleNode::from_bytes(data_1);
        let node_2 = MerkleNode::from_bytes(data_2);
        let node_3 = MerkleNode::from_bytes(data_3);

        let tree = MerkleTree::new(vec![node_1, node_2, node_3]);
        let proof = tree.proof_by_indices(&[0, 2]).unwrap();

        let serialized_proof = proof.scorex_serialize_bytes().unwrap();
        let deserialized_proof = BatchMerkleProof::scorex_parse_bytes(&serialized_proof).unwrap();

        assert_eq!(proof, deserialized_proof, "Deserialized proof should match the original");
    }
}
```

#### Code References

- **MerkleTree**: [`merkletree.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-merkle-tree/src/merkletree.rs)
- **BatchMerkleProof**: [`batchmerkleproof.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-merkle-tree/src/batchmerkleproof.rs)
- **Serialization Methods**: [`scorex_serializable.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/sigma-ser/src/scorex_serializable.rs)


### Scala (`scrypto`) Testing

For Scala, the `scrypto` library is used to test Merkle Batch Proofs. Below are the test cases using ScalaTest, covering tree creation, proof generation, verification, and serialization.

```scala
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import scorex.crypto.authds.merkle.{MerkleTree, BatchMerkleProof}
import scorex.crypto.authds.merkle.serialization.BatchMerkleProofSerializer
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.utils.Random

class MerkleBatchProofSpec extends AnyFlatSpec with Matchers {
  implicit val hf = Blake2b256

  "Merkle Tree" should "be created correctly" in {
    val leafData = Seq.fill(3)(Random.randomBytes(32)) // Generate random leaf data
    val tree = MerkleTree(leafData.map(Digest32 @@ _)) // Create a Merkle Tree

    tree.rootHash should not be null
  }

  "Batch Merkle Proof" should "be generated correctly" in {
    val leafData = Seq.fill(3)(Random.randomBytes(32)) // Generate random leaf data
    val tree = MerkleTree(leafData.map(Digest32 @@ _)) // Create a Merkle Tree

    val proof = tree.proofByIndices(Seq(0, 2)).get // Generate batch proof for elements at index 0 and 2
    proof.indices.length shouldEqual 2
  }

  it should "verify correctly" in {
    val leafData = Seq.fill(3)(Random.randomBytes(32)) // Generate random leaf data
    val tree = MerkleTree(leafData.map(Digest32 @@ _)) // Create a Merkle Tree

    val proof = tree.proofByIndices(Seq(0, 2)).get // Generate batch proof for elements at index 0 and 2
    proof.valid(tree.rootHash) shouldBe true // Verify the proof against the tree's root hash
  }

  it should "serialize and deserialize correctly" in {
    val leafData = Seq.fill(3)(Random.randomBytes(32)) // Generate random leaf data
    val tree = MerkleTree(leafData.map(Digest32 @@ _)) // Create a Merkle Tree

    val proof = tree.proofByIndices(Seq(0, 2)).get // Generate batch proof for elements at index 0 and 2
    val serializer = new BatchMerkleProofSerializer[Digest32, Blake2b256.type] // Serializer for BatchMerkleProof

    val serializedProof = serializer.serialize(proof) // Serialize the proof
    val deserializedProof = serializer.deserialize(serializedProof).get // Deserialize the proof

    proof shouldEqual deserializedProof // Check that the original and deserialized proofs are equal
  }
}
```

#### Code References

- **MerkleTree**: [`MerkleTree.scala`](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/merkle/MerkleTree.scala)
- **BatchMerkleProof**: [`BatchMerkleProof.scala`](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/merkle/BatchMerkleProof.scala)
- **BatchMerkleProofSerializer**: [`BatchMerkleProofSerializer.scala`](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/merkle/serialization/BatchMerkleProofSerializer.scala)

### Explanation:  

- **Merkle Tree Creation**: The test generates random leaf data and creates a `MerkleTree`. This ensures that the tree is correctly constructed and the root hash is generated.
- **Batch Merkle Proof Generation**: The test creates a batch proof for selected elements (indices 0 and 2) of the Merkle Tree.
- **Proof Verification**: The test verifies the validity of the generated batch proof against the Merkle root, ensuring the proof correctly represents the inclusion of those elements in the tree.
- **Serialization and Deserialization**: The test checks the ability to serialize a batch proof, then deserialize it back to its original form, confirming the integrity of the proof after these operations.

These tests collectively ensure that the core functionality of Merkle Batch Proofs in `scrypto` operates correctly, providing developers with confidence in using this library for cryptographic proofs in their applications.