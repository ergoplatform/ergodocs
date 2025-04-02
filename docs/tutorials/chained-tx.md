---
tags:
  - Chained Transactions
  - Transactions
  - ergpy
  - Python
  - Tutorial
  - Guide
---

# Sending Chained Transactions

Chained transactions allow you to spend outputs of off-chain transactions in a sequence.

The following example, adapted from [ergpy examples](https://github.com/mgpai22/ergpy/tree/main/examples), demonstrates how to send chained transactions. It also includes information from GetBlok about a [Transaction Group framework](https://github.com/GetBlok-io/Subpooling#frameworks--abstractions) for sending large interrelated transactions.

## Establish a Connection to the Blockchain

To begin, you need to establish a connection to the Ergo blockchain. Choose either the MainNet or TestNet node URL and set it as the `node_url`.

```python
# Assign a node_url, either MainNet or TestNet
node_url: str = "http://213.239.193.208:9052/"

ergo = appkit.ErgoAppKit(node_url=node_url)
```

## Wallet Mnemonic

Next, define your wallet mnemonic, which is a sequence of words that acts as your wallet's secret key. Replace the example `wallet_mnemonic` with your own mnemonic.

```python
wallet_mnemonic = "decline reward asthma enter three clean borrow repeat identify wisdom horn pull entire adapt neglect."

receiver_addresses = [
    "3WwdXmYP39DLmDWJ6grH9ArXbWuCt2uGAh46VTfeGPrHKJJY6cSJ",
    "3WwuG9amNVDwkJdgT5Ce7aJCfeoafVmd9tag9AEiAZwgPi7pYX3w",
    "3Wxk5oofZ3Laq2CpFW4Fi9YQiaep9bZr6QFg4s4xpzz4bi9tZq2U"
]

amount = [0.22, 0.33, 0.11]

consecutive_transactions = 3

# the amount of time in seconds the program will pause in between submitting transactions
sleep_time = 0.5

# here, we calculate the number of ergs required for the genesis outbox
genesis_amount = [consecutive_transactions * (0.22 + 0.33 + 0.11) + (consecutive_transactions + 1) * 0.001]

# wallet of the sender
genesis_receiver = [""]
```

## Create an Output Box

Create an output box for the transaction by following the code snippet below. This code returns an outbox from the signed transaction.

```python
genesis_tx = helper_functions.simple_send(ergo=ergo, amount=genesis_amount, wallet_mnemonic=wallet_mnemonic,
                                          receiver_addresses=genesis_receiver, return_signed=True)
genesis_outbox = appkit.get_outputs_to_spend(genesis_tx, 0)
```

## Submit the Transactions

Submit the transactions to the Ergo blockchain using the following code. This code submits the transaction to the node and prints the transaction ID (`txid`) to the console.

```python
print(ergo.txId(genesis_tx))
outBox_list = []

for x in range(consecutive_transactions):
    if x == 0:  # The first transaction gets the input box from the genesis outbox
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=genesis_outbox,
                                            return_signed=True, chained=True)
    elif x == consecutive_transactions - 1:  # The last transaction is not chained
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=

amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=outBox_list[x - 1],
                                            return_signed=True)
    else:  # Transactions in between get the input box from the prior chained transaction
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=outBox_list[x - 1],
                                            return_signed=True, chained=True)
    tx_1_outbox = appkit.get_outputs_to_spend(tx_1, 0)
    outBox_list.append(tx_1_outbox)
    time.sleep(sleep_time)

# Submit the final transaction to the node
print(ergo.txId(tx_1))

time.sleep(sleep_time)
helper_functions.exit()
```

Feel free to adjust the code to suit your specific needs.
