---
tags:
  - Roadmap
---

# Ergo Development Roadmap & History

Ergo is a blockchain platform designed to provide a secure, efficient, and user-friendly environment for the development of decentralized applications and financial tools. This roadmap outlines the key milestones and objectives for the development and growth of the Ergo ecosystem.

## Resources

//// details | Vision & Key Features
    {type: info, open: false}

Ergo is a cutting-edge smart contract platform that provides secure, accessible, and decentralized financial tools to empower ordinary people. Utilizing a sophisticated scripting language and advanced cryptographic features, Ergo builds on fundamental blockchain principles to transform the concept of Contractual Money.

Ergo aims to establish itself as a mineable digital asset akin to "Digital Gold 2.0," supporting trustless derivatives and dynamic contracts. The development of Ergo’s DeFi ecosystem and the integration of sidechains will broaden the decentralized monetary base and derivative money supply, enhancing financial inclusivity and accessibility worldwide.

Ergo’s commitment to decentralization, fairness, and accessibility is evident in its adoption of the Autolykos Proof-of-Work protocol, which facilitates a user-friendly environment where lightweight clients can interact directly with the blockchain, making Ergo a practical and programmable currency ready for use.


- [x] **eUTXO Model:** Allows UTXOs to carry arbitrary data and complex scripts, enabling advanced smart contracts
- [x] **Autolykos PoW Algorithm:** ASIC-resistant and designed for fair mining, promoting decentralization
- [x] **Emission Schedule:** Ensures a stable and predictable supply of ERG tokens
- [x] **NiPoPoWs (Non-Interactive Proofs of Proof-of-Work):** Enables efficient light clients, log-space mining, trustless sidechains, and enhances accessibility and decentralization by allowing mobile SPV clients and lite full nodes
- [x] **ErgoScript:** Supports clear and concise smart contract development with Σ-protocols
- [x] **Storage Rent:** Mitigates blockchain bloat, incentivizes efficient storage usage, and contributes to long-term economic sustainability
- [x] **Turing-Complete Smart Contracts:** Allows for complex on-chain computations and advanced dApp development
- [x] **Long-Term Economic Sustainability:** Ensured through storage rent, transaction fees from DeFi, and subpool mining

