# How to set up and configure a full Ergo node

## Quick Start

You can run [ergo-installer.sh](https://github.com/ergoplatform/ergo/blob/master/ergo-installer.sh)

```bash
curl -s https://raw.githubusercontent.com/ergoplatform/ergo/master/ergo-installer.sh | sh -s -- --api-key=<YOUR_API_KEY>
```

With this script you'll have the latest Ergo node installed without any hassle.

If you'd prefer to get set up manually, here's a [step-by-step guide](https://github.com/ergoplatform/ergo/wiki/Set-up-a-full-node).

## Optimization

The Raspberry Pi is a very powerful device but it has hardware limitations which prevent it from syncing a full Ergo node quickly and efficiently. Below are a few things you can do to ensure a smooth setup process.

> Note: This was written as of Ergo node release 4.0.27 and tested on multiple Pi4 with 4gb RAM

### Memory

If you are booting from a microSD card then it is definintely worth paying a little more for the extra headroom. 

* 32gb: completed node sync in 4.5 days
* 256gb: completed node sync in 40 hours

### SWAP Size

Increase the system's total accessible memory beyond its hardware capabilities. 

```bash
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
CONF_SWAPSIZE=4096 
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
sudo reboot now
```

### Limit Heap

When ready to launch the node we want to set a maximum limit of 2gb.

```bash
java -Xmx2g -jar ergo-<release-version>.jar --mainnet -c ergo.conf
```


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


## Resources

- [How to setup an Ergo Node on a Raspberry Pi](https://youtu.be/yDqhlgz0244)



