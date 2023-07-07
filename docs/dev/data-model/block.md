---
tags:
  - Data Model
---
# Understanding Blocks in Ergo

Ergo operates with a block interval [set at two minutes](difficulty.md). Each block initially releases 75 Ergs, which are distributed among the miners and the Treasury. This arrangement is applicable for the first two years of operation. Starting from the second year, the release rate undergoes a decrease by 3.0 Ergs, followed by a consistent reduction of an additional 3.0 Ergs every three months. This systematic decrease was initially programmed to halt the emission eight years after Ergo's launch. However, following the introduction of [EIP-27](eip27.md), the emission period has been extended up until approximately the year 2045.

## Understanding the Block Structure: The Extension Section

Similar to other blockchains such as Bitcoin and Ethereum, Ergo divides blocks into different sections for better functionality. While Bitcoin comprises simply a block header and transactions, Ergo offers a more complex structure with additional sections:

* Header
* Transactions
* Extensions
* Proofs of UTXO transformation

Among these, the 'extension' section carries specific obligatory fields. These include NIPoPoWs links (appearing once every 1,024 block epoch) and parameters that allow for [miner voting](governance.md), such as the current block size. The extension section can also accommodate arbitrary fields as per requirement.

The essence of this intricate design is to allow diverse nodes and clients to download only those block sections which are relevant to them. This strategy significantly curtails the storage, bandwidth, and CPU usage demands, making the system more efficient.

## Useful Resources

Ergo further bolsters its flexibility and efficiency by supporting [Superblock Clients](log_space.md). This feature offers an additional layer of adaptability to meet varying user requirements.
