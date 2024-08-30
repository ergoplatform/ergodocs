# Using Merkle Batch Proofs on Ergo

## Overview

While full support for Merkle Trees and Batch Proofs is available in the `sigma-rust` library, which is extensively used in Rust-based Ergo applications, integration into the core JVM-based `sigmastate-interpreter` for direct use within ErgoScript remains in progress. There is an open issue in the `sigmastate-interpreter` repository to support Merkle Trees natively, which would allow for direct handling of static data within ErgoScript, enhancing efficiency in various blockchain operations, such as proof-of-transaction and securing extension block data.

Until this feature is fully integrated into `sigmastate-interpreter`, developers working in JVM-based environments can leverage `scrypto`, which provides essential cryptographic functionalities, including Merkle Tree management and Batch Proof generation and verification.

For more details on the ongoing integration efforts, you can refer to the [GitHub issue #296](https://github.com/ergoplatform/ergo/issues/296) in the Ergo repository.

Now, let's delve into the practical steps of using Merkle Batch Proofs in Ergo.

## Using Sigma-Rust for Rust-based Applications

The `sigma-rust` library provides comprehensive tools to create, manage, and verify Merkle Batch Proofs in Rust-based Ergo applications. Below is a step-by-step guide with code examples.

#### Step 1: Setting Up the Environment

Before you begin working with Merkle Batch Proofs in `sigma-rust`, ensure your environment is properly set up:

1. **Clone the Sigma-Rust Repository**:
   ```bash
   git clone https://github.com/ergoplatform/sigma-rust.git
   cd sigma-rust
   ```

2. **Install Rust**: 
   Follow the instructions on [rust-lang.org](https://www.rust-lang.org/tools/install) to install Rust if you haven't done so.

3. **Build the Project**:
   ```bash
   cargo build
   ```

#### Step 2: Creating a Merkle Tree

First, create a Merkle tree using the `MerkleTree` structure provided by the `sigma-rust` library.

```rust
use sigma_merkle_tree::merkletree::MerkleTree;
use sigma_merkle_tree::MerkleNode;

fn create_merkle_tree() {
    let data_1 = [1u8; 32];
    let data_2 = [2u8; 32];
    let data_3 = [3u8; 32];

    let node_1 = MerkleNode::from_bytes(data_1);
    let node_2 = MerkleNode::from_bytes(data_2);
    let node_3 = MerkleNode::from_bytes(data_3);

    let tree = MerkleTree::new(vec![node_1, node_2, node_3]);
    println!("Merkle Root: {:?}", tree.root_hash());
}
```

**Code Reference**: The `MerkleTree` structure is implemented in the [`merkletree.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-merkle-tree/src/merkletree.rs) file.

#### Step 3: Generating a Batch Merkle Proof

Once the Merkle tree is created, you can generate a batch Merkle proof for specific leaves. This proof can be used to verify the inclusion of multiple elements.

```rust
use sigma_merkle_tree::batchmerkleproof::BatchMerkleProof;

fn generate_batch_merkle_proof(tree: &MerkleTree) {
    let proof = tree.proof_by_indices(&[0, 2]).unwrap();
    println!("Batch Merkle Proof: {:?}", proof);
}
```

**Code Reference**: The `BatchMerkleProof` structure and its methods are implemented in the [`batchmerkleproof.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-merkle-tree/src/batchmerkleproof.rs) file.

#### Step 4: Verifying the Batch Merkle Proof

The generated proof can be verified against the Merkle root to ensure that the specified leaves are indeed part of the tree.

```rust
fn verify_batch_merkle_proof(tree: &MerkleTree, proof: &BatchMerkleProof) {
    assert!(proof.valid(tree.root_hash().as_ref()));
    println!("Proof is valid.");
}
```

#### Step 5: Serialization and Deserialization

Merkle batch proofs can be serialized and deserialized for storage or transmission, which is crucial for many blockchain applications where proofs are shared between nodes or stored for future verification.

```rust
use sigma_ser::ScorexSerializable;

fn serialize_and_deserialize_proof(proof: &BatchMerkleProof) {
    let serialized_proof = proof.scorex_serialize_bytes().unwrap();
    let deserialized_proof = BatchMerkleProof::scorex_parse_bytes(&serialized_proof).unwrap();
    
    assert_eq!(proof, &deserialized_proof);
    println!("Serialization and deserialization successful.");
}
```

## Using Scrypto for JVM-based Applications

For JVM-based applications, `scrypto` provides similar functionalities to `sigma-rust`. It works closely with the `sigmastate-interpreter` to handle cryptographic operations, including Merkle Trees and Batch Proofs.

#### Step 1: Setting Up the Environment

To work with `scrypto`, follow these steps:

1. **Clone the Scrypto Repository**:
   ```bash
   git clone https://github.com/input-output-hk/scrypto.git
   cd scrypto
   ```

2. **Ensure Scala and SBT Are Installed**: 
   You can install Scala and SBT by following the instructions on [scala-lang.org](https://www.scala-lang.org/download/).

3. **Build the Project**:
   ```bash
   sbt compile
   ```

#### Step 2: Creating a Merkle Tree

The Merkle Tree can be constructed using the `MerkleTree` class in Scrypto, similarly to how it's done in Rust.

```scala
import scorex.crypto.authds.merkle.MerkleTree
import scorex.crypto.authds.LeafData
import scorex.crypto.hash.Blake2b256

implicit val hf = Blake2b256

val leafData = Seq.fill(5)(LeafData @@ scorex.utils.Random.randomBytes(32))
val tree = MerkleTree(leafData)
println(s"Merkle Root: ${hf.encode(tree.rootHash)}")
```

**Code Reference**: The `MerkleTree` class is implemented in the [`MerkleTree.scala`](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/merkle/MerkleTree.scala) file.

#### Step 3: Generating a Batch Merkle Proof

In Scrypto, you can generate a batch Merkle proof by specifying the indices of the leaves you want to prove.

```scala
import scorex.crypto.authds.merkle.{BatchMerkleProof, Leaf}

val batchProof = tree.proofByIndices(Seq(0, 2)).get
println(s"Batch Merkle Proof: $batchProof")
```

**Code Reference**: The `BatchMerkleProof` class and its methods are implemented in the [`BatchMerkleProof.scala`](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/merkle/BatchMerkleProof.scala) file.

#### Step 4: Verifying the Batch Merkle Proof

You can then verify the generated proof to ensure that the elements are part of the Merkle tree.

```scala
val isValid = batchProof.valid(tree.rootHash)
println(s"Batch Merkle Proof is valid: $isValid")
```

#### Step 5: Serialization and Deserialization

To serialize and deserialize the proof, Scrypto provides dedicated classes and methods, ensuring the proof can be efficiently stored or transmitted.

```scala
import scorex.crypto.authds.merkle.serialization.BatchMerkleProofSerializer

val serializer = new BatchMerkleProofSerializer[Digest32, Blake2b256.type]
val serializedProof = serializer.serialize(batchProof)
val deserializedProof = serializer.deserialize(serializedProof).get

assert(batchProof == deserializedProof)
println("Serialization and deserialization successful.")
```

**Code Reference**: The `BatchMerkleProofSerializer` class is implemented in the [`BatchMerkleProofSerializer.scala`](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/merkle/serialization/BatchMerkleProofSerializer.scala) file.

### Example: End-to-End Workflow in Scrypto

Here’s an example tying together all the steps in Scrypto:

```scala
import scorex.crypto.authds.merkle.{MerkleTree, Leaf, BatchMerkleProof}
import scorex.crypto.authds.merkle.serialization.BatchMerkleProofSerializer
import scorex.crypto.hash.Blake2b256
import scorex.crypto.hash.Digest32

implicit val hf = Blake2b256

// Create the Merkle tree
val leafData = Seq.fill(5)(LeafData @@ scorex.utils.Random.randomBytes(32))
val tree = MerkleTree(leafData)

// Generate the batch Merkle proof
val batchProof = tree.proofByIndices(Seq(0, 2)).get

// Verify the proof
val isValid = batchProof.valid(tree.rootHash)
println(s"Batch Merkle Proof is valid: $isValid")

// Serialize and deserialize the proof
val serializer = new BatchMerkleProofSerializer[Digest32, Blake2b256.type]
val serializedProof = serializer.serialize(batchProof)
val deserializedProof = serializer.deserialize(serializedProof).get

assert(batchProof == deserializedProof)
println("Serialization and deserialization successful.")
```