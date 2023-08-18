---
tags:
  - NIPoPoWs
  - Mining
---

# Log-Space Mining

In Proof-of-Work (PoW) consensus models like Ergo and Bitcoin, miners are tasked with maintaining the blockchain. This process not only consumes computational resources but also requires storage resources to keep all blockchain data from the genesis block.

A common question for new miners is: Is it necessary to download all the data from the genesis block? Can't we just download the most relevant blocks to maintain the network?

The answer lies in the block headers of the blockchain. These headers should provide sufficient data access. By integrating [NIPoPoWs](https://NIPoPoWs.com/) (Non-Interactive Proofs of Proof of Work), we can create interlinked block header sets, reducing the need for historical data storage.

Miners should be able to efficiently access key blocks in the blockchain from the headers of old blocks. Each new block encapsulates the state of the current network. As new blocks are created, a set of new block headers can verify the current UTXO set. Since new blocks contain data from old block header sets, it enables light mining by eliminating the need to download all blockchain data.

So, what's the goal of compiling old PoW history into a snapshot?

Let's denote **C** as old blocks and **K** as new blocks. The snapshot's size can grow when **K** (new blocks) are constant, and **C** (old blocks) increase linearly. However, it can also shrink depending on the smart contract applications. The issue of miners maintaining large data loads can be addressed by bootstrapping through NIPoPoWs.


**NIPoPoW Implementation**

Instead of accessing all blocks, superblocks (or light clients) are sufficient to verify all blocks. This is achieved by preserving the blockchain's historical data through smart contracts. The introduction of these superblock clients on NIPoPoWs can be done via 'velvet' or soft forks, allowing *"light"* miners to bootstrap through "online" mining.

NIPoPoWs enable smart contracts to preserve historical data, allowing new *"light"* miners to operate in an "online" fashion. This concept is the crux of Logarithmic Space Mining. Rather than storing all blockchain data locally on nodes, the unnecessary part can be compiled into the blockchain itself. New miners don't need to carry the historical data, and as they continue to mine, new *"light"* miners will assist other *"light"* miners in bootstrapping. There's no need to carry old historical data, and old miners can discard historical data for lighter mining. This is how the miner population can abandon old blocks and enhance system efficiency.



## NiPoPoWs Explained
- NiPoPoWs are a way of creating super light clients.
- Their primary benefit is reduced communication costs. 
- NiPoPoWs can be consumed by remote chains and smart contracts.
- Ergo blockchain is constructed to support NiPoPoWs through interconnected blocks.
  
### Underlying Theory:
1. In traditional blockchains, a node will inquire, download, and validate the entire blockchain.
2. Simplified Payment Verification (SPV) nodes only download block headers but still validate the proof of work.
3. In NiPoPoWs, super light clients are convinced of the validity of a proof of work without downloading the entire blockchain.

## Log-Space Mining: A New Concept
- This idea involves mining blocks on top of NiPoPoWs instead of regular chains.
- Potential for various sampling methods.
- Open area of research on how to generalize the op code and determine practicality.

## Interoperability Between Chains
- Cross-chain protocols can be enabled by NiPoPoWs.
- Value is increased across the entire blockchain ecosystem when chains can communicate and operate under a common standard.

## Challenges & Future Prospects
- Different chains, such as Litecoin, can potentially implement NiPoPoWs through different methods (hard fork, soft fork, velvet fork).
- The future may see a standard for cross-chain protocols, increasing the entire blockchain ecosystem's value.
  


## Conclusion
NiPoPoWs offer a promising approach to constructing super light clients and introduce potentials like Log-Space Mining. Their potential to enhance interoperability between chains could significantly advance the blockchain ecosystem. Stay tuned for more exciting updates and discussions in future ErgoCast episodes.



## Resources

In [NIPoPoWs & Log-Space Mining – Ergo Cast Episode #5](https://ergocast.io/episode/NIPoPoWs-ergo-cast-episode-5/), Dionysis Zindros provides a comprehensive overview of Non-Interactive Proofs of Proof-of-Work. Dionysis meticulously explains what Non-Interactive Proofs of Proof-of-Work are, their operation, implementation, and impact. Additionally, we reveal a new piece of research that has not been shared publicly yet: log-space mining.

This section is based on a [recently published](https://eprint.iacr.org/2021/623.pdf) article by IOHK. For more information, please see the following [video.](https://www.youtube.com/watch?v=s05ypkSC7gk)
