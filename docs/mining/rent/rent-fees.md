# Storage Rent Fees

The [FeeSimulator.scala](https://github.com/ergoplatform/ergo/blob/master/src/test/scala/org/ergoplatform/tools/FeeSimulator.scala) tool is a valuable resource for simulating storage fees. It can be used to calculate the average size of a "standard box" based on the sizes of two P2PK-protected boxes, one holding ergs only and the other holding an additional asset. The results are as follows:

- **Standard Box size**: 105 bytes
- **Storage fee**: 0.13125 ergs for a standard box

This suggests that a standard box could incur a storage fee of approximately **0.13 ergs every four years**.

The connection between transaction fees and storage fees is a crucial aspect to consider, especially in terms of how miners decide to implement it. For example, if miners require a transaction to cover the byte size of input boxes, proportionate to their lifetimes, they will receive a constant reward from a fixed-size UTXO set for four years. After this period, the reward per block will be calculated as `perOutputFee * (numberOfBoxes / (4 * BlocksPerYear))`. Given that Ergo's UTXO set size is similar to Bitcoin's (~60 million), the estimated reward per block could be:

- 7.49 Erg + transaction fees

For more detailed information, refer to the original paper, "A Systematic Approach To Cryptocurrency Fees," available [here](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf).

## Fee Value Adjustments

It's important to note that a box cannot be created with fewer ergs than a minimum value per byte. The current default value is **360 nanoergs per byte**. Miners have the ability to vote to adjust this value within the range of `[0, 10000]` nanoergs per byte, with the capacity to increase by 2 or decrease by -2, and a per-epoch adjustment rate of 10 nanoergs/byte. 

> For example, if the majority of miners vote to increase the default value during an epoch of 1,024 blocks, the value for the next epoch will be adjusted to 370 nanoergs/block.

Every four years, **a miner has the opportunity to collect a storage rent fee by respending the box and recreating it, maintaining all register states** except for R0 (which holds the monetary value) and R3 (which holds the creation height and a reference to the transaction identifier and output index where the box was created). The storage rent fee is determined by network voting on the storage rent fee per byte value. The default value for this parameter is 1,250,000 nanoergs/byte. Miners can choose to change this within the `[0…2,500,000]` range by voting for 1 or -1, with a change step of 25,000.

For more information on fee adjustments, refer to the [Governance](governance.md) section.

## Modeling Storage Rent Potential 

An Ergo community member has created a series of insightful posts on r/ergonauts, providing a deep dive into Ergo's potential:

- [Part 1 - Tracking Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/tyymax/tracking_storage_rent_potential/)
- [Part 2 - Discovering Ergo's Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/)
- [Part 3 - Tracking Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/13e8f8g/tracking_storage_rent_potential_3rd_ed/)