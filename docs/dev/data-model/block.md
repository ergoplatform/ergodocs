## Blocks in Ergo

The block interval in Ergo is set to 2 minutes, and each block releases 75 Ergs to be distributed among the miners and the Treasury during the first two years. However, starting from the second year, the emission rate decreases by 3.0 Ergs, and after that, it continues to drop every three months by an additional 3.0 Ergs. This decline was originally designed to stop emission eight years after the launch. However, with EIP-27, this emission period has been extended to approximately the year 2045.

## Extension Section

Like Bitcoin, Ethereum, and other blockchains, Ergo divides blocks into different sections. In Bitcoin, a block comprises just a block header and the transactions. In contrast, Ergo introduces extra sections that enable additional functionalities:

* Header
* Transactions
* Extensions
* Proofs of UTXO transformation

The 'extension' section contains certain mandatory fields, including links for NIPoPoWs (once every 1,024 block epoch) and parameters for miner voting, such as the current block size. It can also hold arbitrary fields.

This design allows various types of nodes and clients to download only those block sections that they need, thereby reducing the demands on storage, bandwidth, and CPU usage.

## Resources

- Ergo also supports [Superblock Clients](log_space.md), offering additional flexibility and efficiency.