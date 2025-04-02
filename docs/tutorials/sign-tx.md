---
tags:
  - Signing Transactions
  - Backend
  - Wallet
  - sigma-rust
  - NodeJS
  - Tutorial
  - Guide
---

# Signing Transactions Using a Backend Wallet

There are various scenarios where signing a transaction on the backend is necessary. This documentation provides instructions on how to accomplish this task using Ergo. We will outline two common use cases: NFT vending machine and off-chain bots that withdraw funds from contracts.

## Use Cases

### NFT Vending Machine

In this use case, you may need to mint a token and send it to a user when their address is funded. To achieve this, it is recommended to define a wallet on your backend that can sign the transactions. The following code snippet demonstrates how this can be done:

```javascript
import SignerWallet from '../src/services/WalletFromMnemonics';

// Example transaction
const unsignedTx = {
  inputs: [...], 
  outputs: [...],
  ...
}

// It is crucial to avoid storing the seed phrase in your code; always use a secret manager.
const wallet = await new SignerWallet().fromMnemonics('add your 12-word seed phrase here');

const signedTx = wallet.sign(unsignedTx);

// The signed transaction can now be submitted to the mempool.

```

### Off-Chain Bot

In this use case, an off-chain bot is responsible for withdrawing funds from a contract. Similar to the previous use case, you will need a backend wallet to sign the transactions. The code snippet below illustrates how to achieve this:

```javascript
import SignerWallet from '../src/services/WalletFromMnemonics';

// Example transaction
const unsignedTx = {
  inputs: [...], 
  outputs: [...],
  ...
}

// It is crucial to avoid storing the seed phrase in your code; always use a secret manager.
const wallet = await new SignerWallet().fromMnemonics('add your 12-word seed phrase here');

const signedTx = wallet.sign(unsignedTx);

// The signed transaction can now be submitted to the mempool.

```

## Additional References

1. **Sigma-rust** - For more details on Ergo's sigma-rust library, please refer to the [sigma-rust repository](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm).
2. **Sigma-rust Discord** - Join the [Sigma-rust Discord channel](https://discord.com/channels/668903786361651200/729692906209673257) to engage in discussions and receive support related to Ergo's sigma-rust library.
3. **dAppstep Repo** - Visit the [dAppstep repository](https://github.com/nirvanush/dappstep-play/blob/main/src/services/WalletFromMnemonics.ts) for further information on using the backend wallet for transaction signing.
