# Understanding Transaction Speed in Blockchains

The speed of transactions, commonly known as Transactions Per Second (TPS), is a vital performance metric for blockchains. It quantifies the capacity of a blockchain to process transactions, expressed in transactions per second.

## Comparative TPS Values for Renowned Blockchains

To provide a perspective, here are the estimated TPS values for some of the leading blockchains:

- **Bitcoin (BTC)**: Roughly 7 TPS (Gobbel, 2017).
- **Ethereum (ETH)**: Roughly 15 TPS (Clincy et al., 2019)
- **Ripple (XRP)**: Roughly 1500 TPS (Clincy et al., 2019)
- **Cardano (ADA)**: Roughly 7 TPS (Can reach up to 250 in controlled tests) (Stamoulis, 2021).
- **Polkadot (DOT)**: Roughly 1500 TPS (Hiemstra et al., 2021)

However, the conventional TPS metric only offers a glimpse into Ergo's true potential. It's not merely about the number of transactions; the weight of the transaction and the computational cost limit per block are equally important. These aspects are shaped by several dynamic factors, including the size of the network and the hardware resources available to miners.

With the [Node v5](jitc.md) already operational, Ergo's raw TPS is approximately **47.5 transactions/second**, with room for further enhancements. For an in-depth technical understanding of how this figure is derived, please refer to [this report](https://github.com/ergoplatform/ergo/blob/d3d95e19b37c83b98de13bdf71d6d62b398e8f0d/metrics/Report.ipynb).

## The Extended Unspent Transaction Output (eUTXO) Model Advantage

Ergo's transaction management system leverages the Extended Unspent Transaction Output (eUTXO) model, which outperforms the traditional UTXO model in terms of efficiency and flexibility. This model allows for multiple outputs in a single transaction, each potentially carrying different tokens. Moreover, Ergo is capable of handling complex DeFi transactions, thereby enabling a broad spectrum of DeFi applications within the network. By processing multiple token types per transaction output and facilitating the simultaneous execution of complex transactions within a block, Ergo significantly boosts its blockchain's performance and scalability.

The primary objective in scaling Ergo is to enhance TPS without compromising the fundamental principles and assurances typically linked with blockchain technology.
