---
tags:
  - UTXO
---

# eUTXO 

Ergo has a similar approach to Cardano’s eUTXO with its own Multi-Stage UTXO model that introduces the concept of *UTXO chains* and allows chaining together smart contracts of arbitrary complexity. 

UTXO provides superior 

- **Privacy**, as UTXOs are one-time objects making it possible to formalise privacy leaks.
- **Scalability**, as parallel transaction processing is more straightforward in UTXO. UTXOs are also more friendly to known stateless client solutions.
- **Interoperability**, as off-chain and sidechain protocols. One-time objects are more straightforward to work with from an off-chain point of view.
- **Transaction Cost Predictability**, where the only on-chain action is validating the smart contracts. As a result, the transaction cost is significantly lower, and most importantly, the transaction cost is predictable, eliminating the need for ‘gas.’

Extended UTXO systems enable **Turing complete** smart contracts. This is a novel innovation that allows the latest generation of blockchains to reclaim the original model that Bitcoin used, but with a lot more power, while adding support for more expressive smart contracts. 


A good introductory article can be found [here](https://dav009.medium.com/learning-ergo-101-blockchain-paradigm-eutxo-c90b0274cf5e) or [DeCo EU Layman Class - Basics of eUTxO](https://www.youtube.com/watch?v=SAWeW6wajEw)

## ErgoScript

ErgoScript is built considering Bitcoin’s security and privacy to make all kinds of complex financial contracts accessible. In comparison, Bitcoin’s design doesn’t allow loops or building any complex smart contracts on top of it. ErgoScript allows for self-replication; therefore, we can use it to create Turing-Complete processes in a blockchain.

Ergo extended Bitcoin’s UTXO model by introducing a readable UTXO design. This enables smart contracts to use UTXOs as data inputs without changing them. Therefore nodes are checking transactions rather than balances. In comparison, in Ethereum’s Account model, nodes check all accounts to validate the system.

UTXO allows for parallel computation, and it’s easier to compute atomic swaps in a non-custodial manner. 






## Resources

- [Off-chain logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/)
- [Interesting explanation on the eUTXO model and dapps built in it](https://youtu.be/Yt4Sg6rs80Q)
- [The Extended UTXO Model - IOHK Research](https://iohk.io/en/research/library/papers/the-extended-utxo-model/)
- [Understanding the Extended UTXO model - docs.cardano](https://docs.cardano.org/plutus/eutxo-explainer)
- [5. Blockchain Basics & Transactions, UTXO and Script Code](https://www.youtube.com/watch?v=zGDTt9Q3vyM)
- [The UTXO Alliance Announcement](https://ergoplatform.org/en/blog/2021-09-26-the-utxo-alliance/)
