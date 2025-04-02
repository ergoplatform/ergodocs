---
tags:
  - Swagger
  - Node
  - API
  - REST API
  - UI
  - RPC Endpoints
---

# Swagger UI for Ergo Node

The Ergo node provides a REST API accessible via HTTP for interaction and control. The full API specification, following the OpenAPI standard, is available [here](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml). When the node is running, a user-friendly Swagger UI interface for exploring and interacting with the API is typically available at `127.0.0.1:9053/swagger` (assuming default port settings).

> Note: `127.0.0.1` refers to your local machine (localhost).

The Swagger UI allows you to perform advanced operations that might not be available through graphical wallet interfaces, such as:

1. Creating non-standard transactions with [registers](registers.md) and context variables.
2. Issuing tokens through transactions.
3. Creating transactions that use specific boxes as inputs.

## Accessing the API

Once the node is running, the API endpoints are typically accessible at `127.0.0.1:9053` (the default API port, distinct from the P2P port 9030).

To explore the API methods without setting up your own node, you can use the Swagger UI of public nodes, such as [http://213.239.193.208:9053/swagger](http://213.239.193.208:9053/swagger) or [http://159.65.11.55:9053/swagger](http://159.65.11.55:9053/swagger). (Note: Public node availability may vary).

To access protected API routes (like wallet operations), you must provide your API key (the secret phrase/password you set in the node configuration) in the `api_key` HTTP header of your requests. Alternatively, you can authorize your session directly within the Swagger UI interface by clicking the `Authorize` button and entering your API key there.

> Note: Most wallet-related and node-control methods in the API are protected. You will need to provide the correct API key (hashed using Blake2b in your configuration file) to access these methods.

## Authorization Process via Swagger UI

1.  Navigate to the Swagger UI page (e.g., `127.0.0.1:9053/swagger`).
2.  Click the green `"Authorize"` button located near the top right.
3.  A dialog box will appear. Enter your plain text API key (the secret phrase you configured) into the `Value` field.
4.  Click `"Authorize"` within the dialog, then `"Close"`.

Your browser session is now authorized to access protected endpoints.

For example, navigate to the `wallet/walletAddresses` endpoint, click `"Try it out"`, and then `"Execute"`. If authorized correctly, you should see the list of addresses managed by your node's wallet.

> Note: The Swagger UI authorization mechanism might appear to accept any input in the `Value` field. However, API calls to protected endpoints will fail if the provided API key does not match the `apiKeyHash` configured in your node. If you encounter authorization errors despite entering the correct key, potential causes include typos, incorrect hashing of the key in the config file, or, rarely, node database issues (try restarting the node first; a resync might be needed in severe cases).

## Main Methods

Here are some of the main methods you can use:

- `/wallet/init` and `/wallet/restore`: Initialize a new wallet (generates a secret mnemonic phrase) or restore an existing wallet from its mnemonic phrase.
- `/wallet/unlock`: Unlock the wallet using the configured wallet password (distinct from the API key). The wallet is typically unlocked automatically after initialization/restoration but locks upon node restart.
- `/wallet/lock`: Lock the wallet, requiring the wallet password for subsequent operations.
- `/wallet/payment/send`: Send a simple payment transaction.
- `/wallet/status`: Get the current status of the wallet (locked/unlocked).
- `/wallet/deriveNextKey`: Derive the next key/address according to the EIP-3 derivation path.
- `/wallet/balances`: Get the wallet's overall ERG and token balances across all tracked addresses.
- `/wallet/transactions`: Get a list of transactions relevant to the wallet's addresses.

### Example: Deriving Addresses

To derive a specific address, navigate to the `/wallet/deriveKey` endpoint, click *"Try it out"*, and enter the desired derivation path in the `derivationPath` field. For example, to derive the first standard address:

```bash
"derivationPath": "m/44'/429'/0'/0/0" 
```
