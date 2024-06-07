# Ergo Full Node Installation Guide

## Getting Started

### Preparing Your Environment

1. **Create a Folder**: Start by creating a folder where you will keep all files related to your Ergo node. A good example is creating a folder named `ergo` in your home directory.

2. **Download or Build the Ergo Client**:
   - **Download**: Visit the [Ergo GitHub releases page](https://github.com/ergoplatform/ergo/releases/) and download the latest `.jar` file.
   - **Build from Source**: If you prefer, you can clone the Ergo repository and compile the `.jar` file yourself using [SBT](https://www.scala-sbt.org/) by running `sbt assembly`. Alternatively, you can set up using Docker by following the guide in [Docker setup](docker.md).

### Setting Up Your Node

1. **Create a Configuration File**: In the `ergo` folder, create a text file named `ergo.conf`. This file will contain settings for your node. Only override the default values if necessary.

    /// details | ergo.conf
        {type: note, open: false}
    You can rename `ergo.conf` to any name you prefer. This file should include any settings you want to change from their default values.
    ///

    Start with this basic configuration:
    ```bash
    ergo {
        node {
            mining = false
        }
    }
    scorex {
        restApi {
            apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
        }
    }
    ```

2. **Launch Your Node**: Open a command line in your `ergo` folder and run the following command:
    ```bash
    java -jar -Xmx4G ergo-*.jar --mainnet -c ergo.conf
    ```

    /// details | -Xmx Flag
        {type: tip, open: false}
    The `-Xmx4G` command sets the maximum amount of memory the node can use to 4 GB. Adjust this value based on your computer's available memory.
    ///
    
3. **Wait for Initialization**: Once you run the command, your node will start syncing with the Ergo network. This process can take some time, so patience is key.

## Verifying Node Synchronization

1. **Monitor Synchronization**: Go to `127.0.0.1:9053/panel` in your web browser to see if your node is actively syncing. It should say "Active synchronization."

2. **Check Sync Status**: Once synchronization is complete, the panel will indicate "Node is synced." You can also check `127.0.0.1:9053/info` to compare the block height with what is reported on [Ergo Explorer](https://explorer.ergoplatform.com/en/).

## Additional Resources

- [Troubleshooting Guide](troubleshooting.md)
- [Frequently Asked Questions (FAQ)](node-faq.md)
- [Using the TestNet Tutorial](testnet.md)

