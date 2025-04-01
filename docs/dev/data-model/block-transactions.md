---
tags:
  - Block
  - Transactions
  - Data Model
---

# Block Transactions

*(Back to: [Block Overview](block.md))*

The Transactions section of an Ergo [block](block.md) is the heart of the blockchain's state changes. It contains a list of all the [transactions](transactions.md) that are included and validated within that specific block. These transactions define how [tokens](eip4.md) and assets are transferred and how the overall state of the Ergo blockchain evolves.

/// details | In the right place?
    {type: info, open: true}
This page covers the structure of the transactions section within an Ergo block. For more general information on transactions, see the [Transaction Overview](transactions.md) page.
///
## Function

* **Value Transfer:** Ergo transactions enable users to transfer ERG (Ergo's native token) and other custom [tokens](eip4.md)/assets to other users on the network.
* **State Transition:** Each transaction consumes existing [unspent boxes](box.md) (which hold tokens and assets) and creates new boxes with potentially modified values and ownership. This process updates the state of the [UTXO set](eutxo.md).
* **[Smart Contract](ergoscript.md) Execution:** Transactions can trigger the execution of [scripts](ergoscript.md) within boxes, allowing for complex logic and decentralized applications to be implemented on the Ergo blockchain.

## Structure

The core structure of an Ergo transaction is defined by the `ErgoTransaction` class in [ErgoTransaction.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/mempool/ErgoTransaction.scala).

Here's a breakdown of its main components:

* **inputs:** A list of `Input` objects, each referencing an existing [box](box.md) that the transaction will spend. Each input includes a `spendingProof` (see [Transaction Signing](signing.md)) to prove the spender has the right to consume the box.
* **[dataInputs](read-only-inputs.md):** A list of `DataInput` objects referencing boxes that the transaction needs to access for its scripts but won't spend. These provide data to the scripts without requiring ownership.
* **outputCandidates:** A list of `ErgoBoxCandidate` objects representing the new boxes that the transaction will create. These candidates define the values, assets, and scripts of the new boxes.

## Validation

Ergo transactions undergo rigorous [validation](validation.md) to ensure they are legitimate and maintain the integrity of the blockchain:

* **Stateless Validation:** Checks that don't require accessing the blockchain state, including:
    * Ensuring the transaction has inputs and outputs.
    * Verifying basic rules (no negative values, unique inputs, etc.).
* **Stateful Validation:** Requires accessing the blockchain state to check:
    * Whether the inputs refer to valid and unspent boxes.
    * Whether the spending proofs are correct.
    * Whether the transaction adheres to rules related to assets, [fees](min-fee.md), and block size limits.
    * Whether the scripts in the inputs are satisfied (using the `ErgoInterpreter` - see [ErgoTree Evaluation](evaluation.md)).

## Key Concepts

* **[Boxes](box.md):** The fundamental building blocks of Ergo's [UTXO model](eutxo.md). They are containers that hold ERG, other tokens, and scripts (smart contracts).
* **[Scripts](ergoscript.md):** Programs written in [ErgoScript](ergoscript.md) (a powerful scripting language) that define the conditions for spending boxes.
* **Spending Proofs:** Cryptographic proofs that demonstrate the spender has the right to use the funds in a box, often involving [signatures](signing.md) or more complex [cryptographic protocols](sigma.md).
* **Context Extension:** A key-value map attached to a spending proof, providing additional data that can be used by scripts during validation. See [Blockchain Context](blockchain-context.md).
