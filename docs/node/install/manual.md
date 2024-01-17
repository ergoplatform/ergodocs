# Ergo Full Node Manual Installation

## Initial Setup

### Download the Ergo Client

Initiate the process by establishing a designated folder (e.g., `~/ergo`) for the node operation and download the latest [Ergo client release](https://github.com/ergoplatform/ergo/releases/) `.jar` file. Alternatively, clone the Ergo repository and compile the `.jar` file from the source using [SBT](https://www.scala-sbt.org/) (`sbt assembly` command), or via [Docker](/node/install/docker).

### Create a configuration file

/// details | ergo.conf
    {type: note, open: false}
The filename `ergo.conf` can be modified as desired. This file is a repository for all configuration parameters, and only parameters differing from the default values need to be overwritten.
///


Subsequently, create an `ergo.conf` configuration file in the same directory as the `.jar` file, containing the following:

```bash
ergo {
    node {
        mining = false
    }
}
```

Launch the node with the command:

```bash
java -jar -Xmx4G ergo-*.jar --mainnet -c ergo.conf
```

See [this page](node-faq.md#java) for getting setup with java.


/// details | -Xmx Flag
    {type: tip, open: false}

* The `-Xmx4G` flag determines the JVM's max heap size; recommended setting is `4-6G` based on available memory. 
* During the initial syncing process, allocate more memory using `-Xmx4g`. Upon completion of the syncing process, reduce this to `-Xmx1g`.
///
Following the execution of this command, the node will commence syncing. Wait for the API initialization before proceeding to the next step.


---

## API Security

### Generate Secret Password

To secure the API, set a unique and robust secret password (avoid using the demonstration secret `hello`).

### Compute Secret's Hash

Use the API at [127.0.0.1:9053/swagger#/utils/hashBlake2b](http://127.0.0.1:9053/swagger#/utils/hashBlake2b) to compute your secret's `Blake2b` hash.

> **Note:** Ensure the `.jar` file is actively running to access the API at `127.0.0.1`, which denotes your local machine.

![Compute Hash of secret](https://user-images.githubusercontent.com/23208922/69916676-ed233400-1483-11ea-8582-f61c38478d31.png)

### Update Configuration File

After obtaining the hash response, input it into the `ergo.conf` file. For instance, the `Blake2b` hash of `hello` is `324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf`.

![response](https://user-images.githubusercontent.com/23208922/69916509-c3690d80-1481-11ea-869f-630cd59cc525.png)

Update the configuration file with the API key hash:

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

Restart the node to initiate syncing and enable API access.

---

## Node Synchronization Verification

During synchronization, the panel displays "Active synchronization".

![active synchronization](https://user-images.githubusercontent.com/23208922/71128146-94d58b80-2212-11ea-9010-5b61a91e8549.png)

Upon completion of synchronization, the panel updates to "Node is synced".

![synced](https://user-images.githubusercontent.com/23208922/71301767-8da4ae00-23c9-11ea-8fc0-a92a9d78b821.png)

Additional verification can be performed at [127.0.0.1:9053/info](http://127.0.0.1:9053/info) by comparing the block height to the latest block height at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/en/).

---



## Resources

* [Troubleshooting Guide](troubleshooting.md)
* [Frequently Asked Questions (FAQ)](node-faq.md)
* [Using the TestNet Tutorial](testnet.md)