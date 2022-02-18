# Wallets

|    Wallet    |   Type  | Native assets | Multisig | Scripts | Ledger | Mixer |
|:------------:|:-------:|:-------------:|:--------:|:-------:|--------|-------|
| Nautilus     | Web     | Yes           |          |         | Soon   | Soon  |
| Ergo Wallet  | Mobile  | Yes           |          |         |        |       |
| SAFEW        | Web     | Yes           |          |         | Soon   | Yes   |
| Node Wallet  | Desktop | Yes           | Yes      | Yes     |        |       |
| Satergo      | Desktop | Yes           |          |         | Soon   | Soon  |
| Minotaur     | Web     | Yes           |          | Yes     |        |       |
| Paper Wallet | Cold    | Yes           |          |         |        |       |
| Viawallet    | Mobile  | Yes           |          |         |        |       |

Note that some wallets are supported by third parties, we only provide the information below as a courtesy.

For interacting with dApps the best solution is to use [Nautilus](https://github.com/capt-nemo429/nautilus-wallet) which is available on the chrome extension store.

## Web Wallets

### Nautilus

### Yoroi

Yoroi is a light-wallet built by Emurgo, a founding partner of Cardano. 

[Yoroi Frontend GitHub](https://github.com/Emurgo/yoroi-frontend)


## Mobile Wallets

### Ergo Wallet

Please see the official wallet [https://ergoplatform.org/en/wallets/](wallet page). 

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
