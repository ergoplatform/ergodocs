# Minotaur Wallet

[Minotaur](https://github.com/minotaur-ergo/minotaur-wallet) stands as the inaugural multi-platform wallet tailored for the Ergo ecosystem, offering a suite of features designed to enhance user experience.

/// details | Comprehensive Video Guide
    {type: info, open: true}
For a visual and detailed guide on how to use Minotaur, watch the comprehensive video tutorial available [here](https://www.youtube.com/watch?v=cUs2EXxNn7s).
///

## Key Features:

- Wallet generation and restoration compatible with Yoroi, Ergo node, and Ergo's Android app.
- Supports mnemonic phrases of various lengths: 12, 15, 18, 21, and 24 words.
- Mnemonic passphrase for additional security.
- Read-only wallet functionality.
- Integration with [cold wallet devices](https://github.com/ergoplatform/ergo-wallet-app/wiki/Cold-wallet).
- Token and NFT management:
    - Displays token names as per [EIP-04](https://github.com/ergoplatform/eips/blob/master/eip-0004.md) standards.
    - Facilitates token transactions.
    - Enables issuing and burning of tokens within dApps.
- Transaction display within the wallet, including pre-signing transaction previews.
- Embedded dApp support, with three dApps currently available for token issuance, token burning, and sigma-usd operations.
- Cross-platform support for Android, iOS, Windows, MacOS, and Linux.
- Wallet encryption via user-defined password.
- ErgoPay integration for seamless transactions.

## Upcoming Features:

- Dynamic dApp integration protocol to add new dApps without requiring wallet updates.
- Minotaur dApp connector extension for Chrome and Firefox.
- Multilingual wallet interface.
- Mempool transaction monitoring.

[comment]: <> (Android 7 or iOS 13 is the minimum requirement to run Ergo Wallet.)

[comment]: <> (For feedback, join the conversation on [Ergo Discord](https://discord.gg/kj7s7nb).)

## Building the Wallet from Source

Ensure Node.js version 20.11 is installed before attempting to build Minotaur:

1. Clone the repository:
   ```
   git clone git@github.com:minotaur-ergo/minotaur-wallet.git
   ```
2. Navigate to the cloned directory and install dependencies:
   ```
   cd minotaur-wallet
   npm install
   ```
3. Build the project with the following commands:
   ```
   npm run build
   npx cap sync
   npx cap update
   ```
   The last two commands synchronize the codebase for Android and iOS platforms. For desktop builds, synchronize the Electron code with:
   ```
   npx cap sync electron
   npx cap update electron
   ```

## Platform-Specific Builds

### Android
Open the `android` directory within the project using Android Studio and proceed with the build process using the IDE or alternative build tools.

### iOS
iOS developers can open the project in Xcode and build the desired version directly from the IDE.

### Desktop
For desktop builds, enter the Electron directory and execute the following commands:
   ```
   npm run build
   npm run electron:pack
   npm run electron:make
   ```

### MacOS
Apple Silicon (M-series) users should opt for the `arm64` build to avoid camera issues. If encountering a "_damaged file_" error, execute:
   ```
   sudo xattr -r -d com.apple.quarantine /Applications/minotaur.app
   ```

## Support the Developer

Contributions are appreciated and help fuel ongoing development. To tip the developer, send your support to:
[9hN2UY1ZvvWMeWRBso28vSyjrAAfGJHh2DkZpE47J7Wqr51YLAR](https://explorer.ergoplatform.com/payment-request?address=9hN2UY1ZvvWMeWRBso28vSyjrAAfGJHh2DkZpE47J7Wqr51YLAR&amount=0&description=)

## Testnet Trials

Minotaur is compatible with both Mainnet and Testnet. To test the wallet, generate a new wallet and acquire test Ergos from [Ergo's Testnet Faucet](https://testnet.ergofaucet.org/).
