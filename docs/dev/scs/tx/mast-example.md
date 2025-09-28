---
tags:
  - ErgoScript
  - Smart Contracts
  - MAST
  - Merkleized Abstract Syntax Trees
  - Tutorial
  - Advanced
  - Multi-Stage Contracts
  - executeFromVar
  - Merkle Proof
---
# Tutorial: Merkleized Abstract Syntax Trees (MAST) in Ergo

Merkleized Abstract Syntax Trees (MAST) are a technique used in blockchain protocols to improve privacy and efficiency for complex smart contracts with multiple spending conditions. Instead of revealing the entire contract script when spending, MAST allows revealing only the specific condition (script branch) that was actually met and proving its inclusion in the original set of conditions.

## Concept

Imagine a contract with several possible ways it can be spent:

*   Condition A: Alice can spend after time T1.
*   Condition B: Bob can spend if he provides a secret value X.
*   Condition C: Alice and Bob can spend together anytime.

Traditionally, the entire script containing all these conditions would be stored in the box's `propositionBytes`. When spending, the whole script is evaluated, revealing all possible spending paths.

With MAST:
1.  Each condition (A, B, C) is treated as a separate script fragment.
2.  These fragments are serialized to their [ErgoTree](../ergotree.md) byte representation (`Coll[Byte]`).
3.  Each byte representation is hashed (e.g., using `blake2b256`).
4.  These hashes are arranged as leaves in a [Merkle Tree](merkle-tree.md).
5.  The **Merkle root** of this tree is calculated and stored in the main locking script of the box (often as a constant).

The locking script essentially says: "This box can be spent if you provide:
1.  A specific script fragment (`scriptBytes`).
2.  A Merkle proof (`merkleProof`) demonstrating that `blake2b256(scriptBytes)` is a valid leaf within the Merkle tree whose root is `expectedMerkleRoot`.
3.  Data (context variables, signatures, etc.) that satisfies the execution of the provided `scriptBytes`."

## Visual Representation

```mermaid
graph TD
    A[Root Hash] --> B[Hash of (Hash A + Hash B)]
    A --> C[Hash of (Hash C + Hash D)]
    B --> D1[Hash A (Alice Spend)]
    B --> E1[Hash B (Bob Spend)]
    C --> F1[Hash C (Timelock)]
    C --> G1[Hash D (Multisig)]
    
    style D1 fill:#f9f,stroke:#333,stroke-width:2px
    style E1 fill:#bbf,stroke:#333,stroke-width:2px
    style F1 fill:#bfb,stroke:#333,stroke-width:2px
    style G1 fill:#fbf,stroke:#333,stroke-width:2px
```
*The Merkle Root (A) commits to all possible spending conditions (leaves).*

When spending using Alice's condition (Hash A), only the necessary path needs to be revealed:

```mermaid
graph TD
    A[Root Hash] --> B[Hash of (Hash A + Hash B)]
    A --> C[Hash C - Provided in Proof]
    B --> D1[Hash A (Alice Spend)]
    B --> E1[Hash B - Provided in Proof]
    
    style A fill:#afa,stroke:#333,stroke-width:2px
    style B fill:#afa,stroke:#333,stroke-width:2px
    style D1 fill:#afa,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style E1 fill:#bbf,stroke:#333,stroke-width:2px

    subgraph Revealed On-Chain
        A
        B
        D1
        AliceScriptBytes["Alice's Script Bytes (getVar[0])"]
    end
    subgraph Provided in Proof "(getVar[1])"
        C
        E1
        ProofPositions["Proof Positions (getVar[2])"]
    end

    AliceScriptBytes -->|blake2b256| D1
```
*Only Alice's script bytes and the sibling hashes (E1, C) needed to reconstruct the root are revealed.*

## Benefits

*   **Privacy:** Only the executed spending condition is revealed on-chain. Unused conditions remain hidden.
*   **Efficiency:** Smaller on-chain footprint for the main locking script (just the root hash). Validation cost can be lower if the executed branch is simple, though Merkle proof verification adds overhead.
*   **Scalability:** Allows for contracts with a very large number of potential conditions without making the base script excessively large or complex.

## Comparison: Traditional vs. MAST Execution

| Aspect           | Traditional Script                     | MAST-based Execution                     |
| :--------------- | :------------------------------------- | :--------------------------------------- |
| Privacy          | All conditions visible on-chain        | Only used condition revealed             |
| Script Size      | Full script stored on-chain            | Only Merkle root stored on-chain         |
| Execution Cost   | Evaluates potentially complex script   | Verifies proof + Evaluates simple branch |
| Complexity Limit | Limited by practical script size/cost  | Can support many conditions              |
| Implementation   | Straightforward ErgoScript             | Requires off-chain prep + proof logic    |
| Security         | Direct script validation               | Requires proper Merkle proof verification|

