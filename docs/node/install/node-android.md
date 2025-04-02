---
tags:
  - Android
  - Node
---
# Running an Ergo Node on Android

/// details | One click setup 
    {type: tip, open: true}

[ErgoNodeAndroid](https://github.com/rustinmyeye/ErgoNodeAndroid) is an attempt at a one-click Ergo node app for Android. This app is based on NeoTerm, and runs automated install scripts to set up and run an Ergo node on Android.

The current version of this app sets up a stateless light node.

///

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

Download the latest Ergo client release from Github using wget. You can find it [here](https://github.com/ergoplatform/ergo/releases), or use the following command to grab the latest release.

```
wget -qO- "https://api.github.com/repos/ergoplatform/ergo/releases/latest" | grep -o 'https://github.com/ergoplatform/ergo/releases/download/.*ergo-[0-9.]*\.jar' | wget -q --show-progress -i- -O ergo.jar

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

Use the following command to run the node for the first time.

```
java -jar ergo.jar --mainnet -c ergo.conf
```
  
The node will now start synchronizing. To track progress, open a browser on your device and navigate to the Ergo Node panel at [http://127.0.0.1:9053/panel](http://127.0.0.1:9053/panel).

For more details regarding node configuration, please refer to the [manual install](manual.md) guide. Note that setting up the API key and wallet is not required.

## Tips and Tricks

- Consider downloading a different keyboard for use in Termux. The stock Samsung keyboard might not work optimally. The Hacker's Keyboard, available in F-Droid, proved to be a solid alternative.
  
- If you wish for your node to be accessible, you will need to set up port forwarding on port 9030 for your Android device in your router settings.
  
- **Memory Allocation**: You will likely need to specify the Java heap space using the `-Xmx` flag, especially on devices with limited RAM. Start with `-Xmx1G` or `-Xmx1536M` and adjust based on your device's performance. The node start command with a heap size of 2Gb looks like this: 

```bash
java -Xmx2G  -jar ergo.jar --mainnet -c ergo.conf
```  
  
- If you use the Ergo Wallet App, you can replace the default node with `http://127.0.0.1:9053`, allowing you to use the node running on your Android device. 
  
- The package `tmux` is useful and recommended if you'd like to run the node in the background. 

## Advanced Setup for RocksDB Compatibility (glibc vs musl libc)

**Issue:** Some Ergo node versions or configurations rely on the RocksDB database engine. RocksDB's pre-compiled Java bindings (JARs) often expect the standard GNU C Library (`glibc`). However, Android and environments like Termux typically use a different C library, `musl libc` (via `Bionic`). This incompatibility can prevent the node from starting if it requires RocksDB (e.g., for certain state types or potentially older versions).

**Workaround (Termux + proot + Arch Linux):** A community-discovered workaround involves using `proot` within Termux to run an Arch Linux environment, which *does* use `glibc`. This allows the RocksDB bindings to function correctly.

**Disclaimer:** This is an advanced procedure and may introduce its own complexities or stability issues. Proceed with caution.

**Steps (High-Level Overview):**

1.  **Install `proot-distro` in Termux:**
    ```bash
    pkg install proot-distro
    ```
2.  **Install Arch Linux:**
    ```bash
    proot-distro install archlinux
    ```
3.  **Login to Arch Linux Environment:**
    ```bash
    proot-distro login archlinux
    ```
4.  **Inside Arch Linux:**
    *   Update package lists: `pacman -Syu`
    *   Install necessary dependencies (Java JDK, wget, etc.): `pacman -S jdk-openjdk wget ...` (Ensure you install a compatible JDK version).
    *   Download/copy the Ergo node `.jar` file and your `ergo.conf` into this Arch Linux environment (e.g., using shared storage access or `wget`).
    *   Run the Ergo node using the `java -jar ...` command as described earlier, but *within* the Arch Linux `proot` environment.

**Considerations:**

*   This adds overhead compared to running directly in Termux.
*   File system access between Termux and the `proot` environment needs careful handling.
*   Ensure the node configuration within the Arch environment points to the correct data directories.
*   This workaround is primarily needed if your specific node configuration requires RocksDB and encounters libc conflicts. Simpler configurations (like digest state without RocksDB) might run directly in Termux as described in the main guide.
