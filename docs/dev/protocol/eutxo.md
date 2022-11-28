---
tags:
  - UTXO
---

# eUTXO 

## UTXO

UTXO provides superior 

- **Privacy**, as UTXOs are one-time objects making it possible to formalise privacy leaks.
- **Scalability**, as parallel transaction processing is more straightforward in UTXO. UTXOs are also more friendly to known stateless client solutions.
- **Interoperability**, as off-chain and sidechain protocols. One-time objects are more straightforward to work with from an off-chain point of view.
- **Transaction Cost Predictability**, where the only on-chain action is validating the smart contracts. As a result, the transaction cost is significantly lower, and most importantly, the transaction cost is predictable, eliminating the need for ‘gas.’

## eUTXO

- Ergo uses the so-called 'extended-UTXO' model (eUTXO), based on the original model that Bitcoin used, with a lot more power, while adding support for more expressive smart contracts. 
- This enables smart contracts to use UTXOs as data inputs without changing them. Therefore nodes are checking transactions rather than balances. In comparison, in Ethereum’s Account model, nodes check all accounts to validate the system.
- UTXO allows for parallel computation, and it’s easier to compute atomic swaps in a non-custodial manner. 
- Ergo's Multi-Stage UTXO model enables Turing-complete smart-contracts as demonstrated in [this peer-reviewed paper](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf). 

## Resources

### Articles

- [Learning Ergo 101 : eUTXO explained for human beings](https://dav009.medium.com/learning-ergo-101-blockchain-paradigm-eutxo-c90b0274cf5e) 
- [Off-chain logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/)
- [The UTXO Alliance Announcement](https://ergoplatform.org/en/blog/2021-09-26-the-utxo-alliance/)

### Documentation

- [The Extended UTXO Model - IOHK Research](https://iohk.io/en/research/library/papers/the-extended-utxo-model/)
- [Understanding the Extended UTXO model - docs.cardano](https://docs.cardano.org/plutus/eutxo-explainer)


### Video

- [Ergo Blockchain Crash Course Part 1: eUTXO Model Review](https://www.youtube.com/watch?v=gGRAjK-VwJs&list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2&index=1)
- [DeCo EU Layman Class - Basics of eUTxO](https://www.youtube.com/watch?v=SAWeW6wajEw)
- [Interesting explanation on the eUTXO model and dapps built in it](https://youtu.be/Yt4Sg6rs80Q)
- [Blockchain Basics & Transactions, UTXO and Script Code](https://www.youtube.com/watch?v=zGDTt9Q3vyM)
