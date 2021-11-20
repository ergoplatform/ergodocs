Handshaking
===========


To establish a connection with another peer, a handshake messages exchange is needed in the first place. This document
describes handshaking procedure and messages format. 

There is also [github.com/SabaunT/ergo-handshake](https://github.com/SabaunT/ergo-handshake)

Peer Feature
------------

A peer feature describes some properties of a peer. Every peer can have one or more peer features. Features are embedded into a handshake message and remain unchanged during the connection. Features are optional by default: a peer can add new ones, and if another peer is not recognizing it, The node will skip the feature. The feature format is arbitrary. Any number of features can be added to the handshake; only handshake message has a size limit (8 KB).
 
The only feature the reference client supported before 3.3.7 is "mode feature" (describing the operating regime of the peer). 
Since 3.3.7, a new feature describing network magic and (pseudorandom) session-id added. 

Handshake Format
----------------

| Length         | Field Name                     | Details                                                      |
| :------------  | :----------------------------  | :-----------                                                 |
|6-8             | Time                           | Reported handshake time (VLQ-encoded, 6 bytes now, 8 bytes max)              |
|1               | Agent name length              | Length of agent name string (unsigned byte) |
|0-255           | Agent name                     | Agent name (e.g. "Cypra wallet") in UTF-8 encoding, 255 bytes max |
|3               | Network protocol version       | Protocol version (e.g. [0, 1, 1]  |
|1               | Peer name length               | Length of peer name string       |      
|0-255           | Peer name                      | Peer name (e.g. "kushti's node") in UTF-8 encoding, 255 bytes max
|1               | Public node flag               | Flag indicating whether the node has a public address (0 or 1) |
|(1)             | Public address length          | Length of public address |
|(*)             | Public address                 | Public IP address bytes, IPv4 of IPv6, 4 or 6 bytes, see Note 2 |
|(4)             | Public address port            | Public address port | 
|1               | Number of peer features        | How many features are encoded further (unsigned byte) | 
|*               | Features                       | Serialized features, one after another (specified below) | 



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