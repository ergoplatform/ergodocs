

# Addresses

Addresses are short strings that correspond to specific scripts and are used to protect a [box](../data-model/box)

Unlike a (hex-encoded) binary representation of a script, an Ergo address use a `Base58-encoding` and therefore has some advantageous characteristics which the binary representation does not offer:

* We can quickly check the integrity of an address via an integrated checksum (which is a "small-sized datum derived from a block of digital data to detect errors that may have been introduced during its transmission or storage" according to Wikipedia).
* A prefix of the address shows you the network and address type. In particular, the network prefix prevents you from mistakenly sending mainnet tokens to the testnet address.
* The address uses an encoding (namely, Base58 as mentioned) that avoids similarly-looking characters and is friendly to double-clicking and line-breaking in emails.
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

For example, sending 10 Ergs to a P2PK address usually means that a corresponding transaction will contain a box in which 10 Ergs are locked by a public key encoded in the P2PK address. Similarly,
in the case of a P2S address, the box will be locked by a script encoded in the address. In the most complicated case of a P2SH script, the box will be protected by a special predefined script that takes the first 192 bits of Blake2b256 hash value for a script shown by an input spending the box. 


Here is an example of how particular addresses are going to look on the testnet: 

* **P2PK** (`3WvsT2Gm4EpsM9Pg18PdY6XyhNNMqXDsvJTbbf6ihLvAmSb7u5RN`)
* **P2SH** (`rbcrmKEYduUvADj9Ts3dSVSG27h54pgrq5fPuwB`)
* **P2S** (`Ms7smJwLGbUAjuWQ`)

And here is how what they look like on the mainnet:

* **P2PK** (`9fRAWhdxEsTcdb8PhGNrZfwqa65zfkuYHAMmkQLcic1gdLSV5vA`)
* **P2SH** (`8UApt8czfFVuTgQmMwtsRBZ4nfWquNiSwCWUjMg`)
* **P2S** (`4MQyML64GnzMxZgm, BxKBaHkvrTvLZrDcZjcsxsF7aSsrN73ijeFZXtbj4CXZHHcvBtqSxQ`)

## Length

**P2S** has no limit since it is the serialized script.
**P2SH** is 192 bits since it is the "first 192 bits of the Blake2b256 hash of serialized script bytes"
**P2PK** length is fixed. you can use the linked class to validate an address (it gives a runtime exception when created from an invalid string). 

in P2S everyone is able to see the script, in P2SH the script is going to be known when is it going to be spent.

P2SH has `0x12` at the beginning, and P2S has `0x13` on testnet and `0x02` and `0x03` on mainnet accordingly (note that in hex you can see that but in base58 it can change to anything).

For an exchange, you can restrict people to only withdraw to P2PK addresses and invalidate any other address. Supporting other types is not recommended.


as you can see 

> 88dhgzEuTXaRxf1rbqBRZ6Zbw9iigdB4PCdjyFKLrk22gnmjKcxZBe53vqJVetRa4tTNF9oowQWPp2c6 

equals

> **03** 10 02 04 a0 0b 08 cd 02 a1 f5 67 16 cb 8d f4 fe b9 37 14 37 90 4b 91 25 b8 2d b9 39 23 8c d7 d9 48 78 6d b3 3d e3 13 9f ea 02 d1 92 a3 9a 8c c7 a7 01 73 00 73 01 8c 23 55 af

## Summary

* **Prefix byte** = `network type + address type` (for example, P2S script on the testnet starts with 0x13 before Base58)
* **checksum** = `leftmost_4_bytes (blake2b256 (prefix byte || content bytes))`
* **address** = `prefix byte || content bytes || checksum`

**What is the generation algorithm of boxid?**

It is a hash over the box contents.

[See the code in AppKit]( https://github.com/ergoplatform/ergo-appkit/blob/9e19c13d82966eaee59433d16c4fb987bea363a7/lib-impl/src/main/java/org/ergoplatform/appkit/impl/OutBoxBuilderImpl.scala#L66)

Bytes are unique as box contains id of parent tx and output position in the tx, and tx id is unique as well

**Are P2S and P2SH are two address formats for the same script?**

It can be. so you can create a p2s and a p2sh address from the same script. in p2s the script is serialized into the address, in p2sh you only have a hash of that serialized script

**Will there be any problems with supporting addresses other than P2PK?**

no problem if the user knows what is he doing which is not true in lots of cases. it also adds more complexity. Specially for p2s address since you cannot validate the input size in your form. 

**ergoTree<->address related conversions**

When you use appkit, there is Address.create() that takes the address string. You can get the ergotree from the resulting object

**Some transactions don't charge fees?**

Fees are not part of the core protocol, but if you miss them, the transaction wont be propagated around the network by default



## Resources

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
- [Integration Guide for Exchanges](guide.md)