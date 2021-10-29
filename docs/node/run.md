# How to set up and configure a full Ergo node

This tutorial explains how to install and run a full Ergo node. It does not cover mining. 

Windows users can also watch the video tutorial. 

[![How to set up and configure a full Ergo node on Windows (video)](https://user-images.githubusercontent.com/23208922/89564982-7670de80-d83b-11ea-874d-bda65a0141ee.png)](https://www.youtube.com/watch?v=fpEDJ1CM6ns "How to configure a full node on Windows (Video tutorial)")

# Node security

There are a few important aspects of node usage that your wallet and money's safety depends on:
* An Ergo node requires storing security-critical parameters in the configuration file. You should never make this file public.
* An Ergo node provides a REST API for interacting with the built-in wallet. Sensitive API methods require a security token, which should never be sent over untrusted channels.
* Access to the Ergo REST API must be restricted to known hosts. In particular, the API must not be accessible from the Internet.

# Prerequisites
To run an Ergo node you need a **JDK/JRE version >= 9** installed on your system. We recommend either version 9 or 11. One way to do this is to install [Oracle Java SE](https://www.oracle.com/technetwork/java/javase/overview/index.html).

**Note that Oracle JDK/JRE <= 8 is no longer supported**. 

The next step is to download the latest [Ergo client release](https://github.com/ergoplatform/ergo/releases/) jar file and create a node configuration file.

Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using [SBT](https://www.scala-sbt.org/) by issuing the `sbt assembly` command.

Create a dedicated folder (such as `~/ergo`) for running the node.
Denote by **ergo_folder** the folder where the jar is kept. 
 
# Running the node for the first time

Create a configuration file `ergo.conf` with the following text in **ergo_folder**. 

	ergo {
	  node {
	    mining = false
	  }
	}

Open a command prompt and `cd` to **ergo_folder**. Then issue the following command to run the node for the first time:

     java -jar ergo-<release>.jar --mainnet -c ergo.conf

The node will start syncing immediately after this. Wait for a few minutes for the API to start and go to the next step.

**Note:** You can use any name for the file instead of `ergo.conf`. All configuration parameters are to be passed through this file and you only need to rewrite parameters that you want to change from the default values. The above config file actually has the default values. 

# Compute the hash of your secret

First, select a secret to protect your API. 
Then go to http://127.0.0.1:9053/swagger#/utils/hashBlake2b and call the API to compute the hash of your secret. Refer to the image below.

![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

Copy the response containing the hash for use in the next step (see below image). In our example, the secret is `hello` whose hash corresponds to `324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf`. 

**IMPORTANT** You must use a different and strong secret. 

![response](https://user-images.githubusercontent.com/23208922/69916509-c3690d80-1481-11ea-869f-630cd59cc525.png)

# Update config file with API key hash

Edit the config file `ergo.conf` and paste the hash copied in the previous step. The file should look as follows:

	ergo {
	  node {
	    mining = false
	  }
	}
	
	scorex {
	 restApi {
	    # Hex-encoded Blake2b256 hash of an API key. 
	    # Should be 64-chars long Base16 string.
	    # below is the hash of the string 'hello'
	    # replace with your actual hash 
	    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
	  }
	}

# Initialize wallet

Restart the node and go to [http://127.0.0.1:9053/panel](http://127.0.0.1:9053/panel) to access the panel. Then set the API key secret from the previous step. Note that you need to set the **secret** and not the hash from the config file. In our example, this is the string `hello`. 

![set API key](https://user-images.githubusercontent.com/23208922/69916579-b7ca1680-1482-11ea-880e-251c8139a613.png)

Click on **Initialize wallet**. After the pop-up opens, there are two ways to proceed depending on your scenario.

1. If this is the first time you are running the node then you need to initialize it with a new mnemonic sentence.
2. If you had created a wallet earlier and would like to obtain the same address (possibly because there are funds stored in it), then you have to restore the wallet using the mnemonic sentence you had saved earlier. 

Follow one of the below steps depending on your situation. 
 
## Initialize wallet from scratch

![Initialize wallet](https://user-images.githubusercontent.com/23208922/69916584-d4fee500-1482-11ea-838c-e8aba9f41c76.png)

In the pop-up that opens, you must enter a wallet password. The mnemonic password is optional. After you click send, the wallet will return a mnemonic sentence as shown below. 

![mnemonic sentence](https://user-images.githubusercontent.com/23208922/69916693-2360b380-1484-11ea-9366-1bf9eb0f8b30.png)

You must copy this sentence and save it in a safe place. This sentence will be needed to restore the wallet on a different computer.

## Restore wallet from earlier

Copy the mnemonic sentence from earlier paste it into the "Mnemonic" field in the Restore-wallet form. Enter a secure wallet password. Leave the Mnemonic password empty (it is only for advanced users). Refer to the figure below.

![restore wallet](https://user-images.githubusercontent.com/23208922/71127599-66a37c00-2211-11ea-9b9e-9a69ac80c306.png)

After the wallet has been successfully restored from the mnemonic sentence, you will see a confirmation as shown in the figure below.

![successfully restored confirmation](https://user-images.githubusercontent.com/23208922/71127600-673c1280-2211-11ea-95eb-7c775c59180d.png)

# Get wallet addresses

This is a test to ensure you have set up the node properly. It will return the current addresses in the wallet. 
In the panel at [http://127.0.0.1:9053/panel](http://127.0.0.1:9053/panel) click on the `Wallet` tab on the left and then on `Get all wallet addresses` to view the addresses currently maintained by the wallet. It should return at least one address if the node is set correctly.

![Get addresses](https://user-images.githubusercontent.com/23208922/69978955-5b82f780-1553-11ea-85b6-413c63a46334.png)

# Check if the node is synced

While the node is syncing, the panel will show "Active synchronization" (see the image below).

![active synchronization](https://user-images.githubusercontent.com/23208922/71128146-94d58b80-2212-11ea-9010-5b61a91e8549.png)

After the node is fully synced, the text will change to "Node is synced", as shown below.

![synced](https://user-images.githubusercontent.com/23208922/71301767-8da4ae00-23c9-11ea-8fc0-a92a9d78b821.png)

# Check wallet balance

Once the node is synced, use the wallet API in the panel to see your balance, as shown below.

![check balance](https://user-images.githubusercontent.com/23208922/71127598-66a37c00-2211-11ea-9d53-f6d7738d1726.png)

# Sending funds

If there is a non-zero balance, you can send Ergs to any other address using the panel as shown below:

![send ergs](https://user-images.githubusercontent.com/23208922/71129066-a28c1080-2214-11ea-9806-7d768059980a.png)

# View the Swagger UI

A Swagger UI is available at [http://127.0.0.1:9053/swagger](http://127.0.0.1:9053/swagger). You had already used it earlier to compute the hash of your secret. 
You can also use this UI to make API calls for advanced operations that are not (yet) available in the panel. Some examples of this are:

1. Creating non-standard transactions with registers and context variables.
2. Creating transactions that issue tokens.
3. Creating transactions that use certain boxes as inputs. 

A future article will discuss each of these operations in detail. 

Note that most methods in the API are protected and you would need to use your secret (from earlier) to access these methods. The following images show the process of setting this secret in the Swagger UI.

Navigate to the top of the page and click the "Authorize" button. Enter your secret in the form that pops-up as shown in the figure below.
![Enter API key](https://user-images.githubusercontent.com/23208922/69916784-450e6a80-1485-11ea-9bb5-681438d11970.png)

After the password is entered and you have clicked "Authorize", you will be shown the popup below:
![Logged in](https://user-images.githubusercontent.com/23208922/69916787-4a6bb500-1485-11ea-90c8-39b274d0f36d.png)

Now navigate to [http://127.0.0.1:9053/swagger#/wallet/walletAddresses](http://127.0.0.1:9053/swagger#/wallet/walletAddresses) **in the same tab where you entered the password** and click on "Try it out". You should see the same list of addresses as you saw earlier from the panel. 

![Get addresses](https://user-images.githubusercontent.com/23208922/69916855-f9a88c00-1485-11ea-8705-887ccffe6471.png)