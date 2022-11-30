# Multi-Stage Contracts

Multi-stage contracts refer to smart contracts that operate on a *stateful* level. Because Ergo uses the *UTXO model* (first seen in Bitcoin), it is possible to process parallelized actions on top of smart contracts. Multi-Stage Contracts provide an extension to Bitcoin’s UTXO model with on-chain computations. It’s a complex design that aims for *infinite scalability*; therefore, it creates more space to build complex solutions that introduce the concept of *UTXO chains*.


We describe how to emulate persistent storage in UTXO based systems using a technique called [transaction trees](tx-tree.md). This allows us to emulate the functionality of account-based systems such as Ethereum without the overhead of accounts. 

## Examples

- Reversible Address with anti-theft features
- A Rock Paper Scissors game with provable fairness
- A full featured ICO that accepts funding in ERGs
 
## Tutorials & Guides
- [Secure User Entry/Bootstrap Funneling In Multi Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)
- [Multi-Stage Protocol Off-Chain & On-Chain Development Workflow](https://www.ergoforum.org/t/multi-stage-protocol-off-chain-on-chain-development-workflow/269)
- [Multi-Stage Contracts in the UTXO Model: Delivery by Alexander Chepurnoy & Amitabh Saxena](https://www.youtube.com/watch?v=g3FlM_WOwBU)
- [Secure User Entry/Bootstrap Funneling In Multi Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)


## References & Resources
- [Multi-Stage Contracts in the UTXO Model](https://storage.googleapis.com/ergo-cms-media/docs/paper_26.pdf)
- [https://ergoplatform.org/docs/ErgoScript.pdf](https://ergoplatform.org/docs/ErgoScript.pdf)


