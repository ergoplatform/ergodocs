---
tags:
  - RPC Endpoints
---

# Swagger UI for Ergo Node

Ergo node provides a REST API that can be accessed via HTTP. The full API specification, in OpenAPI format, is available [here](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml). When the node is running, a user-friendly Swagger UI is available at `127.0.0.1:9053/swagger`.

> Note: `127.0.0.1` refers to your local machine.

The Swagger UI allows you to perform advanced operations that are not available in the panel, such as:

1. Creating non-standard transactions with [registers](registers.md) and context variables.
2. Issuing tokens through transactions.
3. Creating transactions that use specific boxes as inputs.

## Accessing the API

Once the node is running, the API can be accessed at `127.0.0.1:9052`. 

To explore the methods without setting up your own node, you can check out one of the public nodes, such as [204.48.31.129:9053/swagger#](http://204.48.31.129:9053/swagger#), [http://128.253.41.49:9053/swagger#](http://128.253.41.49:9053/swagger), etc. 

To access protected API routes, you must provide your secret phrase in the request headers `[api_key, Content-Type]`. Alternatively, you can authorize via the web interface in your browser by clicking the `Authorize` button in Swagger and entering your secret phrase there.

> Note: Most methods in the API are protected, and you will need to use your secret (that you configured earlier) to access these methods.

## Authorization Process

To authorize, navigate to the top of the Swagger UI page and click the `"Authorize"` button. Enter your secret in the form that pops up. After entering the secret and clicking `"Authorize"`, you should see a confirmation popup.

Now, in the same tab where you entered the password, navigate to `127.0.0.1:9053/swagger#/wallet/walletAddresses` and click `"Try it out"`. You should see the same list of addresses as you saw earlier from the panel.

> Note: Swagger will accept any password in the UI, but will fail to execute commands if the password provided is incorrect. If you are certain the password you're using is correct, this issue can occur during database corruption. First, attempt to restart and see if the node can fix itself. Otherwise, a resync will be required.

## Main Methods

Here are some of the main methods you can use:

- `/wallet/init` and `/wallet/restore`: Create a wallet (and a secret mnemonic) or restore a wallet from a mnemonic.
- `/wallet/unlock`: Unlock the wallet (it is unlocked after init but locked after restart).
- `/wallet/lock`: Lock the wallet.
- `/wallet/payment/send`: Send a simple payment.
- `/wallet/status`: Get wallet status.
- `/wallet/deriveNextKey`: Derive a new key according to EIP-3 (BIP 44 implementation for Ergo).
- `/wallet/balances`: Get wallet balance (for all the addresses).
- `/wallet/transactions`: Get wallet transactions (for all the addresses).

### Example: Deriving Addresses

To derive addresses, navigate to `localhost:9053/swagger#/wallet/walletDeriveKey` and click *Try it out*. Enter the following in the `derivationPath` field:

```bash
"derivationPath": "m/44'/429'/0'/0/0" 
```





