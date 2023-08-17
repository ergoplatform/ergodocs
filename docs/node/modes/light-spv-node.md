---
tags:
  - NIPoPoWs
---

# Light-SPV Mode

## What is SPV?

[Simplified Payment Verification (SPV)](spv.md) allows for a simplified way of verifying transactions by only downloading and verifying the block headers, rather than the entire blockchain. This makes it possible for users with limited resources to participate in the network and make transactions without needing a full node.

## Ergo's NIPoPoWs

Ergo implements Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) to enhance the efficiency of SPV wallets. NIPoPoWs are short stand-alone strings that allow a computer program to verify events on a proof-of-work-based blockchain without connecting to the blockchain network or downloading all block headers. This enables the creation of lightweight SPV wallets that only need to download a small sample of block headers, around 250, compared to other SPV clients that may need to download around half a million block headers. The sample size remains relatively small even as the blockchain grows larger over time.

We are currently developing a highly efficient Ergo wallet with SPV security. Stay updated on the progress of this development [here](https://github.com/ergoplatform/sigma-rust/milestone/17).

