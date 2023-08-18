# Executing a Chained Transaction

Chained transactions allow for the sequential use of outputs from off-chain transactions. This guide will walk you through the process of submitting a chained transaction on Ergo. The basic method demonstrated here is based on the [ergpy examples](https://github.com/mgpai22/ergpy/tree/main/examples). For managing extensive interlinked transactions, you can refer to the [Transaction Group framework](https://github.com/GetBlok-io/Subpooling#frameworks--abstractions) provided by GetBlok.

## Establish a Blockchain Connection

Start by defining the URL of the node to connect to the Ergo blockchain. This could be either a MainNet or TestNet node URL. The connection is then established using the `ErgoAppKit`.

```python
# Assign the node URL
node_url: str = "http://213.239.193.208:9052/"

# Establish the connection
ergo = appkit.ErgoAppKit(node_url=node_url)
```

## Set Up Wallet Mnemonic

Next, prepare your wallet mnemonic. This is a sentence-like password that will be used to access your wallet. This example includes receiver addresses and the amount to be sent in each transaction. Furthermore, it sets a sleep time, which is the delay between transaction submissions. The required amount for the genesis outbox, which is the first transaction in the chain, is also calculated.

```python
# Define the wallet mnemonic
wallet_mnemonic = "decline reward asthma enter three clean borrow repeat identify wisdom horn pull entire adapt neglect."

# Specify receiver addresses
receiver_addresses = [
    "3WwdXmYP39DLmDWJ6grH9ArXbWuCt2uGAh46VTfeGPrHKJJY6cSJ",
    "3WwuG9amNVDwkJdgT5Ce7aJCfeoafVmd9tag9AEiAZwgPi7pYX3w",
    "3Wxk5oofZ3Laq2CpFW4Fi9YQiaep9bZr6QFg4s4xpzz4bi9tZq2U"
]

# Define the amount for each transaction
amount = [0.22, 0.33, 0.11]

# Set the number of consecutive transactions
consecutive_transactions = 3

# Define the time gap between submissions of transactions
sleep_time = 0.5 

# Calculate the total amount for the genesis outbox
genesis_amount = [consecutive_transactions * (0.22 + 0.33 + 0.11) + (consecutive_transactions + 1) * 0.001]

# Wallet of the sender
genesis_receiver = [""]  
```

## Generate an Output Box

To create an output box from the signed transaction, we use the `simple_send` method from the `helper_functions` module. The function returns a signed transaction, which we then use to obtain the genesis outbox.

```python
# Generate a signed transaction
genesis_tx = helper_functions.simple_send(ergo=ergo, amount=genesis_amount, wallet_mnemonic=wallet_mnemonic,
                                          receiver_addresses=genesis_receiver, return_signed=True)
# Get the genesis outbox
genesis_outbox = appkit.get_outputs_to_spend(genesis_tx, 0)      
```

## Submit the Transactions

Finally, we submit the transactions to the node. For each transaction in the chain, we use the output box from the previous transaction as the input box for the current transaction. The first transaction retrieves the input box from the genesis outbox. The last transaction is not chained, i.e., its output box

 will not be used as an input box in any subsequent transaction. The ID of the genesis transaction and the last transaction are printed to the console. After the final transaction is submitted, the process ends.

```python
# Print the transaction ID of the genesis transaction
print(ergo.txId(genesis_tx))  

outBox_list = []

# Process all the transactions in the chain
for x in range(consecutive_transactions):
    # If it's the first transaction
    if x == 0: 
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=genesis_outbox,
                                            return_signed=True, chained=True)
    # If it's the last transaction
    elif x == consecutive_transactions - 1: 
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=outBox_list[x - 1],
                                            return_signed=True)
    # If it's neither the first nor the last transaction
    else: 
        tx_1 = helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic,
                                            receiver_addresses=receiver_addresses, input_box=outBox_list[x - 1],
                                            return_signed=True, chained=True)
    # Get the outbox from the current transaction
    tx_1_outbox = appkit.get_outputs_to_spend(tx_1, 0)
    outBox_list.append(tx_1_outbox)
    
    # Pause before processing the next transaction
    time.sleep(sleep_time)

# Print the transaction ID of the last transaction
print(ergo.txId(tx_1)) 

# Pause before ending the program
time.sleep(sleep_time)

# End the program
helper_functions.exit()
```
