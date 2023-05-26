---
tags:
  - Data Model
---
# Understanding Registers

In a [box](box.md), up to six extra registers can be used to store typed data. Scripts have the ability to access their own registers and the registers of input and output boxes of the spending transaction.

A [eutxo](eutxo.md) box in Ergo platform extends the traditional concept of a box (as in Bitcoin, which holds a single amount), and uses registers to store various values, like its native [tokens](tokens.md).

Both [ErgoScript](/dev/scs/ergoscript) and [ErgoTree](/dev/scs/ergotree) are **typed**, meaning that when a script accesses a register, it anticipates a specific type which is denoted in brackets.

For instance,

```scala
// Assign the value of the R4 register of the current box to the variable x
val x = SELF.R4[Int]
```

In the above example, the register is expected to have an `Int` type. Therefore, the expression `SELF.R4[Int]` should return a valid `Option[Int]` type value.

When you try to retrieve the value of the register `SELF.R4[Int]`, there are three potential scenarios:

1. The register does not exist, hence `SELF.R4[Int].isDefined` will return `false`.
2. The register has an `Int` type value, thus `SELF.R4[Int].get` will fetch that value, and `SELF.R4[Int].isDefined` will be `true`.
3. The register carries a value of a different type, in which case `SELF.R4[Int]` will fail, and it will not produce a valid `Option[Int]` type value.

In some use cases, a register may contain values of various types. An additional register can be employed as a tag to facilitate the access of such a register.

```scala
val tagOpt = SELF.R5[Int] // Retrieve the value of the register R5 of type Int and assign it to the variable `tagOpt`
val res = if (tagOpt.isDefined) { // Check if `tagOpt` is not empty
  val tag = tagOpt.get // Obtain the value of `tagOpt` and assign it to the variable `tag`
  if (tag == 1) { // Check if `tag` equals 1
    val x = SELF.R4[Int].get // Retrieve the value of the register R4 of type Int and assign it to the variable `x`
    // Compute `res` using the value `x` of type Int
  } else if (tag == 2) { // Check if `tag` equals 2
    val x = SELF.R4[GroupElement].get // Retrieve the value of the register R4 of type GroupElement and assign it to the variable `x`
    // Compute `res` using the value `x` of type GroupElement
  } else if (tag == 3) { // Check if `tag` equals 3
    val x = SELF.R4[ Array[Byte] ].get // Retrieve the value of the register R4 of type Array[Byte] and assign it to the variable `x`
    // Compute `res` using the value `x` of type Array[Byte]
  } else {
    // Compute `res` when `tag` is neither 1, 2, nor 3
  }
} else {
  // Compute `res` when the register is not present
}
```
