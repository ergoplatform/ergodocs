---
tags:
  - Roadmap
---

# Ergo Development Roadmap & History

Ergo is a blockchain platform designed to provide a secure, efficient, and user-friendly environment for the development of decentralized applications and financial tools. This roadmap outlines the key milestones and objectives for the development and growth of the Ergo ecosystem.


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



////
/// details | Who develops Ergo? 
    {type: info, open: false}
Ergo is developed a by a combination of the [Ergo Foundation](ergo-foundation.md), community developers and the recently launched [DevDAO](dev-dao.md)
///

## Core Development


### Node (Reference Client Protocol)

The Ergo node is the backbone of the network, and its ongoing development and optimization are crucial for ensuring a seamless user experience and maintaining the platform's security and performance. Key features and enhancements include:

- [x] Node V5 with JITC (Just-in-Time Costing)
- [x] Pruned Full Node & UTXO Set Snapshots
- [x] [Babel Fees](babel.md)
- [ ] P2P layer optimization
- [ ] Bootstrapping improvements
- [ ] Node V6 implementation
    - [ ] Composable Transactions
    - [ ] Zero-Knowledge Multi-Signature Setups
- [ ] [Sub-blocks](sub-blocks.md)
- [ ] Sidechain implementation modularization
- [ ] Potential RocksDb integration
- [ ] Signature re-checking optimization
- [ ] Enhanced testing for indices, scans, and wallet


### Sigma Language 

The Sigma language and its associated SDKs are crucial for enabling advanced cryptographic features and smart contracts on the Ergo platform. The development of Sigma 6.0, along with the implementation of JIT costing and other optimizations, will further enhance the capabilities and performance of Ergo's smart contract ecosystem.

