# ErgoPi

## Getting Started

The Raspberry Pi is small, inexpensive, and meets the requirements to run an Ergo full node.

Alternatively to the simple instructions below, see [Tutorial: Running an Ergo Full Node on a Headless Raspberry Pi](https://github.com/ccgarant/ergo-full-node-raspi) for a more comprehensive start to finish setup guide. 


### Prerequisites 

- Pi4 with 4gb RAM or above is optimal. 
- Due to the intensive disk I/O, a SSD with 64GB+ is preferred.

### Preperation

```
sudo apt update && sudo apt upgrade -y
sudo apt install default-jdk -y
```

Install the Java JDK

```
sudo apt install default-jdk
```

#### SWAP Size

The Raspberry Pi is a very powerful device but it has some limitations which prevent it from syncing a full Ergo node quickly and efficiently. Below are a few things you can do to ensure a smooth setup process.

Increase the swap space your Pi has access to

```bash
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```

Increase to `4096` (MB)

```bash
CONF_SWAPSIZE=4096
```

Then re-enable the swap and reboot.

```bash
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
sudo reboot now
```


#### More tips

- WiFi has less issues than Ethernet
- Make sure your Pi is in a well-vented area. 
- Disable your screen-saver for the sync. 
- [Using ZRAM](https://ikarus.sg/using-zram-to-get-more-out-of-your-raspberry-pi/)

### Quick Start

This script will download the latest version of the node, prompt you to set an API key, and start the sync while displaying the progress in terminal. 

```bash
bash -c "$(curl -s https://node.phenotype.dev)"
```

If you'd prefer to get set up manually, here's a [step-by-step guide](https://github.com/ergoplatform/ergo/wiki/Set-up-a-full-node). When ready to launch the node make sure to set a maximum limit of 2GB by using the `-Xmx2g` flag.




## Light Mode

A basic config on mainnet should look like this

```conf
ergo {
    node {
        mining = false
    }

}      
        
scorex {
    restApi {
        apiKeyHash = "$BLAKE_HASH"
    }
}
```

There are several configuration options that be tweaked in your `ergo.conf` file. The [resource directory on the main GitHub repository](https://github.com/ergoplatform/ergo/tree/master/src/main/resources) has examples of all available options. 

- `skipV1TransactionsValidation`: Skip validation of transactions before block 417,792
- `blocksToKeep` denotes the number of blocks to keep with transactions and `ADproofs`. 
- `stateType` with the options `utxo` and `digest`.
  - `utxo` keep full utxo set, that allows to validate arbitrary block and generate ADProofs. (default)
  - `digest` - keep state root hash only and validate transactions via ADProofs.
- `maxConnections`: The maximum amount of peers the node should try and connect to over the P2P layer. 




#### Launch

```
java -jar -Xmx2g ergo.jar --mainnet -c ergo.conf
```



## Resources

- [How to setup an Ergo Node on a Raspberry Pi](https://youtu.be/yDqhlgz0244)
- [ergo-rpi](https://github.com/Eeysirhc/ergo-rpi)

