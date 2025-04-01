---
tags:
  - Plasma
  - AVL Trees
  - Layer 2
  - Library
  - GetBlok
---

# Plasma

[GetBlok Plasma](https://github.com/GetBlok-io/GetBlok-Plasma) is a library on top of Ergo [Appkit](appkit.md) that provides an abstraction layer to simplify the process of integrating AVL Trees (AKA Plasma) into off-chain code. The goal is to give developers an easy way to use this Layer-2 scaling solution in contracts, off-chain code, and distributed systems managing the Plasma itself. GetBlok Plasma uses the default versioned storage implementation powered by LevelDB, with another SwayDB implementation in the works. **This allows for distributed systems to keep track of the key-value pairs held in digests stored on-chain.**

See these documents to get started;

- [AVL Trees / Plasma In ErgoScript: Basics, Tips, and Design Patterns](https://github.com/GetBlok-io/GetBlok-Plasma/blob/master/documents/AVL_Trees.MD)
- [Mining Pool Operating At Layer 2](https://github.com/GetBlok-io/GetBlok-Plasma/blob/master/documents/SmartPool_Plasma.MD)

## Details

Creating and managing AVL Trees is greatly simplified when using the library. To create a normal,
un-stored / temporary AVL Tree, we use *Plasma Maps*. Plasma Maps look similar to normal Scala maps on the surface
with a few changes that make them compatible with on-chain AVL Trees.

```scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.PlasmaMap
import org.ergoplatform.appkit.ErgoId
import sigmastate.{AvlTreeFlags, Values}
// Plasma Map that uses ErgoId's as keys, and ErgoTrees as values
val plasmaMap = new PlasmaMap[ErgoId, Values.ErgoTree](AvlTreeFlags.AllOperationsAllowed, PlasmaParameters.default)
```

All Plasma Maps use 32 byte digests and Blake2b256 hashing. Any class may be inserted into a Plasma Map
so long as there is a corresponding implicit `ByteConversion` for that class.

```scala
import io.getblok.getblok_plasma.ByteConversion
import org.ergoplatform.appkit.ErgoId
import sigmastate.Values
import sigmastate.serialization.ErgoTreeSerializer

// Default ByteConversions for ErgoId and ErgoTree
implicit val convertsId: ByteConversion[ErgoId] = new ByteConversion[ErgoId] {
  override def convertToBytes(t: ErgoId): Array[Byte] = t.getBytes

  override def convertFromBytes(bytes: Array[Byte]): ErgoId = new ErgoId(bytes)
}

implicit val convertsErgoTree: ByteConversion[Values.ErgoTree] = new ByteConversion[Values.ErgoTree] {
  override def convertToBytes(t: Values.ErgoTree): Array[Byte] = t.bytes

  override def convertFromBytes(bytes: Array[Byte]): Values.ErgoTree = ErgoTreeSerializer.DefaultSerializer.deserializeErgoTree(bytes)
}
```

Custom classes may also be used with their own definitions to allow for flexibility in contracts:

```scala
import com.google.common.primitives.{Ints, Longs}
import io.getblok.getblok_plasma.ByteConversion
import org.bouncycastle.util.encoders.Hex
import org.ergoplatform.appkit.{ErgoType, ErgoValue}
import sigmastate.eval.Colls
import special.collection.Coll

case class StateScore(score: Long, paid: Boolean) {
  def toBytes: Array[Byte] = Longs.toByteArray(score) ++ Array(if(paid) 1.toByte else 0.toByte)
}

def getPaid(byte: Byte): Boolean = {
  byte match {
    case 0 =>
      false
    case 1 =>
      true
    case _ =>
      throw new Exception("A payment byte was serialized incorrectly!")
  }
}
  implicit val scoreConversion: ByteConversion[StateScore] = new ByteConversion[StateScore] {
    override def convertToBytes(t: StateScore): Array[Byte] = t.toBytes

    override def convertFromBytes(bytes: Array[Byte]): StateScore = StateScore(Longs.fromByteArray(bytes.slice(0, 8)), getPaid(bytes.slice(8, 9).head))
  }
```

Once a Plasma Map is created, operations may be performed on it. All operations done on a Plasma Map
return some `OpResult` that wraps the Plasma Map's *value* field. The set of these `OpResult`s
are returned in a `ProvenResult`, which holds the returned values along with a `Proof` object that holds
the corresponding proof for the batched set of operations. `OpResult`s are all returned in the order in 
which they were entered.

```scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.{OpResult, PlasmaMap, Proof, ProvenResult}
import io.getblok.getblok_plasma.ByteConversion.convertsLongVal
import org.ergoplatform.appkit.ErgoId
import sigmastate.AvlTreeFlags
val tokenMap = new PlasmaMap[ErgoId, Long](AvlTreeFlags.AllOperationsAllowed, PlasmaParameters.default)

val cometId: ErgoId = ErgoId.create("0cd8c9f416e5b1ca9f986a7f10a84191dfb85941619e49e53c0dc30ebf83324b")
val tokenData: Seq[(ErgoId, Long)] = Seq(cometId -> 100L)

val result: ProvenResult[Long] = tokenMap.insert(tokenData: _*)

val opResults: Seq[OpResult[Long]] = result.response
val proof: Proof = result.proof

```

All of these classes have functions to convert between common types used in Ergo Appkit. This allows for easy
interactions between Plasma Map's and on-chain contracts.

```scala
import io.getblok.getblok_plasma.collections.{PlasmaMap, Proof}
import org.ergoplatform.appkit.{ErgoClient, ErgoContract, ErgoId, Parameters}

implicit val ergoClient: ErgoClient
implicit val myContract: ErgoContract
implicit val myMap: PlasmaMap[ErgoId, Long]
implicit val myProof: Proof
ergoClient.execute {
  ctx =>
    val txB = ctx.newTxBuilder()
    val outB = txB.outBoxBuilder()
    val outBox = outB
            .value(Parameters.OneErg)
            .contract(myContract)
            .registers(myMap.ergoValue, myProof.ergoValue)
            .build()
}
```
## LocalPlasmaMap
Interacting with a locally stored Plasma Map is done in a similar way, except that you must use the
`LocalPlasmaMap` class instead.
```scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.LocalPlasmaMap
import io.getblok.getblok_plasma.ByteConversion.convertsLongKey
import scorex.crypto.authds.avltree.batch.VersionedLDBAVLStorage
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.db.LDBVersionedStore
import sigmastate.{AvlTreeFlags, Values}
import java.io.File

val ldbStore = new LDBVersionedStore(new File("./level"), 10)
val avlStorage = new VersionedLDBAVLStorage[Digest32](ldbStore, PlasmaParameters.default.toNodeParams)(Blake2b256)
val localMap = new LocalPlasmaMap[Long, Values.ErgoTree](avlStorage, AvlTreeFlags.AllOperationsAllowed, PlasmaParameters.default)
```

## ProxyPlasmaMap

It can be useful to apply changes to a tree without necessarily committing to them. This is especially
true in the context of chained transactions or unexpected errors. For example, if changes are applied to the
tree but latency causes connection to the node to be lost, then the locally stored tree may have changes
that do not exist on-chain!

To deal with this problem, you can use a `ProxyPlasmaMap`. This PlasmaMap applies changes on a temporary
tree which allows you to receive proofs for the operations you perform. However, none of these changes
are saved to storage until the `commitChanges()` function is called. This ensures that unexpected errors
can be dealt with easily.

When dealing with the `ProxyPlasmaMap`, changes must first be explicitly enabled by calling
`initiate()`. This function initializes the internal temporary map. Following this, operations
may be performed on the map. All operations are applied to the temporary map, but are also kept
track of inside an internal Queue. Once `commitChanges()` is called, the Queued operations are applied
to persistent storage, and the temporary map is destroyed.

```scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.{LocalPlasmaMap, ProxyPlasmaMap}
import org.ergoplatform.appkit.ErgoId
import scorex.crypto.authds.avltree.batch.VersionedLDBAVLStorage
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.db.LDBVersionedStore
import sigmastate.{AvlTreeFlags, Values}
import io.getblok.getblok_plasma.ByteConversion.convertsLongVal
import java.io.File

val ldbStore = new LDBVersionedStore(new File("./level"), 10)
val avlStorage = new VersionedLDBAVLStorage[Digest32](ldbStore, PlasmaParameters.default.toNodeParams)(Blake2b256)
val proxyMap = new ProxyPlasmaMap[ErgoId, Long](avlStorage, AvlTreeFlags.AllOperationsAllowed, PlasmaParameters.default)
val ergopadId: ErgoId = ErgoId.create("d71693c49a84fbbecd4908c94813b46514b18b67a99952dc1e6e4791556de413")
val tokenDataErgoPad: Seq[(ErgoId, Long)] = Seq(ergopadId -> 100L)


// This will fail due to the ProxyMap being un-initiated
proxyMap.insert(tokenDataErgoPad: _*)

// Initiates operations on the tree
proxyMap.initiate()

// This will be successfully applied to the internal temporary tree, while also queueing this
// operation for later application into persistence
proxyMap.insert(tokenDataErgoPad: _*)

// This commits ALL of the changes made on the temporary tree into persistent storage, while also
// destroying the temporary tree
proxyMap.commitChanges()

val cometId: ErgoId = ErgoId.create("0cd8c9f416e5b1ca9f986a7f10a84191dfb85941619e49e53c0dc30ebf83324b")
val tokenDataComet: Seq[(ErgoId, Long)] = Seq(cometId -> 100L)

proxyMap.initiate()
proxyMap.insert(tokenDataComet: _*)

// This commits only the next operation that exists in the Queue. This does NOT destroy
// the temporary map.
proxyMap.commitNextOperation()

// This drops any uncommitted changes and destroys the temporary map. In this case,
// all changes were already committed since only one operation was performed.

proxyMap.dropChanges()
```


## Resources

- [Plasma Example: Off-chain Bank operating at Layer 2](https://www.ergoforum.org/t/offchain-bank-operating-at-layer-2/3367)
- [GetBlok Plasma](https://github.com/GetBlok-io/GetBlok-Plasma)
- [GetBlok: SmartPool Plasma](https://github.com/GetBlok-io/GetBlok-Plasma/blob/master/documents/SmartPool_Plasma.MD)
- [Paideia - Plasma Staking](https://github.com/ergo-pad/paideia-contracts/blob/main/paideia_contracts/contracts/plasma_staking/ergoscript/latest/plasmaStaking.es)
