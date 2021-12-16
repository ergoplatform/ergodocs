## Dust

Some users (miners in particular) may have noticed their Yoroi wallet becoming slow and unusable with the increasing number of transactions generated

This page provides an overview of how to recover access to your coins in this case.

## Why does this happen?

Ergo is based on the extended-UTXO model. A side-effect of UTXOs is a term coined *dust*. Dust refers to fractional values of ERG and is usually below the protocol fee, miner wallets are prone to becoming *dusty* with the stream of rewards coming into thier wallet. All these excess UTXOs can cause a slowdown and ultimately, make yoroi inaccessible. To get a deeper overview of transactions on Ergo please see [this page](../dev/protocol/transaction.md)

Yoroi is currently being restructured to elleviate this - in the meantime prevention tips and troubleshooting are available below. 


## Troubleshooting

### If you still have access to your wallet

- Use the **Send All Assets** function in yoroi to collect all your UTXO boxes into one. 
- Switch to the Mobile Wallet. 

### If your wallet is unresponsive

- If you have an Android device available, switch to the [mobile wallet](https://ergoplatform.org/en/wallets/) and restore your wallet. You may need to derive extra addresses for your balance to appear. 
- If on iOS, multiple addresses are not supported yet so you will need to use the node with the following steps.

1. Download and run the `.jar` file (see [node quick install](quick.md))
2. **While the node is syncing**, restore your wallet.
3. Derive any any extra addresses you may have using the instructions usomg [swagger API](swagger.md)


Once the node is fully syncronised you balance should be visible. 



### I've resynced and my balance is still 0

If you've written down your secret phrase, you may have miswrote or mistyped a word. The available words is [available here](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) and you will need to manually check each word and determine any mistakes. 



