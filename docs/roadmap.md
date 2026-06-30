---
tags:
  - Roadmap
owner: docs
last_reviewed: 2026-06-30
source_repos:
  - repo: ergoplatform/eips
    branch: master
    paths:
      - eip-0044.md
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/devnet.conf
      - src/main/resources/mainnet.conf
      - src/main/scala/org/ergoplatform/nodeView
  - repo: ScorexFoundation/sigmastate-interpreter
    branch: develop
    paths:
      - docs
      - interpreter
      - data
  - repo: ergoplatform/sigma-rust
    branch: develop
    paths:
      - ergo-lib
      - ergotree-interpreter
      - ergoscript-compiler
      - bindings
  - repo: ergoplatform/ergo-appkit
    branch: develop
    paths:
      - README.md
      - appkit/src
  - repo: mwaddip/ergo-node-rust
    branch: master
    paths:
      - README.md
  - repo: mwaddip/santa
    branch: main
    paths:
      - README.md
  - repo: mwaddip/santa-blitzen
    branch: master
    paths:
      - README.md
  - repo: mwaddip/santa-vixen
    branch: master
    paths:
      - README.md
  - repo: mwaddip/santa-donner
    branch: main
    paths:
      - README.md
  - repo: arkadianet/ergo
    branch: main
    paths:
      - README.md
  - repo: mwaddip/ergots
    branch: master
    paths:
      - README.md
      - packages/scorex/package.json
      - packages/nipopow/package.json
      - packages/avltree/package.json
      - packages/ergoscript
      - packages/transaction/package.json
  - repo: odiseusme/matrix-pulse
    branch: master
    paths:
      - README.md
  - repo: decentbob/ergo-marketplace
    branch: main
    paths:
      - README.md
      - VISION.md
      - DESIGN.md
  - repo: Lithos-Protocol/Lithos-Client
    branch: master
    paths:
      - README.md
      - TestnetNode.md
  - repo: rosen-bridge/watcher
    branch: master
    paths:
      - README.md
  - repo: rosen-bridge/guard-service
    branch: master
    paths:
      - README.md
  - repo: ChainCashLabs/chaincash
    branch: master
    paths:
      - contracts
      - docs/server.md
      - docs/whitepaper/chaincash.pdf
  - repo: StabilityNexus/Gluon-Ergo-UI
    branch: main
    paths:
      - README.md
  - repo: machinafi/sdk
    branch: master
    paths:
      - README.md
      - src
  - repo: cannonQ/ergo-p2p-options-frontend
    branch: master
    paths:
      - README.md
      - packages/core
      - packages/web
source_of_truth:
  - https://github.com/ergoplatform/eips/tree/master/eip-0044.md
  - https://github.com/ergoplatform/ergo/releases
  - https://github.com/ScorexFoundation/sigmastate-interpreter/releases
  - https://github.com/ergoplatform/sigma-rust
  - https://github.com/ergoplatform/ergo-appkit/releases/tag/v6.0.0
  - https://github.com/mwaddip/ergo-node-rust/releases
  - https://github.com/mwaddip/santa
  - https://github.com/mwaddip/santa-blitzen
  - https://github.com/mwaddip/santa-vixen
  - https://github.com/mwaddip/santa-donner
  - https://github.com/arkadianet/ergo
  - https://github.com/mwaddip/ergots
  - https://github.com/odiseusme/matrix-pulse
  - https://github.com/decentbob/ergo-marketplace
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test
  - https://github.com/rosen-bridge
  - https://github.com/ChainCashLabs/chaincash
  - https://github.com/StabilityNexus/Gluon-Ergo-UI
  - https://github.com/machinafi/sdk/releases/tag/0.1.0-alpha.0
  - https://github.com/cannonQ/ergo-p2p-options-frontend
  - https://ebiome.cc
  - https://github.com/cannonQ/ergo-mempool-watcher
  - https://github.com/ergonames/ergonames-services/blob/master/sdk/INTEGRATION.md
---

# Ergo Development Roadmap & History

This page tracks major Ergo development history and active work as of **June 30, 2026**. It is not a promise of delivery dates. Public repositories, release notes, EIPs, and project pages are the source of truth.

Ergo's roadmap is research-led: protocol changes move through papers, EIPs, testnets, client releases, and community review before mainnet activation. Ecosystem projects move at different speeds, so items below are grouped as **completed**, **active**, or **experimental** rather than presented as a single linear release plan.

## How To Read This Page

| Status | Meaning |
| --- | --- |
| **Live** | Available to normal users or operators, with caveats documented on the project page. |
| **Released** | Published upstream release or merged implementation, but not necessarily activated everywhere. |
| **Testnet / RC** | Public testnet, release candidate, or special devnet build. Do not treat as mainnet production. |
| **Alpha / prototype** | Public code or UI exists, but contracts, UX, audits, or wallet support may still change. |
| **Research** | Design, paper, EIP, or exploratory implementation. Delivery depends on review and testing. |

## Development Focus

Near-term protocol work is focused on the 6.x reference-node and Sigma stack, with Matrix DevNet used for protocol-breaking changes before any mainnet proposal. Rust and TypeScript implementations now provide useful cross-checks alongside the JVM reference stack.

