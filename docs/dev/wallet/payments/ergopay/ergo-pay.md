---
tags:
  - dApp Development
---

# ErgoPay

ErgoPay, Ergo's dApp connector for non-web wallet applications is now ready to use and test by end-users.

Probably many of you think of a dApp connector as something connecting between a website-based dApp and a browser extension wallet, like Yoroi and Metamask do it with website dApps. Not everyone wants to use a web extension wallet, and not every dApp is a website. That's why we came up with ErgoPay, which can connect every kind of wallet with every kind of dApp. Some more information about the technical background for non-developers [can be found here](https://www.reddit.com/r/ergonauts/comments/sc9lbk/comment/hu9v6dk/?utm_source=share&utm_medium=web2x&context=3).

ErgoPay is implemented in **Ergo Wallet App 1.6**, and a first showcase dApp to mint and burn tokens is live now. 

Keen to try it out? Here's how!

1. Make sure you have installed Ergo Wallet App 1.6. It's currently not rolled out to all users, but in open beta on Google Play ([join](https://play.google.com/apps/testing/org.ergoplatform.android)) and in closed beta on TestFlight (DM me your Apple ID to join). Or [download the APK on GitHub](https://github.com/ergoplatform/ergo-wallet-app/releases) and sideload.
2. Head over and open the showcase app: [https://golfgl.de/ergopayshowcase/](https://golfgl.de/ergopayshowcase/)  
You can do this on your mobile device or on your desktop - ErgoPay works both on the same device, or on different devices. This way, you can use a dApp where it's most convenient for you, and use the wallet where you prefer. ErgoPay even supports Cold wallets,  try it!
1. The showcase dApp has a menu on the left side to choose what functionality to use: mint a new token, or burn a token. The dApp works both on testnet and mainnet. It will automatically detect this through the information delivered by ErgoPay. Let's start with minting a token.
2. Enter the information for your awesome token. When done, scan the presented QR code with your wallet app if you are on desktop. If you are on mobile, tap the button to open the wallet app. The wallet app will ask with what wallet the request should be processed, and a confirmation screen will show you what will happen when you confirm: Your new token is minted, and the tx fee of 0.001 will be withdrawn. This is probably the cheapest way to mint a token on the Ergo blockchain.
3. Confirm the transaction and enjoy your new token when the transaction is confirmed. (*BTW: Emojis in the token name are supported.)*
4. When you want to get rid of your token or a spam token someone sent you, choose the "Burn a token" functionality from the showcase dApp. For burning a token, the dApp needs to connect your wallet to show you a list of available tokens to burn. Do it by scanning the QR code or tapping the button.
5. Your wallet will be connected within seconds and you can choose the token to burn. Important: You can burn every token, so don't choose tokens of value. (Or do if you usually burn cash as well.)
6. Same procedure as before: Scan QR or tap the wallet button, and confirm the tx to burn a token. This is the cheapest way to get rid of spam tokens, sending them away costs more!

Have fun! We hope other dApps will implement ErgoPay protocol soon!

## Implement a dApp using ErgoPay

Ergo Wallet App 1.6 and above supports ErgoPay, a protocol to interchange transaction data with dApps. Using it, your dApp can prepare a transaction for the user to sign inside his wallet app. The user can accept signing the transaction, or decline it. This way, you as a dApp developer are flexible in building transactions and don’t need to rely on how a wallet might generate a transaction, while your dApp user is safe because his secrets never leave his device and can check what transaction will be issued before confirming it.

### ErgoPay vs web dApp connector

What’s the difference between ErgoPay and a web dApp connector Yoroi and Nautilus wallet provide? ErgoPay can connect every kind of wallet with every kind of dApp, while a web dApp connector is restricted to web extension wallets and website dApps. It can only connect processes living in the same web browser.
Because you don’t know which type of wallet application will connect to your dApp, a part of your logic must run on a server open to be connected by user’s wallet applications. For a website dApp it means that some of your code needs to live on your backend. This doesn’t make things more complicated — on the contrary, on the backend, you aren’t restricted to using JavaScript or derivates, but are free to choose the language and framework that fits your needs the bests.

## Resources

- [ergopay-payment-portal](https://github.com/MrStahlfelge/ergopay-payment-portal)