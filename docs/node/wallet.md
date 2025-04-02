---
tags:
  - Wallet
  - Node
  - API
  - Setup
  - Initialize
  - Restore
  - Unlock
  - Lock
  - Keys
  - BIP39
  - BIP32
---

## Initialize Wallet

To initialize the wallet, restart the node and navigate to the [panel](http://127.0.0.1:9053/panel). Set the API key secret from the previous step. Remember to use the **secret**, not the hash from the config file. In our example, this is the string `hello`. 

![set API key](https://user-images.githubusercontent.com/23208922/69916579-b7ca1680-1482-11ea-880e-251c8139a613.png)

Click on **Initialize wallet**. A pop-up will appear with two options:

1. **Initialize a new wallet**: If this is your first time running the node, you need to initialize it with a new mnemonic sentence.
2. **Restore an existing wallet**: If you have created a wallet before and want to access the same address (possibly because it contains funds), you need to restore the wallet using the previously saved mnemonic sentence. 

Choose the option that suits your situation. 

### Initialize Wallet from Scratch

![Initialize wallet](https://user-images.githubusercontent.com/23208922/69916584-d4fee500-1482-11ea-838c-e8aba9f41c76.png)

In the pop-up, enter a wallet password. The mnemonic password is optional. After clicking send, the wallet will return a mnemonic sentence. 

![mnemonic sentence](https://user-images.githubusercontent.com/23208922/69916693-2360b380-1484-11ea-9366-1bf9eb0f8b30.png)

Make sure to copy this sentence and store it in a safe place. You will need this sentence to restore the wallet on a different computer.

### Restore Wallet from Earlier

To restore a wallet, copy the previously saved mnemonic sentence and paste it into the "Mnemonic" field in the Restore-wallet form. Enter a secure wallet password. Leave the Mnemonic password field empty (it is only for advanced users). 

![restore wallet](https://user-images.githubusercontent.com/23208922/71127599-66a37c00-2211-11ea-9b9e-9a69ac80c306.png)

After successfully restoring the wallet from the mnemonic sentence, you will see a confirmation message.

![successfully restored confirmation](https://user-images.githubusercontent.com/23208922/71127600-673c1280-2211-11ea-95eb-7c775c59180d.png)

### Get Wallet Addresses

To ensure the node is set up properly, you can test it by retrieving the current addresses in the wallet. In the panel, click on the `Wallet` tab on the left and then on `Get all wallet addresses`. The wallet should return at least one address if the node is set up correctly.

![Get addresses](https://user-images.githubusercontent.com/23208922/69978955-5b82f780-1553-11ea-85b6-413c63a46334.png)

### Check Wallet Balance

Once the node is synced, you can check your balance using the wallet API in the panel.

![check balance](https://user-images.githubusercontent.com/23208922/71127598-66a37c00-2211-11ea-9d53-f6d7738d1726.png)

### Sending Funds

If your balance is non-zero, you can send Ergs to any other address using the panel.

![send ergs](https://user-images.githubusercontent.com/23208922/71129066-a28c1080-2214-11ea-9806-7d768059980a.png)
