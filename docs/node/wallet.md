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
owner: docs
last_reviewed: 2026-06-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - ergo-wallet/src/main/scala/org/ergoplatform/wallet/
      - src/main/scala/org/ergoplatform/nodeView/wallet/
      - src/main/scala/org/ergoplatform/http/api/WalletApiRoute.scala
      - src/main/scala/org/ergoplatform/http/api/WalletApiOperations.scala
source_of_truth:
  - https://github.com/ergoplatform/ergo/commit/d4ed37891cec
  - https://github.com/ergoplatform/ergo/tree/master/ergo-wallet/src/main/scala/org/ergoplatform/wallet
  - https://github.com/ergoplatform/ergo/tree/master/src/main/scala/org/ergoplatform/nodeView/wallet
  - https://github.com/ergoplatform/ergo/tree/master/src/main/scala/org/ergoplatform/http/api/WalletApiRoute.scala
  - https://github.com/ergoplatform/ergo/tree/master/src/main/scala/org/ergoplatform/http/api/WalletApiOperations.scala
---

## Initialize Wallet

To initialize the wallet, restart the node and navigate to the [panel](http://127.0.0.1:9053/panel) (Swagger UI). Set the API key using the secret phrase you configured previously. Remember to use the **plain text secret phrase**, not the hash stored in the configuration file. In our example, this is the string `hello`.

![set API key](https://user-images.githubusercontent.com/23208922/69916579-b7ca1680-1482-11ea-880e-251c8139a613.png)

Click on **Initialize wallet** (or execute the `/wallet/init` or `/wallet/restore` endpoint). A pop-up or response will appear depending on the method used. You have two main options:

1. **Initialize a new wallet**: If this is your first time running the node, choose this option to generate a new mnemonic sentence.
2. **Restore an existing wallet**: If you have an existing wallet (e.g., from a previous installation or another wallet software) and want to access its funds, choose this option and provide your previously saved mnemonic sentence.

Choose the option that suits your situation.

### Initialize Wallet from Scratch

![Initialize wallet](https://user-images.githubusercontent.com/23208922/69916584-d4fee500-1482-11ea-838c-e8aba9f41c76.png)

In the pop-up form (or API request body for `/wallet/init`), enter a secure password for encrypting your wallet file. The 'Mnemonic password' (BIP-39 passphrase) field is optional but adds extra security. After clicking 'Send' (or executing the request), the API response will contain the generated mnemonic sentence.

![mnemonic sentence](https://user-images.githubusercontent.com/23208922/69916693-2360b380-1484-11ea-9366-1bf9eb0f8b30.png)

Make sure to copy this sentence accurately and store it securely offline. You will need this exact sentence (and the optional passphrase, if used) to restore your wallet later or on a different device.

### Restore Wallet from Earlier

To restore an existing wallet, paste your previously saved mnemonic sentence into the 'Mnemonic' field in the Restore-wallet form (or the `mnemonic` field in the `/wallet/restore` API request). Enter a secure password to encrypt the restored wallet file. Leave the 'Mnemonic password' field empty unless your original mnemonic was created with a BIP-39 passphrase; in that case, enter the passphrase here.

![restore wallet](https://user-images.githubusercontent.com/23208922/71127599-66a37c00-2211-11ea-9b9e-9a69ac80c306.png)

After successfully restoring the wallet from the mnemonic sentence, you will see a confirmation message.

![successfully restored confirmation](https://user-images.githubusercontent.com/23208922/71127600-673c1280-2211-11ea-95eb-7c775c59180d.png)

### Get Wallet Addresses

To verify the wallet is initialized or restored correctly, you can retrieve its addresses. Using the Swagger UI panel, navigate to the `Wallet` section and execute the `/wallet/addresses` endpoint. The response should list at least one derived address if the wallet setup was successful.

Recent node versions also refresh the wallet's tracked public-key cache during initialization and restore. After either flow, `/wallet/deriveNextKey` can derive additional EIP-3 or legacy keys without losing the already tracked keys. Wallet restore remains disabled on pruned nodes.

![Get addresses](https://user-images.githubusercontent.com/23208922/69978955-5b82f780-1553-11ea-85b6-413c63a46334.png)

### Check Wallet Balance

Once the node is fully synchronized with the blockchain, you can check your wallet balance using the `/wallet/balances` endpoint in the Swagger UI.

Use `/wallet/balances/withUnconfirmed` when you need a balance that also accounts for unconfirmed transactions in the mempool.

![check balance](https://user-images.githubusercontent.com/23208922/71127598-66a37c00-2211-11ea-9d53-f6d7738d1726.png)

### Sending Funds

If your wallet has a non-zero balance, you can initiate transactions (e.g., sending ERG) using endpoints like `/wallet/payment/send` via the Swagger UI or other API clients.

Wallet box queries such as `/wallet/boxes` and `/wallet/boxes/unspent` support `minConfirmations=-1` when you want mempool boxes considered. For confirmed-only views, use a non-negative confirmation count.

Recent transaction-builder code validates supplied input IDs before constructing unsigned inputs. Input IDs must be valid hex strings of the expected modifier-ID length; malformed or too-short IDs are rejected instead of being silently dropped.

![send ergs](https://user-images.githubusercontent.com/23208922/71129066-a28c1080-2214-11ea-9806-7d768059980a.png)
