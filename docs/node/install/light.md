# Light mode


It's possible to run the node in a *light mode* using the `stateType` variable. 

- `digest`
- `utxo`

Mainnet `ergo.conf` for a **light node** (no UTXO, checking and storing only last 2880 blocks) 

The `blocksToKeep` variable allows you to specify how many of the previous blocks you want to store. 

```
ergo {
  node {
    stateType = "digest"
    blocksToKeep = 2880
    mining = false
  }


}

scorex {

 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    apiKeyHash = "6ed54addddaf10fe8fcda330bd443a57914fbce38a9fa27248b07e361cc76a41"
  }
}
```