---
tags:
  - Data Model
  - Registers
  - Box
---

# Ergo Box Registers

*(Back to: [Box Overview](box.md))*

In Ergo's blockchain model, a [**box**](box.md) is a versatile entity that not only holds the value of cryptocurrency but also contains additional data in the form of **registers**. This makes it a more functional and flexible version of the [Unspent Transaction Output (UTXO)](eutxo.md) found in Bitcoin and many other cryptocurrencies.

**Each box contains at least four essential pieces of information:**

1. The value in NanoErgs (1 Erg = 1000000000 NanoErgs).
2. The protection [script](ergoscript.md) (similar to Bitcoin's `scriptPubKey`) or "[smart contract](ergoscript.md)", which secures the box's expenditure.
3. Any additional assets or [tokens](eip4.md) contained within the box.
4. Details about the box's creation, including the `txId` (the ID of the [transaction](transactions.md) that created the box) and an [output index](transactions.md#anatomy). This information also includes a `maxCreation` height parameter set by the box creator (note: this is not the actual creation height; it aids in the creation of "payment channels").

These pieces of information are stored in the first four registers (R0-R3) of the box. The remaining registers, from R4 to R9, can be used to store custom data for use in smart contracts. Scripts can access their own registers and the registers of [input](transactions.md#anatomy) and [output](transactions.md#anatomy) boxes of the spending transaction.

| Register | Value                                      | Access via ErgoScript (`Box.` prefix) |
|----------|--------------------------------------------|---------------------------------------|
| R0       | Value (in nanoErgs)                        | `value`                               |
| R1       | Protection script ([ErgoTree](ergotree.md)) | `propositionBytes`                    |
| R2       | Assets ([Tokens](eip4.md))             | `tokens`                              |
| R3       | Creation details (`(txId, outputIndex)`) | `creationInfo`                        |
| R4-R9    | Available for custom use                   | `R4[T]`, `R5[T]`, ... `R9[T]`         |


/// admonition | Keep in mind!
    type: warning

Registers must be densely packed; you cannot place an empty register between non-empty ones (e.g., you cannot define R5 if R4 is empty).
///


### Register R0

Register R0 holds the monetary value of the box in nanoERGs. Use `Box.value` to access this register, where `Box` could signify [`SELF`](blockchain-context.md#self), or any box in the [`INPUTS`](blockchain-context.md#inputs) or [`OUTPUTS`](blockchain-context.md#outputs) collections.

### Register R1

Register R1 stores the proposition bytes (the compiled [ErgoTree](ergotree.md)) of the guarding [ErgoScript](ergoscript.md) contract associated with the box. Use `Box.propositionBytes` to access this register.

### Register R2

Register R2 contains a collection of [tokens](eip4.md) stored in the box. Each token is identified by two elements: a unique token id (`Coll[Byte]`) and the quantity (`Long`) of the specific token. Use `Box.tokens` to access this collection (`Coll[(Coll[Byte], Long)]`).

### Register R3

Register R3 holds information about the box’s creation: `(txId: Coll[Byte], index: Short)`. Use `Box.creationInfo` to access this register. The creation height (the block height when the box was created) is accessible via `Box.creationInfo._2` and is part of Ergo's unique [storage rent](storage-rent.md) feature, where boxes can be spent after four years, allowing [miners](mining-overview.md) to charge a small fee and recycle ERGs back into the blockchain.

### Optional Registers R4-R9

These registers can contain any data defined when the box first originates from a transaction. The data could be of any common type found in [ErgoScript](ergoscript.md), along with more complex types built from Pairs and Collections. These registers may also contain complex types such as `Box`, [`SigmaProp`](sigma.md), `GroupElement`, and [`AVLTree`](avl.md).

The optional registers can hold any of the following data types:

- `Int`, `Long` with standard Scala semantics.
- `BigInt` - a 256-bit integer (all computations are modulo 2^256).
- `GroupElement` - a point on the Secp256k1 curve represented in compressed format.
- `Coll[Byte]` - a byte collection, conceptually similar to Scala's `Array[Byte]`.
- Collection of the above (i.e., `Coll[Int]`, `Coll[GroupElement]`, `Coll[Coll[Byte]]`, and so forth).

A `boxId` is calculated based on the contents of all the registers, uniquely defining a box. This can be compared to Bitcoin's (`txId`, `vOut`) pairs.

/// admonition | Note
Ergo `txId` is dependent solely on the message and not on [signatures](signing.md) (similar to Bitcoin [SegWit](https://en.bitcoin.it/wiki/Segregated_Witness) transactions). Hence, a `txId` is accessible even before signing. Like Bitcoin, Ergo supports [chained transactions](chained.md), meaning boxes with 0 confirmations can be spent.
///


## Typed Registers

Both [ErgoScript](ergoscript.md) and [ErgoTree](ergotree.md) are **typed**, meaning that when a script accesses a register, it expects a specific type which is denoted in brackets.


For instance,

```scala
// Assign the value of the R4 register of the current box (SELF) to the variable x
// The script expects R4 to contain an Int.
val x = SELF.R4[Int]
```

In the above example, the register is expected to have an `Int` type. Therefore, the expression `SELF.R4[Int]` returns an `Option[Int]` type value.

When you try to retrieve the value of the register `SELF.R4[Int]`, there are three potential scenarios:

1. The register R4 does not exist (was not defined when the box was created), hence `SELF.R4[Int].isDefined` will return `false`.
2. The register R4 exists and has an `Int` type value, thus `SELF.R4[Int].get` will fetch that value, and `SELF.R4[Int].isDefined` will be `true`.
3. The register R4 exists but carries a value of a different type (e.g., `Coll[Byte]`), in which case accessing it as `SELF.R4[Int]` will fail the script execution during [validation](validation.md).

In some use cases, a register may contain values of various types depending on context. An additional register can be employed as a tag to facilitate the access of such a register safely.

```scala
// Example using R5 as a type tag for data in R4
val tagOpt = SELF.R5[Int] // Retrieve the value of the register R5 of type Int and assign it to the variable `tagOpt`
val res = if (tagOpt.isDefined) { // Check if `tagOpt` is not empty
  val tag = tagOpt.get // Obtain the value of `tagOpt` and assign it to the variable `tag`
  if (tag == 1) { // Check if `tag` equals 1, indicating R4 holds an Int
    val x = SELF.R4[Int].get // Retrieve the value of the register R4 of type Int and assign it to the variable `x`
    // Compute `res` using the value `x` of type Int
    sigmaProp(x > 10) // Example condition
  } else if (tag == 2) { // Check if `tag` equals 2, indicating R4 holds a GroupElement
    val x = SELF.R4[GroupElement].get // Retrieve the value of the register R4 of type GroupElement and assign it to the variable `x`
    // Compute `res` using the value `x` of type GroupElement
    sigmaProp(x == someGroupElement) // Example condition
  } else if (tag == 3) { // Check if `tag` equals 3, indicating R4 holds Coll[Byte]
    val x = SELF.R4[Coll[Byte]].get // Retrieve the value of the register R4 of type Coll[Byte] and assign it to the variable `x`
    // Compute `res` using the value `x` of type Coll[Byte]
    sigmaProp(blake2b256(x) == someHash) // Example condition
  } else {
    // Handle unexpected tag value - fail the script
    sigmaProp(false)
  }
} else {
  // Handle case where tag register R5 is not present - fail the script
  sigmaProp(false)
}
// Context Variables used: SELF (See blockchain-context.md)
// Functions used: sigmaProp, PK (See sigma.md)
```
