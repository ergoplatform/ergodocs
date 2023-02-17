

# Addresses

## Introduction 

Rather than storing a single amount (like BTC), an ergo [eutxo](eutxo.md) box has some registers to store arbitrary values, like its native tokens.

Addresses are short strings that correspond to specific scripts and are used to protect a [box](box.md)

So, each box has an ERG amount and may or may not have a bunch of `{tokenid, token amount}` pairs, all in the UTXO model.

Unlike account-based models like eth, ergo tokens are native and are not smart contracts.


## Base58

Unlike a (hex-encoded) binary representation of a script, an Ergo address use a `Base58-encoding` and therefore has some advantageous characteristics which the binary representation does not offer:

* We can quickly check the integrity of an address via an integrated checksum (a "small-sized datum derived from a block of digital data to detect errors that may have been introduced during its transmission or storage", according to Wikipedia).
* A prefix of the Address shows you the network and address type. In particular, the network prefix prevents you from mistakenly sending mainnet tokens to the testnet Address.
* The Address uses an encoding (namely, Base58, as mentioned) that avoids similarly-looking characters and is friendly to double-clicking and line-breaking in emails.
* An address encodes network type, address type, checksum, and enough information to correspond with particular scripts.

Let's look at the prefix byte, which contains information about the network and address types:

## Possible Types

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

For example, 

- Sending 10 ERG to a **P2PK** address usually means that a corresponding transaction will contain a box in which 10 Ergs are locked by a public key encoded in the **P2PK** Address. 
- Similarly, in the case of a **P2S** address, the box will be locked by a script encoded in the Address. 
- In the most complicated case of a **P2SH** script, the box will be protected by a special predefined script that takes the first 192 bits of *Blake2b256* hash value for a script shown by an input spending the box. 

Here are some examples of the various types of addresses you'll see on the testnet: 

* **P2PK** (`3WvsT2Gm4EpsM9Pg18PdY6XyhNNMqXDsvJTbbf6ihLvAmSb7u5RN`)
* **P2SH** (`rbcrmKEYduUvADj9Ts3dSVSG27h54pgrq5fPuwB`)
* **P2S** (`Ms7smJwLGbUAjuWQ`)

And here is how what they look like on the mainnet:

* **P2PK** (`9fRAWhdxEsTcdb8PhGNrZfwqa65zfkuYHAMmkQLcic1gdLSV5vA`)
* **P2SH** (`8UApt8czfFVuTgQmMwtsRBZ4nfWquNiSwCWUjMg`)
* **P2S** (`4MQyML64GnzMxZgm, BxKBaHkvrTvLZrDcZjcsxsF7aSsrN73ijeFZXtbj4CXZHHcvBtqSxQ`)

> Note: **P2S** can start with any number, D, M, or any other of base58. `9` is always a **P2PK** address on the mainnet.

## Summary

* **Prefix byte** = `network type + address type` 
    * (for example, P2S script on the testnet starts with `0x13` before Base58)
* **checksum** = `leftmost_4_bytes (blake2b256 (prefix byte || content bytes))`
* **address** = `prefix byte || content bytes || checksum`

## Address validation

[ergo-simple-addresses](https://github.com/kushti/ergo-simple-addresses) contains few zero-dependencies Java-friendly utils for working with addresses. The [Integration Guide for Exchanges](guide.md) may also be relevant. There is also a simple method in [Fleet](https://github.com/fleet-sdk/core/blob/master/src/models/ergoAddress.ts#L164). 

- **P2S** has no limit since it is the serialized script.
- **P2SH** is 192 bits since it is the "first 192 bits of the Blake2b256 hash of serialized script bytes."
- **P2PK** length is fixed. You can use the [linked class](https://github.com/ergoplatform/ergo-appkit/blob/9e19c13d82966eaee59433d16c4fb987bea363a7/lib-impl/src/main/java/org/ergoplatform/appkit/impl/OutBoxBuilderImpl.scala#L66) to validate an address (it gives a runtime exception when created from an invalid string). 

In P2S, everyone can see the script; in P2SH, the script will be known when it will be spent.

P2SH has `0x12` at the beginning, and P2S has `0x13` on testnet and `0x02` and `0x03` on mainnet accordingly (note that in hex, you can see that, but in base58, it can change to anything).

As you can see 

> 88dhgzEuTXaRxf1rbqBRZ6Zbw9iigdB4PCdjyFKLrk22gnmjKcxZBe53vqJVetRa4tTNF9oowQWPp2c6 

equals

> **03** 10 02 04 a0 0b 08 cd 02 a1 f5 67 16 cb 8d f4 fe b9 37 14 37 90 4b 91 25 b8 2d b9 39 23 8c d7 d9 48 78 6d b3 3d e3 13 9f ea 02 d1 92 a3 9a 8c c7 a7 01 73 00 73 01 8c 23 55 af



## Resources

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
