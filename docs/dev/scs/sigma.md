---
tags:
  - Sigma Protocols
  - Cryptography
  - Zero-Knowledge Proofs
---

# Sigma Protocols

*(Back to: [ErgoScript Overview](ergoscript.md))*

## Introduction

**Sigma protocols** (Σ-protocols) are a class of cryptographic proof systems that play a central role in the Ergo blockchain. These protocols allow a **prover** to convince a **verifier** that they know a value, such as a secret key, without revealing the value itself (a property related to [zero-knowledge proofs](zkp.md)). Σ-protocols are the foundation for many [privacy](zkp.md)-preserving and [multi-signature](threshold.md) functionalities in Ergo.

In **[ErgoScript](ergoscript.md)**, proving and verifying cryptographic statements are first-class primitives, giving developers access to powerful Σ-protocols. Scripts protecting [transaction outputs](transactions.md) can contain **Σ-statements**, which must be proven (by generating **Σ-proofs**) before the outputs can be spent.

Conceptually, Σ-proofs are generalizations of [digital signatures](signing.md). The **[Schnorr signature scheme](schnorr.md)** is the canonical example of a Σ-proof: it allows the recipient to prove knowledge of a secret ([discrete logarithm](dlog.md)) without revealing it. Σ-proofs in Ergo extend this concept, allowing the creation of more complex cryptographic protocols like **[multi-signature](threshold.md)**, **[ring signatures](ring.md)**, and **[threshold signatures](threshold.md)**.

### Elementary Σ-Protocols in ErgoScript

ErgoScript offers two elementary Σ-protocols over a group of prime order, such as an elliptic curve group:

1. **Proof of Knowledge of Discrete Logarithm ([Schnorr Signature](schnorr.md))**: This protocol proves knowledge of the discrete logarithm of a given public key with respect to a fixed generator. Essentially, this is the Schnorr signature scheme.
2. **Proof of Equality of Discrete Logarithms ([Diffie-Hellman Tuple](diffie.md))**: This protocol proves that two values share the same discrete logarithm across two different generators.

These basic protocols can be composed to create more advanced proofs using logical connectives like **AND**, **OR**, and **THRESHOLD**. This **composability** is what enables the creation of sophisticated [smart contracts](ergoscript.md) and multi-signature schemes.

