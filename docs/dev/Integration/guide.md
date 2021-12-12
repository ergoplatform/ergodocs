This guide is for helping developers integrate Ergo into exchanges, wallets, pools wallets etc.

Introduction
------------

Some quick facts useful for an integration:

* like Bitcoin, a transaction in Ergo has multiple inputs and outputs. Unspent outputs are single-use entities. However, Ergo is built from scratch; thus, scripts and transaction formats are different.
* like in Bitcoin, there are some standard scripts in Ergo associated with addresses, e.g. P2PK addresses. There's an article on address schemes available [here](https://ergoplatform.org/en/blog/2019_07_24_ergo_address/)
* Ergo has an inbuilt wallet API which is enough for most use-cases. API has a Swagger interface (on 127.0.0.1:9053 by default in the mainnet, 127.0.0.1:9052 in the testnet) with descriptions and examples for API methods.
* How to set up a node: https://ergoplatform.org/en/blog/2019_12_02_how_to_setup/, https://github.com/ergoplatform/ergo/wiki/Set-up-a-full-node

Please run the node with -Xmx3G flag, e.g. ```java -jar -Xmx3G ergo-4.0.4.jar --mainnet -c mainnet.conf```

Node Wallet
-----------

Node wallet has UI available @ 127.0.0.1:9053/panel by default on the mainnet (127.0.0.1:9052/panel on the testnet). Main methods:

* */wallet/init* and */wallet/restore* to create a wallet (and a secret mnemonic) and restore wallet from mnemonic
* */wallet/unlock* to unlock the wallet (it is unlocked after init but locked after restart)
* */wallet/lock* to lock the wallet
* */wallet/payment/send* to send a simple payment
* */wallet/status* to get wallet status
* */wallet/deriveNextKey* to derive a new key according to EIP-3 (BIP 44 implementation for Ergo)
* */wallet/balances* to get wallet balance (for all the addresses) 
* */wallet/transactions* to get wallet transactions (for all the addresses) 

Create an external wallet.
========================

If you plan to perform your wallet logic externally, you can do so with a library and the block explorer. **Please note, you need to consider mempool transactions to avoid double-spending generation**.

Available libraries are:

* [*ergo-wallet*](https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet) made in Java (sources are in [Ergo node repository](https://github.com/ergoplatform/ergo/tree/master/ergo-wallet))
* [*sigma-rust*](https://github.com/ergoplatform/sigma-rust/) in Rust with WASM bindings for JavaScript/TypeScript
* [*ergo-ts*](https://github.com/coinbarn/ergo-ts) in TypeScript
* [*ergo-golang*](https://github.com/azhiganov/ergo-golang) in Go (still raw)


Offline Signing
---------------
Transaction assembly and offline signing demo using ergo-wallet and Java is provided in [this gist](https://gist.github.com/kushti/c040f244865a451b94df01032c7a3456 )

Transaction assembly and signing in Rust
https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/tx_builder.rs#L552-L592

https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/signing.rs#L133-L161

Transaction assembly and signing in JavaScript
https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/bindings/ergo-lib-wasm/tests/test_transaction.js#L9-L69

Composing transactions outside the node
--------------------------------------

To get unspent UTXOs for some address, please use transactions/boxes/byAddress/unspent Explorer API method: 
```
https://api.ergoplatform.com/transactions/boxes/byAddress/unspent/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M 
```
You need to exclude UTXOs spent in the mempool! Use /transactions/unconfirmed/byAddress Explorer API method for that: https://api.ergoplatform.com/transactions/unconfirmed/byAddress/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M

Broadcasting transaction
------------------------

To broadcast a transaction made outside the node, the easiest way is to serialize it into JSON; in Java, it could be like:

```
   Json json = JsonCodecsWrapper.ergoLikeTransactionEncoder().apply(tx);
   System.out.println(json.toString());
```

and then send this JSON via a POST request to the public Explorer *https://api.ergoplatform.com/api/v0/transactions/send*, your private Explorer or a node with open API (POST to http://{node_ip}:9053/transactions )

Address generation
------------------

Secret seed and derived addresses generation demo using ergo-wallet and Java is provided in [this gist](https://gist.github.com/kushti/70dcfa841dfb504721f09c911b0fc53d)


Own Testnet and Explorer Infrastructure
---------------------------------------

You can use [*ergo-bootstrap*](https://github.com/ergoplatform/ergo-bootstrap) to install Explorer backend easily (and so not rely on public ones). 

To start your own testnet, use the following node:
```
ergo {
  networkType = "testnet"

  node {
    mining = true
    offlineGeneration = true
    useExternalMiner = false
  }
}

scorex {

 network {
    bindAddress = "0.0.0.0:9020"
    nodeName = "ergo-testnet-4.0.4"
    knownPeers = []
  }

 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    # Below is hash corresponding to API_KEY = "hello" (with no quotes)
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}
```

Then the node will CPU-mine its own chain. 

Any suggestions for improvements are welcomed! Please send them to team@ergoplatform.org or #development channel in [Discord](https://discord.gg/kj7s7nb)