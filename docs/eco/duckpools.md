---
tags:
  - DuckPools
  - Lending
  - DeFi
  - dApp
  - dApp-Live
owner: docs
last_reviewed: 2026-05-30
source_repos:
  - repo: duckpools/interest-contracts
    branch: main
    paths:
      - README.md
  - repo: duckpools/logic-contracts
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://duckpools.io/
  - https://github.com/duckpools/interest-contracts
  - https://github.com/duckpools/logic-contracts
---

# DuckPools: Ergo Lending Protocol

[duckpools.io](https://duckpools.io/) is a decentralized finance (DeFi) application (dApp) built on the Ergo blockchain. It offers lending pools that allow users to lend ERG and its tokens to earn yield and borrow assets.

## DuckPools: A Collateralized Lending Platform with Algorithmic Lending Pools

**About DuckPools:**

DuckPools is a lending platform developed on the Ergo blockchain. It is currently developing features such as:

- **Algorithmic Lending Pools:** Users can provide ERG or native assets to lending pools and earn passive income on their capital.

- **Collateralized Loans:** Users can secure funds with their collateral!

DuckPools aims to be a catalyst for an explosive DeFi ecosystem on Ergo. The platform facilitates increased utility of ERG and Ergo native assets and boosts the Total Value Locked (TVL) in Ergo DeFi.

## Contract Architecture

DuckPools separates lending logic across contracts with explicit oracle-like support components:

- **Interest contract**: tracks the value of borrow tokens as interest accrues over time. Pool and collateral contracts read this value from R5 to calculate debt, repayment amounts, and loan values.
- **Logic / quote contract**: reports collateral value, liquidation thresholds, penalties, minimum values, loan-size limits, short-loan fees, and box-index references used to validate the quoted collateral.
- **Pool and collateral contracts**: consume the interest and quote boxes as data inputs when validating borrow, repay, liquidation, and collateral-adjustment flows.

These contracts are implementation interfaces, not just UI code. The READMEs in the source repositories describe required registers, NFT identifiers, and validation assumptions for implementations.

Developer references:

- [interest-contracts](https://github.com/duckpools/interest-contracts): interest-contract specification work.
- [logic-contracts](https://github.com/duckpools/logic-contracts): logic-contract interfaces and implementations for collateral pricing.

**Community Resources**

- [Website](https://duckpools.io)
- [Discord](https://discord.gg/znRMge8kQm)
- [Github](https://github.com/duckpools)
