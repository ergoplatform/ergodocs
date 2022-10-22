---
tags:
  - Tutorial
---


# Integration

A guide for helping developers from exchanges/pools/etc integrate Ergo. 

Any suggestions for improvements are welcomed! 

Please send them to team@ergoplatform.org or join us on [`#development` on Discord](https://discord.gg/kj7s7nb).


## Getting Started


Some quick facts about Ergo that are useful to know. 

* like Bitcoin, a transaction in Ergo has multiple *inputs* and *outputs*. Unspent outputs are **single-use entities**. However, Ergo is built from scratch; thus, scripts and transaction formats are different.
* Just like Bitcoin, there are some standard scripts in Ergo associated with addresses, e.g. `P2PK` addresses. [Read more here on the address scheme](/dev/wallet/address)
* Rather than storing a single amount (like BTC), an ergo eutxo box has some registers to store arbitrary values, like its native tokens. So, each box has an ERG amount and may or may not have a bunch of {tokenid, token amount} pairs, all in the UTXO model.
* Ergo has an inbuilt wallet API which is enough for most use-cases. API has a Swagger interface on `127.0.0.1:9053` by default in the mainnet (`9052` on testnet).
* See the full guide on setting [How to set up a node](/node/platforms/tutorial) and the associated [troubleshooting](/node/platforms/troubleshooting) page.



### Node Wallet


- **Web interface**: [127.0.0.1:9053/panel](https://127.0.0.1:9053/panel) (`9052` on the testnet). 

Main methods:

* `/wallet/init` to create a wallet (and a secret mnemonic)  
* `/wallet/restore` to restore a wallet from mnemonic
* `/wallet/unlock` to unlock the wallet (it is unlocked after init but locked after restart). You have to unlock it before signing transactions
* `/wallet/lock` to lock the wallet
* `/wallet/payment/send` to send a simple payment
* `/wallet/status` to get wallet status
* `/wallet/deriveNextKey` to derive a new key according to EIP-3 (BIP 44 implementation for Ergo)
* `/wallet/balances` to get wallet balance (for all the addresses) 
* `/wallet/transactions` to get wallet transactions (for all the addresses) 

### Creating an external wallet.

If you plan to perform your wallet logic externally, you can do so with a library and the block explorer. 

**Please note, you will need to consider mempool transactions to avoid double-spending generation**.

Available libraries are:

* [*ergo-appkit*](https://github.com/ergoplatform/ergo-appkit) Complete java sdk.
* [*ergo-wallet*](https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet) made in Java (sources are in [Ergo node repository](https://github.com/ergoplatform/ergo/tree/master/ergo-wallet))
* [*sigma-rust*](https://github.com/ergoplatform/sigma-rust/) in Rust with WASM bindings for JavaScript/TypeScript
* [*ergo-ts*](https://github.com/coinbarn/ergo-ts) in TypeScript
* [*ergo-golang*](https://github.com/azhiganov/ergo-golang) in Go (still raw)


### Offline Signing

- Transaction assembly and offline signing demo using ergo-wallet and Java is provided in [AdressGenerationDemo.java](https://gist.github.com/kushti/c040f244865a451b94df01032c7a3456 )
- Transaction assembly and signing in Rust: [tx_builder.rs](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/tx_builder.rs#L552-L592) and [signing.rs](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/signing.rs#L133-L161)
- [Transaction assembly and signing in JavaScript](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/bindings/ergo-lib-wasm/tests/test_transaction.js#L9-L69)


### Address generation

Secret seed and derived addresses generation demo using ergo-wallet and Java is provided in [AdressGenerationDemo.java](https://gist.github.com/kushti/70dcfa841dfb504721f09c911b0fc53d)


To generate new addresses in the same wallet you can use the `/wallet/deriveNextKey` API method

```bash
curl -X GET "http://localhost:9053/wallet/deriveNextKey" -H  "accept: application/json" -H  "api_key: hello"
```




### Composing transactions outside the node


To get unspent UTXOs for some address, please use `transactions/boxes/byAddress/unspent` Explorer API method: 

```
https://api.ergoplatform.com/transactions/boxes/byAddress/unspent/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M 
```

You need to exclude UTXOs spent in the mempool. Use `/transactions/unconfirmed/byAddress` Explorer API method for that:

```
https://api.ergoplatform.com/transactions/unconfirmed/byAddress/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M
```

### Broadcasting transaction


To broadcast a transaction made outside the node, the easiest way is to serialize it into `JSON`; in Java, it could be like:

```
Json json = JsonCodecsWrapper.ergoLikeTransactionEncoder().apply(tx);
System.out.println(json.toString());
```

and then send this `JSON` via a POST request to the public Explorer 

```
https://api.ergoplatform.com/api/v0/transactions/send*
```

your private Explorer or a node with open API (`POST` to `http://{node_ip}:9053/transactions` )



## Infrastructure

### Explorer

There is a public explorer hosted at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/)

You can use [*ergo-bootstrap*](https://github.com/ergoplatform/ergo-bootstrap) to easily install the Explorer backend (and not rely on public ones). 

### Testnet

See [this page](/dev/start/testnet) for information on the public testnets.



## Troubleshooting

### Dust Collection

Please consider collecting deposits dust from miners periodically (who create a lot of small UTXOs).



Ergo is based on the extended-UTXO model. A side-effect of UTXOs is a term coined *dust*. Dust refers to fractional values of ERG and is usually below the protocol fee, miner wallets are prone to becoming *dusty* with the stream of rewards coming into their wallet. All these excess UTXOs can cause a slowdown and ultimately, make impact your nodes functionability. **This is important to set-up for large exchanges who will recieve a lot of mining traffic. You need to collect dust aggressively, new dust arrives all the time for miners**



**To solve**

- Get utxos from `/wallet/boxes/unspent` with min number of confirmations
- Get their `ids` and `total sum`
- Get their *binary representations* of utxos via `/utxo/byIdBinary/{boxId}`


Finally, construct the payment transaction like:
  
```
{
  "requests": [
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 10000000000
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
    "utxo1", "utxo2"
  ],
  "dataInputsRaw": [
  ]
} 
```

and post to `/wallet/transaction/send`

Set value and fee accordingly, `value + fee = total sum of utxos`

You can query with specific parameters like this, 

```
curl -X GET "http://127.0.0.1:9053/wallet/boxes/unspent?minConfirmations=10&minInclusionHeight=0" -H  "accept: application/json" -H  "api_key: hello"
```

Another (and simple) way to collect is to set 

```
ergo {
 wallet {
   maxInputs = 300 
   optimalInputs = 100
 }
}
```

and send `1 ERG` to the change address, however, the node will attach 100 dust inputs (so send any large amounts of change to the change address as well)

#### Failed to sign boxes

This error can occur as a result of too many inputs being collected in a transaction for dusty wallets. 

```bash
Failed to sign boxes due to Estimated execution cost 1001580 exceeds the limit 1000000: Vector(ErgoBox(0275eb3a125bc02fe997cb98c0de8131bd9b2e4617110d
```



### Native Asssets

In the case of large airdrops, many users mistakenly end up putting exchange addresses to receive native assets. An *auto-burn* method will be in future versions of the node to reduce the manual component of this task. See this [Issue](https://github.com/ergoplatform/ergo/issues/1604) for more information.

Send the following request via `/wallet/payment/send`, replacing the `tokenId` with the IDs from the tokens spamming your wallets. 

```
[
  {
    "address": "4MQyMKvMbnCJG3aJ",
    "value": 100000000,
    "assets": [
      {"tokenId":"e55adbda4e42f2bd21b1cb9498c105ff3bc1069012942d6158412f55759369c3","amount":1},
      {"tokenId":"6dd3e0ac4edd9702094aa4e3cad7c0c73d5437292c11805adf5d5068312748b4","amount":1}
    ]
  }
]
```

#### Tokens with Value

- SigUSD ($1): `472c3d4ecaa08fb7392ff041ee2e6af75f4a558810a74b28600549d5392810e8` 
- SigRSV
- ergopad
- NETA
- LunaDog
- Erdoge

