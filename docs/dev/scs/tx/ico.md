Another popular use case on Ethereum is an Initial Coin Offering (ICO) contract. An ICO mirrors an Initial Public Offering (IPO), providing a mechanism for a project to collect funding (often in stablecoins or the platform's native token) and then issue project "shares" (in the form of new tokens) to investors.

Generally, an ICO comprises 3 stages:

- [**Funding**](#funding): During this period, investors are allowed to fund the project.
- [**Issuance**](#issuance): A new asset token is created and issued to investors.
- [**Withdrawal**](#withdrawal): Investors can withdraw their newly issued tokens.

This example ICO contract is quite complex compared to previous examples as it involves multiple stages and parties. The number of investors might run into the thousands. A naive solution, similar to some approaches on account-based models like the [ERC-20 standard](https://theethereum.wiki/w/index.php/ERC20_Token_Standard) on Ethereum, might attempt to store all investor data directly within the contract state.

Unlike Ethereum, Ergo contracts cannot store arbitrarily large datasets directly. Instead, Ergo utilizes authenticated data structures like AVL trees. We store only a compact digest (e.g., ~33 bytes for an AvlTree) representing the root hash and state of a potentially vast (key, value) dictionary. To access or modify elements in the dictionary, a spending transaction must provide cryptographic proofs (lookup or modification proofs). This allows a contract to authenticate large datasets using very little on-chain storage.

## Funding

The project initiates the ICO by creating a box guarded by the script shown below. This initial box also contains, in its R5 register, the authenticated digest of an empty dictionary intended to store (investor PK hash, invested amount) pairs. Here, an "investor PK hash" refers to the hash of the script (typically a standard P2PK script) that will guard the box containing the investor's withdrawn ICO tokens after the funding period ends.

```scala
// check if the index of the current input is 0
val selfIndexIsZero = INPUTS(0).id == SELF.id

// get the AVL tree proof from a register
val proof = getVar[Coll[Byte]](1).get

// collect pk and value of all inputs, except for the first one
val toAdd = INPUTS.slice(1, INPUTS.size).map({(b: Box) =>
    val pk = b.R4[Coll[Byte]].get
    val value = longToByteArray(b.value)
    (pk, value)
})

// insert the collected inputs into the AVL tree, using the proof
val modifiedTree = SELF.R5[AvlTree].get.insert(toAdd, proof).get

// get the expected AVL tree from the first output
val expectedTree = OUTPUTS(0).R5[AvlTree].get

// check if the self output is correct by comparing the script
// if the current height is less than 2000, compare the script to the current box
// otherwise, compare the script to the issuance script
val selfOutputCorrect =
    if (HEIGHT < 2000) OUTPUTS(0).propositionBytes == SELF.propositionBytes
    else OUTPUTS(0).propositionBytes == issuanceScript

// check if there is only one output and if the self output is correct
val outputsCorrect = OUTPUTS.size == 1 && selfOutputCorrect

// check if the index is 0, outputs are correct, and the expected tree matches the modified tree
selfIndexIsZero && outputsCorrect && modifiedTree == expectedTree

```

The first funding transaction spends this initial box and creates a new box containing the same script but with an updated dictionary digest in R5 reflecting the first investment. Subsequent funding transactions spend the box created by the *previous* funding transaction. The script ensures that the ICO contract box is always the first input (`INPUTS(0)`). Additional inputs in the transaction represent contributions from investors. Each investor input must contain the hash of their withdrawal script (their public key hash) in register R4. The ICO script verifies (using the provided AVL tree proof) that the investor PK hashes and their corresponding investment amounts (box values) are correctly inserted into the dictionary. The script also ensures that only one output box is created, carrying forward the updated dictionary digest and the accumulated Ergs (fees are ignored in this simplified example).

During this funding stage, which lasts until block height 2,000, withdrawals are not permitted; Ergs can only be added to the ICO box. The first transaction occurring at or after height 2,000 must transition the contract to the next stage by changing the output box's script to `issuanceScript` (described next), while keeping the dictionary data (digest) the same.

## Issuance

This stage involves a single transaction to transition to the withdrawal stage. The spending transaction performs the following actions, verified by the `issuanceScript`:
1.  **Updates AVL Tree Flags**: It changes the allowed operations on the dictionary from "inserts only" to "removals only" by updating the `enabledOperations` flag in the `AvlTreeData`.
2.  **Verifies Token Issuance**: It checks that the correct amount of ICO tokens are issued. In Ergo, a transaction can issue a new token, whose ID is determined by the ID of the first input box. The `issuanceScript` verifies that a new token (with this ID) is created in the first output box (`OUTPUTS(0)`) with a total supply equal to the total nanoErgs collected during the funding stage (`SELF.value`).
3.  **Transitions to Withdrawal Script**: It ensures the output box (`OUTPUTS(0)`) containing the tokens and the dictionary digest is protected by the `withdrawScript` for the next stage.
4.  **Checks Outputs**: It verifies that the transaction has exactly two outputs: `OUTPUTS(0)` (the main contract box for the withdrawal stage) and `OUTPUTS(1)` (a box sending the collected Ergs to the project's designated address, identified by `projectPubKeyHash`).

The complete `issuanceScript` is shown below.

```scala
// Get the open and closed trees
val openTree = SELF.R5[AvlTree].get
val closedTree = OUTPUTS(0).R5[AvlTree].get

// Check that the digests, key lengths and values are the same
val correctDigest = openTree.digest == closedTree.digest
val correctKeyLength = openTree.keyLength == closedTree.keyLength
val correctValue = openTree.valueLengthOpt == closedTree.valueLengthOpt

// Check that the closed tree is a remove-only tree
val removeOnlyTree = closedTree.enabledOperations == 4

// Check that the token IDs and amounts are correct
val tokenId: Coll[Byte] = INPUTS(0).id
val tokenIssued = OUTPUTS(0).tokens(0)._2
val correctTokenNumber = OUTPUTS(0).tokens.size == 1 && OUTPUTS(1).tokens.size == 0
val correctTokenIssued = SELF.value == tokenIssued
val correctTokenId = OUTPUTS(0).R4[Coll[Byte]].get == tokenId && OUTPUTS(0).tokens(0)._1 == tokenId

// Check that the values have been preserved, the state has changed and the project public key is correct
val valuePreserved = OUTPUTS.size == 2 && correctTokenNumber && correctTokenIssued && correctTokenId
val stateChanged = OUTPUTS(0).propositionBytes == withdrawScript
val projectPubKey = SELF.R5[Coll[Byte]].get == projectPubKeyHash
val treeIsCorrect = correctDigest && correctValue && correctKeyLength && removeOnlyTree

// Check if the tree is correct, the values have been preserved and the state has changed
val stateIsCorrect = projectPubKey && treeIsCorrect && valuePreserved && stateChanged

```

## Withdrawal

Investors can now withdraw their allocated ICO tokens. The withdrawal process typically happens in batches. A withdrawal transaction spends the current ICO box (`SELF`) and creates `N + 1` outputs:
*   `OUTPUTS(0)`: The new ICO box, containing the remaining tokens and the updated dictionary digest (with withdrawn entries removed). It is protected by the same `withdrawScript`.
*   `OUTPUTS(1)` to `OUTPUTS(N)`: Boxes sent to the withdrawing investors. Each box is protected by the investor's script (whose hash was stored as the key in the dictionary) and contains the corresponding amount of ICO tokens.

The `withdrawScript` requires two AVL tree proofs provided in context variables:
1.  `lookupProof`: Proves the existence and amounts associated with the investor keys being withdrawn.
2.  `removeProof`: Proves that these investor entries have been correctly removed from the dictionary, resulting in the updated dictionary digest found in `OUTPUTS(0)`.

The complete `withdrawScript` is shown below:

```scala
// Get removeProof and lookupProof
val removeProof = getVar[Coll[Byte]](2).get
val lookupProof = getVar[Coll[Byte]](3).get

// Get withdraw indexes and tokenId
val withdrawIndexes = getVar[Coll[Int]](4).get
val tokenId: Coll[Byte] = SELF.R4[Coll[Byte]].get

// Map over withdrawIndexes and find tokenIds
val withdrawals = withdrawIndexes.map({(idx: Int) =>
    val b = OUTPUTS(idx)
    if (b.tokens(0)._1 == tokenId)
        (blake2b256(b.propositionBytes), b.tokens(0)._2)
    else
        (blake2b256(b.propositionBytes), 0L)
    })

// Get withdrawValues and calculate the total amount withdrawn
val withdrawValues = withdrawals.map({(t: (Coll[Byte], Long)) => t._2})
val total = withdrawValues.fold(0L, {(l1: Long, l2: Long) => l1 + l2 })

// Get list of nodes to remove and removed values
val toRemove = withdrawals.map({(t: (Coll[Byte], Long)) => t._1})
val initialTree = SELF.R5[AvlTree].get
val removedValues = initialTree.getMany(toRemove, lookupProof).map(
    {(o: Option[Coll[Byte]]) => byteArrayToLong(o.get)}
    )

// Check if removedValues equals withdrawValues
val valuesCorrect = removedValues == withdrawValues

// Remove nodes and check if the outTree is correct
val modifiedTree = initialTree.remove(toRemove, removeProof).get
val outTreeCorrect = OUTPUTS(0).R5[AvlTree].get == modifiedTree

// Check if the tokenIds and amounts are correct
val selfTokenCorrect = SELF.tokens(0)._1 == tokenId
val outTokenCorrect = OUTPUTS(0).tokens(0)._1 == tokenId
val outTokenCorrectAmt = OUTPUTS(0).tokens(0)._2 + total == SELF.tokens(0)._2
val tokenPreserved = selfTokenCorrect && outTokenCorrect && outTokenCorrectAmt

// Check if the SELF and OUTPUTS are correct
val selfOutputCorrect = OUTPUTS(0).propositionBytes == SELF.propositionBytes
val outTreeCorrect = OUTPUTS(0).R5[AvlTree].get == modifiedTree

// Check if everything is correct
valuesCorrect && outTreeCorrect && selfOutputCorrect && tokenPreserved
```

Note that the ICO example presented here includes several simplifications. For instance, transaction fees are not explicitly handled in the scripts (though they would be required in a real transaction).

Additionally, the contract does not include logic for self-destruction or final cleanup after the withdrawal stage is complete.

## Comet Refundable ICO

Comet has a refundable ICO live at [thecomettoken.com/ICO](https://thecomettoken.com/ICO)

The contract used is [provided](https://github.com/CometCommunity/CometCommunity/blob/main/RefundableIcoContract):

```scala
{
  // Receipt Tokens held in Contract
  val receiptTokens = SELF.tokens(0)._2
  // Comet Held in Contract
  val cometTokens = SELF.tokens(1)._2
  // Receipt Token Id
  val receiptId = fromBase58("5HWxQHyjjVFNEWtswcc71922Bq84LsmtMbgEG5eNxAKZ")
  // Comet Token Id
  val cometId = fromBase58("s9d3vUc6AhNAPZhxnGXCitQFqdAXN6X7gXT3h9GupWE")
  // Swap Price
  val amountToSwap = 15 * (OUTPUTS(0).value - SELF.value) / 100000
  // Refund Price
  val amountToRefund = 15 * (SELF.value - OUTPUTS(0).value) / 100000

  // Conditions that are always true
  val alwaysTrue = allOf(Coll(
    OUTPUTS(0).propositionBytes == SELF.propositionBytes, // OUTPUT(0) is contract box
    OUTPUTS(0).R4[Coll[Byte]].get == SELF.id, // Protect against spending two contract boxes of same value in 1 tx.
    OUTPUTS(0).tokens(0)._1 == receiptId // Contract always holds receipt tokens
  ))

  // Conditions that depend on spending action
  val conditionals = if (OUTPUTS(0).value > SELF.value) { // Purchase comet condition
    allOf(Coll(
      OUTPUTS(0).tokens(0)._2 >= receiptTokens - amountToSwap, // Unlock value amount of receipt for spending
      OUTPUTS(0).tokens(1)._1 == cometId,
      OUTPUTS(0).tokens(1)._2 >= cometTokens - amountToSwap // Unlock value amount of comet for spending
    ))
  } else { // Refund comet condition
    allOf(Coll(
      OUTPUTS(0).tokens(0)._2 >= receiptTokens + amountToRefund, // Unlock receipt amount of Erg for spending
      OUTPUTS(0).tokens(1)._1 == cometId,
      OUTPUTS(0).tokens(1)._2 >= cometTokens + amountToRefund // Unlock comet amount of Erg for spending
    ))
  }

  val drainAddressConditions = allOf(Coll(
    OUTPUTS(0).value == SELF.value,
    OUTPUTS(0).tokens(0)._2 == receiptTokens, // Cannot withdraw receipt tokens
    OUTPUTS(0).tokens(1)._1 == cometId,
    OUTPUTS(0).tokens(1)._2 >= 1 // Free up all comet
  ))

  val addFunds = alwaysTrue && allOf(Coll(
    OUTPUTS(0).value >= SELF.value,
    OUTPUTS(0).tokens(0)._2 == receiptTokens, // Cannot withdraw receipt tokens
    OUTPUTS(0).tokens(1)._1 == cometId,
    OUTPUTS(0).tokens(1)._2 >= SELF.tokens(1)._2,
    OUTPUTS.size == 2 // Requires setup such that no change Box is made
  ))

  // Define the spending conditions for draining the address
  val drainAddress = sigmaProp(alwaysTrue && drainAddressConditions && PK("9h6Ao31CVSsYisf4pWTM43jv6k3BaXV3jovGfaRj9PrqfYms6Rf"))
  // Define the spending conditions before the deadline
  val beforeDeadline = sigmaProp(alwaysTrue && conditionals)
  // Define the spending conditions after the deadline
  val afterDeadline = sigmaProp(PK("9h6Ao31CVSsYisf4pWTM43jv6k3BaXV3jovGfaRj9PrqfYms6Rf") && HEIGHT > 1550468)

  // Combine all spending conditions using logical OR
  sigmaProp(beforeDeadline || afterDeadline || drainAddress || addFunds)
}
```