For more information please see the [Why Ergo?](https://docs.ergoplatform.com/dev/protocol/why/) section.

////


//// details | General Overarching Ergo Design and Implementation Roadmap 
    {type: info, open: false}
/// details | Phase 1: Foundations 
    {type: info, open: true}
- [x] Start with the basic design of Ergo as digital gold (commodity money).
- [x] Introduce programmability features including:
    - [x] Crypto contracts
    - [x] Stealth addresses
    - [x] Arbitrarily complex signatures
    - [x] Mixing schemes
- [x] Position Ergo as a basis for unstoppable, grassroots economies, serving as a decentralized central bank digital currency [(CBDC)](cbdc.md) for the people.
///
/// details | Phase 2: Initial Experiments 
    {type: info, open: true}
- [x] Conduct initial experiments to test functionality and user engagement.
- [x] Evaluate the outcomes considering the initial motivations.
///
/// details | Phase 3: Defining Adoption 
    {type: info, open: true}
- [ ] Clarify the term "adoption" as it is often ambiguous in industry discussions.
- [ ] Develop metrics or KPIs to measure adoption success.
///
/// details | Phase 4: Scaling and Optimization 
    {type: info, open: true}
- [x] Peer-to-peer (P2P) level optimizations and rework.
- [ ] Consider pre-block commitments to transaction ordering (sub-blocks).
- [ ] Aim to increase transactions per second (TPS) while maintaining security.
**Constraints for Scaling**
- Limitations include requirements for a flat P2P network running on commodity hardware.
- No use of centralized or "bankster" data centers for scalability.
///
/// details | Phase 5: Offloading Solutions 
    {type: info, open: true}
- [ ] Propose options for offloading transactions to Layer 2 or sidechains, if not already implemented.
- [x] Introduce ["Know Your Assumptions" KYA](kya.md) as a way to explain security in offloading options in a concise and understandable manner.
///
/// details | Phase 6: Convergence 
    {type: info, open: true}
- [ ] Multiple developments in scaling, optimization, and offloading are expected to converge, culminating in a comprehensive solution for widespread adoption.
///
Summarised from [Kushti, 7 Aug, 2023](https://t.me/ergoplatform/419168)

/// details | Scaling Ergo
    {type: info, open: false}
Creating a scalable blockchain infrastructure is a complex task. Ergo, fortified by a decade of [research](documents.md), rigorous testing, and ongoing development, has risen to the challenge. This guide will walk you through Ergo's sophisticated scalability features.

Blockchain scalability is primarily influenced by three factors:

- **Cryptoeconomic incentive model**: This model ensures that miners receive suitable rewards for the various costs associated with scaling a blockchain, which may include an increase in state-related costs.
- **Consensus model**: The chosen model can determine the feasibility of certain scalability solutions. For example, the Proof of Stake consensus model does not support Non-interactive Proofs of Proof-of-Work (NiPoPoWs).
- **Accounting model**: This pertains to the management of transactions and operations within the blockchain. Bitcoin uses the UTXO Model, while Ethereum uses the Account Model.

Ergo's innovative approach to scalability, underpinned by these aspects, sets it apart from other blockchain technologies. Unlike Ethereum's Account model, which manages storage changes and validity checks on-chain during code execution, Ergo's [eUTXO](eutxo.md) employs a unique strategy: transactions are created off-chain, and validation checks are conducted on-chain.

This approach reduces the operational load on each network node, thereby enhancing overall efficiency. The immutability of the transaction graph allows for further optimization of this process, increasing the number of transactions processed per second. Additionally, the use of light-verifying nodes boosts both the scalability and accessibility of the network.

To gain a comprehensive understanding of Ergo's scalability, delve into the role of each layer in this process:

- [Layer 0](layer0.md): The *Network* or *Peer-to-Peer* Layer
- [Layer 1](layer1.md): The Core Blockchain Layer
- [Layer 2](layer2.md): The Off-chain Layer

These layers work in harmony to enhance Ergo's scalability, making it a flexible and potent choice for both developers and users. This collaborative model enables Ergo to provide robust, scalable solutions that are prepared to meet the challenges of global expansion.
///

////
//// details | Who develops Ergo?
    {type: info, open: false}
Ergo is developed a by a combination of the [Ergo Foundation](ergo-foundation.md), community developers and the recently launched [DevDAO](devdao.md)

/// admonition | See the [code respositories supported by the Ergo Foundation](ef-scope.md#code-repositories-supported-by-the-ergo-foundation).
    type: info
///

////




## Ergo Timeline


/// details | 2019: Genesis Year
    {open: false}

- **Milestones:**
    - **July 1:** Ergo mainnet launched during the "crypto winter"
    - **Autumn:** Ergo Foundation established
- **Development:**
    - First tools and libraries emerged
    - Inaugural crowdfunding using UTXOs and smart contracts
    - Zero-join paper published
    - Multi-stage contracts paper by Amitabh released
    - First smart contract formally verified
///



/// details | 2020: Foundation Building
    {open: false}

- **Milestones:**
    - **January 7:** Introduction of the Ergo Foundation as a community-driven entity
- **Launches:**
    - Ergo Mixer (initially a raw application, later improved by Anon2020)
    - **Late August:** Oracle pools
    - Zero-knowledge treasury by anon_real
    - Auction House
- **Partnerships:** Collaboration with Emurgo for joint research (Oracle Pools, SigmaUSD, headless dApp framework)
- **Listings:** CoinEx, Gate.io
- **Community:** Roadmap released and Discord community initiated
///



/// details | 2021: Expansion and Recognition
    {open: false}

- **Launches:**
    - **Q1:** SigmaUSD launched
- **Ecosystem Growth:**
    - Spectrum DEX and DeFi ecosystem development began
    - Autolykos v2 hard fork: opened Ergo to mining pools, improved liquidity and brought many new users into the ecosystem
- **Partnerships and Listings:**
    - Collaboration with Jinse, Chinese community expanded to 10,000+ members
    - Listed on KuCoin and Changelly
- **Community Milestones:**
    - UTXO Alliance formed
    - Inaugural Ergo Summit and two hackathons
- **Governance and Legal:**
    - [EIP-27](eip27.md) discussions initiated
    - US Legal Opinion obtained on Ergo's security classification
    - **December 19:** Ergo Foundation incorporated in Singapore
- **Team Expansion:**
    - Joseph Armeanio and Mark Glasgow join Ergo Foundation (Mark replacing Martin S.)
    - **November 1:** Daniel Friedman (IOHK) appointed Advisor to Ergo Foundation Board
- **Additional Achievements:**
    - The EF hired wallet developers to alleviate users' lack of usable wallet options
///


/// details | 2022: Technical Advancements
    {open: false}

- **Protocol Upgrades:**
    - [EIP-27](eip27.md) (emission soft-fork) was implemented
    - [EIP-37](eip37.md) (difficulty retargeting hard fork) was implemented
- Ergo was listed on the following exchanges:
    - Indodax
    - Huobi
    - Bittrue
- **Ecosystem Expansion:**
    - Parallel asset was launched on Flux
    - The [Sigmanauts Program](sigmanauts.md) was launched on 01/22
- **Community Engagement:**
    - Two summits and three hackathons were held, with a total of 45 entries
    - [ergoplatform.org](https://ergoplatform.org) and [sigmaverse.io](https://sigmaverse.io) were redesigned and relaunched
- **Technical Milestone:** Node V5 with [JITC](jitc.md) (Just-In-Time Compilation) was released
- **Team Growth:**
    - Warwick (CW), Stacie, and Alison Robson joined as Ergo Foundation Officers
- **Marketing Initiative:** An 'open source economy' pitch deck was created and distributed
///



/// details | 2023: Ecosystem Flourishing
    {open: false}

- **Milestones:**
    - [Significant donations to EF Treasury from ecosystem projects](https://ergoplatform.org/en/news/news/The-Ergo-Foundation-Path-to-a-Robust-Digital-Ecosystem)
    - Storage rent activation
    - Sigmanauts
        - **01/23**: [sigmanauts.com](https://sigmanauts.com/) launches.
        - **03/23**: Sigmanauts [voting rework](https://docs.google.com/document/d/1kuf_l9tZOdg7vMgVSKuV0FIUlpHmxWiWjMi89z-XTdE/edit#heading=h.e1tnpe3qjzte).
        - **03/23**: [Mission Statement](https://docs.google.com/document/d/1J6PdyyxoEEqI0nEr64ZZBGU4Lkr8Cr37GqNSs4qHo7Q/edit) published.
        - **00/23**: The Sigmanauts attend their first event @ RareEVO.
        - **00/23**: The Ergo Foundation donates 160,000 SPF to the Sigmanauts treasury.
        - **00/23**: The Sigmanauts begin managing the [@ergo_platform](https://x.com/ergo_platform) Twitter account.
- **Integrations:**
    - Bitpanda listing
    - nonkyc.io
    - Koinly
    - StealthEx
- **Core Developments:**
    - Sigma.js
    - UTXO Set Snapshots
    - bootstrapping with NiPoPoWs
    - SigmaState advancements
    - Kushti's 'A Scalability Plan for Ergo' and [sub-block confirmation protocol](https://ergoplatform.org/en/blog/Ergo's-Newest-Advancement-Sub-Blocks) work
- **Development:**
    - [Pruned Full Node](pruned-full-node.md)
    - Plasma Library on top of AVL Trees, drastically improving light client verification efficiency compared to traditional merkle tree data structures
    - ergo-lib-go
    - uExplorer
    - FleetSDK
    - [Ledger support (developer mode)](https://ergoplatform.org/en/blog/Ledger-Launches-Ergo-Support-in-Developer-Mode)
    - Oracles v2
- **Community Events:**
    - [Ergo Summit 2023](https://ergoplatform.org/en/news/Ergo-Summit-2023)
    - ErgoVersary 2023
    - ErgoHack VI and VII
- **Community Initiatives:**
    - Erg0ne
    - Sigmanauts @ NFTxLV
    - Sigmanauts mining pool
- **Ecosystem:**
    - ergexplorer
    - Off-The-Grid
    - DeFi:
        - [Rosen Lite](https://ergoplatform.org/en/news/Rosen-Bridge-Officially-Launches-on-Ergo-Mainnet/)
        - [SigmaFi](https://ergoplatform.org/en/blog/Sigma-Finance-A-Peer-to-Peer-Bond-Protocol)
        - [Duckpools](https://ergoplatform.org/en/blog/Duckpools-A-Lending-and-Borrowing-Protocol-on-Ergo)
        - [AuctionHouse v3](https://ergoplatform.org/en/news/Auction-House-V3-Launches-on-Mainnet)
        - [AuctionCoin](https://auctioncoin.app/)
        - [Hodlcoin](https://app.hodlcoin.co.in/) & [PhoenixFinance](https://phoenixfi.app/)
        - Spectrum Finance yield farming
        - [Hodlbox](https://hodlbox.xyz/)
        - [Lilium](https://www.liliumergo.io/)
        - [single-tx-swap](https://www.single-tx-swap.com/)
        - [EXLE MVP](https://ergoplatform.org/en/blog/Empowering-Communities-Interest-Free-Loans-Drive-Economic-Growth-for-Kenyan-Cooperative)
        - [TabbyPOS](https://www.tabbylab.io/)
        - [Crux Finance MVP](https://cruxfinance.io/)
        - [x] SigmaO options trading platform


///
/// details | 2024: Future Horizons (In Progress and Planned)
    {open: true}


- Ongoing work to define rules for new releases and research-driven development frameworks
- Encouragement of new stakeholder organizations within the Ergo ecosystem

#### Milestones

- [x] [ErgoHack VIII - Ergo as a Smart Layer](http://docs.ergoplatform.org/events/ergohack/#ergohackviii)
- [x] [DAO for Ergo core](devdao.md)
- [x] Ergo achieved [#1 in TVL% of market cap for a PoW chain](https://x.com/cannon_qq/status/1772254513920876671?t=8KODg1I33kaPSNQw_wn2Bg)
- [x] Ergo listed on MEXC exchange
- [x] Ergo Node improvements:
    - Successful migration from LevelDB to RocksDB
    - 6.0.0-alpha1 release with Global.some/none methods and AVL+ Tree optimizations
- [x] Sigma protocol updates:
    - Sigma 5.0.14 release
    - Sigma 6.0.0 update with scrypto 3.0.0
- [x] Infrastructure improvements:
    - Sigmaspace blockchain indexer completion (full index <24 hours)
    - Resolved indexer issues (rollbacks, duplicates, threading)
    - Sigmaspace explorer API compatibility with ergoplatform.org
    - Sigmaspace storage rent dashboard launch

#### Sigmanauts Achievements

- [x] Sigmanauts Mining Pool launch
- [x] Storage rent integration completed for Sigmanauts Mining Pool
- [x] First proposal on Paideia passes (January 2024)
- [x] Official takeover of Market-Making services management (March 2024)
- [x] Substantial EF grant received matching Sigmanauts-raised funds (March 2024)

#### Application Achievements

**Wallet Developments**

- [x] Nautilus Wallet improvements:

    - Version 0.15.0 release
    - Abyss v0.13.0-beta.1 with performance improvements
    - New frontend implementation
    - Improved Firefox compatibility
    - Enhanced asset ranking and sorting in Assets and Send tabs
    - Comprehensive dApp documentation

- [x] Minotaur Wallet:

    - Version 2.0.1 production release

- [x] Satergo Wallet:

    - 3x faster transaction history loading
    - New Ergonnection library version
    - Simplified Windows installations

**Infrastructure & Tools**

- [x] Sigmaspace development:

    - Complete blockchain indexer (<24 hours full index)
    - Storage rent dashboard launch with tracking features
    - Explorer API compatibility with ergoplatform.org

- [x] Lithos progress:

    - Initial client development completion
    - Fraud proofs contracts for NISPs (PoW verification, header validation)

- [x] Rosen Bridge improvements:

    - Enhanced decimal handling logic for cross-chain transactions
    - API and UI revisions

**DeFi Applications**

- [x] SigmaUSD improvements:

    - Enhanced stability mechanisms
    - Oracle upgrade exploration

- [x] Fleet SDK advancements:

    - AgeUSD integration completion
    - Enhanced development toolkit

- [x] Celaut platform development
- [x] Bene fundraising platform updates

#### Development Focus

**Reference Client**

- [ ] [Sub-blocks](subblocks.md) implementation:

    - Data types and update procedures
    - Candidate generation
    - Block template regeneration integration

- [ ] P2P layer optimization and review
- [ ] Bootstrapping improvements
- [ ] Sidechain implementation modularization
- [x] RocksDB integration and optimization
- [ ] Enhanced testing for indices, scans, and wallet

**Sigma**

- [ ] [Sigma 6.0 implementation](https://github.com/ergoplatform/eips/blob/a24fc414abbc10e6ee59f878b280d9ecc725e10c/eip-0050.md) and validation context extension research

    - [x] Progress on Sigma 6.0 features:

        - SOption[] serialization
        - Header serialization/deserialization
        - Header.checkPoW implementation
        - Global.powHit implementation
        - Enhanced collections and numeric methods
        - Improved error messages


- [ ] Signature re-checking optimization
- [ ] ErgoScript 2.0
- [ ] [EIP-0046: Atomic Chains](https://github.com/ergoplatform/eips/blob/2de4ea0deff12a276f74df57ef3a14dab2c5dfb8/eip-0046.md)
- [ ] [EIP-0047: Pooled Transaction Inputs](https://github.com/ergoplatform/eips/blob/0836dd1eca323c6b5fd6b5172c27a465bd4449cd/eip-0047.md)
- [ ] [MerkleTrees](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/296)
- [ ] [EIP-44](https://github.com/ergoplatform/eips/blob/master/eip-0044.md): Arbitrary Data Signing Standard
- [ ] Revisiting formal verification implementation
- [ ] Bulletproofs
- [ ] Exploration of Rust and JavaScript support in addition to ErgoScript
- [ ] Consideration of high-level language support (e.g., Lisp)
- [ ] Improvements to error-checking and debugging tools
- [x] Enhanced stateless validation in Sigma-Rust

**SDKs**

- [x] [AppKit](appkit.md)
- [x] [FleetSDK](fleet.md)

    - [x] Integration with AgeUSD stablecoin
- [x] [sigma-rust](sigma-rust.md)
    - [ ] JIT costing implementation in Sigma-Rust
    - [ ] 6.0 features implementation in Sigma-Rust
    - [ ] Sigma-Rust-Mini development
- [x] Sigma.js

**Libraries & Tooling**

- [x] [ergo-lib-go](https://github.com/sigmaspace-io/ergo-lib-go)
- [x] [escript.online](https://escript.online)
    - [x] [Blockly Playground Integration](https://escript.online/blockly)
- [x] Token metadata standards discussion
- [x] Lithos light-client integration progress

**Mining Ecosystem**

- [ ] Lithos decentralized mining pool infrastructure expected launch by end of 2024
- [ ] Plans for reintroduction of Fair Initial Mining Offerings (FIMOs)

**Wallets**

- [x] Nautilus

    - [x] Manifest v3 rework

- [ ] Ledger

    - [x] Available in developer mode

- [x] Keystone Integration progress
- [ ] EIP-12 / EIP-20
- [ ] Metamask integration
- [ ] Trustwallet Integration
- [ ] Light SPV Clients using NiPoPoWs

**Ecosystem Growth**

- [x] DeFi ecosystem expansion:

      - New protocols exploration
      - NFT platform improvements

- [ ] Continuous integration of new protocols and platforms
- [x] UX/UI improvement initiatives across applications

**Documentation & Education**

- [x] New educational materials on:

      - Merkle trees
      - Extension blocks
      - Soft-fork rules
      - Signature schemes
      - ErgoScript compilation

- [x] Ergo Forum enhancement as knowledge hub

**Development Process Improvements**

- [x] Enhanced focus on code quality and review processes
- [x] Improved version management procedures
- [x] Better transparency in development communication

**Ongoing Challenges**

- [ ] **Scalability Improvements (Layer 1 and Layer 2)**

  - Sub-blocks implementation for enhanced transaction throughput
  - Layer 2 solutions exploration:

      - Weak consensus mechanisms for local payment networks
      - Digital bearer certificates

  - P2P layer optimization for network efficiency
  - Bootstrapping improvements for faster node synchronization
  - Research into enhanced transaction processing and network scalability

- [ ] **Usability Enhancements**
  - Wallet and dApp user experience improvements
  - Development tools advancement:

      - Comprehensive ErgoScript debugger
      - Enhanced escript.online functionality
      - Structured output for debugging

  - Documentation and education:

      - Improved developer documentation
      - Enhanced tutorials and guides
      - Better onboarding resources

  - Streamlined development workflows

- [ ] **Security Strengthening**

    - Ongoing vulnerability assessment and mitigation
    - Protocol security mechanism enhancements
    - Smart contract security improvements
    - Regular security audits and reviews
    - Implementation of best practices for secure development

- [ ] **Ecosystem Development**

    - Continuous discussions for improved accessibility
    - Potential listings on US markets
    - Balancing rapid development with thorough testing
    - Enhanced coordination between development teams
    - Streamlined contribution processes

- [ ] **Technical Debt and Optimization**

    - Code quality maintenance
    - Performance optimization
    - System architecture improvements
    - Technical documentation updates
    - Development process refinements
///






## DeFi Ecosystem
Every new addition to our growing DeFi ecosystem contributes to the expansion of trustless collateral, the decentralized monetary base, and the supply of derivative assets.


### Decentralized Exchanges 

- [x] [ErgoDex](spectrum.md) (AMM + Yield Farming)
- [x] [ErgoAuctionHouse](ergo-auctions.md) (peer-to-peer auctions)
    - [x] [Trade House](https://ergoauctions.org/trade?pair=ERG-SigUSD) (orderbook-based P2P DEX)
- [x] [SkyHarbor](skyharbor.md) (NFT Market)

    - [x] [SkyHarbor Raffle for new UI](https://skyharbor.medium.com/enhancing-the-nft-experience-skyharbors-new-initiative-9679e94e3cd8)
- [x] [single-tx-swap](https://www.single-tx-swap.com/) (trustless p2p swaps)
- [x] [TokenJay](https://tokenjay.app/app/#purchases) (p2p escrow)
- [x] [Crooks Finance](https://crooks-fi.com/) (buying, trading, and staking meme cryptocurrency tokens)
- [ ] [PalmyraComDex](palmyra.md) (commodities DEX) ([Alpha live](https://palmyra.app/)!)
- [ ] [Crystal Pool](crystal-pool.md) (instant L1 order-based trading)
- [ ] [Machina Finance](machina-finance.md) (grid DEX)
- [x] [Mew Finance](https://mewfinance.com/)

###  Stablecoins

- [x] [SigmaUSD](sigmausd.md) stablecoin (Djed protocol)
    - [ ] [SigmaUSD v2](https://gist.github.com/kushti/3f34ed7d70cc6919c29f5bc65772b02e)
- [x] [Gluon](gluon.md) (gold stablecoin)
- [ ] [DexyGold](dexy.md) (seigniorage stablecoin)

### Lending and Borrowing
- [x] [SigmaFi](sigmafi.md) (peer-to-peer loans via bonds)
- [x] [Duckpools](duckpools.md) (lending pools)
    - [x] [optionPools](optionPools.md) (option markets)
- [x] [EXLE](exle.md) (uncollateralized lending)

### Gaming and Metaverse
- [x] [BlitzTCG](blitz.md) (trading card game)
- [x] [CyberVerse](cyberverse.md) (metaverse gaming platform)

    - [x] Cyberverse Multiplayer

### Derivatives and Synthetics
- [x] [SigmaO](sigmao.md) (trustless options)
- [x] [HodlCoin](hodlcoin.md) (trustless ERG derivative with non-declining price)
- [x] [AuctionCoin](auction-coin.md) (emission via auctions)
- [x] [Hodlbox](https://hodlbox.xyz/) (long-term locking)
- [ ] [OptionCoin](optioncoin.md) (decentralized options trading with token emission)
- [ ] [ChainCash](chaincash.md) (elastic p2p money creation based on assets and trust)

### Crowdfunding

- [x] [ErgoRaffle](ergoraffle.md) (decentralized crowdfunding)
    - [ ] V2 [features](ergoraffle.md#v2)

### Interoperability and Bridges

- [x] [Oracle Pools](oracle.md) (federated transparent data providing)
- [x] [Rosen Bridge](rosen.md) (two-layered federated bridge)
    - [x] ADA Bridge
    - [x] BTC Bridge
        - [ ] Runes Integration
    - [x] EVM Bridge
    - [ ] R&D for Monero
    - [ ] RosenFast Service
    - [ ] Bridge Expansion Kit
    - [ ] Bridge SDK
    - [ ] DOGE Bridge
    - [ ] BCH Bridge
    - [ ] Hummingbot Integration / Customisation
- [ ] [Sigma Chains](sigma-chains.md) - Revitalizing Proof of Work

    - [ ] Trustless Relays (Superseding BTC custody solutions with Ergo smart-contracts)
    - [ ] Implementing sidechains with trustless transfers and various consensus mechanisms (merged mined with ERG, other blockchains, or double merged mined)
    - [ ] Expanding Ergo's contractual layer to sidechains, incorporating features like Bulletproofs-based sigma protocols and elevating certain contracts to first-class citizens
    - [ ] Experimenting with scalability solutions like sharding on sidechains
    - [ ] Utilizing ERG and other tokens on Ergo and sidechains from launch, fostering a rich and diverse DeFi ecosystem
    - [ ] Launching existing applications on sidechains, contingent on modifications to the contractual layer



### Privacy and Mixing
- [x] [ErgoMixer](ergomixer.md) (non-interactive, non-custodial mixer)
    - [x] Stealth addresses
- [ ] [SigmaJoin](sigmajoin.md)
- [ ] Privacy-Preserving Voting

### DAOs and Governance

- [x] [Paideia](paideia.md) (DAO toolkit)
- [ ] [Lithos](lithos.md) (decentralized mining infrastructure)
- [ ] [The Field](the-field.md) (peer-to-pool pledging protocol)


### Tooling

- [x] [Lilium](https://www.liliumergo.io/) (NFT sale platform)
- [x] [Moria Finance](moria-finance.md) (fund management)
- [x] Trustless Relys
- [x] [Random Number Generator](sigmarand.md)
- [x] [TabbyPOS](tabbypos.md) (Point of Sale device)
- [x] [Crux Finance](https://cruxfinance.io/) (Token charts, portfolio viewer and more)
- [ ] [ErgoNames](ergonames.md) (decentralized naming system)
- [ ] [Reputation System](reputation-system.md) (Testnet Live)

#### Miner Tooling

- [x] [GuapSwap](guapswap.md) (miner token swapping)
- [x] [CYTI](cyti.md) (Choose Your Token ID)


#### Other Infrastructure

- [ergexplorer](https://ergexplorer.com/)
- [sigmaspace](https://sigmaspace.io/)


## References


//// details | References
    {type: info, open: false}


/// details | Developing Digital Gold 2.0 and its Infrastructure 
    {type: tip, open: false}

The following is adapted from [this post on the R&D DAO for Ergo Core thread](https://www.ergoforum.org/t/ergodevs-r-d-dao-for-ergo-core/4663). 

**Vision**
The Ergo Core Dev DAO envisions Ergo as Digital Gold 2.0, a mineable digital commodity with trustless derivatives and expressive contracts. By building upon Ergo's robust DeFi ecosystem and introducing sidechains, we aim to expand the decentralized monetary base and derivative money supply, creating a more inclusive and accessible financial system for the Ergo community and beyond.

**Completed Milestones**
The Ergo platform, with the support of the Ergo Foundation and community developers, has already made significant strides in developing its infrastructure and DeFi ecosystem. This includes launching basic infrastructure such as wallets and explorers, as well as a wide range of DeFi tools and trustless derivatives, such as:

- [x] SigmaUSD stablecoin (Djed protocol)
- [x] Spectrum DEX (AMM-based)
- [x] ErgoMixer (non-interactive, non-custodial mixer)
- [x] ErgoAuctionHouse (peer-to-peer auctions)
- [x] SigmaFi (peer-to-peer loans via bonds)
- [x] Duckpools (lending pools)
- [x] ErgoRaffle (decentralized crowdfunding)
- [x] EXLE (uncollateralized lending)
- [x] SigmaO (trustless options)
- [x] HodlCoin (trustless ERG derivative with non-declining price)
- [x] AuctionCoin (emission via auctions)
- [x] Oracle Pools (federated transparent data providing)
- [x] Rosen Bridge (two-layered federated bridge)

These tools collectively contribute to the creation of more trustless collateral through various means such as AuctionCoin, OptionCoin, and fair initial mining offerings. As a result, Ergo's decentralized monetary base and derivative money supply continue to grow. It's worth noting that the entire DeFi ecosystem on Ergo is built upon its unique ErgoTree/ErgoScript contractual layer, also known as Sigma, which provides a secure and flexible foundation for the development of complex financial applications.

**Upcoming Milestones**
Looking ahead, key milestones include:

- [ ] The launch of new DeFi tools such as Paideia, Dexy/Gluon stablecoins, ChainCash, Analog Ergo, and OptionCoin
- [ ] Implementing sidechains with trustless transfers and various consensus mechanisms (merged mined with ERG, other blockchains, or double merged mined)
- [ ] Expanding Ergo's contractual layer to sidechains, incorporating features like Bulletproofs-based sigma protocols and elevating certain contracts to first-class citizens
- [ ] Experimenting with scalability solutions like sharding on sidechains
- [ ] Utilizing ERG and other tokens on Ergo and sidechains from launch, fostering a rich and diverse DeFi ecosystem
- [ ] Launching existing applications on sidechains, contingent on modifications to the contractual layer

By achieving these milestones, the Ergo Core Dev DAO aims to establish Ergo and its Sigma layer as a central hub for UTXO PoW blockchains with powerful smart contract capabilities.

**Monetization Strategies for ErgoDevs DAO**
To ensure the sustainability and growth of the Ergo ecosystem, the ErgoDevs DAO is exploring various monetization strategies, such as:

- [ ] Receiving a percentage of sidechain token emissions, similar to the Ergo Treasury contract
- [ ] Offering consultancy services and support for launching applications on sigma chains

These strategies will help fund ongoing development and foster a thriving community of developers and users around the Ergo platform, in collaboration with the Ergo Foundation and the wider Ergo community.
///






- (Nov 22) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226/4?u=glasgowm)
- (Dec 21) [Ergo protocol research and client development roadmap](https://www.reddit.com/r/ergonauts/comments/qfjhw4/ergo_protocol_research_and_client_development/)
- (Sep 21) [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629)
- (Jul 21) [Network congestion on Jul 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
- (May 20) [Protecting mempool from computationally heavy transactions](https://www.ergoforum.org/t/protecting-mempool-from-computationally-heavy-transactions/231)
- (May 20) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)

////


