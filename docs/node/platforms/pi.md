## How to set up and configure a full Ergo node

This page explains how to install and run a full Ergo node. It does not cover mining. 

- UNIX Systems can run [ergo-installer.sh](https://github.com/ergoplatform/ergo/blob/master/ergo-installer.sh)


## Tutorial

### Getting Started

To run an Ergo node you need a **JDK/JRE version >= 9** installed on your system. We recommend either version 9 or 11. One way to do this is to install [SDKMAN](https://sdkman.io/install) for UNIX based systems 

```
curl -s "https://get.sdkman.io" | bash
sdk install java
```


### Running the node

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
java -jar -Xmx3G -Dlogback.stdout.level=WARN -Dlogback.file.level=ERR ergo.jar --mainnet -c ergo.conf
# The -Xmx flag sets the max heap size for the jvm
# low-level logging only
```
The node will start syncing immediately after this. Wait for a few minutes for the API to start and go to the next step.


### Securing the API

We need to set a secret password to protect the API. In this example we'll use `hello` - but you **must use a different and strong secret.**

Go to [127.0.0.1:9053/swagger#/utils/hashBlake2b](http://127.0.0.1:9053/swagger#/utils/hashBlake2b) and call the API to compute the `Blake2b` hash of your secret. 

> ![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

Copy the hash response which we'll place back in the `ergo.conf` file. 

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

Your node should now be syncing. If you'd like to initialise a wallet place see [this page](/node/wallet)

### Check if the node is synced

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

### Deriving Addresses

Navigate to `localhost:9053/swagger#/wallet/walletDeriveKey` 

click **Try it out**

```  
"derivationPath": "m/44'/429'/0'/0/0" 
```

The wallet needs to be unlocked, and you need to authorize on top right on swagger
click execute and check the address you get in the response. Please note that Swagger will accept any password in the UI, but will fail to execute commands if the password provided is incorrect.

If you are certain the password you're using is correct, this issue can occur during database corruption. First, attempt to restart and see if the node can fix itself.  Otherwise, a resync will be required. 

See the [Swagger API](/node/swagger) page for more infomation. 

## Node security

Unless you are running the node on a publicly accessible web-server, your node should be protected by your router. 

If you wish to host a public node, there are a few important aspects your wallet and money's safety depends on:

* You should never make the `ergo.conf` file public.
* Sensitive API methods require a security token, which should never be sent over untrusted channels.
* Access to the Ergo REST API must be restricted to known hosts. In particular, the API must not be accessible from the Internet.

There is an [example nginx.conf](https://github.com/glasgowm148/ergoscripts/blob/main/misc/nginx.config) available.  

## Compiling from source

Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using the [`sbt assembly`](https://www.scala-sbt.org/)  command.
