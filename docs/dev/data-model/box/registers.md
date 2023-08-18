---
tags:
  - Data Model
  - Registers
---

# Ergo Box Registers

In Ergo's blockchain model, a [box](box.md) is a versatile entity that not only holds the value of cryptocurrency but also contains additional data in the form of registers. This makes it a more functional and flexible version of the Unspent Transaction Output (UTXO) found in Bitcoin and many other cryptocurrencies.

Each box contains at least four essential pieces of information:

1. The value in NanoErgs (1 Erg = 1000000000 NanoErgs).
2. The protection script (similar to Bitcoin's `scriptPubKey`) or "smart contract", which secures the box's expenditure.
3. Any additional assets or tokens contained within the box.
4. Details about the box's creation, including the `txId`, which is the ID of the transaction that created the box, and an output index. This information also includes a `maxCreation` height parameter set by the box creator (note: this is not the actual creation height; it aids in the creation of "payment channels").

These pieces of information are stored in the first four registers of the box. The remaining registers, from R4 to R9, can be used to store custom data for use in smart contracts. Scripts can access their own registers and the registers of input and output boxes of the spending transaction.

 Register | Value |
---|---|
 R0 | Value (in nanoErgs as Base58) |
 R1 | Protection script (Smart Contract) |
 R2 | Assets (tokens) |
 R3 | Creation details |
 R4-R9 | Available for custom use |

> Note: Registers must be densely packed; you cannot place an empty register between non-empty ones. 

### Register R0

Register R0 holds the monetary value of the box in nanoERGs. Use the `Box.value` command to access this register, where `Box` could signify `SELF` or any box in the `INPUTS` or `OUTPUTS` collections.

### Register R1

Register R1 stores the proposition bytes of the guarding ErgoScript contract associated with the box. Use `Box.propositionBytes` to access this register.

### Register R2

Register R2 contains a collection of tokens stored in the box. Each token is identified by two elements: a unique token id and the quantity of the specific token. Use `Box.tokens` to access this collection.

### Register R3

Register R3 holds information about the box’s creation, such as the originating transaction id, the box's output index (i.e., the index used in `OUTPUTS`), and the block height at the creation time of the transaction from which the box originates. Use `Box.creationInfo` to access this register. The creation height is part of Ergo's unique storage rent feature, where boxes can be spent after four years, allowing miners to charge a small fee and recycle ERGs back into the blockchain.

### Optional Registers R4 - R9

These registers can contain any data defined when the box first originates from a transaction. The data could be of any common type found in ErgoScript, along with more complex types built from Pairs and Collections. These registers may also contain complex types such as `Box`, `SigmaProp`, `GroupElement`, and `AVLTree`.

The optional registers can hold any of the following data types:

- `Int`, `Long` with standard Scala semantics.
- `BigInt` - a 256-bit integer (all computations are modulo 2^256).
- `GroupElement` - a point on the Secp256k1 curve represented in compressed format.
- `Coll[Byte]` - a byte collection, conceptually similar to Scala's `Array[Byte]`.
- Collection of the above (i.e., `Coll[Int]`, `Coll[GroupElement]`, `Coll[Coll[Byte]]`, and so forth).

A `boxId` is calculated based on the contents of all the registers, uniquely defining a box. This can be compared to Bitcoin's (txId, vOut) pairs.

> Note: Ergo `txId` is dependent solely on the message and not on signatures (similar to Bitcoin SegWit transactions). Hence, a txId is accessible even before signing. Like Bitcoin, Ergo supports chained transactions, meaning boxes with 0 confirmations can be spent.

## Typed Registers

Both [ErgoScript](/dev/scs/ergoscript) and [ErgoTree](/dev/scs/ergotree) are **typed**, meaning that when a script accesses a register, it expects a specific type which is denoted in brackets.


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



