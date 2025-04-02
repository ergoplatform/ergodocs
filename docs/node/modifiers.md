---
tags:
  - Modifiers
  - Blocks
  - Node
  - P2P
  - Technical
---
# Ergo Modifiers

In Ergo's P2P protocol, the fundamental units of data exchanged between nodes, such as blocks and transactions, are referred to as "modifiers." Modifiers are transmitted as part of the network synchronization process. The Modifier Exchange process encompasses the protocols and systems designed to exchange this information efficiently and securely across the network.


## Ergo Block Structure

The [Ergo block](block.md), a critical structure in the Ergo blockchain, differs from many other blockchain systems by comprising four distinct sections (modifiers):

* **Header**: Contains the minimal information necessary to synchronize the chain and validate Proof-of-Work (PoW) correctness. It includes cryptographic hashes (roots) of the other sections.
* **Block Transactions**: Consists of the ordered sequence of transactions included within the block.
* **ADProofs**: Contains Authenticated Dictionary proofs associated with the transactions in the `BlockTransactions` section. These proofs allow light clients to validate transactions against the UTXO set state root hash found in the header.
* **Extension**: Holds supplementary information. This includes [interlinks](nipopows.md) (for NiPoPoWs) and, for blocks at the end of a voting epoch, the blockchain parameters resulting from miner voting.

## Header Section

The table below details the fields contained within the Header modifier:

| Field              | Size (Bytes) | Description                                                                                           |
|--------------------|--------------|-------------------------------------------------------------------------------------------------------|
| version            | 1            | Block version number, incremented with each soft or hard fork                                         |
| parentId           | 32           | Identifier of the parent block                                                                        |
| ADProofsRoot       | 32           | Hash of ADProofs for transactions in the block                                                        |
| stateRoot          | 32           | Root hash of the authenticated UTXO set state (an AVL+ tree) after applying the block's transactions. |
| transactionsRoot   | 32           | Root hash of the Merkle tree of transactions included in the block.                                   |
| timestamp          | 8            | Block timestamp (in milliseconds since the beginning of the Unix Epoch).                              |
| nBits              | 8            | Current difficulty target (encoded in a compressed format).                                           |
| height             | 4            | Block height (distance from the genesis block).                                                       |
| extensionRoot      | 32           | Root hash of the block's extension section.                                                           |
| powSolution        | 75-107       | Solution to the Autolykos v2 Proof-of-Work puzzle.                                                    |
| votes              | 3            | Bytes representing miner votes for changes in system parameters.                                      |

In specific modes, nodes can calculate certain fields independently:

- **parentId**: Calculated when `status==bootstrap` AND `PoPoWBootstrap == false`.
- **ADProofsRoot**: Calculated when `status==regular` AND `ADState==false AND BlocksToKeep>0`.
- **stateRoot**: Calculated when `status==regular` AND `ADState==false AND BlocksToKeep>0`.

## Extension Section

The Extension section functions as a key-value store capable of holding various data relevant to the block or protocol state.

Keys are consistently 2 bytes long, and the maximum size for a value is 64 bytes. The total size of the Extension section must not exceed 32,768 bytes (previously 16,384, updated post-EIP-38).

Certain key prefixes have predefined meanings:
*   **Parameters (`0x00` prefix)**: If the first byte of the key is `0x00`, the second byte identifies a specific blockchain parameter (e.g., block size limit, cost per byte). The value associated with this key represents the parameter's value. These are typically included only in blocks at the end of a voting epoch.
*   **Interlinks (`0x01` prefix)**: Keys starting with `0x01` are used for storing the [NiPoPoW interlinks vector](nipopows.md). The second byte indicates the level `k` of the link. The value contains the actual block ID (32 bytes) representing the link at that level.

Other key prefixes are available for future protocol extensions or application-specific data.
