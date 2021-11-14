# Blocks

The Ergo block interval is 2 minutes and for the first 2 years, each block will release a total of 75 Ergs to be shared between the miners and the Treasury (Treasury discussed below). But starting at year 2, the rate of emission will fall by 3.0 Ergs and thereafter further decline every 3 months by an additional 3.0 Ergs, which will result in an end to emission 8 years after launch.

## Extension Section

In Ergo, just like Bitcoin, Ethereum, and other blockchains, blocks are broken into sections. In Bitcoin, there's simply a block header and the transactions themselves. But in Ergo, we have some extra sections that enable new functionality:

* Header
* Transactions
* Extensions
* Proofs of UTXO transformation

The 'extension' section contains certain mandatory fields (including links for NiPoPoW, once per 1,024 block epoch) and parameters for miner voting, such as current block size. It can also contain arbitrary fields.

**What this means in practice is that different types of nodes and clients can download only those sections of the blocks they need – reducing the demands for storage, bandwidth, and CPU cycles.**


## Mining in Log-Space
- [Mining in Logarithmic Space: NIPoPoW Power and Ergo](https://ergoplatform.org/en/blog/2021-07-19-mining-in-logarithmic-space-nipopow-power-and-ergo/)