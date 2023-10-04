# Oracles on Ergo

Oracles form the critical infrastructure in a decentralized financial system, connecting off-chain data with on-chain transactions. They provide essential data feeds for various operations, from atomic swaps to more complex interactions like lending/borrowing and dynamic market-making. Yet, DeFi ecosystems are vulnerable to Flash Loan attacks due to centralized price oracle misinformation.

## Oracle Pools on Ergo

Ergo has pioneered [Oracle Pools](https://ergoplatform.org/en/blog/2020-08-31-ergos-oracle-pools-and-what-they-mean-for-the-ecosystem/) to sustain a resilient DeFi ecosystem. Utilizing the Extended UTXO (eUTXO) model and the powerful ErgoScript programming language, Ergo facilitates highly decentralized oracle networks. Oracle Pools serve as an abstraction layer over the Oracle data, allowing scalable benefits while managing trade-offs between cost and speed. An example of this is the operational [ERG/USD oracle pool](https://explorer.ergoplatform.com/en/oracle-pools-list) on the Ergo Blockchain.

External oracle data, when posted on-chain, must be precisely encoded within a transaction. Oracle pools, which consist of various interconnected components, require specific transactions to transition through the pool protocol's different stages. [Oracle Core](https://github.com/ergoplatform/oracle-core) handles these complex transactions, which include data posting and executing the on-chain oracle pool protocol (like data point averaging). It is packaged with the [Oracle Pool Bootstrap](https://github.com/ergoplatform/oracle-core/tree/master/oracle-pool-bootstrap) and a [Connector Library](https://github.com/ergoplatform/oracle-core/tree/master/connectors/connector-lib). You can refer to the [ada-usd-oracle](https://github.com/ergoplatform/oracle-core/blob/master/scripts/ada-usd-oracle/oracle-config.yaml) source for an illustration. For a comprehensive perspective, see this [overview](https://github.com/Emurgo/Emurgo-Research/blob/master/oracles/Oracle-Pools.md) by Robert Kornacki.


### Introduction to Oracle Pools V2

The following section delves into the Oracle Pools V2, an innovative upgrade to the existing Oracle Pool v1.0, as documented in [EIP16](https://github.com/ergoplatform/eips/blob/eip16/eip-0016.md). This proposed update is designed to resolve various drawbacks associated with the first version such as the generation of extensive dust, low rewards, complexity due to two types of pool boxes, and issues related to the non-transferability of oracle and ballot tokens.

Oracle Pools V2 offers a range of new features and improvements including a single pool address, an epoch counter, a compact pool box, a refresh box, token-based rewards, no separate funding process, reward accumulation, and transferability of oracle and ballot tokens.

For detailed steps on how to bootstrap an ERG/XAU pool on testnet with this new version, follow the guide [here](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md).

To gain a deeper understanding of these changes and how they enhance the overall performance of Oracle Pools, refer to the comprehensive [EIP-0023 Oracle pool 2.0](https://github.com/ergoplatform/eips/pull/41). The document provides an exhaustive comparison between versions v1.0 and v2.0, highlighting the significant advancements in the latter.

For further details, refer to [Oracles-V2](oracles-v2.md).

For an easy docker setup see [easy-ergo-oracle](https://github.com/reqlez/ergo-easy-oracle)

## Resources

### Forum Posts

- [Trustless Oracle Contracts](https://www.ergoforum.org/t/trustless-oracle-contracts/3793)
- [Shrimpcoin - The first shrimp-pinned stablecoin on Ergo](https://www.ergoforum.org/t/shrimpcoin-the-first-shrimp-pinned-stablecoin-on-ergo/1381) (Inactive)

### GitHub

- [eth/usd connector](https://github.com/Luivatra/oracle-core/tree/eth-connector)
- [Ergo oracles](https://github.com/sininen-taivas/ergo-oracle) | A command-line tool to launch oracles, with implementations for USD/ERG, EUR/ERG, BTC/ERG, AUG/ERG prices. [Forum topic with example](https://www.ergoforum.org/t/erg-usd-oracle-on-top-of-ergo/119).

### Articles

- [Chainlink Oracles vs. Ergo Oracle Pools](https://ergoplatform.org/en/blog/2021-04-27-chainlink-oracles-vs-ergo-oracle-pools/)
- [Oracle Pools - A New Oracle Model](https://www.ergoforum.org/t/oracle-pools-a-new-oracle-model/263)
- [Interoperability with Cardano Oracles](https://ergoplatform.org/en/blog/2020-11-09-first-steps-towards-interoperability-with-cardano-oracles/)
- [Ergo Blockchain: Oracle Pool Governance Update](https://curiaregiscrypto.medium.com/ergo-blockchain-oracle-pool-governance-update-d078d58571b0)
- [The Role of Ergo Oracles](https://veriumfellow.medium.com/oracle-special-4e36cfa6a852)

### The Delphi Project (Inactive)

The Delphi Project aimed to facilitate exploration, operation, and launching of decentralized oracles on the Ergo blockchain. 

- [Website](https://delphiproject.org/#)
- [Final Report](https://hackmd.io/@abchris/S1dHZcwyc)

