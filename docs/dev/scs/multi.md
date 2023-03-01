# Multi-Stage Protocols

A multi-stage protocol is a sequence of steps or stages executed to achieve a particular outcome or goal. In the context of computer networks and distributed systems, multi-stage protocols are often used to facilitate communication and data transfer between different nodes or components of the system.

Each stage of the protocol is designed to perform a specific task or function, and the successful completion of each stage depends on the completion of the previous stage. Multi-stage protocols may also incorporate error handling and recovery mechanisms to ensure that the protocol can continue functioning despite errors or failures.

Multi-stage protocols can be used to execute complex transactions and smart contracts, with each stage representing a specific step in the transaction or contract execution process. This provides a structured approach to executing complex transactions and computations while ensuring that the various stages are executed correctly and with appropriate dependencies on each other.

Multi-Stage Contracts provide an extension to Bitcoin’s UTXO model with on-chain computations. Because Ergo uses the *UTXO model* (first seen in Bitcoin), it is possible to process parallelised actions on top of smart contracts. It is a complex design that aims for *infinite scalability*, creating more space to build complex solutions that introduce the concept of *UTXO chains*.

Multi-stage contracts refer to smart contracts that operate on a *stateful* level. 

We describe how to emulate persistent storage in UTXO-based systems using ['transaction trees'](tx-tree.md). Allowing us to emulate the functionality of account-based systems such as Ethereum without the overhead of accounts. 


## Examples

- Reversible Address with anti-theft features
- A Rock Paper Scissors game with provable fairness
- A full-featured ICO that accepts funding in ERGs
 
## Tutorials & Guides
- [Secure User Entry/Bootstrap Funneling In Multi Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)
- [Multi-Stage Protocol Off-Chain & On-Chain Development Workflow](https://www.ergoforum.org/t/multi-stage-protocol-off-chain-on-chain-development-workflow/269)
- [Multi-Stage Contracts in the UTXO Model: Delivery by Alexander Chepurnoy & Amitabh Saxena](https://www.youtube.com/watch?v=g3FlM_WOwBU)
- [Secure User Entry/Bootstrap Funneling In Multi Stage Protocols](https://www.ergoforum.org/t/secure-user-entry-bootstrap-funneling-in-multi-stage-protocols/228)


## References & Resources
- [Multi-Stage Contracts in the UTXO Model](https://storage.googleapis.com/ergo-cms-media/docs/paper_26.pdf)
- [Multi-Stage Contracts in the UTXO Model: Delivery by Alexander Chepurnoy & Amitabh Saxena](https://www.youtube.com/watch?v=g3FlM_WOwBU)
- [https://ergoplatform.org/docs/ErgoScript.pdf](https://ergoplatform.org/docs/ErgoScript.pdf)


## What is a multistage contract?

- Consider a protocol for an Ethereum contract
The contract starts in State 1 and ends in State 3


## Enriched Context Levels

- Level 1: current UTXO, height and timestamp
- Level 2: current transaction (inputs and outputs)
- Level 3: current block header and block solution
- Level 4: current block (other sibling transactions)


- Script code can have predicates on objects in context. 
    - Example `OUTPUT(0).value >= 1000`
- It is known that Level 2 can emulate Turing complete (hence Ethereum)
However, the proof uses Rule 110 cellular automation. Reduction is not efficient
- We need something more efficient than Rule 110. This is our contribution.


## How to ensure that each stage follows protocol?

Code in context Level 2 and higher allows multistage protocols

Spending transaction must create another UTXO with the required properties. 

```scala
out.propositionBytes == state_n_code && 
out.R4[Int].get == SELF.R4[Int].get // ensure data is propagated
```

- [Transaction Trees](tx-tree.md): First UTXO chained to second, Second to third, etc.