# Get a Wallet

Use this page to choose a wallet and learn basic wallet safety.

## Pick a Wallet

| Need | Best fit | Notes |
| --- | --- | --- |
| Browser dApps | [Nautilus](dev/wallet/nautilus.md) | Common choice for web dApps and wallet connector flows. |
| Desktop wallet | [Minotaur](dev/wallet/minotaur.md) | Desktop-focused wallet option. |
| Desktop wallet with optional full node | [Satergo](dev/wallet/satergo.md) | Useful if you want a desktop wallet with node-oriented options. |
| Mobile wallet | [Ergo Mobile Wallet](https://ergoplatform.org/en/ergo-wallet-app/) | Good fit for mobile holding and payments. |
| Hardware wallet | [Ledger](dev/wallet/payments/ledger.md) | Better for higher-value custody and hardware signing. |
| Offline storage | [Cold Wallet Guide](tutorials/cold-wallet.md) | Use for long-term holding and reduced online exposure. |
| Paper wallet | [Paper Wallet](dev/wallet/paper-wallet.md) | Only use if you understand backup and spending risks. |
| Node wallet | [Node Wallet Overview](node/wallet.md) | Operator/developer flow, not the simplest user wallet. |
| Multisig | [Multisig](dev/wallet/multisig.md) | Shared custody and higher-control setups. |
| Android browser extensions | [Nautilus or Safew on Android](tutorials/Ergo-Browser-Wallets-on-Android.md) | For mobile browser dApp access. |

For broader comparison, see [Wallets Overview](dev/wallets.md).

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
- Use [Access Issues](tutorials/access-issues.md) if a wallet does not load or connect.

## Payments and dApps

- [dApp Connector](dev/wallet/payments/dApp.md): browser dApp connection.
- [ErgoPay](dev/wallet/payments/ergopay/ergo-pay.md): link and QR payment flow.
- [ErgoAuth](dev/wallet/payments/ergoauth.md): authentication with wallet signatures.
- [Message Signing](tutorials/message-signing.md): verify actions and ownership.
- [Proxy Payments](dev/wallet/payments/proxy.md): payment proxy contracts.

## Standards and Internals

- [Wallet Standards](dev/wallet/eip-standards.md)
- [Keys](dev/wallet/keys.md)
- [Addresses](dev/wallet/address.md)
- [Address Types](dev/wallet/address/address_types.md)
- [Address Validation](dev/wallet/address/address_validation.md)
- [EIP-3 HD Wallets](dev/wallet/standards/eip3.md)
