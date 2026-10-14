---
tags:
  - Node
  - Devnet
  - Configuration
  - Testing
owner: docs
last_reviewed: 2026-09-23
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/scala/org/ergoplatform/settings/NetworkType.scala
      - src/main/resources/devnet.conf
  - repo: arkadianet/ergo
    branch: main
    paths:
      - scripts/devnet-mixed/genesis.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/blob/master/src/main/scala/org/ergoplatform/settings/NetworkType.scala
  - https://github.com/arkadianet/ergo/blob/main/scripts/devnet-mixed/genesis.conf
---

# Fixed-Difficulty Devnet (devnet60)

A private network for multi-node tests: 6.0 launch parameters from the genesis block (the first mined header
is version 1, as the candidate generator makes it with no parent; 6.0 headers from block 2), difficulty pinned
at 1 so that every node (and a trivial external solver) produces blocks at once, and one chain identity that the Scala
node and the arkadianet Rust node share. Use it when you need several nodes on one machine to agree, disagree or resync
under conditions you control. For a single node with a wallet, [Fork Your Own Chain](mine-your-own-chain.md)
is simpler; for public compatibility testing, use [testnet](testnet.md).

## What devnet60 Is

`ergo.networkType = "devnet60"` selects a network type the node defines but ships no config file or CLI flag
for (`NetworkType.scala`: "used in tests only currently, devnet which is starting from 6.0 activated since
genesis block"; the node's tests reference it). It differs from [`devnet.conf`](devnetconf.md) (`networkType = "devnet"`, 5.0 rules from
genesis, difficulty adjusting every 16 blocks, 100 ms blocks) in three ways that matter for multi-node work:

