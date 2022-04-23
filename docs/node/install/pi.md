## How to set up and configure a full Ergo node


You can run [ergo-installer.sh](https://github.com/ergoplatform/ergo/blob/master/ergo-installer.sh)

```bash
curl -s https://raw.githubusercontent.com/ergoplatform/ergo/master/ergo-installer.sh | sh -s -- --api-key=<YOUR_API_KEY>
```

With this script you'll have the latest Ergo node installed without any hassle.

If you'd prefer to get set up manually, here's a [step-by-step.](/node/platforms/tutorial).

## Light Mode
```conf
ergo {
    node {
        # Full options available at 
        # https://github.com/ergoplatform/ergo/blob/master/src/main/resources/application.conf
        
        mining = false

        # Skip validation of transactions in the mainnet before block 417,792 (in v1 blocks).
        # Block 417,792 is checkpointed by the protocol (so its UTXO set as well).
        # The node still applying transactions to UTXO set and so checks UTXO set digests for each block.
        skipV1TransactionsValidation = true
        
        # Number of last blocks to keep with transactions and ADproofs, for all other blocks only header will be stored.
        # Keep all blocks from genesis if negative
        blocksToKeep = 1440 # keep ~2 days of blocks
        
        # State type.  Possible options are:
        # "utxo" - keep full utxo set, that allows to validate arbitrary block and generate ADProofs
        # "digest" - keep state root hash only and validate transactions via ADProofs

        stateType = digest # Note: You cannot validate arbitrary block and generate ADProofs due to this


    }

}      
        
scorex {
    restApi {
        apiKeyHash = "$BLAKE_HASH"
        
    }
    network {
		    # Max P2P connections
			# Lower number better for low-RAM
            maxConnections = 10

        }
}
```


### Resources

- [How to setup an Ergo Node on a Raspberry Pi](https://youtu.be/yDqhlgz0244)
