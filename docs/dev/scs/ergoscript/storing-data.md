# Data Storage in ErgoScript

The Ergo blockchain allows data storage primarily through placing it in the [*registers*](registers.md) during the creation of a [box](box.md). Another method involves using [_context variables_](context-variables.md) when a box is being spent, but for this discussion, we'll focus on the former.

An Ergo box consists of ten registers, labeled `R0` through `R9`. The first four of these (`R0` through `R3`) are reserved by the protocol. The remaining six registers (`R4` through `R9`) are available for data storage and are initially empty. It's worth noting that an empty register cannot be sandwiched between full registers.

Here's an example of how registers can be utilized in ErgoScript:

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