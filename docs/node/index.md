The Ergo Node is part of Ergo's peer-to-peer network which hosts and synchronises a copy of the entire Ergo blockchain. 

## Getting Started

To set up a node please select the intended platform. 

- [Mac](/node/platforms/mac)
- [Linux](/node/platforms/linux)
- [Pi](/node/platforms/pi)
- [Windows](/node/platforms/windows)
- [Docker](/node/platforms/docker)

Supporting pages

- [Troubleshooting](/node/platforms/troubleshooting)
- [Tutorial](/node/platforms/tutorial)
- [FAQ](/node/#faq)
- [Using the TestNet](/dev/start/testnet)


## API

- [API Docs](https://api.ergoplatform.com/api/v1/docs/)
- [Node API](https://git.io/fjqwb)
- [Explorer API](https://git.io/fjqwN)


## FAQ

### Is there any benefits for running a node?

There is no financial incentive to run a node, doing so helps increase the security of the network.


### Are nodes visible anywhere?

Public nodes can be seen on [nodespyder](https://ergo.nodespyder.io/). Please note that unless you are running the node on a publicly accessible web-server, your node should be protected by your router. 


- To run a public node see this example [nginx.conf](https://github.com/glasgowm148/ergoscripts/blob/main/misc/nginx.config) available.  
- Using a [remote node](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/mainnet.conf) is insecure, please use them with caution.


### Node security

Unless you are running the node on a publicly accessible web-server, your node should be protected by your router. 

If you wish to host a public node, there are a few important aspects your wallet and money's safety depends on:

* You should never make the `ergo.conf` file public.
* Sensitive API methods require a security token, which should never be sent over untrusted channels.
* Access to the Ergo REST API must be restricted to known hosts. In particular, the API must not be accessible from the Internet.



### How do I safely shut down?

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

### Compiling from source

Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using the [`sbt assembly`](https://www.scala-sbt.org/)  command.