## ErgoScript MAST Example (with Proof Verification)

This example demonstrates the core on-chain logic using context variables to receive the script branch and its Merkle proof.

```scala
{
  // Merkle root of all possible spending conditions (calculated off-chain)
  // This would typically be embedded as a constant in the script
  val merkleRoot = SELF.R4[Coll[Byte]].get // Example: Get root from R4

  // Context variable 0: The specific spending script bytes being executed
  val providedScriptBytes = getVar[Coll[Byte]](0).getOrElse(Coll[Byte]()) 
  
  // Context variable 1: The Merkle proof (sibling hashes)
  val merkleProof = getVar[Coll[Coll[Byte]]](1).getOrElse(Coll[Coll[Byte]]()) 
  
  // Context variable 2: The positions of sibling hashes (0 for left, 1 for right)
  val proofPositions = getVar[Coll[Byte]](2).getOrElse(Coll[Byte]())

  // Hash the provided script to get the leaf hash
  val leafHash = blake2b256(providedScriptBytes)
  
  // --- Merkle Proof Verification Logic ---
  // (Simplified helper function - real implementation might be more complex/optimized)
  // Assumes 'verifyMerkleProof' takes root, leaf, proof, positions and returns Boolean
  val proofIsValid = verifyMerkleProof(merkleRoot, leafHash, merkleProof, proofPositions)
  // --- End Merkle Proof Verification ---

  // If the proof is valid, execute the provided script fragment
  // The script fragment itself should return SigmaProp
  val spendingCondition = if (proofIsValid) {
    executeFromVar[SigmaProp](0) // Execute script from context variable 0
  } else {
    sigmaProp(false) // Proof invalid, reject
  }
  
  spendingCondition
}

// --- Helper Function (Conceptual - Needs careful implementation/testing) ---
// This function would need to be defined within the script scope or 
// potentially made available via context extension or future built-ins.
def verifyMerkleProof(root: Coll[Byte], leaf: Coll[Byte], proof: Coll[Coll[Byte]], positions: Coll[Byte]): Boolean = {
  // Basic check for consistent proof/position lengths
  if (proof.size != positions.size) {
      false
  } else {
      // Start with the leaf hash
      val currentHash = proof.fold(leaf, { (h: Coll[Byte], i: Int) => 
          val proofElement = proof(i)
          val position = positions(i)
          
          // Combine current hash with proof element based on position
          if (position == 0) { // proofElement is on the right
              blake2b256(h ++ proofElement)
          } else { // proofElement is on the left
              blake2b256(proofElement ++ h)
          }
      })
      // Check if the calculated root matches the expected root
      currentHash == root
  }
}
```
*(Note: The `verifyMerkleProof` function shown is conceptual and simplified. Real-world implementations require careful handling of edge cases and potential optimizations. Currently, complex proof verification directly in ErgoScript can be costly.)*

## Practical Implementation Steps (Off-Chain)

The setup for MAST happens off-chain before creating the box locked by the MAST script.

1.  **Define & Compile Conditions:**
    ```scala
    // Using Ergo's AppKit (Scala Example)
    import org.ergoplatform.appkit._
    import scorex.crypto.hash.Blake2b256
    import scorex.utils.ByteArray

    val alicePk = prover.getP2PKAddress.pubkey // Get Alice's public key
    val bobPk = ... // Get Bob's public key

    // Define spending conditions as ErgoScript strings
    val aliceSpendScript = s"{ proveDlog(alicePk) }"
    val bobSpendScript = s"{ proveDlog(bobPk) }"
    val timelockScript = s"{ HEIGHT > 100000 }"

    // Compile scripts to ErgoTree bytes using BlockchainContext (ctx)
    val aliceBytes = ctx.compileContract(ConstantsBuilder.create().item("alicePk", alicePk).build(), aliceSpendScript).getErgoTree.bytes
    val bobBytes = ctx.compileContract(ConstantsBuilder.create().item("bobPk", bobPk).build(), bobSpendScript).getErgoTree.bytes
    val timelockBytes = ctx.compileContract(ConstantsBuilder.empty(), timelockScript).getErgoTree.bytes
    ```

2.  **Build Merkle Tree:**
    ```scala
    // Hash each condition's ErgoTree bytes
    val hashAlice = Blake2b256.hash(aliceBytes)
    val hashBob = Blake2b256.hash(bobBytes)
    val hashTimelock = Blake2b256.hash(timelockBytes)

    // Use a Merkle Tree library (conceptual - replace with actual library usage)
    // Example: val tree = MerkleTree.build(Seq(hashAlice, hashBob, hashTimelock))
    // val merkleRoot: Array[Byte] = tree.rootHash 
    val merkleRoot: Array[Byte] = ??? // Calculate the root hash
    ```

