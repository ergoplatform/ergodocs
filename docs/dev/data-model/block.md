---
tags:
  - Data Model
---
# Understanding Blocks in Ergo

Ergo operates on a block interval [set at two minutes](difficulty.md). Each block initially releases 75 Ergs, distributed among miners and the Treasury. This setup is valid for the first two years of operation. From the second year onwards, the release rate decreases by 3.0 Ergs, with a consistent reduction of an additional 3.0 Ergs every three months. This systematic decrease was initially programmed to stop emission eight years after Ergo's launch. However, with the introduction of [EIP-27](eip27.md), the emission period has been extended to approximately the year 2045.

## Block Structure in Ergo: The Extension Section

Ergo, like other blockchains such as Bitcoin and Ethereum, divides blocks into different sections for improved functionality. Unlike Bitcoin, which consists only of a block header and transactions, Ergo provides a more complex structure with additional sections:

* Header
* Transactions
* Extensions
* Proofs of UTXO transformation

The 'extension' section contains specific mandatory fields, including NIPoPoWs links (appearing once every 1,024 block epoch) and parameters for [miner voting](governance.md), such as the current block size. The extension section can also include arbitrary fields as needed.

This complex design allows various nodes and clients to download only the block sections relevant to them, significantly reducing storage, bandwidth, and CPU usage demands, thereby enhancing system efficiency.

## Additional Resources

Ergo enhances its flexibility and efficiency by supporting [Superblock Clients](log_space.md), providing an additional layer of adaptability to accommodate diverse user needs.