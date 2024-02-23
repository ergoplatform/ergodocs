# Why Ergo?

Ergo is a next-generation smart contract platform that ensures the economic freedom of ordinary people through secure, accessible, and decentralized financial tools.

It is backed by a powerful and secure scripting language, a suite of powerful zero-knowledge proofs, and a foundation rooted in the best principles and research in cryptography and blockchain technology.


## The Vision Behind Ergo
Let's incorporate the new information seamlessly into the existing content, ensuring all key points, including "Ergo offers unparalleled support," are highlighted effectively. I'll maintain the structure and integrate the new details into relevant sections or create new ones as needed.

### A Fusion of Research and Practicality

Ergo stands as a beacon in blockchain technology, encapsulating over a decade of blockchain evolution. This platform merges proven blockchain concepts with the latest in peer-reviewed academic research in digital currencies and cryptography. Such a blend has empowered Ergo to embed [advanced cryptographic features](documents.md) directly into its core, crafting a blockchain that is both resilient and equipped for future innovations. ErgoScript, the platform's programming language, exemplifies this innovation by enabling a wide range of functionalities, including ring signatures, atomic swaps, and the creation of self-replicating scripts, all designed to set sophisticated rules for currency spending.

### Strength and Security

Engineered with a strong emphasis on security and versatility, Ergo offers a reliable foundation for dApps to operate with predictable costs, safeguarding the integrity of financial contracts. Its smart contracts, capable of executing a diverse array of operations, ensure Turing completeness without compromising on predictability or affordability. The introduction of [Sigma Protocols](/dev/scs/sigma) and [Multi-stage Contracts](/dev/scs/multi) enhances this further by supporting non-interactive zero-knowledge proofs and complex transaction conditions, thereby facilitating intricate, secure, and efficient smart contract creation.

### Intelligent and User-Friendly

At its core, Ergo leverages Sigma Protocols [(Σ-Protocols)](sigma.md) to power its smart contracts, enabling the use of efficient zero-knowledge proofs. This innovation allows for the performance of complex and privacy-sensitive tasks without intermediaries, fostering a trustless environment with unparalleled application-level privacy. It's a testament to Ergo's commitment to creating an intelligent, user-friendly blockchain platform where security and accessibility go hand in hand.

### Secure and Accessible to All

Ergo's dedication to making blockchain security universally accessible is evident through its implementation of Non-Interactive Proofs of Proof-of-Work [(NIPoPoWs)](nipopows.md), which allow users to transact and verify with confidence without the need for a full node. This feature, requiring as little as 1 MB of data, ensures that Ergo's benefits are accessible on virtually any device, further democratizing blockchain use. Additionally, Ergo addresses blockchain sustainability through [Storage Rent](rent.md), incentivizing efficient data storage, and the [eUTXO](eutxo.md) model, which enhances privacy, scalability, and interoperability, solidifying Ergo's position as a secure and inclusive platform.

### Commodity Money and Innovation

Ergo transcends the traditional concept of a blockchain token, embodying **commodity money** with real-world consumption of resources like electricity and hardware wear and tear for mining new ERG. This approach is rooted in the practice of securing commodities with cryptography, a path first paved by Bitcoin. However, Ergo distinguishes itself with features that have remained unique for over four and a half years since its mainnet launch, including:

