
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