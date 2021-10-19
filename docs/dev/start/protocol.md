# The Ergo Protocol
Ergo is a UTXO based blockchain with Proof-of-Work consensus. In this aspect it is similar to Bitcoin. Ergo uses standard Elliptic Curve Cryptography and the exact same curve as Bitcoin (Secp256k1). Unlike Bitcoin and similar to Cardano, Ergo uses the so called "extended-UTXO model", which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. Due to this, Ergo supports advanced financial contracts similar to those in Ethereum's account-based model.

This document gives a brief overview of Ergo. For more details, refer to the documents and resources on Ergo Platform's website.
## Box
A UTXO is short for unspent transaction output. We can also consider spent transaction outputs (UTXOs that have been spent). In Ergo, a transaction output (whether spent or unspent) is called a box.

A box at the minimum has 4 pieces of information.

1. The value in NanoErgs (1 Erg = 1000000000 NanoErgs).
2. The guard script (like scriptPubKey of Bitcoin). This is also called the "smart contract".
3. Additional assets (tokens) stored in this box.
4. Creation info of the box (txId, the identifier of the transaction that created the box along with an output index). It also contains a "maxCreation" height parameter defined by the box creator (this is not the creation height; its use is to easily create "payment-channels").

**These are stored in the first 4 registers (numbered R0-R3) of the box.**

In addition, a box can have 6 optional registers (R4-R9) to store custom data for use in smart contracts. Registers must be densely packed, that is, we cannot sandwich empty registers between non-empty ones. The optional registers can contain data of any of the following types:

- Int, Long with the usual semantics of Scala.
- BigInt which is a 256 bit integer (i.e., all computation is done modulo 2^256).
- GroupElement, a point on the Secp256k1 curve represented in compressed format.
- Coll[Byte], which is a collection of bytes, semantically similar to Array[Byte] in Scala.
- Collection of the above, i.e., Coll[Int], Coll[GroupElement], Coll[Coll[Byte]], etc.
- A boxId is calculated based on the contents of all the registers. This boxId uniquely defines a box and can be considered equivalent to Bitcoin's (txId, vOut) pairs.

>Note that Ergo txId depends only on the message and not on signatures (similar to Bitcoin SegWit transactions). Hence, a txId is available even before signing. Similar to Bitcoin, Ergo supports chained transactions (i.e., spending of boxes with 0 confirmations).

## Anatomy of an Ergo transaction
An Ergo transaction consists of:

1. One or more Input boxes (source of funds). These boxes must already exist and will be destroyed. The guard script in each of these boxes will be evaluated and must return true for the transaction to be considered valid,
2. One or more Output boxes (destination of funds). These boxes will be created.
3. Zero or more Data-Inputs boxes. These are additional boxes whose data can be referenced and used by smart contracts of the inputs. The guard script in these boxes will not be evaluated.

Data-inputs are unique to Ergo and not yet present in other extended-UTXO systems. A data-input box can be shared by multiple transactions and only a single reference to the box will be stored in the block. A data-input box can also be spent in the same transaction as long as it existed before the transaction was applied. As an example, the box with id d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1 was used as both an input and a data-input in this transaction. While the use of data-inputs may not be immediately apparent, they play a major role in making Ergo more friendly to DeFi applications where we want to refer to a box without needing (or having the ability) to spend it, such as in decentralized order-books (DEX). For instance, the above transaction used a "timestamping service" to timestamp a box that was provided as a data-input.

A script in Ergo can refer to other boxes in the transaction. For instance, the code snippet INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000 in any of the inputs boxes would enforce that the first input and the second output boxes must have value greater than 10000 and 20000 respectively.

## Ergo Proof-of-Work (PoW)
Ergo uses Autolykos as the underlying PoW algorithm. Autolykos v2 (current version of PoW) is memory-hard ASIC-resistant PoW algorithm oriented towards GPUs.

## Storage Rent
Another unique feature of Ergo is the concept of storage-rent, which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent and a new box is created with the lower value). This allows Ergo to avoid long-term bloat of the UTXO set.

## ErgoScript
Ergo provides advanced programming abilities for financial contracts using a high-level language called ErgoScript. As a simple example, the below script allows only Alice to spend a box before a certain height and only Bob to spend the box after that.

if (HEIGHT < 100000) alicePubKey else bobPubKey 
We refer the reader to the various resources on the main website.