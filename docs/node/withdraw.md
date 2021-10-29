## Spending mining reward

This text is to help miners to withdraw funds mined.
 
A lot of folks launched a node and also a miner, with `pubkeyHex` from the miner embedded in the node config. Now
information on how to recognize the coins mined and withdraw them to another address. 
 
## On keys.

A miner can see a lot of keys in different formats. 

First, mining software and also mining support in the node (namely, `ergo.node.miningPubKeyHex` setting in the config) are using a `Base16-encoded` "raw" public key, which is just an encoded serialized point on elliptic curve. This key is enough for a miner (which can avoid then supporting Base58, address forming etc).

Second, a node wallet shows Pay-To-Public-Key (P2PK) addresses, which are starting with "9". P2PK adress contains not just elliptic curve point, but also network prefix and `checksum`, similarly to Bitcoin P2PK and P2PKH addresses. 

Third, there is `minig/rewardAddress` API method, which is intended for external tools generating block candidates. This API method shows something like `88dhgzEuTXaSfKEbxfa6vghvEGdBH39sn9h7As2Y2Z6SGd8bKXCXmRLY5JtU4g4RYBP4WcZWb3JwjXDK`, which is a special script to pay a miner in encoded form.

Anyway, if you put pubkeyHex from you miner into your node, everything is okay, just don't worry about different keys seen.

## Getting you balance shown & withdrawals

Probably you don't see mined coins after wallet initialization, if its done on height after blocks mined. Please note,
the node is not scanning blocks backwards, it is only scanning new blocks after the initialization. Thus in order to find mined coins, full blockchain rescan is needed atm (or, if you mine, launch another node on another machine, or on the same machine with different ports set in the config, namely, set new values to `scorex.restApi.bindAddress` and `scorex.network.bindAddress` fields; also please use version 3.0.1 as it is easier to configurate). 

## In order to spend rewards you need to follow the steps below:

### 1. Clear node state, if you're going to stop working node.

In order to clear the state of your node you need to stop the node and then remove all contents of `.ergo` directory (it could be hidden from you on Mac and Linux, try `ls -a` command in the directory you ran the node from).

### 2. Restoring a local wallet from the seed-phrase used in the Autolykos miner

Remember that mnemonic sentence you set in the `config.json` when configuring your Autolykos miner - now you need to restore build-in wallet from it. In order to restore your wallet start the node again and send a POST request to `http://[your_node_ip]:9053/wallet/restore` containing the `application/json` content-type body like:

```scala
{
  "pass": "your_wallet_pass",
  "mnemonic": "mnemonic_sentense_from_your_miner",
  "mnemonicPass": "mnemonic_pass_if_set"
}
```

, where `pass` is a new unique pass to be used to encrypt wallet data on your local disk, and `mnemonic` is a mnemonic phrase you copied from your Autolykos miner config (`config.json`). Please especially pay your attention to `mnemonicPass` field - this is a password of your mnemonic phrase, it's optional and you could have configured it when generating your mnemonic. So add this field to the request only in case your mnemonic is really protected with a pass, remove this field otherwise.

Don't forget to authorize your request setting correct `api_key` HTTP header corresponding to the `apiKeyHash` your configured in the node config file.

ATTENTION: In order to let the wallet scan all the blocks from the genesis you need to restore the wallet before your node would have started downloading full blocks (Check `fullHeight` in `/info` API method response - while it is `null` your node haven't start downloading full blocks)

### 3. Check your balance

When your node got synced with the network check `/wallet/balances` API method. The response should look like:

```scala
{
  "height": 3560,
  "balance": 67500000000,
  "assets": {}
}
```

Pay attention to the `height` field first - it should equal `fullHeight` displaying by `/info` API route. `balance` is a confirmed balance found by your wallet.

### 4. Make a transaction spending your reward

In order to withdraw a reward from your wallet, create a new payment transaction using `/wallet/payment/send` API route. In order to perform this operation send a POST request containing an `application/json` content-type body like:

```scala
{
  "address": "your_address",
  "value": 10000000
}
```

, where `address` is the address you want to move your funds to and `value` is how many nanoERGs you wish to move.



When the request is sent the node would return transation id in response. You can use [explorer](https://explorer.ergoplatform.com) to check when your transaction gets to the block.