- [x] Crypto contracts
- [x] Threshold Signatures
- [x] Sigma Protocols
- [x] AVL Trees
- [ ] [Sigma 6.0 implementation](https://github.com/ergoplatform/eips/blob/a24fc414abbc10e6ee59f878b280d9ecc725e10c/eip-0050.md) and validation context extension research
- [ ] Atomic Transactions
- [ ] ErgoScript 2.0
- [ ] [MerkleTrees](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/296)
- [ ] Revisiting formal verification implementation


#### SDKs

- [x] [AppKit](appkit.md)
- [x] [FleetSDK](fleet.md)
- [x] [sigma-rust](sigma-rust.md)
    - [ ] JIT costing implementation in Sigma-Rust
    - [ ] 6.0 features implementation in Sigma-Rust
    - [ ] Sigma-Rust-Mini development
- [x] Sigma.js
- [ ] Consideration of high-level language support (e.g., Lisp)

#### Libraries and Tooling

- [x] [ergo-lib-go](https://github.com/sigmaspace-io/ergo-lib-go)
- [x] [escript.online](https://escript.online)
    - [x] [Blockly Playground Integration](https://escript.online/blockly)
- [ ] Improvements to error-checking and debugging tools


### Scaling

- [x] Plasma Library on top of AVL Trees, drastically improving light client verification efficiency compared to traditional merkle tree data structures
- [ ] Layer 2 or sidechain offloading proposals, engineered with long-term scaling in mind and using advanced, well-researched tools
- [ ] "Know Your Assumptions" (KYA) introduction for offloading security
- [ ] Sigma Chains development
    - [ ] Implementing sidechains with trustless transfers and various consensus mechanisms (merged mined with ERG, other blockchains, or double merged mined)
    - [ ] Expanding Ergo's contractual layer to sidechains, incorporating features like Bulletproofs-based sigma protocols and elevating certain contracts to first-class citizens
    - [ ] Experimenting with scalability solutions like sharding on sidechains
    - [ ] Utilizing ERG and other tokens on Ergo and sidechains from launch, fostering a rich and diverse DeFi ecosystem
    - [ ] Launching existing applications on sidechains, contingent on modifications to the contractual layer

### Mining Infrastructure

- [ ] Lithos decentralized mining pool infrastructure expected launch by end of 2024
- [ ] Plans for reintroduction of Fair Initial Mining Offerings (FIMOs)

### EIPs

Ergo Improvement Proposals (EIPs) are a set of guidelines and standards designed for the continuous improvement of Ergo. These proposals encompass a wide range of aspects, including but not limited to, core protocol specifications, client APIs, dApp/contract standards, and more.

Here are some of the EIPs that have been proposed and implemented:

- [x] [EIP-0001: UTXO-Set Scanning Wallet API](eip1.md): This EIP focuses on extending the wallet to serve the needs of external applications by providing a flexible scanning interface.
- [x] [EIP-0020: ErgoPay](eip20.md): An interaction protocol between wallet application and dApp for creating, signing and sending Ergo transactions.
- [x] [EIP-0037: Tweaking Difficulty Adjustment Algorithm](eip37.md): This EIP proposes changes to make the current difficulty readjustment more reactive and smoother.
- [x] [EIP-0027: Emission Retargeting Soft-Fork](eip27.md): This EIP proposes an amendment to the emission schedule to ensure the long-term sustainability of the mining protocol.

To gain a better understanding of the structure and formatting of EIPs, we encourage you to review the existing EIPs on [GitHub](https://github.com/ergoplatform/eips) or within [this documentation](https://docs.ergoplatform.com/tags/#eip). This will provide you with a clear picture of the expectations and standards associated with EIPs.

#### Open EIPs

See the [Pull requests](https://github.com/ergoplatform/eips/pulls) section for full details on the open EIPs, some of the most notable are;

- [ ] [Ready to merge/implemented PRs #86](https://github.com/ergoplatform/eips/issues/86)
- [ ] EIP-0042 Multi-Signature Wallet
- [ ] [[WIP] EIP-50 - Sigma 6.0](https://github.com/ergoplatform/eips/pull/100)

### Governance

- Ongoing work to define rules for new releases and research-driven development frameworks
- Encouragement of new stakeholder organizations within the Ergo ecosystem

### Wallets

- [x] Nautilus 
    - [x] Manifest v3 rework
- [ ] Light SPV Clients using NiPoPoWs
- [ ] EIP-12 / EIP-20




## DeFi Ecosystem

Each addition to our budding ecosystem helps to create even more trustless collaterral and expands the decentralised monetary base and deriviative money supply. 

- [ ] The launch of new DeFi tools such as Paideia, Dexy/Gluon stablecoins, ChainCash, Analog Ergo, and OptionCoin

### Decentralized Exchanges 

- [x] Spectrum DEX (AMM-based)
- [x] Trade House
- [x] Crystal Pool
- [ ] [Machina Finance](machina.md) (grid DEX)
- [ ] [PalmyraComDex](palmyra.md) (commodities DEX)

###  Stablecoins

- [x] SigmaUSD stablecoin (Djed protocol)
- [ ] [Gluon](gluon.md) (stablecoin)
- [ ] [DexyGold](dexy.md) (stablecoin)

### Lending and Borrowing
- [x] [SigmaFi](sigmafi.md) (peer-to-peer loans via bonds)
- [x] [Duckpools](duckpools.md) (lending pools)
- [x] [EXLE](exle.md) (uncollateralized lending)
- [ ] Yield Farming on Spectrum

### Derivatives and Synthetics
- [x] [SigmaO](sigmao.md) (trustless options)
- [x] [HodlCoin](hodlcoin.md) (trustless ERG derivative with non-declining price)
- [ ] OptionCoin
- [ ] [ChainCash](chaincash.md) (elastic money creation based on assets and trust)

### Crowdfunding and Auctions
- [x] [ErgoRaffle](raffle.md) (decentralized crowdfunding)
    - [ ] v2
- [x] [ErgoAuctionHouse](ergoauctions.md) (peer-to-peer auctions)
- [x] [AuctionCoin](auctioncoin.md) (emission via auctions)

### Interoperability and Bridges

- [x] [Rosen Bridge](rosen.md) (two-layered federated bridge)
    - [x] ADA Bridge
    - [ ] BTC Bridge
        - [ ] Runes Integration
    - [ ] EVM Bridge
- [ ] [Analog Ergo](analog-ergo.md) (atomic swaps)
- [x] [Oracle Pools](oracle.md) (federated transparent data providing)
- [ ] Trustless Relays


### Privacy and Mixing
- [x] ErgoMixer (non-interactive, non-custodial mixer)
    - [x] Stealth addresses
- [ ] [SigmaJoin](sigmajoin.md)
- [ ] Privacy-Preserving Voting

### DAOs and Governance

- [x] Paideia (DAO toolkit)
- [ ] [Lithos](lithos.md) (decentralized mining infrastructure)

### Misc

- [x] [GuapSwap](guapswap.md) (miner token swapping)


### Gaming and Metaverse
- [x] BlitzTCG (trading card game)
- [x] CyberVerse (metaverse gaming platform)




## References


//// details | Ergo Foundation History
    {type: tip, open: true}

/// details | 2020
    {type: success, open: false}
- Introduced the Ergo Foundation, a community-driven entity.
- Released roadmap and started Discord.
- Partnered with Emurgo, bringing extensive joint research on Oracle Pools, SigmaUSD, and the headless dApp framework.
- Listed on CoinEx and Gate.io.
///
/// details | 2021
    {type: success, open: false}
- Strengthened the Ergo Foundation with new members and advisors
- Incorporated the first legal entity in Singapore to meet formal arrangements required in the industry
- Achieved key milestones:
  - Autolykos v2 Hard-Fork, opening Ergo to mining pools and improving liquidity
  - Partnerships and marketing efforts in China, growing the community to >10k members
  - Listings on KuCoin and Changelly
  - Formation of the UTXO Alliance
  - Initiation of EIP-27 discussions
  - Hiring of wallet developers to address users' lack of usable wallet options
  - Obtained a US Legal Opinion determining Ergo is unlikely to be classified as a security
  - Organized first summits and two hackathons

///
/// details | 2022
    {type: success, open: false}

- Expanded the Ergo Foundation with new officers to engage the wider community
- Created a pitch deck highlighting the rapidly developing 'open source economy' on Ergo
- Achieved key milestones:
  - Listings on Indodax, Huobi, and Bittrue
  - Parallel asset launches on Flux
  - [EIP-27](eip27.md) re-emission soft-fork and [EIP-37](eip37.md) difficulty retargeting hard fork
  - Two summits and three hackathons with 45 entries
  - Redesign and relaunch of [ergoplatform.org](https://ergoplatform.org) and [sigmaverse.io](https://sigmaverse.io)
  - Release of Node [V5 JITC](jitc.md)
///
/// details | 2023
    {type: success, open: false}
- Significant donations to EF Treasury from ecosystem projects and activation of storage rent
- New partnerships and listings, including Bitpanda, nonkyc.io, Koinly, and StealthEx
- Organized [Ergo Summit 2023](https://ergoplatform.org/en/news/Ergo-Summit-2023), ErgoVersary 2023, and Ergohack VI and VII
- Core developments: Sigma.js, UTXO Set Snapshots, bootstrapping with NiPoPoWs, work on SigmaState
- Scaling updates from kushti and work on a [sub-block confirmation protocol](https://ergoplatform.org/en/blog/Ergo's-Newest-Advancement-Sub-Blocks)
- New tooling: FleetSDK, [Ledger in developer mode](https://ergoplatform.org/en/blog/Ledger-Launches-Ergo-Support-in-Developer-Mode), Oracles v2
- Thriving ecosystem with numerous projects launched, including [Rosen Lite](https://ergoplatform.org/en/news/Rosen-Bridge-Officially-Launches-on-Ergo-Mainnet/), [SigmaFi](https://ergoplatform.org/en/blog/Sigma-Finance-A-Peer-to-Peer-Bond-Protocol), [Duckpools](https://ergoplatform.org/en/blog/Duckpools-A-Lending-and-Borrowing-Protocol-on-Ergo), and many more
- Pruned Full Node is [now live](pruned-full-node.md)
- Plasma
///
////



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



<!--
#### DevDAO Core Development for Q1/Q2 2024 

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


#### Tooling


- (TBD) Development of [SPV Client](spv.md)
- [Sigma Chains](sigma-chains.md) 

### Application Layer

- EVM and BTC Bridge for [Rosen](rosen.md)
- 
- [DexyGold](dexy.md) 
- [Machina Finance](machina-finance.md)
- [ChainCash](chaincash.md)
- [PalmyraComDex](palmyra.md)
- [BlitzTCG](blitz.md)
- [Paideia](paideia.md)
- 
- 
- 
-->

- (Nov 22) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226/4?u=glasgowm)
- (Dec 21) [Ergo protocol research and client development roadmap](https://www.reddit.com/r/ergonauts/comments/qfjhw4/ergo_protocol_research_and_client_development/)
- (Sep 21) [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629)
- (Jul 21) [Network congestion on Jul 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
- (May 20) [Protecting mempool from computationally heavy transactions](https://www.ergoforum.org/t/protecting-mempool-from-computationally-heavy-transactions/231)
- (May 20) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)

////


