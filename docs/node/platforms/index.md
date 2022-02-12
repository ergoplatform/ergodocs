# Getting Started

## Platforms

To set up a node please select the intended platform. 

- [Mac](/node/platforms/mac)
- [Linux](/node/platforms/linux)
- [Pi](/node/platforms/pi)
- [Windows](/node/platforms/windows)
- [Docker](/node/platforms/docker)


## FAQ

### How do I safely shut down?

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

### Node security

Unless you are running the node on a publicly accessible web-server, your node should be protected by your router. 

If you wish to host a public node, there are a few important aspects your wallet and money's safety depends on:

* You should never make the `ergo.conf` file public.
* Sensitive API methods require a security token, which should never be sent over untrusted channels.
* Access to the Ergo REST API must be restricted to known hosts. In particular, the API must not be accessible from the Internet.

There is an [example nginx.conf](https://github.com/glasgowm148/ergoscripts/blob/main/misc/nginx.config) available.  


### Compiling from source

Note that instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from the source using the [`sbt assembly`](https://www.scala-sbt.org/)  command.


## Troubleshooting

### Stuck on 'Active Syncronisation' 

If your node is stuck on Active Syncronisation with no noticable increase in the height, please attempt the following steps.

1. Grep your log file using the commands from [here](/commands) to see if there's anything noticably wrong.
2. Shut down your instance, take a backup and attempt to restart.
3. Join the [#node]() channel for support or open an issue on GitHub.

### Displays as 'Syncronised' even though it isn't.

If your node is displaying as syncronised even though the height does not match the latest one found on [the explorer](https://explorer.ergoplatform.com/). 

### My correct address/balance is not displayed

1. Attempt to derive new addresses as per the [swagger](/node/swagger) instructions.