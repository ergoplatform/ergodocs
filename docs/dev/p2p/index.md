---
tags:
  - P2P
---
# P2P Protocol Overview

The Ergo network protocol uses full nodes (peers) to maintain a collaborative peer-to-peer network for block and transaction exchange. This ensures a decentralized and robust system with a high degree of security and integrity.

## Introduction

The [**Full Node**](install.md) is an essential part of the Ergo network. It downloads and verifies every block (and transaction) to maintain a full copy of the blockchain. This way, full nodes contribute to the network's resilience, ensuring transaction and block information is readily available to other nodes. These nodes also relay the verified blocks and transactions to other nodes, helping keep the network up-to-date.

## [Handshake](/dev/p2p/p2p-handshake)

In the Ergo network, establishing a connection between peers requires an exchange of handshake messages. These messages share various features that describe peer properties and remain unchanged during the connection. Each message may include details such as handshake time, agent name, network protocol version, and public address. Specific features such as client capabilities or a session peer feature introduced in version 3.3.7 provide additional information. If there's no handshake received within a predefined `handshakeTimeout`, the connection is dropped.

## [Network Messages](/dev/p2p/network)

The Ergo P2P protocol includes a suite of network messages such as Get Peers, Peers, Sync Info, Inv, Request Modifier, and Modifier. These messages, each identified by a specific code, facilitate operations like node discovery, synchronization, object inventory transmission, and modifier requests. The protocol also defines various record types including Peer, Feature, Modifier, and Header, providing structure for the message content. Various resources and demo applications are available for implementing this protocol.

## [Modifier Exchange](/dev/p2p/modifiers)

In Ergo's P2P protocol, blocks and transactions are called "modifiers". Modifiers are transmitted between nodes as part of the network synchronization process. The Modifier Exchange process encompasses the protocols and systems in place to exchange this information efficiently and securely across the network.

## [Synchronization](synchronisation.md)

Ergo blockchain synchronization revolves around transitioning the state of modifiers from 'Unknown' to 'Held.' The states in between include 'Requested,' 'Received,' and 'Held.' During synchronization, different protocols come into play, such as the Inv protocol, which deals with the transmission and request of modifiers, and Headers synchronization, responsible for synchronizing the node's headers chain with the network. Further, Block Section synchronization ensures the alignment of block sections with the network. The 'DeliveryTracker' ensures the transition from the 'Requested' state to 'Received,' while the NodeViewHolder (NVH) handles the move from 'Received' to 'Held.' This process facilitates the seamless synchronization and updating of the Ergo blockchain.

## Misc

- On the mainnet, P2P uses port `9030` and port `9053` for the API.
- For network crawling, try [libp2p.io](https://libp2p.io/), a modular network stack that allows you to build your own peer-to-peer applications. 

