---
tags:
- Sharding
- Sub Block Confirmation Protocols
- Microblocks
---

# Layer 1 (On-chain) Scalability in Ergo

Layer 1 refers to the foundational protocol layer of a blockchain system. It handles core functions such as transaction processing, consensus mechanisms, and security protocols. Ergo's Layer 1 has been designed with scalability in mind, incorporating features that enhance transaction processing capacity and overall throughput.

## Mainnet 5.0 Activation

The [*'Just in time costing'*](jitc.md) update introduced in Node V5 has significantly increased Ergo's block capacity. This update has boosted the network's transaction processing capability by approximately 5-10 times.

## Future Research Directions

Ergo's Layer 1 also lays the groundwork for future scalability enhancements through techniques such as Sharding and the implementation of Sub-Block Confirmation Protocols and Microblocks.

### Sharding

**Sharding** is a technique that divides the blockchain database into smaller partitions, known as 'shards.' Each shard can independently process transactions and smart contracts, enabling parallel transaction processing and significantly enhancing blockchain scalability. While not currently integrated into Ergo, sharding represents a promising direction for future development.

For a more detailed study of sharding, consider the paper [*' On the Security and Performance of Blockchain Sharding'*](https://eprint.iacr.org/2021/1276). You can also explore this page on [sharding and atomic composability on Ergo](../atomic-composability/#sharding-and-atomic-composability) for more context.

### Sub-Block Confirmation Protocols and Microblocks

Ergo's scalability is further enhanced by its *extension sections* within blocks, which can contain **mandatory and arbitrary key-value data**. Specific anchors embedded in these sections enable the creation of microblocks, similar to the Bitcoin-NG model. Furthermore, it becomes possible to generate Aspen-style service chains or generic sidechains through velvet or soft forks.

Platforms like [Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) and [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf) exhibit Microblocks and Sub-block confirmation protocols. By leveraging Ergo's *extension sections*, these strategies can significantly increase the blockchain's throughput. Microblocks allow for quicker block generation times, thereby enhancing transaction throughput.

As of 2023, these topics continue to stimulate intense research. For a deeper dive, consider the paper *[Flux: Revisiting Near Blocks for Proof-of-Work Blockchains](https://eprint.iacr.org/2018/415.pdf)*.