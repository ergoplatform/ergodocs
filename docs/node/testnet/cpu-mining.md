# CPU Mining

/// admonition | Warning!
    type: warning
Please do not GPU mine the testnet! It prevents CPU miners from winning any blocks and then leaves a high difficulty when you stop.
///

## Getting Set-up
> Please refer to [node](install.md) for basic node set-up up to this point.

To CPU mine on the testnet, your `testnet.conf` should look like this. 

```conf
  ergo {
    networkType = "testnet"

    node {
      mining = true
      useExternalMiner = false
    }
  }

  scorex {

  network {
      bindAddress = "0.0.0.0:9022"
      nodeName = "ergo-testnet"
      #knownPeers = []
    }

  restApi {
      # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
      # Below is hash corresponding to API_KEY = "hello" (with no quotes)
      apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
    }
  }
```

Then run 

```
java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
```

Make sure your wallet is initialised and unlocked, providing you're fully syncronised you should see an output like this indicating that you are mining.

```
INFO  [ef-critical-dispatcher-15] o.e.m.CandidateGenerator$ - Assembling a block candidate for block #120866 from 1 transactions available
INFO  [ef-critical-dispatcher-15] o.e.m.CandidateGenerator$ - No fee proposition found in txs List(1c79bade7ba9a6eb22333f8457fb3816cef119d0ad0fd7e72737ff25676918c6)
INFO  [ef-critical-dispatcher-15] o.e.m.CandidateGenerator$ - Got candidate block at height 120866 with 1 transactions, msg 3551b7fd6f3eeee2476529213162c8824b6b54e4909696b7359afa71300d119d
INFO  [ef-critical-dispatcher-15] o.e.m.CandidateGenerator - Generated new candidate in 5 ms
INFO  [tor.default-dispatcher-13] o.e.m.ErgoMiningThread - Trying nonce 1000
INFO  [tor.default-dispatcher-13] o.e.m.ErgoMiningThread - Trying nonce 2000
INFO  [tor.default-dispatcher-13] o.e.m.ErgoMiningThread - Trying nonce 3000
INFO  [tor.default-dispatcher-13] o.e.m.ErgoMiningThread - Trying nonce 4000
INFO  [tor.default-dispatcher-13] o.e.m.ErgoMiningThread - Trying nonce 5000
```

Your rewards will be sent to your `rewardPublicKey`, which is different from your wallet address. 

```
curl -X GET "http://127.0.0.1:9052/mining/rewardPublicKey" -H  "accept: application/json"
```

/// admonition | Keep in mind
Please note that blocks take 720 confirmations on Ergo.
///


## Resources

[testnet.sigmaexplorer.org](https://testnet.sigmaexplorer.org/) is a handy alternative version of the ergo explorer that shows miner distribution, hashrate and difficulty. 