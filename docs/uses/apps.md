
## Applications

Check out [sigmaverse.io](https://sigmaverse.io/) - *your portal to the Ergo Universe* 

## Live dApps

### ErgoDex
> Beta live on [Ergo](https://ergodex.io)

- [ErgoLabs](https://github.com/ergolabs) 
- [EIP-0014: Decentalized Exchange Contracts](https://github.com/ergoplatform/eips/pull/27)
- [Single-Chain Swap Contracts (DEX basis) by Alex Chepurnoy](https://www.youtube.com/watch)

### SigmaUSD
> [sigmausd.io](https://sigmausd.io), The first UTxO-based stable coin - an instantiation of the [AgeUSD protocol](https://github.com/Emurgo/age-usd). Its economic model designed in partnership between IOHK, Ergo, and Emurgo maintains the conservative settings for collateral reserves and avoids the need for liquidations. Along with that, it supports a fully decentralised stablecoin emission setup.

- The UI for the front-end is available at [anon-real/sigma-usd](https://github.com/anon-real/sigma-usd) 
- [Ergo Summit 2021 - The IOHK Perspective - Designing the AgeUSD StableCoin](https://youtu.be/zG-rxMCDIa0?t=9247)
- [Overview Video (with diagrams)](https://www.youtube.com/watch?v=O3hPEp3tzoU)
- [Building Ergo: How the AgeUSD stablecoin works](https://ergoplatform.org/en/blog/2021-02-05-building-ergo-how-the-ageusd-stablecoin-works/)

**Dexy**

- [Dexy: USD Simplest Stablecoin](https://www.ergoforum.org/t/dexy-usd-simplest-stablecoin-design/1430)
- [A Simplest Stablecoin?](https://www.ergoforum.org/t/a-simplest-stablecoin/413)


### ErgoMixer
> Due to secret generation under the hood, it must be run as a local application. 

[ErgoMixer](https://github.com/ergoMixer/ergoMixBack) is the first working non-custodial, programmable, non-interactive mixer in the cryptocurrency space. 

- Technical Slides: [ZeroJoin: Combining Zerocoin and Coinjoin](https://ergoplatform.org/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf)
- [Video tutorial](https://www.youtube.com/watch?v=03_2HH82Plw)

### ErgoAuctions

- [Ergo Auction House](http://ergoauctions.org/#/auction/active) lets you buy and sell collectible tokens, art, and much more.
  - [Source code](https://github.com/anon-real/ErgoAuctionHouse)
  - [v2 contracts](https://github.com/ergoplatform/eips/pull/39/files)
- [Profit-Sharing for Ergo Auctions House](https://www.ergoforum.org/t/profit-sharing-for-ergo-auctions-house/708)


### Raffle
- [ErgoRaffle GitHub](https://github.com/ErgoRaffle/raffle-documentation)

## In Development

### ErgoFund

> In development


- [Ergo Crowdfunding CLI](https://github.com/robkorn/ergo-crowdfunding-cli) | Command-line tool which enables participating and interacting with crowdfunding campaigns on Ergo
- [Scanner](https://github.com/ergoplatform/scanner) 
- ZK Treasury |  a tool for joint spendings with on-chain privacy 
  - [Server](https://github.com/anon-real/DistributedSigsServer) 
  - [Client](https://github.com/anon-real/DistributedSigsClient)
- ['A Collective Spending Appproach'](https://www.reddit.com/r/ergonauts/comments/ohftim/ergoteam_a_simpler_collective_spending_approach/)

### ErgoProfitSharingDapp

This service will provide a way for dapps to distribute gains among dapps' token holders.

The first user of this service will be the ErgoMixer. 

Ergomixer's income (in ERG and other tokens) is currently received by its creator, aka 'anon2020s', since it has only one stakeholder at the moment. He has announced that he is willing to create and sell some tokens shortly to obtain more stakeholders; let's call this token MIX. Later, anyone with the MIX tokens can stake them in the Profit Sharing contract and obtain the mixer's incomes proportional to their staked tokens.

So, it is NOT a way to stake ERG at first. But, it CAN BE USED in the future in some creative services to provide ERG-staking.

- [Ergo Profit Sharing dApp](https://github.com/mhssamadani/ErgoProfitSharingDapp)

**Use-cases**
- [A solution for staking](https://www.ergoforum.org/t/a-solution-for-staking/1057)
- [Paying fee in ErgoMix in primary tokens](https://www.ergoforum.org/t/paying-fee-in-ergomix-in-primary-tokens/73)
- [Profit-Sharing for Ergo Auctions House](https://www.ergoforum.org/t/profit-sharing-for-ergo-auctions-house/708)



### LETS

> Development starting soon.


## Tooling

### Zero-Knowledge

> In development
>
### Oracles
> v2 contracts in review.

When external oracle data is posted on-chain, it needs to be encoded exactly within a transaction. Furthermore, oracle pools have many different moving parts that require transactions to be issued to move between the different stages of the pool protocol. [Oracle Core](https://github.com/ergoplatform/oracle-core) creates all of the complex transactions which post the data on-chain & run the oracle pool protocol on-chain (such as averaging data points). This comes bundled with [Oracle Pool Bootstrap](https://github.com/ergoplatform/oracle-core/tree/master/oracle-pool-bootstrap) and a [Connector Library](https://github.com/ergoplatform/oracle-core/tree/master/connectors/connector-lib). The [ada-usd-oracle](https://github.com/ergoplatform/oracle-core/blob/master/scripts/ada-usd-oracle/oracle-config.yaml) source can be seen here. Currently, only the erg-USD-oracle is live as seen in the [Oracle Pool List](https://explorer.ergoplatform.com/en/oracle-pools-list)

See this [overview](https://github.com/Emurgo/Emurgo-Research/blob/master/oracles/Oracle-Pools.md) by Robert Kornacki.

**Resources**

- [eth/usd connector](https://github.com/Luivatra/oracle-core/tree/eth-connector)
- [Ergo oracles](https://github.com/sininen-taivas/ergo-oracle) | simple command-line tool to launch oracles. Inbuilt implementations for USD/ERG, EUR/ERG, BTC/ERG, AUG/ERG (gold) prices delivery. 
- [Learn about data inputs and the truly novel innovations they bring to UTXO-based Blockchains](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/Unlocking%20The%20Potential%20Of%20The%20UTXO%20Model.md)
 - [Ergo oracles](https://github.com/sininen-taivas/ergo-oracle) | simple command-line tool to launch oracles. Inbuilt implementations for USD/ERG, EUR/ERG, BTC/ERG, AUG/ERG (gold) prices delivery. See also a [forum topic with example](https://www.ergoforum.org/t/erg-usd-oracle-on-top-of-ergo/119)
  

**v2**

- [Oracle pool 2.0 contracts finalized (for initial draft).](https://github.com/ergoplatform/eips/blob/eip23/eip-0023.md)
- [Tests for oracle pool 2.0](https://github.com/scalahub/OraclePool/tree/v2/src/test/scala/oraclepool/v2)


**Articles**

- [Chainlink Oracles vs. Ergo Oracle Pools](https://ergoplatform.org/en/blog/2021-04-27-chainlink-oracles-vs-ergo-oracle-pools/)
- [Oracle Pools - A New Oracle Model](https://www.ergoforum.org/t/oracle-pools-a-new-oracle-model/263)
- [First steps towards interoperability with Cardano oracles](https://ergoplatform.org/en/blog/2020-11-09-first-steps-towards-interoperability-with-cardano-oracles/)
- [Ergo Blockchain: Oracle Pool Governance Update](https://curiaregiscrypto.medium.com/ergo-blockchain-oracle-pool-governance-update-d078d58571b0)
- [The role of Ergo Oracles](https://veriumfellow.medium.com/oracle-special-4e36cfa6a852)

### Misc

- [ErgoFaucet.org](https://github.com/zargarzadehm/ergo-faucet)
- Various utilities are listed on [ergosites.github.io](https://ergosites.github.io/#ex2-tabs-3)
- [ergo.watch](https://ergo.watch) | [Git](https://github.com/abchrisxyz/ergowatch)


## ERGOHACK

**ERGOHACK I**

- [ErgoRaffle](https://github.com/ErgoRaffle)
- Ergo Index Fund
- [Smart Pools](https://github.com/WilfordGrimley/ErgoSmartPools)
- [Sigma Stamp](https://www.sigmastamp.ml/)
- Ergo Charts
- [Simpler Joint Spending Tool](https://www.ergoforum.org/t/a-simpler-collective-spending-approach-for-everyone/476%20)

**ERGOHACK II**

- [ErgoLend](https://github.com/Ergo-Lend/)
- [Minotaur Wallet](https://github.com/minotaur-ergo/minotaur-wallet)
- [Ergopad](https://github.com/Ergohack-Dashboard-Project)
- [Ergo Subpooling](https://github.com/K-Singh/ergo-subpooling)
- [HYPO10USE: QUIDGAMES](https://github.com/hypo10use/quid-games)
- Ergo Audio

**Many more possible!**

- [Bonds based on Ergo (or the “Yield protocol”)](https://www.ergoforum.org/t/bonds-based-on-ergo-or-the-yield-protocol/128)
- [An ICO Example On Top Of Ergo](https://github.com/ergoplatform/ergo/wiki/An-ICO-Example-On-Top-Of-Ergo)
- [A Local Exchange Trading System On Top Of Ergo](https://github.com/ergoplatform/ergo/wiki/A-Local-Exchange-Trading-System-On-Top-Of-Ergo)
- [A Trustless Local Exchange Trading System](https://github.com/ergoplatform/ergo/wiki/A-Trustless-Local-Exchange-Trading-System)
- [(E)mail Client for Limited or Blocked Internet](https://www.ergoforum.org/t/e-mail-client-for-limited-or-blocked-internet/134)
- [LETS start the discussion](https://ergoplatform.org/en/blog/2021-07-01-lets-start-the-discussion/)
- [Self-Soverign Defi](https://ergoforum.org/t/self-sovereign-defi/260)
- [Payment channels without multisignatures](https://www.ergoforum.org/t/payment-channels-without-multisignatures/2219)
- ErgoFans | Decentralised content producer platform | Patreon/Onlyfans
- ErgoGigs | Decentralised gigs! (Fiverr)
- ErgoEarn | earn for learning (Coinbase Earn)
- ErgoStats | on-chain analysis (glassnode)
- [Shrimpcoin - The first shrimp-pinned stablecoin on Ergo](https://www.ergoforum.org/t/shrimpcoin-the-first-shrimp-pinned-stablecoin-on-ergo/1381)




* Crowdfunding: the basic contract is described in the ErgoScipt whitepaper: https://ergoplatform.org/docs/ErgoScript.pdf , we made testing crowdfunding campaign using just the node: https://www.ergoforum.org/t/simple-crowdfunding/70 and then CLI tool was developed. No UI was done though, and CLI tool now needs to be updated for post-3.3.0 node API. 

* Loans: we have interest-free loan contract example: https://www.ergoforum.org/t/interest-free-loan-contract/67 . With SigmaUSD loans can be attractive to miners and not only. Please also check targeted microloan contract from "Smart Contracts for the People" article: http://chepurnoy.org/blog/2018/10/smart-contracts-for-the-people/

*  Mining power derivatives: https://www.ergoforum.org/t/mining-power-derivatives-two-tokens-approach/277

* Lotteries: https://www.ergoforum.org/t/a-lottery-on-top-of-ergo/137 as a starting point.

* Profit-sharing schemes: https://www.ergoforum.org/t/running-a-business-on-top-of-ergo/423

* Email and paper clients for limited or blocked Internet: https://www.ergoforum.org/t/e-mail-client-for-limited-or-blocked-internet/134 

* Local exchange trading systems and other community currencies: https://ergoplatform.org/en/blog/2019_04_22-lets/ and https://ergoplatform.org/en/blog/2019_05_29-exchange/ 

* Decentralized exchanges: we already have some team working on both orderbook-based DEX and AMM-based DEXes, but more contributors always welcome! (especially with UI dev).



There are many tools for developers now, such as Headless DApp Framework (by Emurgo) https://github.com/Emurgo/ergo-headless-dapp-framework , ErgoAppKit (by @morphic ): https://github.com/ergoplatform/ergo-appkit , Ergo Playground for play with contracts (check ready examples  at ErgoScript By Example repo: https://github.com/ergoplatform/ergoscript-by-example ), Ergo JS Template to make UI easily https://github.com/anon-real/ergo-js-template etc  

Making applications on top of Ergo is not about fun and following proper first principles, but also can be profitable these days! So come and build on top of Ergo!

## Powerful But Safe Contracts

Ethereum is an exceptional platform, but there are things it does not do well. Its Turing-complete smart contracts are powerful, but dangerous – as incidents from The DAO to the Parity wallet exploits have proven, with tens of millions of dollars in collateral damage. With complexity comes uncertainty, and potentially catastrophic vulnerabilities. Contracts can be expensive to run, and depending on network conditions may execute unpredictably – or not at all. 

Ergo takes a fundamentally different approach to smart contract development. The team, which has extensive experience with blockchain platforms, frameworks and organisations from Nxt and Waves to Scorex and IOHK, has adopted a declarative model for programming whereby it’s always known in advance how much code will cost to run – and, indeed, whether it will run precisely as intended. While that might on the surface limit code complexity, it’s nevertheless possible to create Turing-complete scripts by iterating processes across multiple blocks. That means Ergo can support versatile dApps that run predictably, with known costs, and don’t have any of the dangers of unrestricted functionality.

## Sigma protocols

The platform is unashamedly conservative, basing as many features as possible on Bitcoin – after all, Bitcoin is the most battle-tested crypto network in existence. Ergo’s UTXO model, PoW mining and finite supply draw on Bitcoin’s approaches to consensus and economic incentives.

But Ergo also incorporates cutting-edge research into new cryptographic processes, using Sigma protocols to enable DeFi applications that would be either complex and messy or simply impossible on other platforms. Sigma protocols are a well-known class of zero-knowledge proofs that allow developers to implement very powerful processes very elegantly. For example, what if you want to build a privacy service that allows any one of a dozen different accounts to spend funds from an address – but no one can tell who has made each transfer? Such a ‘ring contract’ is possible with Ethereum, but it would require a clunky and expensive workaround. With Ergo’s Sigma protocols, it’s possible to implement this kind of use case and many others quickly, efficiently and – above all – securely. Sigma protocols have not been deployed in such generic form within crypto before. Yet this kind of out-of-the-box functionality is hugely valuable, especially when no other DeFi platform offers it.

_Ergo enables new models of financial interaction, underpinned by smart contracts built on flexible and powerful Sigma protocols but easily accessible to developers._

One of the most exciting things about blockchain is the possibility of making digital agreements without any trusted intermediaries. In the simplest use case, pioneered by Bitcoin, Alice can send a payment directly to Bob, wherever the two of them are located around the world, with no bank or any trusted third party needed. However, with the functionality of a modern blockchain like Ergo, it is possible to make far more complex and sophisticated financial agreements than simple payments. Take the following example.

## Gold-backed tokens

Alice uses ERGs to purchase gold-backed tokens from Bob. Bob stores the gold in a secure vault, and uses the blockchain to issue one token for every Troy ounce of gold he has. Alice can then use these tokens freely in different contracts, transferring and trading them under whatever conditions she specifies in the smart contract code. When Alice wants to sell the tokens for physical gold, she can conduct another transaction with Bob, receiving ERG in return, at market price.

The point of blockchain contracts is to eliminate the need for trust. While the purchase transaction is now trustless, in this instance Alice still needs to trust Bob about two things. Firstly, Bob may refuse to swap the gold tokens back to ERG at the correct price when Alice wants to sell. Secondly, Bob may default on his obligations – running away with the gold, or misusing the funds he receives and running a fractional reserve.

## Extending the contracts

To address these issues, we can create an Oracle, or decentralised price feed. This uses multiple sources of external data to record the price of gold to the blockchain at regular intervals. This price feed will be the reference point for the redemption contract that manages the sale of Alice’s gold with Bob (or any other participant). Thus the system automatically enforces the right price when a swap takes place.

The second situation requires a third-party insurer, Charlie, whose service is also hosted on the blockchain with a smart contract. When Alice purchases gold from Bob, she additionally buys an insurance contract from Charlie. The payment can be dependent on factors including the amount of insurance required, and Bob’s reputation – again, managed by a decentralized feedback mechanism. Now, if Bob defaults, Alice will automatically receive the value of her gold tokens, with Charlie effectively acting as a buyer of last resort.

## Programmable contracts

There are, of course, many other example use cases like this one. We can also extend this use case, adding further economic actors. For example, Charlie may sell shares in his insurance business to Dave and other participants, providing them with a proportion of revenues in return for ensuring he has the capital he needs to cover any liabilities from the outset.

However, even the most complex use case is simpler than general-purpose software that can be used to program any contract. After all, generalised logic must be both far-reaching and secure. Moreover, even a specialised contract is made up of many steps, each of which is fairly simple. Thus another requirement for a general-purpose platform is that it should simplify the process of writing contracts, making them as accessible (and safe) as possible. This can be achieved with the use of template agreements, with customisable parameters. The insurance contract above could be based on a module with flexible parameters, for example. This could be used and reused in many different circumstances.

## Ergo’s approach

This is essentially the approach that Ergo takes, providing superior support for real-world financial agreements. It does this through:

1. Support for multi-stage contracts ([watch details for developers](https://www.youtube.com/watch?v=g3FlM_WOwBU))
2. A simple high-level language, ErgoScript, enabling clear descriptions of contractual logic
3. Support for formal verification of contracts for improved security guarantees (Ergo Platform deployed its [first formally verified p2p crowdfunding contract](https://twitter.com/chepurnoy/status/1239936086106935296) just three months after the network launched)
4. Easy Oracle creation
5. Native support for complex signature schemes

In short, creating financial contracts on the blockchain isn’t just about the functionality you provide. It’s about making that functionality safe and accessible, as well as powerful. Ergo achieves this and more.

DeFi dApps have overloaded the Ethereum blockchain, causing long delays and soaring fees for transactions. Ethereum and many other platforms besides have researched and implemented fixes to address the lack of capacity. However, all of the solutions are imperfect in one way or another. Larger blocks are the obvious but clumsy fix, resulting in centralisation as fewer miners can afford the bandwidth, storage and CPU cycles to participate. Reducing the number of block validators – another approach taken to increase throughput – also necessarily centralises the blockchain. Sharding, while potentially very promising, has yet to be implemented successfully, and in some proposed implementations, breaks atomic composability because shards cannot communicate seamlessly.

Thus many of the ways projects seek to ensure their blockchains are fit for purpose result in greater centralisation or loss of critical functionality. 

**Marginal gains**

Ergo’s developers are watching developments in the DeFi space closely, especially some of the proposals that aim to scale blockchains while maintaining security, decentralisation and atomic composability. In the meantime, there is much that can be done to improve blockchain capacity. The concept of ‘marginal gains’, often applied in sports, is useful: a number of small, incremental gains in different areas all add up to a substantial compound effect.

For Ergo, there are several design principles and choices that have been taken to realise efficiencies in different areas.

* [Storage rent](https://ergoplatform.org/en/blog/2020_04_21_ergo_positioning/) is akin to ‘on-chain garbage collection’, reducing blockchain bloat and lowering the long-term costs of mining, improving economic sustainability.
* NiPoPoWs (non-interactive proof-of-proof-of-works) enable [mobile SPV clients](https://ergoplatform.org/en/blog/2020_05_1_spv_security/) and [even lite full nodes](https://ergoplatform.org/en/blog/2020_05_08_lite_full_nodes/), again reducing the barriers to maintaining the network and improving decentralisation.
* A [smart contract language](https://ergoplatform.org/docs/ErgoScript.pdf) that is finite and clear, without the messiness and possible chain bloat of Turing-complete languages and their unintended consequences.
* [Sigma Protocols](https://ergoplatform.org/en/blog/2020_03_16_ergo_sigma/), which allow for powerful cryptographic use cases, implemented elegantly and efficiently.

As DeFi emerges as a major use case for blockchain, the stakes could not be higher. Blockchains that are fit for purpose will thrive; those that do not allow the functionality to sustain the required transaction load simply cannot establish a foothold. At the same time moving too fast and implementing untested technology is equally dangerous. 

There are efficiencies to be gained in first-generation blockchains. Ergo continues to prioritise this approach while researching future upgrades.


<!--StartFragment-->

#### Ergo Blockchain is Layer 1 Protocol for powerful Decentralized Finance Contracts that builds advanced cryptographic features and radically new DeFi functionality on the rock-solid foundations laid by a decade of blockchain theory and development. The Proof of Work consensus algorithm and underlying UTxO model enable robust scalability and security. Ergo is also partnered with [EMURGO](https://emurgo.io/) , the commercial arm of Cardano, to improve research on blockchain and zero-knowledge ecosystems. To check out some smart contract deployments, see our GitHub repositories [here](https://github.com/ergoplatform) and [here](https://github.com/Emurgo).

## Stablecoin

Blockchain assets can be extremely volatile. That’s why investors often seek digital assets which are pegged to national currencies. A Stablecoin is the most primitive integration of cryptocurrencies with the off-chain world. Until DAI, fiat custody services were provided by centralized services. The first example of a stable coin, USDT, is backed by [actual dollars](https://cryptobriefing.com/external-auditor-first-confirm-tethers-usdt-backing/) held in banks. However, for a decentralized financial system, we need other means of fiat-pegged currencies. 

Launched in February, Ergo’s native stablecoin SigUSD is based on AgeUSD protocol to provide a robust Reserve/Mint contract. Providing a truly decentralized finance experience. It’s collateralized with its own native cryptocurrency reserves ERG using SigRSV as the trust component which gives SigUSD’s $1 value. SigRSV collateral ratio is set to a minimum of a 400% ratio with SigUSD. This design prohibits liquidations such as we saw in [2020 March crash](https://forum.makerdao.com/t/black-thursday-response-thread/1433). As Emurgo states, "Black Thursday," when MakerDAO CDPs were triggered for liquidation due to volatility and then sold for $0 due to blockchain congestion that prevented others from bidding, demonstrated that a new design is needed. For SigmaUSD, this scenario is not possible.

## Oracle

Oracles are the backbone of a decentralized financial system. It connects off-chain data with the on-chain world. Normally, ETH has no info about the current market price. During a swap order in a decentralized exchange, a swap contract needs to call the data from various data sources to obtain market price. Thus, oracles are the messengers of the crypto ecosystem. Not only in atomic swaps but also in more complex interactions such as lending/borrowing assets or dynamic market-making need the data feeds provided by oracles. DeFi ecosystem suffered from Flash Loan attacks, caused by [misinformation from centralized price oracles](https://insights.glassnode.com/defi-attacks-flash-loans-centralized-price-oracles/).

Ergo developed [Oracle Pools](https://ergoplatform.org/en/blog/2020-08-31-ergos-oracle-pools-and-what-they-mean-for-the-ecosystem/) to maintain a robust DeFi ecosystem. Because of the eUTXO design and its rich programming language ErgoScript, oracle networks can be more decentralized. In the extended UTXO model, we have a lot of flexibility and power available to build new protocols. This can be utilized to construct oracle datapoint hierarchies of confidence. In short, they are an abstraction above oracle pools which allows us to scale the benefits of oracle pools as much as we desire, at the cost of price and speed. [ERG/USD oracle pool](https://explorer.ergoplatform.com/en/oracle-pools-list) is running on Ergo Blockchain.

## NFT

Blockchains aren’t only about cryptocurrencies. Audio or visual artworks can also be deployed on immutable smart contracts of blockchains. These artworks are represented by [Non-Fungible Tokens](https://en.wikipedia.org/wiki/Non-fungible_token). Furthermore, artworks can be traded in decentralized auction houses. This would help artists to reach the world without any restriction of governments or without any need for centralized licensing firms. It means the democratization of art markets with the help of public blockchain.

Some examples like [Rarible](https://rarible.com/) or [Opensea](https://opensea.io/) are auction markets running on Ethereum Network. Any artist can create and sell their artwork in there, however, gas prices to mint an NFT can take up to $100. Ergo’s scalable and faster design would reduce the gas costs to almost zero, without giving up security or speed. [Ergo NFT Auctionhouse](https://ergoauctions.org/#/auction/active?type=picture) is open for months and it allows listings for a picture, audio, or any other kind of non-fungible tokens.

## DEX

Until 2020 DeFi Summer, Value Locked in DeFi ([TVL](https://medium.com/coinmonks/google-sheets-analytics-total-value-locked-in-defi-33b926c18a9f)) was too low to use the platforms effectively. After an increasing interest and new token issuance every day, Decentralized Exchanges (DEX) came into the sunlight. Their benefits are for people who don’t want to give up the custody of their funds. DEXes democratized the exchange experience for both blockchain developers and crypto investors. 

[ErgoDEX](https://ergonaut.space/ergodex.pdf) can provide more functions than Ethereum based DEXes. ErgoDEX [has more properties](https://ergoplatform.org/en/blog/2021-04-06-ergodex-model-amm-and-order-book-type-exchange/) such as limit orders, partial filling, and buy-back supports. Ergo’s Multi-Stage Contracts allows for timed release payments, so a code implemented in the contract can help investors to cancel their order with a minimal loss if the developers of the project don’t deliver their promises. With the implementation of NIPoPoWS, DEX will be interoperable in both PoS and PoW blockchains. Users can enjoy the freedom of exchanges with self-custodial wallets.

## DAO

DAO stands for [Decentral Autonomous Organizations](https://www.investopedia.com/tech/what-dao/). Cryptocurrencies are decentralized (not all of them!), and so their platforms. The governance of these platforms is run by decentralized entities. Every decision is made by pseudo-anonym individuals of DeFi platforms for prohibiting the centralization of power. Therefore, certain tokens are used for voting or making enhancements to these DeFi platforms. [New coin issuances](https://wbtc.network/), redefinition of purposes etc. are all very vital features and can’t be left to a small group of individuals if the crypto ecosystem is for the masses. [Zero-Knowledge Treasury Vaults](https://ergoplatform.org/en/blog/2020-09-04-announcing-the-zk-treasury-on-ergo/) with multi-key signature are the first example of a DAO in Ergo Blockchain.

## Lending - Borrowing

Lending and borrowing are two components that increase liquidity flow in financial systems. For example, you have Bitcoins but you want to leverage your holding without selling your BTC. So, you can stake your BTC (you can also use your house as collateral in this sense) as collateral to borrow SigUSD and use it in exchanges or yield farming protocols. On the other side of your interaction, another user can leverage her unused SigUSD by staking in the lending protocol. Traditional banks have very low-interest rates and they might suck up a lot of revenue from your deposits. With decentral lending protocols such as [Compound](https://compound.finance/), users will be able to use lend/borrow services and move their funds across all crypto ecosystems without any need for centralized platforms such as banks or exchanges. Crypto lending protocols are open to more experimental designs such as [interest-free loans](https://www.ergoforum.org/t/interest-free-loan-contract/67), innovating even more use cases on blockchains.

## Derivatives

Besides buying and selling the tokens of a protocol, traders also want to monetize via various strategies such as options or leveraged future contracts. In traditional finance, these tools are provided by brokerage firms and in the crypto world by centralized exchanges. However, this can turn out to be very harmful towards traders by making exchanges big casinos who can see the player’s hands. That’s why in decentralized finance, there is also an alternative as options or derivatives trading smart contract platform. [Synthetix](https://www.synthetix.io/) is an example of leveraged assets trading platform. The platform token creates liquidity for the traders who want to take leveraged positions. [Hegic](https://www.hegic.co/) on the other hand provides an options trading platform for traders who wants to bet on call-put options via smart contracts. These are just two examples of derivatives protocols on Ethereum. Ergo Blockchain’s Multi-Stage Contracts can also provide these protocols on top of it.

## Insurance

Another big sector of the finance industry is Insurance. Every exchangeable asset carries a risk of losing it, whether by unprecedented risks such as taking a bullet to your Ledger Wallet or foreseeable risks such as [rug pulls](https://www.coingecko.com/en/glossary/rug-pulled). New protocols emerged such as [Nexus Mutual](https://nexusmutual.io/) to tackle the decentral insurance problem. If you think about insurance, it pays a premium to risk bearers in case a bad event happens, exchanging your money for security. In a Decentralized Insurance platform: Your participation, risk bearers’ participation and validation of the trade by oracles can all be governed by smart contracts to create a smoothly functioning DeFi ecosystem.

## Yield Aggregation

So after an expansion of new decentralized exchanges such as [Bancor](https://bancor.network/), [Balancer](https://balancer.finance/), [Uniswap](https://uniswap.org/), [Sushiswap](https://www.sushi.com/), and [Curve](https://resources.curve.fi/), people are started to look for easier ways to move capital around those exchanges to create the best yields. Yield Aggregators are helping users to automate the liquidity farming actions. The first example of a yield aggregation protocol is [Yearn Finance](https://yearn.finance/). In the protocol, users can choose different yield farming strategies among the vaults deployed. Not only users but also developers can leverage yield farming platforms by creating their unique yield farming strategies and deploying them on protocols. Such examples will be very useful for market-making algorithms in the future by supporting deep liquidity all across DeFi.

## Index Coins

Not all crypto investors are conscient about different blockchain use cases. Some of the investors may want to benefit from indexed tokens to invest in various cryptocurrencies. For such an innovation dynamic market-making(DMM) algorithms would be necessary to adjust the funds after price changes. Besides, people who will release index tokens must have the market knowledge to decide which tokens must be involved in the indexed and for how many percentage. Some examples of index coins running on Ethereum are ASSY, YETI, PIPT, YLA issued by [Powerpool Protocol](https://powerpool.finance/). 

## Asset Tokenization

Asset Tokenization is meeting traditional financial assets with crypto. A centralized exchange [FTX](https://ftx.com/markets/stocks) provides US stocks in exchange for cryptocurrencies. This phenomenon, however, is very new due to regulation problems. Stock tokens are not yet traded on decentralized exchanges. Another example of tokenization of real-world assets would be real estate tokenization. With the help of cryptocurrencies, [houses can be fractionated](https://labsgroup.io/) into thousands of tokens representing real estate. These kinds of implementations will help retail investors to invest in houses all around the world with minimal savings.

*All the utilities of traditional banks are becoming decentralized applications on smart contract platforms. Ergo is providing robust and rich infrastructure with **ErgoScript** language to support a complex DeFi ecosystem powered by **Multi-Stage Contracts**.*