On the application side, Rosen Bridge, wallets, explorers, mining tools, and DeFi applications are maintained by independent teams. Experimental work such as Lithos, ChainCash/Basis, Machina, Etcha, Degens.World tooling, and agent/wallet applications is tracked separately from production-ready infrastructure. EF, treasury, votes, Sigmanauts, DevDAO, and community-team responsibilities are covered as governance context rather than protocol status.

## Pipeline Overview

This is the clearest short-form view of what is in the pipeline. Items are grouped by maturity, not promised delivery order.

| Stage | Work in view | What it means |
| --- | --- | --- |
| In flight | 6.0.x node maintenance, Sigma SDK 6.0.x, AppKit 6.0, mempool/synchronisation fixes, extension-section validation, wallet and dApp compatibility work | Keep the current production stack stable while downstream tools move onto the 6.x line. |
| In flight | Rosen Bridge operations and chain/service maintenance | Maintain live bridge paths while watcher, guard, service, SDK, cleanup, and chain-specific components continue evolving. |
| In flight | Spectrum, SigmaUSD, Dexy, Gluon, SigmaFi, Duckpools, Oracle Pools, Paideia, wallets, explorers, [eBiome](ebiome.md), and ecosystem utilities | Keep established application and data infrastructure usable while individual projects continue at different maintenance levels. |
| Testnet / validation | Matrix DevNet / 6.5.x, [Lithos](lithos.md), [Rust node](rust-node.md), SANTA, `sigma-rust`, [ergots](ergots.md), [Matrix Pulse](matrix-pulse.md) | Test protocol-breaking changes, mining decentralization, independent implementation behavior, and Matrix observability before any production claims. |
| Alpha / prototype | [ChainCash](chaincash.md) / Basis, [Machina Finance](machina-finance.md), [Etcha](etcha.md), Degens.World tooling, [Ergo Marketplace](ergo-marketplace.md), Palmyra, Crystal Pool, Mew Finance, agent-wallet flows | Build application-layer experiments on Ergo while contracts, wallet support, UX, and risk assumptions are still changing. |
| Research / standards | [Sub-blocks](subblocks.md), Sigma Chains / sidechains, NiPoPoW bootstrapping, pruned/light operation, EIP-44, EIP-46, EIP-47, Bulletproof-related work | Keep protocol and standards work moving through papers, EIPs, implementation review, and test environments. |
| Public beta / ecosystem services | [ErgoNames](ergonames.md), Reputation System, The Field, FIMOs, privacy-preserving voting, SigmaJoin, trustless relays, and advanced wallet/signing flows | Track identity, coordination, privacy, and miner-facing services as they move from beta or research into durable infrastructure. |
| Governance / operations | EF future handover, treasury/vote reporting, Sigmanauts responsibilities, DevDAO-funded work, docs/source-watch maintenance | Make ecosystem responsibilities and funding trails easier to inspect as work becomes less Foundation-centered. |

| Track | Near-term watch points |
| --- | --- |
| Protocol | 6.0.x release notes, Matrix DevNet evidence, activation settings, and concrete mainnet proposals. |
| SDKs and tooling | AppKit 6 adoption, Sigma SDK releases, `sigma-rust` parity notes, `ergots` package stability, SANTA vectors and runners. |
| Scaling and mining | Lithos mainnet-readiness notes, Stratum/miner docs, sub-block test evidence, light/pruned-node operator guidance. |
| Interoperability | Rosen chain status, Runes-related work, Firo/Handshake/Monero-related bridge work, Bridge Expansion Kit and SDK releases. |
| Applications | ChainCash/Basis signing support, Machina and Etcha audit/production status, Palmyra/Crystal/Mew status, wallet-native flows, agent app safety notes. |
| Ecosystem services | Oracle Pools / Oracles v2 status, Paideia activity, ErgoNames beta/genesis and SDK status, Reputation System, Matrix Pulse, eBiome, The Field, and miner-facing utility updates. |
| Governance | EF treasury updates, EF votes, Sigmanauts handovers, DevDAO deliverables, and docs review issues. |

## Current Snapshot

