# Simplified Payment Verification (SPV)

A full Bitcoin node checks all the blocks in the blockchain (using headers) and ensures no fraudulent transactions. However, running a full node requires significant bandwidth, storage, and processing power, making it unsuitable for resource-limited devices like mobile devices. This is especially true for Bitcoin, where the blockchain size has exceeded 270 GB and continues to grow ([source](https://www.blockchain.com/charts/blocks-size)).

To address this issue, Satoshi Nakamoto proposed Simplified Payment Verification (SPV) in the [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf). SPV allows users to verify payments without running a full network node. Instead, users only need to keep a copy of the block headers of the longest proof-of-work chain. By querying network nodes, users can obtain the Merkle branch linking their transaction to the block it's timestamped in. Although users cannot independently verify the transaction, they can trust that a network node has accepted it and that subsequent blocks confirm its validity.

It's important to note that SPV is not a perfect solution and is vulnerable to attacks where an attacker overpowers the network and deceives SPV users.

While SPV mode is intended for resource-limited devices, it may not always be feasible. For example, Ethereum's headers alone total around 5 GB to download, making it challenging for Ethereum mobile clients to validate chain validity. As a result, these clients often have to blindly trust third parties.

Efforts have been made to reduce the requirements for SPV mode by checking only a few random headers instead of all. However, securely implementing this approach requires significant work.

## Efficient SPV with NIPoPoWs

To further enhance the efficiency of SPV wallets, Ergo implements Non-Interactive Proofs of Proof-of-Work (NIPoPoWs). NIPoPoWs are short stand-alone strings that allow a computer program to verify events on a proof-of-work-based blockchain without connecting to the blockchain network or downloading all block headers. These proofs can demonstrate that a cryptocurrency payment was made, for example.

By leveraging NIPoPoWs, Ergo enables the creation of highly efficient ['Light SPV'](light-spv-node.md) mobile wallets. Compared to full nodes, SPV wallets are already lightweight as they only require the download of block headers instead of the entire blockchain. NIPoPoW wallets need to download only a small sample of block