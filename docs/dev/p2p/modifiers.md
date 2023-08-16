---
tags:
- P2P
---

# Modifier Exchange

In Ergo's P2P protocol, blocks and transactions are referred to as "modifiers". Modifiers are transmitted between nodes as part of the network synchronization process. The Modifier Exchange process encompasses the protocols and systems in place to exchange this information efficiently and securely across the network.

## Understanding Modifiers

Modifiers are fundamental elements in the Ergo network that represent either blocks or transactions. They are crucial for maintaining the state of the blockchain and are exchanged between nodes during the network synchronization process.

## Modifier Exchange Process

The Modifier Exchange process involves several steps:

1. **Inventory Transmission (Inv)**: A node sends an Inv message to its peers to inform them about the new modifiers it has.
2. **Modifier Request (RequestModifier)**: Upon receiving an Inv message, a node sends a RequestModifier message to request the new modifiers.
3. **Modifier Delivery (Modifier)**: The node that initially sent the Inv message responds with a Modifier message that delivers the requested modifiers.

This process ensures that all nodes in the network maintain an up-to-date state of the blockchain.

## Source Code

For a deeper understanding of how modifiers are implemented in the Ergo network, you can explore the source code in the following directory:

- [src/main/scala/org/ergoplatform/modifiers](https://github.com/ergoplatform/ergo/tree/master/src/main/scala/org/ergoplatform/modifiers)