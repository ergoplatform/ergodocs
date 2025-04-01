---
tags:
  - UTXO
  - eUTXO
---

# Extending the Power of the UTXO Model


Ergo utilizes the **Extended UTXO (eUTXO) model**, based on Bitcoin's original UTXO model but with enhanced capabilities that enable more expressive [smart contracts](ergoscript.md). This section explores the advantages and features of eUTXO.

## The Benefits of UTXO

The choice to build upon the UTXO model brings several significant advantages to Ergo:

- **[Privacy](zkp.md)**: UTXOs being one-time objects allow for formalized privacy measures, enhancing user confidentiality.
- **[Scalability](scaling.md)**: UTXO's inherent design supports parallel transaction processing, making it simpler to scale the network. Additionally, UTXOs are more compatible with stateless client solutions like [NIPoPoWs](nipopows.md).
- **[Interoperability](use-cases-overview.md#infrastructure)**: UTXOs are well-suited for [off-chain](off-chain.md) and [sidechain](sidechains.md) protocols, enabling seamless integration with various solutions beyond the main chain.
- **Transaction Cost Predictability**: In Ergo, the on-chain action is primarily focused on validating smart contracts, resulting in significantly lower [transaction costs](min-fee.md). Moreover, the transaction costs are predictable, eliminating the need for gas-like mechanisms found in other platforms.

By leveraging the advantages of UTXO and extending its capabilities with eUTXO, Ergo provides a powerful and efficient platform for building and executing smart contracts.

## eUTXO and Smart Contracts

In the eUTXO model, Ergo allows [smart contracts](ergoscript.md) to utilize UTXOs as [data inputs](read-only-inputs.md) without modifying them. This means that [nodes](modes.md) primarily verify [transactions](transactions.md) rather than balances. In comparison, Ethereum's Account model requires nodes to check all accounts to validate the system.

By leveraging eUTXO, Ergo enables parallel computation and facilitates non-custodial [atomic swaps](atomic.md). This makes it easier to perform complex operations securely and efficiently.

Furthermore, Ergo's [Multi-Stage UTXO model](multi.md), as detailed in [this peer-reviewed paper](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf), enables the implementation of *Turing-complete smart contracts.* *(Note: [ErgoScript](ergoscript.md) itself is not Turing-complete by design for security, but the model allows for Turing-complete computations via multi-stage protocols).*

You can see a comparison between Ergo's eUTXO model and the Account-Based model [here](accountveutxo.md).



## Resources

### Articles

- [Learning Ergo 101 : eUTXO explained for human beings](https://dav009.medium.com/learning-ergo-101-blockchain-paradigm-eutxo-c90b0274cf5e) 
- [Off-chain logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/)
- [The UTXO Alliance Announcement](https://ergoplatform.org/en/blog/2021-09-26-the-utxo-alliance/)

### Documentation

- [The Extended UTXO Model - IOHK Research](https://iohk.io/en/research/library/papers/the-extended-utxo-model/)
- [Understanding the Extended UTXO model - docs.cardano](https://docs.cardano.org/learn/eutxo-explainer)


### Video

- [Ergo Blockchain Crash Course Part 1: eUTXO Model Review](https://www.youtube.com/watch?v=gGRAjK-VwJs&list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2&index=1)
- [DeCo EU Layman Class - Basics of eUTxO](https://www.youtube.com/watch?v=SAWeW6wajEw)
- [Interesting explanation on the eUTXO model and dapps built in it](https://youtu.be/Yt4Sg6rs80Q)
- [Blockchain Basics & Transactions, UTXO and Script Code](https://www.youtube.com/watch?v=zGDTt9Q3vyM)
