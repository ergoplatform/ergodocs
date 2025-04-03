---
tags:
  - Why Ergo
  - Overview
---

# Why Ergo?

Ergo is a next-generation smart contract platform that ensures the economic freedom of ordinary people through secure, accessible, and decentralized financial tools. Backed by a powerful scripting language, advanced cryptographic features, and a foundation rooted in the best principles of blockchain technology, Ergo is poised to revolutionize the concept of Contractual Money.

## The Vision Behind Ergo

### A Fusion of Research and Practicality

Ergo encapsulates over a decade of blockchain evolution, merging proven concepts with the latest in peer-reviewed academic research. This blend has empowered Ergo to embed [advanced cryptographic features](documents.md) directly into its core, crafting a resilient blockchain equipped for future innovations. 

ErgoScript, the platform's programming language, exemplifies this innovation by enabling a wide range of functionalities, including ring signatures, atomic swaps, and self-replicating scripts, designed to set sophisticated rules for currency spending.

### Strength and Security

Engineered with a strong emphasis on security and versatility, Ergo offers a reliable foundation for dApps to operate with predictable costs. Its smart contracts ensure Turing completeness without compromising on predictability or affordability. Ergo adopts a declarative model for programming whereby it's always known in advance how much code will cost to run, avoiding the dangers of unrestricted functionality seen in some other platforms.

The introduction of [Sigma Protocols](sigma.md) and [Multi-stage Contracts](multi.md) enhances this further by supporting non-interactive zero-knowledge proofs and complex transaction conditions, facilitating intricate, secure, and efficient smart contract creation.

### Intelligent and User-Friendly

Ergo leverages Sigma Protocols [(Σ-Protocols)](sigma.md) to power its smart contracts, enabling the use of efficient zero-knowledge proofs. This allows for the performance of complex, privacy-sensitive tasks without intermediaries, fostering a trustless environment with unparalleled application-level privacy.

### Secure and Accessible to All

Ergo's dedication to universal blockchain security is evident through its implementation of Non-Interactive Proofs of Proof-of-Work [(NIPoPoWs)](nipopows.md). This feature allows users to transact and verify with confidence without a full node, requiring as little as 1 MB of data, making Ergo accessible on virtually any device.

Additionally, Ergo addresses sustainability through [Storage Rent](rent.md), incentivizing efficient data storage, and the [eUTXO](eutxo.md) model, enhancing privacy, scalability, and interoperability.

### Commodity Money and Innovation

Ergo transcends the traditional concept of a blockchain token, embodying **commodity money** with real-world consumption of resources for mining. This approach, rooted in securing commodities with cryptography, distinguishes Ergo with unique features:

- Incentives for long-term mining stability.
- [Demurrage](storage-rent.md), reinforcing Ergo as a genuine commodity.
- Support for decentralized derivatives and DeFi without intermediaries.
- SigmaFi ([SigmaFi](sigmafi.md) bonds), a peer-to-peer DeFi solution surpassing traditional financial institutions in transparency and risk management.
- Unparalleled support for developing [cryptographic protocols](crypto.md), including [non-interactive mixers](mixer.md) and [stealth addresses](stealth-address.md)

Ergo's recognition as the leading PoW cryptocurrency in DeFi supply demonstrates the practical application of its innovative features.

/// details | Open Source 
    {type: info, open: true}
**Open Source and Decentralized:** The majority of Ergo's ecosystem is open source, permissionless, and decentralized, fostering community involvement and allowing developers to build dApps quickly and efficiently.
///

## The Genesis of Ergo

Launched in 2019 by esteemed developers and cryptocurrency luminaries, including Alex Chepurnoy and Dmitry Meshkov, Ergo emerged from a shared vision to revolutionize the blockchain landscape. The initiative aimed to craft an efficient, secure, and user-friendly platform for financial contracts.

### A Fair Start

Ergo was dedicated to ensuring a fair and equitable launch, reflecting Bitcoin's foundational principles to prevent undue influence from large-scale investors. This strategy democratized access and established a sustainable economic model for the network's growth. 

The mining protocol allocated a portion of the rewards to a treasury, managed by the non-profit Ergo Foundation, to support ongoing development and adoption. In its first 2.5 years, the Foundation accumulated 4,330,791.5 ERGs (4.43% of the total supply). For more information, visit the [Ergo Foundation](ergo-foundation.md) and [emission](emission.md) sections.

- **Fixed Supply:** Ergo has a fixed supply of 97,739,924 coins, combating inflation.
- **Extended Emission Schedule:** Through EIP-27, Ergo's mining rewards are extended for approximately 17.38 years, enhancing sustainability and making $ERG more scarce and valuable over time.

