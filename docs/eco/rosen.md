---
tags:
  - Rosen Bridge
  - Bridge
  - Cross-Chain
  - Interoperability
  - dApp
  - dApp-Beta
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: rosen-bridge/watcher
    branch: master
    paths:
      - README.md
  - repo: rosen-bridge/guard-service
    branch: master
    paths:
      - README.md
  - repo: rosen-bridge/ui
    branch: master
    paths:
      - README.md
  - repo: rosen-bridge/rosen-sdk
    branch: dev
    paths:
      - README.md
  - repo: rosen-bridge/rosenet
    branch: dev
    paths:
      - README.md
  - repo: rosen-bridge/sign-protocols
    branch: dev
    paths:
      - README.md
  - repo: rosen-bridge/cleanup-service
    branch: dev
    paths:
      - README.md
  - repo: rosen-bridge/network-client
    branch: dev
    paths:
      - README.md
  - repo: SavonarolaLabs/rosen-ui
    branch: main
    paths:
      - src/routes
      - src/lib
source_of_truth:
  - https://github.com/rosen-bridge/watcher/releases/tag/6.2.1
  - https://github.com/rosen-bridge/guard-service/releases/tag/9.1.1
  - https://github.com/rosen-bridge/ui/releases/tag/rosen-service-4.3.5
  - https://github.com/rosen-bridge/rosen-sdk
  - https://github.com/rosen-bridge/rosenet
  - https://github.com/rosen-bridge/sign-protocols
  - https://github.com/rosen-bridge/rosen-chains
  - https://github.com/rosen-bridge/cleanup-service
  - https://github.com/rosen-bridge/network-client
  - https://github.com/SavonarolaLabs/rosen-ui
---
# Rosen Bridge: The Future of Cross-Chain Asset Transfers

