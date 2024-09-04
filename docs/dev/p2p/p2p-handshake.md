---
tags:
  - P2P
---

# Handshaking in P2P Protocol


This document outlines the procedure and format of handshake messages, which are essential for establishing a connection with another peer.

For implementation examples, refer to:

- [Ergonnection](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/ErgoSocket.java), a P2P Java library for Ergo, which provides practical implementation of the handshake process, socket management, and message handling.
- [Ergo Handshake](https://github.com/SabaunT/ergo-handshake), a repository that provides a reference implementation of the handshake process in the Ergo protocol.

## Peer Features

Peer features are properties that describe a peer. A peer can have multiple features, which are embedded in a handshake message and remain constant throughout the connection. Features are optional, and a peer can add new ones. If a feature is unrecognized by another peer, it will be skipped. The format of the feature is arbitrary, and any number can be added to the handshake, subject to the handshake message size limit of 8 KB.

Before version 3.3.7, the reference client only supported the "mode feature" (which describes the operating regime of the peer). Since version 3.3.7, a new feature that describes network magic and a pseudorandom session ID has been added.

**Example Implementation**:  

- In the [Ergonnection library](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/records/Feature.java), the `Feature` class represents individual peer features with an `id` and `data`. The features are serialized and deserialized to be included in handshake messages, ensuring that they can be transmitted and interpreted correctly during the handshake.

## Handshake Format

The table below outlines the format of a handshake message:

| Length | Field Name              | Details                                                                                   |
|--------|-------------------------|-------------------------------------------------------------------------------------------|
| 6-8    | Time                    | Reported handshake time (VLQ-encoded, 6 bytes now, 8 bytes max)                           |
| 1      | Agent name length       | Length of an agent name string (unsigned byte)                                            |
| 0-255  | Agent name              | Agent name (e.g., "Cypra wallet") in UTF-8 encoding, 255 bytes max                        |
| 3      | Network protocol version| Protocol version (e.g., [0, 1, 1])                                                        |
| 1      | Peer name length        | Length of peer name string                                                                |

### For Client Capabilities (Mode Feature):

| Length | Field Name                                  | Details                                                           |
|--------|---------------------------------------------|-------------------------------------------------------------------|
| 1      | Feature id                                  | For mode feature = 16                                              |
| 1-2    | Feature body length                         | Length of feature description (VLQ-encoded, up to 2 bytes)        |
| 1      | State type                                  | State representation, 0 = UTXO, 1 = digest                        |
| 1      | Whether the peer is verifying transactions  | 1 = transactions being verified, 0 = not verified                 |
| 1      | Whether the node bootstrapped via NiPoPoW   | 1 if yes, 0 if no (then following field is missed)                |
| (4)    | NiPoPoW suffix length                       | Suffix length for NiPoPoW bootstrapping                           |
| 1-4    | How many blocks kept                        | Signed integer (ZigZag then VLQ encoded), if -1 then all blocks are stored |

**Example Implementation**:  

- The [Peer class](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/records/Peer.java) in the Ergonnection library represents a peer in the network, including features such as agent name, peer name, version, and a list of features. This class handles serialization and deserialization of peer data during the handshake process.

### For Session Peer Feature Introduced in 3.3.7:

| Length | Field Name                                  | Details                                                           |
|--------|---------------------------------------------|-------------------------------------------------------------------|
| 1      | Feature id                                  | For session feature = 3                                           |
| 1-2    | Feature body length                         | Length of feature description (VLQ-encoded, up to 2 bytes)        |
| 4      | Network magic                               | Network magic bytes, see notes                                    |
| 8      | Session id                                  | 64 bits long random session ID                                    |

### Notes:

1. For the testnet, magic bytes are `[2, 0, 0, 1]` (in decimal). For mainnet, `[1, 0, 2, 4]` (in decimal).
2. For IPv4 or IPv6 address bytes, "The result is in network byte order: the highest order byte of the address is in `getAddress()[0]`." Please check `Inet4Address.getAddress()` or `Inet6Address.getAddress()` in Java's JDK for details.
3. For the reference client, the session ID is currently used only to avoid connections to self.

**Example Implementation**:  

- The `Protocol` class in the [Ergonnection library](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/protocol/Protocol.java) manages the deserialization of various protocol messages, including those that handle session features. This ensures that features such as network magic and session IDs are correctly processed during the handshake.

## Handshake Procedure

A peer sends a handshake message, and another peer replies. If no handshake is received within the `handshakeTimeout`, the connection is dropped. The default value for `handshakeTimeout` is 30 seconds.

**Example Implementation**:  

- In the [ErgoSocket class](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/ErgoSocket.java), the handshake process is handled through methods like `sendHandshake()` and `acceptHandshake()`, which manage the serialization and deserialization of handshake data, including the peer's features and session information.
