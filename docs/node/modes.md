# Modes of Operation



The Ergo node supports multiple security models, allowing users to choose the mode that best suits their needs. 

The available modes are:

- [Full *'Archive'* Node Mode](full-node.md): This is the standard mode, similar to a full Bitcoin node.
- [Pruned-Fullnode Mode](pruned-full-node.md): Downloads all headers, validates proofs-of-work, and links structures, followed by downloading a UTXO snapshot from peers and the full blocks succeeding it. 
- [Light-Fullnode Mode](light-full-node.md) only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting. 
- [Light-SPV Mode](light-spv-node.md): A lightweight mode that allows users to verify transactions without downloading the entire blockchain.




<!--TODO: ## Mode-Related Settings

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
- [modifiersProcessing](https://github.com/ergoplatform/ergo/blob/e6086e23ecd45f1e01a3e4c0344f003cec1a5b11/papers/yellow/modifiersProcessing.tex)--> 