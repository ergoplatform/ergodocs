# Common Misconceptions

/// details | FUD FAQ
    type: tip

This page aims to provide some clarity around some common misconceptions that have cropped up about Ergo.
///

## Emission

###  Ergo developers can manipulate the emission

The emission process of Ergo is controlled by a transparent smart contract, which is accessible for public viewing in Ergo's source code. This contract restricts developers from arbitrarily extracting coins. Any modifications to the emission process, such as the [EIP-27](eip27.md) soft-fork, necessitate a consensus from the miners and are publicly visible on the blockchain. This capability, outlined in one of Ergo's [foundational papers](https://docs.ergoplatform.com/documents/#foundational-papers) [*'Soft Power: Upgrading Chain Macroeconomic Policy Through Soft Forks'*](https://eprint.iacr.org/2021/577.pdf), empowers miners to adjust the exact rate of emission reduction, facilitating a smooth transition to a self-sustaining network.  

### All Erg was pre-mined

A common misconception is that Ergo coins were pre-mined and stored in a smart contract, potentially giving developers undue influence over the coin supply. However, Ergo's emission process is unique and transparent. Coins were produced at the blockchain's genesis and are systematically awarded to miners for their role in securing the network and processing transactions. This approach offers advantages, such as mitigating potential inflation bugs that have troubled other blockchains when coins are generated with each block.

The emission process is governed by a smart contract, which is publicly viewable in Ergo's source code. This contract does not permit developers to arbitrarily extract coins. Any changes to the emission process, such as the EIP-27 hardfork, require consensus from the miners and are visible on the blockchain.

#### There are no *Out-of-Thin-Air* Emission in the "Coinbase" Transaction in Ergo

Ergo prohibits out-of-thin-air emission in the "coinbase" transaction, the first transaction in each block that rewards the miner. This ensures that every Ergo coin or token originates from a legitimate source and is traceable in the transaction history, maintaining the integrity and scarcity of Ergo's native cryptocurrency.

###  EFYT was an ICO

The Ergo-First-Year-Token (EFYT) was not a traditional ICO. Instead, it was an airdrop distributed on the Waves DEX to foster an early community for Ergo and gather resources for the platform's pre-launch development. EFYT tokens, swapped from the treasury, constitute less than 1% of the total supply, marking a departure from the fundraising practices associated with many ICOs.

For more information see [this page](emission.md)

### Ergo won't be able to support miners after emissions ends

After the scheduled emissions conclude in 2045, miners on Ergo will continue to be incentivized through alternative methods. One such approach involves transaction fees and Miner Extracted Value (MEV). Transactions on Ergo generate fees (paid in Ergs), with a portion of these fees awarded to miners. MEV represents the total value miners can extract from a block using tactics like reordering, front-running, and other advanced techniques. Miners can increase their MEV earnings by efficiently executing transactions in high MEV blocks, which encourages them to contribute their hash power to the network.

Another form of MEV we have on Ergo is through [**Storage Rent**](rent.md). This mechanism requires users to pay for the storage their data occupies on the network. Consequently, miners receive a consistent income stream, as they earn Ergs from fees users pay for content storage. See [this page](rent-fees.md) for more information on the potential of storage rent.

In future, Miners could also benefit from custom emission contracts as part of a Fair Initial Mining Offering (FIMO) process. These contracts reward miners with non-native tokens, ensuring new projects have equal opportunities to distribute tokens to the community while incentivizing miners to participate in mining.

Miners can also operate [off-chain execution bots](dex_bots.md) on the same machine to earn additional ERG rewards. [Machina Finance](machina-finance.md) is also developing an *extensible* off-chain bot framework to make this process simpler, so you'll be able to run one program to provide liquidity to the entire Ergo defi ecosystem. 

## Mining

###  ASICs will take over Ergo

While ASICs and FPGAs can pose centralization risks, there are currently no known serious efforts towards creating ASICs for Ergo. The Ergo algorithm is designed to neutralize any advantage ASICs might typically bring. If ASIC development becomes a threat to Ergo's decentralization, the community has the power to introduce protocol improvements via a hardfork.

###  FPGAs are already taking over Ergo

While it's true that FPGAs can achieve up to 3Mh/W, double the efficiency of the best Nvidia cards, their current impact on Ergo is minimal. This is due to a chip shortage and lack of public miners making FPGAs currently non-competitive. Even if you could buy an E300 at retail prices today, the Return on Investment (ROI) would take approximately 52 years. Furthermore, SRAM, despite its faster read/write capabilities, is not a feasible long-term option for Ergo mining due to its lower density and the algorithm's increasing memory requirements. Therefore, the claim that FPGAs are already taking over Ergo is a misconception.

### Ergo is at risk of a 51% attack

The current network status can be monitored using miningpoolstats. Even if a single entity were to control over 51% of the network's mining power, the real-world risk of an attack is very low. It is highly unlikely that a major player like 2miners would jeopardize their business by executing an attack on the network. Lithos is a project that aims to create a decentralized mining pool infrastructure.This protocol provides a low-risk opportunity for lenders to earn yield on their ERG by providing collateral to mining pools while promoting increasingly decentralized block production. This means that the project plans to enable miners to directly insert necessary transactions into blocks in a fully decentralized and trustless manner, bringing significant benefits to miners outside of just decentralization. For more information, please refer to the [Lithos project page](lithos.md).

### Ergo ignored miners who warned about the difficulty algorithm

It's important to remember, that *Ergo* is a collective community, not a single entity, The centralised component, the Ergo Foundation (EF) is essentially a network of people committed to the platform's success via spending the treasury and does not vote on matters related to development and community consensus. 

The initial concerns from miners were indeed taken into account. However, these early warnings were primarily about potential difficulties during price fluctuations, not the 'death-spiral' scenario that eventually led to the hard fork. After extensive discussions with core developers and leading miners and pools, the consensus was that the current situation, while painful in the short-term, was less painful than implementing a hard fork. The community was hopeful that as Ergo gained more traction, a stable and increasing hashrate would naturally follow, mitigating these concerns.

The unforeseen circumstances surrounding the ETH merge were exceptional and couldn't be predicted with absolute certainty. Although we had prepared for potential risks after a community developer brought this scenario to our attention, the specific details of the merge, the rapid migration of miners, and fluctuating prices surpassed our expectations, necessitating immediate intervention. We express our gratitude to the miners who intervened and donated their hash power to assist with the situation. We have since taken measures to streamline the [EIP](eip.md) process and encourage greater miner participation.

Ergo empowers miners by returning control to them in the crypto-space, adhering to the fundamental principles of decentralization. Ergo's advanced [governance](governance.md) features and the inclusion of miners in key discussions, as demonstrated by the [EIP27](eip27.md) discussions, underscore this commitment. During these discussions, the community introduced 'vote tokens' to enable miners to participate actively, further establishing Ergo as a blockchain that values and supports its miners.

### Ergo's current difficulty adjustment algorithm is being manipulated

Post EIP-27 implementation, the more frequent difficulty adjustments have inadvertently made Ergo more appealing for profit hoppers. It's important to note that some degree of this activity is inevitable in any blockchain network. Presently, the algorithm effectively maintains an average block time of 120 seconds, as intended. 

While there's been a noted fluctuation in the hashrate of a particular solo pool, this variance accounts for only about 10% of the total hashrate. The actual influence this has on the profitability for the wider mining community is being closely examined.

We urge the Ergo community—both miners and developers—to actively participate in this conversation. Assess the real-world implications and the validity of these concerns. If necessary, formulate and suggest an EIP for potential modifications. Ultimately, the future trajectory of Ergo's algorithm rests in the hands of its community.

## Organisational

### Ergo's marketing sucks.

Ergo's marketing strategy is rooted in community engagement and organic growth, diverging from conventional marketing tactics often employed by other projects. This strategy prioritizes the cultivation of a well-informed and actively involved community. Ergo's unique features and capabilities serve as its primary selling points, and the team is committed to letting these attributes stand out on their own. Regular updates and developments are communicated through various channels, including social media, blog posts, and community meetings.

The marketing efforts are primarily aimed at increasing awareness, educating the community, and highlighting the unique features and capabilities of Ergo. The objective is to stimulate organic growth and attract users who value the platform's technological advantages and commitment to privacy, security, and genuine decentralization. The [Sigmanauts](sigmanauts.md) programme has been successful, with mature pathways that allow for a smooth transition for individuals to make meaningful contributions and help shape and grow Ergo. This resilient marketing approach was designed to kickstart truly organic and decentralized compounding growth. Now, with their own treasury, the Sigmanauts are making proposals and expenditures, running campaigns, creating content, attending events, and planning for the future.

### Ergo won't succeed without VC investment

Ergo's success is not dependent on venture capital (VC) investment. While VC funding can provide resources for growth, it can also lead to centralization and conflicts of interest. Ergo is designed to be a decentralized, community-driven project, and its development and growth are fueled by the community and the team's efforts. The project has made significant progress without VC funding, demonstrating that it can thrive and innovate without such investment. Ergo's robust technology, active community, and commitment to decentralization are its main drivers of success.

###  The Foundation is centralized

The Ergo Foundation provides guidance in the early stages of the network, but its influence is transitional. As the network matures, the Foundation's role diminishes, paving the way for a fully community-driven ecosystem. For more information please see the [Ergo Foundation Transparency Report](ergo-foundation-2022.md)

###  Ergo could not operate without its foundation

The Ergo Foundation undoubtedly plays a pivotal role in shaping the trajectory and fostering the development of Ergo. However, as the ERG token ecosystem evolves, it's steadily becoming more decentralized and less dependent on the Foundation or any singular centralized authority. Emblematic of its decentralized ethos, Ergo operates as an open-source, permissionless platform. This ensures that developers, innovators, and enthusiasts can introduce applications or tokens without seeking explicit endorsement or intervention from the Foundation.

The development momentum would persist, and mechanisms like storage rent would enable miners to access and utilize the Foundation's funds. Many entities, encompassing mining pools, exchanges, dApps, and even teams like Spectrum Labs and ErgoPad, actively maintain the network nodes and contribute to its vitality.

The potential hesitancy of traditional exchanges to list Ergo without an overseeing body might arise. However, the decentralized spirit of the crypto realm ensures that even in the absence of the Ergo Foundation, decentralized exchanges (DEXs) and peer-to-peer platforms would seamlessly facilitate the trading of Ergo.

Although the Foundation serves as a vital community conduit, fostering discussions and spearheading initiatives, the continuity of Ergo isn't solely tied to its existence. Should the Foundation ever disband, the community and other contributors are well-equipped to carry the torch forward. The [Sigmanauts](sigmanauts.md) programme is the beginnings of this, who tries to create a community of users of the Ergo blockchain to explore how it can be of benefit, and they try to represent the interests of users in the larger Ergo ecosystem and indicates that the community can lead and maintain momentum even without the Foundation's direct involvement.


### Ergo is a 'Russian coin'

Ergo is a global project and is not tied to any specific country or region. While some of the developers and contributors may be based in Russia, Ergo's community and user base are spread across the world. The project's decentralized nature ensures that it is not influenced by the policies or politics of any single country. Ergo's primary goal is to provide a robust, secure, and decentralized platform for all users, regardless of their geographical location.

###  Ergo is an unregistered security

Ergo's status under the SEC's regulations is a gray area, as is the case with many cryptocurrencies. However, based on the Howey Test, Ergo is not considered a security. Ergo has one of the most extensive public distributions among smart contract platforms, and the initial allocation by the Ergo Foundation was primarily to kickstart the ecosystem.

### The Foundation's actions are causing price depreciation

The Ergo Foundation's monthly expenses are a minuscule portion of the total trading volume, equivalent to the mining rewards of 1-2 days. Most of these expenses are paid in ERG, meaning there are minimal direct liquidations. The recipients of these payments have the freedom to manage them as they see fit. It's worth noting that our developers often work for compensation below the market rate. For a detailed breakdown of the Foundation's expenditures, refer to the [Ergo Foundation 2022 Transparency Report](ergo-foundation-2022.md).

## Ecosystem

### Ergo's Total Value Locked (TVL) ratio is too low

Ergo, a relatively new network, has dedicated substantial time and resources to establish a robust base infrastructure. This foundational work is now bearing fruit as the Total Value Locked (TVL) is witnessing a swift uptick due to the ease of deploying decentralized applications (dApps) on the network. For the most recent TVL statistics, platforms such as DeFi Llama provide up-to-date information. The recent introduction of the Rosen Bridge is anticipated to significantly enhance liquidity by enabling seamless transfers from Cardano and other blockchain networks. These networks can leverage Ergo's advanced DeFi ecosystem using wrapped tokens, thereby augmenting the utility and value of Ergo.

### The ecosystem isn't growing

Ergo's ecosystem is steadily growing. The development team is continuously working on new features and improvements, and the community is actively contributing to the project's growth. The number of decentralized applications (dApps) built on Ergo is increasing, and more developers are choosing Ergo for their projects due to its unique features and capabilities. The growth of the ecosystem can be tracked on various platforms such as DefiLlama and Artemus.

### This new stablecoin will kill SigmaUSD

The introduction of a new stablecoin does not necessarily mean the end of SigmaUSD. The cryptocurrency market is vast and diverse, and there is room for multiple stablecoins to coexist. SigmaUSD has unique features that set it apart from other stablecoins, such as its algorithmic design and the security of the Ergo blockchain. Furthermore, competition in the stablecoin market can lead to innovation and improvement, benefiting the users in the end.

## Technical

###  eUTXO is too difficult for developers

The extended UTXO (eUTXO) model, adopted by Ergo, might initially seem complex, especially for developers accustomed to the account-based model. However, it offers increased flexibility and security. Over time, as more resources and tutorials become available, the learning curve will flatten, making it more accessible for all developers.

### Ergo should've used an easier language than Scala

Ergo utilizes Scala as its primary language due to its cross-platform capabilities, conciseness, efficiency, and multi-paradigm nature. ErgoScript, based on Scala, is used for scripting, but off-chain code can be written in any language. Developers have access to a variety of tools and Software Development Kits (SDKs) for JVM, Rust, and JS/TS. Scala's unique features, such as the ability to run the same code on JVM and JavaScript natively, its concise syntax, and its ability to use primitive unboxed types for efficiency, make it a suitable choice for Ergo. 

### Ergo's lack of in-built Sharding means it won't scale with atomic composability

This misconception arises from a misunderstanding of how Ergo handles scalability and atomic composability. While it's true that Ergo doesn't use in-built sharding, it employs other strategies to ensure scalability without compromising atomic composability. Ergo optimizes the use of resources within the constraints of existing blockchain platforms, rather than resorting to unproven technologies. It also uses the eUTXO model and ErgoScript to allow for the atomic execution of complex, multi-stage transactions within a single transaction. Layer 2 solutions like Hydra state channels also contribute to atomic composability. Furthermore, concepts like ACE could enhance the execution of complex and composable smart contracts. Therefore, Ergo's approach to scalability and atomic composability is not reliant on in-built sharding.

###  Proof of Work is not sustainable

The sustainability of Proof of Work (PoW) is frequently debated. Critics argue that it's energy-intensive and thus environmentally unfriendly. While there's truth to the energy consumption, it's essential to put it into perspective. If the energy used in PoW is directly proportional to its value and security, then its consumption can be justified. Moreover, as technology advances, more efficient and environmentally-friendly mining solutions will emerge, further diminishing the environmental concerns.

### Proof of Work may face increased regulatory scrutiny

While Proof of Work (PoW) has been subject to criticism in media outlets, it remains a complex issue to address legally. Furthermore, even if legal challenges arise, implementing a ban on PoW is a daunting task, as evidenced by attempts in countries such as China. It is our belief that PoW-based cryptocurrencies that have had a fair launch stand the best chance of weathering potential regulatory challenges.

### Ergo is a privacy coin

While Ergo does offer privacy features, it is not solely a privacy coin. Ergo's protocol allows for the creation of private transactions, but it also supports transparent transactions. This flexibility allows users to choose the level of privacy they want for their transactions. It's important to note that privacy features are not unique to Ergo. Other major cryptocurrencies like Bitcoin and Ethereum also have mixing and privacy features at the application layer, yet they are not classified as privacy coins. Ergo's privacy features are optional and are part of a broader set of capabilities aimed at creating a robust, flexible, and secure blockchain platform.


### Ergo transactions are too slow

Ergo's 2-minute block interval, while seemingly slow, is a strategic choice to ensure network security and stability, especially for a system that supports complex smart contracts. This interval provides a buffer for various network activities, aids in decision-making processes, and adds a layer of security against potential threats. Additionally, Ergo can employ scaling methods like "weak blocks" to enhance transaction throughput and confirmation speed. 

In addition to the 2-minute block interval, Ergo can utilise scaling methods such as the recently proposed ["weak blocks"](weak-blocks.md) to improve both the transaction throughput (TPS) and the speed of transaction confirmations. Weak blocks are block candidates with lower difficulty levels than standard blocks. They are propagated through the network along with new transactions, effectively optimizing network bandwidth usage. 

### Ergo's development is too slow

While Ergo's development pace might seem slower compared to other blockchain projects, it's important to understand the reasons behind it. Ergo introduces a new paradigm in the blockchain space, specifically the eUTXO model, which offers enhanced security, simplicity, support for off-chain protocols, and improved scalability. Implementing this model requires a deep understanding of its intricacies and potential challenges, which naturally takes time. Additionally, Ergo is committed to a fair start, avoiding practices like pre-mining or ICOs to ensure a more equitable token distribution. This approach might slow down the initial development and growth of the project, but it's a strategic decision to ensure long-term sustainability and fairness.

### Ergo is at risk of quantum attacks

While the development of practical quantum computers is still speculative, Ergo is aware of the potential threat they pose. Current post-quantum (PQ) digital signature schemes, such as Lamport signatures, have limitations and are not yet ready for widespread use. Ergo uses efficient sigma-protocols, but post-quantum alternatives are still considered impractical. Therefore, it's premature to implement changes to address quantum computing risks. In case of a crypto-disaster, like the advent of efficient quantum computers or vulnerabilities in elliptic curves, the best response would be to transition to a blockchain with robust post-quantum security measures. Until the threat of quantum computing becomes more imminent, the focus should be on monitoring developments in the field, exploring potential post-quantum solutions, and planning for a smooth transition to a more secure blockchain if necessary.

For more information, watch [Quantum Computing and Resistance | Ergo Clips](https://www.youtube.com/watch?v=A5SJy7c3bfs&ab_channel=ErgoClips)

### There is nothing unique in Ergo

Ergo stands out from other blockchain projects due to its unique features and capabilities. One of these is ErgoScript, a powerful and secure scripting language that supports a wide range of features. These include ring signatures, atomic swaps, multiple currencies, and self-replicating scripts, providing developers with the tools they need to create complex and secure applications.

Another distinctive feature of Ergo is its use of Sigma Protocols. These non-interactive zero-knowledge proofs can be composed using basic *AND/OR* logic, offering a robust and flexible framework for creating secure and private transactions.

Ergo also supports multi-stage contracts, extending the standard threshold `m‐of‐n` signature protection. This allows for the specification of complex recipients of these coins, facilitating the creation of intricate, secure, and efficient smart contracts.

The use of Non-Interactive Proofs of Proof of Work (NIPoPoWs) is another unique aspect of Ergo. NIPoPoWs enable truly decentralized Ergo DApps and off-chain protocols via light clients, enhancing the overall efficiency and scalability of the network.

Ergo also implements a feature known as Storage Rent, which helps manage blockchain bloat and turns it into a profitable venture. This ensures the long-term sustainability of the network by incentivizing efficient use of storage space.

Finally, Ergo employs the eUTXO model, which enhances privacy, scalability, and interoperability. By extending Bitcoin's contract-writing method, Ergo attaches a guard script and additional custom data to each coin, positioning Ergo as a uniquely beneficial platform for Contractual Money.

For more detailed information, please refer to the [Discover Ergo: The Blockchain of the Future](why.md) document.


