# Modes of Operation


The Ergo node has supported multiple security models since the very first testing network (`Testnet0`)

In addition to running in the standard *full node mode*, like a full Bitcoin node, The Ergo reference implementation supports [Light-SPV](light-spv-node.md), [Light-Fullnode](light-full-node.md), and [Pruned-Fullnode](pruned-full-node.md) modes which are described below. 



## Mode-Related Settings

Ergo has the following settings which determine a mode:

-   **`ADState: Boolean`** - keeps state roothash only.
-   **`VerifyTransactions: Boolean`** - download block transactions and verify them (requires BlocksToKeep == 0 if disabled).
-   **`PoPoWBootstrap: Boolean`** - download PoPoW proof only
-   **`BlocksToKeep: Int`** - number of last blocks to keep with transactions; for all other blocks, it keeps Header only. Keep all blocks from
    genesis if negative
-   **`MinimalSuffix: Int`** - minimal suffix size for PoPoW proof (maybe
    pre-defined constant).

`if(VerifyTransactions == false) require(BlocksToKeep == 0)` Mode from "multimode.md" can be determined as follows:

- [modifiersValidation](https://github.com/ergoplatform/ergo/blob/e6086e23ecd45f1e01a3e4c0344f003cec1a5b11/papers/yellow/modifiersValidation.tex)
- [modifiersProcessing](https://github.com/ergoplatform/ergo/blob/e6086e23ecd45f1e01a3e4c0344f003cec1a5b11/papers/yellow/modifiersProcessing.tex)