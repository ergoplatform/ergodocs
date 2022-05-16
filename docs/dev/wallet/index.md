# Wallets

Note that wallets are supported by third parties, we only provide the information below as a courtesy.

| Wallet                                                                                                 | Type    | dApp-C | Full Node | Ledger | [E-Pay](https://github.com/ergoplatform/eips/blob/master/eip-0020.md) | Tokens | [Mixer](https://docs.ergoplatform.com/uses/mixer/#ergomixer) |   |
|--------------------------------------------------------------------------------------------------------|---------|--------|-----------|--------|-----------------------------------------------------------------------|--------|--------------------------------------------------------------|---|
| [Nautilus](https://chrome.google.com/webstore/detail/nautilus-wallet/gjlmehlldlphhljhpnlddaodbjjcchai) | Web     | ✅      |           | ✅      |                                                                       | ✅      | 🔜                                                            |   |
| [Ergo Wallet](https://ergoplatform.org/en/mobile_wallets/)                                             | Mobile  |        | 🔗         | 🔜      | ✅                                                                     | ✅      |                                                              |   |
| [SAFEW](https://ergoplatform.org/en/blog/2022-03-25-storing-ergo-safew/)                               | Web     | ✅      |           | ✅      | ✅*                                                                    | ✅      | ✅                                                            |   |
| [Node Wallet](https://docs.ergoplatform.com/node/platforms/)                                           | Desktop |        | ✅         |        |                                                                       | ✅      |                                                              |   |
| [Satergo](https://www.satergo.com)                                                                     | Desktop |        |           | 🔜      |                                                                       | ✅      | 🔜                                                            |   |
| [Minotaur](https://github.com/minotaur-ergo/minotaur-wallet)                                           | Web     |        |           |        |                                                                       | ✅      | 🔜                                                            |   |
| [Paper Wallet](https://anon-br.github.io/ergo-paper-wallet/)                                           | Cold    |        |           |        |                                                                       | ✅      |                                                              |   |
| [Viawallet](https://apps.apple.com/us/app/viawallet-multi-chain-wallet/id1462031389)                   | Mobile  |        |           |        |                                                                       | 🚫      |                                                              |   |
| [URL Wallet](https://erg.urlwallet.org/)                                                               | URL     |        |           |        |                                                                       | ?      |                                                              |   |
| [Yoroi](https://yoroi-wallet.com/)                                                                     | Web     | ✅      |           |        |                                                                       | ✅      |                                                              |   |

## Web Wallets

### Nautilus

### Yoroi

Yoroi is a light-wallet built by Emurgo, a founding partner of Cardano. 

[Yoroi Frontend GitHub](https://github.com/Emurgo/yoroi-frontend)


## Mobile Wallets

### Ergo Wallet

Please see the official wallet [wallet page](https://ergoplatform.org/en/mobile_wallets/). 

## Desktop

### Satergo

As an alternative to the full-node on desktop, there is a JVM wallet available at [satergo.com](https://www.satergo.com)

### [Node](/node)

The node comes with a wallet panel interface. 


## Hardware

- Ledger Support in development (see below)  | Tesseract & Yoroi

- [tesseract-one/ledger-app-ergo](https://github.com/tesseract-one/ledger-app-ergo)
- [anon-br/ledgerjs-hw-app-ergo](https://github.com/anon-br/ledgerjs-hw-app-ergo)

Here is [a guide](https://putukusuma.medium.com/build-an-app-for-ledger-nano-s-on-macbook-and-docker-46be51701206) on how to deploy it on the device (just skip the docker part): 

## Misc

- [URL Wallet (Your key is in the URL, use this wallet for temporary use cases only!)](https://erg.urlwallet.org/)
- [Ergo Paper Wallet](https://anon-br.github.io/ergo-paper-wallet/)
- [SwiftAPI](https://github.com/ergoplatform/sigma-rust/blob/31aa0922d03f632d22fdc348b2604d23ed296586/bindings/ergo-wallet-ios/Sources/ErgoWallet/ErgoWallet.swift)
- iOS (Tethered) Beta | [Ergo Light Client](https://github.com/bjenkinsgit/ErgoIOSLiteClient.git) | Community | Requires a full node
