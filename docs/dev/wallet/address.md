

# Addresses

We take a closer look into the Ergo address formatting, how they work and what makes them preferable to other types of blockchain addresses.

The moment you install any cryptocurrency wallet, you automatically create an address with it. Very loosely speaking, you can compare a wallet to a traditional bank account and an address to the matching account number.
It is precisely one of these alphanumeric addresses needed to either send money from person A to person B, receive money, or [withdraw your mining rewards](https://ergoplatform.org/en/blog/2019_07_03_mining_withdrawal/).
If you want to start using the Ergo wallet and dive deeper into its functions, check out the [the following link](https://ergoplatform.org/en/blog/2019_06_04_wallet-documentation/).



## Now, what exactly are addresses?


Addresses are short strings that correspond to specific scripts and are used to protect a [box](../data-model/box.md)

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

* `3` - **P2PK** (`3WvsT2Gm4EpsM9Pg18PdY6XyhNNMqXDsvJTbbf6ihLvAmSb7u5RN`)
* `?` - **P2SH** (`rbcrmKEYduUvADj9Ts3dSVSG27h54pgrq5fPuwB`)
* `?` - **P2S** (`Ms7smJwLGbUAjuWQ`)

And here is how what they look like on the mainnet:

* `9 `- **P2PK** (`9fRAWhdxEsTcdb8PhGNrZfwqa65zfkuYHAMmkQLcic1gdLSV5vA`)
* `?` - **P2SH** (`8UApt8czfFVuTgQmMwtsRBZ4nfWquNiSwCWUjMg`)
* `?` - **P2S** (`4MQyML64GnzMxZgm, BxKBaHkvrTvLZrDcZjcsxsF7aSsrN73ijeFZXtbj4CXZHHcvBtqSxQ`)

## Summary

* **Prefix byte** = `network type + address type` (for example, P2S script on the testnet starts with 0x13 before Base58)
* **checksum** = `leftmost_4_bytes (blake2b256 (prefix byte || content bytes))`
* **address** = `prefix byte || content bytes || checksum`


## Resources

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
