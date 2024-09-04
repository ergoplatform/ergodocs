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

# Cryptographic Primitives and Structures in Ergo

This document provides an in-depth look at the cryptographic schemes, protocols, and data structures used in the Ergo blockchain. The security and functionality of transactions on the Ergo platform rely heavily on cryptographic signatures and data integrity mechanisms. These ensure that only authorized parties can approve transactions and maintain the integrity of the data. This document outlines the internal workings of these cryptographic schemes, focusing on their implementation within the Ergo ecosystem, particularly in [`sigmastate-interpreter`](https://github.com/ScorexFoundation/sigmastate-interpreter), [`sigma-rust`](https://github.com/ergoplatform/sigma-rust), and [`Scrypto`](https://github.com/input-output-hk/scrypto).

## Overview

Ergo supports a wide range of cryptographic protocols via **composable Sigma protocols** integrated into the core of its blockchain. Cryptographic signature schemes are used to verify that a transaction was created by the owner of the corresponding private key, preventing unauthorized spending and ensuring the security of smart contracts.

### Cryptographic Toolkit

- **Hash Functions**: [SHA-256](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/hash/Sha256.scala) & [Blake2b](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/hash/Blake2b.scala)
- **Encoding**: `Base58`
- **Signing Algorithms**: ECDSA (`secp256k1`) and Schnorr
- **Primitive Secrets**: Schnorr Signature & Diffie-Hellman Tuple
- **Non-Interactive Proofs**: Proofs for Sigma statements are made non-interactive using the **Fiat-Shamir transformation**.

For more information on cryptographic functions in ErgoScript, refer to [ErgoScript Cryptographic Functions](dev/scs/global-functions.md#cryptographic-functions).

### Data Structures

Ergo employs specialized cryptographic data structures, which are key to its efficiency and security:

- **AVL+ Trees**: Used in Ergo's **Authenticated Dynamic Dictionary (ADD)**, AVL+ trees ensure that the state changes within the UTXO model are efficiently tracked and cryptographically verified. AVL+ trees maintain logarithmic performance for inserts, deletions, and lookups while providing cryptographic proofs of state changes. See the Scrypto implementation: [BatchAVLProver.scala](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/avltree/batch/BatchAVLProver.scala) and [BatchAVLVerifier.scala](https://github.com/input-output-hk/scrypto/blob/master/shared/src/main/scala/scorex/crypto/authds/avltree/batch/BatchAVLVerifier.scala).

- **Merkle Trees**: Merkle trees secure and verify large datasets, such as the transactions within a block. They allow for efficient verification of transaction integrity without needing to download the entire dataset. Learn more about [Merkle Trees](merkle-tree.md).

---

## Schnorr Signatures

Schnorr signatures form a core part of Ergo’s cryptographic framework, known for their simplicity, efficiency, and security. Compared to ECDSA, Schnorr signatures are better suited for complex cryptographic protocols and privacy-preserving transactions in blockchains.

### How Schnorr Signatures Work

The implementation of Schnorr signatures in Ergo is distributed across both the **sigmastate-interpreter** and **sigma-rust** repositories.

```rust
// Key Generation (sigma-rust)
let private_key = SecretKey::random();
let public_key = PublicKey::from(&private_key);
```

#### Key Generation

A user generates a private key \(x\) and computes the public key \(P = xG\), where \(G\) is the generator point on the elliptic curve (SecP256K1). This is implemented in [`secret_key.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/wallet/secret_key.rs).

#### Signing

To sign a message \(m\), the user generates a random nonce \(k\), computes \(R = kG\), and generates the signature:

$$
e = H(R || P || m)
$$

$$
s = k + ex
$$

The signing logic is implemented in [`signing.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/wallet/signing.rs) and [`DLogProtocol.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/crypto/DLogProtocol.scala).

#### Verification

To verify the signature, the verifier computes:

$$
R' = sG - eP
$$

If \(e = H(R' || P || m)\), the signature is valid.

### Example

Here is an example demonstrating Schnorr signature signing and verification using **sigma-rust**:

```rust
let message = "sample message";
let (sig, _) = sign(&private_key, message);
let is_valid = verify(&public_key, &sig, message);
assert!(is_valid);
```

### Use Cases of Schnorr Signatures

- **Multi-Signature Protocols**: Schnorr signatures support **MuSig** (multi-signature aggregation), enabling multiple participants to collaboratively sign a transaction. This is useful for multi-signature wallets and allows trustless coordination.
  
- **Adaptor Signatures**: These are used for private swaps, allowing conditional transactions (e.g., atomic swaps between different cryptocurrencies) to be executed without revealing sensitive information. Ergo has demonstrated private swaps with Bitcoin Cash using this technique.

---

## Sigma Protocols

Sigma protocols enable privacy-preserving proofs and cryptographic operations in Ergo. They allow a prover to convince a verifier that they possess knowledge of a secret without revealing the secret itself, making them ideal for privacy-focused smart contracts.

### Components of Sigma Protocols

1. **Commitment**: The prover sends a commitment that doesn't reveal the secret.
2. **Challenge**: The verifier sends a challenge to the prover.
3. **Response**: The prover responds, demonstrating their knowledge of the secret without revealing it.

Sigma protocols are particularly well-suited for multi-party computations and **zero-knowledge proofs**. Learn more about [Sigma Protocols](sigma.md).

### Example

Here is an example of how Sigma protocols are used to create zero-knowledge proofs:

```scala
val prover = new SigmaProver(secretKey)
val proof = prover.prove(challenge)
```

### Non-Interactive Sigma Protocols

Sigma protocols in blockchains are made **non-interactive** using the **Fiat-Shamir transformation**, allowing their use in decentralized applications. This transformation replaces the interactive challenge with a deterministic process, making the proof verifiable without interaction.

Sigma protocol implementations can be found in:

- [`SigmaPropProver.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/org/ergoplatform/SigmaPropProver.scala) (Scala)
- [`prover_result.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/chain/transaction/input/prover_result.rs) (Rust)

### Use Cases of Sigma Protocols

- **Mixers and Fungibility**: Ergo’s **ZeroJoin** mixer uses ring signatures and Sigma protocols to preserve transaction fungibility. Learn more in [ZeroJoin](zerojoin.md).
- **Stealth Addresses**: Sigma protocols power **stealth addresses**, allowing users to receive payments privately without exposing their public keys. See more about [Stealth Addresses](stealth-address.md).

---

## ErgoTree and Signature Schemes

**ErgoTree** is Ergo’s smart contract framework. It allows the creation of complex spending conditions using Sigma protocols and Schnorr signatures.

### Signature Scheme Integration in ErgoTree

ErgoTree scripts define conditions under which UTXOs (called "boxes") can be spent. These conditions often require complex cryptographic operations, such as multi-signature verification or Sigma proof evaluations.

- **Complex Spending Conditions**: ErgoTree allows contracts to define sophisticated conditions, including multi-signature schemes, time-based locks, and cryptographic proofs (e.g., Sigma proofs). For more details, refer to [ErgoTree](ergo-tree.md).
- **Ring and Threshold Signatures**: ErgoTree supports **ring signatures** for privacy-preserving transactions and **threshold signatures** for collaborative smart contracts.

### Example

```scala
val tree = ErgoTree.multiSig(2, List(pubKey1, pubKey2, pubKey3))
val spendingCondition = tree.evaluate(tx)
```


## Security Considerations

Ergo’s cryptographic schemes are grounded in the **hardness of the discrete logarithm problem** and other well-established cryptographic assumptions. Proper use of cryptography is critical to ensuring the security of smart contracts. Developers must carefully design their ErgoTree scripts to avoid vulnerabilities like weak randomness or improper validation checks.

For testing and verifying the security of cryptographic schemes, Ergo has robust test coverage in the `sigmastate-interpreter`, such as in the [SigningSpecification](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/test/scala/sigmastate/crypto/SigningSpecification.scala).

## Conclusion

Ergo's cryptographic framework is built on strong foundations like Schnorr signatures, Sigma protocols, **Scrypto** primitives, and robust data structures like **AVL+ trees** and **Merkle trees**. These cryptographic tools enable flexible, secure, and privacy-preserving transactions, supporting decentralized applications that require advanced security and efficiency. The cryptographic primitives, Sigma protocols, and signature schemes are implemented across the `sigmastate-interpreter` and `sigma-rust` repositories, providing a powerful platform for developers.

For more information, visit the [sigmastate-interpreter repository](https://github.com/ScorexFoundation/sigmastate-interpreter), [sigma-rust repository](https://github.com/ergoplatform/sigma-rust), and [Scrypto](https://github.com/input-output-hk/scrypto).


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