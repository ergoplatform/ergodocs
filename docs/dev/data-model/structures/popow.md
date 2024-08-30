# Proof of Proof-of-Work (PoPow) Data Structures in Ergo

## Overview

Proof of Proof-of-Work (PoPow) is an advanced protocol that enables lightweight clients to securely and efficiently verify that a blockchain follows the longest chain rule without downloading the entire blockchain. This is particularly important for resource-constrained devices, such as mobile phones or IoT devices, where downloading and storing the entire blockchain is impractical.

The PoPow protocol is built on top of several key data structures that facilitate this efficient verification process. This documentation page provides an in-depth look at these data structures, how they interact, and their roles within the PoPow protocol.

## Key Data Structures in PoPow

The PoPow protocol relies on a combination of interlink vectors, NiPoPoW proofs, and Merkle trees to achieve its goals. Each of these data structures plays a specific role in enabling efficient verification of the blockchain's integrity.

1. [**Interlink Vectors**](interlink-vectors.md):
      - **Purpose**: Interlink vectors store references to previous block headers at different difficulty levels. They allow lightweight clients to verify the blockchain's integrity by checking only a subset of blocks, rather than the entire chain.
      - **Structure**: An interlink vector is an array where each element points to a previous block header. The level of each element is determined by the number of leading zeros in the block's hash, corresponding to the difficulty level of that block.
      - **Usage**: Interlink vectors are updated as new blocks are added to the blockchain, ensuring that the latest blocks are always accessible for verification. They are particularly useful in scenarios where quick and efficient chain validation is needed.
      - **Code Reference**: [InterlinkVector.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/popow/InterlinkVector.scala)

2. [**NiPoPoW (Non-Interactive Proof of Proof-of-Work) Proofs**](nipopows.md):
      - **Purpose**: NiPoPoW proofs allow a lightweight client to verify that a given chain is the correct one (i.e., the chain with the most cumulative work) without interacting with the blockchain network.
      - **Structure**: A NiPoPoW proof consists of a sequence of block headers from the blockchain, including interlink references and proof chains. The proof chain includes blocks that represent a certain amount of work, with a gap between them that ensures the inclusion of the most important blocks.
      - **Usage**: NiPoPoW proofs are used by clients to verify that a blockchain adheres to the longest chain rule by checking the work done on the chain. They reduce the amount of data that needs to be processed while maintaining a high level of security.
      - **Code Reference**: [NipopowProof.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/popow/NipopowProof.scala)
3. [**Merkle Trees**](merkle-tree.md):
      - **Purpose**: Merkle trees are used to efficiently verify the inclusion of specific data elements (such as transactions or block headers) in a larger dataset. In the context of PoPow, Merkle trees help verify that the interlink vectors and other components of the PoPow proof are correctly formed.
      - **Structure**: A Merkle tree is a binary tree where each leaf node is a hash of a block of data, and each non-leaf node is a hash of its child nodes. The root of the tree, known as the Merkle root, serves as a cryptographic commitment to the entire dataset.
      - **Usage**: In PoPow, Merkle trees are used to generate Merkle proofs that verify the inclusion of specific blocks or headers in the chain. These proofs are then included in the NiPoPoW proof to provide lightweight clients with the necessary evidence to trust the blockchain's integrity.
      - **Code Reference**: [Extension.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/extension/Extension.scala)

## Interaction Between Data Structures

The PoPow protocol leverages the interaction between interlink vectors, NiPoPoW proofs, and Merkle trees to provide a comprehensive solution for lightweight blockchain verification. Here's how these data structures work together:

1. **Interlink vectors** are generated and updated as new blocks are mined. These vectors provide references to important block headers at different difficulty levels, allowing clients to quickly identify and verify the most relevant parts of the blockchain.

2. **NiPoPoW proofs** are constructed using the interlink vectors and the chain of block headers. These proofs include a carefully selected subset of block headers that represent the chain's cumulative work, along with the interlink references needed to verify the chain's integrity.

3. **Merkle trees** are used to create cryptographic proofs that verify the inclusion of specific data elements, such as block headers or interlink references, in the PoPow proof. These Merkle proofs are included in the NiPoPoW proof, providing clients with a compact and secure way to verify the blockchain.

The combination of these data structures ensures that the PoPow protocol is both secure and efficient, enabling lightweight clients to participate in the blockchain network without requiring extensive resources.

## Example: Constructing a NiPoPoW Proof

Here is a step-by-step overview of how a NiPoPoW proof is constructed using the PoPow data structures:

1. **Collect Block Headers**:
      - A set of block headers is selected from the blockchain, representing different points in the chain with varying difficulty levels. These headers are chosen based on the work they represent and their relevance to the chain's integrity.

2. **Build the Interlink Vector**:
      - The interlink vector is constructed by referencing the selected block headers. Each element in the vector points to a block header with a specific difficulty level, ensuring that the proof covers the entire chain.

3. **Generate Merkle Proofs**:
      - Merkle proofs are generated for the selected block headers and interlink references. These proofs ensure that the data elements included in the proof are valid and can be verified by the client.

4. **Assemble the NiPoPoW Proof**:
      - The block headers, interlink vector, and Merkle proofs are assembled into a NiPoPoW proof. This proof is then sent to the client, who can use it to verify the blockchain's integrity.

5. **Verification by the Client**:
      - The client verifies the NiPoPoW proof by checking the Merkle proofs and ensuring that the interlink vector correctly references the block headers. If the proof is valid, the client can trust that the blockchain follows the longest chain rule.

## Conclusion

The PoPow protocol is a powerful tool for enabling secure and efficient blockchain verification by lightweight clients. By leveraging interlink vectors, NiPoPoW proofs, and Merkle trees, PoPow provides a scalable solution for verifying the integrity of the blockchain without requiring extensive resources.

Developers working with the Ergo blockchain should familiarize themselves with these data structures and their interactions to effectively implement and utilize PoPow in their applications. As the Ergo ecosystem continues to grow, PoPow and its associated data structures will play a crucial role in maintaining the security and scalability of the network.