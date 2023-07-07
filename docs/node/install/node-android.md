# Running an Ergo Node on Android

## Getting Started

Operating an Ergo full node on an Android device offers several intriguing benefits. For instance, it allows individuals without access to a desktop or laptop to sync the entire Ergo blockchain on their mobile device. This process also enables the use of personal nodes for applications such as the Ergo mobile wallet or the Ergo Mixer on mobile devices.

## Device Requirements

To run an Ergo node on an Android device, your device must meet the following minimum system requirements:

- Android OS version 7.0 or higher
- At least 25 GB of fast storage
- A minimum of 1GB of RAM available for apps (1GB is untested, but should work with some patience)

These requirements have been successfully tested on a Samsung Galaxy S8+.

## Preparation

To run an Ergo node on an Android device, you'll need a terminal emulator app. We've tested the Termux emulator app and found it suitable for this task. You'll first need to download and install [F-Droid](https://f-droid.org), a catalog of FOSS (Free and Open Source Software) applications for Android. Then, within F-Droid, search for `Termux - Terminal emulator with packages`, download and install it.

## Installing Packages in Termux

Launch Termux and update and upgrade all packages. Use the default responses for all prompts during the upgrade.

```
pkg upgrade
```

Next, install the packages `wget` and `OpenJDK-17`. These are essential to download the .jar file from GitHub and run it.

```
pkg install wget openjdk-17
```

## Downloading the Ergo Client Release & Setting Up the Config File

Download the latest Ergo client release from Github using wget. You can find it [here](https://github.com/ergoplatform/ergo/releases). Ensure you copy the direct link to the file.

```
wget https://github.com/ergoplatform/ergo/releases/download/v5.0.4/ergo-5.0.4.jar
```

Create a config file named `ergo.conf` using nano.

```
nano ergo.conf
```

Paste the following text into nano, then press CTRL + O, ENTER to save, and CTRL + X to exit.

```
ergo {
   node {
       mining = false
   }
}
```

## Launching the Node For the First Time

Use the following command to run the node for the first time (replace "`<release>`" with the version of the node that you downloaded).

```
java -jar ergo-<release>.jar --mainnet -c ergo.conf
```
  
The node will now start synchronizing. To track progress, open a browser on your device and navigate to the Ergo Node panel at http://127.0.0.1:9053/panel.

For more details regarding node configuration, please refer to the [manual install](manual.md) guide. Note that setting up the API key and wallet is not required.

## Tips and Tricks

- Consider downloading a different keyboard for use in Termux. The stock Samsung keyboard might not work optimally. The Hacker's Keyboard, available in F-Droid, proved to be a solid alternative.
  
- If you wish for your node to be accessible, you will need to set up port forwarding on port 9030 for your Android device in your router settings.
  
- You might need to specify the Java heap space with the -Xmx flag depending on your device. On the Samsung S8+, a heap size of -Xmx1536M was optimal. The node start command with a heap size of 2Gb looks like this: 

```bash
java -Xmx2G  -jar ergo-<release>.jar --mainnet -c ergo.conf
```  

- If you use the Ergo Wallet App, you can replace the default node with [http://127.0.0.1:9053](http://127.0.0.1:9053), allowing you to use the node running on your Android device. 
  
- The package 'tmux' is useful if you want to run other programs alongside the node within Termux.
