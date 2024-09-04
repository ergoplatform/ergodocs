---
tags:
  - Sigma Protocols
---

$$
\newcommand{\lst}[1]{#1}
\newcommand{\Tup}[1]{(#1)}
\newcommand{\Apply}[2]{#1\langle#2\rangle}
\newcommand{\MSig}[3]{\text{def}~#1(#2): #3}
\newcommand{\Ov}[1]{\overline{#1}}
\newcommand{\TyLam}[3]{\lambda(\Ov{#1:#2}).#3}
\newcommand{\Trait}[2]{\text{trait}~#1~\{ #2 \}}
\newcommand{\To}{\mapsto}
\newcommand{\Low}[1]{\mathcal{L}{[\![#1]\!]}}
\newcommand{\Lam}[2]{\lambda#1.#2}
\newcommand{\IfThenElse}[3]{\text{if}~(#1)~#2~\text{else}~#3}
\newcommand{\False}{\text{false}}
\newcommand{\True}{\text{true}}
\newcommand{\langname}{ErgoTree}
\newcommand{\corelang}{Core-\lambda}
$$

# Cryptographic 

This document provides an in-depth look at the cryptographic schemes, protocols, and data structures used in the Ergo blockchain. The security and functionality of transactions on the Ergo platform rely heavily on cryptographic signatures and data integrity mechanisms, ensuring that only authorized parties can approve transactions and that data integrity is maintained. This document outlines the internal workings of these cryptographic schemes, focusing on their implementation within the Ergo ecosystem, particularly in [`sigmastate-interpreter`](https://github.com/ScorexFoundation/sigmastate-interpreter), [`sigma-rust`](https://github.com/ergoplatform/sigma-rust), and [`Scrypto`](https://github.com/input-output-hk/scrypto).

## Overview

Ergo supports a wide range of cryptographic protocols via **composable Sigma protocols** integrated into the core of its blockchain. These protocols are the foundation of Ergo’s cryptographic security and smart contract framework. Cryptographic signature schemes are used to verify that a transaction was created by the owner of the corresponding private key, preventing unauthorized spending and ensuring the security of smart contracts.

### Cryptographic Toolkit

- **Hash Functions**: [SHA-256](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/hash/Sha256.scala) & [Blake2b](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/hash/Blake2b.scala)
- **Encoding**: `Base58`
- **Signing Algorithms**: ECDSA (`secp256k1`) and Schnorr
- **Primitive Secrets**: Schnorr Signature & Diffie-Hellman Tuple
- **Non-Interactive Proofs**: Proofs for Sigma statements are made non-interactive using the **Fiat-Shamir transformation**.

For more information on cryptographic functions in ErgoScript, refer to [ErgoScript Cryptographic Functions](dev/scs/global-functions.md#cryptographic-functions).

### Data Structures

Ergo employs specialized cryptographic data structures, which are key to its efficiency and security:

- **AVL+ Trees**: Used in Ergo's **Authenticated Dynamic Dictionary (ADD)**, AVL+ trees ensure that the state changes within the UTXO model are efficiently tracked and cryptographically verified. AVL+ trees maintain logarithmic performance for inserts, deletions, and lookups while providing cryptographic proofs of state changes. Learn more about the implementation in [BatchAVLProver.scala](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/avltree/batch/BatchAVLProver.scala) and [BatchAVLVerifier.scala](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/avltree/batch/BatchAVLVerifier.scala).

- **Merkle Trees**: Merkle trees secure and verify large datasets, such as the transactions within a block. They allow for efficient verification of transaction integrity without needing to download the entire dataset. Learn more about [Merkle Trees](merkle-tree.md).

---

## Sigma Protocols

Sigma protocols, or **Σ-protocols**, are a fundamental part of Ergo’s cryptographic framework, allowing a prover to convince a verifier of knowledge of a secret without revealing the secret itself. This makes Sigma protocols ideal for privacy-preserving applications, such as multi-party computations, ring signatures, and threshold signatures.

### How Sigma Protocols Work

Sigma protocols allow for various cryptographic proofs, including:

- **Proof of Knowledge of Discrete Logarithm**: Proving possession of a secret key without revealing it (e.g., Schnorr signatures).
- **Proof of Equality of Discrete Logarithms (Diffie-Hellman Tuple)**: Proving that two logarithms are equal without revealing their values.

These elementary Sigma protocols can be combined to form more complex proofs using logical connectives like **AND**, **OR**, and **Threshold (k-out-of-n)**.

### Composability in Sigma Protocols

One of the powerful features of Sigma protocols is their **composability**. They can be combined using simple logic to create complex cryptographic conditions for smart contracts:

- **OR**: Prove knowledge of one of several secrets (e.g., **one-of-two ring signature**).
- **AND**: Prove knowledge of all required secrets.
- **Threshold (k-out-of-n)**: Prove knowledge of at least **k** secrets out of **n**. For example, a **3-out-of-5 threshold signature** could require three signatures from five possible participants.

These flexible combinations allow Ergo developers to create powerful privacy-preserving smart contracts and applications.

### Example: 3-out-of-5 Threshold Signature

Consider a **3-out-of-5 threshold signature** that allows any three participants to sign a transaction. Here’s an example of an ErgoScript that implements such a threshold signature:

```scala
val ringScript = s"""
{
atLeast(
  3, 
  Coll(
    PK("9f8ZQt1Sue6W5ACdMSPRzsHj3jjiZkbYy3CEtB4BisxEyk4RsNk"), 
    PK("9hFWPyhCJcw4KQyCGu4yAGfC1ieRAKyFg24FKjLJK2uDgA873uq"), 
    PK("9fdVP2jca1e5nCTT6q9ijZLssGj6v4juY8gEAxUhp7YTuSsLspS"), 
    PK("9gAKeRu1W4Dh6adWXnnYmfqjCTnxnSMtym2LPPMPErCkusCd6F3"),
    PK("9gmNsqrqdSppLUBqg2UzREmmivgqh1r3jmNcLAc53hk3YCvAGWE")
  )
)
}
```

The above is a `3-out-of-5` **threshold signature** example, compiled into a **Pay-to-Script-Hash (P2S)** address. This allows three participants from a group of five to sign and spend funds.

For more information please see the dedicated [Sigma Protocols](sigma.md) section.

---

## Schnorr Signatures

Schnorr signatures form a core part of Ergo’s cryptographic framework. Known for their simplicity, efficiency, and security, Schnorr signatures are used to prove that the signer possesses the private key corresponding to a public key used in a transaction.

### How Schnorr Signatures Work

The Schnorr signature scheme is based on the hardness of the discrete logarithm problem and operates as follows:

- **Key Generation**: A user generates a private key \(x\) and computes the corresponding public key \(P = xG\), where \(G\) is the generator point on the elliptic curve SecP256K1.
  
- **Signing**: To sign a message \(m\), the user generates a random nonce \(k\), computes \(R = kG\), and generates the signature:

$$
e = H(R || P || m)
$$

$$
s = k + ex
$$

- **Verification**: The verifier checks the signature by computing \(R' = sG - eP\) and verifying:

$$
e = H(R' || P || m)
$$

Schnorr signatures are efficient and secure, and are a core primitive in Ergo. They are used in multi-signature wallets, privacy-preserving transactions, and as part of complex Sigma protocols.

For more information please see the dedicated [Schnorr](schnorr.md) section.

---

## Diffie-Hellman Protocol

The **Diffie-Hellman (DH)** protocol is a method of securely exchanging cryptographic keys over a public channel. In Ergo, the **Diffie-Hellman Tuple (DHT)** is used to prove that two logarithms are equal, without revealing the logarithms themselves. This is a critical part of privacy-preserving applications like **stealth addresses** and **mixers**.

### Diffie-Hellman Tuple (DHT)

In a **Diffie-Hellman Tuple**, a prover demonstrates knowledge of a shared secret \(x\) such that:

$$
u = g^x \quad \text{and} \quad v = h^x
$$

The protocol follows a challenge-response model to prove this relationship without revealing the secret \(x\).

### Use Cases

- **Stealth Addresses**: Stealth addresses use Diffie-Hellman key exchange to generate unique one-time addresses for every transaction, ensuring the recipient’s privacy.
  
- **Mixers**: In Ergo’s **ZeroJoin** mixer, the security is based on the **Decision Diffie-Hellman (DDH) assumption**, ensuring that transactions are private and fungible.

Learn more about how **Diffie-Hellman Tuples** are implemented in [sigma-rust](https://github.com/ergoplatform/sigma-rust/pull/315).

For more information please see the dedicated [Diffie](diffie.md) section.

---

## Security Considerations

Ergo’s cryptographic schemes are grounded in the **hardness of the discrete logarithm problem** and other well-established cryptographic assumptions. Proper use of cryptography is critical to ensuring smart contract security. Developers should carefully design contracts to avoid vulnerabilities, such as weak randomness or improper validation checks.

Ergo’s cryptographic schemes are extensively tested in the `sigmastate-interpreter`, such as in [SigningSpecification.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/test/scala/sigmastate/crypto/SigningSpecification.scala).

---

## Conclusion

Ergo’s cryptographic framework, based on Sigma protocols, Schnorr signatures, and Diffie-Hellman key exchanges, provides robust tools for secure and privacy-preserving decentralized applications. With the flexibility to combine cryptographic proofs into complex contracts using threshold signatures and ring signatures, Ergo enables developers to create powerful privacy-preserving applications, all while maintaining strong security guarantees.

For more information, visit:
- [sigmastate-interpreter repository](https://github.com/ScorexFoundation/sigmastate-interpreter)
- [sigma-rust repository](https://github.com/ergoplatform/sigma-rust)
- [Scrypto repository](https://github.com/input-output-hk/scrypto)


<!--
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
--> 