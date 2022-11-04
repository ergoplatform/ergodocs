
### chain 

Chain-specific settings. Change only if you are going to launch a new chain. 

#### protocolVersion
```
protocolVersion = 3
```

Blockchain protocol version supported by the client.

Please do not increase this value manually; this should be done by client developers.

#### addressPrefix 
```
addressPrefix = 16
```
Network address prefix, currently reserved values are 0 (Ergo mainnet) and 16 (Ergo testnet)

#### monetary
##### fixedRatePeriod
```
fixedRatePeriod = 525600
```
The number of blocks reward won't change (2 years)

##### fixedRate
```
fixedRate = 75000000000
```
number of coins issued every block during fixedRatePeriod (75 Ergo)
##### foundersInitialReward
```
foundersInitialReward = 7500000000
```

Part of coins issued, that is going to the foundation during fixedRatePeriod (7.5 Ergo)


##### epochLength
```
 epochLength = 64800
```
number of blocks between reward reduction (90 days)

##### oneEpochReduction
```
oneEpochReduction = 3000000000
```

The number of coins reward decreases every epoch (3 Ergo)


##### minerRewardDelay
```
minerRewardDelay = 720
```
The delay between the block mined and a time when the reward can be spent. ~ 1 day.
#### reemission
##### checkReemissionRules
```
checkReemissionRules = false
```
##### emissionNftId
```
      emissionNftId = ""
```
##### reemissionTokenId
```
      reemissionTokenId = ""
```
##### reemissionNftId
```
reemissionNftId = ""
```
##### activationHeight
```
activationHeight = 777217
```

##### reemissionStartHeight
```
reemissionStartHeight = 2080800
```
##### injectionBoxBytesEncoded
```
injectionBoxBytesEncoded = ""
```
#### noPremineProof
```
noPremineProof = [
      "'Chaos reigns': what the papers say about the no-deal Brexit vote", # https://www.theguardian.com/politics/2019/mar/14/chaos-reigns-what-the-papers-say-about-the-no-deal-brexit-vote
      "习近平的两会时间|这里有份习近平两会日历，请查收！", # http://www.xinhuanet.com/politics/2019lh/2019-03/13/c_1124232018.htm
      "ТАСС сообщил об обнаружении нескольких майнинговых ферм на столичных рынках", # https://www.vedomosti.ru/politics/news/2019/03/14/796376-mainingovih-ferm
      "000000000000000000139a3e61bd5721827b51a5309a8bfeca0b8c4b5c060931", # https://www.blockchain.com/btc/block/000000000000000000139a3e61bd5721827b51a5309a8bfeca0b8c4b5c060931
      "0xef1d584d77e74e3c509de625dc17893b22b73d040b5d5302bbf832065f928d03" # https://etherscan.io/block/0xef1d584d77e74e3c509de625dc17893b22b73d040b5d5302bbf832065f928d03
    ]
```

Latest news from media (the Guardian, Xinhua, Vedomosti), existing cryptocurrency block ids (Bitcoin, Ethereum)


####  foundersPubkeys 
```
 foundersPubkeys = [
      "039bb5fe52359a64c99a60fd944fc5e388cbdc4d37ff091cc841c3ee79060b8647",
      "031fb52cf6e805f80d97cde289f4f757d49accf0c83fb864b27d2cf982c37f9a8b",
      "0352ac2a471339b0d23b3d2c5ce0db0e81c969f77891b9edf0bda7fd39a78184e7"
    ]
```

Public keys of founders, represented as just group elements
   
