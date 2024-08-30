# Interlink Vectors in Ergo

## Overview

Interlink vectors are a crucial component in the Proof-of-Proof-of-Work (PoPow) protocol, which allows lightweight clients to verify the correctness of the blockchain without needing to download and validate the entire chain. These vectors store references to previous block headers at varying heights, forming a hierarchical structure that supports efficient validation and compression of blockchain data.

Interlink vectors enable clients to follow the longest chain rule and verify that a blockchain follows this rule with minimal resource requirements. This documentation provides an overview of the structure, purpose, and implementation of interlink vectors in the Ergo blockchain.

## Purpose of Interlink Vectors

In a blockchain, each block contains a reference to the previous block, forming a linked chain. However, in some cases, particularly in lightweight clients, it is impractical to download and validate every block. Interlink vectors address this by storing references to previous blocks in a way that allows the verification of the chain's integrity without requiring access to the entire blockchain.

Interlink vectors are used in conjunction with Merkle trees and PoPow proofs to create a scalable and secure method for verifying the longest chain. They are particularly valuable for lightweight clients, such as mobile or IoT devices, where storage and processing power are limited.

## Structure of Interlink Vectors

An interlink vector is essentially an array of block headers. Each element in the array points to a previous block header at a certain level of the chain. The levels are defined by the number of leading zeros in the block’s hash, which corresponds to the difficulty level of the block.

For example, the first element in the vector might point to a block with a single leading zero in its hash, the second to a block with two leading zeros, and so on. This structure allows for the efficient verification of the chain, as only a subset of blocks needs to be checked to confirm that the chain is valid.

The key properties of interlink vectors are:

- **Efficiency**: They enable the verification of the longest chain with minimal data.
- **Scalability**: They allow lightweight clients to participate in the blockchain without needing to download the entire chain.
- **Security**: They ensure that the chain being followed adheres to the longest chain rule.

## Implementation in Ergo

Interlink vectors are implemented in the Ergo blockchain as part of the PoPow protocol. They are stored in the block headers and updated with each new block added to the chain. The vector is constructed by recursively hashing previous block headers, starting from the genesis block.

The steps for implementing and using interlink vectors in Ergo are as follows:

1. **Creating the Interlink Vector**:
    - When a new block is mined, its hash is calculated.
    - The number of leading zeros in the hash determines the level of the block in the interlink vector.
    - The block header is added to the vector at the corresponding level.

2. **Updating the Interlink Vector**:
    - As new blocks are added to the chain, the interlink vector is updated by adding references to the new block headers.
    - If a block at a higher level (i.e., with more leading zeros) is found, it replaces the reference to the previous block at that level in the vector.

3. **Verifying the Chain with Interlink Vectors**:
    - To verify the correctness of the chain, a client only needs to check the blocks referenced in the interlink vector.
    - The client can confirm that the chain follows the longest chain rule by verifying that each block in the vector adheres to the difficulty level required for that position in the vector.

4. **Batch Merkle Proofs and Interlink Vectors**:
    - Interlink vectors are often used in conjunction with batch Merkle proofs to provide efficient and secure verification.
    - A batch Merkle proof allows the client to verify multiple elements in the interlink vector simultaneously, reducing the computational overhead.

## Example Usage

Consider a scenario where a lightweight client wants to verify the blockchain up to a certain height. The client can download the interlink vector from the latest block and check the references to previous blocks at each level. By verifying the Merkle proofs for these references, the client can confirm that the chain is valid without downloading the entire chain.

Here’s an example of how the interlink vector might be used in practice:

```rust
use sigma_merkle_tree::batchmerkleproof::BatchMerkleProof;
use sigma_merkle_tree::merkletree::MerkleTree;
use sigma_merkle_tree::MerkleNode;

fn verify_interlink_vector(tree: &MerkleTree, proof: &BatchMerkleProof) {
    // Verify the Merkle proof for the interlink vector
    assert!(proof.valid(tree.root_hash().as_ref()));
    println!("Interlink vector is valid.");
}
```

In this example, the client generates a batch Merkle proof for the interlink vector and verifies it against the Merkle root of the blockchain. This process ensures that the interlink vector is correctly formed and that the blockchain follows the longest chain rule.
