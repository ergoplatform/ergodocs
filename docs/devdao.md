# Developer DAO

The Developer DAO (DevDAO) is a decentralized autonomous organization focused on research, development, and maintenance of the Ergo protocol and its associated infrastructure. The DevDAO aims to promote transparency, scalability, and community involvement in the core development efforts of the Ergo ecosystem.

/// admonition | This page is adapted from [ErgoDevs - R&D DAO for Ergo core on ergoforum](https://www.ergoforum.org/t/ergodevs-r-d-dao-for-ergo-core/4663) 
    type: info
///

## Motivation

Currently, the development of core repositories and infrastructure projects is not transparent enough and lacks scalability. Additionally, the promotion of the Ergo protocol, ErgoScript, and dApp development on Ergo is not being done effectively. The establishment of the DevDAO aims to address these issues by scaling core development and education efforts.

## Scope

The scope of the DevDAO includes:

- Research: Blockchain (PoW and PoW-based protocols, privacy-enhancing protocols, sidechains, optimistic and ZK verification of off-chain computations), and monetary (alternative monetary systems on the blockchain, stablecoins, mechanism design in tokenomics)
- Core development: Reference client implemented in Scala repositories (debox, scorex-util, scrypto, sigmastate-interpreter, ergo), and parts of the protocol implemented in Rust (sigma-rust)
- Infrastructure: Libraries and open-source wallets (AppKit, Fleet, Nautilus, ergo-wallet)
- Oracle pool framework
- ChainCash (as an assembler level for monetary innovations, such as local exchange trading systems)

## Vision

The DevDAO envisions Ergo as Digital Gold 2.0, a mineable digital commodity with trustless derivatives and expressive contracts. By building upon Ergo's robust DeFi ecosystem and introducing sidechains, the DevDAO aims to expand the decentralized monetary base and derivative money supply, creating a more inclusive and accessible financial system for the Ergo community and beyond.

## Completed Milestones

The Ergo platform, with the support of the Ergo Foundation and community developers, has already made significant strides in developing its infrastructure and DeFi ecosystem. This includes launching basic infrastructure such as wallets and explorers, as well as a wide range of DeFi tools and trustless derivatives, such as:

- SigmaUSD stablecoin (Djed protocol)
- Spectrum DEX (AMM-based)
- ErgoMixer (non-interactive, non-custodial mixer)
- ErgoAuctionHouse (peer-to-peer auctions)
- SigmaFi (peer-to-peer loans via bonds)
- Duckpools (lending pools)
- ErgoRaffle (decentralized crowdfunding)
- EXLE (uncollateralized lending)
- SigmaO (trustless options)
- HodlCoin (trustless ERG derivative with non-declining price)
- AuctionCoin (emission via auctions)
- Oracle Pools (federated transparent data providing)
- Rosen Bridge (two-layered federated bridge)

These tools collectively contribute to the creation of more trustless collateral through various means such as AuctionCoin, OptionCoin, and fair initial mining offerings. As a result, Ergo's decentralized monetary base and derivative money supply continue to grow. It's worth noting that the entire DeFi ecosystem on Ergo is built upon its unique ErgoTree/ErgoScript contractual layer, also known as Sigma, which provides a secure and flexible foundation for the development of complex financial applications.

## Upcoming Milestones

Looking ahead, key milestones include:

- The launch of new DeFi tools such as Paideia, Dexy/Gluon stablecoins, ChainCash, Analog Ergo, and OptionCoin
- Implementing sidechains with trustless transfers and various consensus mechanisms (merged mined with ERG, other blockchains, or double merged mined)
- Expanding Ergo's contractual layer to sidechains, incorporating features like Bulletproofs-based sigma protocols and elevating certain contracts to first-class citizens
- Experimenting with scalability solutions like sharding on sidechains
- Utilizing ERG and other tokens on Ergo and sidechains from launch, fostering a rich and diverse DeFi ecosystem
- Launching existing applications on sidechains, contingent on modifications to the contractual layer

By achieving these milestones, the DevDAO aims to establish Ergo and its Sigma layer as a central hub for UTXO PoW blockchains with powerful smart contract capabilities.

## Monetization Strategies

To ensure the sustainability and growth of the Ergo ecosystem, the DevDAO is exploring various monetization strategies, such as:

- Receiving a percentage of sidechain token emissions, similar to the Ergo Treasury contract
- Offering consultancy services and support for launching applications on sigma chains

These strategies will help fund ongoing development and foster a thriving community of developers and users around the Ergo platform, in collaboration with the Ergo Foundation and the wider Ergo community.

## Goals

- Organize discussions on research topics, EIPs, and workshops
- Find funding for bounties and salaries
- Maintain existing infrastructure, improve existing protocol-related code and libraries, and explorers
- Bring thousands of new developers into Ergo dApp development by creating and promoting tutorials and dApp examples
- Support the needs of dApps and wallets
- Help with auditing and testing dApps

## Committees

To track the achievement of the goals mentioned above, the DevDAO has several committees. Every DevDAO member may be a member of one or more committees:

- Research committee
- Scala core committee
- Rust core committee
- Infrastructure committee
- Education committee
- ChainCash and monetary innovations committee

## Funding Sources

- Ergo Foundation (EF)
- Projects on Ergo (e.g., Gold Cooperative is already sponsoring Oracle Pools and ChainCash development)
- Crypto funds

## Funding Mechanisms

- Bounties
- Sponsorship of part-time and full-time developers
- Grants

## Development Plan

### Q1 2024

- Research: Initial sidechain prototyping (no p2p, tests showing block generation, verification, and transfer for a sidechain having only cross-chain support features mentioned in the ErgoHack whitepaper)
- Node: RocksDB, UTXO set scanner, sub-block based blocks propagation EIP and basic entities
- Sigma: 6.0 planning and versioning code for serializers, new methods, new types
- Sigma-Rust: Planning further development (costing, 6.0 support)
- ChainCash: Tests for refund, contracts for custom tokens, another presentation
- Oracle pools: Planning further development, final audit of EIP, considering dev rewards in contracts
- AppKit: To be determined
- Other repos: Planning further development
- Education: To be determined

### Q2 2024

- Research: Design docs for concrete sidechains, plan for research in other fields, forming research group
- Node: The simplest sidechain with p2p support, subblocks based propagation in the testnet
- Oracle pools: EIP merging, releasing oracle pool version with dev rewards support, considering extensions (for delivering sport events, etc.)
- Sigma: 6.0 implementation
- Sigma-Rust: To be determined
- AppKit: To be determined
- Other repos: To be determined
- Education: To be determined

### Q3-Q4 2024

- Research: To be determined
- Node: Sub-blocks support in mining API and weak confirmations API, another p2p level audit, refactoring, tests for p2p layer
- Oracle pools: To be determined
- Sigma: 6.0 audit and tests, 6.0 activation, planning further development
- Sigma-Rust: To be determined
- AppKit: To be determined
- Other repos: To be determined
- Education: To be determined

Note: The areas marked as "To be determined" indicate that it is challenging to plan precisely how a direction will be shaped in a specific time period, as it depends on the contributions from the community, including you! With the establishment of the DevDAO, things should become more transparent and better planned.
