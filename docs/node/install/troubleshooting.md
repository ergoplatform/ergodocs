#  Node Troubleshooting Guide

This document aims to help you troubleshoot common issues with the Ergo reference client. If you encounter a problem not covered here, please create a [new issue on GitHub](https://github.com/ergoplatform/ergo/issues/new/choose) and provide the following details:

- Node version
- Java command used
- RAM/CPU specification
- Operating System
- JVM version
- Storage location (Cloud, SSD, etc)
- output of ERROR/WARN

You can obtain the output of ERROR/WARN by executing the following command:

```bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN' > output.log
```

## Searching the Logs

The following commands can help you search your logs for specific entries:

```bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
tail -Fn+0 ergo.log | grep 'ERROR'
tail -Fn+0 ergo.log | grep "not modified"
tail -Fn+0 ergo.log | grep ERR
tail -Fn+0 ergo.log | grep xception
tail -Fn+0 ergo.log | grep "stuck"
```

## Synchronization Issues

There are common problems that may occur during synchronization.

### Stuck on 'Active Synchronization'

If your node is stuck on Active Synchronization without a noticeable increase in height, try the following steps:

1. Use the log commands from above to see if there is anything noticeably wrong.
2. Shut down your instance, take a backup, and try to restart.
3. Join the [#node](https://discord.gg/jjRP2uNAv5) channel on Discord for support or open an issue on GitHub.

### Node Appears 'Synchronised' Even When It Isn't

If your node appears synchronised even though the height doesn't match the latest one found on the [explorer](https://explorer.ergoplatform.com/), you can add this to your `.conf` file under `ergo { node {`:

```conf
# A node is considering that the chain is synced if sees a block header with timestamp no more
# than headerChainDiff blocks on average from future
# 800 blocks ~= 1600 minutes (~1.1 days)
# headerChainDiff = 80
```

You might also be experiencing a [header downloading problem during synchronization](https://github.com/ergoplatform/ergo/issues/1657).

### Lowering `maxConnections` 

To alleviate some performance issues on later blocks, you can lower the default `maxConnections` from 30 to 10 in your `ergo.conf`:

```bash
network {
    maxConnections = 10
}
```

This makes the sync process slower but it should run more smoothly.

### Reverting Without Resyncing

The latest versions of the node will attempt to fix any errors on their own, but if it fails, there is no way to manually roll back.

### Resyncing From Scratch

To resync, remove the following two directories and restart the node:

```bash
rm -rf .ergo/state
rm -rf .ergo/history
```

## Wallet Issues

### Correct Address/Balance Not Displayed

If your correct address or balance isn't displayed, follow these steps:

1. Make sure the wallet is synchronised.
2. Try to derive new addresses as per the [swagger](/node/swagger) instructions.
3. Ensure you derived additional addresses during the sync process.
4. If the problem persists, restore the wallet on a different client.

## Common Error Messages

### 'Unable to Define External Address'

If you see this warning:

```
WARN [tor.default-dispatcher-11] s.c.n.NetworkController - 
Unable to define external address.
Specify it manually in `scorex.network.declaredAddress`
```

it means you aren't running a public node. You can ignore this warning.

### 'Got GetReaders Request in State None'

This error message is normal in the first few minutes of starting the node:

```
WARN  [ergoref-api-dispatcher-9] 
o.e.n.ErgoReadersHolder 
Got GetReaders request in state (None,None,None,None)
```

If you continue to receive this message, it likely indicates database corruption, which can be caused by unexpected shutdowns. To resync, remove the directories `.ergo/state` and `.ergo/history`, then restart the node.

### 'Invalid Z Bytes'

This error is related to parsing the `z` value for this constructor: `UncheckedSchnorr(dl, None, challenge, SecondDLogProverMessage(z))`.

To view the log entries surrounding this error, use the following command:

```bash
cat ergo.log | grep -A 30 -B 30 "Invalid z bytes"
```

### 'Dead Letters'

In Akka, messages that cannot be delivered are routed to an actor with the path `/deadLetters`. Dead letters do not necessarily indicate a problem but are logged by default for caution.

To search for these messages, use the following command:

```bash
tail -Fn+0 ergo.log | grep "akka.log-dead-letters"
```

### 'Failed to Connect to localhost Port 9053: Connection Refused'

You can use these commands to troubleshoot:

```bash
netstat -ln | grep 9053
sudo netstat -tulpn
```

### 'Tree Root Should Be Real'

This error typically means you're trying to sign a box that you don't own (i.e., you don't have the private key needed to sign).