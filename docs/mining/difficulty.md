# Difficulty Adjustment

> You can use the [difficulty & epoch monitor](https://cds.oette.info/ergo_diff.htm) to get an estimate for the next difficulty due. 

Before [EIP37](https://docs.ergoplatform.com/mining/standards/eip37/) was implemented, Autolykos had a slow difficulty adjustment mechanism that responded to fluctuating hashrate, This helped prevent adversarial hopping with a 1.9% error rate compared to Bitcoin's 9.1% error rate. This adjustment was based on the linear least squares method, which used the past eight epochs (8 x 1024 blocks) to calculate the difficulty function, as described in [this paper](https://eprint.iacr.org/2017/731.pdf), to achieve a target block interval of 120 seconds (2 minutes on average during steady hashrate).

However, a large influx of mining hashrate over multiple epochs, especially with super-linear hashrate growth over time (as we seen with the ETH merge), resulted in a huge spike in difficulty, while a few slow epochs can cause a significant drop. EIP37 was proposed and implemented to address this issue. This proposal allows for a more efficient and timely adjustment of the difficulty level based on a shorter, more recent block history, reducing the impact of sudden changes in hashrate. The implementation of EIP37 has made Ergo's mining process more robust and resistant to adversarial.


**Why 2 minutes?**

The 2-minute target block interval in Ergo is chosen to provide a security buffer against various issues and attacks that can arise in a P2P cryptocurrency network that supports smart contracts. These include propagation delays, spam attacks, and verifier dilemmas, among others. A shorter block interval could expose the network to Timewarp attacks, a type of difficulty manipulation attack that can result in blocks being mined too quickly or too slowly. Moreover, using an epoch length of ~4.2 hours (with a normal block rate) in Ergo already greatly improves Bitcoin's two weeks. Overall, a 2-minute block interval strikes a balance between network security and transaction speed, making Ergo an efficient and secure cryptocurrency for everyday use.