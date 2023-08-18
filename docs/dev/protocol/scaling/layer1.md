---
tags:
- Sharding
- Sub Block Confirmation Protocols
- Microblocks
---

# Layer 1: On-chain Scalability in Ergo

Layer 1, the foundational protocol layer of a blockchain system, is responsible for core functions such as transaction processing, consensus mechanisms, and security protocols. Ergo's Layer 1 is designed with a focus on scalability, incorporating features that boost transaction processing capacity and overall throughput.

## Mainnet 5.0 Activation and its Impact

The introduction of the [*'Just in time costing'*](jitc.md) update in Node V5 has led to a substantial increase in Ergo's block capacity. This enhancement has amplified the network's transaction processing capability by an estimated 5-10 times.

## Future Scalability Enhancements

Ergo's Layer 1 also sets the stage for potential scalability improvements through techniques such as Sharding, and the implementation of Sub-Block Confirmation Protocols and Microblocks.

### Sharding

**Sharding** is a scalability technique that partitions the blockchain database into smaller segments, known as 'shards.' Each shard can process transactions and smart contracts independently, enabling parallel transaction processing and significantly boosting blockchain scalability. Although not currently integrated into Ergo, sharding is a promising area for future development.

For an in-depth understanding of sharding, refer to the paper [*' On the Security and Performance of Blockchain Sharding'*](https://eprint.iacr.org/2021/1276). For additional context, visit this page on [sharding and atomic composability on Ergo](../atomic-composability/#sharding-and-atomic-composability).

### Sub-Block Confirmation Protocols and Microblocks

Ergo's scalability is further augmented by its *extension sections* within blocks, which can contain **mandatory and arbitrary key-value data**. Specific anchors embedded in these sections facilitate the creation of microblocks, akin to the Bitcoin-NG model. Additionally, it opens up the possibility to generate Aspen-style service chains or generic sidechains through velvet or soft forks.

Platforms such as [Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) and [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf) demonstrate Microblocks and Sub-block confirmation protocols. By utilizing Ergo's *extension sections*, these strategies can markedly enhance the blockchain's throughput. Microblocks enable faster block generation times, thereby improving transaction throughput.

These topics continue to be the focus of intense research as of 2023. For a comprehensive understanding, refer to the paper *[Flux: Revisiting Near Blocks for Proof-of-Work Blockchains](https://eprint.iacr.org/2018/415.pdf)*.
