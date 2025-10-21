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

#### Example submission commands

```bash
# Attempt to broadcast a 6.0 transaction to a 5.x node (expected rejection)
curl -s -o /tmp/tx-5x-response.json -w "HTTP %{http_code}\n" -H "Content-Type: application/json" --data @tx-6.0.json http://localhost:9053/transactions && cat /tmp/tx-5x-response.json
```

- **Expected result:** An `HTTP 400` status with an error payload indicating why the transaction was rejected (for example, `InvalidErgoTreeVersion` or `Script reduced to false`).

```bash
# Broadcast the same transaction to a 6.0 devnet node (expected acceptance)
curl -s -o /tmp/tx-60-response.json -w "HTTP %{http_code}\n" -H "Content-Type: application/json" --data @tx-6.0.json http://localhost:9055/transactions && cat /tmp/tx-60-response.json
```

- **Expected result:** An `HTTP 200` status and a JSON body containing the accepted transaction ID, for example `{ "id": "<txId>" }`.

```bash
# Verify whether the transaction is sitting in the 6.0 node mempool
txId=$(jq -r '.id' /tmp/tx-60-response.json)
curl -I http://localhost:9055/transactions/unconfirmed/$txId
```

- **Expected result:** An `HTTP 200` header while the transaction remains unconfirmed, or `HTTP 404` once it has been mined or dropped.

## Testing Compatibility Across Versions

### Scenario 1: Testing Transactions with 6.0 Features on 5.x Nodes

Ensure that transactions containing 6.0 features are **not** accepted by 5.x nodes. This is crucial for maintaining backward compatibility and preventing issues before the soft fork activates on public networks.

1. Run the rejection command above against your 5.x node and confirm it returns `HTTP 400`.
2. Inspect `/tmp/tx-5x-response.json` for an error payload that references the ErgoTree version or script failure reason.
3. Optionally issue `curl -I http://localhost:9053/transactions/unconfirmed/$txId` (using the ID from your 6.0 response) to confirm the transaction never entered the legacy node mempool.

### Scenario 2: Testing Pre-6.0 Transactions on 6.0 Nodes

Submit transactions that use only pre-6.0 features to your DevNet where 6.0 is active. Verify that these transactions are accepted and processed correctly, ensuring that the introduction of 6.0 features does not break existing functionality.

1. Broadcast a pre-6.0 transaction to the 6.0 devnet node and expect an `HTTP 200` response with a transaction ID.
2. Query `curl -I http://localhost:9055/transactions/unconfirmed/$txId` to ensure the transaction is tracked until it is mined.
3. Cross-check `curl -s http://localhost:9055/transactions/unconfirmed` to verify the payload lists your transaction with the anticipated inputs and outputs.

### Scenario 3: Comprehensive Post-Activation Testing on DevNet

Once 6.0 features are activated on your DevNet, test a variety of transactions (both pre-6.0 and 6.0-specific). Verify that all transactions behave as expected according to the protocol rules.

- Alternate between the 5.x and 6.0 submission commands to document exactly which transactions are accepted or rejected.
- Record the HTTP status codes and response bodies as evidence in your test plan.
- After mining, confirm the transactions appear via `curl -s http://localhost:9055/blocks/{headerId}/transactions` and that no unexpected rejections appear in the node logs.

## Example Test Cases

### Test Case 1: 6.0 Feature Transaction on DevNet

- **Step 1**: Create an ErgoScript using a new opcode introduced in 6.0.
- **Step 2**: Compile the script and create a transaction using it.
- **Step 3**: Submit the transaction to your DevNet (6.0 activated) with the acceptance command above and ensure you receive `HTTP 200` plus a transaction ID.
- **Step 4**: Submit the same transaction to a 5.x node using the rejection command and record the resulting `HTTP 400` payload.

### Test Case 2: Mixed Transaction

- **Step 1**: Create a transaction containing both pre-6.0 and 6.0 features.
- **Step 2**: Test the transaction on a 6.0 DevNet, expecting `HTTP 200` and a mempool entry for the transaction ID.
- **Step 3**: Submit the transaction to a 5.x node and capture the rejection payload for your report.

### Test Case 3: Legacy Transaction on 6.0 Node

- **Step 1**: Create a transaction using only features available in 5.x.
- **Step 2**: Submit the transaction to both 5.x and 6.0 nodes (pre- and post-activation) and confirm each responds with `HTTP 200`.

## Conclusion

Testing 6.0 specific transactions against both 5.x and 6.0 nodes is crucial for ensuring a smooth protocol upgrade and maintaining compatibility across versions. By following the steps outlined in this guide and utilizing the new features in ErgoScript 6.0, you can prepare for the transition to Ergo 6.0, ensuring that applications and smart contracts continue to function as expected.

For further details on each feature, refer to the pull requests mentioned in the [6.0.0-alpha0 release notes](https://github.com/ergoplatform/ergo/releases/tag/v6.0.0-alpha0).
