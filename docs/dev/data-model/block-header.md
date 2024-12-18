# Block Header

The block header in Ergo serves as a concise summary of a block's critical information. It plays a vital role in maintaining the integrity and security of the blockchain. 

## Functions

* **Chain Synchronization:**  Headers enable efficient synchronization between nodes on the network. By exchanging and validating headers, nodes can quickly agree on the current state of the blockchain without downloading every full block.
* **Proof-of-Work Validation:** The header contains information necessary to verify the miner's Proof-of-Work (PoW) solution, ensuring that the block meets the network's difficulty requirements.
* **Block Integrity:**  Headers include hashes that link to other sections of the block (transactions, proofs, extension), guaranteeing the integrity of the entire block. Any tampering with the block's content would result in a mismatch of these hashes.

## Components

The `Header` class in  [Header.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/header/Header.scala) defines the structure of the block header. Here's an overview of the key fields:

* **version:**  Indicates the protocol version used to create the block. This allows for future upgrades and changes to the blockchain while maintaining backward compatibility.
* **parentId:**  The ID of the previous block in the blockchain. This links blocks together, forming a chain.
* **ADProofsRoot:** A cryptographic digest of the proofs that validate changes to the UTXO set (the record of unspent transaction outputs).
* **stateRoot:**  A digest representing the root of the Merkle tree that captures the state of the UTXO set after this block is applied.
* **transactionsRoot:** A digest of the Merkle root of all transactions included in the block.
* **timestamp:** The time when the block was created, as reported by the miner.
* **nBits:**  Represents the difficulty target for the block, determining how hard it was to mine.
* **height:** The block's height in the blockchain (genesis block has height 1).
* **extensionRoot:**  A digest of the Merkle root of the extension section, which can contain arbitrary data.
* **powSolution:** The solution to the Proof-of-Work puzzle, demonstrating that the miner expended the necessary computational effort.
* **votes:**  Votes cast by miners to signal preferences for changes to consensus parameters.
* **unparsedBytes:**  A field to accommodate future protocol upgrades, allowing for the inclusion of data not yet parsed by current versions.
* **sizeOpt:** An optional field storing the size of the header to optimize performance.


## Key Concepts

* **[Merkle Tree:](merkle-tree.md)** A data structure used extensively in blockchains to efficiently verify data integrity. It allows for quick verification that a particular piece of data is included in a larger set.
* **UTXO (Unspent Transaction Output) Set:** The record of all unspent transaction outputs on the blockchain, representing the current distribution of the cryptocurrency.
* **Proof-of-Work (PoW):** A consensus mechanism that requires miners to solve a computationally intensive puzzle to add blocks to the blockchain. This ensures the security and immutability of the chain.

