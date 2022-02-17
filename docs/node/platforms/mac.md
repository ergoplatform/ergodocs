# Mac



## Getting Started

To run an Ergo node you need Java installed on your system. 

```
curl -s "https://get.sdkman.io" | bash
# We recommend either version 9 or 11. 
sdk install java 11.0.13.8.1-amzn
```

Then run the following script to download the node and setup your `API` password

```
bash -c "$(curl -s https://n.phenotype.dev)"
```

You can track the status of the sync by comparing the heights found in [127.0.0.1:9053/info](http://127.0.0.1:9053/info) to the the ones on the [explorer](https://explorer.ergoplatform.com/en/).


Please see the [troubleshooting page](/node/platforms/troubleshooting) for more information. 

## One-Liner (Experimental)

Tested on M1, also runs the command and tracks the progress for you on the CLI. 

```
bash -c "$(curl -s https://node-gui.phenotype.dev)"
```

*The source code is available on [GitHub](https://github.com/glasgowm148/ergoscripts).*
