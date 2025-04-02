---
tags:
  - Logarithmic Space Mining
  - Mining
  - NIPoPoWs
  - Light Clients
---
# Mining in Logarithmic Space

Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) allow smart contracts to retain historical data, enabling new *light* miners to operate in an *online* mode. This concept, known as Logarithmic Space Mining, allows for the compilation of unnecessary parts of the blockchain data into the blockchain itself. New miners don't need to carry historical data, and as they continue to mine, they assist other light miners in bootstrapping. This eliminates the need to carry old historical data, allowing old miners to discard historical data for lighter mining. This approach makes the entire miner population abandon old blocks, enhancing the system's efficiency.

This protocol is the first to achieve *always secure*, *always succinct*, and *online* Non-Interactive Proofs of Proof-of-Work, all necessary components for a logarithmic space mining scheme.

In this [video](https://www.youtube.com/watch?v=s05ypkSC7gk), Dionysis Zindros provides a detailed explanation of what Non-Interactive Proofs of Proof-of-Work truly are. He also evaluates the operation, implementation, and impact of this primitive.

## Overview

Miners in Ergo, Bitcoin, or any other PoW consensus model must constantly maintain the blockchain. This not only uses computational resources but also storage resources to maintain all blockchain data from the genesis block.

A new miner might ask: Is it strictly necessary to download all the data from the genesis block? Why can't we download only the most relevant blocks to maintain the network?

The block headers of the blockchain should be sufficient to access the necessary data. [NIPoPoWs](https://NIPoPoWs.com/) can be integrated to form interlinked block header sets that will reduce historical data storage.

Miners should be able to efficiently access key blocks in the blockchain from the headers of the old blocks. Each new block must indicate all of the current networks. As new blocks are created, a set of new block headers can be enough to check for the current UTXO set. Since the new blocks contain the data of old stringed block header sets, it enables light mining by eliminating the need to download all the blockchain data.

## NIPoPoW Implementation

Instead of accessing all of the blocks, superblocks (or light-clients) are enough to verify all of the blocks. This is accomplished by maintaining the historical data of the blockchain through smart contracts. The introduction of these superblock clients on NIPoPoWs can be done via 'velvet' or soft forks, and after that "light" miners can bootstrap through "online" mining.

## Resources 

##### Articles

- [Mining in Logarithmic Space - IOHK](https://eprint.iacr.org/2021/623.pdf)

##### Videos
- [Ergoversary 20201 - Logarithmic Mining Update from Dionysis](https://www.youtube.com/watch?v=s05ypkSC7gk)
- [NIPoPoWs & Log-Space Mining – Ergo Cast Episode #5](https://ergocast.io/episode/NIPoPoWs-ergo-cast-episode-5/)
