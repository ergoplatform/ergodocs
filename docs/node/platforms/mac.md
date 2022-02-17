# Mac



## Getting Started

### Prerequisites 

To run an Ergo node you need Java installed on your system. 

The most painless way to do this is with [SDKMAN](https://sdkman.io/install).

```
curl -s "https://get.sdkman.io" | bash
# We recommend either version 9 or 11. 
sdk install java 11.0.13.8.1-amzn
```

### Setup Script

This script will:

1. Download the latest version of the node in a folder called `ergo` in the current directory.
2. Prompt you to set an API password.
3. Computes the hash of that password and relaunches the node. 

You can then view the status by tracking the `height`, `headersHeight` and monitoring the `.log` files. 

```
bash -c "$(curl -s https://n.phenotype.dev)"
```

### Shutdown 

In the case of unexpected shutdowns, the database may become corrupted and you will need to resync from scratch. 

To safely shut down the node, use the following command

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

To relaunch the node

```bash
java -jar -Xmx3G -Dlogback.stdout.level=WARN -Dlogback.file.level=ERR ergo.jar --mainnet -c ergo.conf
```

Please see the [troubleshooting page](/docs/node/troubleshooting) for more information. 


### Wallet

If you'd like to initialise a wallet place see [this page](/node/wallet)

## One-Liner (Experimental)

Tested on M1, also runs the command and tracks the progress for you on the CLI. 

```
bash -c "$(curl -s https://node-gui.phenotype.dev)"
```

*The source code is available on [GitHub](https://github.com/glasgowm148/ergoscripts).*