| Area | Status |
| --- | --- |
| Reference node | **Released / testnet**: mainnet 6.0.x line is active; 6.1.x and 6.5.0 Matrix DevNet builds are used for testing newer work. |
| Sigma / ErgoScript | **Released**: Sigma SDK 6.0.x has shipped, with 6.0.5 released in June 2026. |
| AppKit | **Released**: AppKit 6.0.0 was released in June 2026 on top of SigmaSDK 6.0.x. |
| Rust / TypeScript stack | **Active implementation research**: `sigma-rust`, `mwaddip/ergo-node-rust`, `arkadianet/ergo`, `ergots`, and SANTA runners are differential-testing surfaces, not replacements for the JVM consensus authority unless upstream marks a path stable. |
| Scaling | **Research / testnet**: sub-blocks, sidechains, NiPoPoW bootstrapping, pruned operation, and devnet testing remain active tracks. |
| Interoperability | **Live + expanding**: Rosen Bridge is live across Ergo, Cardano, BTC, EVM/BSC, and DOGE, with more chain work and Runes-related support in progress. |
| Mining decentralization | **Testnet**: Lithos has moved through multiple 2026 testnet releases, reaching `v4.2.0-test`. |
| DeFi and monetary systems | **Mixed**: Spectrum, SigmaUSD, Dexy, Gluon Gold, SigmaFi, Duckpools, Machina, Etcha, ChainCash/Basis, Ergo Marketplace, and related tools cover live, alpha, and prototype stages. |
| Data and observability | **Active tooling**: eBiome, Matrix Pulse, Ergo Mempool Watcher, explorers, and knowledge-base tooling expand monitoring, analytics, forensics, and project-context surfaces. |
| Governance and funding | **Decentralizing**: the Ergo Foundation has narrowed its role; [Sigmanauts](sigmanauts.md) and independent teams now manage more ecosystem functions. See [Ergo Foundation Treasury](ef-treasury.md), [EF Votes](ef-votes.md), and [EF Future](ef-future.md). |

## Ecosystem Map

Ergo's ecosystem includes active applications, research prototypes, legacy projects, and low-activity experiments. A project appearing here is part of the roadmap/timeline record; it is not a recommendation or audit statement.

| Area | Covered items |
| --- | --- |
| DEXs, swaps, and markets | [Spectrum / ErgoDex / ErgoDEX](spectrum.md), [ErgoAuctionHouse](ergo-auctions.md), Trade House, [SkyHarbor](skyharbor.md), [Single Transaction Swap](single-tx-swap.md), [TokenJay](token-jay.md), Crooks Finance, [Palmyra ComDEX](palmyra.md), [Crystal Pool](crystal-pool.md), [Machina Finance](machina-finance.md), [Mew Finance](mew-finance.md), [Ergo Marketplace](ergo-marketplace.md), [Hodlcoin](hodlcoin.md) / Phoenix Finance, [Lilium](lilium.md), [Hodlbox](hodlbox.md), and [AuctionCoin](auction-coin.md). |
| Stablecoins and monetary systems | [SigmaUSD](sigmausd.md), SigmaUSD v2 research, [Dexy / DexyGold](dexy.md), [Gluon](gluon.md), [ChainCash](chaincash.md), Basis, [OptionCoin](optioncoin.md), [AuctionCoin](auction-coin.md), [HodlCoin](hodlcoin.md), and [Analog Ergo](analog-ergo.md). |
| Lending, options, and derivatives | [SigmaFi](sigmafi.md), [Duckpools](duckpools.md), [optionPools](optionPools.md), [EXLE](exle.md), [SigmaO](sigmao.md), [Etcha](etcha.md), [Machina Finance](machina-finance.md), [OptionCoin](optioncoin.md), and [Moria Finance](moria-finance.md). |
| Games, NFTs, and crowdfunding | [BlitzTCG](blitz.md), [CyberVerse](cyberverse.md), [ErgoRaffle](ergoraffle.md), [Auction House](ergo-auctions.md), [SkyHarbor](skyharbor.md), [Lilium](lilium.md), [Night Owl](nightowl.md), and related historical NFT/game experiments. |
| Bridges, oracles, and sidechains | [Oracle Pools](oracle.md), [Oracles v2](oracles-v2.md), [Rosen Bridge](rosen.md), ADA Bridge, BTC Bridge, EVM Bridge, DOGE Bridge, BCH Bridge, Runes Integration, R&D for Monero, RosenFast Service, Bridge Expansion Kit, Bridge SDK, Hummingbot Integration / Customisation, [Sigma Chains](sigma-chains.md), Trustless Relays, sidechains, and Flux parallel assets. |
| Privacy | [ErgoMixer](ergomixer.md), [Stealth addresses](stealth-address.md), [SigmaJoin](sigmajoin.md), Privacy-Preserving Voting, and mix-related wallet integration work. |
| Governance, mining, and community infra | [Paideia](paideia.md), [Lithos](lithos.md), [The Field](the-field.md), [Sigmanauts](sigmanauts.md) Mining Pool, storage-rent pool integration, Fair Initial Mining Offering research, [GuapSwap](guapswap.md), and [CYTI](cyti.md). |
| Tools, data, and identity | [Moria Finance](moria-finance.md), Trustless Relays, [Random Number Generator](sigmarand.md), [TabbyPOS](tabbypos.md), [Crux Finance](crux.md), [ErgoNames](ergonames.md) public beta and SDK integration work, [Reputation System](reputation-system.md), [Matrix Pulse](matrix-pulse.md), [eBiome](ebiome.md), [Ergomempool Visualizer / Watcher](mempool-vis.md), [Ergo Knowledge Base](ergo-knowledge-base.md), ergexplorer, sigmaspace, [TokenJay](token-jay.md), and ecosystem dashboards. |
| Wallets and UX | [Nautilus](nautilus.md), [Minotaur](minotaur.md), [Satergo](satergo.md), [SAFEW](safew.md), [Ledger](ledger.md) developer-mode support, Keystone integration, [EIP-12](eip12-types.md) / [EIP-20](eip20.md) connector work, [ErgoPay](ergo-pay.md), Metamask/TrustWallet exploration, and NiPoPoW-based light client work. |

