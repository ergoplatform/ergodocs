
# Transaction Speed

Transaction speed, specifically TPS, measures the transactions per block/second a blockchain can perform, quantifying how quickly a blockchain can complete transactions.  

Below are approximated TPS values for some popular blockchains:

* BTC - ~7 TPS (Gobbel, 2017).
* ETH - ~15 TPS (Clincy et al (table1), 2019)
* XRP - ~ 1500 TPS (Clincy et al (table1), 2019)
* ADA - ~ ~7 TPS (~250 in controlled tests) (Stamoulis, 2021).
* DOT - ~1500 TPS (Hiemstra et al., 2021)

In the context of Ergo, the TPS (transactions per second) metric is not very insightful. While the number of transactions a platform can handle is important, on Ergo, the weight of the transactions and the computational cost limit per block are more crucial factors. The cost limit of transactions is affected by various dynamic factors, including the network size and the hardware miners have. 

With the release of [Node v5](jitc.md), the raw TPS numbers should bring us to around **47.5tx/s** - improvements on top of this are still possible. 

The focus is on raising the TPS without compromising classic blockchain assumptions and guarantees. 
