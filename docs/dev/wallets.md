# Choosing an Ergo Wallet

A wallet is your gateway to the Ergo ecosystem – it lets you securely store, send, and receive ERG and other tokens built on Ergo. Choosing the right wallet depends on your needs and how you plan to interact with Ergo.

<!-- Developer Note: This page currently resides under /dev/. Consider moving or creating a dedicated user-facing wallet page under a more accessible navigation path like /wallets/ or /introduction/wallets/. -->

**How to Choose?**

*   **For Mobile Users:** If you primarily use your phone, look at the **Mobile Wallets**.
*   **For Desktop Users:** If you prefer managing funds on your computer, check out **Desktop Wallets**.
*   **For Browser Interaction (dApps):** If you want to easily connect to Ergo applications (dApps) directly from your browser, consider a **Browser Extension Wallet**.
*   **For Maximum Security (Offline Storage):** For storing larger amounts long-term, a **Paper Wallet** or using the cold wallet features of mobile/desktop wallets is recommended.

/// details | Disclaimer
    {type: warning, open: true}
Please note that these wallets are developed and maintained by independent teams within the Ergo community. Always download from official sources and practice safe security habits. The information provided here is for guidance only.
///

## Recommended Wallets

Here are some popular and well-regarded wallets used by the Ergo community, grouped by type:

### Mobile Wallets (iOS & Android)

