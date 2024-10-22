---
tags:
  - KYA
---

# Know Your Assumptions (KYA) in Ergo

The Ergo ecosystem embraces the **KYA (Know Your Assumptions)** model, promoting transparency and user awareness regarding the assumptions made when interacting with decentralized finance (DeFi) protocols. This approach encourages users to understand risks and security concerns when using wallets like Nautilus and dApps such as Spectrum and Duckpools.

## Research Paper: *KYA - A Treatise on Assumptions in Cryptocurrencies and DeFi*

Developer Kushti is working on a research paper titled [KYA - A Treatise on Assumptions in Cryptocurrencies and DeFi](https://github.com/kushti/kya). It explores key assumptions underlying blockchain and DeFi protocols, highlighting their impact on security, decentralization, and risk management.

> "In decentralized finance, users can verify protocol assumptions, reversing the invasive privacy checks of traditional finance." - Kushti

The KYA framework encourages users to verify the protocols they interact with, fostering informed and secure participation in DeFi.

## KYA Prompts in the Ergo Ecosystem

Ergo introduces **KYA prompts** to inform users of key assumptions before interacting with different protocols. These prompts are designed to provide clear, concise information about the risks, requirements, and assumptions associated with each protocol, enabling users to make informed decisions.

KYA prompts typically cover the following areas:

1. **Security Assumptions**: Highlighting the underlying security mechanisms, such as cryptographic algorithms, consensus models, and trusted parties.
2. **Economic Assumptions**: Providing details on tokenomics, incentives, and economic factors that affect the protocol's stability and sustainability.
3. **User Responsibilities**: Outlining what actions users need to take to ensure their safety, such as managing private keys or understanding potential risks in smart contracts.
4. **External Dependencies**: Identifying any reliance on third-party services or external data, such as oracles, that could impact the protocol's functionality.
5. **Transparency**: Ensuring that users are aware of any opaque components or centralized elements within a supposedly decentralized protocol.

Projects like **SigmaFi** have adopted KYA prompts, helping users assess critical assumptions and understand the underlying technology. These prompts serve as a valuable tool in empowering users, promoting transparency, and mitigating risks in the DeFi landscape.

For more, see [Building a standard KYA Prompt](https://www.reddit.com/r/ergonauts/comments/159h9rs/building_a_standard_kya_prompt/).

## Ergo’s Assumptions

Ergo builds on Bitcoin's security with its own unique set of assumptions to ensure a scalable and secure system.

### 1. Bootstrapping Techniques

Ergo uses techniques like hash-based authenticated data structures, NiPoPoW proofs, and UTXO set snapshots for security, optimized storage, and scalability.

### 2. Signature Scheme

Ergo employs **Schnorr signatures** based on the secp256k1 curve and sigma protocols, enhancing cryptographic security through the **decisional Diffie-Hellman assumption**.

### 3. Miner Behavior

Ergo assumes honest miner behavior akin to Bitcoin, using a **storage rent** mechanism to sustain block rewards and incentivize efficient data retention.

### 4. Scalability and Security

Ergo's architecture supports Layer 1 scalability while maintaining security, offering smart contracts and cryptographic protocols that ensure safe DeFi interactions.

## Bitcoin as Digital Gold

Bitcoin’s security model rests on several key assumptions:

1. **Hash Function Security**: Bitcoin relies on SHA-256's resistance to collision and preimage attacks.
2. **Digital Signature Scheme**: Assumes no quantum computer will break 128-bit elliptic curve security.
3. **Honest Mining Hashrate**: Assumes the majority of miners will follow protocol rules, underpinning Bitcoin's consensus.

Despite these assumptions, Bitcoin has functioned effectively for over 13 years.

## DeFi Applications on Ergo

Ergo's platform underpins various DeFi applications, ensuring security, scalability, and flexibility.

### 1. Oracles

Ergo supports secure oracle integration, providing reliable data for dApps in the ecosystem.

### 2. ErgoDEX

Formerly Spectrum, **ErgoDEX** facilitates trustless peer-to-peer trading on Ergo, leveraging the platform’s security features.

### 3. Stablecoins: Djed and SigUSD

**Djed** and **SigUSD** are decentralized stablecoins built on Ergo, enhancing the DeFi ecosystem with transparent value stability.

### 4. Dexy

**Dexy** is a user-friendly decentralized exchange, utilizing Ergo's security and scalability to provide an accessible trading experience.

## References

1. [Original KYA Post](https://www.ergoforum.org/t/know-your-assumptions/4198)
2. [The Importance of KYA](https://ergoplatform.org/en/blog/The-Importance-of-Know-Your-Assumptions/)
3. [KYA Research Paper](https://docs.ergoplatform.com/contribute/standards/kya/#research-paper)
4. [Kushti’s KYA Paper](https://github.com/kushti/kya/blob/master/kya.pdf)
5. [SigmaFi dApp](https://sigmafi.app/#/)