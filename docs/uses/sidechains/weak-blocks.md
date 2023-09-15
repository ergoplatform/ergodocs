# Weak Blocks

As of August 2023, lighter clients have seen considerable advancements with versions 5.0.12 and 5.0.13 of the reference client offering support for bootstrapping with UTXO set snapshots and NiPoPoWs. While Layer 0 (L0) optimizations continue to be a hot topic, there is an increasing demand for faster transaction confirmations.

Weak-blocks are block candidates in the Ergo blockchain that have a lower difficulty threshold compared to standard blocks. For end-users, the introduction of weak-blocks aims to significantly speed up transaction confirmations to around 20 seconds and better utilize network bandwidth, ultimately providing a more efficient and responsive user experience. This document delves into the technical details, advantages, and the strategic plan for implementing weak-blocks using sidechains in Ergo.

## The Scalability Dilemma

While there are many proposals claiming to improve scalability, such as switching to Proof-of-Stake or DAG structures, the real issue often boils down to two key areas:

1. **Propagation Efficiency**: How well transactions and blocks propagate through the peer-to-peer network.
2. **Network Load**: Optimizing the network so that it remains decentralized and efficient.

Proof-of-Work, while not requiring additional messages for block creation, still needs improvement in how blocks and transactions propagate through the network.

## Why Not Microblocks or Bitcoin-NG?

Bitcoin-NG was initially considered in Ergo's 2017 roadmap but later abandoned due to competing proposals. The principle behind Bitcoin-NG was to use microblocks to follow an empty PoW block, which serves merely as a leader election signal. Although microblocks can improve network utilization, alternative solutions like compact blocks offer similar results. Therefore, Ergo is considering the use of "weak-blocks" as an alternative.

## What are Weak-Blocks?

Weak-blocks are essentially block candidates with lower difficulty than a regular block. For instance, if a weak-block has 1/128th of a regular block's difficulty, we could expect one weak-block to be generated per second on average.

### Advantages

1. **Optimal Network Utilization**: Weak-blocks are sent around the network along with new transaction IDs, utilizing the network bandwidth optimally.
2. **Faster Confirmation**: A transaction could be considered weakly confirmed with fewer confirmations from the majority hashrate, in practical terms, under about 20 seconds.
3. **Incentivization**: Weak-blocks can commit to sidechains, making fast sidechains possible and providing miners with additional rewards.

## Sidechains

Sidechains allow for segregated, dedicated chains where specific tasks or applications can be run. This offloads the main Ergo chain, providing another avenue for scalability. Weak-blocks can commit to these sidechains, adding another layer of efficiency and speed to the Ergo ecosystem.

## Implementation Plan

- Use weak-blocks instead of microblocks for optimal network utilization and faster confirmations.
- Distribute weak-blocks in a cut-through way similar to other efficient block propagation techniques.
- Incentivize the reporting of weak-blocks by linking them to sidechain commitments.

## Conclusion

Weak-blocks and sidechains present an efficient approach to address some of the fundamental scalability issues in proof-of-work blockchains like Ergo. By focusing on these, Ergo aims to improve both the network efficiency and transaction confirmation speed without compromising decentralization.

## References

- [ergoforum: A Scalability Plan for Ergo ](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226/5)