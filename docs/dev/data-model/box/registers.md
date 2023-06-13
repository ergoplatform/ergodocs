---
tags:
  - Data Model
---

# Registers

Each [box](box.md), at the very least, holds four key pieces of information:

1. The value in NanoErgs (1 Erg = 1000000000 NanoErgs).
2. The protection script (akin to Bitcoin's `scriptPubKey`) or "smart contract", safeguarding the box's expenditure.
3. Any additional assets or tokens housed within the box.
4. Creation details of the box, including the `txId`, which is the ID of the transaction that created the box, and an output index. This information also includes a `maxCreation` height parameter set by the box creator (note: this is not the actual creation height; it aids in the creation of "payment channels").

These pieces of information are stored in the first four registers of the box. The rest of the registers, from R4 to R9, can be used to store custom data for use in smart contracts. Scripts can access their own registers and the registers of input and output boxes of the spending transaction.

| Register | Value |
|---|---|
| R0 | Value (in nanoErgs as Base58) |
| R1 | Protection script (Smart Contract) |
| R2 | Assets (tokens) |
| R3 | Creation details |
| R4-R9 | Available for custom use |

> Remember, registers need to be densely packed; you cannot place an empty register between non-empty ones. 


### Register R0

This register encapsulates the monetary value of the box in nanoERGs. It can be accessed using the `Box.value` command, where `Box` could signify `SELF` or any box in the `INPUTS` or `OUTPUTS` collections.

### Register R1

Register R1 contains the proposition bytes of the guarding ErgoScript contract associated with the box. Access this register using `Box.propositionBytes`.

### Register R2

R2 holds a collection of tokens stored in the box. Each token is identified by two elements: a unique token id and the quantity of the specific token. Use `Box.tokens` to access this collection.

### Register R3

R3 stores information about the box’s creation, such as the originating transaction id, the box's output index (i.e., the index used in `OUTPUTS`), and the block height at the creation time of the transaction from which the box originates. Access this register using `Box.creationInfo`. The creation height plays a role in Ergo's unique storage rent feature, where boxes can be spent after four years, enabling miners to charge a small fee and recycle ERGs back into the blockchain.

### Registers 



### Optional Registers R4 - R9

These registers can contain any data defined when the box first originates from a transaction. The data could be of any common type found in ErgoScript, along with more complex types built from Pairs and Collections. These registers may also contain complex types such as `Box`, `SigmaProp`, `GroupElement`, and `AVLTree`.

The optional registers can hold any of the following data types:

- `Int`, `Long` with standard Scala semantics.
- `BigInt` - a 256-bit integer (all computations are modulo 2^256).
- `GroupElement` - a point on the Secp256k1 curve represented in compressed format.
- `Coll[Byte]` - a byte collection, conceptually akin to Scala's `Array[Byte]`.
- Collection of the above (i.e., `Coll[Int]`, `Coll[GroupElement]`, `Coll[Coll[Byte]]`, and so forth).

A `boxId` is calculated based on the contents of all the registers, uniquely defining a box. This can be equated to Bitcoin's (txId, vOut) pairs.

> Note that Ergo `txId` is dependent solely on the message and not on signatures (similar to Bitcoin SegWit transactions). Hence, a txId is accessible even before signing. Like Bitcoin, Ergo supports chained transactions, meaning boxes with 0 confirmations can be spent.




## Typed

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