3.  **Create MAST Box:**
    ```scala
    // Embed the Merkle Root, e.g., in R4
    val mastContract = ctx.compileContract(ConstantsBuilder.empty(), """
      {
        val expectedRoot = SELF.R4[Coll[Byte]].get 
        // ... rest of MAST verification script from above ... 
        verifyMerkleProof(expectedRoot, blake2b256(getVar[Coll[Byte]](0).get), getVar[Coll[Coll[Byte]]](1).get, getVar[Coll[Byte]](2).get) &&
        executeFromVar[SigmaProp](0)
      }
    """)

    val boxValue = 1000000L // 0.001 ERG
    val outBox = txBuilder.outBoxBuilder()
      .value(boxValue)
      .contract(mastContract)
      .registers(ErgoValue.of(merkleRoot)) // Store root in R4
      .build()
    ```

4.  **Spending Transaction (Off-Chain Prep):**
    ```scala
    // When spending using Alice's condition:
    val chosenConditionBytes = aliceBytes
    // val proof = tree.getProofForLeaf(hashAlice) // Generate Merkle proof (hashes and positions)
    val proofHashes: Seq[Array[Byte]] = ??? 
    val proofPositions: Array[Byte] = ??? // 0 for right sibling, 1 for left

    // Prepare context variables
    val contextVars = Seq(
        new ContextVar(0.toByte, ErgoValue.of(chosenConditionBytes)),
        new ContextVar(1.toByte, ErgoValue.of(proofHashes.map(ErgoValue.of).toArray, ErgoType.collType(ErgoType.collType(ErgoType.byteType())))),
        new ContextVar(2.toByte, ErgoValue.of(proofPositions))
    )

    // Build the transaction using the MAST box as input and providing contextVars
    val unsignedTx = txBuilder
        .boxesToSpend(Seq(mastInputBox))
        .outputs(...)
        .fee(...)
        .withContextVars(contextVars:_*) // Pass context variables
        .sendChangeTo(...)
        .build()

    // Sign the transaction (requires Alice's key for the executed script)
    val signedTx = prover.sign(unsignedTx) 
    ```

## Security Considerations

1.  **Merkle Proof Verification:** The on-chain script **must** correctly and completely verify the provided Merkle proof against the expected root hash. The `verifyMerkleProof` example above is simplified; a robust implementation is crucial. Without proper verification, an attacker could provide arbitrary script bytes and bypass the intended logic.
2.  **Script Execution:** Ensure `executeFromVar` is only called *after* the Merkle proof is successfully verified.
3.  **Context Variable Indices:** Use distinct and well-defined indices for context variables (`getVar`, `executeFromVar`) to avoid collisions or unintended data access.
4.  **Gas Costs:** Verifying Merkle proofs on-chain consumes computational resources and increases transaction fees. Optimize proof verification logic or consider patterns where verification is minimized.
5.  **Off-Chain Security:** The process of generating the Merkle tree, calculating the root, and generating proofs for spending must be secure and correct off-chain.

## Merkleized Finite State Machines (MFSMs)

The MAST concept can be combined with [Finite State Machines (FSMs)](fsm-example.md) for complex multi-stage contracts:

1.  **State Transitions as Branches:** Each possible state transition logic in an FSM can be represented as a separate script branch in a Merkle tree.
2.  **Implementation Pattern:** The main contract box stores the current FSM state identifier (e.g., in R4) and the Merkle root of all possible state *transition scripts*. To transition, the spender provides the specific transition script bytes and its Merkle proof via context variables. The main script verifies the proof and then uses `executeFromVar` to run the transition script, which validates the state change (e.g., checks `INPUTS(0).R4` vs `OUTPUTS(0).R4`).
3.  **Benefits:** Allows complex FSMs without revealing all possible states and transitions on-chain, enhancing privacy and potentially reducing on-chain script size.

## Resources & Examples

*   **Specifications in `sigmastate-interpreter`:**
    *   [`MASTExampleSpecification.scala`](https://github.com/ergoplatform/sigmastate-interpreter/blob/develop/sigmastate/src/test/scala/sigmastate/utxo/examples/MASTExampleSpecification.scala): Provides Scala code demonstrating MAST concepts in a testing context.
*   **Related Primitives:**
    *   [Context Extension (`getVar`, `executeFromVar`)](lang-spec.md#PredefinedFunctions)
    *   [Register Execution (`executeFromSelfReg`)](lang-spec.md#box-type)
*   **Conceptual Docs:**
    *   [Merkle Trees](../../data-model/structures/merkle/merkle-tree.md)

Implementing MAST securely requires careful design of both the on-chain verification script and the off-chain preparation steps (tree generation, proof creation).
