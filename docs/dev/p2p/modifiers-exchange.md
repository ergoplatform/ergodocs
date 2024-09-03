---
tags:
- P2P
---

# Modifier Exchange

In Ergo's P2P protocol, blocks and transactions are referred to as "modifiers". Modifiers are transmitted between nodes as part of the network synchronization process. The Modifier Exchange process encompasses the protocols and systems in place to exchange this information efficiently and securely across the network.

## Understanding Modifiers

Modifiers are fundamental elements in the Ergo network that represent either blocks or transactions. They are crucial for maintaining the state of the blockchain and are exchanged between nodes during the network synchronization process.

In the Ergo source code, modifiers are represented in a hierarchical structure that differentiates between various types of data exchanged in the network. These include block sections, transactions, and other consensus-critical data.

For specific implementation details, refer to the following:

- **AbstractModifier**: The base trait for all modifiers.
- **Block Sections**: Which include key parts of blocks like `Header`, `BlockTransactions`, `ADProofs`.
- **Transactions**: Represented by the `ErgoTransaction` class.

For more details, see the [Ergo Modifiers](https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers) directory on GitHub.

## Modifier Exchange Process

The Modifier Exchange process involves several steps:

1. **Inventory Transmission (Inv)**: A node sends an Inv message to its peers to inform them about the new modifiers it has. This message contains identifiers for the modifiers, allowing peers to determine whether they need any of the new data.
        - **Code Reference**: The `InvSpec` class in the [network/message](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/InvSpec.scala) directory handles the construction and parsing of Inv messages.

2. **Modifier Request (RequestModifier)**: Upon receiving an Inv message, a node sends a RequestModifier message to request the new modifiers it does not yet possess. This helps nodes synchronize with the most recent state of the blockchain.
        - **Code Reference**: The `RequestModifierSpec` class in the [network/message](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/RequestModifierSpec.scala) directory defines how these requests are structured and transmitted.

3. **Modifier Delivery (Modifier)**: The node that initially sent the Inv message responds with a Modifier message that delivers the requested modifiers. This message contains the actual data (e.g., block sections, transactions) needed by the requesting node.
        - **Code Reference**: The `ModifiersSpec` class in the [network/message](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/ModifiersSpec.scala) directory is responsible for managing the delivery of modifiers.

This process ensures that all nodes in the network maintain an up-to-date state of the blockchain, crucial for the integrity and performance of the Ergo network.

## Source Code

For a deeper understanding of how modifiers are implemented and managed in the Ergo network, you can explore the following key components in the Ergo repository:

- **[src/main/scala/org/ergoplatform/modifiers](https://github.com/ergoplatform/ergo/tree/master/ergo-core/src/main/scala/org/ergoplatform/modifiers)**: This directory contains the core classes and traits defining the different types of modifiers in the Ergo blockchain.
- **[InvSpec.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/InvSpec.scala)**: Handles the inventory message (Inv) specification.
- **[RequestModifierSpec.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/RequestModifierSpec.scala)**: Manages the request for specific modifiers.
- **[ModifiersSpec.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/ModifiersSpec.scala)**: Oversees the structure and delivery of modifier messages.

By exploring these files, you can gain a comprehensive understanding of how modifiers are exchanged and synchronized across nodes in the Ergo network.
