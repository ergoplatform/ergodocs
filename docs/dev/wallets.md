---
title: Choosing an Ergo Wallet
description: An overview of recommended Ergo wallets for different platforms and use cases, including mobile, desktop, browser extensions, and cold storage.
tags:
  - Wallet
  - Mobile Wallet
  - Desktop Wallet
  - Browser Extension
  - Cold Storage
  - Security
  - Getting Started
---

# Choosing an Ergo Wallet

A wallet is your essential gateway to the Ergo ecosystem. It allows you to securely store, send, and receive ERG and other [tokens](tokens.md) built on Ergo, as well as interact with [decentralized applications (dApps)](get-started.md). Choosing the right wallet depends on your technical comfort, security needs, and how you plan to use Ergo.

<!-- Developer Note: This page provides a general overview suitable for all users, despite its location under /dev/. -->

!!! warning "Disclaimer"
    The wallets listed here are primarily developed and maintained by independent teams within the Ergo community. Always download software from official sources linked here and practice strong security habits (like safeguarding your seed phrase). This information is for guidance only; conduct your own research before entrusting funds to any wallet.

## How to Choose a Wallet?

Consider these common needs:

*   **📱 Mobile Use:** If you need access to your funds primarily on your smartphone (iOS or Android), look at **Mobile Wallets**.
*   **💻 Desktop Management:** If you prefer managing funds on your computer (Windows, macOS, Linux), check out **Desktop Wallets**.
*   **🌐 dApp Interaction:** If you plan to frequently interact with Ergo dApps directly through your web browser, a **Browser Extension Wallet** is often the most convenient.
*   **🔒 Maximum Security / Long-Term Storage:** For storing significant amounts of ERG or holding funds offline ("cold storage"), consider a **Paper Wallet** or the offline/cold wallet features available in some mobile/desktop wallets.

## Recommended Wallets by Type

Here are popular and well-regarded wallets used by the Ergo community:

### Mobile Wallets (iOS & Android)

