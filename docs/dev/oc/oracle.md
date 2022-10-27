# Oracle Core

[Oracle core](https://github.com/ergoplatform/oracle-core#roadmap) is the off-chain component run by oracles, who are part of an oracle pool. This oracle core provides an HTTP API interface for reading the current protocol state & another for submitting data points. Once a data point is submitted, the oracle core will automatically generate the required tx and post it as well as any other actions required for the protocol to run. This allows the oracle to participate in the oracle pool protocol without extra effort for the oracle operator.

The oracle core requires the user to access a full node wallet to create transactions & perform UTXO-set scanning. Furthermore, each oracle core is designed to work with only a single oracle pool. Suppose an operator runs several oracles in several oracle pools. In that case, you can use a single full node, but several instances of oracle cores must be run (and set with different API ports).

The current oracle core is built to run the protocol specified in the [EIP-0023 PR](https://github.com/ergoplatform/eips/pull/41).
