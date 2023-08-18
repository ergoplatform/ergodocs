---
tags:
  - P2P
---

# Handshaking in P2P Protocol


This document outlines the procedure and format of handshake messages, which are essential for establishing a connection with another peer. 

For implementation examples, refer to:
- [Ergonnection](https://github.com/Satergo/Ergonnection/blob/master/src/main/java/com/satergo/ergonnection/ErgoSocket.java), a P2P Java library for Ergo
- [github.com/SabaunT/ergo-handshake](https://github.com/SabaunT/ergo-handshake)

## Peer Features


Peer features are properties that describe a peer. A peer can have multiple features, which are embedded in a handshake message and remain constant throughout the connection. Features are optional, and a peer can add new ones. If a feature is unrecognized by another peer, it will be skipped. The format of the feature is arbitrary, and any number can be added to the handshake, subject to the handshake message size limit of 8 KB.
 
Before version 3.3.7, the reference client only supported the "mode feature" (which describes the operating regime of the peer). Since version 3.3.7, a new feature that describes network magic and a pseudorandom session-id has been added. 

## Handshake Format


The table below outlines the format of a handshake message:

 Length         | Field Name                     | Details                                                      |
 :------------  | :----------------------------  | :-----------                                                 |
6-8             | Time                           | Reported handshake time (VLQ-encoded, 6 bytes now, 8 bytes max)              |
1               | Agent name length              | Length of an agent name string (unsigned byte) |
0-255           | Agent name                     | Agent name (e.g. "Cypra wallet") in UTF-8 encoding, 255 bytes max |
3               | Network protocol version       | Protocol version (e.g. [0, 1, 1])  |
1               | Peer name length               | Length of peer name string       |      


For client capabilities (Mode feature):

| Length         | Field Name                                  | Details                       |                                
| :------------  | :-------------------------------------      | :-----------                  |  
|1               | Feature id                                  | for mode feature = 16         |    
|1-2               | Feature body length                         | Length of feature description (VLQ-encoded, up to 2 bytes)|
|1               | State type                                  | State representation, 0 = utxo, 1 = digest |
|1               | Whether the peer verifying transactions     | 1 = transactions being verified, 0 = not verified |                               
|1               | Whether the node bootstrapped via NiPoPoW   | 1 if yes, 0 if no (then following field is missed) |
|(4)             | Nipopow suffix length                       | Suffix length for NiPoPoW bootstrapping |      
|1-4               | How many block kept                         | signed integer (ZigZag then VLQ encoded), if -1 then all the blocks are stored |
 
For session peer feature introduced in 3.3.7:

| Length         | Field Name                                  | Details                       |                                
| :------------  | :-------------------------------------      | :-----------                  |  
|1               | Feature id                                  | for session feature = 3         |    
|1-2               | Feature body length                         | Length of feature description (VLQ-encoded, up to 2 bytes) |
|4               | Network magic                               | Network magic bytes, see notes |
|8               | Session id                                  | 64 bits long random session id |


Notes:

1. For the testnet, magic bytes are `[2, 0, 0, 1]` (in decimal). For mainnet, `[1, 0, 2, 4]` (in decimal).   
2. For IPv4 or IP6 address bytes, "The result is in network byte order: the highest order byte of the address is in 
`getAddress()[0]`. Please check `Inet4Address.getAddress()` or `Inet4Address.getAddress()` in Java's JDK for details.
3. For reference client, session id is currently used only to avoid connections to self

Handshake Procedure
-------------------

A peer is sending a handshake message, another replies. If there's no handshake got within `handshakeTimeout`, then the connection is dropped. Default value for `handshakeTimeout = 30s`