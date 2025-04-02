---
tags:
  - Rosen Bridge
  - Bridge
  - Cross-Chain
  - Interoperability
  - dApp
  - dApp-Beta
---
# Rosen Bridge: The Future of Cross-Chain Asset Transfers

[Rosen Bridge](https://rosen.tech), an open-source protocol, is pioneering the future of cross-chain asset transfers. It's currently in beta, testing its first bridge to Cardano. Rosen Bridge leverages Ergo's capabilities to facilitate secure and efficient coin and token transfers between Ergo and other blockchains.
/// details | Latest Developments
     {type: tip, open: true}
Rosen Bridge is expected to launch imminently, join the [Rosen Telegram chat](https://t.me/rosenbridge_erg) to keep up to date.
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
