# Chain Configuration Settings

This section pertains to chain-specific settings, which should typically be left untouched unless you are planning to launch a new blockchain.

### protocolVersion
```
protocolVersion = 3
```
The `protocolVersion` parameter represents the version of the blockchain protocol that the client supports. Please refrain from manually adjusting this value; it should be managed by client developers.

### addressPrefix 
```
addressPrefix = 16
```
This parameter denotes the network address prefix. Currently, the reserved values are 0 for Ergo mainnet and 16 for Ergo testnet.

### Monetary Configuration
#### fixedRatePeriod
```
fixedRatePeriod = 525600
```
This parameter specifies the number of blocks during which the reward amount does not change. In this case, it is set to remain constant for approximately two years.

#### fixedRate
```
fixedRate = 75000000000
```
This sets the number of coins (75 Ergo) to be issued every block during the `fixedRatePeriod`.

#### foundersInitialReward
```
foundersInitialReward = 7500000000
```
This parameter denotes the fraction of coins issued, that goes to the foundation during `fixedRatePeriod` (7.5 Ergo). 

#### epochLength
```
 epochLength = 64800
```
This represents the number of blocks between each reward reduction, set to occur every 90 days.

#### oneEpochReduction
```
oneEpochReduction = 3000000000
```
This indicates the amount by which the reward decreases after each epoch (3 Ergo).

#### minerRewardDelay
```
minerRewardDelay = 720
```
This represents the delay (about 1 day) between the block being mined and the miner being able to spend the reward.

### Reemission Configuration
The parameters below are related to reemission settings of the protocol:

```
checkReemissionRules = false
emissionNftId = ""
reemissionTokenId = ""
reemissionNftId = ""
activationHeight = 777217
reemissionStartHeight = 2080800
injectionBoxBytesEncoded = ""
```
The exact roles and potential values of these parameters are not clarified in this document and would need further specification.

### noPremineProof
```
noPremineProof = [
      "'Chaos reigns': what the papers say about the no-deal Brexit vote",
      "习近平的两会时间|这里有份习近平两会日历，请查收！",
      "ТАСС сообщил об обнаружении нескольких майнинговых ферм на столичных рынках",
      "000000000000000000139a3e61bd5721827b51a5309a8bfeca0b8c4b5c060931",
      "0xef1d584d77e74e3c509de625dc17893b22b73d040b5d5302bbf832065f928d03"
    ]
```
The `noPremineProof` parameter includes the latest news from media outlets (the Guardian, Xinhua, Vedomosti) and existing cryptocurrency block IDs (Bitcoin, Ethereum) as evidence of no premine. 

### foundersPubkeys 
```
 foundersPubkeys = [
      "039bb5fe52359a64c99a60fd944fc5e388cbdc4d37ff091cc841c3ee79060b8647",
      "031fb52cf6e805f80d97cde

289f4f757d49accf0c83fb864b27d2cf982c37f9a8b",
      "0352ac2a471339b0d23b3d2c5ce0db0e81c969f77891b9edf0bda7fd39a78184e7"
    ]
```
The `foundersPubkeys` parameter represents the public keys of the founders, expressed as group elements.
