---
tags:
  - History Pruning
  - Node
  - Storage
  - Configuration
---

# History Pruning


"History Pruning" is a feature in Ergo's blockchain that allows nodes to reduce the amount of stored historical block data, which can lead to a significant decrease in storage requirements. It's particularly useful for nodes running on devices with limited storage capacity.

## What is History Pruning?

The concept of pruning in blockchain technology involves the removal of some of the less relevant data on a node while keeping the information necessary for maintaining the network's security and functionality. In Ergo's case, this means removing certain block data but keeping all block headers.


## How does it work?

This is achieved using the [`ergo.node.blocksToKeep`](conf-node.md#blocks-to-keep) parameter. This parameter dictates the number of full blocks (i.e., blocks containing all transactions) that the node should store. Once this limit is reached, the node will start pruning older blocks, removing the full transactions but retaining the block headers.

## Importance of Block Headers

A block header in a blockchain is a portion of a block that contains metadata about the block, including the reference to the previous block (which establishes the chain's sequence), the difficulty target for the block, and a nonce value that is part of the Proof-of-Work system. The block header is crucial for the operation of the blockchain, as it helps maintain the integrity and continuity of the blockchain.

## Full-Node Security

By keeping the block headers, a node can still participate in verifying and validating new blocks and transactions, thus maintaining full-node security. Full-node security refers to the ability of a node to independently validate the rules of the network without relying on other nodes.
