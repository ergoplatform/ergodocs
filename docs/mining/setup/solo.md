# Solo Mining

You can solo mine on any pool that offers a solo port. Otherwise, you will essentially need to host your own pool.

Firstly, check out this [calculator](https://docs.google.com/forms/d/e/1FAIpQLScBFv3mxpu5Erv55zvfFuIo2NnaWht3cc70xZoRo-3c58Cv0A/viewform) if you're not sure if you should be solo mining.

There is now a solo-mining smart subpool on [getblok](https://www.getblok.io/smartpools/). Alternatively 2Miners, solopool.org and others offer Solo mining. 



## Getting Started

To solo mine you will need one of the following depending on your setup. 

- [Autolykos2_NV_Miner](https://https://github.com/mhssamadani/Autolykos2_NV_Miner)
- [Autolykos2_AMD_Miner](https://github.com/mhssamadani/Autolykos2_AMD_Miner)

You may or may not need to use Stratum Server and Stratum Proxy to operate them. These two projects are here:

- [ErgoStratumServer](https://github.com/mhssamadani/ErgoStratumServer)
- [ErgoStratumProxy](https://github.com/mhssamadani/ErgoStratumProxy)

To be able to spend any ERG mined this way, you will need to add this to your `.config`

```
ergo {
  wallet {
    checkEIP27 = true
  }
}
```

##  ​/mining​/solution entrypoint

```
{
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
  "n": "0000000000000000",
  "d": 987654321
}
```

- pk is public key as binary
- n is nonce
- w and d are not used anymore in Autolykos2 and **constant**

## Resources

- [Ergo Node + Stratum Server mining tutorial](https://www.youtube.com/watch?v=_1M8dGpfKjU)
- [Youtube: Mine Ergo from your own Node](https://www.youtube.com/watch?v=ubov4oweA20)
- [ErgoForum: Q&A on mining (for pool operators and solo miner)](https://www.ergoforum.org/t/q-a-on-mining-for-pool-operators-and-solo-miners/587)


