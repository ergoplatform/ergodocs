---
tags:
  - UTXO
---
# Data Inputs 

Rather than forcing all transactions to destroy/spend all inputs as is the norm in historic UTXO-based Blockchains, what if we instead brought in the concept of *"read-only inputs"*? These would allow any transaction to reference any other box (UTXO) currently in the UTXO-set and read the data held in it without any of the problems normally inherent in eUTXO. 

This is exactly what data inputs are.

No smart contract execution occurs because the box is not being destroyed/spent. This means that a given UTXO can be read by every single tx in a block/slot in parallel as none consume the data, but all share a reference to it. Transaction fees decrease due to no contract execution and no extra output needing to be created. All further negatives are also addressed, making data inputs a clear design choice that all UTXO-based blockchains should implement.

See this introductory article, [Unlocking The Potential Of The UTXO Model](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/Unlocking%20The%20Potential%20Of%20The%20UTXO%20Model.md) for more information. There are also forum posts with more information; [Building A Portable And Reusable (PaR) UTXO dApp Standard](https://www.ergoforum.org/t/building-a-portable-and-reusable-par-utxo-dapp-standard/441) and [Data Inputs Semantics](https://www.ergoforum.org/t/data-inputs-semantics/654)