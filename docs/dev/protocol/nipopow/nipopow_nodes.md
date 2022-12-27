---
tags:
  - NIPoPoWs
---

# Light Nodes

**Light Clients** are essential when considering the hurdles cryptocurrency faces with mass adoption. Most crypto users do not have the necessary tools to run a full node. Running a full node means having a strong processor with high electricity wattage and more than a hundred gigabytes of memory to store the entire blockchain. Light clients are enable verification with a limited supply of data providers (nodes) and significantly reduce the amount of data storage and bandwidth needed for everyday users.

The use of light clients with the implementation of NIPoPoWs makes it possible to interact with the blockchain through block headers by using only a couple of kilobytes. Verifying whether a transaction happened on the blockchain becomes simplified. This enables users to interact with the blockchain using more efficient and convenient mobile wallets.

NIPoPoWs allow very efficient mobile wallets to be created. SPV wallets are already very lightweight compared to full nodes because they only require the download of block headers, not the whole blockchain. NIPoPoW wallets need to download only a small sample of block headers, around 250, when SPV clients need to download half a million block headers. The sample needed changes but doesn't grow much in size as the blockchain grows larger over the years, even after accumulated decades of data.

NIPoPoWs enable Ergo to build a mobile SPV client that requires around just 100KB of block headers to be downloaded.
