# FAQ

This page aims to provide a background on Ergo and answers to some of the most frequently asked questions. 

## Background

- Ergo is currently available on the following [wallets](https://ergoplatform.org/en/wallets/) and [exchanges](https://ergoplatform.org/en/exchanges/). 
- The development roadmap can be seen [here](https://ergoplatform.org/en/ecosystem/#Roadmap).
- To see the applications currently running on Ergo, check out [sigmaverse.io](https://sigmaverse.io/).
- To read about Ergo from a less technical perspective, visit [ergonaut.space](https://ergonaut.space/en/home). 
- If you want to mine, see the [Miners Handbook](https://ergonaut.space/en/Guides/Mining).

### What is Ergo?

Ergo is a Resilient Platform for Contractual Money. It is designed to be a platform for applications with the main focus to provide an efficient, secure and easy way to implement financial contracts.

To achieve this goal, Ergo includes various technical and economic improvements to existing blockchain solutions. Every coin in Ergo is protected by a program in ErgoScript, which is a powerful and protocol friendly scripting language based on Σ-protocols. It specifies conditions under which a coin can be used: who can spend them, when, under what external conditions, to whom, and so on.

Extended support of light nodes makes Ergo friendly for end users and allows it to run contracts on common devices such as mobile phones trustlessly. To be useful in the long-term, Ergo is strictly following a long‐term survivability approach — it uses widely-researched solutions that are not going to result in security issues in the future, while also preventing performance degradation over time with a new economic model.

Finally, Ergo is a self‐amendable protocol, that allows it to absorb new ideas and improve itself in the future. The focuses on long‐term survivability and self‐amendability are what give Ergo its resiliency.

### Why '*Ergo*'? 

"Ergo" is a versatile term with deep roots in both Latin and Greek. In Latin, "ergo" serves as a conjunction meaning "therefore," commonly used to introduce logical conclusions. This reflects the cryptocurrency's design, which aims for logical, straightforward, and efficient use.

In Greek, the related word "ἔργον" (ergon) translates to "work" or "task," which subtly nods to the work or effort that goes into mining and maintaining the blockchain—key aspects of cryptocurrency functioning. The choice of the name "Ergo" cleverly plays on these themes, emphasizing the coin's user-friendly and work-efficient ethos, hence the description of its design as ergonomic. This aligns with the overall philosophy of reducing effort and increasing effectiveness in its applications and transactions.

Additionally, "ERG" is the ticker symbol for the Ergo cryptocurrency, further tying back to the term's roots in work and energy (erg being a small unit of energy in physics), which metaphorically could be seen as the "energy" users invest in the network. 

The name "Ergo" encapsulates both a philosophical approach and a practical application, making it a fitting choice for a digital currency designed to be efficient and logical.

### Where can I see analytics on use?

[analytics](analytics.md) provides an overview of various metrics available.


### How does it differ from Bitcoin?

Ergo is a cryptocurrency that builds upon the same UTXO model as Bitcoin but extends its functionality with additional features. Ergo allows for more complex programmability by providing access to the entire spending transaction and the block solution in the execution context. This enables the creation of Turing-complete contracts and the implementation of contractual money, where digital coins can be explicitly bound to a contract in the form of executable code.

### What is contractual money?

Contractual money is digital money that is bound to a contract in the form of executable code, which enforces specific rules and conditions for its usage. This is in contrast to traditional money, where contracts are external to the money itself and may be in the form of laws, corporate terms, or informal agreements. Contractual money allows for more precise control over how the money is spent and can be used to implement various use cases, such as microcredit systems or local exchange trading systems.


### When was Ergo launched?

Mainnet July 2019. Before this, there was *Ergo-First-Year-Token*

**What is EFYT?**

Ergo-First-Year-Token was airdropped and distributed on Waves DEX starting with a 100,000 EFYT airdrop in May 2017. EFYT served the dual purposes of helping build an early community of stakeholders and enthusiasts for Ergo and raising a small number of funds for the platform before launch to fund development, promotion etc. EFYT is strictly a Waves token and is not the same as an Erg; the Ergo mainnet native token is mined after Ergo's mainnet launch.

The max supply of EFYT is 1,970,945.0. This is 10% of the first year of Ergo token emission and the same number of Ergs that the Treasury will receive, meaning that the Treasury will have received 1,970,945.0 Ergs during year 1, sufficient to swap the max supply of EFYT for Erg.

### Why 97,739,924?

> A pre-agreed smart contract controls emission in Ergo, so we tried to have a simple enough emission curve with the total limited supply being close to 100M (and emission to be done in 8-10 years).

The max supply is simply the amount needed to create the initial genesis state: 

- A box with proof-of-no-premine (1 ERG)
- [Foundation treasury](https://explorer.ergoplatform.com/en/addresses/4L1ktFSzm3SH1UioDuUf5hyaraHird4D2dEACwQ1qHGjSKtA6KaNvSzRCZXZGf9jkfNAEC1SrYaZmCuvb2BKiXk5zW9xuvrXFT7FdNe2KqbymiZvo5UQLAm5jQY8ZBRhTZ4AFtZa1UF5nd4aofwPiL7YkJuyiL5hDHMZL1ZnyL746tHmRYMjAhCgE7d698dRhkdSeVy) (4,330,791.5 ERG)
- [Miner Reward Box](https://explorer.ergoplatform.com/en/addresses/2Z4YBkDsDvQj8BX7xiySFewjitqp2ge9c99jfes2whbtKitZTxdBYqbrVZUvZvKv6aqn9by4kp3LE1c26LCyosFnVnm6b6U1JYvWpYmL2ZnixJbXLjWAWuBThV1D6dLpqZJYQHYDznJCk49g5TUiS4q8khpag2aNmHwREV7JSsypHdHLgJT7MGaw51aJfNubyzSKxZ4AJXFS27EfXwyCLzW1K6GVqwkJtCoPvrcLqmqwacAWJPkmh78nke9H4oT88XmSbRt2n9aWZjosiZCafZ4osUDxmZcc5QVEeTWn8drSraY3eFKe8Mu9MSCcVU) with the required ERG for 2,080,800 Blocks according to the emission schedule until rewards equal 0 and storage rent and EIP-27-reemission-box takes over (93,409,132 ERG). 

The treasury box is protected by a vesting smart contract that ensures an initial unlocked amount and then only releases an amount of ERG that provides funds for 2.5 years (never exceeding 10% of the circulating supply). All of this results in these specific amounts.

In total, this happens to be 97,739,924.5 ERG.

For proof-of-no-premine, the pre-genesis state in Ergo contains block hashes from Bitcoin and Eth and also headlines from the Guardian, Vedomosti and Xinhua around the moment of launch, which can be seen in [mainnet.conf](https://github.com/ergoplatform/ergo/blob/1935c95560a30b19cdb52c1a291e8a389ba63c97/src/main/resources/mainnet.conf#L11)

```scala
   /**
    * Generates a genesis box that contains proofs of no premine.
    * This is a long-living box with special bytes in registers.
    * @param chainSettings Chain settings of the Ergo network
    * @return The genesis box with the given properties
    */
  private def noPremineBox(chainSettings: ChainSettings): ErgoBox = {
    // create a map of ErgoBox non-mandatory registers with the premine proofs
    val proofsBytes = chainSettings.noPremineProof.map(b => ByteArrayConstant(b.getBytes("UTF-8")))
    val proofs = ErgoBox.nonMandatoryRegisters.zip(proofsBytes).toMap
    // create a genesis box with a value of CoinsInOneErgo, a proposition script of FalseLeaf, an empty tokens sequence, and the premine proofs in non-mandatory registers
    createGenesisBox(EmissionRules.CoinsInOneErgo, Constants.FalseLeaf, Seq.empty, proofs)
  }

```

```JSON
 {
"boxId": "b8ce8cfe331e5eadfb0783bdc375c94413433f65e1e45857d71550d42e4d83bd",
"value": 1000000000,
"ergoTree": "10010100d17300",
"assets": [],
"creationHeight": 0,
"additionalRegisters": {
  "R5": "0e42307864303761393732393334363864393133326335613261646162326535326132333030396536373938363038653437623064323632336337653365393233343633",
  "R6": "0e464272657869743a20626f746820546f727920736964657320706c617920646f776e207269736b206f66206e6f2d6465616c20616674657220627573696e65737320616c61726d",
  "R8": "0e45d094d0b8d0b2d0b8d0b4d0b5d0bdd0b4d18b20d0a7d0a2d09fd09720d0b2d18bd180d0b0d181d182d183d18220d0bdd0b02033332520d0bdd0b020d0b0d0bad186d0b8d18e",
  "R7": "0e54e8bfb0e8af84efbc9ae5b9b3e8a1a1e38081e68c81e7bbade38081e58c85e5aeb9e28094e28094e696b0e697b6e4bba3e5ba94e5afb9e585a8e79083e58c96e68c91e68898e79a84e4b8ade59bbde4b98be98193",
  "R4": "0e4030303030303030303030303030303030303031346332653265376533336435316165376536366636636362363934326333343337313237623336633333373437"
}
```
The code for the emission schedule can be found [here](https://github.com/ergoplatform/ergo/blob/e6086e23ecd45f1e01a3e4c0344f003cec1a5b11/src/test/scala/org/ergoplatform/mining/ErgoMinerPropSpec.scala#L24)





### What is the *Ergo Foundation*?


The [Ergo Foundation](https://ergoplatform.org/en/foundation/) is a community-driven entity focused on:

  - Promoting non-breaking development of Ergo Platform protocol;
  - Promoting the widespread adoption and use of Ergo Platform and its native token (ERG);
  - Developing the ecosystem around Ergo;
  - Promoting the use of Ergo Platform and blockchain technology for social good;
  - Supporting truly decentralised infrastructure and;
  - Supporting privacy as a basic human right.


To fund development, promotion, events, and any other activities which may advance the platform, Ergo has in place a Treasury, which will receive **4.43%** of the Ergs released during emission. During the first two years post‐mainnet launch, the Treasury received 7.5 Ergs per block. 

### What is the [Emission Schedule](https://ergoplatform.org/en/blog/2019_05_20-curve/)?

Ergo has a maximum supply of **97,739,925** Ergs, to be completed by 2045. The block reward lowers to 3ERG in 2026. You can see this emission schedule on [ergo.watch](https://ergo.watch/emission)

## Future Plans & Ecosystem Growth

### What are Ergo's future plans, especially in terms of how you grow your ecosystem?

Position Ergo as a basis for unstoppable, grassroots economies, serving as a decentralized central bank digital currency (CBDC) for the people. See 'General Overarching Ergo Design and Implementation Roadmap' amongst other roadmaps here: [Roadmap](roadmap.md#resources)

Continue to solve pain points in development. UX is a big one which will be helped hugely by sub-blocks. We have two hardware wallets just about ready (Ledger, Keystone), more courses, tutorials, guides, resources, etc appearing daily making it easier to onboard developers.

[Developer Getting Started Guide](dev/get-started.md)

Bulk of our issue is lack of T1 exchanges and professional marketing. Rosen is helping here by connecting extensive liquidity to our DeFi stack (for example, DOGE could launch HodlDOGE on-chain, rsBTC can go in the mixer, etc)

Will continue to push with Kraken and other OnRamps

You can mint new tokens, nfts, and transact them for next to nothing. Everything is open source. It's a fun ecosystem to play in and could have mass appeal once the above is solved.

[Project Management Board 1](https://ergo.getgrist.com/jf9KPR1HUDJH/Project-Management/p/24)
[Project Management Board 2](https://ergo.getgrist.com/jf9KPR1HUDJH/Project-Management/p/16)

DAOs are now live and the community can help to grow the ecosystem in a more structured and decentralised way.

[Sigmanauts Program](contribute/sigmanauts.md)

We have dozens of volunteers who drive ergo forward already. We're not reliant on a centralised entity or group pushing things forward. This kind of growth is a slow-burn but cummulative. I've been applying Start up Growth Engineering to Ergo, optimising for agency, pushing decision ownership to the front line, appropriate alignment, removing barriers to necessary, creating linear resources so that we're best positioned to drive compounding growth via network effects.

## Artificial Intelligence (AI)

### What is Ergo's view on the current AI agent space, as many ecosystems are trying to attract developers to build agents on top of their platforms?

Ergo blockchain is well-suited for Artificial Economic Intelligence (AEI) due to its simplicity in handling contracts, enabling easy issuance of peer-to-peer financial instruments like bonds. Its flexible contract templates allow for seamless modifications, supporting the evolutionary development of AEI-to-AEI agreements.

[Artificial Economic Intelligence On (Ergo) Blockchain - Ergo Forum](https://www.ergoforum.org/t/artifical-economic-intelligence-on-ergo-blockchain/4429)

Community has recently started building SharkNet - a curated dataset of ErgoScript examples to train better dev tools.
[SharkNet GitHub](https://github.com/The-Last-Byte-Bar/SharkNet/tree/main)

And there is an AI bot trained on all our docs, whitepapers and chats, available on our website or directly here:
[Ergo Documentation AI Chatbot](https://www.chatbase.co/chatbot-iframe/zxB2uzZfYoHIpA98eTzgM)

## Privacy

### How important is privacy for Ergo currently, and how do you plan to avoid the issues that some privacy-focused projects have faced, like legal challenges?

Privacy is a core principle for Ergo, considered a fundamental human right, and is implemented through opt-in protocols and robust cryptographic methods within its eUTXO model, ensuring strong protection while maintaining necessary transparency. To sidestep legal challenges, Ergo operates as a fully open-source platform with clear documentation and transparent development practices.

Innovations like ErgoMixer—the first non-custodial, programmable, non-interactive mixer offering features such as token mixing, covert addresses, [stealth addresses](uses/stealth-address.md), SigmaUSD minting, and Tor support—demonstrate this commitment. More advanced ideas like [SigmaJoin](eco/sigmajoin.md#key-advantages) and [Mixicles](uses/mixicles.md) are also proposed.

Contracts can't be shut down. We avoid legal challenges by pushing for completely unstoppable designs, educating the community on Knowing Their Assumptions and best practices.

[Know Your Assumptions (KYA)](contribute/standards/kya.md)

## Competitiveness & Differentiation

### How do you see this space in terms of its competitiveness and how are you going to really differentiate yourself?

There are very few smart contract platforms that align with the original vision for Bitcoin: Grassroots distribution (95% of tokens to the community), UTXO-based, Proof-of-Work, simple assumptions, avoiding exotic protocols or overcomplicating things. For building protocols that support real value, Ergo ticks all the boxes apart from market-share.

[Ergo as the Endgame for Crypto? - Ergo Forum](https://www.ergoforum.org/t/ergo-as-the-endgame-for-crypto/5076)

Ergo differentiates itself in a competitive landscape by using a UTXO-based model rather than the account-based systems common in platforms like Ethereum. This simplifies contract development and reduces complexity compared to coding in Solidity. This approach resonates with Bitcoin enthusiasts who favor smart contracts aligned with Bitcoin’s principles.

This page covers key aspects of the Ergo contract model which makes it different:
[ErgoScript Paradigm](dev/scs/index.md#paradigm)

Design patterns will continue to mature, and we'll keep developing innovative protocols and designs that re-capture the cypherpunk spirit:

- [ChainCash: A Practical Approach to Elastic Money Creation](uses/chaincash.md)
- [Dexy: A Seigniorage-Based Stablecoin](eco/dexy.md)
- [Blockchain-based trustless derivatives: HashrateCoin and RandomCoin - Ergo Forum](https://www.ergoforum.org/t/blockchain-based-trustless-derivatives-hashratecoin-and-randomcoin/4999)

While the bulk of the market may not prioritize these aspects, builders do, and their dApps attract a wider audience.

For the everyday user, the Pure Degenerate Finance (DegFi) dApps on Ergo enable high-risk, high-reward opportunities through transparent game-theoretic interactions.

[Degenerate Finance (DegFi)](uses/degfi.md)

These are launching at an accelerated rate as the base layer maturity now allows it, and could bring in a huge amount of people with the right design, incentives and hype.

## Discussions

### Why Scala? 

Ergo's primary language is Scala. Similarly, the scripting language used by Ergo, ErgoScript, is also based on Scala, but the off-chain code can be written in any language. Developers have access to a growing selection of tools and Software Development Kits (SDKs) for JVM, Rust and JS/TS.


Scala has several features that set it apart from other JVM languages. 

- Firstly, it is truly cross-platform, as the same code can run on JVM and JavaScript natively. This is a feature that is not found in many other languages. 
- Additionally, key ecosystem libraries for Scala support all platforms, and the popularity of Scala.js and Scala-native is increasing. 
- Another advantage of Scala is its conciseness, both in terms of syntax and conceptual level. 
- Despite its high-level nature, Scala can also be more efficient than similar Java code due to its ability to use primitive unboxed types, and the ability of the Scala compiler to perform code specialization. 
- Furthermore, Scala is multi-paradigm, allowing for the combination of OOP, FP, and LP, making it suitable for a wide range of domains. 
- Lastly, Scala3 brings even more powerful features such as metaprogramming and tools for zero-cost abstractions.

### How fast is Ergo?

TPS (Transactions Per Second) is not a useful metric. On Ergo Reference Node v.5, TPS is estimated to be a minimum of 47.5 tx/s. However, transactions can happen in three scaling layers or levels:

- L0: Ergo Reference Nodes, which can be bootstrapped using NiPoPoWs proofs and UTXO set snapshots.
- L1: Ergo has extensions that allow for a wide variety of scaling solutions such as Sharding, Hydra, or BitcoinNG-style macroblocks.
- L2 (off-chain): Ergo should be compatible with the Lightning Network, Rainbow Network, and many more. The implementation here will depend on the needs of the applications being built on Ergo.

The general idea is that many transactions can happen in L1 or L2 and these transactions can be bundled and settled on the L0 layer of the Ergo blockchain using a single transaction. Thanks to the high flexibility of ErgoScript programming model, many different protocols are possible, each one solving scalability problem in a specific domain (like simple payment transactions).
Ergo blockchain can be thought as common settlement layer for many L1/L2 protocols and applications.

See the [scaling](scaling.md) page for more information.

## Mining

### What about energy consumption? 

- [Proof of Work, Energy & Ergo](https://ergoplatform.org/en/blog/2022-03-29-proof-of-work-energy-and-ergo/)

### Why was non-outsourceability turned off?

Autolykos v1 originally had non-outsourceability built-in to prevent mining pools on Ergo. However, it became apparent that it's only possible to avoid pools with smart contracts. So, they  (the miners) turned it off so that not only larger players could take advantage of the loophole. Ergo is now focusing on memory hardness to keep mining as fair as possible, which should help prevent ASICs mining at least. There are also some improvements for pooling, e.g. Stratum 2 protocol. 


> ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044) was presented by Alex Chepurnoy at the WTSC workshop associated with Financial Cryptography and Data Security 2020 in Malaysia



- It's also discussed here on 'Unblocked with Robert Kornacki' [(14:45)](https://www.youtube.com/watch?v=2sbTMrQwWOw&feature=youtu.be)

Mining pools have certain benefits just now being exposed by Ergo, like more equitable token distribution for dApps/ projects. This is now available to miners on GETBLOK.io, using the world's first *working* SmartPools/subpooling system.

### What about 51% Attacks?

Mining pools offer a buffer against network attacks as the hash rate is distributed across thousands of individual miners.

The memory hardened aspect of ergo also makes this attack vector more expensive as there is no ASIC support to rent. With the collective rentable rigs, there are more viable paths to a 51% attack. In theory, someone could build a massive GPU farm to try to launch such an attack. If a bad actor can rent a warehouse of ASIC and mine on a small chain with 51% attacks is a viable option.

Usually, this attack is made for profit, and massive dumping occurs on an exchange as it is occurring. The attacker will dump tokens on a business and then "double-spend" them back into their wallet. The current exchange situation doesn't provide the liquidity for a viable offramp, and the rentable ASIC support isn't an option. 

Other coins like Ethereum classic are a bad comparisons, as they shared the same mining algorithm as Eth. One could buy more than 100% of the hash rate of eth classic on NiceHash, and it's not the same case for Ergo. Ergo also believes in the 'Good Miner' principle; in the case of Bitcoin - it was a good thing 51% existed. 

### How will miners be supported after emissions?

After the scheduled emissions conclude in 2045, miners on Ergo will continue to be incentivized through alternative methods. One such approach involves transaction fees and Miner Extracted Value (MEV). Transactions on Ergo generate fees (paid in Ergs), with a portion of these fees awarded to miners. MEV represents the total value miners can extract from a block using tactics like reordering, front-running, and other advanced techniques. Miners can increase their MEV earnings by efficiently executing transactions in high MEV blocks, which encourages them to contribute their hash power to the network.


Another incentive for miners on Ergo is through [**Storage Rent**](rent.md). This mechanism requires users to pay for the storage their data occupies on the network. Consequently, miners receive a consistent income stream, as they earn Ergs from fees users pay for content storage. [This post](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/) provides insight into future mining rewards from storage rent.

Miners can also benefit from custom emission contracts as part of a Fair Initial Mining Offering (FIMO) process. These contracts reward miners with non-native tokens, ensuring new projects have equal opportunities to distribute tokens to the community while incentivizing miners to participate in mining.

Moreover, miners can operate [off-chain execution bots](dex_bots.md) on the same machine to earn additional ERG rewards. [Machina Finance](machina-finance.md) is also developing an *extensible* off-chain bot framework.

In summary, miners on Ergo are incentivized through transaction fees (including MEV), storage rent, custom emission contracts that reward non-native tokens as part of the FIMO (Fair Initial Mining Offering), and more.


### Is Proof of Useful Work being considered?

While Proof of Useful Work (PoUW) is an interesting concept, it is still in the research phase. Ergo, being open to implementing new ideas, is willing to explore PoUW. However, a radical change to Ergo's consensus mechanism that requires a hard fork would likely be beyond the scope and resources of Ergo's small core development team and limited budget.

Currently, Ergo is considering conducting preliminary research and establishing specifications for PoUW, but its actual usefulness is still uncertain. It is difficult to make a definitive judgment at this time.

PoUW is an intriguing concept, but there are practical challenges associated with its implementation. The [Ofelimos paper](https://iohk.io/en/blog/posts/2022/08/16/introducing-ofelimos-a-proof-of-useful-work-consensus-protocol/) has made a breakthrough in terms of security definitions, but it is important to find a concrete approach that avoids potential private optimizations.

From an economic standpoint, PoUW introduces various interesting and possibly unconventional dynamics, as someone would need to pay for useful work. In the worst case scenario, the payer could collude with miners.

Therefore, during the bootstrapping phase, it seems necessary to have rewards determined by the protocol.

The most realistic option, it seems, would be to launch a PoUW sidechain. However, what other possibilities could be explored? Furthermore, what options could benefit the Ergo main chain and its ecosystem?

- [See previous community discussion - Aug 2022](https://t.me/ergoplatform/292754)

## How can I stake my Erg?

Ergo is a PoW (**Proof of Work**) coin, not a PoS (**Proof of Stake**), which means that blocks are validated by miners, not by stakes; therefore, you can't stake Erg directly.

However, it is possible to earn some yield from your ERG in combination with Ergo in liquidity pools, tokenisation of dApps, trading bots, lending platforms, and other mechanisms. 

You can 'stake' native tokens on Ergo in some form (on ergopad.io *live*, Night Owl Casino *soon*, ErgoMixer *soon*,+ more)  

For more info on earning off your Erg, look at the [Yield guide](https://ergonaut.space/en/Guides/yield).


## Quantum 

The development of practical quantum computers remains a subject of speculation, and their exact timeline is unclear. In anticipation of this potential threat, various post-quantum (PQ) digital signature schemes have been proposed, such as Lamport signatures. However, these PQ schemes often face limitations in terms of efficiency, thorough study, and standardization.

Ergo employs an efficient class of zero-knowledge proofs known as sigma-protocols, but the known post-quantum alternatives are still considered exotic and impractical for widespread use. As a result, it may be premature to implement any concrete changes to address the potential risks posed by quantum computing.

In the event of a crypto-disaster—such as the development of an efficient quantum computer, number-theoretical attacks on elliptic curves, or other unforeseen vulnerabilities—transitioning to a blockchain with robust post-quantum security measures would be the best course of action. 

Until the threat of quantum computing becomes more imminent or tangible, it may be more productive to focus on monitoring developments in the field, exploring potential post-quantum solutions, and considering strategies for smoothly transitioning to a more secure blockchain in the event of a crypto-disaster.

- [Quantum Computing and Resistance | Ergo Clips](https://www.youtube.com/watch?v=A5SJy7c3bfs&ab_channel=ErgoClips)

## Atomic Composability

Ergo's approach to scalability and atomic composability revolves around a combination of innovative and diverse solutions that address multiple layers of the protocol. By leveraging the Extended UTXO (eUTXO) model, advanced cryptography, and off-chain transactions, Ergo mitigates the scalability concerns that have plagued other blockchain platforms.

## Sharding

Sharding is a scaling technique in which the blockchain is divided into smaller, parallel chains, called shards, that can process transactions and smart contracts independently. This allows for increased throughput and parallelism while maintaining the security and decentralization properties of the main chain.

Ergo is designed to support sharding with its unique architecture. Ergo blocks have extension sections with mandatory and arbitrary key-value data. By placing certain anchors in these sections, it is possible to implement sharding solutions like Bitcoin-NG style micro blocks, Aspen-like service chains, or generic sidechains using velvet or soft forks. Sharding allows Ergo to process multiple transactions simultaneously across different shards, significantly improving the blockchain's overall transaction throughput.




## [EIPs](eip.md)

### What is Ergo's approach to Forking?

- **Velvet-Fork**: Only requires a minority of nodes to upgrade. Introduced by the NiPoPoW paper, the key idea is that you can use the scheme even if only some blocks in the chain include the interlink structure and allows for "gradual deployment" without harming the miners that haven't upgraded to the new rules. In this way, it acts similar to a soft fork in that clients that upgrade to new rules are still compatible with those that don't. 
- **Soft-fork**'s require some nodes to upgrade. Our recent re-emission Soft-Fork EIP37 was possible as it's enforced on miner nodes only via protocol rules. These can be approved with 90% support from miners. 
- **Hard-Fork** Requires all nodes to upgrade. 

Ergo follows a soft-forkability approach --- if a supermajority (90%+) of the network accepts a new feature, it is activated; however, old nodes that do not upgrade continue to operate normally and skip over this feature validation. Disruptive hard forks should be avoided in Ergo unless critical. 

### [EIP-0027](https://github.com/ergoplatform/eips/blob/master/eip-0027.md)

With the updated emission schedule described, re-emission (with 3 ERG re-emission rewards per block) would be enough for 4,566,336 blocks (~17.38 years).

### EIP-0037

The original Difficulty Adjustment Algorithm for Ergo worked well in most cases, including huge price drops, 100x initial difficulty misestimation during mainnet launch, and so on. However, the previous simplified and limitless version of the algorithm is bumpy. A big influx of mining hash rate over multiple epochs, especially with super-linear hash rate growth over time, may result in a huge difficulty spike. Similarly, a few slow epochs may cause a huge drop. Also, for dapps and other applications, it would be desirable to make difficulty readjustment more reactive (previously, readjustment takes place every 1024 blocks, and eight epochs, so about two weeks normally, are considered).

This was resolved with the [EIP-37](https://github.com/ergoplatform/eips/pull/79). 

EIP37 is a hard fork which makes the difficulty adjustment more reactive by shortening epoch length, amplifying the weight of the last epoch and some limits on difficulty changes. 
The 'epoch length' is to be set to 128 blocks. 
It calculates the difficulty in two ways according to the past eight epochs of 128 blocks each.
Then it takes an average from classic and predictive difficulties and limits the change so that the test can never be changed by more than 50% per epoch.


Broader conversations about [difficulty adjustments on ergoforum](https://www.ergoforum.org/t/diff-adjustment-potential-design-tradeoffs/3875)

## General FAQs

**Q: Are there plans to put together a Plutus Pioneer-style program for ErgoScript?**

A: The Ergo Foundation aims to sponsor educational programs, and fostering talent is one of its core goals. The Foundation actively supports the development of educational initiatives for ErgoScript.

**Q: How do you see the Ergo network funding development over time?**

A: In the longer term, the Ergo network envisions a community development DAO that operates in parallel with the Ergo Foundation. Funding for this DAO could come from projects that tokenize on the Ergo Blockchain. By donating a portion of their tokens to the Ergo Foundation or the community DAO, projects can contribute to the ongoing funding of the network.

**Q: To what extent can there be competition for dApps?**

A: Competition among dApps is actively encouraged within the Ergo ecosystem. Competition is essential for fostering a vibrant DEFI environment. It enables traders to arbitrage across dApps, increases network activity, and improves market efficiency. The Ergo network welcomes competition as it creates opportunities for innovation and market growth.

**Q: Free software tends to undercut incentives. How does Ergo address this?**

A: While free software is highly valued in the blockchain community, Ergo acknowledges the need to strike a balance between incentivizing development and providing open-source solutions. Ergo's unique contract model, built on the Extended UTXO framework, requires the creation of infrastructure from scratch. By developing innovative tools and infrastructure, Ergo aims to attract developers and promote the growth of the ecosystem.

**Q: Who is using Ergo? How does the user profile differ from other chains?**

A: Ergo is still a young network, with primary users currently consisting of miners, developers, and investors. However, as Ergo continues to build tooling and infrastructure, it aims to cater to a broader range of markets and user profiles. Ergo's focus is on developing specialized solutions to support different projects and their unique requirements.

**Q: Where does Ergo excel? What are its disadvantages compared to other chains?**

A: Ergo excels in several areas, leveraging the benefits of the Extended UTXO model, such as advanced privacy options with Sigma protocols, sidechain integration, and the potential to revolutionize SPV client implementation. However, Ergo recognizes that it lags behind in terms of mindshare compared to chains built on the Ethereum Virtual Machine (EVM). Ergo is actively working to overcome this challenge and believes that the market mindset will shift over time to embrace the resilience and privacy advantages offered by the network.

**Q: How does Ergo address environmental concerns related to Proof-of-Work (PoW)?**

A: Ergo acknowledges that PoW is energy-intensive compared to Proof-of-Stake (PoS). However, Ergo's design is conservative, focusing on well-known and tested Sigma protocols for privacy. The network is designed to be upgradeable, allowing for the adoption of newer, resilient cryptographic frameworks in the future. Ergo values research and employs methods and cryptography that have been rigorously tested to ensure security and store of value properties.

**Q: How is Ergo onboarding developers and cultivating its developer community?**

A: Ergo recognizes the importance of documentation, developer tools, and educational resources in onboarding developers. The network is actively working on creating these resources to streamline the process of converting non-web3 developers to Ergo. Ergo offers bounties, hackathons, and prizes to incentivize developers to learn, improve, and contribute to the Ergo ecosystem.

**Q: Is Ergo supporting peer knowledge sharing and respecting proprietary IP?**

A: Ergo promotes open-source development and transparency. While intellectual property (IP) exists

 in the blockchain industry, Ergo believes that open-source frameworks accelerate innovation, provide replicable metrics, and undergo community review, resulting in stronger and more secure projects. Ergo encourages developers to embrace open-source principles and the benefits it brings to the ecosystem.

**Q: Are there signs of rivalry and synergy within the Ergo ecosystem?**

A: Ergo's extended UTXO model and smart contract capabilities create opportunities for synergy within the ecosystem. Ergo is designed to support smart financial contracts and innovative frameworks. While competition naturally arises in the market, Ergo focuses on fostering collaboration and innovation through open-source code, allowing projects to leverage the network's tooling and infrastructure.

**Q: How does Ergo improve infrastructure and develop human capital?**

A: Ergo actively invests in improving infrastructure, offering incentives, expanding documentation, creating educational tools, and providing opportunities for developers to contribute to the core network. The network aims to attract and cultivate talent by offering resources and support for developers.

**Q: Does Ergo subsidize certain projects, potentially undermining long-term innovation and competition?**

A: Ergo aims to provide a level playing field for all projects and promotes decentralization. While it may appear that certain projects receive subsidies, Ergo strives to ensure fair competition and prevent insider advantages. The network believes that long-term competitiveness should be based on technological merit and benefits to users rather than preferential treatment from the start.

**Q: Does Ergo stimulate innovation and competition among its native projects?**

A: Ergo encourages innovation and competition through open-source code and the development of unique smart contract frameworks. The network continuously works towards improving tooling, documentation, and resources to support developers and stimulate innovation within the ecosystem.

**Q: How does the user profile of Ergo compare to other chains?**

A: As a young network, Ergo's user profile primarily consists of miners, developers, and investors. However, as the ecosystem grows and expands its tooling, Ergo aims to attract users from diverse backgrounds and cater to different markets and industries.

**Q: Which regions are adopting Ergo the most?**

A: Ergo's user base is globally distributed, with miners and investors coming from various regions. The network is still in its early stages, and as it develops further, adoption in different regions may vary based on market demands and specific use cases.

**Q: How does Ergo strike a balance between encouraging peer knowledge sharing and respecting proprietary IP?**

A: Ergo advocates for transparency and open-source development, considering the benefits it brings to the community. While proprietary IP exists, Ergo believes that open collaboration and community review lead to stronger projects and increased security. The network aims to provide replicable metrics and transparency, enabling developers to build on top of Ergo's open infrastructure.

**Q: Are there signs of collaboration and synergy within the Ergo ecosystem?**

A: Ergo was built to support smart financial contracts, and as the extended UTXO model and ErgoScript develop, new innovative frameworks are expected to emerge. The ecosystem benefits from the collaboration and specialization of developers and projects built on top of Ergo, fostering synergy within specific niches and industries.
