# How to sign transaction using backend wallet

There are many cases when it's required to sign a transaction on backend.

Use cases:

- NFT vending machine - mint token and send to user when the address gets funded
- Off-chain bot that withdraws funds from a contract.
  
In both cases, you may want to define a wallet on your backend to be able to sign those txs.
Here is a code reference on how it is done on the [dAppstep repo](https://github.com/nirvanush/dappstep-play/blob/main/src/services/WalletFromMnemonics.ts)


#### And here is how you can use it in your app:

```javascript
import SignerWallet from '../src/services/WalletFromMnemonics';

// example tx
const unsignedTx = {
  inputs: [...], 
  outputs: [...],
  ...
}

// You should never write the seedphrase in your code, always use a secret manager.
const wallet = await new SignerWallet().fromMnemonics('add your seed phrase of 12 words here');

const signedTx = wallet.sign(unsignedTx);

// Now you can submit this tx to mempool

```


#### References:
1. **Sigma-rust** https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm
2. **Sigma-rust discord** https://discord.com/channels/668903786361651200/729692906209673257

