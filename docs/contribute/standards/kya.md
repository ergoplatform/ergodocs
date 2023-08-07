---
tags:
  - KYA
---
# 'Know Your Assumptions' (KYA) in Ergo

Ergo operates on the KYA (Know Your Assumptions) model, which aims to educate users about the assumptions they make when interacting with decentralized finance (DeFi) protocols. This model has been embraced by the Ergo community and is utilized during the initialization of a wallet in Nautilus or when using dApps like Spectrum or Duckpools.

## Research Paper: KYA - A Treatise On Assumptions in Cryptocurrencies and DeFi

kushti has initiated the development of a research paper titled [KYA - A Treatise On Assumptions in Cryptocurrencies and DeFi](https://github.com/kushti/kya). The introduction of the paper is provided below:

> This research paper aims to address several crucial questions that have been largely overlooked in the cryptocurrency industry, despite their fundamental importance. We firmly believe that the industry's existence heavily relies on these questions, and it is essential to provide affirmative answers to them.

> Additionally, we strive to systematize the knowledge surrounding the assumptions upon which cryptocurrency and DeFi protocols are built. Understanding the explicit or implicit assumptions that underpin these protocols is critical for properly comprehending their security and level of decentralization.

By exploring these questions and assumptions, the KYA model in Ergo contributes to the broader understanding of the cryptocurrency and DeFi landscape. It encourages users to be aware of the underlying assumptions and promotes a more informed and secure participation in the ecosystem.

## Bitcoin As A Digital Gold

The assumptions underlying the security of Bitcoin are based on several key factors:

1. **Hash Function Security:** The security of Bitcoin relies on the assumption that the SHA-256 hash function is not broken. This assumption means that the known security properties of the hash function, such as collision resistance, second preimage resistance, and preimage resistance, hold true.

2. **Digital Signature Scheme:** Bitcoin's security assumes that the digital signature scheme used is not broken. Specifically, the assumption is that quantum computers capable of solving the Discrete Log Problem for an elliptic curve of 128-bit security will not emerge.

3. **Honest Mining Hashrate:** The majority of the mining hashrate in the Bitcoin network is assumed to be honest, meaning that it follows the Bitcoin protocol. The definition of "honest" behavior varies, but generally, it involves building on the longest chain, adhering to protocol validation rules, and contributing valid inputs. While this assumption is complex due to the intricacies of the protocol, it forms a fundamental basis for the security of Bitcoin.

It is important to note that Bitcoin's assumptions are not without challenges and uncertainties. The real-world implementation of the protocol introduces complexities beyond simplified models, and deviations from the expected behavior can occur. However, Bitcoin has been functioning for over 13 years, and many theoretical issues have not materialized in practice.

## Ergo

Ergo aims to achieve a broad set of features securely while relying on a modest set of assumptions, building upon Bitcoin's foundation. Some key considerations in Ergo's assumptions include:

1. **Bootstrapping Techniques:** Ergo offers multiple techniques for bootstrapping the protocol securely. These techniques include the use of hash-based authenticated data structures for UTXO set transformations, downloading UTXO set snapshots, and utilizing NiPoPoW proofs. These techniques ensure security guarantees while reducing storage requirements and enabling log-space storage for blockchain components.

2. **Signature Scheme:** Ergo employs Schnorr signatures, which are simpler and formally proven to be secure, on top of the secp256k1 curve used in Bitcoin. Additionally, Ergo supports building cryptographic protocols as applications based on sigma protocols, with some applications relying on the decisional Diffie-Hellman assumption.

3. **Miners' Behavior:** Ergo shares similarities with Bitcoin regarding honest behavior expectations from miners. However, Ergo introduces the concept of storage rent, which aims to simplify miners' incentivization, particularly in the context of long-term block rewards.

Ergo's design allows for L1 scalability, feature-rich contracts, and cryptographic protocols while maintaining the same level of security as Bitcoin. It leverages existing assumptions while offering innovative solutions to address scalability challenges and expand functionality.

## DeFi Apps on Ergo

Ergo serves as the foundation for various decentralized finance (DeFi) applications. Some notable examples include:

1. **Oracles:** Oracles play a crucial role in providing external data to DeFi protocols. Ergo supports the integration of oracles, enabling secure and reliable data feeds from the external world.

2. **ErgoDEX:** ErgoDEX, formerly known as Spectrum, is a decentralized exchange (DEX) built on Ergo. It leverages Ergo's security guarantees and features, enabling trustless peer-to-peer trading of digital assets.

3. **Djed and SigUSD:** Djed and SigUSD are stablecoin projects built on Ergo. They provide stable value representation and decentralized governance mechanisms, offering stability and transparency in the Ergo ecosystem.

4. **Dexy:** Dexy is another DEX built on Ergo that focuses on simplicity and user experience. It aims to provide an intuitive and efficient trading platform for Ergo users.

These DeFi applications benefit from Ergo's robust security, flexibility, and scalability, enabling users to engage in decentralized financial activities with confidence.

The KYA model in Ergo, coupled with the research paper's insights, contributes to a better understanding of the assumptions and security considerations underlying cryptocurrency and DeFi protocols. It empowers users to make informed decisions and participate in the ecosystem more securely.

## More Information

See this [detailed forum post]([Know Your Assumptions (KYA) An Alternative to Traditional Know-Your-Customer (KYC) Practices](https://www.ergoforum.org/t/know-your-assumptions-kya-an-alternative-to-traditional-know-your-customer-kyc-practices/4409) for an overview and discussion on KYA. 