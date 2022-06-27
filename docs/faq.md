# FAQ


## Getting Started

- Ergo is currently available on the following [wallets](https://ergoplatform.org/en/wallets/) and [exchanges](https://ergoplatform.org/en/exchanges/). 
- The development roadmap can be seen [here](https://ergoplatform.org/en/ecosystem/#Roadmap).
- To see the applications currently running on Ergo, check out [sigmaverse.io](https://sigmaverse.io/).
- To read about Ergo from a less technical perspective, visit [ergonaut.space](https://ergonaut.space/en/home). 
- If you want to mine, see the [Miners Handbook](https://ergonaut.space/en/Guides/Mining).

## Why '*Ergo*'? 

Ergo means "therefore" in Latin but "work" in Greek. This is also a play on the fact that the cryptocurrency's design is ***ergo***nomical.

## Why Ergo?

Ergo is a next-generation smart contract platform that enables anyone to participate in the digital DeFi revolution now.

Ensuring economic freedom for ordinary people through decentralized, private and secure financial tools.

**🔑 Key Objectives**

- Research-led but real-world focused.
- Powerful & Safe
- Intelligent and Straightforward
- Secure and Accessible

**🔑 Key Features**

- **[Sigma Protocols](/dev/scs/sigma) (Σ)** - a type of non-interactive zero-knowledge proofs that are flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.
- **[Multi-stage Contracts](/dev/scs/multi)** - In addition to the regular protection offered by using a threshold `m‐of‐n` signature, Ergo also allows specifying the possible recipients of these coins, which may be another contract with similar complex conditions. This *"chaining"* approach allows the implementation of **secure and efficient smart contracts of arbitrary complexity**. 
- **[Non-Interactive Proofs of Proof of Work (NIPoPoWs)](/dev/protocol/nipopow/)**  are essential for two reasons: Light Clients and Side Chains. 
- **[Storage Rent](/dev/protocol/rent/)** acts as *on-chain garbage collection*


Keeping all this in mind, we expect Ergo's design to be uniquely useful as Contractual Money.




## What is the [Emission Schedule](https://ergoplatform.org/en/blog/2019_05_20-curve/)?

Ergo has a maximum supply of **97,739,925** Ergs, to be completed in **8 years** after launch. However, there is currently voting underway to extend this to 2045. 

## When was Ergo launched?

Mainnet July 2019. Before this, there was *Ergo-First-Year-Token*

**What is EFYT?**

Ergo-First-Year-Token was airdropped and distributed on Waves DEX starting with a 100,000 EFYT airdrop in May 2017. EFYT served the dual purposes of helping to build an early community of stakeholders and enthusiasts for Ergo and of raising a small number of funds for the platform before launch to fund development, promotion etc. EFYT is strictly a Waves token and is not the same as an Erg, which is the Ergo mainnet native token mined after Ergo's mainnet launch.

It should be noted that the max supply of EFYT is 1,970,945.0. This is 10% of the first year of Ergo token emission and the same number of Ergs that the Treasury will receive, meaning that the Treasury will have received 1,970,945.0 Ergs during year 1, sufficient to swap the max supply of EFYT for Erg.

**Why 97,739,924?**

> Emission in Ergo is controlled by pre-agreed smart contract, so we tried to have simple enough emission curve with total limited supply being close to 100M (and emission to be done in 8-10 years).

The max supply is simply the amount needed to create the initial genesis state: 
- A box with proof-of-no-premine (1 ERG)
- Foundation treasury (4,330,791.5 ERG)
- [Miner Reward Box](https://explorer.ergoplatform.com/en/addresses/2Z4YBkDsDvQj8BX7xiySFewjitqp2ge9c99jfes2whbtKitZTxdBYqbrVZUvZvKv6aqn9by4kp3LE1c26LCyosFnVnm6b6U1JYvWpYmL2ZnixJbXLjWAWuBThV1D6dLpqZJYQHYDznJCk49g5TUiS4q8khpag2aNmHwREV7JSsypHdHLgJT7MGaw51aJfNubyzSKxZ4AJXFS27EfXwyCLzW1K6GVqwkJtCoPvrcLqmqwacAWJPkmh78nke9H4oT88XmSbRt2n9aWZjosiZCafZ4osUDxmZcc5QVEeTWn8drSraY3eFKe8Mu9MSCcVU) with the required ERG for 2,080,800 Blocks according to the emission schedule until rewards equal 0 and storage rent and EIP-27-reemission-box takes over (93,409,132 ERG). 

The treasury box is protected by a vesting smart contract that ensures an initial unlocked amount and then only releases an amount of ERG that provides funds for 2.5 years (never exceeding 10% of the circulating supply). All of this results in these specific amounts.

In total, this happens to be 97,739,924.5 ERG.

For proof-of-no-premine, pre-genesis state in Ergo contains block hashes from Bitcoin and eth and also headlines from the Guardian, Vedomosti and Xinhua around moment of launch which can be seen in [mainnet.conf](https://github.com/ergoplatform/ergo/blob/1935c95560a30b19cdb52c1a291e8a389ba63c97/src/main/resources/mainnet.conf#L11)

```scala
  /**
    * Genesis box that contains proofs of no premine.
    * It is a long-living box with special bytes in registers
    */
  private def noPremineBox(chainSettings: ChainSettings): ErgoBox = {
    val proofsBytes = chainSettings.noPremineProof.map(b => ByteArrayConstant(b.getBytes("UTF-8")))
    val proofs = ErgoBox.nonMandatoryRegisters.zip(proofsBytes).toMap
    createGenesisBox(EmissionRules.CoinsInOneErgo, Constants.FalseLeaf, Seq.empty, proofs)
  }
```

```json
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



## Ergo Foundation


The [Ergo Foundation](https://ergoplatform.org/en/foundation/) is a community-driven entity focused on:

  - Promoting non-breaking development of Ergo Platform protocol;
  - Promoting the widespread adoption and use of Ergo Platform and its native token (ERG);
  - Developing the ecosystem around the Ergo Platform;
  - Promoting the use of Ergo Platform and blockchain technology for social good;
  - Supporting truly decentralised infrastructure, and;
  - Supporting privacy as a basic human right.

### Funding

To fund development, promotion, events, and any other activities which may advance the platform, Ergo has in place a Treasury, which will receive **4.43%** of the Ergs released during emission. During the first two years post‐mainnet launch, the Treasury received 7.5 Ergs per block. 

Readers familiar with some other PoW protocols with a Treasury, such as ZCash, may find this to be similar; however, it should be noted that the number of Ergs going to the Treasury comprise a total of only **4,330,791.5**, or 4.43% of the total monetary base, and is completed in just 2.5 years. This compares with ZCash's Treasury, which was 10% of the ZCash total monetary base and 20% of all issued ZCash coins during the first four years. 


## What is the teams' background?

Ergo is designed and implemented by experienced developers and researchers who hold publications and PhDs in cryptography, compiler theory, blockchain technology, and cryptographic e-cash. The team has a solid background in core development with cryptocurrencies and blockchain frameworks such as Nxt, Scorex and Waves. Alexander' kushti' Chepurnoy was a co-founder of smartcontract.com (now Chainlink), a core developer at NXT (The first full PoS), and one of the first employees at IOHK; he was a Research Fellow and Team Scorex Manager. 

The full team can be seen on Ergo's [Hall of Fame](https://ergoplatform.org/en/hall_of_fame/).

## Interview

### Extended UTXO is a new contract framework, are their plants to put together a Plutus Pioneer-style program for ErgoScript? 
 
The Ergo Foundation can sponsor the money for educational programs, and this is of the core goals of the Ergo Foundation as an organization. 

### How do you see the Ergo network funding development over time?  

Longer-term, we propose a community development DAO that operates in parallel to the Ergo Foundation. One potential mechanism to fund this would be through projects that tokenize on the Ergo Blockchain. Open source development often comes with a variety of assistance from the community. 

If new projects are willing to donate a small allocation of their tokens to either the Ergo Foundation or a community DAO, it opens a long-term funding path.  

We have already started discussions with projects. 
 
### To what extent can there be competing for dApps? For example, it is hard to imagine more than one Dex on Ergo, but maybe? What potential synergies are there?

We actively encourage competing dapps. Competition is a critical part of creating a DEFI environment. It opens the ability for traders to arbitrage across dapps and creates increased activity on the network. Competing marketplaces also increases market efficiency. We encourage competition. It creates market opportunities and incentives to innovate. 
 
### Free software is great, but it does tend to undercut incentives. But, I also notice that Ergo isn't super fast about posting new code. Is that what is going on with that, preserving incentives?
 
Free software is amazing. Bitcoin would not exist without free software. Much of the internet would not exist without Linux. Ergo is a new contract model. Most projects are based on EVM or previous forks.

Much of the infrastructure has to be created from scratch to match Ergo’s model. Is that a negative? No, it is a bi-product of leading the Extended UTXO model to market.  

So far we have produced the first extended UTXO dapp, stablecoin, oracle framework, NFT, and dex. Currently, there is ongoing R&D into multiple L2 solutions. Ergo will most likely start with plasma channels first, and expand to models with more complexity. We are also in the development process of bridging to other ecosystems. Additionally, a framework for sidechains has come out of our R&D group and will be implemented in 2022. 
 
### Who is using Ergo? What are the top countries using the chain? How does the user profile differ from other chains?
 
Ergo is still a very young network. At this point, the primary users are either investors or miners. However, as we build tooling, we have a path to capture multiple markets. Ergo is not a native token. It is a base layer blockchain; the focus is to create the basic tooling to support demand on top of the base layer. 

Unique needs arise when analyzing different projects. We are already putting together multiple Ergo Improvement Protocols to support development. 

Market specialization is the focus of developers and projects on top of Ergo. Our goal is to build a variety of tooling and infrastructure to support this growth. 
 
### Where does Ergo excel? What disadvantages relative to other chains? 
 
Ergo’s advantages beyond the benefits of Extended UTXO, we have a lot of interesting privacy options with Sigma protocols, Ergo also has a simple path to sidechains and a way to revolutionize SPV client implementation. Ultralite SPV clients via Nipopows with full node security have never been implemented. 

Ergo is pushing the boundaries of Proof of Work and Extended UTXO simultaneously. We plan to continue the research first approach and push the boundaries of what POW is capable of. 

I would say there are two disadvantages. The first is time. There is considerable mindshare developed around EVM, and the account model in this comparison, Extended UTXO, is behind. 

The second is the current market mindset does care about first principles or crypto or the actual resilience of distributed systems. However, we do believe that both of these will change in time. 

Real decentralization, privacy, and resilience are not attractive when you don’t need them. 

This type of network does come with a tradeoff vs systems designed to be more centralized, permissioned, and optimized. The value of resilience only matters in difficult environments.  
 
### I would be interested in some real critique rather than nonsense FUD about PoW not being environmentally friendly.
 
POW is energy-intensive relative to POS. However, the security model is known. The design of Ergo is pretty conservative. We chose Sigma protocols because they are well known. They have been studied and tested in depth for a long time. 

There are newer fancier cryptographic frameworks. However they have not been rigorously tested to the point where the assumptions can be considered truly sound. If the assumptions breaks, the cryptography breaks as well. Ergo is also designed to be amendable, meaning it can be upgraded in time. If newer cryptography demonstrates resilience we can always add it in the future. 

PoW is seen as a store of value based on the energy used to back the production of the digital asset. The best way to encourage ERG as a store of value is to use well researched methods and cryptography. 

Proof of Stake is not a bad, we are happy to work with Proof of Stake chains. 

One of the largest short term liabilities in POS tokens is that they resemble a security much more than a fair launched POW token.  

There are areas in POS where the security models are not known as they have not been fully implemented.

The reality with POS is each particular network has to create security assumptions based on various factors unique to each project. 
 
In terms of usability, consensus, etc. there are a lot of unique challenges in Proof of Stake.  

If POS projects support stake migration, how will that alter network congestion, TLV in DEFI, and rates of return in DEFI? 

There are a lot of factors that are hard to predict. Ergo is not anti-proof of stake. However, there are many unknowns and complexities project to project. 

### Sufficient provision of production inputs -Human capital How much effort is the chain making to onboard talents & produce its future army of developers?

Onboarding developers is first a matter of documentation and developer tools. This is in motion and we will continue to increase resources towards this end. We also offer bounties that give developers a pathway to learn, improve and familiarize themselves with the inner workings of Ergo. We also have hosted hackathons that have brought about projects converting into dapps. Moving forward, I would like to increase the frequency of hackathons and increase the offered prizes. Hackathon Ideas Privacy Tokenizing on Top of Ergo Documentation and Developer Tools.

### How easy is it for non-web3 developers to convert? (e.g. C++ & Java peeps can learn Rust, used by Solana, in a month. For Avalanche you can code in multiple languages. Few likes Solidity.) 

This honestly depends on the talent of the actual developers to start with. Not all developers start with an equal skillset. As we create additional resources, documentation, and educational tools, this process will be more streamlined. You can build on top of Ergo in a variety of languages.

### Financial capital How much financial ammunition does the chain have in the pipeline?

The Ergo Foundation has a small allocation of block rewards. We are in the process of designing frameworks for additional funding and community DAO’s. Financial ammunition sounds like a really sexy way to say how large of a position is not public. This did not happen with Ergo. Why? To promote decentralization.
Personally I think that partnering with larger firms or investors makes sense after a significant period of being on the market (as with bitcoin) rather than an insider advantage from launch.

### Infrastructure: How much infrastructure does the chain have or is planned at least? Peer competition within industries?

Ergo has a pretty broad technical base. Native tokens, smart contracts, Bridges, L2 solutions, Oracles, Privacy tools, Sidechains, SPV clients. All of these are iterative and will evolve as the network develops. These are built on top of the extended UTXO model, which bring native advantages (security, parallelism, and predictable costing)

### Are there signs of strong rivalry in the same niches emerging within the L1?

Most L1s (IMO) are built for throughput at the cost of resiliency.
Throughput is attractive, but the most efficient model for throughput will always be centralized.
The benefit/tradeoff of a decentralized network is resilience. Ergo has the capacity to increase throughput with L2 solutions, and sidechains. But it will never be as fast as a centralized system.
The closer a system gets to centralization or as the user requirements increase, the faster it gets.

### Does the dev culture of the chain strike the right balance btw encouraging peer knowledge sharing & respecting proprietary IP?

IP requires trust in the “proprietary technology.” Closed projects require a leap of faith. The point of bitcoin was to remove faith and replace it with auditable certainty.
How many times in crypto have we heard…
My new system has 104859234 TPS! but sorry it is proprietary…
The test environment cannot be disclosed. But trust us…
You can’t replicate it locally but trust us…
Ergo is trustless and open. I cannot police projects in an open network, but I can encourage developers to recognize the benefits. It is better to provide metrics that can be replicated. It is better to provide transparency. I could use the example here of Uniswap V3.
Had they open-sourced this framework, it would have evolved. Open source accelerates frameworks becoming more efficient for users, most likely more profitable.

https://cointelegraph.com/news/half-of-uniswap-v3-liquidity-providers-are-losing-money-new-research
There are also serious security concerns from closed projects as the community review process does not occur. A lack of community review could potentially lead to catastrophic hacks.
https://ambcrypto.com/now-fixed-solana-protocol-library-bug-had-potential-to-expose-2-6-billion-to-risk-of-theft/
The goal of the Ergo network is the benefit the users. I believe that IP protects profit, often at the user’s expense.
Projects with a strong attachment to IP can build on other networks and always bridge into Ergo to access the network liquidity and tooling.

### Clusters of supporting sectors Are there signs of synergetic niches / industries emerging within the L1 ecosystem?

Ergo was built for financial smart contracts before DEFI was even a term. Given the strengths of the extended UTXO model, this is a significant growth sector for ERG. As Ergoscript and the Extended UTXO model develop I believe new innovative frameworks will be discovered.

### Quality of domestic demand How does the user profile of this L1 compare to other chains?

At this point, the primary users are miners, developers, and investors, aside from the telegram trading chat, which is the traditional degenerate dumpster fire crypto chat. I am honestly quite impressed with the overall mindset, contributions, skills, and principles of the active community.

### Where in the world is the chain getting the most adoption?

Currently, the most extensive set of users are miners and investors. These are relatively globally distributed. I believe this is a product of the Extended UTXO model being young. We have a large number of community developers and the work/advancements being made can be tracked weekly.

### Role of the blockchain itself? What’s the chain doing to promote rivalry among its native projects & stimulate innovation?

Innovation and competition are stimulated through open-source code. Ergo brought a new smart contract model to market and has led the way in building on this model. As we move forward we need to bootstrap tooling and documentation for new developers.

### What’s the chain doing to improve infrastructure & human capital supply?

We actively offer incentives, put together documentation educational tools, and expand open development positions for the core network.

### Is the chain “subsidizing” certain projects to help them gain ST advantage, which may inadvertently undermine innovation & competition in LT?

It may appear that way to some.
We are a young network (being we have a new smart contract model) We are very competitive long-term with the tech we bring to the table. The network is still in its infancy. Price does lead to developer adoption. However, it is hard to claim or disavow strategic advantages when you lack competition. That is due to bringing a new type of network to crypto.
Extended UTXO has a bright future but is still very young. The advantages are obvious, but it is relatively new.
