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

## API Performance Issues

### Timeouts or Unresponsiveness Under Load

**Symptoms:**

*   API requests (e.g., from your wallet, dApp backend, or scripts) take a very long time to respond or fail with timeout errors.
*   The node's web panel (`/panel`) might become slow or unresponsive.
*   This often occurs when the node is handling multiple concurrent API requests or processing large amounts of data.

**Potential Causes & Solutions:**

1.  **Insufficient JVM Memory:** The Java Virtual Machine (JVM) running the node might not have enough allocated memory (heap space) to handle the load efficiently, leading to excessive garbage collection pauses or out-of-memory situations.
    *   **Check:** Monitor the node's memory usage using system tools (like `htop`, Task Manager) or JVM monitoring tools if available. Look for high memory usage approaching the allocated limit.
    *   **Solution:** Increase the maximum heap size allocated to the JVM using the `-Xmx` flag in your node startup command. For example, if you are running with `-Xmx4G`, try increasing it to `-Xmx6G` or `-Xmx8G` (ensure your system has enough physical RAM).
        ```bash
        # Example startup command with increased memory:
        java -jar -Xmx6G ergo-*.jar --mainnet -c ergo.conf
        ```
    *   Restart the node after changing the `-Xmx` value.

2.  **High System Load:** The server running the node might be overloaded due to other processes consuming CPU, RAM, or disk I/O. Check overall system resource usage.

3.  **Node Mode Limitations:** Certain node modes (like Digest mode) might have inherent limitations in handling specific API queries that require scanning the full UTXO set, potentially leading to slower responses for those queries. Refer to the [Node Modes](modes.md) documentation.

4.  **Network Latency:** Slow network connections between your client application and the node can also contribute to perceived timeouts.

5.  **Specific API Endpoint Issues:** Occasionally, a specific API endpoint might have a bug or inefficiency causing performance problems. Check the [Ergo Node GitHub Issues](https://github.com/ergoplatform/ergo/issues) for reports related to the endpoint you're using.

## Wallet Issues

### Correct Address/Balance Not Displayed

If your correct address or balance isn't displayed, follow these steps:

1. Make sure the wallet is synchronised.
2. Try to derive new addresses as per the [swagger](swagger.md) instructions.
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

## Issues with Public Nodes & Explorers

While running your own node provides the most control and trust, many users rely on public infrastructure (nodes and explorers) for convenience or when running a personal node isn't feasible.

**Known Public Resources (Community-Run, Status May Vary):**

*   **Node Lists:**
    *   [ergonodes.net](https://ergonodes.net/list): Provides a list of public nodes with basic status monitoring.
*   **Explorers (Often provide public API access):**
    *   [explorer.ergoplatform.com](https://explorer.ergoplatform.com/en/) (Official)
    *   [ergexplorer.com](https://ergexplorer.com/)
    *   [sigmaspace.io](https://sigmaspace.io/)
    *   [ergobackup.aap.cornell.edu](https://ergobackup.aap.cornell.edu/) (May primarily be a backup service, check API availability)
*   *(Note: This list is not exhaustive and uptime/reliability are not guaranteed. Always verify the trustworthiness and status of a public service before relying on it for critical operations.)*

**Troubleshooting Public Infrastructure Issues:**

If you encounter problems with a public node or explorer (e.g., incorrect data, API timeouts, connectivity problems, website errors):

1.  **Try Alternatives:** The simplest first step is to switch your wallet or application to use a different public node/explorer from the lists above or other known community resources. The issue might be specific to the service you were initially using.
2.  **Check Service Status:**
    *   For nodes listed on [ergonodes.net](https://ergonodes.net/list), check their reported status (height, sync status).
    *   Check the explorer website itself for any status banners or announcements.
    *   Look in community channels (Discord, Telegram) for recent reports about the specific service.
3.  **Identify the Operator (If Possible):** Some public services are run by known community projects or individuals. If you can identify the operator, check their specific project channels (Discord, Telegram, GitHub) for status updates or to report issues.
4.  **Report in General Community Channels:** If the operator is unknown or the issue seems widespread, report the problem in general Ergo community support channels (like the [#node](https://discord.gg/jjRP2uNAv5) or relevant dApp/wallet channels on Discord). Provide clear details:
    *   The IP address or URL of the public node/explorer.
    *   The specific issue encountered (e.g., "API endpoint X returning 500 error", "Explorer website not loading", "Node Y on ergonodes.net stuck at height Z", "Incorrect balance reported via API").
    *   The time the issue occurred.
    *   Any relevant transaction IDs, addresses, or API queries if applicable.
    *   Screenshots if helpful.
5.  **Check GitHub Repositories:** If the public node is part of a known open-source project (e.g., an explorer), check that project's GitHub repository issues section to see if the problem has already been reported or to file a new issue.
6.  **Understand Limitations:** Public infrastructure consists of shared resources. Operators may perform maintenance, experience downtime, have performance limits (e.g., unofficial API rate limits), or encounter occasional indexing issues (especially nodes using the `extraIndex` feature). For time-sensitive or critical applications, running your own node remains the most reliable option.
