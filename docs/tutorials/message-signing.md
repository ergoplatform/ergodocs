
---
tags:
  - Message Signing
  - Authentication
  - Nautilus
  - sigma-rust
  - Wallet
  - Security
  - Tutorial
  - Guide
---

# Message signing and user authentication with Nautilus wallet and sigma-rust

Did you know that besides transactions you can sign any piece of data?
Here is how you do it using Nautilus wallet
```javascript
const message = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
const signature = ergo.sign_data('<your_addr>', message);
```

Yeah… but why? you may ask.
Well, because now you can post it to your NodeJS backend application and do this, using sigma-rust:

```javascript
import * as ergoWasm from 'ergo-lib-wasm-nodejs'
const isValid = ergoWasm.verify_signature(addr, message, signature);
if (isValid) { // authenticated!!! }
```

This is called wallet authentication - the way to verify that the user/client is the owner of the address he is claiming to be.

In SigmaValley we allow NFT owners to edit their plot information and upload custom models. So if isValid === true and the backend knows that the request came from the wallet owner, I can now request all the tokens on that address and provide the client with access to protected functionality or data.

```javascript
const balance = await request
  .get(`https://api.ergoplatform.com/api/v1/addresses/${addr}/balance/confirmed`)
  .then(res => res.body);
if (balance.tokens.find(token => token.tokenId === '<valid token>') {
   // Allow user break SigmaValley
}
```

You can use the same method to allow your users to upload their NFT as a character in your game or build an NFT-based ticketing system, the uses are limitless. 

## Next steps/security tips

1. **User expiration mechanism** - The example above is very simplified, you can use it right away, but for more secure applications you may consider implementing some message expiration mechanism. Instead of signing a random message, you can include an expiration date to it and force users to sign a new message once in a while. You can also switch to a more popular JTW token authentication once the user is verified.
2. **Check the token balance on every request** - it's not enough to check whether the user holds the NFT only once. The user can get access and sell his NFT to someone else. It's a good idea to move the balance check and the verification to authentication middleware to be executed on every request to your protected routes.


References:

1. **Sigma-rust** https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm
2. **Sigma-rust discord** https://discord.com/channels/668903786361651200/729692906209673257
