# Fork Your Own Ergo Chain

### Configuration

To start your custom Ergo chain, you need to modify the configuration to ensure it doesn't clash with the Ergo mainnet or public testnet. The key changes involve setting a unique `addressPrefix` and custom `magicBytes`.

Here’s an updated configuration for your `testnet.conf` file:

```conf
ergo {
  networkType = "testnet"

  node {
    mining = true
    offlineGeneration = true
    useExternalMiner = false
  }

  chain {
    addressPrefix = 32 #  to avoid address clashing with Ergo mainnet and public testnet
  }
}

scorex {
  network {
    magicBytes = [2, 0, 4, 8] # custom value to avoid connections with other networks
    bindAddress = "0.0.0.0:9022"
    nodeName = "ergo-testnet-5"
    #knownPeers = []
  }

  restApi {
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}
```

### Steps to Run the Node

1. **Set Up the Configuration:**

    - Make sure your `testnet.conf` file is configured as shown above. This will help prevent address clashes with the mainnet and public testnet by using a custom `addressPrefix` and `magicBytes`.

2. **Compile the Node:**

    - Use the following command to compile the Ergo node:
      ```shell
      sbt assembly
      ```
    - This will generate an `ergo.jar` file at `/target/scala*/ergo-*.jar`.

3. **Run the Node:**

    - Start the node using the command:
      ```bash
      java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
      ```

4. **Initialize and Unlock the Wallet:**

    - Access the panel at `127.0.0.1:9052/panel` to initialize and unlock your wallet. This is necessary as the first blocks will be generated using Autolykos v1.

### Additional Support

For deeper modifications or any questions, you can join the community on:

- **Telegram:** [Ergo Developers Chat](https://t.me/ErgoDevelopers)
- **Discord:** [Ergo Platform Developers Channel](https://discord.gg/ergo-platform-668903786361651200)

This setup ensures your custom chain runs independently and avoids conflicts with existing networks.