- Incentives for long-term stability within the mining sector.
- The implementation of [demurrage](storage-rent.md), reinforcing the notion of Ergo as a genuine commodity by incurring ledger maintenance costs.
- Support for decentralized derivatives and DeFi, enabling users to lend ERG, convert it to stablecoins, etc., without third-party intervention.
- Introduction of SigmaFi ([SigmaFi](sigmafi.md) bonds and others), a peer-to-peer DeFi solution offering comprehensive risk assessment across the network, surpassing transparency and risk management capabilities of traditional financial institutions.
- Ergo offers unparalleled support for developing [cryptographic protocols](cryptographic.md) as applications, including [non-interactive mixers](mixer.md) and [stealth addresses](stealth.md), enhancing privacy and security.
- As a platform for contractual money, Ergo excels in leveraging cryptocurrencies for real-world applications by establishing money with well-defined trust assumptions. Further discussions and insights can be accessed at [Ergo Forum](https://www.ergoforum.org/c/community/high-level-discussions/12).

Ergo's recognition as the leading Proof of Work (PoW) cryptocurrency in terms of supply locked in DeFi underscores the practical application and benefits of its features, demonstrating that its innovative solutions extend beyond theoretical concepts.

Through meticulous integration of these new insights, the narrative now fully captures Ergo's comprehensive and pioneering approach to blockchain technology, highlighting its unique strengths and contributions to the field.

By extending Bitcoin's contract-writing method, Ergo attaches a guard script and additional custom data to each coin. This feature positions Ergo as a uniquely beneficial platform for Contractual Money.

**With these features, Ergo is poised to redefine the concept of Contractual Money.**

Explore the [Ecosystem](https://docs.ergoplatform.com/uses/) section for an overview of all the current and potential uses for Ergo.


/// details | Open Source
    {type: info, open: true}
**Open Source and Decentralized:** The majority of Ergo's ecosystem is open source, permissionless, and decentralized, fostering community involvement. This allows developers to build dApps quickly and efficiently.
///

## The Genesis of Ergo

Launched in 2019 by a cohort of esteemed developers and cryptocurrency luminaries, including Alex Chepurnoy and Dmitry Meshkov, Ergo emerged from a shared vision to revolutionize the blockchain landscape. This initiative aimed to craft a supremely efficient, secure, and user-friendly platform for financial contracts, leveraging the transformative potential of blockchain technology. The inception of Ergo was driven by the recognition of a pressing need for a decentralized platform that could securely and efficiently handle the complexities of digital financial contracts, foreseeing the pivotal role of DeFi across various sectors.


### A Fair Start

From its inception, Ergo was dedicated to ensuring a fair and equitable launch, reflecting the foundational principles of Bitcoin to prevent undue influence from venture capitalists or large-scale investors. This strategy aimed not only to democratize access but also to establish a sustainable economic model for the network's growth. The mining protocol was designed to allocate a portion of the rewards to a treasury, managed by the non-profit Ergo Foundation, to support ongoing development and adoption efforts. In its first 2.5 years, the Foundation accumulated 4,330,791.5 ERGs, or about 4.43% of the total supply, with a focus on promoting Ergo's widespread use. For more information about the role and initiatives of the Ergo Foundation, please visit [here](ergo-foundation.md), and for more details on emission, see the [emission](emission.md) section.

Highlighting the strategic absence of venture capital in its early phase underscores Ergo's dedication to community-led governance and the preservation of decentralization as its core ethos. This model promotes a truly decentralized blockchain environment, where the community's interest and the platform's integrity remain paramount.



- **Fixed Supply:** Ergo has a fixed supply of 97,739,924 coins. This fixed supply combats inflation by preventing the arbitrary creation of new coins.
- **Extended Emission Schedule:** Through EIP-27, Ergo's mining rewards are extended for approximately 17.38 years, enhancing the platform's sustainability. As a result, $ERG is becoming more scarce and valuable over time.


## Why Ergo Embraces Proof-of-Work?

Ergo utilizes the [Autolykos](autolykos.md) Proof-of-Work protocol, a testament to our commitment to decentralization and fairness. Proof of Work, a protocol with a proven track record of security, enables a user-friendly environment where lightweight clients can interact directly with the blockchain, eliminating the need for intermediaries. This approach is pivotal in creating a truly programmable currency that is accessible and ready for use today.

### How Does Ergo Address Bitcoin's Challenges?

Ergo is designed to address several key challenges that are inherent to Bitcoin, enhancing the functionality, security, scalability, and privacy of the cryptocurrency ecosystem. The table below presents a comprehensive comparison between the issues faced by Bitcoin and the innovative solutions proposed by Ergo. These solutions involve advanced smart contract functionality, improved network security, efficient data structures for light clients, robust privacy tools, and scalable governance mechanisms. These improvements are geared towards creating a more inclusive and versatile blockchain platform.

| Challenges Faced by Bitcoin                                                                                                                               | Ergo's Solution                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Limited smart contract functionality                                                                                                                      | A rich language (ErgoScript) combined with the eUTXO model, Sigma protocols and transaction chaining (for turing completeness)                                                                                                 |
| Unclear network security as the block reward subsidy approaches zero and transaction fees remain low and volatile                                         | More revenue from transaction fees due to DeFi and higher usage/scalability, storage rent, mining by subpools of tokens issued on Ergo (providing even more security incentive)                                                |
| Lack of economy around state leading to miners receiving no compensation for holding the UTXO set in high cost memory - this is a big obstacle to scaling | Storage Rent provides additional rewards for miners while increasing network security. It also compensates miners for long-term holding of the UTXO set, thus allowing larger state growth and (indirectly) larger block sizes |
| Inefficient merkle tree data structure leading to inefficient light clients (Ethereum has the same problem)                                               | AVL trees leading to drastically more efficient light client verification, and thereby allowing the use of commodity hardware to verify transactions. This is also used in Plasma (layer 2 on Ergo built by Getblok.io)        |
| Weak and cumbersome optional privacy tools, some of which have been compromised                                                                           | Sigma protocols enable true peer to peer privacy. ErgoMixer is the only token-mixer that can provide better anonymity than Monero given enough utilisation.                                                                    |
| Massive scaling challenges which led to the ‘Blocksize Wars’                                                                                              | Decentralized on-chain governance based on extensive research - block size can be increased securely. NiPoPoWs enable light clients with full node security guarantees. Ergo offers more Layer-2 options than Bitcoin.         |

### How Does Ergo Address Ethereum's Challenges?

The Account model of Ethereum is imperative. This means that the typical task of sending coins from Alice to Bob requires changing the balances in storage as a series of operations. On the other hand, Ergo's UTXO based programming model is **declarative**.

ErgoScript contracts specify conditions for a transaction to be accepted by the blockchain (not changes to be made in the storage state as a result of the contract execution).

| Challenges Faced by Ethereum                                                                                                                              | Ergo's Solution                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Creating transactions and utilizing smart contracts requires paying fees in ETH and maintaining an ETH balance, thereby leading to a poor user experience | Babel Fees on Ergo allow the user to pay the transaction fee in whatever native tokens they have in a wallet                                                                                                                                                                                                         |
| Gas requirement and the ‘stopping problem’                                                                                                                | Ergo does not have gas fees, nor the stopping problem, as most computations are done off-chain. They are also cost predictable for on-chain verification and computation                                                                                                                                             |
| High gas fees and network congestion                                                                                                                      | Ergo is engineered from the ground up with long-term scaling in mind, using the most advanced and well researched tools                                                                                                                                                                                              |
| Node centralization in AWS / Infura                                                                                                                       | Anyone can run a node on Ergo (similar to Bitcoin), and while the miners may increase block size limit, there are mitigants built in to prevent this from leading to a bad node running experience                                                                                                                   |
| Censorship: Most blocks are OFAC blocks                                                                                                                   | Decentralization and PoW is deeply ingrained in Ergo’s ethos and Ergo will resist censorship in any form                                                                                                                                                                                                             |
| Centralization of Monetary Policy with Vitalik and Ethereum Foundation able to change emission at their whim                                              | All ERGs were created on day 1 in the genesis block and can only be released to miners per the pre-set emission schedule. Any proposed changes to the emission via hard fork or soft fork requires a supermajority approval of miners. Under NO circumstances can the supply of 97.7 million ERGs ever be increased. |
| Poor security and frequent hacks costing billions                                                                                                         | UTXO model and efficient onchain verification with most computation done off chain                                                                                                                                                                                                                                   |
| Poor privacy tools because the Account ledger model is not suitable for attaining high privacy                                                            | Combination of the eUTXO model and sigma protocols can achieve optional privacy superior to that achieved by Monero                                                                                                                                                                                                  |

View [Comparisons](https://ergonaut.space/en/Community/Comparisons) with other projects.



## Want to Learn More?


### Meet the Minds Behind Ergo

Ergo is powered by a team of experienced developers and researchers with strong academic backgrounds, including PhDs and multiple publications in cryptography, compiler theory, blockchain technology, and cryptographic e-cash. Our team members have extensive experience in core development for cryptocurrencies and blockchain frameworks such as Nxt, Scorex, and Waves.

One of our notable contributors, Alexander _kushti_ Chepurnoy, co-founded smartcontract.com (now known as Chainlink), served as a core developer at NXT (the pioneering full PoS blockchain), and was among the first few employees at IOHK where he was a Research Fellow and Team Scorex Manager.

To learn more about the individuals contributing to Ergo's success, visit Ergo's [Hall of Fame](https://ergoplatform.org/en/hall_of_fame/). For more information on the foundation members, refer to the [2022 Transparency Report](ergo-foundation-2022.md).

### Roadmap

Stay ahead of Ergo's journey by visiting the 'Roadmap' section [on our website](https://ergoplatform.org/en/ecosystem/#Roadmap). Here, you can explore our upcoming projects and innovative features. Each roadmap item is accompanied by detailed links for a deeper understanding.

### Resources

Here are some resources to deepen your understanding of Ergo:

- [The Ergo Manifesto](https://ergonaut.space/en/Ergo/manifesto)
- [Explore Yield-Generating Strategies on Ergo](https://ergonaut.space/en/Guides/yield)
- Our comprehensive [FAQ](faq.md)
- [cafebedouin.org: _Why Ergo_](https://cafebedouin.org/2021/12/09/why-ergo/)
- Join our community chats across the web listed at [direct.me/ergo](https://direct.me/ergo)

> _"Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital."_

