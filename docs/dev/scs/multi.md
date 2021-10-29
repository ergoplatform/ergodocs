# Multi-Stage Contracts

So you’ve heard about smart contracts, but what are multi-stage contracts? Multi-stage contracts refer to smart contracts that are operating on a stateful level. Because Ergo uses the UTXO model, it is possible to process parallelized actions on top of smart contracts. 

For a blockchain to contain smart contracts, it should have loops. These loops can later refer to themselves and check whether an operation is working or not. Bitcoin’s UTXO design is very primitive, and it doesn’t contain Turing-complete smart contracts. Ethereum has this capability, but it’s a primitive version of a Turing-complete language. Ergo Blockchain provides a different approach to multi-stage contracts, empowered by the extended UTXO model. Permitting a lighter network and broader use cases.

- [Multi-Stage Contracts](https://ergoplatform.org/en/blog/2021-04-16-multi-stage-contracts/)
- [Multi-Stage Contracts in the UTXO Model: Delivery by Alexander Chepurnoy & Amitabh Saxena](https://www.youtube.com/watch?v=g3FlM_WOwBU)

Talk http://deic.uab.cat/conferences/cbt/cbt2019/resources/chepurnoy.ogv

Slides http://deic.uab.cat/conferences/cbt/cbt2019/resources/chepurnoy.pdf

Paper https://link.springer.com/chapter/10.1007/978-3-030-31500-9_16

https://twitter.com/ergoplatformorg/status/1178577553789014016