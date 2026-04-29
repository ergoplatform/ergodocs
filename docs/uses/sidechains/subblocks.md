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

In 2026 the input-block / ordering-block work moved under the Matrix implementation and devnet test stream.

- `Jan 2`: the Matrix whitepaper, [Splitting Ergo Blocks Into Input and Ordering Blocks For Fast Transaction Propagation and Confirmation](https://github.com/ergoplatform/ergo/blob/weak-blocks/papers/inputblocks/main.pdf), was published.
- `Jan 12` to `Jan 14`: the initial subblock and input-block API methods were described in `openapi.yaml` and deployed on a devnet seed node.
- `Feb 1` to `Feb 4`: the devnet was relaunched with a `60s` ordering-block delay and 60 input blocks per ordering block, with several mining peers testing.
- `Mar 4` to `Mar 25`: fixes landed for full-block propagation to out-of-sync peers, wallet and mempool support, public testnet syncing, P2P tasks, DoS prevention, and cache growth.
- `Apr 22`: Matrix was merged with the 6.0.3 candidate line, the network difficulty check for input blocks was completed, and a new jar was deployed to devnet.
- `Apr 28`: extra P2P checks were added to reduce DoS exposure and the external miner API was implemented. Stratum proxy tweaks remained before GPU mining tests.

Current caveats: the devnet/testnet stream was still finding serialization, sync, and peer-ban edge cases. Production users should treat subblocks as active protocol R&D until release notes state otherwise.
