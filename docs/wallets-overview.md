---
owner: docs
last_reviewed: 2026-06-08
source_repos:
  - repo: arkadianet/ergo-vanitygen-rust
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/arkadianet/ergo-vanitygen-rust
  - https://github.com/ergoplatform/ergo-wallet-app/releases/tag/v2.4.2313
  - https://github.com/Satergo/Satergo/releases/tag/v1.9.4
---

# Get a Wallet

Use this page to choose a wallet and learn basic wallet safety.

## Pick a Wallet

| Need | Best fit | Notes |
| --- | --- | --- |
| Browser dApps | [Nautilus](nautilus.md) | Common choice for web dApps and wallet connector flows. |
| Desktop wallet | [Minotaur](minotaur.md) | Desktop-focused wallet option. |
| Desktop wallet with optional full node | [Satergo](satergo.md) | Useful if you want a desktop wallet with node-oriented options. |
| Mobile wallet | [Ergo Mobile Wallet](https://ergoplatform.org/en/ergo-wallet-app/) | Good fit for mobile holding and payments. |
| Hardware wallet | [Ledger](ledger.md) | Better for higher-value custody and hardware signing. |
| Offline storage | [Cold Wallet Guide](cold-wallet.md) | Use for long-term holding and reduced online exposure. |
| Paper wallet | [Paper Wallet](paper-wallet.md) | Only use if you understand backup and spending risks. |
| Node wallet | [Node Wallet Overview](wallet.md) | Operator/developer flow, not the simplest user wallet. |
| Multisig | [Multisig](multisig.md) | Shared custody and higher-control setups. |
| Android browser extensions | [Nautilus or Safew on Android](Ergo-Browser-Wallets-on-Android.md) | For mobile browser dApp access. |

For broader comparison, see [Wallets Overview](wallets.md).

## Recent Wallet Releases

- [Ergo Wallet App `v2.4.2313`](https://github.com/ergoplatform/ergo-wallet-app/releases/tag/v2.4.2313) updates the Android build for Android 15+ and fixes status-bar/camera cutout and gesture-bar UI overlap.
- [Satergo `v1.9.4`](https://github.com/Satergo/Satergo/releases/tag/v1.9.4) fixes node launching and improves send-option address labels.

## Quick Decision

| If you are... | Choose |
| --- | --- |
| New and using dApps | Nautilus |
| New and mostly holding on mobile | Ergo Mobile Wallet |
| Holding larger amounts | Ledger or cold storage |
| Running infrastructure | Node wallet only if needed |
| Managing shared funds | Multisig |

## Safety First

- Write down seed phrases offline.
- Never share seed phrases or private keys.
- Verify addresses before sending.
- Try small transactions before large transfers.
- Keep wallet software updated.
- Use [Access Issues](access-issues.md) if a wallet does not load or connect.

## Advanced Address Tools

Vanity address tools search for addresses matching a chosen pattern. [ergo-vanitygen-rust](https://github.com/arkadianet/ergo-vanitygen-rust) is a Rust vanity-address generator with GUI and CLI modes, local seed generation, paper-wallet output, and pattern difficulty estimation. Treat vanity generation as advanced custody tooling: build or download only from trusted sources, verify generated addresses, and protect any seed phrase it creates.

## Payments and dApps

- [dApp Connector](dApp.md): browser dApp connection.
- [ErgoPay](ergo-pay.md): link and QR payment flow.
- [ErgoAuth](ergoauth.md): authentication with wallet signatures.
- [Message Signing](message-signing.md): verify actions and ownership.
- [Proxy Payments](proxy.md): payment proxy contracts.

## Standards and Internals

- [Wallet Standards](eip-standards.md)
- [Keys](keys.md)
- [Addresses](address.md)
- [Address Types](address_types.md)
- [Address Validation](address_validation.md)
- [EIP-3 HD Wallets](eip3.md)
