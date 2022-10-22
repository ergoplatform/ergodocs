The Ergo Node is part of Ergo's peer-to-peer network which hosts and synchronises a copy of the entire Ergo blockchain and a critical piece of infrastructure developers will use to interact with the blockchain. 

There is no financial incentive to run a node, but doing so helps increase the security of the network.

If you want to install a node see this page or get [setup on the test-net](/dev/start/testnet/)

> If you're simply looking for a daily wallet we advise one of the options in the [wallets](/dev/wallet) page. (Ergo Mobile even has a cold-storage feature!). You can also use the [Satergo desktop wallet](dev/wallet/wallets/#satergo-desktop) which has an option to install a full node with it. 

## Prerequisites
To run an Ergo node you need a **JDK/JRE version >= 9** installed on your system. 

We recommend [Oracle Java SE](https://www.oracle.com/technetwork/java/javase/overview/index.html) or for Unix-based operating systems, SDKMAN.

```bash
curl -s "https://get.sdkman.io" | bash
sdk install java 11.0.13.8.1-amzn
```

The only hardware requirements is ~20GB of space to store the chain, and ~8GB of RAM memory for handling the sync.

## Running the node

Create a dedicated folder (such as `~/ergo`) for running the node and download the latest [Ergo client release](https://github.com/ergoplatform/ergo/releases/) `.jar` 

> Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using [SBT](https://www.scala-sbt.org/) by issuing the `sbt assembly` command. Alternatively, you can also use [Docker](/node/install/docker)



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
java -jar -Xmx4G ergo-*.jar --mainnet -c ergo.conf
```

- The `-Xmx4G` flag sets the max heap size for the JVM. `4-6G` recommended.

It is better to use more memory on heap`-Xmx4g` for initial syncing. `-Xmx1g` should be enough when node is full synced.
The node will start syncing immediately after this. Wait for a few minutes for the API to start and go to the next step.

> **Note:** You can use any name for the file instead of `ergo.conf`. All configuration parameters are to be passed through this file and you only need to rewrite parameters that you want to change from the default values. The above config file actually has the default values. 

The node will start syncing immediately after this. 


## Securing the API

We need to set a secret password to protect the API. In this example we'll use `hello` - but **you must use a different and strong secret.**

Go to [127.0.0.1:9053/swagger#/utils/hashBlake2b](http://127.0.0.1:9053/swagger#/utils/hashBlake2b) and call the API to compute the `Blake2b` hash of your secret. 

![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

Copy the hash response which we'll place back in the `ergo.conf` file. 

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


**Next Steps**

- [Initialising a wallet](/node/wallet)
- [Troubleshooting](/node/install/troubleshooting)
- [FAQ](/node/#faq)
- [Using the TestNet](/dev/start/testnet)

To safely shut down the node, use the following command

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

Running this command in a new terminal will let you spot any errors or warnings. 

```
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
```


## Check if the node is synced

While the node is syncing, the panel will show "Active synchronization" (see the image below).

![active synchronization](https://user-images.githubusercontent.com/23208922/71128146-94d58b80-2212-11ea-9010-5b61a91e8549.png)

After the node is fully synced, the text will change to "Node is synced", as shown below.

![synced](https://user-images.githubusercontent.com/23208922/71301767-8da4ae00-23c9-11ea-8fc0-a92a9d78b821.png)

You can also check this at [127.0.0.1:9053/info](http://127.0.0.1:9053/info) and compare to the latest block height given at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/en/)


## Resources

- [FAQ](faq.md)
- [API Docs](https://api.ergoplatform.com/api/v1/docs/)
- [Node API](https://git.io/fjqwb)
- [Explorer API](https://git.io/fjqwN)
- [Ergo.Watch API](https://ergo.watch/api/v0/docs)
- [TokenJay API](https://api.tokenjay.app/swagger-ui/index.html;jsessionid=59429AD4DF081E2E3450C2834095D427?attribute=redirectWithRedirectView)
- [synced-node](https://github.com/mgpai22/ergo-synced-node)
- [ergonodes.net](http://ergonodes.net/) 




