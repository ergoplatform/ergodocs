---
tags:
  - Sidechains
  - NiPoPoWs
  - Sigma Chains
owner: docs
last_reviewed: 2026-07-02
source_repos:
  - repo: BetterMoneyLabs/braid
    branch: master
    paths:
      - whitepaper/whitepaper.pdf
  - repo: arkadianet/Aegis-USE
    branch: main
    paths:
      - README.md
      - ROADMAP.md
      - dev-docs/sidechain
source_of_truth:
  - https://github.com/BetterMoneyLabs/braid/blob/master/whitepaper/whitepaper.pdf
  - https://github.com/arkadianet/Aegis-USE
  - https://github.com/ergoplatform/eips/pull/103
ia_status: directory
---

# Sidechains on Ergo: Leveraging Sigma Chains and NiPoPoWs

Ergo's robust architectural design supports the innovative development of sidechains through the Sigma Chains framework, incorporating Non-Interactive Proofs of Proof-of-Work (NiPoPoWs) to ensure efficient and secure cross-chain interaction. This document explores the concept of sidechains within the Ergo ecosystem, emphasizing their utility, the implementation of Sigma Chains, and how NiPoPoWs facilitate robust sidechain functionality.

/// admonition | Recent Developments

Explore recent advancements in sidechain technology through the [ErgoHack VII project](https://github.com/ross-weir/ergohack-sidechain/tree/main), which focuses on implementing sidechains in Ergo.
///

Adjacent research also includes [Braid](braid.md), a double merged-mined Bitcoin and Ergo sidechain design. Treat it as research material rather than a deployed Ergo sidechain.

### Aegis-USE research prototype

[Aegis-USE](https://github.com/arkadianet/Aegis-USE) is a public research prototype for private USE payments on an Ergo-merge-mined sidechain. Its design uses private notes and nullifiers, a 1:1 USE peg, and a hash-native STARK stack. The proposed trustless peg-out path depends on the still-open [EIP-0045 `verifyStark` proposal](https://github.com/ergoplatform/eips/pull/103), so it is not available on Ergo mainnet.

The repository marks the software **unaudited, testnet-only, and unsuitable for real value**. External cryptographic review has not started. Treat its reported devnet round trip as prototype evidence, not production or mainnet readiness.

A July 2026 team update said sidechain bridge work is still moving as an open-source reference stack. Current focus areas are relayer hardening, a trustless burn path, evidence/release process, and no-broadcast unsigned transaction flows. The described architecture uses a Substrate/Frontier EVM sidechain with ErgoScript boxes, registers, and AVL settlement state on Ergo. It builds on the ErgoHack VII two-way pegged sidechain design as prior art but adapts the model rather than directly copying the repository. It is not mainnet production-ready yet; remaining work includes verification boundaries, operator evidence, recovery assumptions, governance/key rotation, benchmarks, and security-review readiness.

A May 2026 dev update described the testnet prototype in more detail: a Substrate + Frontier EVM sidechain, five ErgoScript contracts on Ergo testnet, an `sERG` ERC-20 representation pegged 1:1 to nanoERG, and a TypeScript relayer using Fleet SDK plus `ethers.js`. The reported full round trip was ERG lock, sidechain mint, sidechain burn, main-chain state update, and ERG unlock. The same update called out the remaining trust boundary: most tracked attack chains had mitigations, but deep sidechain reorg / phantom-burn handling still depended on off-chain burn revalidation and a trusted sidechain-state oracle. Later discussion targeted extension-block commitments and NiPoPoW-based burn proofs as the path away from that oracle bottleneck.

## What is a Sidechain?

A sidechain is a separate blockchain that is connected to a main chain via a two-way peg. This connection allows for the transfer of assets between the main and side chains under different rules or functionalities, enabling sidechains to operate independently while enhancing the overall scalability and flexibility of the main chain.

## Sigma Chains: A Framework for Sidechains on Ergo

Sigma Chains are a specialized implementation framework for sidechains on Ergo, designed to provide enhanced programmability, cross-chain compatibility, and economic sustainability. They enable a wide range of applications by allowing each sidechain to maintain customized features while securing robust connectivity to the Ergo main chain.

### Key Benefits of Sigma Chains  

- **Programmability**: Support for complex smart contracts, enabling applications ranging from DeFi to digital identities.
- **Cross-Chain Compatibility**: Facilitates seamless interactions between Ergo and other blockchain networks, enhancing liquidity and interoperability.
- **Economic Sustainability**: Incorporates mechanisms such as storage rent and demurrage within sidechains, ensuring long-term economic viability.

## Non-Interactive Proofs of Proof-of-Work (NiPoPoWs)

NiPoPoWs are critical cryptographic components that enable sidechains to verify the state of the main chain efficiently and securely without requiring the entire chain's data. They are particularly beneficial for lightweight clients and are instrumental in reducing the computational burden on sidechain systems.

### Applications of NiPoPoWs in Sidechains  

- **Efficient Block Verification**: Allows sidechains to verify main chain block headers efficiently, negating the need for full blockchain downloads.
- **Scalability and Security**: Supports scalability solutions like state channels and provides a security mechanism to verify off-chain transactions securely.

## Implementing Two-Way Pegged Sidechains on Ergo

The Sigma Chains framework facilitates the development of two-way pegged sidechains by providing a clear structure for asset transfers and state synchronization between the Ergo main chain and sidechains.

### Implementation Steps

1. **Initiating the Transfer**: Users lock assets into a contract on the Ergo main chain, initiating their transfer to the sidechain.
2. **Operating Independently**: The sidechain, utilizing Sigma Chains, operates under its own rules and issues corresponding assets to the user.
3. **Secure Asset Return**: To transfer assets back, the sidechain burns its tokens and provides proof of this action to the main chain, which then unlocks the original assets.

### Security and Data Considerations  

- **Robust Consensus Mechanisms**: Essential for preventing fraud and ensuring the integrity of transactions across the Ergo network.
- **Data Storage on Main Chain**: Critical transaction and state data are stored on the main chain, ensuring that interactions are verifiable and secure.

## Conclusion

Sigma Chains and NiPoPoWs together provide a powerful and flexible framework for implementing sidechains on the Ergo platform. By enhancing the programmability, economic sustainability, and cross-chain compatibility of sidechains, these technologies help foster a scalable, interoperable, and robust blockchain ecosystem. As Ergo continues to evolve, the integration of these advanced technologies will be pivotal in driving innovation and adoption in the broader blockchain space.
