# Transaction Chains

In a multi-stage protocol, a **transaction chain** is a sequence of transactions that are executed in a specific order to achieve a particular outcome or goal. Each transaction in the chain depends on the successful execution of the previous transaction, and the overall success of the protocol depends on the successful execution of the entire transaction chain.

For example, a transaction chain in a decentralised exchange protocol might involve several steps to execute a trade between two parties. The transaction chain might include steps such as:

- Approving the exchange to spend the required tokens from the user's wallet
- Depositing the tokens to be traded into the exchange's smart contract
- Placing an order to buy or sell tokens at a specific price
- Matching the order with a corresponding buy or sell order
- Executing the trade by transferring the tokens and corresponding payment between the parties
- Withdrawing the traded tokens and payment from the exchange's smart contract back to the respective parties' wallets

In this example, each transaction in the chain depends on the successful execution of the previous transaction, and the overall success of the trade depends on the successful execution of the entire transaction chain. If any transactions fail or encounter an error, the entire chain may fail, and the trade will not be executed.

Overall, transaction chains are an important aspect of multi-stage protocols. They provide a structured approach to achieving specific goals or outcomes while ensuring that the various transactions are executed in a specific order and with appropriate dependencies on each other.


## Process

A **transaction chain** is used for creating a multi-stage protocol whose code does not contain loops or `if` statements. 

A transaction chain is created as follows:

### 1: Represent as N
Represent an Ethereum contract’s execution using n sequential steps, where each step represents a transaction that modifies its state. The states before and after a transaction are a directed graph's start and end nodes, with the transaction as the edge joining them. As an example, a 3-stage contract, such as the ICO example of Section 4.3, is represented as:

![](../../../assets/img/scs/tx-chain.png)

The states contain data and the code that was executed in the transaction.

### 2: State

Hardwire state `n`’s code and data inside state `n − 1`’s code. Then require the code of state `n − 1` to output a box containing state n’s code and data. An example is given in the following pseudocode:

```scala
// Ensure the output box has the same ErgoScript code as the state box and the same R4 data
// This is used to propagate data from the state box to the output box
out.propositionBytes == state_n_code &&
out.R4[Int].get == SELF.R4[Int].get
```

The above code uses the field `propositionBytes` of a box, which contains the binary representation of its guard script as a collection of bytes.

### 3: Repeat

Repeat Step 2 by replacing `(n, n − 1)` by `(n − 1, n − 2)` while `n > 2`


To avoid code size increase at each iteration, we ideally work with hashes, as in hash(out.propositionBytes) == state n code hash. However, for clarity of presentation, we will skip this optimization.

Next, we will look at [Transaction Trees](tx-tree.md)