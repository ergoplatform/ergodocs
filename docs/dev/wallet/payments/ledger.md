---
tags:
  - JavaScript
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: arobsn/ledger-ergo-js
    branch: master
    paths:
      - README.md
  - repo: ergoplatform/ledger-app-ergo
    branch: main
    paths:
      - README.md
      - doc
source_of_truth:
  - https://github.com/arobsn/ledger-ergo-js
  - https://github.com/arobsn/ledger-ergo-js/releases/tag/v0.2.0
  - https://github.com/arobsn/ledger-ergo-js/releases/tag/v0.2.1
  - https://github.com/ergoplatform/ledger-app-ergo
---

# Ledger

## Developer mode

The current Ergo Ledger application lives in [ergoplatform/ledger-app-ergo](https://github.com/ergoplatform/ledger-app-ergo). Its README covers local compilation, sideloading, generated API documentation, and the current automated test setup for Nano S+, Nano X, Stax, and Flex devices.

For broader hardware-wallet implementation context, see [Hardware Wallet Integration with sigma-rust](hardware-wallet-integration.md) and [Nautilus Wallet](nautilus.md).

## Resources

For wallet developers

- [ledger-ergo-js](https://github.com/arobsn/ledger-ergo-js) is the maintained JavaScript binding library for the Ergo Ledger app. The `v0.2.0` release added OS-level helpers such as `openApp()`, `closeApp()`, and `getCurrentAppInfo()`, and `v0.2.1` followed with error-code fixes for `openApp()`.
- The current app implementation is [ergoplatform/ledger-app-ergo](https://github.com/ergoplatform/ledger-app-ergo).
- [ledger4j - Ledger HID Communications Library](https://github.com/aionnetwork/ledger4j)
- [lib-ledger-core](https://github.com/LedgerHQ/lib-ledger-core)