| | `devnet` (`devnet.conf`) | `devnet60` (this page) |
|---|---|---|
| Launch parameters | block version 3 (5.0 rules) | block version 4 (6.0 rules); the sub-blocks parameter is added only at a voting-epoch start, which never comes on this devnet |
| Difficulty | starts at 1, adjusts every 16 blocks | pinned at 1: the epoch is 2^25 blocks, longer than any test chain |
| Block interval | 100 ms | 20 s (block production is set by the miner's polling interval, below) |
| Shared with | Scala node only | Scala node and `arkadianet/ergo` (`network = "devnet"`) |

Because the difficulty never moves, a block is valid with any nonce, which is what lets a Rust node without an
internal miner mine through its `/mining` endpoints with a fixed solution, and what makes runs repeatable.

## Configuration

Save as `devnet60.conf`. The `chain` section fixes the chain identity (several of its values already match
`application.conf` defaults and are stated for completeness); `node`, `wallet` and `scorex` are one node's
local settings.

```conf
ergo {
  networkType = "devnet60"

  chain {
    protocolVersion = 4
    addressPrefix = 16
    initialDifficultyHex = "01"
    epochLength = 33554432          # 2^25: difficulty is never recalculated
    blockInterval = 20s
    # Root hash of the genesis UTXO state. It depends on the genesis boxes (the emission box script
    # embeds monetary.minerRewardDelay): change the monetary settings, and derive it again (see below).
    genesisStateDigestHex = "cb63aa99a3060f341781d8662b58bf18b9ad258db4fe88d09f8f71cb668cad4502"
    monetary.minerRewardDelay = 720
    voting {
      votingLength = 33554432
      softForkEpochs = 32
      activationEpochs = 32
      version2ActivationHeight = 2147483647   # the historical v2 hard fork never fires, as on testnet
      version2ActivationDifficultyHex = "20"
    }
    reemission {
      checkReemissionRules = false
      activationHeight = 100000001
    }
  }

  node {
    stateType = "utxo"
    verifyTransactions = true
    blocksToKeep = -1
    mining = true                       # the miner; set false on followers
    offlineGeneration = true            # mine with no peers (the first node has none)
    useExternalMiner = false
    internalMinerPollingInterval = 2s   # about one block per poll at difficulty 1: this sets the block rate
  }

  wallet {
    # The node's public test mnemonic (application.conf): gives the internal miner a key without a wallet
    # initialised through the API. Any funds on this chain are worthless; never use it elsewhere.
    testMnemonic = "ozone drill grab fiber curtain grace pudding thank cruise elder eight picnic"
    testKeysQty = 5
  }
}

scorex {
  network {
    magicBytes = [7, 7, 7, 7]           # the magic arkadianet's devnet uses; a second network on the same host takes another value on all its nodes
    bindAddress = "0.0.0.0:9030"
    # no declaredAddress on a loopback setup (see "A Second Node")
    nodeName = "devnet60-A"
    knownPeers = []                     # followers: ["127.0.0.1:9030"]
    allowLocal = true                   # required on a node that dials 127.0.0.1 (knownPeers); inbound loopback is accepted regardless
  }
  restApi {
    bindAddress = "127.0.0.1:9052"
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"   # hash of "hello"; change it
  }
}
```

Create the data directory first (`mkdir -p` the `ergo.directory` you set; the node refuses one that does not
exist), then run it with the config path and **no network flag**: `--devnet` pulls `devnet.conf` in as a
fallback and then aborts, because the flag's network type must equal the file's, and there is no `--devnet60`.

```bash
java -Xmx1g -jar ergo-6.0.6.jar -c devnet60.conf
```

The log says `Running without network config`; that is expected, the file carries the whole identity. Blocks
appear at the polling interval: `curl -s 127.0.0.1:9052/info | jq .fullHeight`.

## A Second Node

Copy the file, change the `bindAddress` and `restApi.bindAddress` ports and `nodeName`, set `mining = false`,
`offlineGeneration = false`, `knownPeers = ["127.0.0.1:9030"]`, keep `allowLocal = true` (this node is the one
dialling a loopback address), and give it its own `ergo.directory` (created first). Leave `declaredAddress`
unset on every node: a node whose declared IP equals a peer's declared IP assumes a shared NAT, asks a UPnP
gateway for the peer's LAN address, and without a gateway never dials that peer, with nothing in the log. It connects, downloads headers and blocks, and reports the same `stateRoot` as the first node
at the same `fullHeight` once the first node stops mining (set `mining = false` and restart it; the nodes reconnect
within a few seconds, the restarted miner dialling the follower from its peer database). Each node lists the other in `/peers/connected` by name; the `address` field is
empty for a peer that declares no address.

A node with another `magicBytes` completes the handshake, is dropped at once (the handshake's session feature
carries the magic) and is removed from the peer database on both sides; nothing is blacklisted and other peers
are unaffected. A node whose only known peer had the wrong magic therefore stops dialling until it is restarted
with a corrected `knownPeers` or `magicBytes`. Two magics can share one host.

## The Genesis Digest

`genesisStateDigestHex` is the root hash of the genesis UTXO set: the emission box (whose script embeds
`monetary.minerRewardDelay` and the emission schedule), the no-premine box and the foundation box. A UTXO node
computes it at first start, logs `Genesis UTXO state generated with hex digest <value>`, and, if the configured
value differs, fails an assertion: the node view holder never starts, the REST API reports no height, and the
process has to be stopped by hand (a digest-mode node trusts the configured value).
To derive it for other monetary settings: start once with any value, read that log line, put the value in the
file and start again. The value above is the one for `minerRewardDelay = 720` (it is also `devnet.conf`'s and
`testnet.conf`'s, which share these genesis boxes).

## The arkadianet Rust Node on the Same Chain

[arkadianet/ergo](rust-node.md) v0.8.0 and later: `network = "devnet"` selects the same parameters (its
`scripts/devnet-mixed/genesis.conf` is the Scala side of this page, and its `rust-node.toml` the Rust side);
`[peers] known = ["127.0.0.1:9030"]`, `allow_local = true`. It has no internal miner: it follows, or, with
`[mining] enabled = true` (otherwise the routes are not mounted), mines through `GET /mining/candidate` and
`POST /mining/solution` with any nonce.

## Operator Notes

- `addressPrefix = 16` (testnet's) keeps addresses distinct from mainnet.
- `internalMinerPollingInterval` is the throttle. At difficulty 1 the miner solves on the first attempt, so
  the interval, not `blockInterval`, sets how fast the chain grows. 500 ms is fine for one miner; with several
  miners on one machine, 1 s or more avoids constant sibling forks.
- The wallet section above is for the miner only. Followers need no wallet.
- `ergo.directory` defaults to `.ergo` under the working directory (or `$DATADIR`); give each node its own, and create it before the first start.
