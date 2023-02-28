---
tags:
  - Data Model
  - Transactions
---
# Transactions



Each Ergo transaction is an **atomic state transition operation**, which means that it *destroys* a [box](box.md) from the state and creates new ones. 


## Anatomy

Each transaction executed on Ergo consists of **these three things**. 

- `One or more` **Input boxes** 
    -  This is the source of your funds for the transaction. 
    -  These boxes must already exist and will be destroyed by the transaction.  
    -  The guard script in each box will be evaluated and must return `true` for the transaction to be considered valid.
- `One or more` **Output boxes**  
    -  This is your destination of funds. 
    -  These boxes will be created.
-  `Zero or more` **Data-Input boxes**  
    -  These are additional boxes whose data can be referenced and used by smart contracts of the inputs. 
    -  The guard script in these boxes will not be evaluated.

### Data Inputs

- [**Data inputs**](read-only-inputs.md) are a unique concept created by Ergo, which were added to Cardano with the *Vasil* Hardfork. These allow multiple transactions to share a data-input box, storing only a single reference to the box in the block. 


## Overview

- If the transaction is spending boxes protected by a non-trivial script, its inputs should also contain *proof of spending correctness* - context extension (user-defined key-value map) and data inputs (links to existing boxes in the state) that you may use during script reduction to crypto, signatures that satisfies the remaining cryptographic protection of the script. 
- Transactions are not encrypted, meaning you can publicly view transactions included in blocks.





## Tools

- [Transaction builder](https://thierrym1212.github.io/txbuilder/) |  The application allows you to manipulate Ergo JSON transactions with a UI and to sign them with a wallet or to prepare the JSON for the Swagger API. It can also load the JSON of an unsigned transaction to edit it.  | [GitHub](https://github.com/ThierryM1212/transaction-builder/)  | [Video](https://youtu.be/0VhfY7osT2k)
