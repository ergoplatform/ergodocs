Message format
----------------

Every message in the P2P protocol has the following format:

| Length         | Field Name                     | Details                                                        |  
| :------------  | :----------------------------  | :-----------                                                   |
|4               | Magic bytes                    | Network-specific magic bytes, see Note 1.                      |              
|1               | Message code                   | One byte describing message type                               |
|4               | Message body length          | Length of handshake body (specified below), as signed 32-bit integer  |
|4               | Handshake body checksum        | First four bytes of blake2b(message body)                    |                                        
|*               | Message body                 | Message body (specified below)                                                             |

Notes:

1. For the testnet, magic bytes are `[2, 0, 0, 1]` (in decimal). For mainnet, `[1, 0, 2, 4]` (in decimal).
2. No `VLQ` and `ZigZag` encoding is used for message length (for historical reasons); bytes are coming in big-endian order.


# 

[Tests for parsing networking messages against test vectors #1264](https://github.com/ergoplatform/ergo/pull/1264)

This PR contains :

- assert() swapped with require() as the latter is non-elidable
- unused parameter nextBlockTimestampOpt is removed from HeadersProcessor.requiredDifficultyAfter()

Different test vectors and simple parsers:

- invalid PoW solution validation test for manually checked test vector
- handshake parsing test for a test vector (bytes got from a 3.3.6 mainnet node)
- SyncInfo networking message parsing test (can be used as a simple spec)
- INV networking message parsing test (can be used as a simple spec)

Demo applications:

- to generate address (AdressGenerationDemo)
- transaction JSON printing added to CreateTransactionDemo