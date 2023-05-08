# Multi-Stage Protocols

While UTXOs scale better and are less error-prone, Ethereum's accounts allow for persistent storage and shared global context.* Multi-Stage Contracts* refers to a a technique using [*transaction trees*](tx-tree.md) that can emulate persistent storage in UTXO-based systems by linking several UTXOs containing small pieces of code to form a large multi-stage protocol. Adding _on-chain computations_ and making it possible to process parallelised actions on top of smart contracts. 

This enables functionality similar to Ethereum's accounts without the overhead of accounts. 

For more information see the *Multi-Stage Contracts in the UTXO Model* [(Paper)](https://storage.googleapis.com/ergo-cms-media/docs/paper_26.pdf) & [(Video Presentation)](https://www.youtube.com/watch?v=g3FlM_WOwBU)


## Examples

We demonstrate this via several examples which include contracts for a [A Rock Paper Scissors game with provable fairness](rock-paper-scissor.md), [Reversible Address with anti-theft features](reversible-address.md) and an [A full-featured ICO](ico.md). 

 
## Tutorials & Guides

- [Secure User Entry/Bootstrap Funneling In Multi Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)
- [Multi-Stage Protocol Off-Chain & On-Chain Development Workflow](https://www.ergoforum.org/t/multi-stage-protocol-off-chain-on-chain-development-workflow/269)
- [Secure User Entry/Bootstrap Funneling In Multi Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)


