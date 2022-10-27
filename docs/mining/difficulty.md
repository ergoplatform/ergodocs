## Difficulty Adjustment

Ergo uses the **linear least square method** to calculate difficulty. This function is based on the past eight epochs (8x1024 blocks), as described in [this paper](https://eprint.iacr.org/2017/731.pdf) to obtain a target block interval of 120s (2 minutes), on average, during steady-hash. 

- [Coin hopping Attack — What after a month of Bitcoin hardfork?](https://medium.com/nikoin/coin-hopping-attack-what-after-a-month-of-bitcoin-hardfork-f5a92151fb7b)

Autolykos will adjust slowly in response to fluctuating hashrate, but this helps prevent **adversarial** hopping. This algorithm has a 1.9% error rate compared to bitcoins 9.1% error rate (exponential 10% hash rate growth). 

You can use the [difficulty & epoch monitor](https://cds.oette.info/ergo_diff.htm) to get an estimate for the next difficulty due. 

**Why 2 minutes?**

As Ergo is a P2P cryptocurrency that supports smart contracts, there is need for security buffer for all the issues and attacks possible; propagation delays, spam attacks, verifier dilemma etc

**Can it be quicker?**

Ergo already uses an epoch length of ~1.5 days (with normal block rate), compared to Bitcoin's two weeks. Having a quicker difficulty readjustment can lead to Timewarp attacks. More epochs were considered, but the retargeting function is also non-linear, so it can adjust sooner than the linear function in certain popular scenarios; and it is unclear whether any hard-fork would be required at this stage. 

There is a discussion ongoing on [ergoforum](https://www.ergoforum.org/t/diff-adjustment-potential-design-tradeoffs/3875/30) regarding a potential improvement to this algorithm. 
