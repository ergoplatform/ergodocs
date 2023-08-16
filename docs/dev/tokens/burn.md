# Burning a token

There are sometimes occasions when you want to delete a token from your wallet. 

- Your address was airdropped a token you no longer want
- You created an NFT but something about it is not right. 
- A project sent you voting or other tokens that you no longer need

To get rid of those tokens, you have a few options.

- **Mobile Wallet:** [TokenJay](https://www.tokenjay.app/app/#burntoken) (This requires an Ergopay compatible wallet like Ergo Mobile Wallet)
- **Nautilus:** [Ergo Token Minter / Burner](https://github.com/ThierryM1212/ergo-token-minter)
- **[SAFEW](https://github.com/ThierryM1212/SAFEW)** supports token burning natively.
- Send to `4MQyMKvMbnCJG3aJ`, a **[P2S (Pay-to-Script)](p2s.md)** representation of a “false” condition, i.e. the box is unspendable. <!--TODO: What? Hash is written into `R4` register of the box, in the explorer It looks like `0e2047ee2cbd52be01e0876c3e0b989a0d4d5f8955200b1fab0e6eeb2b182555c2fb`, where `0e` is type descriptor (byte array), `20` is bytestring length (0x20 in hex = 32), `47ee2cbd52be01e0876c3e0b989a0d4d5f8955200b1fab0e6eeb2b182555c2fb` is the hash of the file. --->


## Programmatically

To burn tokens programmatically, simply spend an Unspent Transaction Output (UTXO) containing the tokens you wish to eliminate. Ensure not to include these tokens in the output of the transaction.

### Using AppKit

If you're working with [AppKit](appkit.md), the transaction builder conveniently offers a `burntoken` method tailored for this purpose.

### Ergo Token Minter Integration

The burn token functionality integrated by `ThierryM1212` can be observed [here](https://github.com/ThierryM1212/ergo-token-minter/blob/main/src/index.js#L254). The crucial steps involved are as follows:

1. Identify and select the input boxes holding the tokens to be burnt, along with a small ERG amount.
2. Construct the output boxes, excluding consideration of the tokens. The transaction builder automatically appends an additional output change box encompassing all tokens.
3. Retrieve the transaction JSON representation.
4. Edit the output change box details to eliminate the tokens intended for burning.
5. Dispatch the modified transaction (JSON) to the network.

This streamlined approach simplifies the process of burning tokens while maintaining transaction integrity.