## How to set up and configure a full Ergo node

This page explains how to install and run a full Ergo node. It does not cover mining. 

- Windows users can also watch the [video tutorial](https://www.youtube.com/watch?v=fpEDJ1CM6ns). 
- UNIX Systems can run [ergo-installer.sh](https://github.com/ergoplatform/ergo/blob/master/ergo-installer.sh)

## Prerequisites
To run an Ergo node you need a **JDK/JRE version >= 9** installed on your system. We recommend either version 9 or 11. One way to do this is to install [Oracle Java SE](https://www.oracle.com/technetwork/java/javase/overview/index.html) or [SDKMAN](https://sdkman.io/install) for UNIX based systems.

 
## Running the node for the first time

Create a dedicated folder (such as `~/ergo`) for running the node.
```bash
mkdir ergo
cd ergo
```

Download the latest [Ergo client release](https://github.com/ergoplatform/ergo/releases/) `.jar` 

Create a configuration file `ergo.conf` 

```
touch ergo.conf
```
with the following text
```
	ergo {
	  node {
	    mining = false
	  }
	}
```
Then issue the following command to run the node for the first time (from within the `ergo` folder):
```
java -jar -Xmx3G ergo-<release>.jar --mainnet -c ergo.conf
# The -Xmx flag sets the max heap size for the jvm
```
The node will start syncing immediately after this. Wait for a few minutes for the API to start and go to the next step.

> **Note:** You can use any name for the file instead of `ergo.conf`. All configuration parameters are to be passed through this file and you only need to rewrite parameters that you want to change from the default values. The above config file actually has the default values. 

## Compute the hash of your secret

We need to set a secret password to protect the API. In this example we'll use `hello` - but you **must use a different and strong secret.**

Go to [127.0.0.1:9053/swagger#/utils/hashBlake2b](http://127.0.0.1:9053/swagger#/utils/hashBlake2b) and call the API to compute the `Blake2b` hash of your secret. 

> ![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

Copy the hash response which we'll place back in the `ergo.conf` file. 

> ![response](https://user-images.githubusercontent.com/23208922/69916509-c3690d80-1481-11ea-869f-630cd59cc525.png)

## Update config file with API key hash

Edit the config file `ergo.conf` and paste the hash copied in the previous step. The file should look as follows:
```
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

Your node should now be syncing. If you'd like to initialise a wallet place see [this page](/node/wallet)

## Check if the node is synced

While the node is syncing, the panel will show "Active synchronization" (see the image below).

> ![active synchronization](https://user-images.githubusercontent.com/23208922/71128146-94d58b80-2212-11ea-9010-5b61a91e8549.png)

After the node is fully synced, the text will change to "Node is synced", as shown below.

> ![synced](https://user-images.githubusercontent.com/23208922/71301767-8da4ae00-23c9-11ea-8fc0-a92a9d78b821.png)

In the case of unexpected shutdowns the database may become corrupted and you need to resync.

To do so remove the following two folders and restart the node. 

```
rm -rf .ergo/state
rm -rf .ergo/history
```

## Deriving Addresses

Navigate to `localhost:9053/swagger#/wallet/walletDeriveKey` 

click **Try it out**

```  
"derivationPath": "m/44'/429'/0'/0/0" 
```

The wallet needs to be unlocked, and you need to authorize on top right on swagger
click execute and check the address you get in the response

## Node security

There are a few important aspects your wallet and money's safety depends on:

* You should never make the `ergo.conf` file public.
* Sensitive API methods require a security token, which should never be sent over untrusted channels.
* Access to the Ergo REST API must be restricted to known hosts. In particular, the API must not be accessible from the Internet.

## Compiling from source
Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using the [`sbt assembly`](https://www.scala-sbt.org/)  command.
