# Android



## Getting Started

Running an Ergo full node on an Android device is an interesting prospect for several reasons. It enables an individual who may not own a desktop or laptop computer to synchronize a copy of the entire Ergo blockchain on their mobile device, and it also makes it possible to utilize one's own node in applications such as the Ergo mobile wallet or the Ergo Mixer on their mobile device.


## Device Requirements

There are minimum system requirements to run an Ergo node on an Android OS device. Android OS of version 7.0 or higher, a minimum of 25 GB of available fast storage, and a minimum of 1GB ram available for apps (1GB is untested, but it should work with some patience). So far, this has been tested and is working well on a Samsung Galaxy S8+.

## Preparation

A terminal emulator app is required to run an Ergo node on an Android device. The emulator app, Termux, has been tested and works well for running the node. To download Termux, you will need first to download and install [F-Droid](https://f-droid.org), an installable catalog of FOSS (Free and Open Source Software) applications for the Android platform. 

Within F-droid, search for `Termux - Terminal emulator with packages` and then download and install it.

## Installing Packages in Termux

The next step is to launch Termux and update and upgrade all packages. Using the default responses to all the prompts during the upgrade is okay.

```
pkg upgrade
```
The next step is to install the packages wget and OpenJDK-17. These are necessary to download the .jar file from GitHub and run it.

```
pkg install wget openjdk-17
```

## Ergo Client Release Download & Setting Up the Config File

The next step is downloading the latest Ergo client release from Github with wget. You can find it [here](https://github.com/ergoplatform/ergo/releases).

Make sure you copy the direct link to the file.

```
wget https://github.com/ergoplatform/ergo/releases/download/v5.0.4/ergo-5.0.4.jar
```

Now a config file named ergo.conf needs to be created. To do this, we will use nano. 

```
nano ergo.conf
```

Copy the following text into nano and do CTRL + O, then ENTER to save and CTRL + X to quit.

```
ergo {
   node {
       mining = false
   }
}
```

## Running the Node For the First Time

Issue the following command to run the node for the first time. (make sure you replace "`<release>` "with the version of the node that you have downloaded)

```
java -jar ergo-<release>.jar --mainnet -c ergo.conf
```
  
At this point, the node will begin synchronization. To view the progress, open a browser on the device, and go to the Ergo Node panel at http://127.0.0.1:9053/panel.

Please refer to the [manual install](manual.md) guide for more details regarding node configuration; however, setting up the API key and wallet is unnecessary.

## Tips and Tricks
  
I recommend downloading a different keyboard to be used in Termux. The stock Samsung keyboard was not working well in my case. A keyboard called Hacker's Keyboard can be found in F-Droid that worked great for me.
  
If you would like your node to be reachable, port forwarding will need to be set up on port 9030 for the Android device in your home router settings.
  
Specifying the Java heap space with the -Xmx flag may be necessary on your device. On the Samsung S8+, a heap size of -Xmx1536M worked well. An example of the node start command with a heap size of 2Gb looks like 

```
java -Xmx2G  -jar ergo-<release>.jar --mainnet -c ergo.conf
```  
If you have the Ergo Wallet App, you can replace the default node with [http://127.0.0.1:9053](http://127.0.0.1:9053). This way, you can use the node running on the Android device. 
  
Installing a package called tmux will help if you want to run other programs alongside the node within Termux.
