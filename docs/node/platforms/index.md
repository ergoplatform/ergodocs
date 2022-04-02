# Getting Started

The Ergo Node is a critical piece of infrastructure developers will use to interact with the blockchain. If you're simply recommending a daily wallet we advice one of the options in the [wallets](/dev/wallet) page. 

Supporting pages

- [Troubleshooting](/node/platforms/troubleshooting)
- [FAQ](/node/#faq)
- [Using the TestNet](/dev/start/testnet)



## Running the node

Create a dedicated folder (such as `~/ergo`) for running the node and download the latest [Ergo client release](https://github.com/ergoplatform/ergo/releases/) `.jar` 

Create a configuration file `ergo.conf` containing the following text
```
ergo {
	node {
		mining = false
	}
}
```

Then issue the following command to run the node for the first time.

```bash
java -jar -Xmx4G -Dlogback.stdout.level=WARN -Dlogback.file.level=ERR ergo.jar --mainnet -c ergo.conf
```

- The `-Xmx4G` flag sets the max heap size for the JVM. `3-4G` recommended.
- The `-Dlogback` flags reduces the number of logs returned. 

The node will start syncing immediately after this. Wait for a few minutes for the API to start and go to the next step.


## Securing the API

We need to set a secret password to protect the API. In this example we'll use `hello` - but you **must use a different and strong secret.**

Go to [127.0.0.1:9053/swagger#/utils/hashBlake2b](http://127.0.0.1:9053/swagger#/utils/hashBlake2b) and call the API to compute the `Blake2b` hash of your secret. 

> ![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

Copy the hash response which we'll place back in the `ergo.conf` file. 

As you can see 

`hello` corresponds to the `Blake2b` hash `324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf`

> ![response](https://user-images.githubusercontent.com/23208922/69916509-c3690d80-1481-11ea-869f-630cd59cc525.png)

We then need to update the config file with API key hash

```conf
	ergo {
	  node {
	    mining = false
	  }
	}
	
	scorex {
	 restApi {
	    ## Hex-encoded Blake2b256 hash of an API key. 
	    ## Should be 64-chars long Base16 string.
	    ## below is the hash of the string 'hello'
	    ## replace with your actual hash 
	    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
	  }
	}
```

Restart and your node should now be syncing and you should be able to access the API. 

If you'd like to initialise a wallet see [this page](/node/wallet)

## Check if the node is synced

While the node is syncing, the panel will show "Active synchronization" (see the image below).

> ![active synchronization](https://user-images.githubusercontent.com/23208922/71128146-94d58b80-2212-11ea-9010-5b61a91e8549.png)

After the node is fully synced, the text will change to "Node is synced", as shown below.

> ![synced](https://user-images.githubusercontent.com/23208922/71301767-8da4ae00-23c9-11ea-8fc0-a92a9d78b821.png)

You can also check this at [127.0.0.1:9053/info](http://127.0.0.1:9053/info) and compare to the latest block height given at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/en/)

## Shutdown 

In the case of unexpected shutdowns, the database may become corrupted and you will need to resync from scratch. 

To safely shut down the node, use the following command

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

To relaunch the node

```bash
java -jar -Xmx4G -Dlogback.stdout.level=WARN -Dlogback.file.level=ERR ergo.jar --mainnet -c ergo.conf
```

Please see the [troubleshooting page](/node/platforms/troubleshooting) for more information. 

## Install Script

> Experimental

Simply run the following command

```
bash -c "$(curl -s https://node.phenotype.dev)"
```


For a full install including prerequisites (Java)

- [Mac](/node/platforms/mac)
- [Linux](/node/platforms/linux)
- [Pi](/node/platforms/pi)
- [Windows](/node/platforms/windows)
- [Docker](/node/platforms/docker)

