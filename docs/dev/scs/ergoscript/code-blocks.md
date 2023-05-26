# Using Code-Blocks in ErgoScript

When using multiple lines in ErgoScript, the lines must be contained within a code-block, which is enclosed in braces `{}`. Consider the following example:

```scala
{
   val out = OUTPUTS(0)
   val in = INPUTS(0)
   in.value == out.value
}
```

In this example, note that Scala accesses arrays using round parentheses `()`, not square brackets `[]` as in Java or Python. Therefore, `OUTPUTS(0)` is referencing the first element of the `OUTPUTS` array. In Scala, the last line of a block serves as the returned value of that block. Here, the returned value is the boolean predicate `in.value == out.value`.

This script maps to the [address](https://wallet.plutomonkey.com/p2s/?source=eyAgCiAgdmFsIG91dCA9IE9VVFBVVFMoMCkKICB2YWwgaW4gPSBJTlBVVFMoMCkKICBpbi52YWx1ZSA9PSBvdXQudmFsdWUKfQ==) `2EUTBShk4TbLWJNwGpkVYh8dAPqbrfvb3p`. It allows anyone to spend the box associated with this address, as long as the first input and the first output of the transaction contain the same value.

We used the `val` keyword to define intermediate immutable variables, similar to Scala. As `val` creates an immutable object, the object's value can't be changed once assigned. This makes the following code snippet invalid:

```scala
...
val out = OUTPUTS(0)        // defines an immutable value and sets it to the first output.  
out = OUTPUTS(1)            // reassignment of a val will cause an error
...
```

Unlike Scala, ErgoScript does not support the `var` keyword, meaning all variables are immutable. 

However, mutable variables can be emulated using lambda syntax, which will be covered separately.

Multiple blocks can be combined as shown below:

```scala
{
  INPUTS(0).id == SELF.id
} || {
  INPUTS(0).value == 100000 
}
```

In this example, the script checks whether the id of the first input is the same as the current box's id or if the value of the first input equals 100,000 nanoErgs.
