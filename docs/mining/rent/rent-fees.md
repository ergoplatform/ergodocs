# Storage Rent Fees

[FeeSimulator.scala](https://github.com/ergoplatform/ergo/blob/master/src/test/scala/org/ergoplatform/tools/FeeSimulator.scala) is useful for outputting simulations related to storage fees. We can use it to calculate the average size of a "standard box" based on the sizes of two P2PK-protected boxes, one holding ergs only and the other holding an additional asset. The results are as follows:

- **Standard Box size**: 105 bytes
- **Storage fee**: 0.13125 ergs for a standard box

This implies that a standard box could incur a storage fee of approximately **0.13 ergs every four years**.

How miners decide to connect transaction fees to storage fees is an important aspect to consider. For instance, if miners demand a transaction to cover the byte size of input boxes, proportionate to their lifetimes, miners will receive a constant reward from a fixed-size UTXO set for four years. Following this period, the reward per block will be worked out as `perOutputFee * (numberOfBoxes / (4 * BlocksPerYear))`. Considering Ergo's UTXO set size is akin to Bitcoin's (~60 million), the estimated reward per block could be:

- 7.49 Erg + transaction fees

The original paper, "A Systematic Approach To Cryptocurrency Fees," can be accessed [here](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf).

## Fee Value Adjustments

It is worth noting that a box cannot be created with fewer ergs than a minimum value per byte. The default value currently stands at **360 nanoergs per byte**. Miners can vote to adjust this value within the range of `[0, 10000]` nanoergs per byte, with the capacity to increase by 2 or decrease by -2, and a per-epoch adjustment rate of 10 nanoergs/byte. 

> For illustrative purposes, if most miners vote to increase the default value during an epoch of 1,024 blocks, the value for the ensuing epoch will be adjusted to 370 nanoergs/block.

Once every four years, **a miner has the opportunity to collect a storage rent fee by respending the box and recreating it, maintaining all register states** except for R0 (which holds the monetary value) and R3 (which holds the creation height and a reference to the transaction identifier and output index where the box was created). Consensus determined by network voting on the storage rent fee per byte value sets the storage rent fee. The default value for this parameter is 1,250,000 nanoergs/byte. Miners can opt to alter this within the `[0…2,500,000]` range by voting for 1 or -1, with a change step of 25,000.

Refer to the [Governance](governance.md) section for more details on fee adjustments.

## Modeling Storage Rent Potential 

An Ergo community member has created a series of informative posts on r/ergonauts. They provide an in-depth exploration of Ergo's potential:

- [Part 1 - Tracking Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/tyymax/tracking_storage_rent_potential/)
- [Part 2 - Discovering Ergo's Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/)
- [Part 3 - Tracking Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/13e8f8g/tracking_storage_rent_potential_3rd_ed/)