## Why Ergo Embraces Proof-of-Work

Ergo utilizes the [Autolykos](autolykos.md) Proof-of-Work protocol, demonstrating its commitment to decentralization and fairness. Proof of Work enables a user-friendly environment where lightweight clients can interact directly with the blockchain, creating a truly programmable currency that is accessible and ready for use today.

### How Does Ergo Address Bitcoin's Challenges?

Ergo addresses several key challenges inherent to Bitcoin, enhancing functionality, security, scalability, and privacy:

| Challenges Faced by Bitcoin                                                                                    | Ergo's Solution                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Limited smart contract functionality                                                                           | Rich language (ErgoScript), eUTXO model, Sigma protocols, transaction chaining                                   |
| Unclear network security as block reward subsidy approaches zero and transaction fees remain low and volatile | More revenue from transaction fees due to DeFi and higher usage/scalability, storage rent, mining by subpools    |
| Lack of economy around state leading to miners receiving no compensation for holding UTXO set                  | Storage Rent provides additional rewards for miners, compensating for long-term UTXO holding                     |
| Inefficient merkle tree data structure leading to inefficient light clients                                    | AVL trees enabling drastically more efficient light client verification                                          |
| Weak and cumbersome optional privacy tools                                                                     | Sigma protocols enable true peer-to-peer privacy, ErgoMixer provides better anonymity than Monero                 |
| Massive scaling challenges                                                                                     | Decentralized on-chain governance, NiPoPoWs enable light clients with full node security, more Layer-2 options   |

### How Does Ergo Address Ethereum's Challenges?

Ergo's UTXO-based programming model is **declarative**, specifying conditions for a transaction to be accepted (not changes to storage state). This contrasts with Ethereum's imperative Account model.

| Challenges Faced by Ethereum                                                                        | Ergo's Solution                                                                                                 |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Creating transactions and utilizing smart contracts requires paying fees in ETH                     | Babel Fees allow users to pay transaction fees in native tokens                                                 |
| Gas requirement and the 'stopping problem'                                                          | No gas fees or stopping problem, most computations done off-chain, cost-predictable on-chain verification       |
| High gas fees and network congestion                                                                | Engineered with long-term scaling in mind, using advanced and well-researched tools                             |
| Node centralization in AWS / Infura                                                                 | Anyone can run a node (similar to Bitcoin), mitigants prevent bad node running experience                      |
| Censorship: Most blocks are OFAC blocks                                                             | Decentralization and PoW deeply ingrained in Ergo's ethos, resists censorship                                   |
| Centralization of Monetary Policy with Vitalik and Ethereum Foundation able to change emission      | All ERGs created in genesis block, released per pre-set emission schedule, changes require supermajority        |
| Poor security and frequent hacks costing billions                                                   | UTXO model and efficient onchain verification with most computation done off-chain                              |
| Poor privacy tools due to Account ledger model                                                      | Combination of eUTXO model and sigma protocols achieves optional privacy superior to Monero                     |

View [Comparisons](https://ergonaut.space/en/Community/Comparisons) with other projects.

## Want to Learn More?

### Meet the Minds Behind Ergo

Ergo is powered by experienced developers and researchers with strong academic backgrounds in cryptography, compiler theory, blockchain technology, and cryptographic e-cash. Our team members have extensive experience in core development for cryptocurrencies and blockchain frameworks.

Notable contributor Alexander _kushti_ Chepurnoy co-founded smartcontract.com (now Chainlink), served as a core developer at NXT, and was among the first employees at IOHK.

Visit Ergo's [Hall of Fame](https://ergoplatform.org/en/hall_of_fame/) to learn more about our contributors. For information on foundation members, refer to the [EF Transparency Report](ergo-foundation.md).

### Roadmap

Stay ahead of Ergo's journey by visiting the 'Roadmap' section [on our website](https://ergoplatform.org/en/ecosystem/#Roadmap), where you can explore upcoming projects and innovative features.

### Resources

Deepen your understanding of Ergo with these resources:

- [The Ergo Manifesto](https://ergonaut.space/en/Ergo/manifesto)
- [Explore Yield-Generating Strategies on Ergo](https://ergonaut.space/en/Guides/yield)
- Our comprehensive [FAQ](faq.md)
- [cafebedouin.org: _Why Ergo_](https://cafebedouin.org/2021/12/09/why-ergo/)
- Join our community chats across the web listed at [direct.me/ergo](https://direct.me/ergo)

> _"Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital."_
