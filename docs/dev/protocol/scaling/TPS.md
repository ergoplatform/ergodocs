# Evaluating Transaction Speed

Transaction speed, often referred to as Transactions Per Second (TPS), is a crucial performance indicator for blockchains. This metric measures the rate at which a blockchain can process transactions, quantified in transactions per second.

## TPS Values for Well-Known Blockchains

Here are the estimated TPS values for a few prominent blockchains:

- **Bitcoin (BTC)**: Approximately 7 TPS (Gobbel, 2017).
- **Ethereum (ETH)**: Approximately 15 TPS (Clincy et al., 2019)
- **Ripple (XRP)**: Approximately 1500 TPS (Clincy et al., 2019)
- **Cardano (ADA)**: Approximately 7 TPS (Around 250 in controlled tests) (Stamoulis, 2021).
- **Polkadot (DOT)**: Approximately 1500 TPS (Hiemstra et al., 2021)

## Ergo's Transaction Speed

However, the standard TPS metric provides only a partial view of Ergo's capabilities. It's not just the quantity of transactions that counts; the transaction weight and the computational cost limit per block also play critical roles. These factors are influenced by various dynamic elements, including the network's size and the hardware resources of miners.

With [Node v5](jitc.md) already live, Ergo's raw TPS stands at approximately **47.5 transactions/second**, and there's potential for further optimization. For a comprehensive technical understanding of how this figure is calculated, refer to [this report](https://github.com/ergoplatform/ergo/blob/d3d95e19b37c83b98de13bdf71d6d62b398e8f0d/metrics/Report.ipynb).

## Extended Unspent Transaction Output (eUTXO) Model

Ergo's transaction management system incorporates the Extended Unspent Transaction Output (eUTXO) model, which surpasses the traditional UTXO model in terms of efficiency and versatility. This model supports multiple outputs in a transaction, each possibly carrying different tokens. Further, Ergo can accommodate complex DeFi transactions, fostering a wide array of DeFi applications within the network. By processing multiple token types per transaction output and enabling the concurrent execution of complex transactions within a block, Ergo effectively enhances its blockchain's performance and scalability.

In scaling Ergo, the goal must be to boost TPS while maintaining the core assumptions and guarantees typically associated with blockchain technology.