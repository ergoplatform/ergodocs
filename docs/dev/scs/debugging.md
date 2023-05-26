# Debugging ErgoScript

Since ErgoScript is usually encapsulated within string literals, it is not feasible to directly set breakpoints within the script text itself for debugging purposes. 

However, ErgoScript is a deliberate subset of Scala, and a robust test suite, SigmaDslSpecification, exists to verify the equivalence between ErgoScript and Scala. As such, you can utilize Scala's debugging capabilities to debug ErgoScript.

An example of such a debugging scenario is provided in the sigmastate-interpreter repository, specifically within [AssetsAtomicExchange.scala#L29](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/83dc78b5c80b11dcab41ba8aa75a0a8a650e6473/sigmastate/src/test/scala/sigmastate/utxo/examples/AssetsAtomicExchange.scala#L29). 

```scala
// See link for full context: 
  lazy val buyerProp = proposition("buyer", { ctx: Context =>
    import ctx._
    (HEIGHT > deadline && pkA) || {
      val tokenData = OUTPUTS(0).R2[Coll[(Coll[Byte], Long)]].get(0)
      val knownId = OUTPUTS(0).R4[Coll[Byte]].get == SELF.id
      allOf(Coll(
        tokenData._1 == tokenId,
        tokenData._2 >= 60L,
        OUTPUTS(0).propositionBytes == pkA.propBytes,
        knownId
      ))
    }
  },
```

In this instance, a breakpoint can be set at the specified line above. Following this, debug run can be executed for the [corresponding test](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/401d40a22430661ed5a397098633465b1e39e3bc/sigmastate/src/test/scala/sigmastate/utxo/examples/AssetsAtomicExchangeTests.scala#L46):

```scala
// Test link:
property("atomic exchange spec") {

```

During this execution, the debugger should halt at the pre-set breakpoint, enabling you to inspect and understand the code behavior in a step-by-step manner.