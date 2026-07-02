---
owner: docs
last_reviewed: 2026-07-02
source_repos:
  - repo: ergoplatform/ergo
    branch: weak-blocks
    paths:
      - papers/inputblocks/main.pdf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/weak-blocks/papers/inputblocks/main.pdf
  - https://github.com/ergoplatform/ergo/pull/2372
  - https://github.com/ergoplatform/ergo/pull/2180
  - https://github.com/ergoplatform/sigmastate-interpreter/pull/1069
---

# Subblocks in Ergo

## Overview

/// details |TLDR
    {type: info, open: true}

With the renaming and introduction of sub-blocks, Ergo now distinguishes between sub-blocks (also called input blocks) and full blocks (now called ordering blocks). This change reduces typical onchain confirmation times from about 2 minutes to roughly 2 seconds, achieving a 17× improvement in detecting transaction failures and transforming the current competitive mempool into a more cooperative environment.
///

### What Are Sub-blocks and Ordering Blocks?

- **Sub-blocks (Input Blocks):**  
  These are block candidates generated with a lower difficulty threshold than full blocks. They are produced approximately once per second and carry most transaction data. This allows transactions to propagate and confirm much faster.
  
- **Ordering Blocks:**  
  These are the traditional full blocks of Ergo’s proof-of-work system, now renamed as ordering blocks. They are generated roughly every 2 minutes and maintain the overall consensus and security of the blockchain.

> **Note:** The naming “input blocks” (or sub-blocks) and “ordering blocks” was proposed in detail in [this document](https://raw.githubusercontent.com/ergoplatform/ergo/e15dcd0b4ca0a72d32d97228f010d813540de39d/papers/subblocks/subblocks.md).

### Enhanced User Experience

- **Rapid Onchain Confirmations:**  
  Everyday transactions—such as receiving tokens from DEX swaps or wallet-to-wallet transfers—can now be confirmed in approximately 2 seconds due to the introduction of sub-blocks. These input blocks are produced roughly every second and carry transaction data, allowing dApps and wallets to detect transaction inclusion almost instantly. However, this does not change the overall 2-minute block time for ordering blocks, which are still required for final settlement and consensus. As a result, existing dApps that rely on ordering blocks for confirmation will continue to behave as before. While some tools may treat sub-block inclusion as sufficient for faster user feedback, more security-sensitive applications—such as centralized exchanges or specific dApps handling large-value transactions—will still wait for a set number of ordering blocks to reduce the risk of chain reorganizations or 51% attacks.
  
- **Faster Failure Detection:**  
  Instead of waiting up to 6 minutes to detect a transaction failure, the new system detects failures in about 2 seconds—a 17× improvement in responsiveness.
  
- **A More Cooperative Mempool:**  
  The design shift transforms the mempool from a competitive (PvP) environment into a cooperative, multiplayer-like system, enhancing overall network responsiveness.

### In a Nutshell

Ergo’s renaming and introduction of sub-blocks (input blocks) paired with ordering blocks significantly improves transaction processing speed and reliability. These changes provide users with near-instant confirmations and faster failure detection, thereby offering a smoother and more efficient experience on the network.

For a deep dive into the technical details behind these changes, see the [technical details](input-blocks.md).

## Recent updates

Late-2025 and 2026 input-block / ordering-block work moved under the Matrix implementation and devnet test stream.

- `Jul 2` 2025: the subblocks devnet seed node was updated with stability fixes and optimizations, and maintainers said a public-testnet roadmap would follow.
- `Aug 5` to `Aug 21` 2025: maintainers were auditing and refactoring critical subblock code, tracking DoS risks for subblock-supporting nodes, and preparing public-testnet miner support after the node `6.0.1` release. [ergoplatform/ergo#2180](https://github.com/ergoplatform/ergo/pull/2180) was identified as the first small pre-subblocks refactoring PR.
- `Sep 3` to `Sep 10` 2025: early Matrix / subblock work reworked input-block P2P propagation around `INV` announcements and transaction-body diffs, so peers should not re-download mempool transactions they already hold. The related SigmaSDK work included context changes for soft-fork fields and rejecting transactions through those fields.
- `Jan 2`: the Matrix whitepaper, [Splitting Ergo Blocks Into Input and Ordering Blocks For Fast Transaction Propagation and Confirmation](https://github.com/ergoplatform/ergo/blob/weak-blocks/papers/inputblocks/main.pdf), was published.
- `Jan 12` to `Jan 14`: the initial subblock and input-block API methods were described in `openapi.yaml` and deployed on a devnet seed node.
- `Feb 1` to `Feb 4`: the devnet was relaunched with a `60s` ordering-block delay and 60 input blocks per ordering block, with several mining peers testing.
- `Mar 4` to `Mar 25`: fixes landed for full-block propagation to out-of-sync peers, wallet and mempool support, public testnet syncing, P2P tasks, DoS prevention, and cache growth.
- `Mar 11` to `Mar 17`: the Matrix branch made the number of input blocks per ordering block readjustable by miner voting rather than hardcoded. Maintainers also clarified that input blocks share the standard full ordering-block limits and that chained transactions can be included in the same input block.
- `Apr 22`: Matrix was merged with the 6.0.3 candidate line, the network difficulty check for input blocks was completed, and a new jar was deployed to devnet.
- `Apr 28`: extra P2P checks were added to reduce DoS exposure and the external miner API was implemented. Stratum proxy tweaks remained before GPU mining tests.
- `Jul 1`: the Matrix branch added verification that delivered input-block transaction bodies match the transaction digest announced in the proven input-block fields, rejecting mismatched bodies before they are cached or processed.
Testing notes:

- The December 2025 rollout plan was gradual: early Matrix peers would be mining pools and solo miners forming an input-block-aware P2P subnetwork, while non-upgraded peers continued normal block propagation. Early extension-section fields were not assumed to be present for every block during that phase.
- Early January testing used a couple of peers and showed the implementation was mostly complete but still needed broad testing, public testnet coverage, and PR splitting for review.
- A 30-second ordering-block setup with 60 input blocks per ordering block produced fork/sync behavior that was hard to analyze. The devnet then moved to `blockInterval = 60s`, which reduced input-block-chain forking.
- February testing ran with three to four mining peers. Operators were asked to reset databases after incompatible jars or serialization changes.
- March testing added wallet and mempool checks, non-mining public-testnet peer sync, and public-testnet versioning around the `6.5.0` test line.
- April testing found a P2P serialization incompatibility and requested latest jars plus database resets before continuing.

Current caveats: the devnet/testnet stream was still finding serialization, sync, peer-ban, fork-tree, and log-volume edge cases. A late-June Matrix DevNet run found excessive competing-fork bookkeeping/log churn; maintainers reported a tree-explosion fix and further RC work in progress. Production users should treat subblocks as active protocol R&D until release notes state otherwise.

### Miner and API work

The April 2026 development stream added API support needed by external miners. GPU mining tests were not ready immediately because Stratum proxy changes were still required. This matters for rollout because Matrix changes affect miner-facing block-candidate flow, not just wallet-facing transaction feedback.
