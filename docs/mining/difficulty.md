---
tags:
  - Difficulty Adjustment
  - Mining
  - Autolykos
  - EIP-37
  - Technical
---

# Understanding Difficulty Adjustment in Ergo

/// admonition | Tooling
    type: tip

Utilize the [Difficulty & Epoch Monitor](https://cds.oette.info/ergo_diff.htm) to predict upcoming difficulty adjustments.
///

Difficulty adjustment is a core mechanism in proof-of-work cryptocurrencies like Ergo. It ensures that blocks are added to the blockchain at a stable rate, aiming for a 120-second block interval in Ergo. This feature is critical for maintaining network security and fairness. Here we explore how Ergo's Autolykos protocol has been adapted over time to offer a robust difficulty adjustment mechanism.

## Autolykos Protocol: The Foundation for Difficulty Adjustment

Ergo's difficulty adjustment is grounded in its Autolykos protocol. Initially, Autolykos employed the linear least squares method for this purpose. This technique relied on historical data from the previous eight epochs (equivalent to 8,192 blocks) to predict future difficulty levels. Compared to Bitcoin's mechanism, it achieved a significantly lower error rate—1.9% as opposed to Bitcoin's 9.1%, as explained in [this paper](https://eprint.iacr.org/2017/731.pdf)

### Challenges and Vulnerabilities with the Original Difficulty Adjustment

While effective, the original Autolykos algorithm was vulnerable to rapid changes in hash rate. For example, during periods of super-linear growth in hash rate, such as the ETH merge, the system would experience severe difficulty spikes. On the flip side, periods of low activity could result in considerable drops in difficulty.

### EIP37: Refining Autolykos for Better Responsiveness

To address these vulnerabilities while retaining the strengths of the Autolykos protocol, Ergo introduced [Ergo Improvement Proposal 37 (EIP37)](eip37.md). This update made the difficulty adjustment mechanism more responsive by considering a shorter and more recent history of blocks. EIP37 didn't replace Autolykos but refined it, making it more resilient against sudden hash rate changes and adversarial disruptions.

With the adoption of EIP37, the Autolykos-based difficulty adjustment in Ergo has become more robust and adaptive. It can now better handle sudden and substantial fluctuations in the network's hash rate, making the network more secure and maintaining the 120-second block interval more consistently.

### The Future of Difficulty Adjustment

The need for performance statistics on the current Difficulty Adjustment Algorithm (DAA) has been expressed. Such data would allow for a comparison with other popular options in backtesting. The efforts of the development team in refining the DAA, both initially and currently, are acknowledged.

It's important to note that backtesting only shows how the DAA will perform against a static adversary. However, in reality, adversaries are adaptive, and all known DAAs are essentially of the same kind. A breakthrough would involve using an adaptive algorithm, although no specific ideas are currently available in this regard.

Finally, the question of whether any other DAA with the same epoch length would perform better has been raised. If not, studying the effects of a shorter epoch length could be a worthwhile topic of investigation.


## The Rationale Behind a 2-Minute Block Interval

Ergo's 2-minute target block interval is a carefully chosen parameter that offers a security cushion against a variety of potential issues and threats that could affect a peer-to-peer cryptocurrency network, especially one that supports complex smart contracts. This article elaborates on the reasons behind this design choice and its benefits.

### Providing Buffers in Network Activities

One of the often-overlooked advantages of the 2-minute block time is that it has provided essential buffers across various activities in the network. Specifically, it aids in decision-making processes related to the verifier's dilemma. In the world of blockchain mining, there is often a trade-off between adding more transactions to a new block and starting the mining process for that block as soon as possible. The 2-minute block time affords miners ample time to make these crucial decisions, thus enhancing the overall stability and integrity of the network.

### Resistance to Timewarp Attacks

A shorter block interval could make the network more susceptible to Timewarp attacks. This type of attack involves a malicious miner manipulating the timestamps of the blocks they mine, tricking the network into believing that more time has passed than actually has. Consequently, the network may lower the mining difficulty, making it easier for the attacker to mine subsequent blocks rapidly. The 2-minute block interval adds a layer of security against such difficulty manipulation attacks.

### Minimizing the Risk of Orphaned Blocks

Another benefit of a 2-minute interval is the reduction in the likelihood of orphaned blocks. These occur when two miners solve a block almost simultaneously, causing the network to accept one and leave the other as an 'orphan.' Orphaned blocks are not only a waste of computational resources but also pose a risk for double-spending attacks. The longer block time allows for more robust propagation and verification processes, thereby minimizing the risks associated with orphaned blocks.

### Efficiency in Epoch Length

Ergo's epoch length, which is approximately 4.2 hours assuming a normal block rate, is considerably shorter than Bitcoin's two-week epoch. This allows for quicker adjustments in network parameters and provides an efficient mechanism for maintaining network health.

## Introduction to 'Weak Blocks'

Another important layer of scalability and efficiency comes from the concept of "weak blocks," a feature aimed at improving both the transaction throughput (TPS) and the speed of transaction confirmations. Weak blocks act as block candidates with lower difficulty levels than standard blocks. They are propagated through the network along with new transactions, effectively optimizing network bandwidth usage. Weak blocks are not only beneficial for faster transaction confirmations but also hold the potential to facilitate quicker and more efficient sidechain operations. For a detailed explanation and further reading on how weak blocks contribute to Ergo's scalability, please refer to [weak-blocks.md](weak-blocks.md).
