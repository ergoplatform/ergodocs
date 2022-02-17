
# FAQ

### How do I safely shut down?

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

### Is there any benefits for running a node?

There is no financial incentive to run a node, doing so helps increase the security of the network.

### Are nodes visible anywhere?

Only public nodes are, which can be seen on [nodespyder](https://ergo.nodespyder.io/). 

To run a public node There is an [example nginx.conf](https://github.com/glasgowm148/ergoscripts/blob/main/misc/nginx.config) available.  

### Node security

Unless you are running the node on a publicly accessible web-server, your node should be protected by your router. 

If you wish to host a public node, there are a few important aspects your wallet and money's safety depends on:

* You should never make the `ergo.conf` file public.
* Sensitive API methods require a security token, which should never be sent over untrusted channels.
* Access to the Ergo REST API must be restricted to known hosts. In particular, the API must not be accessible from the Internet.

### Compiling from source

Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using the [`sbt assembly`](https://www.scala-sbt.org/)  command.


