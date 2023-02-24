---
tags:
  - NIPoPoWs
---

# Light-SPV Mode

## Overview 


[Simplified Payment Verification (SPV)](spv.md) allows for a simplified way of verifying transactions by only downloading and verifying the block headers, rather than the entire blockchain. This makes it possible for users with limited resources to participate in the network and make transactions without needing a full node.

## Ergo's NIPoPoWs

While SPV wallets are already very lightweight compared to full nodes, NIPoPoW-empowered SPV wallets need to download only a tiny sample of block headers, around 250, while other SPV clients need may to download around half a million block headers. The sample needed changes but does not grow much in size as the blockchain grows more extensive, even after accumulated decades of data.


A highly efficient Ergo wallet with SPV security is currently in development. Keep an eye out for updates [here](https://github.com/ergoplatform/sigma-rust/milestone/17).




## Technical Workflow

### Bootstrap

1.  Send **`GetPoPoWProof`** for all connections.
2.  On receiving **`PoPoWProof`**, apply it to History (History should determine whether this PoPoWProof is better than its current best header chain).
3.  **`GOTO`** regular regime.

### Regular

1.  Send ErgoSyncInfo message to connected peers
2.  Get a response with an INV message containing the ids of blocks, better than
    our best block.
3.  Request headers for all ids from 2.
4.  On receiving Header:

```java
    if(History.apply(header).isSuccess) {
        State.apply(header) // just change state roothash
    if(!isInitialBootstrapping) Broadcast INV for this header
    } else {
        blacklist peer
    }
```

