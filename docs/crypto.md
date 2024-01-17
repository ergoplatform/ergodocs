---
tags:
  - Sigma Protocols
---

# Cryptographic

Ergo has generic support for variety of cryptographic protocols (via composable sigma-protocols built into core).

## Crypto Primitives

- **Hash**: `Sha256`, `Blake2b256`
- **Encoding**: `Base58`
- **Signing Algorithm**: ECDSA (`secp256k1`) & Schnorr 
- **Primitive Secrets**: Schnorr Signature & Diffie-Hellman tuple
- **Non-Interactive**: The proof of sigma-statements are made non-interactive with the **Fiat-Shamir** transformation.
- [EIP-0003: Deterministic Wallet Standard](eip3.md)

See [this page](dev/scs/global-functions.md#cryptographic-functions) for a description of the global Cryptographic functions available in ErgoScript.

## Before Ergo

- **Bitcoin**: ECDSA signatures with Schnorr signature [added recently](https://news.bitcoin.com/bitcoin-cash-protocol-successfully-upgrades-schnorr-signatures-are-here/)
- **Bitcoin Forks** Usually adding some cryptography to the protocol (e.g new instructions in ZCASH)
- **Ethereum / EVM chains**: Instructions and precompiled contracts. Pairing operations to support 


## Use Cases

### Schnorr Signature

In the simplest case a signature in Ergo transaction is a Schnorr signature, in general case it is a signature corresponding to a subset of Generalized Schnorr Proofs.

- Ergo uses the same elliptic curve as Bitcoin (SecP256K1).
- Ergo's Schnorr signature is pretty close to known standards (RFCs). 
- Allows us to adopt known protocols such as [MuSig](https://eprint.iacr.org/2018/068). 
- It's possible to create **adaptor signatures** which can be used for private swaps. 
- There were private swap demos with Bitcoin Cash


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| Potentially, a lot of protocols | - | The same as Bitcoin |


### Mixers

- Basic tool to restore fungibility of digital notes.
- Basic scheme, ZeroJoin, is based on ring signatures and proof of knowledge for a **Diffie-Hellman tuple** 
- [Paper with contracts](https://eprint.iacr.org/2020/560)

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| No onchain mixing | Trusted setup-based or inefficient | Efficient, minimal trust assumptions |




### Stealth Addresses

A *Stealth Address* is a [DHT](diffie.md) contract that you can spend from without revealing your public key.



This allows a customer to derive a one-time payment address for a store, without revealing the payment to anyone but the store owner. 


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

See the [Stealth Addresses](stealth-address.md) page for more information.


### Ring and Threshold Signatures

- Native support in Ergo, also, more complex schemes support (e.g ring AND threshold)
- Implementations: node API, [Zero-Knowledge Treasury](zkt.md) on top of Ergo



| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

### Checking A Signature

You can do basic things in a contract like calculating the hash, but what if you want to check a signature for abitrary message in a contract. This can be done trivially in Ergo, an example is available in SuSy bridge implementation

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | Efficient ECDSA | Efficient Schnorr |



## Scrypto

[Scrypto](scrypto.md) is an open source cryptographic toolkit designed to make it easier and safer for developers to use cryptography in their applications.
