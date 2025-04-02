---
tags:
  - Node
  - Installation
  - Manual Setup
  - Full Node
  - Guide
---

# Ergo Full Node Installation Guide

## Getting Started

### Preparing Your Environment

1. **Create a Folder**: Start by creating a folder where you will keep all files related to your Ergo node. A good example is creating a folder named `ergo` in your home directory.

2. **Download or Build the Ergo Client**:
   - **Download**: Visit the [Ergo GitHub releases page](https://github.com/ergoplatform/ergo/releases/) and download the latest stable `.jar` file. This is the recommended method for most users.
   - **Build from Source**: If you need a specific version (e.g., a release candidate) or want to contribute to development, you can build the node from source:
      1. **Prerequisites**: Ensure you have [Git](https://git-scm.com/downloads) and a compatible Java Development Kit (JDK >= 9, check Ergo repository README for specific version recommendations) and [SBT](https://www.scala-sbt.org/download.html) installed.
      2. **Clone Repository**: `git clone https://github.com/ergoplatform/ergo.git`
      3. **Navigate to Directory**: `cd ergo`
      4. **Checkout Specific Version (Optional)**:
         * To build the latest development code, stay on the default branch (`master`).
         * To build a specific release or release candidate (RC), check out the corresponding tag: `git checkout v5.0.10` or `git checkout v6.0.0-RC2` (Replace tag name as needed. Find tags on the [releases page](https://github.com/ergoplatform/ergo/releases/)).
      5. **Handle SNAPSHOT Dependencies (If Applicable)**: Some development versions or RCs might depend on unreleased SNAPSHOT versions of libraries (like `scorex-util` or `sigmastate-interpreter`). If the build fails due to missing SNAPSHOT dependencies, you may need to clone those respective repositories, check out the correct branches/tags, and publish them locally first using `sbt publishLocal`. Consult the Ergo repository's README or developer channels for specific instructions if you encounter this.
      6. **Compile the JAR**: Run `sbt assembly`. This command compiles the code and packages it into a single executable `.jar` file located in the `target/scala-*/` directory (e.g., `target/scala-2.13/ergo-*.jar`).
      7. **Alternative (Docker)**: You can also build and run using Docker, see the [Docker setup guide](docker.md).

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
