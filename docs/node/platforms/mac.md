# Mac

The following *one-liner* will:

1. set up an `/ergo` folder and download the latest `ergo.jar`
3. Prompt you to set an API key
4. Sets the API key, restarts and starts syncing.
5. Displays progress in CLI.

```
bash -c "$(curl -s https://node.phenotype.dev)"
```

*The source code is available on [GitHub](https://github.com/glasgowm148/ergoscripts). Tested on Intel/M1*


## Prerequisites 

To run an Ergo node you need a **JDK/JRE version >= 9** installed on your system. 

We recommend either version 9 or 11. 

One way to do this is to install [SDKMAN](https://sdkman.io/install)

```
curl -s "https://get.sdkman.io" | bash
sdk install java
```

You will then run the node, set an API key, restart and monitor the sync. 

If you'd prefer to get set up manually, here's a [step-by-step.](/node/platforms/tutorial)