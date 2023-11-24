# Wallets


/// details | Disclaimer
    {type: warning, open: true}
Note that wallets are supported by third parties, we only provide the information below as a courtesy.
///
/// details | Funds stuck in Yoroi?
    {type: warning, open: false}
If you have your Ergo wallet open in Yoroi and know the password for it, you can use [this tool](https://github.com/satsen/yoroi-ergo-wallet-recover) to decrypt the wallet and send all funds to a new wallet of yours.
///
| Wallet | Type | dApp-C | Node | Cold Wallet | [E-Pay](https://github.com/ergoplatform/eips/blob/master/eip-0020.md) | [Mixer](https://docs.ergoplatform.com/uses/mixer/#ergomixer) |
|---|---|---|---|---|---|---|
| [Nautilus](https://chrome.google.com/webstore/detail/nautilus-wallet/gjlmehlldlphhljhpnlddaodbjjcchai) | Web | ✅ |  | ✅ |  | 🔜 |
| [Ergo Wallet](https://ergoplatform.org/en/ergo-wallet-app/) | Mobile |  | 🔗 | ✅ | ✅ |  |
| [SAFEW](https://ergoplatform.org/en/blog/2022-03-25-storing-ergo-safew/) | Web | ✅ | 🔗 | ✅ | 🔗 | ✅ |
| [Node Wallet](https://docs.ergoplatform.com/node/install/) | Desktop |  | ✅ |  |  |  |
| [Satergo](https://www.satergo.com) | Desktop |  | ✅ | 🔜 |  | 🔜 |
| [Minotaur](https://github.com/minotaur-ergo/minotaur-wallet) | Web |  |  | ✅ | 🔗 | 🔜 |
| [Paper Wallet](https://anon-br.github.io/ergo-paper-wallet/) | Cold |  |  |  |  |  |
| [Viawallet](https://apps.apple.com/us/app/viawallet-multi-chain-wallet/id1462031389) | Mobile |  |  |  |  |  |
| [URL Wallet](https://erg.urlwallet.org/) | URL |  |  |  |  |  |
| [Zelcore](https://erg.urlwallet.org/) | 3rd party |  |  |  |  |  |

## Wallets

### Nautilus (Web)

> Nautilus is a privacy-focused web-based wallet 

Ledger support is currently available [in developer mode for ledger](ledger.md)

### Ergo Wallet (Android) / Terminus (iOS)

Please see the official [wallet page](https://ergoplatform.org/en/mobile-wallets/). 

### Minotaur (Multi-Platform)

Minotaur is a multi-platform dApp wallet with _dApp stack support_, allowing any dApp to be embedded directly in the app. 


### SAFEW (Web)

> Simple And Fast Ergo Wallet is the most feature-rich wallet, best suited for developers. It has several features such as

- Ergopay-support
- Ledger Support
- Export CSV
- Configure Explorer, Node, and UI address used.
- ErgoMixer access
- Transaction builder in Expert mode (mint/burn/etc)
- Chained transactions

More information is available on their [GitHub](https://github.com/ThierryM1212/SAFEW)

### Satergo (Desktop) 

> Desktop wallet for the cryptocurrency Ergo with embedded node functionality. Available at [satergo.com](https://www.satergo.com)

More information is available on their [GitHub](https://github.com/Satergo/Satergo)


### [Node](install.md) (Server) 

The full node comes with a wallet panel interface. This is generally only recommended for developers. 

## Others

- [tesseract-one/ledger-app-ergo](https://github.com/tesseract-one/ledger-app-ergo)
- [anon-br/ledgerjs-hw-app-ergo](https://github.com/anon-br/ledgerjs-hw-app-ergo)
- [URL Wallet (Your key is in the URL, use this wallet for temporary use cases only!)](https://erg.urlwallet.org/)
- [Ergo Paper Wallet](https://anon-br.github.io/ergo-paper-wallet/)
- [SwiftAPI](https://github.com/ergoplatform/sigma-rust/blob/31aa0922d03f632d22fdc348b2604d23ed296586/bindings/ergo-wallet-ios/Sources/ErgoWallet/ErgoWallet.swift)
- iOS (Tethered) Beta | [Ergo Light Client](https://github.com/bjenkinsgit/ErgoIOSLiteClient.git) | Community | Requires a full node

