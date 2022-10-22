# SigmaBoolean

```scala
  /** Algebraic data type of sigma proposition expressions.
    * Values of this type are used as values of SigmaProp type of SigmaScript and SigmaDsl
    */
  trait SigmaBoolean {
    /** Unique id of the node class used in serialization of SigmaBoolean. */
    val opCode: OpCode
    /** Size of the proposition tree (number of nodes). */
    def size: Int
  }
 ```
[Values.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sigmastate/src/main/scala/sigmastate/Values.scala#L745)