*   [**Ergo Mobile Wallet (Terminus on iOS):**](https://ergoplatform.org/en/ergo-wallet-app/) A user-friendly option for managing ERG and tokens on your smartphone. Supports NFTs, creating offline ("cold") wallets for extra security, and easy payment scanning (QR codes). A community favorite for mobile use.

*   [**Minotaur Wallet:**](minotaur.md) Offers multi-signature capabilities (requiring multiple approvals for transactions), which is useful for shared funds but might be more complex for beginners. *(Note: Installation might be more involved as it's under active development).*

### Browser Extension Wallets

*   [**Nautilus Wallet:**](nautilus.md) Very popular and widely used. Works as a browser extension (like MetaMask for Ethereum) allowing easy connection to Ergo dApps. Manages ERG, tokens, and NFTs. Includes features for privacy and optimizing transaction costs. Ideal for users frequently interacting with Ergo applications online.

### Desktop Wallets

*   [**Satergo Wallet:**](satergo.md) A desktop wallet designed to work with a full Ergo node (a copy of the blockchain running on your computer). Offers comprehensive features and is a good choice if you want to run your own node without complex configurations.

*   **Node Wallet:** The wallet built into the core Ergo node software. Generally recommended only for developers or advanced users running a node via command line. [Satergo](satergo.md) provides a more user-friendly interface for running a node wallet. *(Link points to node installation: [Node Install](https://docs.ergoplatform.com/node/install/))*

### Other Wallet Types

*   [**SAFEW Wallet:**](safew.md) A web-based wallet (accessed via a website) with advanced features, including integration with ErgoMixer (for privacy) and tools for developers. Suitable for more experienced users.

*   [**Ergo Paper Wallet:**](paper-wallet.md) A simple way to create a wallet offline for maximum security. You generate a key on paper (or save a file securely offline). Good for long-term storage ("cold storage") or gifting ERG, but less convenient for frequent transactions.

## Quick Comparison

| Wallet Type             | Platform(s)        | Ease of Use (Beginner) | Connects to dApps? | Good for Offline/Cold Storage? | Key Feature                                    |
|-------------------------|--------------------|------------------------|--------------------|--------------------------------|------------------------------------------------|
| Ergo Mobile / Terminus  | iOS, Android       | High                   | Limited (ErgoPay)  | Yes (via offline mode)         | Convenient mobile use, NFT support             |
| Nautilus                | Browser Extension  | Medium                 | Yes (Directly)     | No                             | Seamless dApp interaction, popular             |
| Satergo                 | Desktop (Win/Mac/Lin)| Medium                 | No                 | Yes (if PC is offline)         | User-friendly full node wallet                 |
| SAFEW                   | Web                | Medium-Low             | Yes (Directly)     | No                             | Advanced features, Mixer access                |
| Minotaur                | Mobile             | Medium-Low             | Limited (ErgoPay)  | Yes (via offline mode)         | Multi-signature security                       |
| Paper Wallet            | Offline Generation | N/A (Setup is simple)  | No                 | Yes (Primary purpose)          | Maximum security for long-term holding         |
| Node Wallet (Core)      | Desktop (Win/Mac/Lin)| Low                    | No                 | Yes (if PC is offline)         | Integrated with core node (Advanced users)     |

/// details | Advanced Feature Comparison
    {type: info, open: false}
    The table below provides a more detailed technical comparison. Note: *TBC* means the feature status needs confirmation.

    | Features                     | Satergo   | Nautilus |   Terminus   | Minotaur |  SafeW  | Node Wallet | Paper Wallet |
    |------------------------------|-----------|----------|--------------|----------|---------|-------------|--------------|
    | TX history                   | ✅        | ✅       | ✅           | ✅       | ✅      | ✅          | ❌           |
    | Configure node               | ✅        | ✅       | ✅           | ❌       | ✅      | ✅          | ❌           |
    | Configure explorer           | ✅        | ✅       | ✅           | ❌       | ✅      | ✅          | ❌           |
    | View-only wallet             | ❌        | ✅       | ✅           | ✅       | ✅      | ✅          | ❌           |
    | [ErgoPay](eip20.md)          | ✅        | ❌       | ✅           | ✅       | ✅      | ✅          | ❌           |
    | Input address selection      | ✅        | ❌       | ✅           | ✅       | *TBC*   | ✅          | ❌           |
    | Address management           | ✅        | ❌       | ✅           | ✅       | ❌      | ✅          | ❌           |
    | Chained TXs                  | ❌        | ✅       | ✅           | ❌       | ✅      | ✅          | ❌           |
    | Many price currencies        | ✅        | ✅       | ✅           | ❌       | ❌      | ❌          | ❌           |
    | NFT viewing                  | ❌        | ✅       | ✅           | ❌       | *TBC*   | ❌          | ❌           |
    | Token prices                 | ❌        | ✅       | ✅           | ❌       | ✅      | ❌          | ❌           |
    | Babel fees                   | ❌        | ✅       | ✅           | ❌       | *TBC*   | ✅          | ❌           |
    | Independent software         | ✅        | ❌       | ✅           | ✅       | ❌      | ✅          | ✅           |
    | Website dApps                | ❌        | ✅       | ❌           | ❌       | ✅      | ❌          | ❌           |
    | Ledger                       | ❌        | ✅       | ❌           | ❌       | ✅      | ❌          | ❌           |
    | Many price sources           | ✅        | ❌       | ❌           | ❌       | ❌      | ❌          | ❌           |
    | Mixer integration            | ❌        | ❌       | ❌           | ❌       | ✅      | ❌          | ❌           |
    | TX history export            | ❌        | ❌       | ❌           | ❌       | ✅      | ❌          | ❌           |
    | Multi-sig                    | ❌        | ❌       | ❌           | ✅       | ❌      | ✅          | ❌           |
    | Mnemonic password            | ✅        | ❌       | ❌           | ✅       | ❌      | ✅          | ❌           |
    | Full node                    | ✅        | ❌       | ❌           | ❌       | ❌      | ✅          | ❌           |
    | Add address at index         | ✅        | ❌       | ❌           | ❌       | ❌      | ✅          | ❌           |
    | Anti address reuse           | ❌        | ✅       | ❌           | ❌       | *TBC*   | ❌          | ❌           |
    | Sending to stealth addresses | ✅        | *TBC*    | *TBC*        | *TBC*    | *TBC*   | ✅          | ❌           |
///

/// details | Funds stuck in Yoroi?
    {type: warning, open: false}
If you have your Ergo wallet open in Yoroi and know the password for it, you can use [this tool](https://github.com/satsen/yoroi-ergo-wallet-recover) to decrypt the wallet and send all funds to a new wallet of yours. Alternatively, check the [access issues](access-issues.md) page for troublehooting other issues.
///


## Resources

- [Ergo Wallet Wonderland: Exploring the Best Wallet for Your Needs](./Ergo_Wallet_Wonderland_Exploring_Wallets__Needs.pdf)
- [SwiftAPI](https://github.com/ergoplatform/sigma-rust/blob/31aa0922d03f632d22fdc348b2604d23ed296586/bindings/ergo-wallet-ios/Sources/ErgoWallet/ErgoWallet.swift)
- iOS (Tethered) Beta | [Ergo Light Client](https://github.com/bjenkinsgit/ErgoIOSLiteClient.git) | Community | Requires a full node
