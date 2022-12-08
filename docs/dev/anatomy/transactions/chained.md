# Send A Chained Transaction

Chained transactions (spending outputs of off-chain transactions)


- The *simple-send* example below was adapted from [ergpy examples](https://github.com/mgpai22/ergpy/tree/main/examples). 
- There are also some writings from GetBlok for a [Transaction Group framework](https://github.com/GetBlok-io/Subpooling#frameworks--abstractions) for sending large sets of transactions that are interrelated.


## Create a connection to the blockchain

```python
# Assign a node_url, either MainNet or TestNet
node_url: str = "http://213.239.193.208:9052/"

ergo = appkit.ErgoAppKit(node_url=node_url)
```

## Wallet mnemonic

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

# wallet of sender
genesis_receiver = [""]  
```

## Create an output box

```python

# This returns an outbox from the signed tx
genesis_tx = helper_functions.simple_send(ergo=ergo, amount=genesis_amount, wallet_mnemonic=wallet_mnemonic,
                                          receiver_addresses=genesis_receiver, return_signed=True)
genesis_outbox = appkit.get_outputs_to_spend(genesis_tx, 0)      
```

## Submit 

```python

# Submits the transaction to the node and prints the txid to the console
print(ergo.txId(genesis_tx))  
outBox_list = []

for x in range(consecutive_transactions):
    if x == 0: # first tx has to get input box from the genesis outbox
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=genesis_outbox,
                                            return_signed=True, chained=True)
    elif x == consecutive_transactions - 1: # last tx is not chained
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=outBox_list[x - 1],
                                            return_signed=True)
    else: # gets input box from the prior chained tx
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=outBox_list[x - 1],
                                            return_signed=True, chained=True)
    tx_1_outbox = appkit.get_outputs_to_spend(tx_1, 0)
    outBox_list.append(tx_1_outbox)
    time.sleep(sleep_time)

# submit transaction to the node
print(ergo.txId(tx_1)) 

time.sleep(sleep_time)
helper_functions.exit()
```
