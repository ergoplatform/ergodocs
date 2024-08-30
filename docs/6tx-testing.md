# Testing 6.0 Specific Transactions Against 5.x and 6.0 Nodes

With the release of Ergo 6.0.0-alpha0, developers can begin testing new features specific to the 6.0 protocol version. However, to ensure backward compatibility and a smooth transition during the soft-fork process, it is essential to validate that transactions using 6.0 features are accepted by both 5.x and 6.0 nodes. This document provides a detailed guide on how to perform these tests and ensure compatibility across versions.

## Why Test 6.0 Specific Transactions?

When introducing new protocol features, it's crucial to verify that:

1. **Backward Compatibility**: Transactions utilizing new features are accepted by 5.x nodes up to the point where the soft fork activates.
2. **Forward Compatibility**: Transactions using only 5.x features continue to be valid and accepted by 6.0 nodes.
3. **Soft-Fork Transition**: Ensure that the transition from 5.x to 6.0 occurs smoothly, without any disruptions or unexpected behavior.

## Setting Up the Testing Environment

### Step 1: Set Up a Development Network (DevNet)

Since version 6.0.0-alpha0 is intended for developer networks, you will need to set up a private DevNet environment to perform these tests.

1. **Download the 6.0.0-alpha0 JAR** from the [official release page](https://github.com/ergoplatform/ergo/releases/tag/v6.0.0-alpha0).

2. **Create a DevNet Configuration**: Use the provided sample configuration as a template to create your own `devnet.conf` file. You can use the following Gist as a reference: [DevNet Config Example](https://gist.github.com/kushti/4f9c6b706ab16fcf2151cf1f3b531f7d).

3. **Launch the Node**: Start the Ergo node with the following command:
   ```bash
   java -jar -Xmx4G ergo-6.0.0-alpha0.jar --devnet -c devnet.conf
   ```

4. **Activate Block Generation**: Unlock the wallet to start block generation. Note that although block generation starts with Autolykos2 by default, the activation of 6.0 features still requires manual unlocking.

5. **Wait for Activation**: The new 6.0 protocol features will become active after 768 blocks (256 + 32 * 16).

### Step 2: Set Up 5.x Nodes

To test compatibility, you will also need to run a node using the 5.x protocol version. Download and set up a 5.x node following similar steps as above, ensuring you have a configuration tailored for your test network.

## Writing and Submitting 6.0 Specific Transactions

### Step 1: Create ErgoScript with 6.0 Features

6.0 introduces several new features to ErgoScript. Some of these include:

- Enhanced cryptographic operations
- Improved serialization mechanisms
- New opcodes for complex scripts

You can find ErgoScript code examples for these features in the following pull requests:

- [ScorexFoundation/sigmastate-interpreter#962](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/962)

- [ScorexFoundation/sigmastate-interpreter#969](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/969)

- [ScorexFoundation/sigmastate-interpreter#968](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/968)

- [ScorexFoundation/sigmastate-interpreter#979](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/979)

- [ScorexFoundation/sigmastate-interpreter#989](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/989)

- [ScorexFoundation/sigmastate-interpreter#1008](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/1008)

### Step 2: Compile and Submit Transactions

Use the `/script/p2sAddress` API method on your 6.0 node to compile ErgoScript code that utilizes 6.0 features. After compiling the script, construct and submit transactions as follows:

1. **Submit to 5.x Node**: Submit the transaction to a node running the 5.x protocol and observe the behavior. The transaction should be rejected if it contains 6.0 specific features.

2. **Submit to 6.0 Node Before Activation**: Before the 6.0 activation height is reached, submit the transaction to the 6.0 node. The transaction should also be rejected as the new features are not yet active.

3. **Submit to 6.0 Node After Activation**: Once the 6.0 features are activated, resubmit the transaction to the 6.0 node. The transaction should now be accepted and processed.

## Testing Compatibility Across Versions

### Scenario 1: Testing Transactions with 6.0 Features on 5.x Nodes

Ensure that transactions containing 6.0 features are **not** accepted by 5.x nodes. This is important for ensuring that the new features do not cause any unexpected behavior in older nodes before the soft fork activates.

### Scenario 2: Testing Pre-6.0 Transactions on 6.0 Nodes

Submit transactions that use only pre-6.0 features to a 6.0 node. Verify that these transactions are accepted and processed correctly, ensuring that backward compatibility is maintained.

### Scenario 3: Post-Activation Testing

After the 6.0 features are activated on the 6.0 node, submit various transactions (both pre-6.0 and 6.0 specific). Verify that all transactions are processed correctly according to their respective protocol rules.

## Example Test Cases

### Test Case 1: Simple Transaction with 6.0 Feature

- **Step 1**: Create an ErgoScript using a new opcode introduced in 6.0.
- **Step 2**: Compile the script and create a transaction using it.
- **Step 3**: Submit the transaction to a 5.x node and verify rejection.
- **Step 4**: Submit the transaction to a 6.0 node before activation and verify rejection.
- **Step 5**: Submit the transaction to a 6.0 node after activation and verify acceptance.

### Test Case 2: Mixed Transaction

- **Step 1**: Create a transaction containing both pre-6.0 and 6.0 features.
- **Step 2**: Test the transaction across both 5.x and 6.0 nodes as in Test Case 1.
- **Step 3**: Ensure that the transaction is accepted only after the 6.0 activation on the 6.0 node.

### Test Case 3: Legacy Transaction

- **Step 1**: Create a transaction using only features available in 5.x.
- **Step 2**: Submit the transaction to both 5.x and 6.0 nodes, before and after the 6.0 activation.
- **Step 3**: Ensure that the transaction is accepted in all scenarios.

## Conclusion

Testing 6.0 specific transactions against both 5.x and 6.0 nodes is crucial for ensuring a smooth protocol upgrade and maintaining compatibility across versions. By following the steps outlined in this guide, developers can confidently prepare for the transition to Ergo 6.0, ensuring that their applications and smart contracts continue to function correctly.

Always refer to the latest documentation and release notes for updates on new features and potential changes to the testing process as the Ergo protocol evolves.