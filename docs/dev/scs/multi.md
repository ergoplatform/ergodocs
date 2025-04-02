---
tags:
  - Multi-Stage Protocols
---

# Multi-Stage Protocols

Unspent Transaction Outputs (UTXOs) are known for their scalability and reduced error rates. However, Ethereum's account model offers the advantages of persistent storage and a shared global context. *Multi-Stage Contracts* utilize a technique involving [*transaction trees*](tx-tree.md) to mimic persistent storage in UTXO-based systems. This is achieved by interlinking multiple UTXOs, each containing snippets of code, to create extensive multi-stage protocols. This approach introduces _on-chain computations_ and enables the **execution of parallel actions within smart contracts**.

This method offers functionality akin to Ethereum's accounts but without the associated overhead.

For additional insights, refer to the *Multi-Stage Contracts in the UTXO Model* [(Paper)](https://storage.googleapis.com/ergo-cms-media/docs/paper_26.pdf) and [(Video Presentation)](https://www.youtube.com/watch?v=g3FlM_WOwBU).

## Examples

The concept is illustrated through various examples, including contracts for a [Rock Paper Scissors game with provable fairness](rock-paper-scissor.md), a [Reversible Address with anti-theft features](reversible-address.md), and a [comprehensive ICO](ico.md).

## Tutorials & Guides

Explore the following resources for a deeper understanding of Multi-Stage Protocols:

- [Ensuring Secure User Entry and Bootstrap Funneling in Multi-Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)
- [Workflow for Multi-Stage Protocol Development: Off-Chain and On-Chain](https://www.ergoforum.org/t/multi-stage-protocol-off-chain-on-chain-development-workflow/269)

(Note: The third link is a duplicate and has been omitted to improve the page's clarity and usefulness.)
