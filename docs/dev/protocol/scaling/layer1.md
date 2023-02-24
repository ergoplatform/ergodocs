# Layer 1 (On-chain)

Layer 1 refers to the underlying architecture or protocol that forms the foundation of the blockchain. Layer 1 is responsible for the basic functionality of the blockchain, including consensus mechanisms, transaction processing, and security features.

Ergo supports multiple on-chain scalability solutions, such as Sharding. Ergo blocks have *extension sections* with **mandatory and arbitrary key-value data**; by putting certain anchors there, it is possible to do BitcoinNG-style micro blocks, Aspen-like service chains or generic sidechains with just velvet or soft forks. 

## Sharding

**Sharding** as per [*' On the Security and Performance of Blockchain Sharding'*](https://eprint.iacr.org/2021/1276)

## Sub-block confirmation protocols

**Sub-block confirmation protocols**, as seen in [Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) and [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf) are an active topic for research in 2023. Also see *[Flux: Revisiting Near Blocks for Proof-of-Work Blockchains](https://eprint.iacr.org/2018/415.pdf)*