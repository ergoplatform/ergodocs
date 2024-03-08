---
tags:
  - Tutorial
---
# Ergo Platform Blockchain Integration Guide

This guide provides developers with the necessary information to integrate with the Ergo Blockchain Platform. For suggestions to improve this guide, please reach out to us at team@ergoplatform.org or join our [`#development` channel on Discord](https://discord.gg/kj7s7nb).

## Key Features

- Ergo's transactions consist of multiple *inputs* and *outputs*, similar to Bitcoin. Unspent outputs, known as **single-use entities**, are used once. Although built from the ground up, Ergo's scripts and transaction formats differ from Bitcoin's. For an in-depth understanding, refer to the [Ergo 'Box' model](../data-model/box.md).
- Ergo incorporates standard scripts, associated with `P2PK` addresses, much like Bitcoin. [Explore more about the address scheme here](/dev/wallet/address).
- An Ergo UTXO box utilizes [registers](registers.md) to store arbitrary values, such as native tokens, rather than a single amount (like BTC). Each box holds an ERG amount and may include {tokenid, token amount} pairs, adhering to the UTXO model.
- The precision of each transaction on the Ergo platform is up to 10^-9 ERG. This means that transactions can be made with a precision of up to 0.000000001 ERG.
- Ergo's built-in wallet API caters to most use cases. The API employs a Swagger interface and operates on `127.0.0.1:9053` by default in the mainnet (`9052` on the testnet).
- Comprehensive guides on [node setup](install.md) and a dedicated [troubleshooting page](troubleshooting.md) are readily available.

## Infrastructure

### Node

We recommend running your own node for optimal performance. However, a public node is available at [213.239.193.208:9053](http://213.239.193.208:9053). For redundancy, contact us at team@ergoplatform.org or join our group chat. A dynamic list of public nodes can be found at [api.tokenjay.app/peers/list](https://api.tokenjay.app/peers/list).

When running a public node, access the web interface at [127.0.0.1:9053/panel](https://127.0.0.1:9053/panel). Note that the port changes to `9052` on the testnet. To get started on the testnet, refer to [this page](/node/testnet).

The average interval time of each block on the Ergo blockchain is approximately 2 minutes.

The required disk size for running an Ergo node depends on various factors such as the size of the blockchain and the number of transactions. It is recommended to have a disk size of at least 100 GB to ensure smooth operation.

You can bootstrap a pruned node using a verified UTXO set snapshot and NiPoPoWs.

#### Exchange Specific Node Settings

For exchange [nodes](install.md), consider implementing the following non-default [wallet settings](conf-wallet.md):

- Set [`ergo.wallet.dustLimit = 1000000`](conf-wallet.md#dust-limit) to disregard incoming payments (e.g., airdrops) of 0.001 ERG or less. Adjust as needed. The default `null` accounts for all incoming payments.
- Set [`ergo.wallet.profile`](conf-wallet.md#profile) to `exchange` to enable larger Bloom filters for more efficient scanning with many addresses.
- Set [`ergo.wallet.tokensWhitelist`](conf-wallet.md#tokens-whitelist) to a non-null value to automatically burn airdrop tokens and similar.

Combine these settings in your configuration:

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
Ergo node offers a REST API accessible via HTTP. The complete API specification, in OpenAPI format, can be found [here](openapi.md). When the node is operational, access the user-friendly Swagger UI at [127.0.0.1:9053/swagger](https://127.0.0.1:9053/panel) or experiment with it [here](swagger_api.md). An optional [indexed node API](indexed-node.md) is also available. 
///

Major wallet functionalities include:

- Wallet creation (`/wallet/init`) and mnemonic generation
- Wallet restoration (`/wallet/restore`) from mnemonic
- Wallet unlock (`/wallet/unlock`) for transaction signing
- Wallet lock (`/wallet/lock`)
- Sending a simple payment (`/wallet/payment/send`)
- Checking wallet status (`/wallet/status`)
- Deriving a new key according to EIP-3 (BIP 44 implementation for Ergo) (`/wallet/deriveNextKey`)
- Checking wallet balance (`/wallet/balances`) for all addresses
- Retrieving wallet transactions (`/wallet/transactions`) for all addresses

### Explorer

The public explorer is available at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/). Community-hosted alternatives include [ergexplorer.com](https://ergexplorer.com/) and [sigmaspace.io](https://sigmaspace.io/).

To install the Explorer backend independently, use [*ergo-bootstrap*](https://github.com/ergoplatform/ergo-bootstrap). 

For additional details, mirrors, and resources, refer to the dedicated [Explorer](explorer.md) section. 

### GQL 

GraphQL queries provide flexible data fetching, minimizing over-fetching and under-fetching. The GraphQL server, built on the Ergo Platform's explorer database schema, is accessible at [gql.ergoplatform.com](https://gql.ergoplatform.com).

The most reliable instance is currently [explore.sigmaspace.io/api/graphql](https://explore.sigmaspace.io/api/graphql).

## Creating an External Wallet

Develop your wallet logic externally using one of the available libraries and the block explorer. 

**Consider mempool transactions to avoid double-spending.**

Available libraries:

- [*ergo-appkit*](https://github.com/ergoplatform/ergo-appkit): A complete Java SDK.
- [*ergo-wallet*](https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet): Developed in Java, source code available in the [Ergo node repository](https://github.com/ergoplatform/ergo/tree/master/ergo-wallet).
- [*sigma-rust*](https://github.com/ergoplatform/sigma-rust/): A Rust library with WASM bindings for JavaScript/TypeScript.
- [*ergo-golang*](https://github.com/azhiganov/ergo-golang): An early-stage Go library.

Ergo's transactions, akin to Bitcoin, consist of multiple inputs and outputs. Unspent outputs, known as single-use entities, are used once. Although Ergo is built from the ground up, its scripts and transaction formats are distinct from Bitcoin's. For an in-depth understanding, refer to the [Ergo 'Box' model](../data-model/box.md).

Ergo incorporates standard scripts, associated with P2PK addresses, much like Bitcoin. An Ergo UTXO box utilizes [registers](registers.md) to store arbitrary values, such as its native tokens, rather than a single amount (like BTC). Consequently, each box holds an ERG amount and may also include {tokenid, token amount} pairs, adhering to the UTXO model.

### Offline Signing

- Demo for transaction assembly and offline signing using ergo-wallet and Java: [AdressGenerationDemo.java](https://gist.github.com/kushti/c040f244865a451b94df01032c7a3456)
- Transaction assembly and signing in Rust: [tx_builder.rs](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/tx_builder.rs#L552-L592) and [signing.rs](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/ergo-lib/src/wallet/signing.rs#L133-L161)
- [Transaction assembly and signing in JavaScript](https://github.com/ergoplatform/sigma-rust/blob/d70bea875792c4e383bfdd71754338695bdb37f8/bindings/ergo-lib-wasm/tests/test_transaction.js#L9-L69)

### Address Generation

Demo for secret seed and derived addresses generation using ergo-wallet and Java: [AdressGenerationDemo.java](https://gist.github.com/kushti/70dcfa841dfb504721f09c911b0fc53d)

Use the `/wallet/deriveNextKey` API to generate new addresses in the same wallet:

```bash
curl -X GET "http://localhost:9053/wallet/deriveNextKey" -H  "accept: application/json" -H  "api_key: hello"
```

### Address Validation

For exchanges, restrict withdrawals to P2PK addresses and invalidate other types. Supporting other types is not recommended. See [address.md] for more information on address types. 

[ergo-simple-addresses](https://github.com/kushti/ergo-simple-addresses) contains Java-friendly utils for working with addresses.

### Composing Transactions Outside the Node

Get unspent UTXOs for an address using the `transactions/boxes/byAddress/unspent` Explorer API method: 

```bash
https://api.ergoplatform.com/transactions/boxes/byAddress/unspent/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M 
```

Exclude UTXOs spent in the mempool using the `/transactions/unconfirmed/byAddress` Explorer API method:

```bash
https://api.ergoplatform.com/transactions/unconfirmed/byAddress/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M
```

### Broadcasting Transactions

To broadcast a transaction made outside the node, serialize it into `JSON`. In Java:

```Java
Json json = JsonCodecsWrapper.ergoLikeTransactionEncoder().apply(tx);
System.out.println(json.toString());
```

Send this `JSON` via a POST request to the public Explorer:

```bash
https://api.ergoplatform.com/api/v0/transactions/send*
```

Or to your private Explorer or a node with open API (`POST` to `http://{node_ip}:9053/transactions`)

## Troubleshooting

### Dust Collection

Collect dust from miners' deposits periodically to prevent small UTXOs from accumulating.

Ergo's extended-UTXO model can lead to *dust* - fractional ERG values usually below the protocol fee. Miner wallets are prone to becoming *dusty* due to the stream of rewards. Excess UTXOs can slow down and impact node functionality. **This is important for exchanges receiving mining traffic. Collect dust aggressively, as new dust arrives constantly for miners.**

Node-specific settings to address this:

- Get UTXOs from `/wallet/boxes/unspent` with min confirmations
- Get their `ids` and `total sum`
- Get *binary representations* of UTXOs via `/utxo/byIdBinary/{boxId}`

Construct the payment transaction:

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

Post to `/wallet/transaction/send`.

Set `value` and `fee` such that `value + fee = total sum of UTXOs`.

Query with specific parameters:

```bash
curl -X GET "http://127.0.0.1:9053/wallet/boxes/unspent?minConfirmations=10&minInclusionHeight=0" -H  "accept: application/json" -H  "api_key: hello"
```

Another simple way to collect dust is to set:

```conf
ergo {
 wallet {
   maxInputs = 300 
   optimalInputs = 100
 }
}
```

And send `1 ERG` to the change address. The node will attach 100 dust inputs (send any large change amounts to the change address as well).

#### Failed to sign boxes

This error can occur due to too many inputs collected in a transaction for dusty wallets:

```bash
Failed to sign boxes due to Estimated execution cost 1001580 exceeds the limit 1000000: Vector(ErgoBox(0275eb3a125bc02fe997cb98c0de8131bd9b2e4617110d
```

### Native Assets

For large airdrops, users may mistakenly put exchange addresses to receive native assets. An *auto-burn* method will be in future node versions to reduce manual effort. See this [Issue](https://github.com/ergoplatform/ergo/issues/1604) for more information.

Send this request via `/wallet/payment/send`, replacing `tokenId` with the IDs of the spamming tokens:

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

There is no central token registry. Use community resources like [supported tokens in the ergotipper bot](https://github.com/Luivatra/ergotipper-tokens) and [spectrum-finance/ergo-token-list](https://github.com/spectrum-finance/ergo-token-list).

### Frequently Asked Questions

**Can P2S and P2SH be two address formats for the same script?**

Yes. For P2S, the script is serialized directly into the address. For P2SH, the address contains only a hash of the serialized script.

**Are there issues with supporting address types other than P2PK?**

Supporting other types isn't a problem if the user is aware of what they're doing, but this is often not the case and can introduce complexity. P2S addresses can't validate input size in forms.

**How are ergoTree and address related for conversions?**

In appkit, `Address.create()` accepts an address string and returns an object from which you can obtain the ergoTree.

**Why do some transactions appear not to pay fees?**

Fees aren't mandatory in the core protocol, but transactions without them won't be propagated around the network by default.

**What algorithm generates a boxid?**

The boxid is generated by hashing the box contents.

[See the code in AppKit for details](https://github.com/ergoplatform/ergo-appkit/blob/9e19c13d82966eaee59433d16c4fb987bea363a7/lib-impl/src/main/java/org/ergoplatform/appkit/impl/OutBoxBuilderImpl.scala#L66)

A box's bytes are unique because they contain:
- The `id` of the parent transaction, 
- The output position in the transaction,
- A unique transaction id.

**Address Rules:**

- address = prefix byte || content bytes || checksum
- Prefix byte = network type + address type
- checksum = leftmost_4_bytes (blake2b256 (prefix byte || content bytes))
- For more information, refer to the [Address Types documentation](https://docs.ergoplatform.com/dev/wallet/address/address_types/).

**Preventive Measures to Avoid Chain Forking:**

- Ergo's view is that disruptive hard forks should be avoided in Ergo unless absolutely critical. Ergo implements various measures to prevent hard forks, such as pushing complexity to the application layer and enabling many things to be implemented via soft-forks.
- If a supermajority (90%+) of the network accepts a new feature, it is activated; however, old nodes that do not upgrade continue to operate normally and skip over this feature validation.
- Velvet-Fork: Only requires a minority of nodes to upgrade. Introduced by the NiPoPoW paper, the key idea is that you can use the scheme even if only some blocks in the chain include the interlink structure and allows for "gradual deployment" without harming the miners that haven't upgraded to the new rules. In this way, it acts similar to a soft fork in that clients that upgrade to new rules are still compatible with those that don't.
- Soft-fork's require some nodes to upgrade. The recent re-emission Soft-Fork EIP37 was possible as it's enforced on miner nodes only via protocol rules. These can be approved with 90% support from miners.
- Hard-Fork Requires all nodes to upgrade.
- For more information, refer to the [Ergo Improvement Proposals (EIPs)](https://github.com/ergoplatform/eips).

**51% Attack Prevention:**

- Ergo utilizes the Autolykos algorithm, a fairly launched efficient ASIC-resistant Proof of Work algorithm to mitigate the risk of a 51% attack. Mining pools offer a buffer against network attacks as the hash rate is distributed across thousands of individual miners. The memory-hardened aspect of Ergo also makes this attack vector more expensive as there is no ASIC support to rent.

**Storage Rent:**

- Ergo's design emphasizes long-term economic sustainability. One of the key strategies to ensure this is the implementation of storage rent or 'demurrage'. Storage rent is a nominal fee levied on unspent outputs after four years. The fee per byte is determined by the storage rent subprotocol. For a box without tokens and complex scripts, this amounts to approximately 0.14 ERG every four years.
- For more information, refer to the [Storage Rent documentation](https://docs.ergoplatform.com/mining/rent/).

**Does the node wallet need to expose its port? If so, is a machine with NAT IP okay?**

Wallet nodes do not necessarily need to expose their ports, although you can do if you want it to be available outside your local network. NAT IP is fine.

**Whitelisting Node IP:**

Ergo does not require adding your node's IP to a whitelist for synchronization.

This comprehensive guide should provide exchanges and developers with the necessary information to integrate with the Ergo platform smoothly. It covers key features, infrastructure setup, wallet creation, troubleshooting, and addresses common concerns such as chain forking prevention, 51% attack mitigation, and storage rent. If you have any further questions or need assistance, please don't hesitate to reach out to the Ergo team or join the community discussions on Discord.