[Rosen Bridge](https://rosen.tech), an open-source protocol, is pioneering the future of cross-chain asset transfers. It's currently in beta, testing its first bridge to Cardano. Rosen Bridge leverages Ergo's capabilities to facilitate secure and efficient coin and token transfers between Ergo and other blockchains.
/// details | Latest Developments
     {type: tip, open: true}
Bridges live between: ADA, BSC, BTC, ETH, DOGE, join the [Rosen Telegram chat](https://t.me/rosenbridge_erg) to keep up to date.
///

## Welcome to RosenBridge

RosenBridge connects Cardano and Ergo with Ethereum, EVM chains, and beyond. The bridge enables secure, efficient, and user‑friendly cross‑chain transfers by keeping consensus and auditability on Ergo, while external chains rely only on multisig or threshold signatures controlled by Guards.

/// details | Video introduction
     {type: info, open: false}
Please see [this video](https://www.youtube.com/watch?v=Xsiy-yPJQ6w) for a visual introduction.
///

## Recent updates

- `Feb 11` to `Apr 22`: Firo and Handshake integrations moved through watcher, guard-service, and rosen-service updates.
- Watcher releases have moved through [6.2.1](https://github.com/rosen-bridge/watcher/releases/tag/6.2.1), including a Bitcoin Runes observation fix for Unisat pagination.
- Guard service releases have moved through [9.1.1](https://github.com/rosen-bridge/guard-service/releases/tag/9.1.1), with dependency updates for Bitcoin Runes RPC support.
- Rosen UI/service releases have moved through `rosen-service-4.3.5` in the [Rosen UI repository](https://github.com/rosen-bridge/ui/releases/tag/rosen-service-4.3.5).
- Rosen shared packages also moved through [rosen-sdk](https://github.com/rosen-bridge/rosen-sdk), [rosenet](https://github.com/rosen-bridge/rosenet), and [sign-protocols](https://github.com/rosen-bridge/sign-protocols) updates. The older [rosen-chains](https://github.com/rosen-bridge/rosen-chains) package repository is archived; chain packages moved into guard-service.
- [network-client](https://github.com/rosen-bridge/network-client) is the Rosen client-library monorepo used by `@rosen-clients/*` packages.
- [cleanup-service](https://github.com/rosen-bridge/cleanup-service) is Rosen infrastructure for cleanup flows such as fraud and slash transactions.
- [SavonarolaLabs/rosen-ui](https://github.com/SavonarolaLabs/rosen-ui) is a small Svelte-based Rosen UI/widget prototype. Treat it as community interface reference, separate from the maintained Rosen UI/service repository.
- `Apr 22`: Rosen stats work added TVL, volume, locked-assets, and user-count metrics, while the app also picked up React 19, Sentry, and live-data improvements.
- The new rosen-service also added Bitcoin Runes support.

## Why RosenBridge

- Decentralized security: Guard‑based m‑of‑n/threshold signatures with independent validation by each Guard.
- User‑friendly: Intuitive UI to initiate cross‑chain transfers with clear fee visibility.
- Broad compatibility: Initially Cardano, Ergo, and Ethereum/EVMs; extensible to new chains supporting multisig/threshold signing.
- Community‑driven: Open source with community feedback and contributions welcomed.

## Explore RosenBridge

- [Concepts & security model](concepts-assumptions.md)
- [How transfers work end‑to‑end](token-transfer-flows.md)
- [Fees and dust collection on Ergo](fees-and-dust.md)
- [Add a new chain](new-chain-integration.md)
- [Benefits at a glance](benefits.md)
- [Events & status](events-and-status.md)
- [Security model details](security-model.md)
- [Troubleshooting guide](rosen-troubleshooting.md)
- [Glossary](rosen-glossary.md)
- [Monero PoC design](bringing-monero.md)
- Roles:
  - [Guards](rosen-guard.md)
  - [Watchers](watcher.md)
- [Tokenomics (RSN)](rosen-tokenomics.md)

/// details | References
     {type: tip, open: false}
- Contracts: https://docs.rosen.tech/rosen/readme-1/rosen/contracts/contract
- Guard: Keygen (Docker): https://docs.rosen.tech/rosen/readme-1/guard/keygen-docker
- Guard: Production Setup: https://docs.rosen.tech/rosen/readme-1/guard/setup
- Watcher: Deploy (Docker): https://docs.rosen.tech/rosen/readme-1/watcher/deploy-docker
///

## Key Features

Rosen Bridge is an [open-source](https://github.com/rosen-bridge) protocol, primarily focused on Ergo, that allows users to seamlessly transfer coins and tokens between Ergo and any other compatible blockchain. The compatibility of the other blockchain, referred to as chainX, is determined by its support for multi-signature transactions or threshold signatures.

One of the unique aspects of this bridge is that it eliminates the need for deploying and using smart contracts on the other chains. This is because consensus on any action is achieved on the Ergo platform by a group of entities known as [Guards](rosen-guard.md). These Guards generate a signed transaction (either for Ergo or chainX) which can then be broadcasted to the other chain by any party, including the Guards themselves.

- **Architecture**: The architecture of the bridge comprises of Watchers and Guards. [Watchers](watcher.md) are responsible for monitoring blockchain activities and reporting them to Guards. The Guards process these events and execute actions, thereby ensuring a high level of security and functionality.
- **Smart Contract Reduction**: The Ergo-centric logic of Rosen Bridge significantly reduces the need for smart contracts on the chains it bridges.
- **RSN Token**: The Rosen Token (RSN) plays a crucial role in the operation of the bridge. It serves as a mechanism for sybil resistance, a system for fee distribution, and a means to access the services of the bridge. (See the [Tokenomics](rosen-tokenomics.md) section)
- **Scalability and User Safety**: The design of Rosen Bridge allows for the addition of new chains through independent modules. It also prioritizes the success of user transactions by waiting for a sufficient number of confirmations.

## Rosen Bridge Operations and Features

/// details | What is the bridge fee structure?
     {type: info, open: false}
Initially, it's the greater of $10 or 0.5% of the transaction value, plus network fees, adjustable by the guard set. The fee is collected in the transferred token on Ergo. Network fees vary: static for Ergo and Cardano, dynamic for EVM-based networks.
///

/// details | Why is the fee so high?
     {type: info, open: false}
Each event has to be reported on by 60%+1 of Watchers, and they need to be incentivised to do so. It also prevents all their permits being exhausted by low-value transactions.
///

/// details | Is there a maximum amount for a single transaction on Rosen Bridge?
     {type: info, open: false}
No fixed maximum, but large transfers may take longer, from hours to 1-2 days, due to manual guard intervention for fund transfers from cold to hot wallets.
///

/// details | How is ADA managed within the system for transactions to Cardano?
     {type: info, open: false}
Network fees in the transaction token on Ergo are sent to a dedicated address for covering network fees on different chains. Currently, the Rosen team manually manages this, with plans for future automation.

///

/// details | How can a project add new token options to the bridge?
     {type: info, open: false}
Projects pay a listing fee to the Rosen Fund, with potential discounts for open-source projects. This involves minting wrapped tokens and updating the token map. Fees are distributed to watchers and guards.
///

/// details | What are the next chains to be added following ADA?
     {type: info, open: false}
The roadmap includes BTC, BSC (EVM-chains), and Dogecoin in the midterm. Code refactoring aims to facilitate adding new chains, with initial chains being the most challenging.
///

/// details | What is the size and composition of the team?
     {type: info, open: false}

The team includes 8 developers, with some frontend and UI tasks outsourced. Additionally, 2-3 developers have worked part-time over the past year, supported by several advisors.

For more information, please see the [Team](rosen-team.md) section.
///
