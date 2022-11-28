# Ergo: A Platform for Cryptographic Applications.

## Introduction

Ergo introduces native support for composable [Sigma Protocols](sigma.md), a class of efficient Generalized Schnorr Proofs, and can be converted into non-interactive form. 

There is also support for ring and threshold signatures out-of-the-box and many cryptographic protocols!


## Before Ergo

- **Bitcoin**: ECDSA signature with Schnorr signature support coming. 
- **Bitcoin Forks** Usually adding some cryptography to the protocol (e.g new insturctions in ZCASH)
- **Ethereum / EVM chains**: Instructions and precompiled contracts. Pairing operations to support 


## Use Cases

### Schnorr Signature

- Ergo's Schnorr signature is pretty close to known standards (RFCs) with certain differences. 
- Allows us to adopt known protocols such as MuSig and others developed in future. 
- It's possible to do adaptor signatures and private swaps based on them. 
- There were private swap demos with Bitcoin Cash
- Ergo uses the same elliptic curve as Bitcoin. 

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| Potentially, a lot of protocols | - | The same as Bitcoin |


### Mixers

- Basic tool to restore fungibility of digital notes.
- Basic scheme, ZeroJoin, is based on ring signatures and proof of knowledge for a **Diffie-Hellman tuple** (for publicly known g, h, u, v, there exists w, such as g&w == u && h^w == v)
- [Paper with contracts](https://eprint.iacr.org/2020/560)
- Few implementations, including [ErgoMixer](mixers.md)

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| No onchain mixing | Trusted setup-based or inefficient | Efficient, minimal trust assumptions |


### Stealth Addresses

- A tool to hide recipient privacy
- [Contracts](https://www.ergoforum.org/t/stealth-address-contract/255)

This allows a customer to derive a one-time payment address for a store, without revealing the payment to anyone but the store owner. 


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

### Ring and Threshold Signatures

- Native support in Ergo, also, more complex schemes support (e.g ring AND threshold)
- Implementations: node API, [Zero-Knowledge Treasury](zkt.md) on top of Ergo



| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

### Checking A Signature

You can do basic things in a contract like calculating the hash, but what if you want to to check a signature for abitrary message in a contract. This can be done trivially in Ergo, example is available in SuSy bridge implementation

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | Efficient ECDSA | Efficient Schnorr |