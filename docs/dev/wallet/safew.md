# SafeW

/// details | Disclaimer
    {type: warning, open: true}
The wallet is not actively maintaned, but still usable for those who desire the extra features offered.
///



[SafeW](https://github.com/ThierryM1212/SAFEW) is a Simple And Fast Ergo Wallet that integrates a dApp connector compatible with EIP-12. It is compatible with Chrome-based browsers (Opera, Brave, Edge, Kiwi, etc.) and Firefox. SAFEW was recognized in [ErgoHack](ergohack.md) 3.

It is ideal for developers because it provides access to the ErgoMixer, a transaction builder in Expert mode, and additional advanced features.

## Storing Ergo with SAFEW
Learn more about storing Ergo with SAFEW in this [blog post](https://ergoplatform.org/en/blog/2022-03-25-storing-ergo-safew/).
/// details | Comprehensive Video Guide
    {type: info, open: true}
For a visual and detailed guide on how to use SAFEW, watch the comprehensive video tutorial available [here](https://www.youtube.com/watch?v=DFf-dDlCpzM).
///


## Releases
- Chrome, Edge, Brave, etc: [Chrome Web Store](https://chrome.google.com/webstore/detail/simple-and-fast-ergo-wall/fmpbldieijjehhalgjblbpgjmijencll/)
- Firefox: [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/safew/)

## Features

- Multiple wallet types:
    - Mnemonic-based wallet for signing within the SAFEW extension.
    - Ergopay/Read-only wallet for signing with an Android/iOS wallet.
    - Ledger hardware wallet support.
- Account management in expert mode, including viewing addresses and their balance in ERG and tokens.
- Address discovery following BIP-44 to find used addresses and generate new ones.
- Transaction history for both confirmed and unconfirmed transactions.
- Unconfirmed balance display for each wallet, account, and address.
- Configuration options for Explorer, Node, and Explorer UI addresses.
- Direct interaction with ErgoMixer from the wallet.
- Transaction builder for advanced users to manipulate JSON of Ergo transactions.
    - Tutorials:
                - [How to mint tokens](https://youtu.be/YR0jkbMLaAY)
                - [How to burn tokens](https://youtu.be/OcyziMIXTtk)
                - [How to send assets to several addresses](https://youtu.be/3N7Qn2BgH0U)
- Export transaction history as CSV.
- Display and mint NFTs including pictures, audio, and videos.
- Burn tokens.
- Chained transactions: send another transaction as soon as the previous one is visible in the Explorer in an unconfirmed state.

## Security

Wallets are stored in the local storage of the SAFEW browser extension. The mnemonic is encrypted with AES-256 using the spending password, which is not stored in the application. The password is required for spending funds or managing addresses. ErgoPay wallets allow for remote transaction signing using iOS or Android wallet v1.6+, avoiding the need to store the encrypted mnemonic in the browser extension's local storage.

## Privacy
Address discovery can be initiated at any time to generate unused addresses. Non-connected sites cannot access wallet information, while connected sites can read the wallet content. The explorer and node used for interacting with the Ergo blockchain are configurable. ErgoPay/ReadOnly wallets enhance privacy by keeping wallet contents hidden. ErgoMixer integration facilitates the use of privacy tools.

## Reliability
The transaction balance displayed when sending funds with SAFEW is computed from the unsigned transaction, not from the UI inputs.


