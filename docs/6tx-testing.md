# Testing 6.0 Specific Transactions Against 5.x and 6.0 Nodes

With the release of Ergo 6.0.0-alpha0, developers have the opportunity to explore and test new protocol features before they are widely deployed. This guide provides comprehensive instructions on how to test 6.0-specific transactions against both 5.x and 6.0 nodes, ensuring compatibility and smooth network upgrades.

## New Features Introduced in Ergo 6.0

Ergo 6.0 introduces several new features and enhancements to the ErgoScript language and the broader protocol. Below is a summary of these new features:

1. **Enhanced Cryptographic Operations**:

   - New opcodes for advanced cryptographic functions, such as multi-signatures and hash-based operations.
   - Example: A new opcode for verifying BLS signatures.

2. **Improved Serialization Mechanisms**:

   - More efficient serialization formats for ErgoTree, reducing the size and improving the speed of transactions.

3. **Expanded Opcodes and Script Constructs**:

   - Introduction of new opcodes to support complex smart contract logic.
   - Example: New operations for handling complex data structures like AVL trees.

4. **New Script Validation Rules**:

   - Enhanced validation rules to support the new features while maintaining backward compatibility with 5.x scripts.

### ErgoScript Code Examples

Here are some examples of ErgoScript code utilizing the new features introduced in Ergo 6.0:

#### Example 1: Using BLS Signature Verification

```scala
{
  val pubKey = decodePoint("04308e09...") // BLS public key
  val sig = decodeByteArray("30450221...") // BLS signature
  val msg = decodeByteArray("48656c6c...") // Message in bytes

  // Verify BLS signature
  pubKey.isValidBLS(sig, msg)
}
```

This script verifies a BLS signature, a feature introduced in Ergo 6.0, making it possible to work with new cryptographic primitives within contracts.

#### Example 2: Handling AVL Trees

```scala
{
  val tree = AVLTree.load("e8a32...") // Load an AVL tree
  val proof = decodeByteArray("123abc...") // Proof of a certain operation

  // Verify a proof against the AVL tree
  tree.verifyProof(proof)
}
```

This script demonstrates how to handle AVL trees, which can be used to maintain authenticated data structures directly in Ergo smart contracts.

## Setting Up the Testing Environment

### Step 1: Establish a Development Network (DevNet)

To perform comprehensive tests, you should set up a private DevNet where 6.0 features are pre-activated.

1. **Download the 6.0.0-alpha0 JAR** from the [official release page](https://github.com/ergoplatform/ergo/releases/tag/v6.0.0-alpha0).

2. **Create a DevNet Configuration**: Use the provided sample configuration as a template to create your own `devnet.conf` file. Refer to the Gist [DevNet Config Example](https://gist.github.com/kushti/4f9c6b706ab16fcf2151cf1f3b531f7d).

3. **Launch the Node with 6.0 Activation**: Start the Ergo node with the following command:
   ```bash
   java -jar -Xmx4G ergo-6.0.0-alpha0.jar --devnet -c devnet.conf
   ```

### Step 2: Set Up 5.x Nodes

To test backward compatibility, you will also need to run a node using the 5.x protocol version. Download and set up a 5.x node following similar steps as above, ensuring you have a configuration tailored for your test network.

## Writing and Submitting 6.0 Specific Transactions

### Step 1: Create ErgoScript with 6.0 Features

Use the new features in ErgoScript 6.0 to write scripts that incorporate enhanced cryptographic operations, improved serialization, and new opcodes.

### Step 2: Compile and Submit Transactions

1. **Compile with 6.0 Features**: Use the `/script/p2sAddress` API method on your 6.0 node to compile ErgoScript code that utilizes 6.0 features.

2. **Submit to 6.0 Node (Pre-Activation on Public Network)**: On a public testnet that hasn’t yet activated 6.0 features, expect transactions with 6.0-specific features to be rejected.

3. **Submit to 6.0 Node (Post-Activation on DevNet)**: On your private DevNet, where 6.0 is already activated, submit the transaction and verify its acceptance.

4. **Submit to 5.x Node**: Submit the transaction to a 5.x node and confirm that it is rejected, ensuring backward compatibility is maintained.

## Testing Compatibility Across Versions

### Scenario 1: Testing Transactions with 6.0 Features on 5.x Nodes

Ensure that transactions containing 6.0 features are **not** accepted by 5.x nodes. This is crucial for maintaining backward compatibility and preventing issues before the soft fork activates on public networks.

### Scenario 2: Testing Pre-6.0 Transactions on 6.0 Nodes

Submit transactions that use only pre-6.0 features to your DevNet where 6.0 is active. Verify that these transactions are accepted and processed correctly, ensuring that the introduction of 6.0 features does not break existing functionality.

### Scenario 3: Comprehensive Post-Activation Testing on DevNet

Once 6.0 features are activated on your DevNet, test a variety of transactions (both pre-6.0 and 6.0-specific). Verify that all transactions behave as expected according to the protocol rules.

## Example Test Cases

### Test Case 1: 6.0 Feature Transaction on DevNet

- **Step 1**: Create an ErgoScript using a new opcode introduced in 6.0.
- **Step 2**: Compile the script and create a transaction using it.
- **Step 3**: Submit the transaction to your DevNet (6.0 activated) and verify acceptance.
- **Step 4**: Submit the same transaction to a 5.x node and verify rejection.

### Test Case 2: Mixed Transaction

- **Step 1**: Create a transaction containing both pre-6.0 and 6.0 features.
- **Step 2**: Test the transaction on a 6.0 DevNet and ensure it is processed correctly.
- **Step 3**: Submit the transaction to a 5.x node and confirm it is rejected.

### Test Case 3: Legacy Transaction on 6.0 Node

- **Step 1**: Create a transaction using only features available in 5.x.
- **Step 2**: Submit the transaction to both 5.x and 6.0 nodes (pre- and post-activation) to ensure it is accepted in all scenarios.

## Conclusion

Testing 6.0 specific transactions against both 5.x and 6.0 nodes is crucial for ensuring a smooth protocol upgrade and maintaining compatibility across versions. By following the steps outlined in this guide and utilizing the new features in ErgoScript 6.0, you can prepare for the transition to Ergo 6.0, ensuring that applications and smart contracts continue to function as expected.

For further details on each feature, refer to the pull requests mentioned in the [6.0.0-alpha0 release notes](https://github.com/ergoplatform/ergo/releases/tag/v6.0.0-alpha0).