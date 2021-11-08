Ergo has Bitcoin-like UTXO transactional model: a transaction is spending one-time objects and creating new one-time objects. We call this object a box. A box is immutable object which could be only created or removed. A box is not simply a coin, rather, it is contains registers with data (and code). Even more, there's nothing in box but registers. There are four predefined registers, with monetary value, protecting script, and identifier of a transaction which created the box and output index in the transaction (and also creation height). Because data of transaction which created the box is included into it, the box has unique contents and thus unique id. A box is first-class citizen in the Ergo protocol. Active boxes set is authenticated via a hash-based data structure, which allows to build lightweight full-nodes (as described in [https://eprint.iacr.org/2016/994](https://eprint.iacr.org/2016/994)). A box may have up to six additional registers with typed data. A script may access its registers (as well as registers of input and output boxes of the spending transaction).

Example of a box (proof-of-no-premine from Ergo genesis state, which contains last block ids from Bitcoin and Ethereum at the moment of launch, and also latest news headlines):
```
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
      "R4": "0e4030303030303030303030303030303030303031346332653265376533336435316165376536366636636362363934326333343337313237623336633333373437"
    }
  }
```

A box, at the minimum, has four pieces of information.

1. The value in NanoErgs (`1 Erg = 1000000000 NanoErgs`).
2. The guard script (like `scriptPubKey` of Bitcoin). This is also called the "smart contract."
3. Additional assets (tokens) are stored in this box.
4. Creation info of the box (`txId`, the identifier of the transaction that created the box along with an output index). It also contains a `maxCreation` height parameter defined by the box creator (this is not the creation height; its use is to create "payment channels easily").

- `R0` = monetary value
- `R1` = protecting script
- `R2` = tokens <— this was missed
- `R3` = identifier of a transaction which created the box and output index in the transaction (and also creation height).

**These are stored in the first four registers (numbered R0-R3) of the box.**

In addition, a box can have six optional registers (R4-R9) to store custom data for use in smart contracts. Registers must be densely packed; that is, we cannot sandwich empty registers between non-empty ones. The optional registers can contain data of any of the following types:

- `Int`, `Long` with the usual semantics of Scala.
- `BigInt`, which is a 256-bit integer (i.e., all computation is done modulo 2^256).
- `GroupElement`, a point on the Secp256k1 curve represented in compressed format.
- `Coll[Byte]`, a collection of bytes, semantically similar to `Array[Byte]` in Scala.
- Collection of the above, i.e., `Coll[Int]`, `Coll[GroupElement]`, `Coll[Coll[Byte]]`, etc.
- A boxId is calculated based on the contents of all the registers. This boxId uniquely defines a box and can be considered equivalent to Bitcoin's (txId, vOut) pairs.

>Note that Ergo `txId` depends only on the message and not on signatures (similar to Bitcoin SegWit transactions). Hence, a txId is available even before signing. Similar to Bitcoin, Ergo supports chained transactions (i.e., spending of boxes with 0 confirmations).



