# AVL Trees in Ergo

AVL trees are highly efficient authenticated data structures that provide native support in Ergo. These trees offer several benefits, including the ability to authenticate data properties without accessing the entire dataset. This page provides an overview of AVL trees, their integration with Ergo, and their performance characteristics.

## AVL Trees in Ergo

Ergo incorporates AVL trees to enhance the security and efficiency of various applications. These authenticated dictionary data structures enable verification and updates without relying on trust in the prover. By reducing the length of modification proofs and minimizing storage requirements for verification, AVL trees establish a robust foundation for maintaining data integrity in the Ergo ecosystem.

## Integration with Ergo: GetBlok Plasma

Developers can seamlessly integrate AVL trees into their Ergo applications using the [GetBlok Plasma](plasma.md) library, built on top of Ergo Appkit. This library simplifies the integration process by providing an abstraction layer that facilitates the incorporation of AVL trees (also known as Plasma) into off-chain code. It offers developers an easy way to leverage AVL trees as a Layer-2 scaling solution in smart contracts, off-chain code, and distributed systems managing the Plasma infrastructure.

## Proof Size and Efficiency

The compact proof sizes of AVL trees contribute to their efficiency. AVL trees in Ergo demonstrate concise and effective authentication proofs, ensuring efficient storage and verification processes within the Ergo blockchain.

### Single Operation Proof Size

![Single Operation Proof Size](../../assets/img/avl/single_op_proof.png)

The figure above illustrates the proof size for a single operation.

### Multiple Operations Proof Size

![Multiple Operations Proof Size](../../assets/img/avl/multiple_op_proof.png)

The figure above showcases the proof size for multiple operations.

## Time for Validation and Verification

AVL trees in Ergo exhibit excellent performance in validation and verification processes. The verification time is optimized, enabling fast and efficient authentication of data. This efficient validation process contributes to the overall performance and scalability of Ergo applications.

### Validation Time

![Validation Time](../../assets/img/avl/validation_time.png)

The figure above displays the time required for validation of AVL trees.

By leveraging AVL trees, developers can enhance the security, efficiency, and scalability of their Ergo projects.

For further details, please refer to the [Improving authenticated dynamic dictionaries, with applications to cryptocurrencies](https://eprint.iacr.org/2016/994.pdf) paper.