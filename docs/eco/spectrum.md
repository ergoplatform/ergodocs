---
tags:
  - Spectrum Finance
  - DEX
  - Cross-Chain
  - Yield Farming
  - Babel Fees
  - dApp
  - dApp-Live
owner: docs
last_reviewed: 2026-05-26
source_repos:
  - repo: spectrum-finance/ergo-dex
    branch: master
    paths:
      - contracts
source_of_truth:
  - https://github.com/spectrum-finance/ergo-dex/tree/master/contracts
---

# Spectrum Finance

[Spectrum](https://spectrum.fi) is a pioneering open-source, cross-chain decentralized exchange (DEX) platform, currently offering liquidity provision (LP), yield farming, and babel fees on the Cardano (ADA) and Ergo (ERG) networks.

## Current Features of Spectrum Finance

- **Liquidity Provision & Yield Farming**: Users can engage in liquidity provision and yield farming.
- **Babel Fees**: Babel fees allow transaction fees to be paid with various tokens.
- **Ergo DEX contracts**: Contract updates in the Ergo DEX repository include staking-bundle template/hash support, rounding fixes, refund fixes, and reward-compounding adjustments.

## Recent updates

- `Mar-Apr`: ErgoDEX/CoinGecko integration work reactivated Ergo tokens on CoinGecko.
- `Mar 4`: PiggyTrade was ported from Python to Kotlin with sigma-rust JNI bindings, faster loading/caching, and on-chain DEX pool data fetching.

## Spectrum Bloom: Next-Generation DeFi Framework

Spectrum Bloom is an upcoming eUTXO-native framework for decentralized finance (DeFi), designed to address and improve upon the limitations of early decentralized exchanges (DEXes).

### Highlights from the Spectrum Bloom White Paper

- **Addressing Early DEX Limitations**: Spectrum Bloom aims to overcome issues such as lack of transparency, composability, and poor performance in early DEX implementations.
- **Decentralization and Openness**: The framework focuses on principles of decentralization, openness, transparency, and sustainability.
- **eUTXO Model**: Utilizes the eUTXO blockchain model, as seen in Ergo and Cardano, supporting multi-stage contracts and multi-token functionality.
- **Innovative DEX Protocol**: Includes a novel protocol for DEX that consists of both on-chain (UTxO and validators) and off-chain (event handlers for state transitions) elements.
- **Liquidity Pooling and Execution**: Spectrum Bloom proposes unique approaches to liquidity pooling and order execution, aiming to streamline processes and reduce overhead.
- **Universal Order Composition**: Introduces universally composable orders, which can be fulfilled from any liquidity source, enhancing flexibility and efficiency.
- **Autonomous Account (AA)**: A key feature where an on-chain entity can validate execution and release user funds for trading, facilitating a dynamic set of applications on eUTXO blockchains.
- **Future Extensions and Applications**: The white paper also discusses potential extensions and applications of the Autonomous Account concept beyond DEXes.

## Resources

### Tutorials

- [Running an off-chain matching bot](https://github.com/ergolabs/ergo-dex-backend#building--running-the-off-chain-services)

### Papers

- [Extended UTxO in production: Techniques, trade-offs, and finding a better balance](https://spectrum.fi/eutxo_in_production.pdf)
- [Spectrum Bloom White Paper](https://spectrum.fi/spectrum_bloom_wp.pdf)

### Dev-Resources

- 🥇 **[Contracts Repository](https://github.com/spectrum-finance/ergo-dex/tree/master/contracts)**: ErgoScript contracts for the DEX.
- 🥇 **[Backend Repository](https://github.com/spectrum-finance/spectrum-offchain-ergo)**: Off-chain services (bots) for matching and execution.
- [EIP-0014: Decentralized Exchange Contracts](https://github.com/ergoplatform/eips/pull/27)