For a detailed introduction to Σ-protocols, refer to the paper [On Σ-protocols](http://www.cs.au.dk/~ivan/Sigma.pdf).

---

## Composability of Σ-Protocols

A powerful feature of Σ-protocols in Ergo is their **composability**. You can create logical combinations of cryptographic statements using basic AND/OR logic.

Examples include:

- **[Ring Signatures](ring.md)**: A ring signature is a proof of knowledge of **one** of multiple secrets. For example:
  > Prove knowledge of either secret A or secret B.

- **[Threshold Signatures](threshold.md)**: A threshold signature is a proof that a certain number of secrets are known. For example:
  > Prove knowledge of at least two of three secrets.

These constructions allow for flexible and privacy-preserving proofs. The **THRESHOLD** construct (also known as **k-out-of-n**) is particularly useful for multi-party agreements, ensuring that a subset of participants can authorize a [transaction](transactions.md) without requiring everyone’s involvement.

#### Example: 3-out-of-5 Threshold Signature

```scala
// Example ErgoScript for a 3-out-of-5 multi-signature contract
val thresholdScript = s"""
{
  atLeast( // Requires at least 3 proofs from the collection below
    3,
    Coll(
      PK("9f8ZQt1Sue6W5ACdMSPRzsHj3jjiZkbYy3CEtB4BisxEyk4RsNk"), // Public Key 1
      PK("9hFWPyhCJcw4KQyCGu4yAGfC1ieRAKyFg24FKjLJK2uDgA873uq"), // Public Key 2
      PK("9fdVP2jca1e5nCTT6q9ijZLssGj6v4juY8gEAxUhp7YTuSsLspS"), // Public Key 3
      PK("9gAKeRu1W4Dh6adWXnnYmfqjCTnxnSMtym2LPPMPErCkusCd6F3"), // Public Key 4
      PK("9gmNsqrqdSppLUBqg2UzREmmivgqh1r3jmNcLAc53hk3YCvAGWE")  // Public Key 5
    )
  )
}
"""
```

This contract is an example of a **3-out-of-5** threshold signature scheme. It can be compiled to a Pay-to-Script (P2S) [address](address.md), where any three of the five public keys can authorize a transaction.

---

## Use Cases of Σ-Protocols

### 1. **Multi-Signature Wallets**
[Multi-signature wallets](multisig.md) are a natural use case for Σ-protocols, where multiple parties are required to authorize a transaction. Σ-protocols allow you to set up flexible conditions such as requiring two out of three signatures, or even more complex schemes involving multiple participants.

### 2. **Ring Signatures for Privacy**
[Ring signatures](ring.md) provide [privacy](zkp.md) by allowing a user to sign a transaction on behalf of a group without revealing which group member signed it. This is particularly useful for creating anonymous transactions and decentralized mixers, such as **[ErgoMixer](ergomixer.md)**. The privacy of ring signatures makes them ideal for applications where anonymity is crucial, such as anonymous donations or private payments.

### 3. **Threshold Signatures**
[Threshold signatures](threshold.md) are critical for decentralized control. For example, a corporate [wallet](wallets.md) could be protected by a 3-out-of-5 signature scheme, ensuring that no single party can unilaterally control the funds.

### 4. **Time-Locked Conditions**
Σ-protocols can be combined with time-locked conditions. For instance, you can construct a contract that allows a transaction to be spent if either a ring signature is provided by a set of participants **before** a certain [block height](block-header.md), or the funds can be refunded by a single party **after** the block height has passed.

### 5. **Decentralized Mixers**
**[ErgoMixer](ergomixer.md)** is an advanced, non-custodial token [mixer](mixer.md) based on Σ-protocols. It leverages ring signatures and [zero-knowledge proofs](zkp.md) to provide enhanced privacy while ensuring that no third party is needed to manage or approve the mixing process. [SigmaJoin](sigmajoin.md), an [off-chain](off-chain.md) implementation concept related to ErgoMixer, further extends the idea of trustless and decentralized privacy mechanisms.

---

## Prover and Verifier Workflow

In Ergo, transaction processing using Σ-protocols involves two main actors: the **Prover** and the **Verifier**.

1. **Prover**:
    - The Prover uses the [**ErgoTree**](ergotree.md) [interpreter](sigmastate-interpreter.md) to reduce a high-level spending condition into a **SigmaBoolean** (the cryptographic proposition that needs to be proven). The SigmaBoolean is then converted into a cryptographic proof using the [Fiat-Shamir transformation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/sigma-dsl.md), ensuring that the transaction can only be authorized by parties who possess the necessary secrets (such as private keys).

2. **Verifier**:
    - The Verifier also uses the ErgoTree interpreter to reduce the spending condition into a SigmaBoolean. It then checks the cryptographic proof against this proposition, ensuring that the transaction is valid and all required conditions are met.

---

## Fiat-Shamir Transformation

The **Fiat-Shamir transformation** is a cryptographic technique that makes interactive proof systems non-interactive, suitable for use in blockchain environments. This is crucial for Sigma protocols, as it allows Σ-proofs to be created and verified without requiring real-time interaction between the prover and the verifier.

In Ergo, Σ-protocols rely on the Fiat-Shamir transformation to generate challenges (hash values) from the commitments and messages involved in the proof. This ensures that the proofs are non-interactive and can be verified deterministically on-chain.

---

## Applications and Resources

### Applications

- **[ErgoMixer](ergomixer.md)**: A state-of-the-art, non-custodial token mixer using Σ-protocols for privacy and anonymity.
- **[SigmaJoin](sigmajoin.md)**: An off-chain implementation concept related to ErgoMixer for decentralized privacy-preserving transactions.
- **Ergo Threshold Signature Contracts**: Use Σ-protocols to create custom multi-signature wallets and contracts.

### DarkFund0

- **DarkFund0**: A ZK fund for privacy applications, sponsoring developments in privacy-focused decentralized finance (DeFi) on Ergo.

### Tutorials

- [Verifying Schnorr Signatures in ErgoScript](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407)
- [Updateable Multisig Pattern](https://www.ergoforum.org/t/updateable-multisig-pattern/3356)

### Presentations

- [Sigma Protocols](https://crypto.sjtu.edu.cn/~yandi/2018%20BIU%20winter%20school/Part%203-Techniques%20for%20Efficient%20ZK%20(cont.)/WS-19-11-sigma-protocols-winter-school-2019-1.pdf)
- [On Σ-protocols](https://cs.au.dk/~ivan/Sigma.pdf)

---

## Conclusion

Sigma protocols form the backbone of Ergo’s smart contracts and cryptographic proofs, enabling flexible and privacy-preserving transactions. Whether it's for simple multi-signature wallets, complex threshold signatures, or advanced privacy-preserving ring signatures, Σ-protocols provide the necessary cryptographic tools for building secure and decentralized applications on the Ergo blockchain.

With their composability and integration into ErgoScript, Σ-protocols make Ergo a versatile platform for privacy-focused cryptographic applications.
