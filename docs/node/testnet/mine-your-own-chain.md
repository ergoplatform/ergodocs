# Fork your own chain!

### Generating `genesisStateDigestHex`

To mine your own chain, you need to generate the `genesisStateDigestHex`, which is a Base16 representation of the *genesis state* roothash. Follow these steps to configure your chain values in the [src/main/resources/testnet.conf](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/testnet.conf) file and compile the node to obtain the `genesisStateDigestHex`.

### Prerequisites

Before proceeding, ensure that you have sbt installed, which is a build tool for Scala. The easiest way to set up sbt is by using [SDKMAN](https://sdkman.io/).

```shell
curl -s "https://get.sdkman.io" | bash 
sdk install sbt
```

### Compiling the Node

To compile the node, run the following command:

```shell
sbt assembly
```

This command will create an `ergo.jar` file at `/target/scala*/ergo-*.jar`.

### Configuring Your `.conf` File

At this stage, your `testnet.conf` file should have the following configuration:

```shell
ergo {
  networkType = "testnet"

  node {
    mining = true
    offlineGeneration = true
    useExternalMiner = false
  }
  
  chain {
    genesisStateDigestHex = "Still to be generated at this stage"
  }
}

scorex {
  network {
    bindAddress = "0.0.0.0:9022"
    nodeName = "ergo-testnet-5"
    #knownPeers = []
  }

  restApi {
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}
```

### Running the Node

Use the following command to run the node:

```shell
java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
```

The console should display a new `genesisStateDigestHex` value. Copy that value and replace the placeholder text `"Still to be generated at this stage"` in the `testnet.conf` file. Remove the "#" characters to uncomment the lines.

Restart your node, and it will start CPU mining its own chain!