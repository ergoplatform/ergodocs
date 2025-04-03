---
tags:
  - Debugging
  - ErgoScript
  - Scala
  - Testing
  - sigmastate-interpreter
  - Appkit
---

# Scala-Based ErgoScript Debugging

Since ErgoScript is a subset of Scala and rigorously tested for equivalence within the [`sigmastate-interpreter`](https://github.com/ScorexFoundation/sigmastate-interpreter) repository, you can leverage standard Scala debugging tools and techniques to test and debug your contract logic off-chain.

## Concept

The core idea is to represent your ErgoScript contract logic as Scala code, typically within a testing environment like ScalaTest or JUnit, often using frameworks like [Appkit](scala.md) or the testing utilities within `sigmastate-interpreter` itself. This allows you to simulate the blockchain context (`Context`, `Box`, `Transaction`, etc.) and execute your contract logic within a standard JVM debugging environment.

## Process

1.  **Set up a Testing Environment:**
    *   Use a project based on Appkit, which provides high-level abstractions for context and transaction building.
    *   Alternatively, work within a fork or local copy of the `sigmastate-interpreter` project, utilizing its internal testing structures and examples.
2.  **Represent Contract Logic:**
    *   Write your contract logic as Scala functions or within test case setups that mirror the ErgoScript structure. Appkit's `ErgoContract` compilation or direct use of `SigmaBuilder` can be employed.
3.  **Simulate Context:**
    *   Create mock `Context`, `Box`, and `Transaction` objects representing the specific scenario you want to test. Populate input/output boxes, registers, context variables, and blockchain parameters (like `HEIGHT`) as needed.
4.  **Set Breakpoints:**
    *   Use your Scala IDE (e.g., IntelliJ IDEA) to set breakpoints within the Scala code representing your contract logic or the test setup code that invokes it.
5.  **Run in Debug Mode:**
    *   Execute the specific test case using the IDE's debugger.
6.  **Inspect and Step Through:**
    *   When the debugger halts at a breakpoint, you can:
        *   Inspect the values of variables (including simulated context data).
        *   Step through the code line by line.
        *   Evaluate expressions.
        *   Validate the logic flow and intermediate results.

## Example Reference

The [AssetsAtomicExchange.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sigmastate/src/test/scala/sigmastate/utxo/examples/AssetsAtomicExchange.scala) tests within the `sigmastate-interpreter` repository provide practical examples of this pattern. Breakpoints can be set within the `proposition` definitions (which contain Scala code mirroring ErgoScript), and the corresponding tests run in debug mode to step through the logic.

```scala
// Snippet from AssetsAtomicExchange - Breakpoint can be set inside this block
lazy val buyerProp = proposition("buyer", { ctx: Context =>
  import ctx._
  (HEIGHT > deadline && pkA) || { // Breakpoint here
    val tokenData = OUTPUTS(0).R2[Coll[(Coll[Byte], Long)]].get(0)
    // ... inspect tokenData, OUTPUTS(0), SELF, etc. ...
    val knownId = OUTPUTS(0).R4[Coll[Byte]].get == SELF.id
    allOf(Coll(
      tokenData._1 == tokenId,
      tokenData._2 >= 60L,
      OUTPUTS(0).propositionBytes == pkA.propBytes,
      knownId
    ))
  }
},
// ...
```

### Debugging Process Example

Using the `AssetsAtomicExchange.scala` example:

1.  **Set Breakpoint:** Place a breakpoint within the `buyerProp` or `sellerProp` definition in `AssetsAtomicExchange.scala` (e.g., inside the `||` block as shown in the snippet above).
2.  **Locate Test:** Find the corresponding test method in [`AssetsAtomicExchangeTests.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sigmastate/src/test/scala/sigmastate/utxo/examples/AssetsAtomicExchangeTests.scala), such as `property("atomic exchange spec")`.
    ```scala
    // Test method for atomic exchange in AssetsAtomicExchangeTests.scala
    property("atomic exchange spec") {
      // Test implementation details...
      // This code sets up the context and attempts the transaction
    }
    ```
3.  **Run Test in Debug Mode:** Right-click the specific test method (or the whole test class) in your IDE and select "Debug".
4.  **Inspect:** The execution will pause at your breakpoint, allowing you to inspect the state of simulated context variables (`ctx`, `HEIGHT`, `INPUTS`, `OUTPUTS`, `SELF`), local variables (`tokenData`, `knownId`), and step through the contract logic evaluation.

This technique provides a powerful way to thoroughly verify contract logic before deployment, catching potential errors in a controlled off-chain environment.
