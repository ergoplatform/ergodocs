
# Storing Data 

The most common way to store data on the Ergo blockchain is by placing it in the [*registers*](registers.md) during [box](box.md) creation. 

Another to store data is by using [_context variables_](context-variables.md) at the time a box is spent. However, we will only discuss the former approach here.
  
An Ergo box consists of ten registers (`R0..R9`), out of which the first four (`R0..R3`) are reserved by the protocol. The remaining six registers (`R4..R9`) are free for storing data and are empty by default. An empty register cannot be sandwiched between full registers. 

The following snippet shows how to use registers in your code:

    {
       val r4 = SELF.R4[GroupElement]
       if (r4.isDefined) {
          val x = r4.get
          proveDlog(x) 
       } else {
          proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))
       } 
    }
     
The line `SELF.R4[GroupElement]` returns an `Option[GroupElement]` type. The semantics of the `Option` type is exactly
the [same as in Scala](https://alvinalexander.com/scala/using-scala-option-some-none-idiom-function-java-null/). If the `Option` is defined, i.e., `SELF.R4` indeed contains a `GroupElement` type, then the first branch 
is executed, otherwise, the second branch is executed. 
