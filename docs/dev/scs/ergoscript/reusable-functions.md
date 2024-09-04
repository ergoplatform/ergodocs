## Debugging Techniques

- Check the versions of dependencies like `ergo-lib-wasm-nodejs` and `ergo-lib-wasm-browser` to ensure you have the latest fixes
- If an issue is suspected to be with the Nautilus wallet, try manually replacing the `.wasm` file in the extension directory with an updated version of `sigma-rust` wasm
- Building Nautilus from source with updated dependencies can help identify issues
- When encountering issues with on-chain boxes, you can try:
  1. Make contract edits (e.g., set a condition to always true)
  2. Compile the modified contract and get the new ErgoTree hex
  3. Replace the ErgoTree of the problematic box with the new hex
  4. Try signing the transaction (it should work even if the modified tree wouldn't validate on-chain)
- For mocking boxes in unit tests, use the `mockUTxO` function from `@fleet-sdk/mock-chain` instead of manually editing box contents

## FAQs

### Is the EIP3 Secret similar to an account index for derived public keys?

Yes, the EIP3 secret is similar to an account index for derived public keys, as confirmed by user 'Aberg (Satergo dev)'. In Satergo wallet it is called the "address index" and custom indices can be used.

### How do I convert a Coll[Byte] of proposition bytes to SigmaProp type? 

Look for the `decodePoint` method, this is probably what you need to convert bytes to a SigmaProp.

### Can I insert two tokens with the same ID but different amounts in a box? 

You can, but some offchain code may get confused. The amounts would get merged into one entry in the box's tokens array.

### How do I fix "Tree root should be real but was UnprovenSchnorr(ProveDlog(Ecp(..." error?

This usually means the transaction was signed by an incorrect public key.

### As a complete coding beginner, should I learn Java then Scala before ErgoScript?

It's recommended to focus on learning UTXO model concepts first. The courses at https://docs.ergoplatform.com/dev/get-started/ are a good starting point without needing Java or Scala.

### How are dApp fees handled in ErgoScript contracts?

In ErgoScript, fees are handled explicitly as part of the transaction building process. See the Token Sale Service contract example: 
https://github.com/ergoplatform/ergoscript-by-example/blob/main/tokenSalesService.md

Key aspects:  

- Tx fee (`MinTxFee`) must be set 
- Box outputs handle the distribution of payment and token amounts
- Fee is paid from input boxes controlled by the dApp/contract

### How can options/Some(...) be used in ErgoScript outside of registers and context variables?

The use of options is de-facto limited to registers and context vars as the source of `Some(...)` values. A workaround is to use a "fake" register and then `box.R4[Boolean].map(r => <some expression which doesn't depend on r>)`.

### What's the proper syntax for fold/map/reduce operations in ErgoScript?

Some examples:
```scala
// Simple sum with fold
def sum(a: Long, b: Box) = a + b.value
val total = INPUTS.fold(0L, sum)

// Declare function separately, use name in fold 
def sum[Long](a:Long, b:Box) = a + b.value
val total = INPUTS.fold(0L, sum)  // Type parameter [Long] not needed

// Upcoming Sigma 6.0 may allow methods like
val total = INPUTS.sumBy(b => b.value)
```

### How to store a script hash in a register using Fleet?

To store script bytes in a register for comparison to a box's `propositionBytes`:
```js
// Create output with register
new OutputBuilder(SAFE_MIN_BOX_VALUE, SELL_ORDER_ADDRESS)  
  // ... 
  .setAdditionalRegisters({
    R8: SColl(SByte, ErgoAddress.fromBase58(DEPOSIT_ADDRESS).ergoTree).toHex()
  })
```

And in the contract:
```scala
{
  // Validate the box is going to the expected script
  someBox.R8[Coll[Byte]].get == someBox.propositionBytes
}
```

## Noted Issues

- There was a bug in `sigma-rust` related to `coll.slice` not gracefully handling empty collections, in contrast to the Scala version used in nodes. This caused issues for around 3 weeks until it was fixed by user 'greenhat'. The fix was merged into the develop branch of `sigma-rust`.
- The fix needs to propagate through the dependency tree, including an update to the Nautilus wallet, before it fully resolves the issues for end users.
- Some unexpected exceptions can arise with ErgoScript when using `.toBigInt` on `Long` register values. Investigation pending.
- Using ErgoNames, if a token containing a registered name is burned, that name would be lost forever. Potential solutions being researched.

## Tutorial Code Snippets

Summing nanoErgs of all inputs:
```scala 
def sum(a: Long, b: Box) = a + b.value
val total = INPUTS.fold(0L, sum)
```

Storing a script hash in a register with Fleet:
```js
new OutputBuilder(SAFE_MIN_BOX_VALUE, SELL_ORDER_ADDRESS)
  .setAdditionalRegisters({ 
    R8: SColl(SByte, ErgoAddress.fromBase58(DEPOSIT_ADDRESS).ergoTree).toHex() 
  });
```

## Additional Resources 
- ErgoScript Language Specification: https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md
- Ergo Playground/eScript IDE: https://escript.online/