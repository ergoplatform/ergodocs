---
tags:
  - ErgoScript
  - Smart Contracts
  - FSM
  - Finite State Machine
  - Tutorial
  - Advanced
  - Multi-Stage Contracts
---
# Tutorial: Finite State Machines (FSM) in Ergo

Finite State Machines (FSMs) are a computational model used to design systems that can be in one of a finite number of states at any given time. The machine transitions from one state to another based on specific inputs or conditions. This model is particularly valuable for implementing [multi-stage protocols](../multi.md) or contracts on the blockchain, where the allowed actions depend on the current state of the contract.

## Concept

In the context of Ergo's [eUTXO model](eutxo.md), an FSM contract is implemented as a sequence of transactions, where each transaction consumes a box representing the *current state* and creates a new box representing the *next state*.

*   **State Representation:** The current state of the FSM is encoded within an Ergo box, typically using its [registers](../boxes-and-registers.md) (e.g., R4 might hold a state identifier like an `Int` or `Byte`). Other registers hold data associated with that state.
*   **Transitions:** The [ErgoScript](../ergoscript.md) guarding the state box defines the valid transitions. It checks:
    *   The conditions required to move from the current state (e.g., specific inputs provided, signatures, blockchain height).
    *   That the output box correctly represents the *next* valid state (e.g., the state identifier in R4 is updated correctly, other registers are preserved or updated according to protocol rules).
*   **Immutability:** Each transaction creates a *new* box for the next state, preserving the immutable nature of the blockchain. The previous state box is consumed (spent).

## Example: Simple Vending Machine FSM

Let's model a simple vending machine:

*   **States:**
    *   `Locked` (State 0): Waiting for payment.
    *   `Paid` (State 1): Payment received, waiting for item selection/dispensing.
*   **Transitions:**
    *   `Locked` -> `Paid`: Requires a transaction input providing the correct payment amount. The output box must be in the `Paid` state.
    *   `Paid` -> `Locked`: Requires a transaction input signaling item dispensing (e.g., signed by the vendor). The output box must return to the `Locked` state, potentially with changed value (representing dispensed item cost).

**Implementation Sketch (ErgoScript):**

```scala
// --- Script for a box in the 'Locked' state (State 0) ---
{
  // Constants defined: requiredPayment (Long), vendorPk (SigmaProp)
  // R4[Int] stores the state identifier (0 for Locked)

  val currentState = SELF.R4[Int].getOrElse(-1) // Get current state ID

  // Transition 1: Payment Received
  val paymentCondition = sigmaProp(
    // Check if exactly one output exists
    OUTPUTS.size == 1 &&
    // Check if the input box value matches the required payment
    INPUTS(0).value >= requiredPayment &&
    // Check if the output box represents the 'Paid' state (State 1)
    OUTPUTS(0).R4[Int].getOrElse(-1) == 1 &&
    // Ensure the output script is the same (points back to this FSM logic)
    OUTPUTS(0).propositionBytes == SELF.propositionBytes &&
    // Ensure vendor PK is preserved (example of preserving data)
    OUTPUTS(0).R5[SigmaProp].getOrElse(sigmaProp(false)) == SELF.R5[SigmaProp].getOrElse(sigmaProp(false)) &&
    // Ensure output value reflects payment minus potential change logic (simplified here)
    OUTPUTS(0).value >= requiredPayment
  )

  // Allow vendor to reclaim funds anytime (example of another path)
  val reclaimCondition = vendorPk

  sigmaProp(currentState == 0) && (paymentCondition || reclaimCondition)
}

// --- Script for a box in the 'Paid' state (State 1) ---
{
  // Constants defined: vendorPk (SigmaProp)
  // R4[Int] stores the state identifier (1 for Paid)

  val currentState = SELF.R4[Int].getOrElse(-1) // Get current state ID

  // Transition 2: Dispense Item (triggered by vendor signature)
  val dispenseCondition = sigmaProp(
    // Check if exactly one output exists
    OUTPUTS.size == 1 &&
    // Check if the output box represents the 'Locked' state (State 0)
    OUTPUTS(0).R4[Int].getOrElse(-1) == 0 &&
    // Ensure the output script is the same
    OUTPUTS(0).propositionBytes == SELF.propositionBytes &&
    // Ensure vendor PK is preserved
    OUTPUTS(0).R5[SigmaProp].getOrElse(sigmaProp(false)) == SELF.R5[SigmaProp].getOrElse(sigmaProp(false)) &&
    // Ensure output value reflects remaining funds (simplified)
    OUTPUTS(0).value == SELF.value // Assuming item cost is handled off-chain or via tokens
  ) && vendorPk // Requires vendor signature to dispense

  sigmaProp(currentState == 1) && dispenseCondition
}
```

*(Note: This is a simplified sketch. Real implementations need careful handling of values, tokens, change, multiple inputs/outputs, and robust error checking.)*

## Benefits in Ergo

*   **Clear State Management:** Explicitly encodes state in boxes and transitions in scripts.
*   **Composability:** FSM contracts can interact with other contracts and protocols.
*   **Security:** Validation rules are enforced on-chain for each state transition.
*   **Predictability:** Contract behavior is determined by the defined states and transitions.

## Resources & Examples

*   **Specifications in `sigmastate-interpreter`:**
    *   [`FsmExampleSpecification.scala`](https://github.com/ergoplatform/sigmastate-interpreter/blob/develop/sc/shared/src/test/scala/sigmastate/utxo/examples/FsmExampleSpecification.scala): Provides Scala code demonstrating FSM concepts in a testing context.
*   **Real-World Examples:**
    *   **ChainCash:** Contracts like [`note.es`](https://github.com/ChainCashLabs/chaincash/blob/master/contracts/onchain/note.es) implement FSM patterns for managing promissory notes and reserves.
*   **Related Concepts:**
    *   [Multi-Stage Contracts](../multi.md)
    *   [eUTXO Model](eutxo.md)
    *   [Box Registers](../boxes-and-registers.md)

## Advanced Concepts

In Ergo, we can implement Merkleized Finite State Machines (MFSMs) which are now possible to implement directly in ErgoScript. This approach allows for more complex state transitions while maintaining efficiency.

As described in the "Advanced ErgoScript Tutorial," we can emulate long-lived contracts by creating new boxes with the same script. While the box ID will change, the contract logic persists across state transitions.

Implementing robust FSMs requires careful planning of states, transitions, and the data that needs to be preserved or updated in registers at each step.
