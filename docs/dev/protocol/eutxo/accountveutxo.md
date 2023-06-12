---
tags:
  - UTXO
---
---
# UTXO vs Account: Understanding Ergo's Transaction Model

Ergo, like Bitcoin, utilizes the Unspent Transaction Outputs (UTXO) model instead of the Account model used in platforms like Ethereum. This documentation aims to explain the UTXO model, also known as the Box model, and highlight the advantages it brings.

## Account Balance and UTXO

In the Account model, a balance is a simple numerical value that increases or decreases with transactions. This is similar to real-world transactions where your bank balance changes when money is added or deducted. Transactions to and from an account directly affect the blockchain balance.

The UTXO model, introduced by Bitcoin, takes a different approach. It considers an individual's balance as a collection of unspent outputs, comparable to having multiple portions of bread dough. The total balance is the sum of these portions, or UTXOs. These UTXOs can be split or merged before being transferred to another address. Let's illustrate this with an example:

1. Alice has 100 units (100 ERG). She sends 75 units to Bob and keeps 25 units for herself.
2. Charlie has 250 units. He transfers 150 units to Bob and retains 100 units.
3. Bob splits 20 units from the 150 units received from Charlie and merges them with the 75 units received from Alice. He then sends a total of 205 units to Dave, keeping 20 units for himself.

Dave now owns 205 units previously owned by Charlie, Alice, and Bob. In the UTXO model, these units can be split and merged, but they maintain their original identity, unlike bread dough. The transaction history of these units can be traced back to when they were initially created.

### Advantages of UTXO

The UTXO model offers several benefits. Firstly, each UTXO is immutable, meaning it cannot be modified during a transaction like an account balance can be. The balance is determined by the transaction history since its creation.

This immutability provides a layer of simplicity and enhances security. A UTXO either exists in its expected form or it doesn't. In the Account model, verifying that an account is in the expected state can be challenging for developers and often leads to mistakes. The UTXO model also provides better support for off-chain protocols like sidechains and the Lightning Network.

While Account models simplify state storage, simplicity doesn't always equate to effectiveness. Ergo's extended UTXO model makes state transitions clearer and more explicit, reducing the chances of unexpected outcomes. Although it may require more effort to handle, it ultimately offers superior and straightforward security.