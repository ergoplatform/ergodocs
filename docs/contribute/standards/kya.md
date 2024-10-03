---
tags:
  - KYA
---


# Know Your Assumptions (KYA) in Ergo

The Ergo ecosystem operates on the **KYA (Know Your Assumptions)** model, which encourages transparency and user awareness regarding the assumptions they make when interacting with decentralized finance (DeFi) protocols. This model, embraced by the Ergo community, plays a significant role during the initialization of a wallet in Nautilus and while using decentralized applications (dApps) like Spectrum and Duckpools.

## Research Paper: *KYA - A Treatise on Assumptions in Cryptocurrencies and DeFi*

Developer Kushti is working on a research paper titled [KYA - A Treatise on Assumptions in Cryptocurrencies and DeFi](https://github.com/kushti/kya), aiming to explore overlooked but fundamental questions in the cryptocurrency space. The introduction highlights the importance of identifying the assumptions on which blockchain and DeFi protocols are built, shedding light on security, decentralization, and potential risks.

> "Traditional financial institutions rely on privacy-invasive checks such as KYC/AML. In the world of decentralized finance, we reverse that control, allowing users to check protocols for their underlying assumptions. KYA practices aim to introduce transparency where users can verify the security and properties of decentralized financial tools."

The KYA framework encourages users to take an active role in verifying the protocols they interact with, offering a more informed and secure participation in the decentralized financial ecosystem.


## KYA Prompts in the Ergo Ecosystem

Ergo introduces **KYA prompts** to educate users about the assumptions involved when interacting with different protocols. These prompts serve as a summary, providing necessary information that users should consider before engaging with the ecosystem’s applications. For example, projects like **SigmaFi** have incorporated KYA prompts to assist users in reviewing critical assumptions and the underlying technology.

For more information please see [Building a standard KYA Prompt](https://www.reddit.com/r/ergonauts/comments/159h9rs/building_a_standard_kya_prompt/)


## Ergo’s Assumptions

Building upon Bitcoin’s security foundation, Ergo operates under a distinct but modest set of assumptions to ensure a secure and scalable system.

### 1. Bootstrapping Techniques

Ergo employs advanced techniques like hash-based authenticated data structures for UTXO transformations, NiPoPoW (Non-Interactive Proofs of Proof-of-Work) proofs, and UTXO set snapshots. These methods enhance the security while optimizing storage requirements and scalability.

### 2. Signature Scheme

Ergo uses **Schnorr signatures** for cryptographic security, relying on the well-established secp256k1 curve also used in Bitcoin. Moreover, Ergo incorporates sigma protocols, enabling the construction of advanced cryptographic applications, with some relying on the **decisional Diffie-Hellman assumption**.

### 3. Miner Behavior

Like Bitcoin, Ergo assumes that the majority of miners will act honestly and follow protocol rules. However, Ergo's **storage rent** concept simplifies miner incentives for long-term sustainability of block rewards, while ensuring that data is retained efficiently.

### 4. Scalability and Security

Ergo’s architecture supports Layer 1 (L1) scalability without compromising security. The platform offers feature-rich smart contracts and cryptographic protocols, ensuring secure interactions within the blockchain while addressing DeFi scalability challenges.

---

## Bitcoin as Digital Gold

Bitcoin’s security model rests on several critical assumptions:

1. **Hash Function Security**: Bitcoin’s reliance on the SHA-256 hash function assumes that its cryptographic properties—collision resistance, preimage resistance—will remain secure.

2. **Digital Signature Scheme**: The elliptic curve signature scheme assumes that quantum computers capable of breaking 128-bit security will not emerge.

3. **Honest Mining Hashrate**: The majority of Bitcoin’s mining power is expected to follow protocol rules, building on the longest chain. This forms the basis of Bitcoin’s consensus and overall security.

Despite uncertainties, Bitcoin has functioned effectively for over 13 years, with no major issues regarding its core assumptions.

---

## DeFi Applications on Ergo

The Ergo platform serves as a foundation for various decentralized finance (DeFi) applications, providing security, scalability, and flexibility.

### 1. Oracles

Ergo supports oracles, which bring reliable external data into DeFi protocols. This integration ensures secure data feeds, which are crucial for many dApps within the ecosystem.

### 2. ErgoDEX

ErgoDEX (formerly Spectrum) is a decentralized exchange (DEX) built on Ergo. Leveraging Ergo's security guarantees, it facilitates trustless peer-to-peer trading of digital assets.

### 3. Stablecoins: Djed and SigUSD

Djed and SigUSD are stablecoins designed on Ergo, providing a decentralized mechanism for stable value representation, contributing to the broader DeFi ecosystem with transparency and decentralization.

### 4. Dexy

Dexy is another decentralized exchange focused on a simplified and user-friendly trading experience. It builds on Ergo’s core security and scalability assumptions to offer a more intuitive platform for users.



## References

1. [Original KYA Post](https://www.ergoforum.org/t/know-your-assumptions/4198)
2. [The Importance of KYA](https://ergoplatform.org/en/blog/The-Importance-of-Know-Your-Assumptions/)
3. [KYA Research Paper](https://docs.ergoplatform.com/contribute/standards/kya/#research-paper)
4. [Kushti’s KYA Paper](https://github.com/kushti/kya/blob/master/kya.pdf)
5. [SigmaFi dApp](https://sigmafi.app/#/)
