# Troubleshooting

Please open a [git issue](https://github.com/ergoplatform/ergo/issues/new/choose) with the following details

- Node version
- Java command used
- RAM/CPU
- Operating System
- JVM version
- Storage location (Cloud, SSD, etc)
- output of ERROR/WARN


```
tail -Fn+0 ergo.log | grep 'ERROR\|WARN' > output.log
```

## Sync

### Stuck on 'Active Syncronisation' 

If your node is stuck on Active Syncronisation with no noticeable increase in the height, please attempt the following steps.

1. Grep your log file using the commands from [here](/commands) to see if there's anything noticeably wrong.
2. Shut down your instance, take a backup and attempt to restart.
3. Join the [#node](https://discord.gg/jjRP2uNAv5) channel on Discord for support or open an issue on GitHub.

### Displays as 'Synchronised' even though it isn't.

If your node is displaying as synchronised even though the height does not match the latest one found on [the explorer](https://explorer.ergoplatform.com/) you can add this to your `.conf` file under `ergo { node {`

```conf
# A node is considering that the chain is synced if sees a block header with timestamp no more
# than headerChainDiff blocks on average from future
# 800 blocks ~= 1600 minutes (~1.1 days)
# headerChainDiff = 80
```

There is currently an open issue for a [header downloading problem during synchronization](https://github.com/ergoplatform/ergo/issues/1657)

### Lowering maxConnections

To allieviate some of the performance issues on later blocks please add the following to your `ergo.conf`

```bash
network {
        maxConnections = 10

          }
```

This will lower the default `maxConnections` from 30 to 10, the sync will be slower but require less resources and sync smoother.

### Is there any way to revert without resyncing?

The latest versions of the node will attempt to fix any errors itself, but if it fails - there is no way to manually roll-back. 

### Searching the logs

Here's some useful log greps

```bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
tail -Fn+0 ergo.log | grep 'ERROR'
tail -Fn+0 ergo.log | grep "not modified"
tail -Fn+0 ergo.log | grep ERR
tail -Fn+0 ergo.log | grep xception
tail -Fn+0 ergo.log | grep "stuck"
```

### How do I resync from scratch? 

To resync, remove the following two folders and restart the node. 

```
rm -rf .ergo/state
rm -rf .ergo/history
```

## Wallet

### My correct address/balance is not displayed

1. Ensure the wallet is synchronised.
2. Attempt to derive new addresses as per the [swagger](/node/swagger) instructions.
3. Ensure you derived the additional addresses during sync.
4. Restore on an alternative wallet if unsuccessful.  


## Error Messages

### Unable to define external address. 


```
WARN [tor.default-dispatcher-11] s.c.n.NetworkController - 
Unable to define external address.
Specify it manually in `scorex.network.declaredAddress`
```

This warning means you aren't running a public node and can be ignored.



###  Got GetReaders request in state None

> It is normal to recieve this in the first few minutes of starting the node.

This means that the database cannot be read. If this is happening continuously it likely indicates database corruption. This can happen due to unexpected shutdowns and also due to 

```
WARN  [ergoref-api-dispatcher-9] 
o.e.n.ErgoReadersHolder 
Got GetReaders request in state (None,None,None,None)
```

To resync, remove the following two folders and restart the node. 

```
rm -rf .ergo/state
rm -rf .ergo/history
```


### Invalid z bytes

It has to do with parsing `z` value for this constructor 
```
UncheckedSchnorr(dl, None, challenge, SecondDLogProverMessage(z))
```

```
cat ergo.log | grep -A 30 -B 30 "Invalid z bytes"
```

**ERROR**

```
02:17:49.838 WARN  [tor.default-dispatcher-11] sigmastate.SigSerializer$ - Invalid z bytes for ProveDlog((f40ee9cecf47e36a18645e5a3cff677772d74ee2792912173aa406fa9a8a2ef4,4d058f2cdd0711eea49a9f289c4643391639a2e323be900b0e2e06cb562c45ba,1)): 6a5f7e7ee68762b61a0e8b64e353f66d0be523b7bf8d56b662112ec47e32ec7183525c9851a608885a34051bc971d6c8600c88d8ce1713
```

### Dead Letters

```
tail -Fn+0 ergo.log | grep "akka.log-dead-letters"
```


In Akka, messages that can't be delivered are routed to a synthetic actor which has the path “/deadLetters”. This is for NON transport lost messages. Akka makes no guarantees for lost messages at the transport layer. Existence of dead letters does not necessarily indicate a problem, but they are logged by default for the sake of caution

```bash
10:37:47.229 INFO  [ctor.default-dispatcher-6] s.c.n.PeerConnectionHandler - Peer handler to ConnectionId(remote=/108.20.208.49:57345, local=/MY_IP:9030, direction=Incoming) destroyed
10:37:47.213 INFO  [tor.default-dispatcher-14] s.c.n.PeerConnectionHandler - Peer handler to ConnectionId(remote=/74.208.214.22:43520, local=/MY_IP:9030, direction=Incoming) destroyed
10:37:47.239 INFO  [Thread-0] org.ergoplatform.ErgoApp - Stopping network services
10:37:47.245 INFO  [Thread-0] org.ergoplatform.ErgoApp - Stopping actors (incl. block generator)
[INFO] [akkaDeadLetter][06/11/2021 10:37:47.246] [ergoref-akka.actor.default-dispatcher-7] [akka://ergoref/user/networkController] Message [scorex.core.network.NetworkController$ReceivableMessages$ShutdownNetwork$] to Actor[akka://ergoref/user/networkController#-2029702693] was not delivered. [4] dead letters encountered. If this is not an expected behavior then Actor[akka://ergoref/user/networkController#-2029702693] may have terminated unexpectedly. This logging can be turned off or adjusted with configuration settings 'akka.log-dead-letters' and 'akka.log-dead-letters-during-shutdown'.
```

### Failed to connect to localhost port 9053: Connection refused


netstat -ln | grep 9053
sudo netstat -tulpn


### Tree root should be real 

This it usually means that you trying to sign a box that you don't own (does not know the private key needed to sign).