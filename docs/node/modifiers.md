---
tags:
  - Modifiers
  - Blocks
  - Node
  - P2P
  - Technical
---
# Ergo Modifiers

In Ergo's P2P protocol, blocks and transactions are called "modifiers". Modifiers are transmitted between nodes as part of the network synchronization process. The Modifier Exchange process encompasses the protocols and systems in place to exchange this information efficiently and securely across the network.


## Ergo Block Structure

The [Ergo block](block.md), a critical structure in the Ergo blockchain, differentiates from most blockchain systems by comprising four distinct sections:

* **Header**: This contains the bare minimum information necessary to synchronize the chain and validate Proof-of-Work (PoW) accuracy. It includes the hashes of other sections.
* **Block Transactions**: This section consists of a series of transactions included within the block.
* **ADProofs**: These proofs are associated with transactions in the corresponding Block Transactions section, allowing light clients to authenticate all transactions and compute a new root hash.
* **Extension**: This section holds additional information that doesn't fit into the previous sections. It includes interlinks and the chain's current parameters when the extension belongs to a block at the end of a voting epoch.

## Header Section

The table below details the fields contained in the Header section:

| Field              | Size (Bytes) | Description                                                                                           |
|--------------------|--------------|-------------------------------------------------------------------------------------------------------|
| version            | 1            | Block version number, incremented with each soft or hard fork                                         |
| parentId           | 32           | Identifier of the parent block                                                                        |
| ADProofsRoot       | 32           | Hash of ADProofs for transactions in the block                                                        |
| stateRoot          | 32           | Root hash of the state (for an AVL+ tree) after the block's application                              |
| transactionsRoot   | 32           | Root hash of transactions in the block (for a Merkle tree)                                            |
| timestamp          | 8            | Block timestamp (expressed in milliseconds since the beginning of Unix Epoch)                         |
| nBits              | 8            | Current difficulty level, presented in a compressed form                                              |
| height             | 4            | Block height                                                                                          |
| extensionRoot      | 32           | Root hash of the extension section                                                                    |
| powSolution        | 75-107       | Solution of the Autolykos PoW puzzle                                                                  |
| votes              | 3            | Votes for changes in system parameters, one byte allocated for each vote                               |

In specific modes, nodes can calculate certain fields independently:

- **parentId**: Calculated when `status==bootstrap` AND `PoPoWBootstrap == false`.
- **ADProofsRoot**: Calculated when `status==regular` AND `ADState==false AND BlocksToKeep>0`.
- **stateRoot**: Calculated when `status==regular` AND `ADState==false AND BlocksToKeep>0`.

## Extension Section

The Extension section serves as a key-value storage accommodating a diverse range of data. 

The key is consistently 2 bytes long, and the maximum size of a value is 64 bytes. The overall Extension size should not exceed 16,384 bytes. 

Certain keys have predefined meanings. For instance, if the first byte of a key equals to `0x00`, the second byte identifies the parameter, and the value determines the parameter's value. <!--TODO: Find this param table and link it.-->

Another predefined key is used for storing the interlinks vector. In this case, the first byte of the key is `0x01`, the second one matches the index of the link in the vector, and the value contains the actual link (32 bytes) prefixed with the frequency it appears in the vector (1 byte). Other prefixes are free for use as required.
