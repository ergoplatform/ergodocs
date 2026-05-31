---
tags:
  - Truffle
  - Trading
  - Wallet
  - ErgoPay
owner: docs
last_reviewed: 2026-05-29
source_repos:
  - repo: FlyingPig5/truffle
    branch: main
    paths:
      - README.md
      - Truffle
source_of_truth:
  - https://github.com/FlyingPig5/truffle
---

# Truffle

[Truffle](https://github.com/FlyingPig5/truffle) is a self-custodial mobile trading app and wallet for Ergo. It is built for fast on-chain trading while keeping users in control of their keys.

The app supports Spectrum/ErgoDex liquidity pools for swaps, stablecoin minting and redeeming for USE, SigUSD/SigRSV, and DexyGold, wallet sends, portfolio views, token price charts, and ErgoPay deep links.

Truffle can be used in two wallet modes:

- **ErgoPay:** add a public address and sign transactions in an external wallet.
- **Mnemonic import:** import a seed phrase and sign locally in the app.

The upstream README marks Truffle as beta software. Users should verify transaction details before signing and treat direct mnemonic import as a hot-wallet mode.

## Links

- [Truffle repository](https://github.com/FlyingPig5/truffle)
- [Releases](https://github.com/FlyingPig5/truffle/releases)
- [Security audit note](https://github.com/FlyingPig5/truffle/blob/main/Security_Audit.md)
