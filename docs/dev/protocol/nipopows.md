---
tags:
  - NIPoPoWs
---

# Non-interactive Proof-of-Proof-of-Work (NIPoPoWs)

Non-interactive Proof-of-Proof-of-Work (NIPoPoWs) is a powerful feature integrated into the Ergo Blockchain, enabling efficient authentication of blockchain events using proof-of-work. NIPoPoWs eliminate the need for direct network connection or downloading all block headers, making them particularly useful for verifying cryptocurrency transactions.

## How NIPoPoWs Work

Ergo's block structure goes beyond the traditional header and transaction format, incorporating an 'extension' section for improved functionality. This section houses:

- NIPoPoWs links, updated every 1,024 block epochs
- Parameters for miner voting, including current block size
- Miscellaneous fields

This unique structure allows different types of nodes and clients to selectively download required block sections, optimizing storage, bandwidth, and CPU usage.

## Applications of NIPoPoWs

NIPoPoWs have been innovatively utilized within the Ergo ecosystem:

### 1. Light Clients

NIPoPoWs facilitate the creation of efficient light clients, enhancing the accessibility and scalability of blockchain networks. Light clients address the challenges of running a full node, which requires substantial resources. With NIPoPoWs, light clients can operate without maintaining the entire blockchain.

### 2. Light Miners

NIPoPoWs enable logarithmic space mining, allowing "light miners" to start with block headers, similar to light clients, without downloading the entire blockchain. By retaining only a select few important blocks, light miners can validate the entire blockchain, eliminating the need for full storage. This approach can be integrated through velvet (soft) forks, avoiding hard fork complexities.

### 3. Sidechains

NIPoPoWs are a novel technology that enables trustless sidechains. They leverage Simplified Payment Verification (SPV) proofs to provide resistance against potential attacks while maintaining a small size for efficient network transmission.

## Ongoing Research and Development

NIPoPoWs have been a crucial part of the Ergo Blockchain since its inception. Ergo is dedicated to continually exploring their potential and expanding this research area in collaboration with partners at IOHK. Increased use of NIPoPoWs is anticipated with ongoing contributions from the active developer community.

## Additional Resources

For those interested in exploring NIPoPoWs further:

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)