# Ergo Storage Rent Fees

The [FeeSimulator.scala tool](https://github.com/ergoplatform/ergo/blob/master/src/test/scala/org/ergoplatform/tools/FeeSimulator.scala) offers a comprehensive means of simulating Ergo's storage rent fees. This tool aids in calculating the average byte size of a standard box based on the dimensions of two types of Pay-to-Public-Key (P2PK)-protected boxes: one containing only ergs and another containing an additional asset. Here's what the simulations reveal:

## Key Metrics

- **Average Size of a Standard Box**: 105 bytes
- **Storage Rent Fee**: 0.13125 ergs for a standard box
- **Projected Storage Rent**: Approximately 0.13 ergs every four years

## Connection to Transaction Fees

While Ergo doesn't mandate a minimum transaction fee on the protocol level, a crucial detail is that each box must contain a minimum value per byte, which currently stands at **360 nanoergs per byte**. Miners can collectively decide to alter this number within a `[0, 10,000]` nanoergs per byte range. The adjustment parameters are as follows:

- **Increment/Decrement Step**: 2 or -2
- **Per-Epoch Adjustment Rate**: 10 nanoergs per byte

> **Example**: Should a majority of miners opt to increase the default value during an epoch consisting of 1,024 blocks, the value for the ensuing epoch would be modified to 370 nanoergs per block.

For further details on how these fee adjustments are made, check out the [Governance section](governance.md).

This enables miners to consistently earn rewards from a fixed-size UTXO set over a four-year span. After that, the reward for each block becomes `perOutputFee * (numberOfBoxes / (4 * BlocksPerYear))`.

Given that Ergo's UTXO set size is in the same ballpark as Bitcoin's (~60 million), the potential block reward could look like this:


- `perOutputFee * (numberOfBoxes / (4 * BlocksPerYear))`
- 0.001 * (60,000,000 / (4 * ))
- **Estimated Block Reward** =  7.49 Ergs plus transaction fees

For an academic perspective on this topic, consult the research paper ["A Systematic Approach To Cryptocurrency Fees"](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf).

## Storage Rent Fee Collection

Every four years, miners can capitalize on the opportunity to collect a storage rent fee by respending and recreating a box. In doing so, all register states remain intact, barring R0 (which holds the monetary value) and R3 (containing the creation height, transaction ID, and output index where the box originated). Network voting determines the rent fee per byte, with the default set at **1,250,000 nanoergs/byte**. The adjustable range for this parameter is `[0…2,500,000]`.

## Further Reading on Storage Rent Potential

If you're keen on diving deeper into Ergo's potential storage rent gains, here are some community-contributed resources:

- [Exploring Ergo's Storage Rent Potential: Part 1](https://www.reddit.com/r/ergonauts/comments/tyymax/tracking_storage_rent_potential/)
- [Unlocking the Secrets of Ergo's Storage Rent: Part 2](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/)
- [A Continual Look at Ergo's Storage Rent Potential: Part 3](https://www.reddit.com/r/ergonauts/comments/13e8f8g/tracking_storage_rent_potential_3rd_ed/)