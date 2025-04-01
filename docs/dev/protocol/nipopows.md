---
tags:
  - NIPoPoWs
  - Light Clients
  - Sidechains
---

# Non-interactive Proof-of-Proof-of-Work (NIPoPoWs)

*(Back to: [Protocol Overview](protocol-overview.md))*

**Non-interactive Proofs of Proof-of-Work (NIPoPoWs)** is a powerful cryptographic protocol integrated into the Ergo blockchain, enabling efficient authentication of blockchain events using [proof-of-work](autolykos-protocol.md). NIPoPoWs allow verifying that an event took place without requiring a direct network connection or downloading all [block headers](block-header.md), making them particularly useful for [cross-chain communication](use-cases-overview.md#infrastructure), [sidechains](sidechains.md), and [light clients](light-spv-node.md).

## How NIPoPoWs Work

NIPoPoWs consist of a prover and a verifier. The prover is a [full node](archival-node.md) on the source blockchain, while the verifier does not have access to the full blockchain but knows its genesis block. The prover generates a short proof that convinces the verifier that an event occurred in the source blockchain. This proof is succinct, growing only polylogarithmically with the size of the blockchain.

The security of NIPoPoWs relies on the honest majority assumption. The verifier accepts multiple proofs, and as long as at least one of them is honestly generated, the verifier can extract the correct information about the occurrence of the event.

Ergo's [block structure](block.md) goes beyond the traditional header and transaction format, incorporating an ['extension' section](extension-section.md) that houses NIPoPoW links, updated every 1,024 block epochs. This unique structure allows different types of [nodes](modes.md) and clients to selectively download required block sections, optimizing storage, bandwidth, and CPU usage.

## Applications of NIPoPoWs

### [Light Clients](nipopow/nipopow_nodes.md)

NIPoPoWs facilitate the creation of efficient [light clients](light-spv-node.md), enhancing the accessibility and [scalability](scaling.md) of blockchain networks. Light clients address the challenges of running a full node, which requires substantial resources. With NIPoPoWs, light clients can operate without maintaining the entire blockchain, as they can verify the occurrence of events using succinct proofs.

### [Light Miners](nipopow/logspace.md)

NIPoPoWs enable [logarithmic space mining](log_space.md), allowing "light miners" to start with block headers, similar to light clients, without downloading the entire blockchain. By retaining only a select few important blocks, light miners can validate the entire blockchain, eliminating the need for full storage. This approach can be integrated through [velvet (soft) forks](velvet-fork.md), avoiding [hard fork](hard-fork.md) complexities.

### [Sidechains](nipopow-sidechains.md)

NIPoPoWs enable the construction of trustless proof-of-work [sidechains](sidechains.md), allowing communication between blockchains without trusted intermediaries. They can be used to transfer assets from one blockchain to another and back, implementing a two-way peg. The security of the sidechain construction relies on the security of the underlying NIPoPoW protocol.

NIPoPoWs leverage Simplified Payment Verification (SPV) proofs to provide resistance against potential attacks while maintaining a small size for efficient network transmission. This novel technology opens up new possibilities for [interoperability](use-cases-overview.md#infrastructure) between blockchains.

### Cross-Chain Communication

NIPoPoWs facilitate generic cross-chain communication, allowing [smart contracts](ergoscript.md) on one blockchain to receive and react to events that occur on another blockchain without the need for a trusted third party. This enables various applications, such as:

- Remote ICOs: Investors can directly pay for tokens in one cryptocurrency (e.g., Bitcoin) and receive the tokens on another blockchain (e.g., Ethereum).
- [Atomic Swaps](atomic.md): Two parties can exchange cryptocurrencies across different blockchains without the need for a centralized exchange, using NIPoPoWs to verify the occurrence of payments.

## Adoption Considerations

To adopt NIPoPoWs, the source blockchain needs to support interlink structures, which can be added through a [velvet fork](velvet-fork.md) without requiring a [hard fork](hard-fork.md). The target blockchain must be able to run the NIPoPoW verification function, which can be implemented in a Turing-complete language such as Solidity.

[Miners](mining-overview.md) and full nodes of the target blockchain do not need to be aware of the source blockchain, as they treat the NIPoPoW proofs as opaque strings passed to a smart contract. This blockchain agnosticism allows users to initiate cross-chain relationships between different blockchains dynamically.

## Ongoing Research and Development

NIPoPoWs have been a crucial part of the Ergo blockchain since its inception. Ergo is dedicated to continually exploring the potential of NIPoPoWs and expanding this research area in collaboration with partners at IOHK. Increased use of NIPoPoWs is anticipated with ongoing contributions from the active developer community.

## Conclusion

Non-interactive Proof-of-Proof-of-Work (NIPoPoWs) is a groundbreaking technology that enables efficient verification of blockchain events without requiring direct network access or full block header downloads. Its applications span light clients, light miners, sidechains, and cross-chain communication, offering enhanced accessibility, scalability, and interoperability for blockchain networks.

Ergo's implementation of NIPoPoWs, along with its unique block structure, positions it at the forefront of this research area. As the blockchain ecosystem continues to evolve, NIPoPoWs are expected to play a significant role in shaping the future of cross-chain interactions and the development of more efficient and accessible blockchain solutions.

## Additional Resources

For those interested in exploring NIPoPoWs further:

- [Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)
- [Compact Storage of Superblocks for NIPoPoW Applications](https://eprint.iacr.org/2019/1444.pdf)
- [Proof-of-Work Sidechains](https://eprint.iacr.org/2018/1048.pdf) by Aggelos Kiayias and Dionysis Zindros
