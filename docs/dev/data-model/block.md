---
tags:
  - Data Model
---
# Understanding Blocks in Ergo

Ergo's blockchain operates on a block interval [set at two minutes](difficulty.md). Initially, each block releases 75 Ergs, which are distributed among miners and the Treasury. This setup is applicable for the first two years of operation. From the second year onwards, the release rate decreases by 3.0 Ergs, and this reduction of an additional 3.0 Ergs continues every three months. This systematic decrease was initially programmed to halt emission eight years post Ergo's launch. However, with the introduction of [EIP-27](eip27.md), the emission period has been extended to approximately the year 2045.

## Ergo Block Structure: The Extension Section

Ergo, similar to other blockchains like Bitcoin and Ethereum, segregates blocks into different sections for enhanced functionality. However, Ergo's structure is more complex than Bitcoin's, which only consists of a block header and transactions. Ergo's structure includes additional sections:

* Header
* Transactions
* Extensions
* Proofs of UTXO transformation

The 'extension' section of Ergo's block structure contains specific mandatory fields, including NIPoPoWs links (which appear once every 1,024 block epoch) and parameters for [miner voting](governance.md), such as the current block size. The extension section can also include arbitrary fields as required.

This intricate design allows various nodes and clients to download only the block sections relevant to them, significantly reducing storage, bandwidth, and CPU usage demands, thereby enhancing system efficiency.

## Additional Resources

To further enhance its flexibility and efficiency, Ergo supports [Superblock Clients](log_space.md), providing an additional layer of adaptability to accommodate diverse user needs.
