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


## Troubleshooting

### Stuck on 'Active Syncronisation' 

If your node is stuck on Active Syncronisation with no noticable increase in the height, please attempt the following steps.

1. Grep your log file using the commands from [here](/commands) to see if there's anything noticably wrong.
2. Shut down your instance, take a backup and attempt to restart.
3. Join the [#node](https://discord.gg/jjRP2uNAv5) channel on Discord for support or open an issue on GitHub.

### Displays as 'Syncronised' even though it isn't.

If your node is displaying as syncronised even though the height does not match the latest one found on [the explorer](https://explorer.ergoplatform.com/). 


### Is there anyway to revert without resyncing?

The node will attempt to do this itself, but if it fails - there is no way to manually rollback. 

### My correct address/balance is not displayed

1. Ensure wallet is syncronised.
2. Attempt to derive new addresses as per the [swagger](/node/swagger) instructions.
3. Ensure you derived the additional addresses during sync.
4. Restore on an alternative wallet. 

### Searching the logs
Here's some useful log greps

```bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
tail -Fn+0 ergo.log | grep 'ERROR'
tail -Fn+0 ergo.log | grep "not modified"
tail -Fn+0 ergo.log | grep ERR
tail -Fn+0 ergo.log | grep xception
tail -Fn+0 ergo.log | grep "akka.log-dead-letters"
tail -Fn+0 ergo.log | grep "stuck"
cat ergo.log | grep -A 30 -B 30 "Invalid z bytes"
```