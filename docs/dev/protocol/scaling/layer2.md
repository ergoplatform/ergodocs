---
tags:
- Layer 2
- Scaling
- Sidechains
- Off-chain Solutions
- Sigma Chains
---
# Layer 2: Off-Chain

Layer 2 solutions are secondary frameworks or protocols constructed on top of a [Layer 1](layer1.md) blockchain protocol. Their purpose is to enhance the efficiency, scalability, and capabilities of the underlying blockchain by facilitating *off-chain* transactions or computations.

Ergo is compatible with a broad range of Layer 2 solutions derived from other UTXO blockchains. The platform can implement various off-chain solutions like [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains, which help alleviate blockchain congestion and offer benefits akin to ZK-rollups.

> Join the Layer 2 discussion on [Telegram](https://t.me/ErgoLayer2) or [Discord]().

## ErgoScript: Powering Layer 2 Transactions

[ErgoScript](ergoscript.md)'s flexible design allows large parts of transactions to be executed on Layer 2, which are then settled on the Ergo blockchain in a single transaction. For instance, a developer successfully used the eUTXO model to airdrop native tokens to [10,000 addresses simultaneously](https://explorer.ergoplatform.com/en/transactions/e2c4954665ccf87791f42983ae4f7031205c2e719709907cbf2ff09e5489d4b8). 

ErgoScript features several advancements like time-weighted data, Turing completeness, read-only data inputs, multi-stage contracts, sigma protocols, NIPoPoWs, and more. These enhancements enable a variety of Layer 2 protocols, each addressing scalability issues in their unique way.

> **Ergo serves as a settlement layer for multiple Layer 2 protocols and applications.**

## Current Layer 2 Projects and Developments

### Layer 2 Solutions Leveraging Sub-Blocks
While sub-blocks are a Layer 1 protocol enhancement, they enable several Layer 2 scaling solutions:

- Faster confirmation times for Layer 2 protocols
- Enhanced support for payment channels
- More efficient state channel operations
- Improved settlement layer for off-chain transactions

Layer 2 protocols can utilize sub-blocks to:

- Group off-chain transactions more efficiently
- Reduce settlement times
- Increase throughput for Layer 2 applications
- Enable more responsive user experiences

### SigmaChains and Sidechains
SigmaChains leverage Ergo's Sigma contracts to create versatile sidechains that can operate as either merge-mined sidechains or standalone blockchains. Key features include:

- Enhanced scalability and privacy features
- Experimental platform for new features
- Various chain commitment options for main chain security
- Comprehensive technical documentation in "Sigma Deck 2"

### ChainCash
ChainCash is developing a decentralized, peer-to-peer monetary system using Layer 2 derivative signature chains. The project features:

- Elastic money creation capabilities
- Digital notes representing various values
- Support for digital tokens and real-world assets
- Implementation of top-up transactions and blockchain scanning

## Plasma: Enhancing Data Structures

Ergo inherently supports [AVL trees](avl.md), an efficient authenticated data structure that allows for proving different properties of the data without accessing the entire dataset.

The ledger is maintained as an AVL tree using **Plasma**. Users conduct off-chain transactions with the bank, resulting in changes in the ledger. The bank periodically publishes a compact snapshot of the ledger on the blockchain.

The [Plasma Library](plasma.md) enables the building of Plasma chains, currently used primarily for:

- Data compression
- Contract simplification
- Plasma staking contracts
- Off-chain operation management

## NIPoPoWs: Facilitating Scalability

[NiPoPoWs](nipopows.md) enhance blockchain interoperability and scalability through:

### Enhanced Security through Interoperability
- Smaller chains can leverage security of larger networks
- Periodic proof-of-work submissions between chains
- Cryptographically secure asset transfers
- Enables seamless asset transfers without centralized intermediaries

### Cross-Chain Communications
- Facilitates smart contract executions across networks
- Enables consolidated data verification
- Supports integrated blockchain ecosystems
- Improves scalability of Layer 2 solutions like sidechains

### Applications in Layer 2 Technologies
- **Sidechains**: NIPoPoWs enable sidechains to operate more autonomously while maintaining security
- **State Channels**: Transactions can be processed off-chain with assurances of eventual consistency
- **Cross-Chain Verification**: Enables efficient verification of transactions across different chains
- **Security Enhancement**: Smaller chains can leverage the security of larger networks

## Emerging Layer 2 Solutions

### Lightning Network

The Lightning Network creates payment channels through multi-signature wallets, enabling off-chain transactions between participants.

### Rainbow Network
A non-custodial exchange and payment network supporting multiple assets through price oracles, enabling off-chain trading, borrowing, and lending.

### Rollups
Two primary types of rollups are being explored:

- **Optimistic Rollups**: Handle transactions on parallel chains using fraud-proof principles
- **ZK-Rollups**: Utilize zkSNARKs to bundle hundreds of transfers off-chain

### Additional Solutions
- **Hydra**: Implements isomorphic state channels for multi-party transactions
- **Zero-Knowledge Contingent Payments**: Enable trustless knowledge-based payments
- **FairSwap/FastSwap protocols**: Provide secure and efficient transaction methods
- **Coinpools**: Group transactions for improved efficiency

## Development Considerations

### Security and Consensus
- Careful evaluation of security implications for new Layer 2 solutions
- Selection of appropriate consensus mechanisms for different applications
- Implementation of robust fraud prevention measures

### User Experience
- Development of mempool chaining for immediate transaction feedback
- Focus on seamless integration between Layer 1 and Layer 2 solutions
- Optimization of transaction processing and confirmation times

### Research and Development
Ongoing research continues to explore:

- Advanced sharding techniques
- Novel consensus mechanisms
- Improved transaction ordering
- Enhanced mempool management

