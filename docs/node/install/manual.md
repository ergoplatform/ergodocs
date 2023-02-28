# Manual Install

This guide is for installing a full node on a server. If you want a full node on your desktop, try [Satergo](https://satergo.com)

## Running the node

Create a dedicated folder (such as `~/ergo`) for running the node and download the latest [Ergo client release](https://github.com/ergoplatform/ergo/releases/) `.jar` 

> Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using [SBT](https://www.scala-sbt.org/) by issuing the `sbt assembly` command. Alternatively, you can also use [Docker](/node/install/docker)



Create a configuration file `ergo.conf` in the same directory as the .jar with the following text
```
ergo {
	node {
		mining = false
	}
}
```

Then issue the following command to run the node for the first time.

```bash
java -jar -Xmx4G ergo-*.jar --mainnet -c ergo.conf
```

> The `-Xmx4G` flag sets the max heap size for the JVM. `4-6G` is recommended depending on your memory allocation.  It is better to use more memory on heap`-Xmx4g` for initial syncing. `-Xmx1g` should be sufficient once the node is fully synced.


The node will start syncing immediately after this. Wait for a few minutes for the API to start and go to the next step.

> **Note:** You can use any name for the file instead of `ergo.conf`. All configuration parameters are to be passed through this file and you only need to rewrite parameters that you want to change from the default values. The above config file actually has the default values. 



## Securing the API

We need to set a secret password to protect the API. In this example, we'll use `hello`, but **you must** use a different and strong secret.**

Navigate [127.0.0.1:9053/swagger#/utils/hashBlake2b](http://127.0.0.1:9053/swagger#/utils/hashBlake2b) and call the API to compute the `Blake2b` hash of your secret. 

> **Please note that `127.0.0.1` is your local machine** and the .jar must be running for it to be available. 

![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

Copy the hash response, which we will place back in the `ergo.conf` file. 

As you can see `hello` corresponds to the `Blake2b` hash `324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf`

![response](https://user-images.githubusercontent.com/23208922/69916509-c3690d80-1481-11ea-869f-630cd59cc525.png)

We then need to update the config file with API key hash

```bash
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


## Check if the node is synced

While the node is syncing, the panel will show "Active synchronization" (see the image below).

![active synchronization](https://user-images.githubusercontent.com/23208922/71128146-94d58b80-2212-11ea-9010-5b61a91e8549.png)

After the node is fully synced, the text will change to "Node is synced", as shown below.

![synced](https://user-images.githubusercontent.com/23208922/71301767-8da4ae00-23c9-11ea-8fc0-a92a9d78b821.png)

You can also check this at [127.0.0.1:9053/info](http://127.0.0.1:9053/info) and compare to the latest block height given at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/en/)

## Shutdown

To safely shut down the node, use the following command

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

Running this command in a new terminal will let you spot any errors or warnings. 

```
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
```


**Next up,** [initialising your wallet](/node/wallet)

## Resources

- [Troubleshooting](/node/install/troubleshooting)
- [FAQ](node-faq.md)
- [Using the TestNet](/node/testnet)