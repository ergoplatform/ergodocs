---
tags:
  - P2P
---

# Network Messages in Ergo's P2P Protocol

This document provides a detailed overview of the network messages in Ergo's P2P protocol. Understanding these messages is crucial for interacting with the Ergo network at a low level. Each message in the protocol has a specific format and serves a unique purpose in the communication between nodes.

## Message Format

Every message in the P2P protocol has the following format:

| Data type         | Field name              | Details                                                                                                                      |  
|:------------------|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| byte\[4\]         | Magic bytes             | For the mainnet, the magic bytes are `{1, 0, 2, 4}`. For testnet, `{2, 0, 0, 1}`.                                            |              
| unsigned byte     | Message code            | One byte describing message type                                                                                             |
| int               | Message body length     | No `VLQ` or `ZigZag` encoding is used for the message length (for historical reasons); bytes are coming in big-endian order. |
| byte\[4\]         | Handshake body checksum | First four bytes of blake2b256(message body)                                                                                 |                                        
| byte\[bodyLength] | Message body            | Message body                                                                                                                 |

For more detailed implementation, you can check out the [Ergo Node View Synchronizer](https://github.com/ergoplatform/ergo/blob/master/src/main/scala/org/ergoplatform/network/ErgoNodeViewSynchronizer.scala) in the Ergo repository.

## Records

Records are structured data types used in the P2P protocol. They include Peer, Feature, Modifier, and Header records.

### Peer

| Data type               | Field name                    | Details                                                           |
|:------------------------|:------------------------------|:------------------------------------------------------------------|
| unsigned byte           | *Length of next field*        |
| UTF-8 String            | Agent name                    |
| byte\[3\]               | Version                       | For example, `{4, 0, 25}`                                         |
| unsigned byte           | *Length of next field*        |
| UTF-8 String            | Peer name                     |
| boolean                 | Whether public address exists |
| (unsigned byte)         | Length of the IP **plus 4**   | When decoding, subtract the value with 4 to get the actual length |
| (byte\[ipLength - 4\])  | The public IP address         |
| (VLQ unsigned **int**)  | Port                          |
| unsigned byte           | Count of peer features        |
| Feature\[featureCount\] | Features                      |

### Feature

| Data type          | Field name   |
|:-------------------|:-------------|
| unsigned byte      | Feature code |
| VLQ unsigned short | Body length  |
| byte\[bodyLength\] | Body         |

### Modifier (Record)

| Data type            | Field name       |
|:---------------------|:-----------------|
| byte\[32\]           | Modifier ID      |
| VLQ unsigned int     | Length of object |
| byte\[objectLength\] | Object           |

### Header

| Data type          | Field name      |
|:-------------------|:----------------|
| VLQ unsigned short | Length of bytes |
| byte\[length]      | Bytes           |

For a deeper understanding of how records are serialized, check out the [Ergo Serialization Documentation](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/serialization/ErgoSerializer.scala).

## Messages

Messages are the primary means of communication between nodes in the P2P network. They include Get Peers, Peers, Sync Info, Inv, Request Modifier, and Modifier messages.

### Get Peers

**Code = 1**

The body is empty.

### Peers

**Code = 2**

Sent in response to Get Peers. Contains all the peers that are currently connected to. Used for node discovery.

| Data type         | Field name     |
|:------------------|:---------------|
| VLQ ZZ int        | Count of peers |
| [Peer](#peer)\[\] | Peers          |

For the Java implementation of the `GetPeers` message, refer to [Ergonnection](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/messages/GetPeers.java).

### Sync Info

**Code = 65**

**New (Added in 4.0.16)**

It is sent only to nodes that report a version of 4.0.16 or higher. For older nodes, the [Sync Info (old)](#sync-info-old) is sent.

Requests an [Inv](#inv) message that provides modifier IDs required by the sender to synchronize their blockchain with the recipient. It allows a peer which has been disconnected or started for the first time to get the data it needs to request the blocks it hasn't seen.

| Data type                        | Field name              |
|:---------------------------------|:------------------------|
| VLQ unsigned short               | The constant value `0`  |
| byte                             | The constant value `-1` |
| unsigned byte                    | Count of headers        |
| [Header](#header)\[headerCount\] | Headers                 |

### Sync Info (old)

**Code = 65**

The old (before 4.0.16) version of the Sync Info message.

| Data type                       | Field name                       |
|:--------------------------------|:---------------------------------|
| VLQ unsigned short              | Count of last header IDs         |
| byte\[32\]\[lastHeaderIdCount\] | Last header IDs (ID byte arrays) |

### Inv

**Code = 55**

Transmits one or more inventories of objects known to the transmitting peer.

It can be sent unsolicited to announce new transactions or blocks, or it can be sent in reply to a [Sync Info](#sync-info) message.

| Data type                  | Field name                |
|:---------------------------|:--------------------------|
| unsigned byte              | Type ID                   |
| VLQ unsigned int           | Count of elements         |
| byte\[32\]\[elementCount\] | Elements (ID byte arrays) |

For an example of how INV messages are handled, see [InvSpec.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/network/message/InvSpec.scala).

### Request Modifier

**Code = 22**

Requests one or more modifiers from another node. The objects are requested by an inventory, which the requesting node typically received previously with an [Inv](#inv) message.

This message cannot be used to request arbitrary data, such as historic transactions no longer in the memory pool. Full nodes may not even be able to provide older blocks if they've pruned old transactions from their block database.

For this reason, this message should usually only be used to request data from a node that previously advertised it had that data by sending an [Inv](#inv) message.

| Data type                  | Field name                |
|:---------------------------|:--------------------------|
| unsigned byte              | Modifier type ID          |
| VLQ unsigned int           | Count of elements         |
| byte\[32\]\[elementCount\] | Elements (ID byte arrays) |

### Modifier

**Code = 33**

Sent in response to Request Modifier.

| Data type                                     | Field name         |
|:----------------------------------------------|:-------------------|
| unsigned byte                                 | Type ID            |
| VLQ unsigned int                              | Count of modifiers |
| [Modifier](#modifier-record)\[modifierCount\] | Modifiers          |

## Pull Requests (PRs) & Tests

The [NiPoPoW powered bootstrapping PR #1365](https://github.com/ergoplatform/ergo/issues/1365) is a relevant enhancement that introduces a method to bootstrap nodes using Non-Interactive Proofs of Proof-of-Work (NiPoPoWs). 

Tests for parsing networking messages against test vectors are discussed in PR [#1264](https://github.com/ergoplatform/ergo/pull/1264), which includes:

- Enhanced validation with `require()` for non-elidable checks.
- Simplified test vectors for invalid PoW solution validation and handshake parsing.
- Introduced SyncInfo networking message parsing test (can be used as a simple spec).

These tests ensure robust handling of network messages in Ergo’s P2P protocol.

## Demo Applications

Demo applications are available for practical implementation, such as:

- **Address Generation**: [AddressGenerationDemo](https://github.com/ergoplatform/ergo/blob/master/ergo-wallet/src/test/java/org/ergoplatform/wallet/AddressGenerationDemo.java)
- **Transaction JSON Printing**: [CreateTransactionDemo](https://github.com/ergoplatform/ergo/blob/master/ergo-wallet/src/test/java/org/ergoplatform/wallet/CreateTransactionDemo.java)

These demos provide examples of how to generate addresses and print transactions using the Ergo wallet functionalities.

## Resources

- A simple implementation of VLQ and ZigZag encoding can be found [here](https://gist.github.com/satsen/5e7bcc38565ad193cf7d906a856f804e).
- A complete implementation of the P2P protocol written in Java can be found in [Ergonnection](https://github.com/Satergo/Ergonnection).

