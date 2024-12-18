---
tags:
  - Blocks
---

# Understanding Blocks in Ergo

Ergo's blockchain operates on a block interval [set at two minutes](difficulty.md). Initially, each block released 75 ERG, which were distributed among miners and the EF Treasury. This setup applied for the first two years of operation. From the second year onwards, the release rate decreased by 3.0 ERGs, with this reduction continuing every three months. This systematic decrease was initially programmed to halt emission eight years post Ergo's launch. However, with the introduction of [EIP-27](eip27.md), the emission period has been extended to approximately the year 2045.

## Ergo Block Structure

Ergo, similar to other blockchains like Bitcoin and Ethereum, segregates blocks into different sections for enhanced functionality. However, Ergo's structure is more complex than Bitcoin's, which only consists of a block header and transactions. Ergo's structure includes additional sections:

1. **Header**: The header contains essential metadata about the block, including information necessary for synchronizing the chain and validating Proof-of-Work (PoW) accuracy. It also includes hashes that link to other sections of the block.
    - The `Header` class, which defines the structure of the block header, can be explored in the [Header.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/header/Header.scala) file on GitHub.

2. **Block Transactions**: This section consists of all the transactions included within the block. It plays a critical role in defining the state changes in the Ergo blockchain.
    - The transaction data structure is detailed in the [ErgoTransaction.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/mempool/ErgoTransaction.scala) file.

3. **ADProofs**: Also known as authenticated data proofs, these are associated with transactions in the corresponding Block Transactions section. ADProofs allow light clients to authenticate all transactions and compute a new root hash without downloading the entire block.
    - ADProofs are managed and structured within the [ADProofs.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/ADProofs.scala) file.

4. **Extension**: This section holds additional information that doesn't fit into the previous sections. It includes interlinks and the chain's current parameters when the extension belongs to a block at the end of a voting epoch.
    - For a detailed look at how the extension data is managed, refer to the [Extension.scala](https://github.com/ergoplatform/ergo/blob/master/ergo-core/src/main/scala/org/ergoplatform/modifiers/history/extension/Extension.scala) file.

### The Extension Section in Detail

The 'extension' section of Ergo's block structure contains specific mandatory fields, including NIPoPoWs links (which appear once every 1,024 block epoch) and parameters for [miner voting](governance.md), such as the current block size. The extension section can also include arbitrary fields as required.

The extension section serves as a key-value storage accommodating a diverse range of data. The key is consistently 2 bytes long, and the maximum size of a value is 64 bytes. The overall Extension size should not exceed 16,384 bytes.

Certain keys have predefined meanings:

- If the first byte of a key equals `0x00`, the second byte identifies the parameter, and the value determines the parameter's value.
- Another predefined key is used for storing the interlinks vector. In this case, the first byte of the key is `0x01`, the second one matches the index of the link in the vector, and the value contains the actual link (32 bytes) prefixed with the frequency it appears in the vector (1 byte).

This intricate design allows various nodes and clients to download only the block sections relevant to them, significantly reducing storage, bandwidth, and CPU usage demands, thereby enhancing system efficiency.

### Additional Resources

To further enhance its flexibility and efficiency, Ergo supports [Superblock Clients](log_space.md), providing an additional layer of adaptability to accommodate diverse user needs.

## Related Concepts: Ergo Modifiers

In Ergo's P2P protocol, blocks and transactions are referred to as "[Modifiers](modifiers.md)". Modifiers are transmitted between nodes as part of the network synchronization process. The Modifier Exchange process encompasses the protocols and systems in place to exchange this information efficiently and securely across the network.
