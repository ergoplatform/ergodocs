---
owner: docs
last_reviewed: 2026-10-21
source_repos:
  - repo: arkadianet/ergo-vanitygen-rust
    branch: main
    paths:
      - README.md
  - repo: arkadianet/Argus
    branch: main
    release_watch: true
    paths:
      - app/pubspec.yaml
source_of_truth:
  - https://github.com/epmw/epmw
  - https://github.com/arkadianet/ergo-vanitygen-rust
  - https://github.com/arkadianet/Argus
  - https://github.com/arkadianet/Argus/releases/tag/v1.0.0-alpha.43
  - https://github.com/arkadianet/Argus/releases/tag/v1.0.0-alpha.59
  - https://github.com/arkadianet/Argus/releases/tag/v1.0.0-alpha.55
  - https://github.com/ergoplatform/ergo-wallet-app/pull/212
  - https://github.com/ergoplatform/ergo-wallet-app/releases/tag/v2.4.2313
  - https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.6
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
| Experimental Android wallet | [Argus](https://github.com/arkadianet/Argus/releases) | Experimental beta for testing; verify release signatures and do not use production funds. |
| Hardware wallet | [Ledger](ledger.md) | Better for higher-value custody and hardware signing. |
| Experimental DIY hardware | [EPMW](https://github.com/epmw/epmw) | Developer hardware-wallet project; not a normal end-user wallet path. |
| Offline storage | [Cold Wallet Guide](cold-wallet.md) | Use for long-term holding and reduced online exposure. |
| Paper wallet | [Paper Wallet](paper-wallet.md) | Only use if you understand backup and spending risks. |
| Node wallet | [Node Wallet Overview](wallet.md) | Operator/developer flow, not the simplest user wallet. |
| Multisig | [Multisig](multisig.md) | Shared custody and higher-control setups. |
| Android browser extensions | [Nautilus or Safew on Android](Ergo-Browser-Wallets-on-Android.md) | For mobile browser dApp access. |

For broader comparison, see [Wallets Overview](wallets.md).

## Recent Wallet Releases

- [Ergo Wallet App `v2.4.2313`](https://github.com/ergoplatform/ergo-wallet-app/releases/tag/v2.4.2313) updates the Android build for Android 15+ and fixes status-bar/camera cutout and gesture-bar UI overlap.
- A May 2026 dev-wallet update identified chained mobile transactions as a mempool-awareness issue. [Draft PR #212](https://github.com/ergoplatform/ergo-wallet-app/pull/212) explored a local metadata-only pending-transaction WAL for hot wallet, cold wallet, and ErgoPay flows; treat it as development work unless release notes say it shipped.
- [Nautilus `v1.3.6`](https://github.com/nautls/nautilus-wallet/releases/tag/v1.3.6) fixes dApp Connector request handling, supports partial signing through `sign_tx_inputs`, checks transaction well-formedness in `submit_tx`, improves QR rendering, and fixes a Ledger Buffer-polyfill override. Verify the installed browser-store version.
- [Satergo `v1.9.4`](https://github.com/Satergo/Satergo/releases/tag/v1.9.4) fixes node launching and improves send-option address labels.
- [Argus `v1.0.0-beta.6`](https://github.com/arkadianet/Argus/releases/tag/v1.0.0-beta.6) is the current checked experimental Android build. It validates recovery-phrase words and checksums before PIN setup, cleans pasted phrases, accepts the ten official BIP-39 languages, and supports legacy pre-1627 Ergo derivation with history-based selection and an explicit advanced override. The beta releases use the same release signing key. The earlier alpha.59 build resolves token names, decimals, and descriptions during ordinary wallet sync and caches them per wallet; automatic resolution requires an `extraIndex` node, never falls back to the explorer, and does not automatically resolve stealth-only holdings. Issuer metadata remains untrusted. Earlier alpha releases stopped automatic NFT artwork requests; remote previews require an IPFS gateway you choose and ordinary web URLs are not fetched automatically.
- Recent alpha releases also make token-heavy transactions safer to construct: token change is split by the serialized box-size limit and funded at the required per-byte minimum, mixed-token boxes can be spent, and token change returns to the wallet for Dexy actions. Watch-only accounts and the initial EIP-19 offline-signing flow are available, but the upstream notes still describe the device and camera path as untested. The wallet remains experimental and unsuitable for production funds; a release signature identifies the publisher and does not constitute a security audit.

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

[EPMW](https://github.com/epmw/epmw), the Ergo Poor Man's Wallet, is an experimental DIY hardware-wallet project. September 2025 dev updates said committed firmware could import a mnemonic seed and show the corresponding XPUB as a QR code; newer development work was focused on user-verifiable entropy generation before full wallet creation and transaction signing.

## Payments and dApps

- [dApp Connector](dApp.md): browser dApp connection.
- [ErgoPay](ergo-pay.md): link and QR payment flow.
- [ErgoNames](ergonames.md): public beta for human-readable wallet names such as `~yourname`.
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
