Handshake
---------

First of all, nodes are doing handshaking by sending each other handshake messages. Handshaking details are provided in [dedicated P2P Handshaking doc](https://github.com/ergoplatform/ergo/wiki/P2P-Handshaking)

Message format
----------------

Every message in P2P protocol has the following format:

| Length         | Field Name                     | Details                                                        |  
| :------------  | :----------------------------  | :-----------                                                   |
|4               | Magic bytes                    | Network-specific magic bytes, see Note 1.                      |              
|1               | Message code                   | One byte describing message type                               |
|4               | Message body length          | Length of handshake body (specified below), as signed 32-bit integer  |
|4               | Handshake body checksum        | First four bytes of blake2b(message body)                    |                                        
|*               | Message body                 | Message body (specified below)                                                             |

Notes:
1. For the testnet, magic bytes are [2, 0, 0, 1] (in decimal). For mainnet, [1, 0, 2, 4] (in decimal).
2. No VLQ and ZigZag encoding is used for message length (for historical reasons), bytes are coming in big-endian order.
[TODO: provide descriptions for possible values of message body]


Syncing
--------
