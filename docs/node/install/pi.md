# ErgoPi

## Getting Started


### Prerequisites 

To sync a full node in `utxo` mode. While ~20GB is sufficient - If you are booting from a microSD card then it is definintely worth paying a little more for the extra headroom. 

* 32gb: completed node sync in 4.5 days
* 256gb: completed node sync in 40 hours

A Pi4 with 4gb RAM or above is optimal. 

### Preperation

```
sudo apt update
sudo apt upgrade
```

Install the Java JDK

```
sudo apt install default-jdk
```

#### SWAP Size

The Raspberry Pi is a very powerful device but it has hardware limitations which prevent it from syncing a full Ergo node quickly and efficiently. Below are a few things you can do to ensure a smooth setup process.

Increase the system's total accessible memory beyond its hardware capabilities. 

```bash
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```

Then replace the value to match this

```bash
CONF_SWAPSIZE=4096
```

Finally, re-enable and reboot.

```bash
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
sudo reboot now
```

### Quick Start

This will download the latest version of the node, prompt you to set an API key, and start the sync while displaying the progress in terminal. 

```bash
bash -c "$(curl -s https://node.phenotype.dev)"
```

If you'd prefer to get set up manually, here's a [step-by-step guide](https://github.com/ergoplatform/ergo/wiki/Set-up-a-full-node). When ready to launch the node we want to set a maximum limit of 2GB by using the `-Xmx2g`.




## Light Mode

There are several configuration options that be tweaked in your `ergo.conf` file. 


- `skipV1TransactionsValidation`: Skip validation of transactions before block 417,792
- `blocksToKeep` denotes the number of blocks to keep with transactions and `ADproofs`. 
- `stateType` with the options `utxo` and `digest`.
  - `utxo` keep full utxo set, that allows to validate arbitrary block and generate ADProofs. (default)
  - `digest` - keep state root hash only and validate transactions via ADProofs.
- `maxConnections`: The maximum amount of peers the node should try and connect to over the P2P layer. 

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
