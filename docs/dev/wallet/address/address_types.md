# Address Types 


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



## P2S vs P2SH

**Typically most people use P2S because it is a lot easier to use. P2SH means you have to keep the contract ready off-chain to be submitted when you create the transaction, and if you lose it, then your funds are stuck forever.** This also makes it harder for other people to use your dApp as they need the contract themselves, rather than just the address. P2SH is technically cheaper since you store less data on-chain, but likely we won't see anyone using P2SH until we start to get heavy load on-chain.

P2SH is a good candidate for a pre-defined contract template (in terms of [EIP-5](eip5.md)) From this perspective context var id can be a template parameter. So fixing concrete id is not necessary. The template hex can be created once and then used across dApps. Sigma already support ContractTemplate, and the corresponding code can be made available in Fleet via Sigma-js.