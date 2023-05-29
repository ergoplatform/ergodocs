---
tags:
  - Data Model
  - Box
---

# Understanding the Ergo 'Box'

The Ergo platform employs a transactional model akin to Bitcoin, known as the Unspent Transaction Output (UTxO) model. Here, transactions expend and generate single-use entities, referred to as a ***'box'***. 

The term 'box' in Ergo's context captures the idea that these entities are like containers holding various types of information (value, tokens, custom data, etc.), beyond just the unspent transaction output balance. This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running scripts or smart contracts, directly on the blockchain.


## Introduction

- A box is an immutable unit, which can be created or removed, but never altered. 
- The box is not just a simple coin; it houses data, code, and registers, with all of its contents exclusively stored in the registers. 
- Four pre-defined registers contain the box's monetary value, its protection script, and the ID of the transaction that created the box.
- Each box has a unique ID, derived from the unique contents of the box, including the data of the transaction that created it.
- Boxes are integral to the Ergo protocol. The active box set is authenticated through a hash-based data structure, facilitating the development of lightweight full nodes, as detailed in [this paper](https://eprint.iacr.org/2016/994). 
- A box can hold up to six additional [registers](registers.md) with typed data, accessible by the script.
- Transactions consist of both *input* and *output* boxes. 

## Example 

Consider the 'proof-of-no-premine' from the Ergo genesis state. This box contains the last block IDs from Bitcoin and Ethereum at the launch time, as well as the latest news headlines:

```JSON
     {
    "boxId": "b8ce8cfe331e5eadfb0783bdc375c94413433f65e1e45857d71550d42e4d83bd",
    "value": 1000000000,
    "ergoTree": "10010100d17300",
    "assets": [],
    "creationHeight": 0,
    "additionalRegisters": {
      "R5": "0e42307864303761393732393334363864393133326335613261646162326535326132333030396536373938363038653437623064323632336337653365393233343633",
      "R6": "0e464272657869743a20626f746820546f727920736964657320706c617920646f776e207269736b206f66206e6f2d6465616c20616674657220627573696e65737320616c61726d",
      "R8": "0e45d094d0b8d0b2d0b8d0b4d0b5d0bdd0b4d18b20d0a7d0a2d09fd09720d0b2d18bd180d0b0d181d182d183d18220d0bdd0b02033332520d0bdd0b020d0b0d0bad186d0b8d18e",
      "R7": "0e54e8bfb0e8af84efbc9ae5b9b3e8a1a1e38081e68c81e7bbade38081e58c85e5aeb9e28094e28094e696b0e697b6e4bba3e5ba94e5afb9e585a8e79083e58c96e68c91e68898e79a84e4b8ade59bbde4b98be98193",
      "R4": "0e403030303030303030303030303030303

0303031346332653265376533336435316165376536366636636362363934326333343337313237623336633333373437"
    }
  }
```


## [Registers](registers.md)

Each box, at the very least, holds four key pieces of information:

1. The value in NanoErgs (1 Erg = 1000000000 NanoErgs).
2. The protection script (akin to Bitcoin's `scriptPubKey`) or "smart contract", safeguarding the box's expenditure.
3. Any additional assets or tokens housed within the box.
4. Creation details of the box, including the `txId`, which is the ID of the transaction that created the box, and an output index. This information also includes a `maxCreation` height parameter set by the box creator (note: this is not the actual creation height; it aids in the creation of "payment channels").

These pieces of information are stored in the first four registers of the box. The rest of the registers, from R4 to R9, can be used to store custom data for use in smart contracts.

### Optional Registers 

| Register | Value |
|---|---|
| R0 | Value (in nanoErgs as Base58) |
| R1 | Protection script (Smart Contract) |
| R2 | Assets (tokens) |
| R3 | Creation details |
| R4-R9 | Available for custom use |

Remember, registers need to be densely packed; you cannot place an empty register between non-empty ones. The optional registers can hold any of the following data types:

- `Int`, `Long` with standard Scala semantics.
- `BigInt` - a 256-bit integer (all computations are modulo 2^256).
- `GroupElement` - a point on the Secp256k1 curve represented in compressed format.
- `Coll[Byte]` - a byte collection, conceptually akin to Scala's `Array[Byte]`.
- Collection of the above (i.e., `Coll[Int]`, `Coll[GroupElement]`, `Coll[Coll[Byte]]`, and so forth).

A boxId is calculated based on the contents of all the registers, uniquely defining a box. This can be equated to Bitcoin's (txId, vOut) pairs.

>Note that Ergo `txId` is dependent solely on the message and not on signatures (similar to Bitcoin SegWit transactions). Hence, a txId is accessible even before signing. Like Bitcoin, Ergo supports chained transactions, meaning boxes with 0 confirmations can be spent.


## Additional Resources

- For the box type description in the [ErgoScript language specification](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md#box-type).
- Visit [ErgoAddress.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/ec71a6f988f7412bc36199f46e7ad8db643478c7/sigmastate/src/main/scala/org/ergoplatform/ErgoAddress.scala), [ErgoBoxCandidate](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/org/ergoplatform/ErgoBoxCandidate.scala#L24-L43), and [ErgoBox](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/org/ergoplatform/ErgoBox.scala#L22-L59).
- For an in-depth explanation on Ergo box modeling, see [this page](box_modeling).
