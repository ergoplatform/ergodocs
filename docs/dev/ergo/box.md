

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

**Articles**

- [UTXO Model Transaction](https://ergoplatform.org/en/blog/2021-10-07-utxo-model-transaction/)
- [Off-chain Logic and eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/)


**An Ergo transaction consists of:**

1. One or more Input boxes (source of funds). These boxes must already exist and will be destroyed. The guard script in each of these boxes will be evaluated and must return true for the transaction to be considered valid,
2. One or more Output boxes (destination of funds). These boxes will be created.
3. Zero or more Data-Inputs boxes. These are additional boxes whose data can be referenced and used by smart contracts of the inputs. The guard script in these boxes will not be evaluated.

Data-inputs are unique to Ergo and not yet present in other extended-UTXO systems. A data-input box can be shared by multiple transactions and only a single reference to the box will be stored in the block. A data-input box can also be spent in the same transaction as long as it existed before the transaction was applied. As an example, the box with id d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1 was used as both an input and a data-input in this transaction. While the use of data-inputs may not be immediately apparent, they play a major role in making Ergo more friendly to DeFi applications where we want to refer to a box without needing (or having the ability) to spend it, such as in decentralized order-books (DEX). For instance, the above transaction used a "timestamping service" to timestamp a box that was provided as a data-input.

A script in Ergo can refer to other boxes in the transaction. For instance, the code snippet INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000 in any of the inputs boxes would enforce that the first input and the second output boxes must have value greater than 10000 and 20000 respectively.



## Addresses

In today's article, we will have a closer look into the Ergo address formatting. In addition to that we are going to explain how they work specifically as well as what makes them preferable to other types of blockchain addresses.

Let's start at the very beginning.

The moment you install any cryptocurrency wallet you automatically create an address with it. Very loosely speaking you can compare a wallet to a traditional bank account and an address to the matching account number.
It is precisely one of these alphanumeric addresses that's needed to either send money from person A to person B, receive money or [withdraw your mining rewards](https://ergoplatform.org/en/blog/2019_07_03_mining_withdrawal/).
If you want to get started using the Ergo wallet and dive deeper into its functions go check out the [following link](https://ergoplatform.org/en/blog/2019_06_04_wallet-documentation/).

Now, what exactly are addresses?

Addresses are short strings that correspond to certain scripts and are used to protect a box ([this](https://www.ergoforum.org/t/ergo-terminology-a-box-and-a-register/32) post that core developer *kushti* published on our forum explains very well what a "box" is).
Unlike a (hex-encoded) binary representation of a script, an Ergo address is using a Base58-encoding and therefore has some very useful characteristics to it which the binary representation do not offer:

* The integrity of an address can easily be checked via an integrated checksum (which is a "small-sized datum derived from a block of digital data for the purpose of detecting errors that may have been introduced during its transmission or storage", according to Wikipedia).
* A prefix of the address is showing you the network and address type. In particular, the network prefix prevents you from mistakenly sending mainnet tokens to the testnet address.
* The address is using an encoding (namely, Base58 as mentioned) which is avoiding similarly looking characters and is friendly to double-clicking and also line-breaking in emails.
* An address is encoding network type, address type, checksum, and enough information to correspond with particular scripts.

Let's look at the prefix byte which contains information about the network and address types:

Possible network types are:

* Mainnet - `0x00`
* Testnet - `0x10`

Address types are (semantics described below):

* `0x01` - Pay-to-PublicKey(P2PK) address
* `0x02` - Pay-to-Script-Hash(P2SH)
* `0x03` - Pay-to-Script(P2S)


For an address type, we form content bytes as follows:

* **P2PK** - serialized (compressed) public key
* **P2SH** - first 192 bits of the Blake2b256 hash of serialized script bytes
* **P2S**  - serialized script (this is where mining rewards go!)

For example, sending 10 Ergs to a P2PK address usually means that a corresponding transaction will contain a box in which 10 Ergs are locked by a public key encoded in the P2PK address. Similarly,
in case of a P2S address the box will be locked by a script encoded in the address. In the most complicated case of a P2SH script, the box will be protected by a special predefined script which is taking first 192 bits of Blake2b256 hash  value for a script which should be shown by an input spending the box. 


Here is an example of how particular addresses are going to look on the testnet: 

* `3` - **P2PK** (`3WvsT2Gm4EpsM9Pg18PdY6XyhNNMqXDsvJTbbf6ihLvAmSb7u5RN`)
* `?` - **P2SH** (`rbcrmKEYduUvADj9Ts3dSVSG27h54pgrq5fPuwB`)
* `?` - **P2S** (`Ms7smJwLGbUAjuWQ`)

And here is how what they look like on the mainnet:

* `9 `- **P2PK** (`9fRAWhdxEsTcdb8PhGNrZfwqa65zfkuYHAMmkQLcic1gdLSV5vA`)
* `?` - **P2SH** (`8UApt8czfFVuTgQmMwtsRBZ4nfWquNiSwCWUjMg`)
* `?` - **P2S** (`4MQyML64GnzMxZgm, BxKBaHkvrTvLZrDcZjcsxsF7aSsrN73ijeFZXtbj4CXZHHcvBtqSxQ`)

In short summary:

* **Prefix byte** = `network type + address type` (for example, P2S script on the testnet starts with 0x13 before Base58)
* **checksum** = `leftmost_4_bytes (blake2b256 (prefix byte || content bytes))`
* **address** = `prefix byte || content bytes || checksum`
