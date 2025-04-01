---
tags:
  - Oracle Core
  - Oracles
  - Off-chain
---

# Oracle Core

[Oracle Core](https://github.com/ergoplatform/oracle-core#roadmap) is a crucial off-chain component run by oracles, who form an integral part of an oracle pool. This core component provides a user-friendly HTTP API interface that allows for reading the current protocol state and submitting data points. Once a data point is submitted, the Oracle Core takes over the heavy lifting. It automatically generates the required transaction, posts it, and performs any other necessary actions for the protocol to run smoothly. This automation significantly reduces the workload for the oracle operator, allowing them to participate in the oracle pool protocol without any additional effort.

To function correctly, the Oracle Core requires access to a full node wallet. This access enables it to create transactions and perform UTXO-set scanning. Each Oracle Core is designed to work exclusively with a single oracle pool. If an operator runs multiple oracles across various oracle pools, they can still use a single full node. However, they will need to run several instances of Oracle Cores, each set with different API ports.

The current Oracle Core is built to run the protocol specified in the [EIP-0023 PR](https://github.com/ergoplatform/eips/pull/41). This protocol outlines the proposed upgrade to Oracle Pool version 1.0, addressing several limitations and introducing new features for improved functionality. These enhancements include a single pool address, epoch counter, compact pool box, reward in tokens, and transferable oracle and ballot tokens, among others. For a detailed technical description and further understanding, refer to [EIP-0023 Oracle Pool 2.0](https://github.com/ergoplatform/eips/pull/41).

For those interested in setting up an ERG/XAU oracle pool in a testnet environment, we have created a comprehensive guide to walk you through the process. The guide provides detailed instructions, making it easy even for those relatively new to the field. Follow the link to access our [Bootstrap an ERG/XAU pool on testnet guide](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md).
