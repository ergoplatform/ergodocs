---
tags:
  - Merged Mining
  - Mining
  - Sigma Chains
---
# Merged Mining on Ergo

## Overview

Merged mining allows miners to mine on multiple blockchains simultaneously using the same hashing power. In the context of Ergo, merged mining is proposed as a key consensus mechanism, particularly for **pegged sidechains** within the planned **[Sigma Chains](sigma-chains.md)** framework. It is designed to enable these sidechains to leverage the security of the main Ergo blockchain without requiring dedicated mining hardware, playing a potential role in revitalizing Proof-of-Work (PoW) and enhancing cross-chain interoperability once implemented.

A key advantage of Ergo's approach is its flexibility compared to implementations like Bitcoin's. Due to Ergo's expressive smart contracts (ErgoScript) and the extended UTXO model, merged mining doesn't need to be strictly tied to the coinbase transaction, allowing for sophisticated contract-based implementations.

## Mechanism for Merged-Mined Sigma Chains

This mechanism describes the typical approach for **merged-mined sidechains** within the Sigma Chains ecosystem. Instead of modifying the mainchain's coinbase transaction structure, these sidechains use a dedicated UTXO (Unspent Transaction Output) on the Ergo mainnet to track the sidechain's progress and validate its Proof-of-Work (PoW).

Here's how it typically works:

1.  **Sidechain Data Representation:** The state and progress of the sidechain are represented as a data tuple, potentially including:
    *   `h`: Sidechain height.
    *   `Th`: State changes (transactions) at height `h`.
    *   `Uh`: Digest of the sidechain's UTXO set AVL+ tree after processing `Th`.
    *   `Ch`: Digest of the sidechain's state history AVL+ tree (committing to previous states).
    *   **PoW Fields:** For merged mining, crucial fields like `nonce` and `solution` demonstrating the PoW performed for the sidechain block at height `h` are added to this tuple.
    (Reference: ErgoHack Sidechain Report, Section 2)

2.  **Submission via Dedicated UTXO:**
    *   A specific UTXO exists on the Ergo mainchain, uniquely identified by a **special NFT** (Non-Fungible Token). This UTXO acts as the official record carrier for the sidechain's merged mining data.
    *   An Ergo miner who also mines the sidechain finds a valid PoW solution satisfying both the Ergo mainchain difficulty *and* the sidechain difficulty.
    *   The miner then creates an Ergo transaction that spends the *current* sidechain data UTXO.
    *   This transaction creates a *new* UTXO, protected by the same NFT, containing the updated sidechain data tuple (including the new height, state digests, and the valid PoW fields) for the latest sidechain block.

3.  **Contract Logic:** The sidechain data UTXO is protected by an ErgoScript contract. This contract enforces the rules for updating the sidechain state:
    *   **Miner Validation:** The contract typically ensures that only a valid Ergo miner (potentially identified via context variables like `minerPubKey`, similar to the emission contract) can spend the box.
    *   **PoW Verification:** The contract enforces rules ensuring the submitted PoW is valid for the sidechain. Full verification logic might reside within the sidechain protocol, but the mainchain contract validates the miner's attestation and potentially basic PoW properties. Smart contracts on the Ergo mainchain can read sidechain data submitted via this UTXO, enabling seamless and secure pegging.
    *   **State Transition:** The contract enforces rules about how the sidechain state progresses (e.g., height must increment correctly, state digests match).

## Merged Mining in the Sigma Chains Ecosystem

Sigma Chains introduce an innovative approach to revitalizing PoW through merged mining. Key aspects include:

*   **Algorithm Agnostic:** Sigma Chains can support various PoW algorithms, making merged mining an attractive option for miners across different hardware classes (ASIC, GPU, CPU) who might find mining other chains unprofitable. This allows them to contribute to Ergo's ecosystem security.
*   **Economic Sustainability:** Merged mining on Sigma Chains allows Ergo miners to be paid in various sidechain tokens for securing those chains. However, ERG is still required for transaction fees when interacting with the Ergo mainnet (e.g., submitting the sidechain state UTXO update), creating a sustainable economic model that benefits miners and reinforces ERG's utility.
*   **Interoperability:** This mechanism forms the basis for efficient and trustless cross-chain interoperability between Ergo and its sidechains. The pegging security is directly tied to the security of the sidechain itself, benefiting from the combined hash power directed towards it.

*(See [Sigma Chains](sigma-chains.md) for more details on the broader vision).*

## Relation to Emission Contract & Rewards

The contract governing the sidechain data UTXO can be viewed as a simplified version of Ergo's main emission contract, or potentially even be combined with it.

*   **Miner Control:** Like the emission contract ensures only miners create emission boxes, the sidechain contract ensures miners (or authorized parties) update the sidechain state UTXO.
*   **Incentives:** This mechanism allows for direct rewarding of merged-mining participants on the Ergo mainchain. The transaction spending the old sidechain UTXO and creating the new one could also be structured to:
    *   Mint and distribute sidechain-specific tokens stored within the sidechain data UTXO itself.
    *   Unlock mainchain ERG or other tokens held in associated contract boxes as a reward for submitting the valid sidechain PoW.

(Reference: ErgoScript Paper, Page 10 example of time-controlled emission, and the concept of miner-spendable contracts).

## Security

The security of a merged-mined sidechain relies on the "honest majority assumption" applied to the *subset* of Ergo miners participating in mining that specific sidechain. If a majority of the hash power directed towards the sidechain (from the pool of participating Ergo miners) is honest, the sidechain's history is considered secure against PoW-based attacks from those miners. The pegging security is equivalent to the security of the sidechain itself.

(Reference: ErgoHack Sidechain Report, Section 2.1)

## Advantages on Ergo

*   **Flexibility:** Not restricted to coinbase transactions, allowing various contract-based implementations.
*   **Leverages ErgoScript:** Enables sophisticated rules, validation, and incentive mechanisms within the sidechain data UTXO contract.
*   **UTXO-Based:** Fits naturally within Ergo's extended UTXO model.
*   **Integrated Incentives:** Allows for seamless rewarding of miners (potentially in sidechain tokens or ERG) on the mainchain for securing the sidechain.
*   **Revitalizes PoW:** Provides profitable avenues for miners using various hardware, strengthening the overall PoW ecosystem.
*   **Enhanced Interoperability:** Forms a core component of the Sigma Chains framework for trustless cross-chain interactions.

## References

*   **[Sigma Chains](sigma-chains.md):** Provides the broader context for merged mining and sidechain constructions on Ergo.
*   **[ErgoHack Sidechain Report:](https://github.com/ross-weir/ergohack-sidechain/blob/main/docs/whitepaper/sidechain.pdf)**  (See Sections 2 and 2.1 for early technical details).
*   **[ErgoScript Paper:](https://storage.googleapis.com/ergo-cms-media/docs/ErgoScript.pdf)** (See Page 10 for Emission Contract Example).

