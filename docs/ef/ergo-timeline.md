
# Timeline

This page gives a rundown of the Ergo Foundation's key achievements, developments, and milestones from 2020 till now. It highlights the yearly progress in different areas like partnerships, core developments, scaling, tooling, and community projects. The timeline also gives a snapshot of ongoing and future projects that are either in progress or under development. Since Ergo is a grassroots project, the line between EF and community achievements can sometimes blur, so we've included all accomplishments and made distinctions where possible.

After adding UTXO set snapshots and NiPoPoWs to the [pruned full node](modes.md) for faster bootstrapping, core development is now focused on optimizing this implementation and exploring sub-block confirmation protocols to enhance transactions and finality. For more details, see the [scaling roadmap](roadmap.md).

### 2024

#### In Progress

Discussions ongoing with several prominent on-ramps trying to secure US access, as well as smaller exchanges which should help our volume, and regional exchanges to ensure ERG is accesible worldwide.

- ErgoSummit
- Metamask
- Website Refresh
- Trust Wallet

#### In Development

- [Sub-block confirmation protocols](subblocks.md)
- EVM Bridge for [Rosen](rosen.md)
- [DexyGold](dexy.md)
- [Machina Finance](machina-finance.md)
- [ChainCash](chaincash.md)

##### Community

- PalmyraComDex MVP
- [BlitzTCG](blitz.md)
- [Paideia](paideia.md)
- [GuapSwap](guapswap.md) V2
- [Thz.FM](thz-fm.md) MVP
- ErgoNames
- [Analog Ergo](analog-ergo.md)
- [SigmaGold](siggold.md)

#### Core Development for Q1/Q2 2024

**[Node](install.md) Development:**

- Implementation of [sub-blocks](subblocks.md)
- Optimization and review of the P2P layer
- Avoidance of re-checking signatures when re-validation provides the same result (e.g., for P2PK inputs)
- Further optimizations during bootstrapping
- Storing only part of the UTXO set tree in RAM
- Potential switch to RocksDb
- Additional tests and polishing for extra indices, scans, and wallet
- Modularization of the codebase to provide a framework for implementing sidechains

**[Sigma](sigma-lang.md) Development:**

- Implementation of Sigma 6.0
- Investigation into the possibility of extending the validation context (useful for sidechains)

**[Sigma-Rust](sigma-rust.md) Development:**

- Implementation of [JIT costing](jitc.md)
- Implementation of 6.0 features to match Scala's capabilities

Please let us know in the development chats what is needed for AppKit, ergo-wallet, and other core repositories.



### 2023

- **Announcements**: [Significant donations made to EF Treasury from ecosystem projects](https://ergoplatform.org/en/news/news/The-Ergo-Foundation-Path-to-a-Robust-Digital-Ecosystem), Storage rent activation. EF makes a donation to the Sigmanauts Treasury
- **Partnerships**: Bitpanda listing, nonkyc.io listings and native token integrations, Koinly integration, StealthEx listing.
- **Events**: [Ergo Summit 2023](https://ergoplatform.org/en/news/Ergo-Summit-2023), ErgoVersary 2023, Ergohack VI and VII.
- **Core**: Sigma.js, UTXO Set Snapshots and bootstrapping with NiPoPoWs, work on SigmaState. 
- **Scaling**: An update from kushti *'A Scalability Plan for Ergo'* and work on a [sub-block confirmation protocol](https://ergoplatform.org/en/blog/Ergo’s-Newest-Advancement-Sub-Blocks).  
- **Tooling**: FleetSDK, [Ledger in developer mode](https://ergoplatform.org/en/blog/Ledger-Launches-Ergo-Support-in-Developer-Mode), Oracles v2.

#### Ecosystem & Community

- **Community**: GreasyCEX, Erg0ne, Sigmanauts @ NFTxLV
- **Mining**: Sigmanauts mining pool.

##### Launched in 2023

- [Rosen Lite](https://ergoplatform.org/en/news/Rosen-Bridge-Officially-Launches-on-Ergo-Mainnet/)
- [SigmaFi](https://ergoplatform.org/en/blog/Sigma-Finance-A-Peer-to-Peer-Bond-Protocol)
- [Duckpools](https://ergoplatform.org/en/blog/Duckpools-A-Lending-and-Borrowing-Protocol-on-Ergo)
- [AuctionHouse v3](https://ergoplatform.org/en/news/Auction-House-V3-Launches-on-Mainnet)
- [AuctionCoin](https://auctioncoin.app/) 
- [Hodlcoin](https://app.hodlcoin.co.in/) & [PheonixFinance](https://phoenixfi.app/)
- [Hodlbox](https://hodlbox.xyz/)
- [Lilium](https://www.liliumergo.io/)
- [single-tx-swap](https://www.single-tx-swap.com/)
- Spectrum Finance launches yield farming
- [EXLE MVP](https://ergoplatform.org/en/blog/Empowering-Communities-Interest-Free-Loans-Drive-Economic-Growth-for-Kenyan-Cooperative)
- [TabbyPOS](https://www.tabbylab.io/)
- [Crux Finance MVP](https://cruxfinance.io/)
- **Tooling**: ergexplorer, ergo-lib-go, Off-The-Grid, uExplorer






### 2022

- Warwick (CW), Stacie, and Alison Robson join the Ergo Foundation as Officers to help expand the EF to the wider community.
- Created and distributed a pitch deck highlighting the 'open source economy' rapidly developing on Ergo and opportunities that present for private investors. 

**2022 Key Achievements**


- Listings on Indodax and Huobi, Bittrue. 
- Parallel asset launches on Flux.
- [EIP-27](eip27.md) re-emission soft-fork boosting confidence in Ergo and ensuring long-term network security.
- [EIP-37](eip37.md) (Difficulty retargeting hard fork).
- Two summits and three hackathons with 45 entries total.
- The redesign & relaunch of [ergoplatform.org](https://ergoplatform.org) and [sigmaverse.io](https://sigmaverse.io)
- Node [V5 JITC]().

### 2021

- Joseph Armeanio joins the Ergo Foundation.
- Mark Glasgow joins the Ergo Foundation, replacing Martin S.
- On Nov 1, IOHK Business Developer Daniel Friedman was appointed Advisor to Ergo Foundation Board.
- On Dec 19, The Ergo Foundation incorporates in Singapore.

**2021 Key Achievements**

- Autolykos v2 Hard-Fork opened Ergo to mining pools, improved liquidity and brought many new users into the ecosystem.
- Partnership with Jinse and China marketing efforts that grew the Chinese community to >10k members.
- Listing on KuCoin, Changelly.
- UTXO Alliance formed. 
- EIP-27 Discussions start.
- The EF hired wallet developers to alleviate users' lack of usable wallet options.
- Obtained a written US Legal Opinion that determines Ergo is unlikely to be classified as a security. 
- Our first summits and two hackathons.
- Incorporated the first legal entity in Singapore to meet the necessity of formal arrangements now required in the industry.

### 2020

- Jan 7, Introducing the Ergo Foundation, a community-driven entity

**2020 Key Achievements**

- Roadmap released, Discord started
- Partnership with Emurgo and extensive joint research brought us Oracle Pools, SigmaUSD, and the headless dApp framework. 
- Listing on CoinEx, Gate.io.

