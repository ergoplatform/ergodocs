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

This document provides an in-depth look at the cryptographic schemes, protocols, and data structures used in the Ergo blockchain. Ergo’s security model relies heavily on advanced cryptographic protocols that ensure the integrity of transactions, protect user privacy, and enforce complex spending conditions within smart contracts. This document outlines the internal workings of these cryptographic schemes, focusing on their implementation within Ergo, particularly through the [`sigmastate-interpreter`](https://github.com/ScorexFoundation/sigmastate-interpreter), [`sigma-rust`](https://github.com/ergoplatform/sigma-rust), and [`Scrypto`](https://github.com/input-output-hk/scrypto) repositories.

## Overview


Ergo’s cryptographic toolkit is built around **composable Sigma protocols**, which allow for flexible, secure, and efficient proofs of knowledge and cryptographic operations within its smart contract framework. These Sigma protocols are the foundation of Ergo’s cryptographic security, and they enable privacy-preserving applications like multi-signature wallets, ring signatures, and threshold signatures.

### Cryptographic Toolkit

- **Hash Functions**: [SHA-256](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/hash/Sha256.scala) & [Blake2b](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/hash/Blake2b.scala) are used for generating secure cryptographic digests and ensuring data integrity.
- **Encoding**: Base58 encoding is used to represent binary data, such as public keys or hashes, in a more human-readable format.
- **Signing Algorithms**: Ergo supports both **ECDSA** (`secp256k1`) and **Schnorr** signatures for secure transaction signing.
- **Primitive Secrets**: **Schnorr signatures** and **Diffie-Hellman tuples** are primitive secrets used in creating proofs of knowledge.
- **Non-Interactive Proofs**: Ergo makes cryptographic proofs **non-interactive** using the **Fiat-Shamir transformation**, making them suitable for blockchain environments.

For more details on cryptographic functions in ErgoScript, see [ErgoScript Cryptographic Functions](dev/scs/global-functions.md#cryptographic-functions).

---

## Sigma Protocols

**Sigma protocols** (Σ-protocols) are a subclass of cryptographic proof systems that allow a prover to convince a verifier of knowledge of a secret without revealing the secret itself. They are integral to the privacy and security features in Ergo, enabling advanced cryptographic applications such as zero-knowledge proofs, ring signatures, and threshold signatures.

### How Sigma Protocols Work

At their core, [Sigma protocols](sigma.md) provide a secure way to prove the following properties:

1. **Proof of Knowledge of Discrete Logarithm**: Prove knowledge of the discrete logarithm of a given public key without revealing the secret key.
   
2. **Proof of Equality of Discrete Logarithms (Diffie-Hellman Tuple)**: Prove that two discrete logarithms (e.g., over different bases) are equal without revealing the logarithms.

These basic Sigma protocols can be combined using logical operators, such as **AND**, **OR**, and **THRESHOLD (k-out-of-n)**, to form complex proofs.

### Composability of Sigma Protocols

One of the key advantages of Sigma protocols is their **composability**. They can be combined in flexible ways to create sophisticated cryptographic contracts:

- **OR Proofs**: Prove knowledge of one secret from a set of secrets (e.g., **ring signatures**).
- **AND Proofs**: Prove knowledge of all secrets in a statement (e.g., multi-signature).
- **Threshold Proofs**: Prove knowledge of at least **k** out of **n** secrets. This is essential for threshold signatures, where a subset of participants must cooperate to authorize a transaction.

These constructs enable the creation of powerful, privacy-preserving applications on Ergo.

### Example: 3-out-of-5 Threshold Signature

Consider a **3-out-of-5 threshold signature** that allows any three participants to sign a transaction. This ErgoScript implements such a scheme:

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

This script enables three participants from a group of five to cooperatively sign and authorize a transaction. It leverages the **THRESHOLD (k-out-of-n)** logic, which is native to Sigma protocols, ensuring that only a subset of participants is required to perform cryptographic operations.

---

## Schnorr Signatures

**Schnorr signatures** are a key part of Ergo’s cryptographic foundation, providing an efficient, simple, and secure way to verify the authenticity of transactions. The Schnorr signature scheme is based on the **hardness of the discrete logarithm problem** and is favored for its performance and security properties over ECDSA.

### How Schnorr Signatures Work

The signing process in Schnorr signatures follows these steps:

1. **Key Generation**: Generate a private key \(x\) and compute the corresponding public key \(P = xG\), where \(G\) is the generator of the elliptic curve (SecP256K1).
   
2. **Signing**: To sign a message \(m\), the user:
   - Picks a random nonce \(k\) and computes \(R = kG\),
   - Computes \(e = H(R || P || m)\),
   - Computes the signature as \(s = k + ex\).

3. **Verification**: The verifier checks the signature by computing \(R' = sG - eP\) and verifying:
   \[
   e = H(R' || P || m)
   \]
   
Schnorr signatures are widely used in Ergo for multi-signature schemes, privacy-enhancing protocols, and adaptor signatures.

### Use Cases of Schnorr Signatures

- **Multi-Signature Wallets**: Schnorr signatures enable efficient and secure multi-signature wallets, where multiple participants must sign a transaction collaboratively.
- **Adaptor Signatures**: Adaptor signatures allow for **conditional private swaps**, such as atomic swaps between different cryptocurrencies, without revealing sensitive information.
  
For detailed examples and implementation, see [Verifying Schnorr Signatures in ErgoScript](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407).

---

## Diffie-Hellman Protocol

The **Diffie-Hellman (DH)** protocol is widely used in cryptography for secure key exchange. In Ergo, the **Diffie-Hellman Tuple (DHT)** protocol allows provers to demonstrate shared knowledge of a secret without revealing it, enabling privacy-preserving cryptographic proofs.

### Diffie-Hellman Tuple (DHT)

In a Diffie-Hellman Tuple, a prover proves knowledge of a shared secret \(x\) such that:

\[
u = g^x \quad \text{and} \quad v = h^x
\]

This protocol can be combined with Sigma protocols to create privacy-preserving smart contracts, such as **stealth addresses** and **mixers**. For instance, **ErgoMix** relies on the security of the Diffie-Hellman protocol to ensure transaction fungibility and user privacy.

### Use Cases of Diffie-Hellman

- **Stealth Addresses**: Ensure that each transaction generates a unique address, making it difficult to link transactions to the original public address, protecting user privacy.
- **ZeroJoin Mixers**: Enable on-chain privacy-preserving mixing of tokens, ensuring that transactions remain fungible and private without reliance on trusted third parties.

For a deep dive into Diffie-Hellman Tuples, refer to [Diffie](diffie.md).

---

## Data Structures in Ergo

Ergo employs specialized cryptographic data structures to ensure secure and efficient state management within its blockchain:

### AVL+ Trees

Ergo uses **AVL+ trees** as part of its **Authenticated Dynamic Dictionary (ADD)** to track UTXO state changes. These trees provide cryptographic proofs of state changes while maintaining logarithmic complexity for inserts, lookups, and deletions. AVL+ trees are essential for the UTXO model’s scalability and efficiency, enabling fast and secure updates across the network.

- **Implementation**: Learn more about AVL+ trees in [BatchAVLProver.scala](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/avltree/batch/BatchAVLProver.scala) and [BatchAVLVerifier.scala](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/avltree/batch/BatchAVLVerifier.scala).

### Merkle Trees

**Merkle trees** are used in Ergo to ensure the integrity of large datasets, such as blocks of transactions, without requiring the entire dataset to be transmitted or verified. By storing only the root hash of a Merkle tree, nodes can quickly verify that individual transactions are part of the block, reducing the overhead of verification.

Learn more about Merkle trees [here](merkle-tree.md).

---

## Security Considerations

The cryptographic schemes in Ergo rely on the **hardness of the discrete logarithm problem** and other well-established cryptographic assumptions. It is critical that developers design smart contracts carefully to avoid vulnerabilities, such as weak randomness or improper use of cryptographic primitives. Ergo provides extensive test coverage for its cryptographic implementations, such as the [SigningSpecification](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/test/scala/sigmastate/crypto/SigningSpecification.scala).

---

## Conclusion

Ergo’s cryptographic framework, built on Sigma protocols, Schnorr signatures, and Diffie-Hellman key exchanges, provides robust tools for secure and privacy-preserving decentralized applications. Its composable cryptographic proofs enable developers to create complex spending conditions, privacy-enhancing features, and flexible multi-signature schemes, all while maintaining a high standard of security.

For more information, visit the [sigmastate-interpreter repository](https://github.com/ScorexFoundation/sigmastate-interpreter), [sigma-rust repository](https://github.com/ergoplatform/sigma-rust), and [Scrypto repository](https://github.com/input-output-hk/scrypto).

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