## Timeline Index

These timeline items matter for continuity. Treat them as current work only when they also appear in the current snapshot, pipeline overview, or detailed roadmap tracks.

| Area | Historical items covered |
| --- | --- |
| Listings, partners, and ecosystem organizations | CoinEx, Gate.io, Jinse, KuCoin, Changelly, Indodax, Huobi, Bittrue, MEXC, Emurgo research, headless dApp framework work, UTXO Alliance, [Sigmanauts](sigmanauts.md), [Erg0ne](ergone.md), Market-Making handover, `ergoplatform.org`, and `sigmaverse.io`. |
| Protocol history | Autolykos v2, [EIP-27](eip27.md), [EIP-37](eip37.md), [JITC](jitc.md), RocksDB migration, UTXO Set Snapshots, [Pruned Full Node](pruned-full-node.md), [Light SPV Clients](light-spv-node.md), [storage rent](storage-rent.md), [sub-blocks](subblocks.md), [soft-fork rules](soft-fork.md), zero-knowledge treasury experiments, [extension-section](extension-section.md), [Merkle-tree](merkle-tree-overview.md), and Merkle trees documentation. |
| Sigma and standards | SigmaState, Sigma.js, Sigma 5.0.14, [Sigma 6.0.0](sigma-6.md), `6.0.0-alpha1`, `Global.some`, AVL+ Tree work, EIP-44 arbitrary data signing, EIP-0046 Atomic Chains, EIP-0047 Pooled Transaction Inputs, [Bulletproofs](pattern-bulletproof-range-proof.md), Sigma-Rust-Mini, and ErgoScript compilation / debugging material. |
| SDKs and tooling | [AppKit](appkit.md), [FleetSDK](fleet.md), [sigma-rust](sigma-rust.md), [Sigma.js](sigmajs.md), [Plasma Library](plasma.md), `ergo-lib-go`, `uExplorer`, [escript.online](ergoscript-tooling.md), Blockly playground work, [Merkle-tree docs](merkle-tree-overview.md), [extension-section docs](extension-section.md), and historical explorer/indexer work. |
| Events and applications | [Ergo Summit](ergosummit.md), [ErgoHack](ergohack.md), [Off-The-Grid](off_the_grid.md), Rosen Lite, PhoenixFinance, [Celaut](celaut.md), [Bene](bene.md), [Sigmaspace](https://sigmaspace.io/), [eBiome](ebiome.md), Storage rent dashboard work, and 2024 NFT / DeFi / UX milestones. |
| Wallet milestones | Nautilus Manifest v3 and Abyss work, Minotaur 2.0.1, Satergo performance work, [Ledger](ledger.md) developer-mode support, Keystone integration, [EIP-12](eip12-types.md) / [EIP-20](eip20.md) connector work, Metamask exploration, Trustwallet exploration, and light-client wallet research. |
| Mining and issuance | [Sigmanauts](sigmanauts.md) Mining Pool, storage-rent pool integration, Lithos mining-pool research, Fair Initial Mining Offering (FIMO) research, and miner-facing token tooling. |

## Recent History

### 2026: Protocol, DevNet, and Application Tooling

- [x] [AppKit v6.0.0](https://github.com/ergoplatform/ergo-appkit/releases/tag/v6.0.0) released on top of SigmaSDK 6.0.x, including EIP-50 / Sigma 6.0 alignment work and prover-evaluated tests.
- [x] [Sigma SDK v6.0.5](https://github.com/ergoplatform/sigmastate-interpreter/releases/tag/v6.0.5) released after the 6.0.0 through 6.0.4 releases, adding regression coverage and serialization/deserialization hardening.
- [x] Ergo node releases moved through `v6.0.2`, `v6.0.2.1`, `v6.0.2.2`, `v6.0.3RC1`, [v6.0.3](https://github.com/ergoplatform/ergo/releases/tag/v6.0.3), and [v6.1.3](https://github.com/ergoplatform/ergo/releases/tag/v6.1.3); [Ergo Matrix 6.5.0 RC1](https://github.com/ergoplatform/ergo/releases/tag/v6.5.0-RC1) added a special DevNet build for protocol-breaking change testing.
- [x] Node protocol work improved mempool consistency, extension-section validation, missing-parent header handling, and SyncInfoV2 continuation-header handling. See [Ergo Node Protocol](protocol.md) and [Synchronisation](synchronisation.md).
- [x] [Lithos](lithos.md) moved through `v3.0.0-test`, `v3.1.0-test`, `v4.0.0-test`, `v4.1.0-test`, and [`v4.2.0-test`](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test), with work on mempool tracking, Stratum behavior, transaction scheduling, and rollup evaluation.
- [x] [ChainCash](chaincash.md) and Basis advanced through reserve-contract rework, note redemption, server/API work, and presentation material for 2026 research events.
- [x] [Gluon Gold](gluon.md) is live at [gluon.gold](https://gluon.gold/) with a public Ergo UI repository.
- [x] [Machina Finance](machina-finance.md) published an alpha orders SDK with grid and limit-order transaction builders.
- [x] [Etcha](etcha.md) entered alpha for peer-to-peer options with physical-delivery and cash-settled flows.
- [x] [Degen Wallet](degens-world.md), Degens.World agent tooling, Ergo MCP, Xergon, and related experimental apps expanded the wallet/agent surface.
- [x] [Rust node](rust-node.md) releases reached the 0.7.x line, including v0.7.4's mining-serve state-root fix, while SANTA added shared conformance vectors/runners for `sigma-rust`, `arkadianet/ergo`, and `mwaddip/ergo-node-rust`.
- [x] [ergots](ergots.md) published browser-compatible TypeScript packages for Scorex codecs, NiPoPoW, AVL+, ErgoScript, and transaction tooling, with current package metadata tracked in docs.
- [x] [Matrix Pulse](matrix-pulse.md) was published as lightweight Matrix input-block observability tooling for local Matrix nodes.
- [x] [eBiome](ebiome.md) launched as a live ecosystem analytics, explorer, and forensics dashboard; its forensics views are heuristic and should not be treated as deterministic attribution.
- [x] [Ergo Marketplace](ergo-marketplace.md) was published as an early design/prototype for permissionless trade infrastructure.
- [x] [ErgoNames](ergonames.md) returned to public beta and published SDK integration guidance for wallet and dApp send flows.
- [x] [ergo-use-x402](ergo-use-x402.md) demonstrated x402 / Agentic Commerce Protocol payment flows for USE on Ergo using Babel fees.
- [x] [Ergo Mempool Watcher](mempool-vis.md) added a public dashboard for local-node mempool inclusion and dwell-time analysis.
- [x] Docs automation gained Source Watch, Discord Dev Digest, and weekly review issue tooling. See [Contribute Automation](automation.md).

The emphasis in 2026 is validation and application work on top of the 6.x stack, while newer implementations continue to prove compatibility before any production claims.

### 2025: 6.0 Line, Rust Parity, and Ecosystem Rebuild

- [x] Sigma SDK 6.0.0, 6.0.1, and 6.0.2 shipped for the 6.x feature line.
- [x] Ergo node 6.0.1 and 6.1.0 releases moved the reference client into the 6.x era.
- [x] Rust and TypeScript implementation work accelerated: `sigma-rust`, `ergots`, and Rust node sync/testing exposed edge cases in costing, serialization, and validation behavior.
- [x] ChainCash/Basis moved from concept toward active contract/server prototypes.
- [x] Rosen Bridge continued chain and service expansion after its earlier mainnet launch.
- [x] EF voting shifted toward focused treasury-control decisions, including on-ramp proposals, ERGOHACK X funding, and operational salary adjustments. See [EF Votes](ef-votes.md).

### 2024: Governance Shift and 6.0 Preparation

- [x] ErgoHack VIII focused on Ergo as a smart layer.
- [x] DevDAO and post-EF development coordination became a more explicit part of the roadmap. See [DevDAO](devdao.md).
- [x] [Sigmanauts](sigmanauts.md) expanded ecosystem responsibilities, including mining pool work and market-making fund management.
- [x] Reference-client work included RocksDB integration, 6.0 alpha work, P2P/bootstrapping review, and sub-block research.
- [x] Sigma 5.0.14 shipped, while Sigma 6.0 implementation work continued.
- [x] Wallet and dApp UX improved across Nautilus, Minotaur, Satergo, and other community wallets.
- [x] Rosen Bridge, Sigmaspace, storage-rent dashboards, explorer/indexer work, and DeFi tooling continued to mature.

## Detailed Roadmap Tracks

### Protocol and Reference Client

| Track | Current state | Watch next |
| --- | --- | --- |
| 6.0.x mainnet line | Active release line for the current interpreter feature set. | Mainnet release notes, activation settings, and any 6.0.x follow-up RCs. |
| Matrix DevNet / 6.5.x | Special devnet build for protocol-breaking change testing. | Devnet config changes, voting settings, and operator instructions. |
| Mempool and synchronisation | Recent work improved consistency checks, missing-parent handling, and SyncInfoV2 handling. | More 6.0.3+ release notes and node protocol PRs. |
| [Sub-blocks](subblocks.md) | Still research / implementation review, not a live mainnet feature. | Extracted PRs, devnet tests, and updated protocol assumptions. |
| Sidechains / Sigma Chains | Research and prototypes continue. | Braid/Sigma Chains docs, trust assumptions, and concrete bridge/relay code. |

### Sigma, SDKs, and Cross-Implementation Testing

| Track | Current state | Watch next |
| --- | --- | --- |
| Sigma SDK | 6.0.x released through 6.0.5. | New SDK releases, EIP-50 finalization, and compatibility notes. |
| AppKit | 6.0.0 released on SigmaSDK 6.0.x. | Downstream library updates and examples that adopt AppKit 6. |
| [sigma-rust](sigma-rust.md) | Compiler/interpreter parity work and bindings continue. | Consensus-sensitive parity claims, JIT costing, and binding releases. |
| [ergots](ergots.md) | TypeScript verification and ErgoScript tooling is active, with published packages for Scorex, NiPoPoW, AVL+, ErgoScript, and transactions. | Package stability, JVM-alignment notes, and evaluator coverage. |
| [Rust Node](rust-node.md) / SANTA | Rust node reached 0.7.x releases; SANTA supplies conformance vectors/runners for sigma-rust, arkadianet/ergo, and mwaddip/ergo-node-rust. | Cross-implementation divergences, new vector tiers, and production-readiness statements. |

### Scaling and Mining

| Track | Current state | Watch next |
| --- | --- | --- |
| [Storage rent](storage-rent.md) and pruning | Live economic/state-management primitives. | Operator guidance, explorer support, and wallet UX. |
| NiPoPoWs / light clients | Core design primitive, with bootstrapping and proof-serving work continuing. | Node, Rust, and SDK support for practical light-client flows. |
| [Lithos](lithos.md) | Testnet client releases reached `v4.2.0-test`. | Mainnet-readiness notes, Stratum/miner docs, collateral flows, and risk disclosures. |
| Sub-blocks / Layer 2 | Research and development track. | Devnet evidence and clear security assumptions. |
| Matrix observability | [Matrix Pulse](matrix-pulse.md) provides local Matrix input-block monitoring for arrivals, applies, queues, forks, and status headers. | Maintained releases, operator docs, and whether Matrix tooling becomes part of standard devnet observability. |
| FIMOs and miner utilities | Fair Initial Mining Offering concepts and miner tooling remain ecosystem-level research / utility work. | Concrete contracts, mining-pool support, and user-facing risk documentation. |

### Interoperability

| Track | Current state | Watch next |
| --- | --- | --- |
| [Rosen Bridge](rosen.md) live chains | Ergo, Cardano, BTC, ETH/EVM/BSC, and DOGE paths are documented as live. | Chain-specific status, confirmation rules, fees, and token-map changes. |
| Rosen infrastructure | Watcher, guard-service, UI/service, SDK, cleanup-service, and network-client repos are active. | Release notes for watcher, guard-service, UI/service, and SDK packages. |
| New chains | Runes, Firo, Handshake, Monero PoC, and Bridge Expansion Kit work are in progress or under review. | Merged extractors/scanners, service releases, and public operator docs. |
| Oracles and data feeds | Oracle Pools are live historical infrastructure; Oracles v2 remains relevant for data-provider and ballot-token design. | Active oracle-core changes, pool bootstrapping docs, and live feed/operator status. |

### DeFi, Monetary Systems, and dApps

| Status | Projects |
| --- | --- |
| Live / user-facing | [Spectrum](spectrum.md), [SigmaUSD](sigmausd.md), [Dexy](dexy.md), [Gluon](gluon.md), [SigmaFi](sigmafi.md), [Duckpools](duckpools.md), [ErgoRaffle](ergoraffle.md), [Auction House](ergo-auctions.md), [SkyHarbor](skyharbor.md), [Rosen Bridge](rosen.md), Oracle Pools. |
| Alpha / public testing | [Machina Finance](machina-finance.md), [Etcha](etcha.md), [Degen Wallet and Degens.World apps](degens-world.md), [Mew Finance](mew-finance.md), [Palmyra ComDEX](palmyra.md), [Crystal Pool](crystal-pool.md). |
| Prototype / research | [ChainCash](chaincash.md), Basis, agent-credit experiments, Sigma Chains, [Ergo Marketplace](ergo-marketplace.md), [OptionCoin](optioncoin.md), [Analog Ergo](analog-ergo.md), and other monetary / sidechain designs. |
| Public beta / watch | [ErgoNames](ergonames.md), [Moria Finance](moria-finance.md), [The Field](the-field.md), [Reputation System](reputation-system.md), [Night Owl](nightowl.md), [ergo-use-x402](ergo-use-x402.md), and other legacy or early-stage ecosystem apps. |
| Needs careful wording | Options, derivatives, monetary systems, and bridge expansions should be described by current repo status, not assumed future launch dates. |

### Data, Observability, and Knowledge Tools

| Track | Current state | Watch next |
| --- | --- | --- |
| [eBiome](ebiome.md) | Live external dashboard for explorer, ecosystem analytics, DeFi/stablecoin/mining/Rosen views, and heuristic forensics. | Public source, data provenance, and clearer caveats around probabilistic entity grouping. |
| [Ergomempool Visualizer / Watcher](mempool-vis.md) | Live mempool visualization plus a public watcher dashboard for local-node inclusion-rate, dwell-time, stuck-transaction, and pool-selection analysis. | Source updates, methodology notes, and whether outputs become operator runbook material. |
| [Ergo Knowledge Base](ergo-knowledge-base.md) | Public knowledge and transcript surfaces make ecosystem calls, chats, summaries, and project context searchable. | New ingestion sources, MCP/tooling updates, and source-backed reuse in docs. |

### Wallets and User Experience

| Track | Current state | Watch next |
| --- | --- | --- |
| Mobile / desktop / browser wallets | Multiple wallet surfaces exist, but feature coverage differs by wallet. | Release notes and supported dApp / ErgoPay / connector flows. |
| Hardware wallets | [Ledger](ledger.md) developer-mode history and Keystone integration context are documented. | Merged firmware/app releases, not just PRs. |
| Advanced signing | ChainCash and some prototype flows still expose signing constraints. | Wallet-native support for raw Schnorr or specialized signing paths. |
| Connector and external-wallet work | EIP-12, EIP-20 / ErgoPay, Keystone, Metamask exploration, and Trustwallet exploration are separate tracks with different maturity. | Wallet release notes, connector compatibility, mobile signing UX, and hardware-wallet production status. |
| Agent and wallet experiments | Degens.World wallet/agent tooling is in public testing / prototype territory. | Store releases, public binaries, audits, and user-safety docs. |

### Governance, Funding, and Maintenance

| Track | Current state | Watch next |
| --- | --- | --- |
| EF role | EF scope, treasury, votes, and future-handover docs now separate governance facts from roadmap claims. | Treasury updates, votes, and [Sigmanauts](sigmanauts.md) handover changes. |
| DevDAO / community development | DevDAO describes research/development committees and funding goals. | Concrete funded work, repos, releases, and public deliverables. |
| DAO and coordination apps | Paideia, Sigmanauts voting, treasury reporting, and ecosystem handovers are part of the governance pipeline. | Active proposals, funded work, handover notes, and public treasury reporting. |
| Docs maintenance | Source Watch, weekly Discord scans, and docs-quality checks run as review loops. | Whether weekly Discord leads become reviewed docs updates instead of stale artifacts. |

## Open Watchlist

These items are important but should not be marked complete without new upstream evidence:

- Sub-blocks moving from research/PR review into a tested devnet or mainnet activation path.
- Matrix DevNet work graduating into a specific mainnet proposal.
- Rust node moving from experimental validation into production node claims.
- SANTA adding broader block/chain/vector coverage and more independent implementation runners.
- Matrix Pulse and similar Matrix DevNet tooling moving from operator/debug aids into maintained observability surfaces.
- eBiome forensics and other analytics dashboards publishing source, methodology, and stronger caveats for heuristic address/entity grouping.
- Mempool watcher data moving from investigative dashboards into repeatable node/operator guidance.
- Lithos publishing mainnet-ready miner/operator docs and risk assumptions.
- Rosen chain expansions beyond currently live paths, especially Runes, Firo, Handshake, and Monero-related work.
- ChainCash/Basis gaining wallet-native signing support, stabilized contracts, and clearer user-facing flows.
- Machina and Etcha moving from alpha/prototype into audited, production user flows.
- Oracle Pools / Oracles v2 operator status and whether active data-provider docs need refresh.
- Wallet connector, ErgoPay, Keystone, Metamask, and Trustwallet work moving from exploration into supported user flows.
- ErgoNames beta/genesis status, contract re-review, public source snapshot, and whether beta names are purged before mainnet launch.
- ErgoNames SDK and wallet integrations moving from beta/testing into wallet-supported send flows.
- ergo-use-x402 moving from example implementation into accepted x402 ecosystem support or a ratified Ergo payment standard.
- Reputation System, The Field, Moria, Palmyra, Crystal Pool, and Mew Finance status changes that would move them between prototype, alpha, live, or legacy buckets.

## Detailed Timeline

The sections below keep the longer timeline and ecosystem lists. Some entries describe the state or expectations at the time they were written; use the current snapshot, pipeline overview, and detailed roadmap tracks above for present-day status.

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
Ergo is developed a by a combination of the [Ergo Foundation](ergo-foundation.md), community developers and the recently launched [DevDAO](devdao.md). See the [Ergo Foundation Treasury](ef-treasury.md) and [EF Votes](ef-votes.md) for foundation funding context.

/// admonition | See the [code repositories historically supported by the Ergo Foundation](ef-scope.md#code-repositories-historically-supported-by-the-ergo-foundation).
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
/// details | 2024: Governance Shift and 6.0 Preparation
    {open: false}

- Development coordination became more explicit across DevDAO, Sigmanauts, the Ergo Foundation, and independent ecosystem teams.
- Reference-client and Sigma work focused on preparing the 6.x line while ecosystem infrastructure continued to mature.

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

- [ ] Lithos decentralized mining pool infrastructure continued toward testnet/mainnet readiness
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

/// details | 2025: 6.x Stack and Ecosystem Rebuild
    {open: false}

- **Protocol and tooling:**
  - Sigma SDK 6.0.0, 6.0.1, and 6.0.2 shipped for the 6.x feature line.
  - Ergo node 6.0.1 and 6.1.0 releases moved the reference client into the 6.x era.
  - `sigma-rust`, [ergots](ergots.md), and [Rust node](rust-node.md) work accelerated, exposing edge cases in costing, serialization, validation, and cross-implementation behavior.
  - AppKit and downstream libraries prepared for the Sigma 6.0 / 6.x stack.
  - Cross-implementation testing became more important as Rust, TypeScript, AppKit, and JVM tooling all touched consensus-sensitive serialization and validation paths.
- **Reference client and protocol work:**
  - 6.x release work built on the 2024 RocksDB, P2P, bootstrapping, and Sigma 6 preparation.
  - Sub-blocks, sidechains, NiPoPoW bootstrapping, pruning, and light-client work remained active research and implementation tracks rather than mainnet-complete features.
  - EIP-44, EIP-46, EIP-47, Sigma 6, and related ErgoScript / ErgoTree improvements stayed part of the standards and protocol backlog.
- **Ecosystem:**
  - [ChainCash](chaincash.md) and Basis moved from concept toward active contract and server prototypes.
  - [Rosen Bridge](rosen.md) continued chain and service expansion after its mainnet launch phase.
  - [Gluon](gluon.md), [Dexy](dexy.md), [SigmaUSD](sigmausd.md), [SigmaFi](sigmafi.md), [Duckpools](duckpools.md), Spectrum, and related DeFi systems continued as a mix of live systems, maintenance work, and protocol experiments.
  - Wallet, DeFi, explorer, and infrastructure work continued across community-maintained projects.
- **Wallets and user experience:**
  - Wallet support remained fragmented by platform and feature set, with browser-wallet, desktop, mobile, ErgoPay, connector, and hardware-wallet flows all needing separate tracking.
  - Advanced signing remained relevant for ChainCash/Basis and other prototype flows.
- **Governance and funding:**
  - EF votes focused on treasury-control decisions, on-ramp proposals, ERGOHACK X funding, and operational salary adjustments. See [EF Votes](ef-votes.md).
  - EF, Sigmanauts, DevDAO, and independent teams continued to separate operational responsibilities from core protocol development.
  - Sigmanauts continued taking on ecosystem responsibilities such as market-making coordination and mining-pool work.
///

/// details | 2026: DevNet, Validation, and Application Tooling
    {open: false}

- **Protocol and releases:**
  - [AppKit v6.0.0](https://github.com/ergoplatform/ergo-appkit/releases/tag/v6.0.0) released on top of SigmaSDK 6.0.x.
  - [Sigma SDK v6.0.5](https://github.com/ergoplatform/sigmastate-interpreter/releases/tag/v6.0.5) followed the 6.0.0 through 6.0.4 releases.
  - Ergo node releases moved through `v6.0.2`, `v6.0.2.1`, `v6.0.2.2`, `v6.0.3RC1`, `v6.0.3`, and `v6.1.3`.
  - [Ergo Matrix 6.5.0 RC1](https://github.com/ergoplatform/ergo/releases/tag/v6.5.0-RC1) added a DevNet build for protocol-breaking change testing.
  - Node protocol work improved mempool consistency, extension-section validation, missing-parent header handling, and SyncInfoV2 continuation-header handling.
  - Matrix DevNet became the main surface for testing protocol-breaking changes before any mainnet proposal.
- **Scaling, mining, and validation:**
  - [Lithos](lithos.md) testnet releases reached [`v4.2.0-test`](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test), with work on mempool tracking, Stratum behavior, transaction scheduling, and rollup evaluation.
  - [Rust node](rust-node.md) releases reached the 0.7.x line.
  - SANTA added shared conformance vectors and runners for cross-implementation testing.
  - Rust node, SANTA, `sigma-rust`, and [ergots](ergots.md) continued to expose consensus and evaluation edge cases for review against the JVM reference stack.
- **Applications and ecosystem:**
  - [ChainCash](chaincash.md) and Basis advanced through reserve-contract rework, note redemption, server/API work, and research presentation material.
  - [Gluon Gold](gluon.md) remained live at [gluon.gold](https://gluon.gold/) with a public Ergo UI repository.
  - [Machina Finance](machina-finance.md) published an alpha orders SDK.
  - [Etcha](etcha.md) entered alpha for peer-to-peer options.
  - [Degen Wallet](degens-world.md), Degens.World agent tooling, Ergo MCP, Xergon, and related experimental apps expanded the wallet and agent surface.
  - Rosen Bridge remained live infrastructure while new-chain, service, watcher, guard, SDK, and Runes-related work continued.
  - The ecosystem continued to split between production infrastructure, alpha applications, and research prototypes, making status wording important for user-facing docs.
- **Governance and operations:**
  - EF treasury, votes, and future-handover docs became more important for explaining what the Ergo Foundation still controls and what has moved to Sigmanauts or independent teams.
  - Market-making, funding, and ecosystem coordination continued to move away from a single Foundation-centered roadmap model.
- **Documentation and maintenance:**
  - Docs automation gained Source Watch, Discord Dev Digest, and weekly review issue tooling. See [Contribute Automation](automation.md).
  - The roadmap, EF pages, wallet pages, Rust node, ChainCash, Rosen, and source-watched docs were updated to use source-backed status rather than stale launch expectations.
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

### Stablecoins

- [x] [SigmaUSD](sigmausd.md) stablecoin (Djed protocol)
  - [ ] [SigmaUSD v2](https://gist.github.com/kushti/3f34ed7d70cc6919c29f5bc65772b02e)
- [x] [Gluon](gluon.md) (gold stablecoin)
- [x] [DexyGold](dexy.md) (seigniorage stablecoin)

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
  - [x] DOGE Bridge
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
