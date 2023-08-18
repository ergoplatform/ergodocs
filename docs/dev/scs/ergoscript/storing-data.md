# Data Storage in ErgoScript

ErgoScript, the language used in the Ergo blockchain, provides two primary methods for data storage. The first method involves the use of [*registers*](registers.md) during the creation of a [box](box.md). The second method utilizes [_context variables_](context-variables.md) when a box is being spent. For the purpose of this discussion, we will concentrate on the use of registers.

An Ergo box is equipped with ten registers, labeled from `R0` to `R9`. The protocol reserves the first four registers (`R0` through `R3`). The remaining six registers (`R4` through `R9`) are available for data storage and are initially empty. It's important to note that you cannot have an empty register between two filled registers.

Below is an example demonstrating how registers can be used in ErgoScript:

```scala
{
   val r4 = SELF.R4[GroupElement]
   if (r4.isDefined) {
      val x = r4.get
      proveDlog(x) 
   } else {
      proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))
   } 
}
```
   
In this code snippet, the line `SELF.R4[GroupElement]` returns an `Option[GroupElement]` type. The `Option` type semantics in ErgoScript are identical to [those in Scala](https://alvinalexander.com/scala/using-scala-option-some-none-idiom-function-java-null/). If the `Option` is defined—meaning `SELF.R4` does contain a `GroupElement` type—then the first branch of the if statement is executed. Otherwise, if `Option` is undefined, the second branch is executed.
