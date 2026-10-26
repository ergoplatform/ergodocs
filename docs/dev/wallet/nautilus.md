---
owner: docs
last_reviewed: 2026-10-25
source_repos:
  - repo: nautls/nautilus-wallet
    branch: master
    release_watch: true
    paths:
      - package.json
      - src/extension/content-scripts/injected.ts
      - docs/dapp-connector/wallet-interaction.md
source_of_truth:
  - https://github.com/nautls/nautilus-wallet
  - https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.6
---

# Nautilus Wallet

[Nautilus Wallet](https://twitter.com/NautilusWallet) is a privacy-focused, web-based wallet designed for the secure management of digital assets within the Ergo ecosystem. It offers an intuitive user interface that caters to both novice and experienced users.

## Features

- **Privacy Enhanced:** Nautilus prioritizes user privacy, employing advanced security measures to protect your digital assets.
- **Ledger Integration:** For those seeking an extra layer of security, Nautilus supports Ledger hardware wallets, currently available in developer mode for advanced users and developers.
- **Developer References:** For the current Ledger app and JS binding stack, see [Ledger](ledger.md) and [Hardware Wallet Integration with sigma-rust](hardware-wallet-integration.md).

## Recent updates

- `May 9`: [Nautilus v1.3.3](https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.3) added Crux and HOF token metadata, switched token-rate fetching to the Sigmaspace DEX API, added Javanese and Malaysian translations, bumped dependencies, and kept package-manager hardening through dependency overrides and explicit built-dependency allowlists.
- `Mar 7`: [Nautilus v1.3.2](https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.2) shipped with `USE`, `CLB USE`, and `DORT` additions.
- `Jan 7`: the Android guide noted that Nautilus `0.9.4` is the last release with a working mobile dApp connector; later mobile connector support is broken.
- `Apr 8`: Javanese translation work was submitted for the wallet app.
- Keystone hardware-wallet integration remains unfinished; supply-chain review is important because that path introduced a large transient dependency set.
- `Aug 13` to `Aug 20` 2025: dev updates said Keystone integration work was nearing Nautilus review, while Nautilus research also covered passwordless transaction signing and a mempool tracker. Treat these as development tracks until Nautilus release notes mark them shipped.
- `Jul 2` to `Jul 31` 2025: dev updates reported fixes for a non-Ledger dApp Connector rendering bug, a wallet-loading reactivity bug, and unstable virtual-mempool handling. Chained multi-transaction signing remained planned in [nautilus-wallet#213](https://github.com/nautls/nautilus-wallet/issues/213), not shipped.

## Current Release

[Nautilus v1.3.6](https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.6) queues and deduplicates dApp Connector window-opening requests, keeps the service worker alive while requests are pending, and checks transaction well-formedness in `submit_tx`. Its [connector implementation](https://github.com/nautls/nautilus-wallet/blob/v1.3.6/src/extension/content-scripts/injected.ts) exposes partial signing as `sign_tx_inputs(unsignedTransaction, indexes)`, returning signed inputs in the requested order. It also improves QR rendering, updates Indonesian, Malay, and Javanese translations, and fixes a Ledger Buffer-polyfill override.

Earlier [v1.3.4](https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.4) added wallet search during dApp connection, Tab selection for mnemonic words, MEOW metadata and a LIT icon, plus form-validation, bundle and dependency changes. [v1.3.5](https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.5) fixed Windows build-output filename sanitization. A published source release and browser-store rollout are separate; check the version actually installed before relying on a new interaction.

## Installation

Nautilus can be easily installed as a browser extension. Select the version compatible with your browser:

- [Chrome Web Store](https://chrome.google.com/webstore/detail/nautilus-wallet/gjlmehlldlphhljhpnlddaodbjjcchai) - Install Nautilus for Google Chrome.
- [Firefox Add-ons](https://addons.mozilla.org/bs/firefox/addon/nautilus/) - Get Nautilus for Mozilla Firefox.

## Getting Started

/// details | Comprehensive Video Guide
    {type: info, open: true}
For a step-by-step guide on setting up and using Nautilus, watch the [comprehensive video tutorial](https://www.youtube.com/watch?v=hMwtwlUpnRQ).
///

## Internationalization (i18n)

There is community interest in providing Nautilus Wallet translations for different languages to improve accessibility. While multi-language support may be planned, the specific process for contributing translations might vary. If you are interested in contributing translations, please inquire in the Nautilus community channels linked below for the current status and contribution guidelines.

## Community Support

Connect with the Nautilus community for support, updates, and discussions:

Join the Nautilus community on [Telegram](http://t.me/@NautilusWallet) or [Discord](https://discord.gg/ergo-platform-668903786361651200), where the chats are bridged between each other for a cohesive conversation experience.
