---
title: Proxy Contracts
description: Learn about proxy contracts, a smart contract pattern used on Ergo for secure dApp interactions.
tags:
  - dApp Development
  - EIP
  - Smart Contracts
---

# Proxy Contracts

Proxy contracts are a specific [smart contract pattern](smart-contracts-overview.md) used on Ergo. They act as intermediaries, allowing users to interact with decentralized applications (dApps) in a controlled and secure manner, especially in scenarios where direct wallet-dApp communication might be complex or limited.

## Origins and Purpose

The concept gained prominence with tools like the [Ergo Assembler](https://github.com/anon-real/ergo-assembler). This enabled early dApps such as [Ergo Auction House](https://ergoauctions.org/), [ErgoUtils](https://ergoutils.org/), and the [SigmaUSD web interface](https://sigmausd.io/#/) to function effectively even before the widespread availability of wallet connectors similar to Ethereum's MetaMask.

Proxy contracts essentially provide a secure "spending script" that users can send funds to. This script then interacts with the target dApp based on predefined rules, ensuring the user's funds are only used as intended for that specific dApp interaction.

## Evolution and Security

Over time, the design of proxy contracts has evolved to address potential vulnerabilities discovered through real-world use, particularly highlighted by incidents involving dApps like [SigmaUSD](https://sigmausd.io/#/).

## Key Design Principles

When designing or interacting with proxy contracts, developers and users should prioritize security:

*   **Fund Safety:** The contract logic must rigorously prevent the dApp developer, the proxy contract creator, or any third party from misappropriating the user's funds. The contract should only allow spending according to the dApp's intended logic and the user's explicit action.
*   **dApp Integrity:** The proxy contract should not introduce new attack vectors. It must protect against manipulation that could compromise the underlying dApp's state or logic (e.g., preventing replay attacks or unexpected state changes).

## Further Information

For a detailed technical specification and discussion on proxy contracts, refer to the official Ergo Improvement Proposal:

*   [EIP-0017: Proxy Contracts](https://github.com/ergoplatform/eips/blob/master/eip-0017.md)
