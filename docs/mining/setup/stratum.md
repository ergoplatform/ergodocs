## ErgoStratum

Stratum mining server for Ergo.

1. Setup a [Ergo Node for solo mining](solo-node.md), making sure to include the EIP27 rules. 
2. Setup [ErgoStratumServer](https://github.com/mhssamadani/ErgoStratumServer) (the pool server)
3. (Optional) Point [ergo-nomp](https://github.com/btclinux/ergo-nomp), a node open mining portal configured for ergo to both. 

For the  Miner Connection and Work Management, [ErgoStratumProxy](https://github.com/mhssamadani/ErgoStratumProxy) is also available and is used when you want to mine with open source miner (client side app).


## start.js

```json
"daemons": [
        {   //Main daemon instance
            "host": "NODE IP ADDRESS",
            "port": 9053,
            "user": "",
            "password": ""
        }
    ],
```

- Make sure to update `varDiff` depending on your hardware.

```json
/* Each pool can have as many ports for your miners to connect to as you wish. Each port can
       be configured to use its own pool difficulty and variable difficulty settings. varDiff is
       optional and will only be used for the ports you configure it for. /
"ports": {
        "3032": { //A port for your miners to connect to
            "diff": 240000,//the pool difficulty for this port
            /*
            * use this parameter to multiply difficulty to b for each request.
            * some miner like NBMiner does not support difficulty method of stratum.
            * if you want your pool work with these miners set this parameters.
            *
            * /
            "multiplyDifficulty": true,
            / Variable difficulty is a feature that will automatically adjust difficulty for
               individual miners based on their hashrate in order to lower networking overhead */
            "varDiff": {
                "minDiff": 240000,//Minimum difficulty
                "maxDiff":  16431986528747520,//Network difficulty will be used if it is lower than this
                "targetTime": 15, //Try to get 1 share per this many seconds
                "retargetTime": 10, //Check to see if we should retarget every this many seconds
                "variancePercent": 30, //Allow time to very this % from target without retargeting
            }
        },
        "3256": { //Another port for your miners to connect to, this port does not use varDiff
            "diff":  240000,//The pool difficulty
```

## Troubleshooting

- Have you tried turning it off and on again?
- Is your [ergo.conf](solo-node.md) configured correctly? 
- You can rescan from [swagger](swagger.md)
- Join the [🃏│solo-mining](https://discord.gg/ergo-platform-668903786361651200) channel on our Discord for community support. 
- The Node needs to be fully syncronised. Make sure your wallet is also unlocked. 
- Try adjusting difficulty in start.js if you're getting *No new blocks* debug errors. 
- If you get `fatal:unable to connect to github.com`, you need to run `git config --global url.https://github.com/.insteadOf git://github.com/`


## Resources



### Youtube

- [Ergo Node + Stratum Server mining tutorial](https://www.youtube.com/watch?v=_1M8dGpfKjU)
- [Youtube: Mine Ergo from your own Node](https://www.youtube.com/watch?v=ubov4oweA20)

### Misc

- [stratum4ergo](https://github.com/Satergo/stratum4ergo) is a Java library for creating Stratum mining pool servers for Ergo.
- [ErgoForum: Q&A on mining (for pool operators and solo miner)](https://www.ergoforum.org/t/q-a-on-mining-for-pool-operators-and-solo-miners/587)


