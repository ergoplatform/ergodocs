## Burning

There are sometimes occasions where you want to delete a token out of your wallet. Common reasons include:

- Your address was airdropped a token you no longer want
- You created an NFT but something about it is not right. So, you want to delete one you created to remint it
- A project sent reserve, voting or other tokens that you no longer need

To delete tokens from your Ergo wallet, you have a few options.



### P2S

`4MQyMKvMbnCJG3aJ` is a P2S (Pay-to-Script) representation of “false” condition, i.e. the box is unspendable. Hash is written into R4 register of the box, in the explorer 

> It looks like `0e2047ee2cbd52be01e0876c3e0b989a0d4d5f8955200b1fab0e6eeb2b182555c2fb`, where `0e` is type descriptor (byte array), `20` is bytestring length (0x20 in hex = 32), `47ee2cbd52be01e0876c3e0b989a0d4d5f8955200b1fab0e6eeb2b182555c2fb` is the hash of the file.

### Services

- [TokenJay](https://www.tokenjay.app/app/#burntoken) (This requires a Ergopay compatible wallet like Ergo Mobile Wallet)
- [Ergo Token Minter / Burner](https://github.com/ThierryM1212/ergo-token-minter) (Possible with a Ergo wallet extension, such as Nautilus)

## Programmatically

Just spend an UTXO with tokens you want to burn and do not include them into output. (for custom tokens sum in outputs can be less than sum in inputs, for ERG, strict equality is required). 


### AppKit

- Transaction builder has a `burntoken` method.

### Ergo Token Minter

The burn token feature I implemented is visible [here](https://github.com/ThierryM1212/ergo-token-minter/blob/main/src/index.js#L254), the important steps to me are:

1. Select the input boxes for the amount of tokens to burn and a small amount of ERG
2. Create the output boxes without considering the tokens, the transaction builder will create an additional output change box including all the tokens
3. Get the transaction json
4. Re-write the output change box in order to remove the tokens you want to burn
5. Send the modified transaction (json)

