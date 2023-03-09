---
tags:
  - Data Model
---
# Registers

A [box](box.md) can have up to six additional registers with typed data. A script can access its registers (as well as registers of input and output boxes of the spending transaction).

Rather than storing a single amount (like BTC), a [eutxo](eutxo.md) box has some registers to store arbitrary values, like its native [tokens](tokens.md).

[ErgoScript](/dev/scs/ergoscript) (as well as [ErgoTree](/dev/scs/ergotree)) is **typed**, so accessing a register is an operation that involves some expected type given in brackets. 

    
For example, 

```scala
// Assign the value of the R4 register of the current box to the variable x
val x = SELF.R4[Int]
```

expects the register (if it is present) to have the type `Int`. Thus, the `SELF.R4[Int]` expression should evaluate a valid `Option[Int]` type value.

There are three possible cases when attempting to get the value of the register SELF.R4[Int]:

1. The register does not exist, so `SELF.R4[Int].isDefined` is `false`.
2. The register contains a value of type Int, in which `SELF.R4[Int].get` returns that value, and `SELF.R4[`Int].isDefined` is true.
3. The register contains a value of a type other than Int, in which case `SELF.R4[Int]` fails and cannot return a valid value of type `Option[Int]`.

    
Within some use cases, a register may have values of different types. We can use an additional register as a tag to access such a register.

```scala
val tagOpt = SELF.R5[Int] // get the value of the register R5 that is of type Int, and assign it to the variable `tagOpt`
val res = if (tagOpt.isDefined) { // check if `tagOpt` is not empty
  val tag = tagOpt.get // get the value of `tagOpt` and assign it to the variable `tag`
  if (tag == 1) { // check if `tag` is equal to 1
    val x = SELF.R4[Int].get // get the value of the register R4 that is of type Int and assign it to the variable `x`
    // compute `res` using the value `x` of type Int
  } else if (tag == 2) { // check if `tag` is equal to 2
    val x = SELF.R4[GroupElement].get // get the value of the register R4 that is of type GroupElement and assign it to the variable `x`
    // compute `res` using the value `x` of type GroupElement
  } else if (tag == 3) { // check if `tag` is equal to 3
    val x = SELF.R4[ Array[Byte] ].get // get the value of the register R4 that is of type Array[Byte] and assign it to the variable `x`
    // compute `res` using the value `x` of type Array[Byte]
  } else {
    // compute `res` when `tag` is not 1, 2 or 3
  }
} else {
  // compute the value of `res` when the register is not present
}
```
