---
tags:
  - Tutorial
---

# Ergo Platform Blockchain Integration Guide

This guide aims to provide developers with the necessary information to integrate with the Ergo Blockchain Platform. For any suggestions to improve this guide, feel free to reach out to us at team@ergoplatform.org or join our [`#development` channel on Discord](https://discord.gg/kj7s7nb).

## Getting Started

Let's start with a quick rundown of Ergo's key features:

* Ergo's transactions, akin to Bitcoin, consist of multiple *inputs* and *outputs*. Unspent outputs, known as **single-use entities**, are used once. Although Ergo is built from the ground up, its scripts and transaction formats are distinct from Bitcoin's. For an in-depth understanding, refer to the [Ergo 'Box' model](../data-model/box.md).
* Ergo incorporates standard scripts, associated with `P2PK` addresses, much like Bitcoin. [Explore more about the address scheme here.](/dev/wallet/address)
* An Ergo UTXO box utilizes [registers](registers.md) to store arbitrary values, such as its native tokens, rather than a single amount (like BTC). Consequently, each box holds an ERG amount and may also include {tokenid, token amount} pairs, adhering to the UTXO model.
* Ergo's inbuilt wallet API caters to most use cases. The API employs a Swagger interface and operates on `127.0.0.1:9053` by default in the mainnet (`9052` on the testnet).
* Comprehensive guides on [node setup](install.md) and a dedicated [troubleshooting page](troubleshooting.md) are readily available for your convenience.
## Infrastructure

### Node

We recommend running your own node for optimal performance. However, if you prefer to use a public node, one is available at [213.239.193.208:9053](http://213.239.193.208:9053). If you require redundancy, don't hesitate to contact us at team@ergoplatform.org or join our group chat. You can also find a dynamic list of public nodes at [api.tokenjay.app/peers/list](https://api.tokenjay.app/peers/list).

If you choose to run a public node, the web interface can be accessed at [127.0.0.1:9053/panel](https://127.0.0.1:9053/panel). Please note that the port changes to `9052` when operating on the testnet. 

To get started on the testnet, please refer to [this page](/node/testnet).

#### Exchange Specific Node Settings

If you are operating an exchange [node](install.md), consider implementing the following non-default [wallet settings](conf-wallet.md):

* Set [`ergo.wallet.dustLimit = 1000000`](conf-wallet.md#dust-limit). This setting causes the node wallet to disregard incoming payments (such as airdrops) of 0.001 ERG or less. This value can be adjusted as per your needs. The default value is `null`, which means the wallet accounts for all incoming payments.
* Set [`ergo.wallet.profile`](conf-wallet.md#profile) to `exchange`. This setting enables the wallet to use larger Bloom filters, leading to more efficient scanning when the wallet has a large number of addresses.
* Set [`ergo.wallet.tokensWhitelist`](conf-wallet.md#tokens-whitelist) to a non-null value to automatically burn airdrop tokens and similar. An example of this can be seen in the code block below.

These settings can be combined to create a configuration section as shown below:

```
  ergo {
    ...
    wallet {
      ...  

      # boxes with value smaller than dustLimit are disregarded in wallet scan logic
      dustLimit = 1000000
      
      # Whitelisted tokens, if non-null, the wallet will automatically burn non-whitelisted tokens from
      # inputs when doing transactions.
      # If tokensWhitelist = [], all the tokens will be burnt,
      # tokensWhitelist = ["example"] means that all the tokens except of "example" will be burnt
      # tokensWhitelist = null means no tokens burnt automatically
      tokensWhitelist = [
        # SigUSD
        "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
        # SigRSV
        "003bd19d0187117f130b62e1bcab0939929ff5c7709f843c5c4dd158949285d0"
      ]
      

      # Wallet profile allows to say wallet what kind of load it should expect,
      # and so spend memory on caches and Bloom filters accordingly.
      # There are three options: user, exchange, appServer
      # User profile is about ordinary planned usage.
      # Exchange consumes ~20 MB of RAM for high-load ready Bloom filters
      # AppServer is in between
      profile = "exchange"
    }
  }    
```    




#### Node Wallet

/// admonition | Swagger
    type: tip
Ergo node also offers a REST API that can be accessed via HTTP. The complete API specification, presented in OpenAPI format, can be found [here](openapi.md). When the node is operational, a user-friendly Swagger UI is accessible at [127.0.0.1:9053/swagger](https://127.0.0.1:9053/panel). You can also experiment with it [here](swagger_api.md). Furthermore, an optional [indexed node API](indexed-node.md) is available. 
///

The major wallet functionalities include:

* Wallet creation (`/wallet/init`) and mnemonic generation
* Wallet restoration (`/wallet/restore`) from mnemonic
* Wallet unlock (`/wallet/unlock`) for transaction signing
* Wallet lock (`/wallet/lock`)
* Sending a simple payment (`/wallet/payment/send`)
* Checking wallet status (`/wallet/status`)
* Deriving a new key according to EIP-3 (BIP 44 implementation for Ergo) (`/wallet/deriveNextKey`)
* Checking wallet balance (`/wallet/balances`) for all addresses
* Retrieving wallet transactions (`/wallet/transactions`) for all addresses



### Explorer

The public explorer is available at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/). Community-hosted alternatives can be found at [ergexplorer.com](https://ergexplorer.com/) and [sigmaspace.io](https://sigmaspace.io/).

To install the Explorer backend independently, you can utilize [*ergo-bootstrap*](https://github.com/ergoplatform/ergo-bootstrap). 

For additional details, mirrors, and resources, refer to the dedicated [Explorer](explorer.md) section. 

### GQL 

GraphQL queries provide a flexible approach to data fetching, minimizing both over-fetching and under-fetching. The GraphQL server, built on top of the Ergo Platform's explorer database schema, is accessible at [gql.ergoplatform.com](https://gql.ergoplatform.com).

The most reliable instance currently is [explore.sigmaspace.io/api/graphql](https://explore.sigmaspace.io/api/graphql).

## Creating an External Wallet

You can develop your wallet logic externally using one of the available libraries and the block explorer. 

**Please ensure to take into consideration mempool transactions to avoid double-spending.**

Available libraries include:

* [*ergo-appkit*](https://github.com/ergoplatform/ergo-appkit): A complete Java SDK.
* [*ergo-wallet*](https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet): Developed in Java, the source code is available at the [Ergo node repository](https://github.com/ergoplatform/ergo/tree/master/ergo-wallet).
* [*sigma-rust*](https://github.com/ergoplatform/sigma-rust/): A Rust library with WASM bindings for JavaScript/TypeScript.
* [*ergo-golang*](https://github.com/azhiganov/ergo-golang): This is a Go library, still in early development stages.


### Offline Signing

- A demo for transaction assembly and offline signing using ergo-wallet and Java is provided in [AdressGenerationDemo.java](https://gist.github.com/kushti/c040f244865a451b94df01032c7a3456 )
- Transaction assembly and signing in Rust: [tx_builder.rs](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/tx_builder.rs#L552-L592) and [signing.rs](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/signing.rs#L133-L161)
- [Transaction assembly and signing in JavaScript](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/bindings/ergo-lib-wasm/tests/test_transaction.js#L9-L69)


### Address generation

A demo for secret seed and derived addresses generation using ergo-wallet and Java is provided in [AdressGenerationDemo.java](https://gist.github.com/kushti/70dcfa841dfb504721f09c911b0fc53d)


You can use the `/wallet/deriveNextKey` API to generate new addresses in the same wallet.

```bash
curl -X GET "http://localhost:9053/wallet/deriveNextKey" -H  "accept: application/json" -H  "api_key: hello"
```

### Address validation

For an exchange, you can restrict people to only withdraw to P2PK addresses and invalidate any other address. Supporting other types is not recommended. See [address.md] for more information on the types of addresses. 

[ergo-simple-addresses](https://github.com/kushti/ergo-simple-addresses) contains a few zero-dependencies Java-friendly utils for working with addresses.

### Composing transactions outside the node


To get unspent UTXOs for some address, please use the `transactions/boxes/byAddress/unspent` Explorer API method: 

```bash
https://api.ergoplatform.com/transactions/boxes/byAddress/unspent/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M 
```

It would be best if you excluded UTXOs spent in the mempool. Use the`/transactions/unconfirmed/byAddress` Explorer API method for that:

```bash
https://api.ergoplatform.com/transactions/unconfirmed/byAddress/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M
```

### Broadcasting transactions


To broadcast a transaction made outside the node, the easiest way is to serialize it into `JSON`; in Java, it could be like this:

```Java
Json json = JsonCodecsWrapper.ergoLikeTransactionEncoder().apply(tx);
System.out.println(json.toString());
```

And then send this `JSON` via a POST request to the public Explorer. 

```bash
https://api.ergoplatform.com/api/v0/transactions/send*
```

your private Explorer or a node with open API (`POST` to `http://{node_ip}:9053/transactions` )



## Troubleshooting

### Dust Collection

Please collect dust from miners' deposits periodically (which creates many small UTXOs).

Ergo is based on the extended-UTXO model. A side-effect of UTXOs is a term coined *dust*. Dust refers to fractional values of ERG and is usually below the protocol fee; miner wallets are prone to becoming *dusty* with the stream of rewards coming into their wallet. All these excess UTXOs can cause a slowdown and ultimately impact your node functionality. **This is important to set up for big exchanges that will receive a lot of mining traffic. You must collect dust aggressively; new dust arrives all the time for miners**

There are some node specific settings


**To solve**

- Get utxos from `/wallet/boxes/unspent` with min number of confirmations
- Get their `ids` and `total sum`
- Get their *binary representations* of utxos via `/utxo/byIdBinary/{boxId}`


Finally, construct the payment transaction like this:
  
```JSON
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

And post to `/wallet/transaction/send`.

Set value and fee accordingly, `value + fee = total sum of utxos`

You can query with specific parameters like this, 

```bash
curl -X GET "http://127.0.0.1:9053/wallet/boxes/unspent?minConfirmations=10&minInclusionHeight=0" -H  "accept: application/json" -H  "api_key: hello"
```

Another (and simple) way to collect is to set 

```conf
ergo {
 wallet {
   maxInputs = 300 
   optimalInputs = 100
 }
}
```

And send `1 ERG` to the change address; however, the node will attach 100 dust inputs (so send any large amounts of change to the change address as well)

#### Failed to sign boxes

This error can occur due to too many inputs collected in a transaction for dusty wallets. 

```bash
Failed to sign boxes due to Estimated execution cost 1001580 exceeds the limit 1000000: Vector(ErgoBox(0275eb3a125bc02fe997cb98c0de8131bd9b2e4617110d
```



### Native Assets

In the case of large airdrops, many users mistakenly end up putting exchange addresses to receive native assets. An *auto-burn* method will be in future versions of the node to reduce the manual component of this task. See this [Issue](https://github.com/ergoplatform/ergo/issues/1604) for more information.

Send the following request via `/wallet/payment/send`, replacing the `tokenId` with the IDs from the tokens spamming your wallets. 

```JSON
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

There is no central database where tokens are registered currently, your best bet is to use community resources like [supported tokens in the ergotipper bot](https://github.com/Luivatra/ergotipper-tokens) and [spectrum-finance/ergo-token-list](https://github.com/spectrum-finance/ergo-token-list).

### Frequently Asked Questions

**Can P2S and P2SH be two address formats for the same script?**

Yes, it is possible to create both a P2S and a P2SH address from the same script. In the case of P2S, the script is serialized directly into the address. Conversely, for P2SH, the address contains only a hash of the serialized script.

**Are there any issues with supporting address types other than P2PK?**

Supporting other address types doesn't pose a problem as long as the user is aware of what they are doing. However, it's worth noting that this is often not the case and it can introduce additional complexity. This is particularly true for P2S addresses, as you cannot validate the input size in your form.

**How are ergoTree and address related in terms of conversions?**

When using the appkit, the `Address.create()` function accepts an address string as an argument. You can then obtain the ergoTree from the object that this function returns.

**Why do some transactions appear not to pay fees?**

While fees are not a mandatory part of the core protocol, transactions without them will not be propagated around the network by default.

**What algorithm is used to generate a boxid?**

The boxid is generated by hashing the contents of the box.

[Refer to the code in AppKit for more details](https://github.com/ergoplatform/ergo-appkit/blob/9e19c13d82966eaee59433d16c4fb987bea363a7/lib-impl/src/main/java/org/ergoplatform/appkit/impl/OutBoxBuilderImpl.scala#L66)

The bytes of a box are unique because they contain:
- The `id` of the parent transaction, 
- The output position in the transaction,
- A unique transaction id. 
