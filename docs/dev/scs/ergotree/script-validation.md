# Efficient Script Validation

For a transaction that has an `INPUTS` collection of boxes to spend, each input box can have a script (termed as the `propositionBytes` property) that protects it. This script needs to be executed within the context of the current transaction. To maintain steady block validation of `1000` transactions per second, a simple transaction with a single input box requires validation of 1000 scripts per second.

To increase the probability of successful mining, the block validation time should be minimized. This allows a miner to start solving the PoW puzzle as soon as possible. 

To validate every script (of an input box), the following steps are performed:

1. A Context object is created with `SELF = box`.
2. ErgoTree is traversed to build a cost graph for cost estimation.
3. The cost estimation is computed by evaluating the cost graph with the current context.
4. If the cost is within the limit, the ErgoTree is evaluated using the context to obtain a sigma proposition (see `SigmaProp`).
5. The Sigma protocol verification procedure is executed.
