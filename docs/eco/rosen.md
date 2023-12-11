---
tags:
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

One of the unique aspects of this bridge is that it eliminates the need for deploying and using smart contracts on the other chains. This is because consensus on any action is achieved on the Ergo platform by a group of entities known as Guards. These Guards generate a signed transaction (either for Ergo or chainX) which can then be broadcasted to the other chain by any party, including the Guards themselves.

- **Architecture**: The architecture of the bridge comprises of Watchers and Guards. [Watchers](rosen-watcher.md) are responsible for monitoring blockchain activities and reporting them to [Guards](rosen-guard.md). The Guards process these events and execute actions, thereby ensuring a high level of security and functionality.
- **Smart Contract Reduction**: The Ergo-centric logic of Rosen Bridge significantly reduces the need for smart contracts on the chains it bridges.
- **RSN Token**: The Rosen Token (RSN) plays a crucial role in the operation of the bridge. It serves as a mechanism for sybil resistance, a system for fee distribution, and a means to access the services of the bridge.
- **Scalability and User Safety**: The design of Rosen Bridge allows for the addition of new chains through independent modules. It also prioritizes the success of user transactions by waiting for a sufficient number of confirmations.

