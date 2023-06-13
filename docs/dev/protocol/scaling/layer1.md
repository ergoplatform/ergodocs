# Layer 1 (On-chain)

Layer 1 signifies the bedrock protocol layer of a blockchain system. This base layer handles fundamental functions including transaction processing, consensus mechanisms, and the implementation of security protocols.


- **Mainnet 5.0 Activation:** The [*'Just in time costing'*](JITC.md) update introduced in Node V5 increased block capacity by approximately 5-10 times. Boosting the network's transaction processing capability and overall throughput.

## Future Research

### Sharding

Ergo's Layer 1 paves the way for enhancing scalability through techniques such as Sharding. 

**Sharding** segregates the blockchain database into smaller partitions known as 'shards.' Each shard is equipped with the functionality to independently process transactions and smart contracts. By facilitating the parallel processing of several transactions, this technique considerably enhances the scalability of a blockchain. While not currently integrated into Ergo, sharding represents a promising direction for future development.

For a more detailed study of sharding, consider the paper [*' On the Security and Performance of Blockchain Sharding'*](https://eprint.iacr.org/2021/1276). You can also explore this page on [sharding and atomic composability on Ergo](atomic-composability/#sharding-and-atomic-composability) for more context.

### Sub-Block Confirmation Protocols and Micro Blocks

Another key aspect of Ergo's scalability comes from its *extension sections* within blocks, which can house **mandatory and arbitrary key-value data**. Specific anchors embedded in these sections enable the creation of micro blocks reminiscent of the Bitcoin-NG model. Furthermore, it becomes possible to generate Aspen-style service chains or generic sidechains through velvet or soft forks.

Platforms like [Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) and [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf) exhibit Micro blocks and Sub-block confirmation protocols. By leveraging Ergo's *extension sections*, these strategies can significantly increase the blockchain's throughput. Micro blocks allow for quicker block generation times, thereby enhancing transaction throughput.

As of 2023, these topics continue to stimulate intense research. For a deeper dive, consider the paper *[Flux: Revisiting Near Blocks for Proof-of-Work Blockchains](https://eprint.iacr.org/2018/415.pdf)*.