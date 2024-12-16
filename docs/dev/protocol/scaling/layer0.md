# Layer 0: The Network Layer

Layer 0, also known as the *Network* or *Peer-to-Peer* (P2P) layer, forms the bedrock of decentralized communication within a blockchain network. It plays a pivotal role in facilitating the exchange of data and information across the network, allowing nodes to distribute and validate transactions, blocks, and other data types without the need for a centralized authority.

## Client Types 

In the context of scaling, the type of client used can significantly impact the performance and efficiency of a blockchain network. Ergo supports multiple types of clients, each offering different levels of security and resource requirements. These client types are designed to cater to various use cases and network conditions, thereby contributing to the overall scalability of the Ergo network. Here are the available client types:

- [**Full 'Archive' Node Mode**](full-node.md): This is the standard mode, akin to a full Bitcoin node. It stores all blocks from the genesis block onwards, checks the proofs of work, verifies the correctness of the linking structure, and maintains a copy of the entire UTXO set. This mode offers the highest level of security but requires significant storage resources, making it less scalable for devices with limited storage capacity.

- [**Pruned-Fullnode Mode**](pruned-full-node.md): This mode downloads all headers, validates proofs-of-work, and links structures. It then downloads a UTXO snapshot from peers and the full blocks succeeding it. By pruning unnecessary data, this mode improves storage efficiency, contributing to network scalability.

- [**Light-Fullnode Mode**](light-full-node.md): This mode only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting. It offers a balance between security and resource efficiency, making it a scalable choice for devices with moderate resources.

- [**Light-SPV Mode**](light-spv-node.md): A lightweight mode that enables users to verify transactions with a small sample of block headers. This mode requires the least resources, making it highly scalable for devices with limited storage and computational capabilities.

In addition to these, Ergo also supports **[Logarithmic space mining](logspace.md)**, which enables the existence of *light miners*. Similar to light clients, light miners can bootstrap using block headers without downloading the entire blockchain. This feature can be integrated into Ergo through a velvet (soft) fork, further enhancing the scalability of the network. 

## Sub Blocks

In the quest for Layer 0 (L0) scalability improvements, one of the most promising advancements is the introduction of "subblocks." These are essentially block candidates with lower proof-of-work difficulty, serving as temporary placeholders that facilitate faster transaction confirmations and optimize network bandwidth. For end-users, this translates into quicker, weakly confirmed transactions—often within 20 seconds—while also making better use of network resources. For a more in-depth look at weak blocks, their advantages, and their role in Ergo's scalability strategy, see this [page](subblocks.md).

## State Bloat Management

One of the key challenges in scaling blockchain networks is managing the growth of the state size, often referred to as 'state bloat'. As the state size increases, it becomes more resource-intensive to maintain and validate, which can limit the scalability of the network. Ergo addresses this issue with effective state bloat management strategies, ensuring that the network remains scalable without compromising on functionality. It achieves this through:

- Persistent updatable storage: This feature allows updates to be verified by a blockchain contract. However, only the digest of the authenticated data structure (along with a few additional bytes, less than 40) is stored in the UTXO set, regardless of the data set size.
- [Storage Rent](rent.md) Fee: Ergo uses a Storage Rent Fee to deter spam and recycle unused data bytes, also known as dust. This fee helps in reducing network pollution and encourages user activity.

## Miner-Adjustable Parameters

In the context of scaling, Ergo provides miners with the flexibility to modify certain parameters that can directly impact the network's scalability:

- **Block size:** Miners can adjust this parameter based on the observed decrease in full block validation time due to advancements in hardware and software. The current block size is set to `8MB`. A larger block size can accommodate more transactions, improving the network's throughput. However, it also requires more computational resources, which can affect the network's decentralization.
- **Transaction size:** As of node `4.0.23`, the transaction size limit for the mempool is `96kb`. Transactions exceeding this size can only be included manually by miners. This limit can be adjusted to balance the network's capacity to process transactions and the computational load on nodes.

For more details on how these parameters can be adjusted and their impact on the network's scalability, please refer to the [Governance](governance.md) section.


