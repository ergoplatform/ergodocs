
# Light SPV Mode Technical Workflow

The technical workflow for the light-SPV mode in Ergo is as follows:

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
