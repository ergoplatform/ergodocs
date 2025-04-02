---
tags:
  - Withdraw
  - Mining Rewards
  - Wallet
  - Node API
  - Transactions
  - P2PK
  - Seed Phrase
---

# Spending Mining Rewards

/// admonition | Keep in mind
    type: warning

Please note this page contains information that pre-dates [EIP-27](eip27.md).
///

This section guides miners on how to withdraw funds they have mined.

Many users have launched both a node and a miner, with the miner's `pubkeyHex` embedded in the node's configuration. This information explains how to identify the coins that have been mined and transfer them to another address.

### Keys Overview

Miners may encounter various keys in different formats. Here are the key formats commonly encountered:

1. **Base16-encoded raw public key**: Mining software and mining support in the node use this format, represented as a serialized point on an elliptic curve. Miners can use this key without the need for Base58 encoding or address formation.

2. **Pay-To-Public-Key (P2PK) addresses**: These addresses are displayed in the node wallet and start with "9." In addition to the elliptic curve point, P2PK addresses also include the network prefix and a checksum, similar to Bitcoin's P2PK and P2PKH addresses.

3. **Mining/rewardAddress API method**: This method is intended for external tools that generate block candidates. It displays a special encoded script, such as `88dhgzEuTXaSfKEbxfa6vghvEGdBH39sn9h7As2Y2Z6SGd8bKXCXmRLY5JtU4g4RYBP4WcZWb3JwjXDK`, used to pay a miner.

As long as you have entered the `pubkeyHex` from your miner into your node, you don't need to worry about the different keys you encounter.

### Viewing Your Balance and Withdrawing Funds

After initializing your wallet, you may not see the mined coins if the initialization occurred after the corresponding blocks were mined. It's important to note that the node does not scan blocks retrospectively; it only scans new blocks after initialization. To find mined coins in this situation, you need to perform a full blockchain rescan (or launch another node on a different machine or with different ports configured in the `scorex.restApi.bindAddress` and `scorex.network.bindAddress` fields of the config). We recommend using version 3.0.1 for easier configuration.

To spend your mining rewards, follow the steps below:

### Step 1: Clear Node State (if stopping the node)

If you intend to stop your node, you must clear its state. To do this, stop the node and remove all contents of the `.ergo` directory. On Mac and Linux, you may need to use the `ls -a` command in the directory where you ran the node to view the hidden directory.

### Step 2: Restoring a Local Wallet from the Autolykos Miner's Seed Phrase

Retrieve the mnemonic sentence you set in the `config.json` when configuring your Autolykos miner. You need to restore the built-in wallet using this phrase. To restore your wallet, start the node again and send a POST request to `http://[your_node_ip]:9053/wallet/restore` with the following `application/json` content-type body:

```json
{
  "pass": "your_wallet_pass",
  "mnemonic": "mnemonic_sentence_from_your_miner",
  "mnemonicPass": "mnemonic_pass_if_set"
}
```

In the request, provide a new, unique `pass` to encrypt the wallet data on your local disk. The `mnemonic` field should contain the mnemonic phrase copied from your Autolykos miner's config (`config.json`). Pay attention to the optional `mnemonicPass` field, which represents the password for your mnemonic phrase. Include this field in the request only if your mnemonic phrase is protected by a password; otherwise,

 remove it.

Ensure that you authorize your request by setting the correct `api_key` HTTP header, corresponding to the `apiKeyHash` you configured in the node's config file.

**ATTENTION**: To allow the wallet to scan all blocks from the genesis, restore the wallet before your node starts downloading full blocks. You can check the `fullHeight` value in the response of the `/info` API method. If `fullHeight` is `null`, it means your node hasn't started downloading full blocks yet.

### Step 3: Checking Your Balance

Once your node is synchronized with the network, check the `/wallet/balances` API method. The response should resemble the following:

```json
{
  "height": 3560,
  "balance": 67500000000,
  "assets": {}
}
```

First, pay attention to the `height` field, which should be equal to the `fullHeight` displayed by the `/info` API route. The `balance` field represents the confirmed balance discovered by your wallet.

### Step 4: Making a Transaction to Spend Your Reward

To withdraw a reward from your wallet, create a new payment transaction using the `/wallet/payment/send` API route. Send a POST request with the following `application/json` content-type body:

```json
{
  "address": "your_address",
  "value": 10000000
}
```

In the request, specify the `address` where you want to move your funds and the `value` representing the amount of nanoERGs you wish to transfer.

After sending the request, the node will return the transaction ID in the response. You can use the [explorer](https://explorer.ergoplatform.com) to track the progress of your transaction until it gets added to a block.
