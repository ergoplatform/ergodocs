# Difficulty Adjustment

Ergo uses the **linear least square method** to calculate difficulty. This function is based on the past eight epochs (8x1024 blocks), as described in [this paper](https://eprint.iacr.org/2017/731.pdf) to obtain a target block interval of 120s (2 minutes), on average, during steady-hash. 

- [Coin hopping Attack — What after a month of Bitcoin hardfork?](https://medium.com/nikoin/coin-hopping-attack-what-after-a-month-of-bitcoin-hardfork-f5a92151fb7b)

Before [EIP37](eip37.md) Autolykos adjusted slowly in response to fluctuating hashrate, this helped to prevent **adversarial** hopping with a 1.9% error rate compared to bitcoins 9.1% error rate (exponential 10% hash rate growth). 

EIP37 was implemented as a big influx of mining hashrate over multiple epochs, especially with super-linear hashrate growth over time (as we seen with the ETH merge) results in huge spike of difficulty. Similarly, few slow epochs may cause huge drop. 

You can use the [difficulty & epoch monitor](https://cds.oette.info/ergo_diff.htm) to get an estimate for the next difficulty due. 

**Why 2 minutes?**

As Ergo is a P2P cryptocurrency that supports smart contracts, there is need for security buffer for all the issues and attacks possible; propagation delays, spam attacks, verifier dilemma etc

**Can it be quicker?**

Ergo already uses an epoch length of ~4.2 hours (with normal block rate), compared to Bitcoin's two weeks. Having a quicker difficulty readjustment can lead to Timewarp attacks. 


