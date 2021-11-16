## What is a 'Box' ? 

Ergo has a Bitcoin-like UTXO transactional model: a transaction is spending one-time objects and creating new one-time objects. We call this object a box. A box is an immutable object which can be only created or removed. A box is not simply a coin; it contains registers with data (and code). Even more, there's nothing inbox but registers. There are four predefined registers, with monetary value, protecting script, and identifier of a transaction which created the box and output index in the transaction (and creation height). Because data of transaction which created the box is included in it, the box has unique contents and, therefore, a unique id. A box is a first-class citizen in the Ergo protocol. Active boxes set is authenticated via a hash-based data structure, which allows building lightweight full-nodes (as described in [this paper](https://eprint.iacr.org/2016/994)). A box may have up to six additional registers with typed data. A script may access its registers (as well as registers of input and output boxes of the spending transaction).

## Example

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

## Optional Registers 

In addition, a box can have six optional registers (R4-R9) to store custom data for use in smart contracts. Registers must be densely packed; that is, we cannot sandwich empty registers between non-empty ones. The optional registers can contain data of any of the following types:

- `Int`, `Long` with the usual semantics of Scala.
`BigInt` is a 256-bit integer (i.e., all computation is done modulo 2^256).
- `GroupElement`, a point on the Secp256k1 curve represented in compressed format.
- `Coll[Byte]`, a collection of bytes, semantically similar to `Array[Byte]` in Scala.
- Collection of the above, i.e., `Coll[Int]`, `Coll[GroupElement]`, `Coll[Coll[Byte]]`, etc.
- A boxId is calculated based on the contents of all the registers. This boxId uniquely defines a box and can be considered equivalent to Bitcoin's (txId, vOut) pairs.

>Note that Ergo `txId` depends only on the message and not on signatures (similar to Bitcoin SegWit transactions). Hence, a txId is available even before signing. Similar to Bitcoin, Ergo supports chained transactions (i.e., spending of boxes with 0 confirmations).


## Box type

Box represents a unit of storage in Ergo blockchain. It contains 10 registers
(indexed 0-9). First 4 are mandatory and the others are optional.

```scala
/** Representation of Ergo boxes used during execution of ErgoTree operations. */
class Box {
  /** Box monetary value in NanoErg */
  def value: Long 
  
  /** Blake2b256 hash of this box's content, basically equals to
    * `blake2b256(bytes)` 
    */
  def id: Coll[Byte] 

  /** Serialized bytes of guarding script, which should be evaluated to true in
    * order to open this box. 
    */
  def propositionBytes: Coll[Byte] 
  
  /** Serialized bytes of this box's content, including proposition bytes. */
  def bytes: Coll[Byte] 
  
  /** Serialized bytes of this box's content, excluding transactionId and index
    * of output. 
    */
  def bytesWithoutRef: Coll[Byte]
    
  /** If `tx` is a transaction which generated this box, then `creationInfo._1`
    * is a height of the tx's block. The `creationInfo._2` is a serialized
    * transaction identifier followed by box index in the transaction outputs.
    */
  def creationInfo: (Int, Coll[Byte]) 
  
  /** Synonym of R2 obligatory register */
  def tokens: Coll[(Coll[Byte], Long)] 
  
  /** Extracts register by id and type.
    * ErgoScript is typed, so accessing a register is an operation which involves some
    * expected type given in brackets. Thus `SELF.R4[Int]` expression should evaluate to a
    * valid value of the `Option[Int]` type.
    *
    * For example `val x = SELF.R4[Int]` expects the
    * register, if it is present, to have type `Int`. At runtime the corresponding type
    * descriptor is passed as `implicit t: RType[T]` parameter of `getReg` method and
    * checked against the actual value of the register.
    *
    * There are three cases:
    * 1) If the register doesn't exist.
    *   Then `val x = SELF.R4[Int]` succeeds and returns the None value, which conforms to
    *   any value of type `Option[T]` for any T. (In the example above T is equal to
    *   `Int`). Calling `x.get` fails when x is equal to None, but `x.isDefined`
    *   succeeds and returns `false`.
    * 2) If the register contains a value `v` of type `Int`.
    *   Then `val x = SELF.R4[Int]` succeeds and returns `Some(v)`, which is a valid value
    *   of type `Option[Int]`. In this case, calling `x.get` succeeds and returns the
    *   value `v` of type `Int`. Calling `x.isDefined` returns `true`.
    * 3) If the register contains a value `v` of type T other then `Int`.
    *   Then `val x = SELF.R4[Int]` fails, because there is no way to return a valid value
    *   of type `Option[Int]`. The value of register is present, so returning it as None
    *   would break the typed semantics of registers collection.
    *
    * In some use cases one register may have values of different types. To access such
    * register an additional register can be used as a tag.
    *
    * <pre class="stHighlight">
    *   val tagOpt = SELF.R5[Int]
    *   val res = if (tagOpt.isDefined) {
    *     val tag = tagOpt.get
    *     if (tag == 1) {
    *       val x = SELF.R4[Int].get
    *       // compute res using value x is of type Int
    *     } else if (tag == 2) {
    *       val x = SELF.R4[GroupElement].get
    *       // compute res using value x is of type GroupElement
    *     } else if (tag == 3) {
    *       val x = SELF.R4[ Array[Byte] ].get
    *       // compute res using value x of type Array[Byte]
    *     } else {
    *       // compute `res` when `tag` is not 1, 2 or 3
    *     }
    *   }
    *   else {
    *     // compute value of res when register is not present
    *   }
    * </pre>
    *
    * @param i zero-based identifier of the register.
    * @tparam T expected type of the register.
    * @return Some(value) if the register is defined AND has the given type.
    *         None otherwise
    * @throws special.sigma.InvalidType exception when the type of the register value is
    *                                   different from T.
    */
  def Ri[T]: Option[T]
}
```

Besides properties, every box can have up to 10 numbered registers.
The following syntax is supported to access registers on box objects:
```
box.R3[Int].get          // access R3 register, check that its value of type Int and return it
box.R3[Int].isDefined    // check that value of R3 is defined and has type Int
box.R3[Int].isEmpty      // check that value of R3 is undefined
box.R3[Int].getOrElse(d) // access R3 value if defined, otherwise return `d`
```


