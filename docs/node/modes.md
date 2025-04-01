# Modes of Operation

*(Back to: [Node Installation](install.md))*

The [Ergo node](install.md) supports multiple security models, providing flexibility for users to select the mode that best aligns with their requirements.

The available modes include:

- [**Full 'Archive' Node Mode**](archival-node.md): This is the standard mode, akin to a full Bitcoin node. It stores all [blocks](block.md) from the [genesis block](emission.md) onwards, checks the [proofs of work](autolykos.md), verifies the correctness of the linking structure, and maintains a copy of the entire [UTXO set](eutxo.md).

- [**Pruned-Fullnode Mode**](pruned-full-node.md): This mode downloads all [headers](block-header.md), validates proofs-of-work, and links structures. It then downloads a UTXO snapshot from peers and the full blocks succeeding it. See also [History Pruning](history-pruning.md).

- [**Light-Fullnode Mode**](light-full-node.md): This mode only holds the root digest of the state dictionary (authenticated state) and checks full blocks or a suffix of the blockchain, depending on the `blocksToKeep` setting ([History Pruning](history-pruning.md)).

- [**Light-SPV Mode**](light-spv-node.md): A lightweight mode that enables users (typically [light clients](nipopow_nodes.md)) to verify [transactions](transactions.md) with a small sample of [block headers](block-header.md) using [NIPoPoWs](nipopows.md).

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
