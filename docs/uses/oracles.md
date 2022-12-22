# Oracles

Oracles are the backbone of a decentralized financial system. It connects off-chain data with the on-chain world. Normally, ETH has no info about the current market price. During a swap order in a decentralized exchange, a swap contract needs to call the data from various sources to obtain market price. Thus, oracles are the messengers of the crypto ecosystem. Not only in atomic swaps but also more complex interactions such as lending/borrowing assets or dynamic market-making need the data feeds provided by oracles. DeFi ecosystem suffered from Flash Loan attacks caused by [misinformation from centralized price oracles](https://insights.glassnode.com/defi-attacks-flash-loans-centralized-price-oracles/).

## Oracle Pools
Ergo developed [Oracle Pools](https://ergoplatform.org/en/blog/2020-08-31-ergos-oracle-pools-and-what-they-mean-for-the-ecosystem/) to maintain a robust DeFi ecosystem. Because of the eUTXO design and its rich programming language, ErgoScript, oracle networks can be more decentralized. In the extended UTXO model, we have a lot of flexibility and power available to build new protocols. This can be utilized to construct oracle datapoint hierarchies of confidence. In short, they are an abstraction above oracle pools, allowing us to scale the benefits of oracle pools as much as we desire at the cost of price and speed. [ERG/USD oracle pool](https://explorer.ergoplatform.com/en/oracle-pools-list) is running on Ergo Blockchain.

When external oracle data is posted on-chain, it needs to be encoded in a very precise way within a transaction. Furthermore, oracle pools have a bunch of different moving parts which require transactions to be issued to move between the different stages of the pool protocol. [Oracle Core](https://github.com/ergoplatform/oracle-core) creates all of the complex transactions which post the data on-chain & run the oracle pool protocol on-chain (such as averaging data points). This comes bundled with [Oracle Pool Bootstrap](https://github.com/ergoplatform/oracle-core/tree/master/oracle-pool-bootstrap) and a [Connector Library](https://github.com/ergoplatform/oracle-core/tree/master/connectors/connector-lib). The [ada-usd-oracle](https://github.com/ergoplatform/oracle-core/blob/master/scripts/ada-usd-oracle/oracle-config.yaml) source can be seen here. 
See this [overview](https://github.com/Emurgo/Emurgo-Research/blob/master/oracles/Oracle-Pools.md) by Robert Kornacki.


### Oracle Pools V2

- [How to bootstrap an ERG/XAU pool on testnet](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md)

This is a proposed update to the oracle pool v1.0 currently deployed and documented in [EIP16](https://github.com/ergoplatform/eips/blob/eip16/eip-0016.md).

In order to motivate the changes proposed in this document, consider the drawbacks of Oracle pool v1.0:

1. Rewards generate a lot of dust
2. Current rewards are too low (related to 1)
3. There are two types of pool boxes. This makes dApps and update mechanism more complex
4. Oracle tokens are non-transferable, so oracles are locked permanently. The same goes for ballot tokens.

Oracle pool v2.0 aims to address the above. 

Below is a summary of the main new features in v2.0 and how it differs from v1.0.

- **Single pool address**: This version of the pool will have only one address, the *pool address*. 
- **Epoch counter**: Pool box will additionally store a counter that is incremented on each collection. This will allow more sophisticated dApps. 
- **Compact pool box**: Pool box is separated from the logic of pool management, which is captured instead in a **refresh** box. This makes the pool box very small for use in other dApps.
- **Refresh box**: The refresh box is used for collecting data-points.   
- **Reward in tokens**: The posting reward will be in the form of tokens instead of Ergs. These tokens can be redeemed separately, which is not part of the protocol.
    - The pool box emits such reward tokens.
- **No separate funding process**: The pool box emits only reward tokens and won't be handing out Ergs. Thus, there won't be a separate funding process required.
- **Reward accumulated**: We will not be creating a new box for rewarding each posting to prevent dust. Instead, the rewards will be accumulated directly in the oracle boxes. 
- **Oracle boxes spent in collection**: Because the rewards must be accumulated, the oracle boxes will be considered as inputs rather than data-inputs when collecting individual rates for averaging. 
    - These inputs will be spent, and a copy of the box with the reward will be created. 
    - This gives us the ability to accumulate rewards while keeping the transaction size similar to when using them as data-inputs in v1.0.
    - Additionally, this allows us to outsource part of the reward logic to the oracle boxes.
    - **Note:** The pool box will still be used as data input in other dApps.
- **Transferable oracle tokens**: Oracle tokens are free to be transferred between public keys.
- **Similar update mechanism**: We will have a similar update mechanism as in v1.0 (threshold number of ballot token holders must vote for an update).
- **Transferable ballot tokens**: Similar to oracle tokens, the ballot tokens are free to be transferred between public keys.


See [EIP-0023 Oracle pool 2.0](https://github.com/ergoplatform/eips/pull/41) for more information. 



## Resources

### Forum Posts

- [Trustless Oracle Contracts](https://www.ergoforum.org/t/trustless-oracle-contracts/3793)
- [Shrimpcoin - The first shrimp-pinned stablecoin on Ergo](https://www.ergoforum.org/t/shrimpcoin-the-first-shrimp-pinned-stablecoin-on-ergo/1381) (Inactive)


### GitHub

- [eth/usd connector](https://github.com/Luivatra/oracle-core/tree/eth-connector)
- [Ergo oracles](https://github.com/sininen-taivas/ergo-oracle) | simple command-line tool to launch oracles. Inbuilt implementations for USD/ERG, EUR/ERG, BTC/ERG, AUG/ERG (gold) prices delivery. 
  - See also a [forum topic with example](https://www.ergoforum.org/t/erg-usd-oracle-on-top-of-ergo/119)



### Articles

- [Chainlink Oracles vs. Ergo Oracle Pools](https://ergoplatform.org/en/blog/2021-04-27-chainlink-oracles-vs-ergo-oracle-pools/)
- [Oracle Pools - A New Oracle Model](https://www.ergoforum.org/t/oracle-pools-a-new-oracle-model/263)
- [First steps towards interoperability with Cardano oracles](https://ergoplatform.org/en/blog/2020-11-09-first-steps-towards-interoperability-with-cardano-oracles/)
- [Ergo Blockchain: Oracle Pool Governance Update](https://curiaregiscrypto.medium.com/ergo-blockchain-oracle-pool-governance-update-d078d58571b0)
- [The role of Ergo Oracles](https://veriumfellow.medium.com/oracle-special-4e36cfa6a852)

### The Delphi Project (Inactive)

The Delphi Project aims to help anyone explore, run, and launch decentralized oracles on the Ergo blockchain. 

- [Website](https://delphiproject.org/#)
- [Final Report](https://hackmd.io/@abchris/S1dHZcwyc)

