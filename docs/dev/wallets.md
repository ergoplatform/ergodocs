# Wallets

Ergo offers a diverse array of wallets, with the [primary wallets](#primary-wallets) listed below being the most popular, representing 95% of all installations within the ecosystem.

/// details | Disclaimer
    {type: warning, open: true}
Please note that the wallets mentioned are maintained by external parties. The information provided here is for reference purposes only.
///

## Primary Wallets

1. [**Nautilus:**](nautilus.md) Nautilus is celebrated within the Ergo community for its widespread use and intuitive interface. Operating as a web-based browser extension, it facilitates seamless interaction with the Ergo ecosystem via a dApp connector, ensuring compatibility with a wide range of decentralized applications. Its extensive feature set includes asset management, NFT functionality, and transaction capabilities. A dedicated dApps section features a wallet optimization tool for UTXO consolidation, which helps reduce storage rent costs. Nautilus also provides a privacy mode and efficient management of connections to various Ergo ecosystem dApps.

2. [**Ergo Mobile Wallet (Terminus on iOS):**](https://ergoplatform.org/en/ergo-wallet-app/) This mobile wallet is a community favorite for its user-friendly interface on smartphones, allowing for smooth token and NFT exchanges. It supports the receipt, transfer, and storage of $ERG and NFTs. It also enables the creation of secure offline cold wallets in flight mode and the recovery of funds through any EIP3 compliant wallet. The Ergo Mobile Wallet includes read-only watch wallets with fiat value comparison and the ability to scan QR codes for easy payments.

3. [**Satergo:**](satergo.md) Satergo is a desktop node wallet tailored for the Ergo platform, offering an accessible solution for users who prefer to run a full node. It supports the Ergo network and provides comprehensive wallet features, making it a suitable option for those looking for both ease of use and advanced wallet functionalities.

For a detailed comparison of wallet features, refer to the [feature overview](#feature-overview) section further down this page.


## Secondary Wallets

1. [**Node Wallet:**](https://docs.ergoplatform.com/node/install/) This desktop wallet interfaces directly with the Ergo blockchain. For those not involved in development, Satergo is generally recommended as a more user-friendly alternative.
2. [**SAFEW Wallet:**](safew.md) SAFEW is a web-based wallet with integrated dApp and ErgoPay connectors, offering a robust set of tools for developers. It provides access to ErgoMixer, features an advanced transaction builder in Expert mode, and includes a range of sophisticated features.
3. [**Minotaur Wallet:**](minotaur.md) The Minotaur Wallet stands out for its multi-signature security feature, requiring multiple approvals for transaction execution, which increases security for shared wallet management and reduces the risk of centralized control. As it is still under development, installation on mobile devices may present some challenges.
4. [**Ergo Paper Wallet:**](paper-wallet.md) This paper wallet is designed for simplicity and ease of use, facilitating straightforward token transactions within the Ergo ecosystem. It is a self-custodial option that prioritizes security, allowing users to generate their wallet completely offline. The standalone file can be downloaded from GitHub, and users can generate their wallet by opening the file in a web browser without an internet connection, ensuring enhanced security. It is an excellent choice for gifting.

## Feature overview

| Features                     | Satergo   | Nautilus |   Terminus   | Minotaur |  SafeW  |
|------------------------------|-----------|----------|--------------|----------|---------|
| TX history                   | ✅        | ✅       | ✅           | ✅       | ✅      |
| Configure node               | ✅        | ✅       | ✅           | ❌       | ✅      |
| Configure explorer           | ✅        | ✅       | ✅           | ❌       | ✅      |
| View-only wallet             | ❌        | ✅       | ✅           | ✅       | ✅      |
| [ErgoPay](eip20.md)          | ✅        | ❌       | ✅           | ✅       | ✅      |
| Input address selection      | ✅        | ❌       | ✅           | ✅       | *TBC*   |
| Address management           | ✅        | ❌       | ✅           | ✅       | ❌      |
| Chained TXs                  | ❌        | ✅       | ✅           | ❌       | ✅      |
| Many price currencies        | ✅        | ✅       | ✅           | ❌       | ❌      |
| NFT viewing                  | ❌        | ✅       | ✅           | ❌       | *TBC*   |
| Token prices                 | ❌        | ✅       | ✅           | ❌       | ✅      |
| Babel fees                   | ❌        | ✅       | ✅           | ❌       | *TBC*   |
| Independent software         | ✅        | ❌       | ✅           | ✅       | ❌      |
| Website dApps                | ❌        | ✅       | ❌           | ❌       | ✅      |
| Ledger                       | ❌        | ✅       | ❌           | ❌       | ✅      |
| Many price sources           | ✅        | ❌       | ❌           | ❌       | ❌      |
| Mixer integration            | ❌        | ❌       | ❌           | ❌       | ✅      |
| TX history export            | ❌        | ❌       | ❌           | ❌       | ✅      |
| Multi-sig                    | ❌        | ❌       | ❌           | ✅       | ❌      |
| Mnemonic password            | ✅        | ❌       | ❌           | ✅       | ❌      |
| Full node                    | ✅        | ❌       | ❌           | ❌       | ❌      |
| Add address at index         | ✅        | ❌       | ❌           | ❌       | ❌      |
| Anti address reuse           | ❌        | ✅       | ❌           | ❌       | *TBC*   |
| Sending to stealth addresses | ✅        | *TBC*    | *TBC*        | *TBC*    | *TBC*   |
| **Total features**           | **12/24** | **12/24** | **13/24** | **8/24** | **11/24** |

## Other Wallets

These wallets are generally not recommended, but are left here for archival purposes.

1. [**Viawallet**](https://apps.apple.com/us/app/viawallet-multi-chain-wallet/id1462031389): A multi-chain wallet offering by CoinEx.
2. [**Zelcore**](https://erg.urlwallet.org/): A wallet provided by Flux, with third-party services.
3. [**URL Wallet**](https://erg.urlwallet.org/): A temporary wallet solution where your key is in the URL. Recommended for temporary use cases only due to security concerns.


/// details | Funds stuck in Yoroi?
    {type: warning, open: false}
If you have your Ergo wallet open in Yoroi and know the password for it, you can use [this tool](https://github.com/satsen/yoroi-ergo-wallet-recover) to decrypt the wallet and send all funds to a new wallet of yours. Alternatively, check the [access issues](access-issues.md) page for troublehooting other issues.
///


## Resources

- [Ergo Wallet Wonderland: Exploring the Best Wallet for Your Needs](./Ergo_Wallet_Wonderland_Exploring_Wallets__Needs.pdf)
- [SwiftAPI](https://github.com/ergoplatform/sigma-rust/blob/31aa0922d03f632d22fdc348b2604d23ed296586/bindings/ergo-wallet-ios/Sources/ErgoWallet/ErgoWallet.swift)
- iOS (Tethered) Beta | [Ergo Light Client](https://github.com/bjenkinsgit/ErgoIOSLiteClient.git) | Community | Requires a full node
