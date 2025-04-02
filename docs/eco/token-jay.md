---
tags:
  - Token Jay
  - P2P Trading
  - Escrow
  - SigmaUSD
  - SigmaRSV
  - Token Burner
  - dApp
---

# Token Jay

## Overview

Token Jay is your one-stop solution for dealing with tokens on Ergo. It offers open, fully documented applications that are accessible to everyone.

You can trade tokens in a trustless and decentralized manner using TokenJay's open P2P Escrow service. Visit [tokenjay.app](https://tokenjay.app/) to get started. Please note that you will need an ErgoPay compatible Wallet Application.

### Tools Available on TokenJay:

#### P2P Escrow

The open P2P Escrow service is a smart contract that facilitates trustless, private sales on the Ergo blockchain for a nominal fee. The contract accepts Ergo tokens, such as a non-fungible token (NFT), 100 SigUSD, or other token(s) from the seller. Once the tokens are in the contract, only a defined buyer sending a defined amount of ERG can access them. If the exchange is successful, the contract sends the tokens to the buyer and the ERG to the seller. The seller can cancel the contract at any time before the exchange is made. 

##### How to use P2P Escrow:

1. Visit [TokenJay](http://tokenjay.app)
2. Connect your wallet by scanning the QR code
3. Navigate to 'Your Token Sales'
4. Click 'Start New Sale'
5. Select the vesting key from your wallet
6. Enter the buyer's address
7. Set the price the buyer should pay (in $ per SPF token, converted into Erg)
8. Click 'Sell Token'
9. Sign the transaction

Once the transaction is confirmed, the buyer can make the purchase via TokenJay. The offer will appear under 'P2P Escrow offers'. The buyer should verify the token and minting transaction to ensure its authenticity. If it's an Ergopad vesting key, they can verify the tokenid in the verifier API:

[https://api.ergopad.io/vesting/vestedWithKey/tokenid](https://api.ergopad.io/vesting/vestedWithKey/tokenid)

This will return whether it is a real key, the token type, and the number of tokens. If everything checks out, they can click 'Buy' and sign the transaction.

Once the transaction is processed, the Erg is sent to the seller, the key is sent to the buyer, and the contract takes a small fee.

For more information, visit [https://tokenjay.app/escrow.html](https://tokenjay.app/escrow.html)

#### SigUSD and SigRSV

With TokenJay, you can convert ERG into SigUSD and SigRSV directly with the bank in a single transaction. Visit [https://tokenjay.app/ageusd.html](https://tokenjay.app/ageusd.html) for more details.

#### Utilities

TokenJay also offers a Token Burner utility that allows you to burn unwanted NFTs and tokens. Visit [https://tokenjay.app/app/#burntoken](https://tokenjay.app/app/#burntoken) to use this utility.