*   **[Ergo Mobile Wallet (Terminus on iOS)](https://ergoplatform.org/en/ergo-wallet-app/)**
    *   **Description:** A user-friendly, feature-rich mobile wallet. Supports ERG, tokens, NFTs, creating offline ("cold") wallets, and ErgoPay QR code scanning. A community favorite.
    *   **Best For:** Everyday mobile use, managing diverse assets, easy payments.

*   **[Minotaur Wallet](wallet/minotaur.md)**
    *   **Description:** Offers advanced features like [multi-signature](multi.md) capabilities (requiring multiple approvals for transactions).
    *   **Best For:** Users needing shared fund control or enhanced security via multi-sig. May be more complex for beginners. *(Note: Check development status for latest features/stability).*

### Browser Extension Wallets

*   **[Nautilus Wallet](wallet/nautilus.md)**
    *   **Description:** A very popular browser extension wallet (similar to MetaMask). Enables seamless connection to Ergo dApps. Manages ERG, tokens, and NFTs. Includes privacy features and transaction optimization.
    *   **Best For:** Users frequently interacting with DeFi, NFT marketplaces, and other web-based Ergo applications.

### Desktop Wallets

*   **[Satergo Wallet](wallet/satergo.md)**
    *   **Description:** A desktop wallet specifically designed to run alongside a full [Ergo Node](../node/install.md). Provides a user-friendly interface for managing funds while contributing to network decentralization.
    *   **Best For:** Users who want to run their own full node for maximum trust and verification, without needing complex command-line interaction.

*   **Node Wallet (Core)**
    *   **Description:** The basic wallet functionality built into the core Ergo reference node software. Accessed via command line or API.
    *   **Best For:** Developers or advanced users comfortable with command-line interfaces who are already running a core node. [Satergo](wallet/satergo.md) offers a graphical alternative for node users.

### Other Wallet Types

*   **[SAFEW Wallet](wallet/safew.md)**
    *   **Description:** A web-based wallet (accessed via a website, requires careful URL verification). Offers advanced features like ErgoMixer integration (for enhanced privacy) and developer tools.
    *   **Best For:** Experienced users needing specific features like mixing or advanced transaction control.

*   **[Ergo Paper Wallet](wallet/paper-wallet.md)**
    *   **Description:** A method to generate wallet keys offline and print them on paper (or save securely offline). Provides maximum security from online threats.
    *   **Best For:** Long-term "cold storage" of significant amounts, gifting ERG. Less convenient for frequent use.

## Quick Comparison Table

This table provides a simplified overview to help you compare options:

| Wallet Type             | Platform(s)        | Ease of Use (Beginner) | Connects to dApps? | Good for Offline/Cold Storage? | Key Feature                                    |
|-------------------------|--------------------|------------------------|--------------------|--------------------------------|------------------------------------------------|
| Ergo Mobile / Terminus  | iOS, Android       | High                   | Limited (ErgoPay)  | Yes (via offline mode)         | Convenient mobile use, NFT support             |
| Nautilus                | Browser Extension  | Medium                 | Yes (Directly)     | No                             | Seamless dApp interaction, popular             |
| Satergo                 | Desktop (Win/Mac/Lin)| Medium                 | No                 | Yes (if PC is offline)         | User-friendly full node wallet                 |
| SAFEW                   | Web                | Medium-Low             | Yes (Directly)     | No                             | Advanced features, Mixer access                |
| Minotaur                | Mobile             | Medium-Low             | Limited (ErgoPay)  | Yes (via offline mode)         | Multi-signature security                       |
| Paper Wallet            | Offline Generation | N/A (Setup is simple)  | No                 | Yes (Primary purpose)          | Maximum security for long-term holding         |
| Node Wallet (Core)      | Desktop (Win/Mac/Lin)| Low                    | No                 | Yes (if PC is offline)         | Integrated with core node (Advanced users)     |

!!! details "Advanced Feature Comparison (Expand)"
    The table below provides a more detailed technical comparison based on community contributions. Note: *TBC* means the feature status needs confirmation.

    | Features                     | Satergo   | Nautilus |   Terminus   | Minotaur |  SafeW  | Node Wallet | Paper Wallet |
    |------------------------------|-----------|----------|--------------|----------|---------|-------------|--------------|
    | TX history                   | ✅        | ✅       | ✅           | ✅       | ✅      | ✅          | ❌           |
    | Configure node               | ✅        | ✅       | ✅           | ❌       | ✅      | ✅          | ❌           |
    | Configure explorer           | ✅        | ✅       | ✅           | ❌       | ✅      | ✅          | ❌           |
    | View-only wallet             | ❌        | ✅       | ✅           | ✅       | ✅      | ✅          | ❌           |
    | ErgoPay (EIP-0020)           | ✅        | ❌       | ✅           | ✅       | ✅      | ✅          | ❌           |
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

!!! warning "Funds stuck in Yoroi?"
    Yoroi wallet no longer supports Ergo. If you have funds in an old Yoroi Ergo wallet and know the password, you might be able to use [this community recovery tool](https://github.com/satsen/yoroi-ergo-wallet-recover) to send funds to a new Ergo wallet. Alternatively, check the [access issues guide](access-issues.md) for other troubleshooting tips.

## Additional Resources

*   **PDF Guide:** [Ergo Wallet Wonderland: Exploring the Best Wallet for Your Needs](./Ergo_Wallet_Wonderland_Exploring_Wallets__Needs.pdf) (May require update)
*   **Developer:** [SwiftAPI for iOS Wallet Dev](https://github.com/ergoplatform/sigma-rust/blob/31aa0922d03f632d22fdc348b2604d23ed296586/bindings/ergo-wallet-ios/Sources/ErgoWallet/ErgoWallet.swift)
*   **Community Project:** [Ergo Light Client (iOS Beta)](https://github.com/bjenkinsgit/ErgoIOSLiteClient.git) (Requires a full node)
