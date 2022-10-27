#  Decentralized P2P options contracts

> 🔗 From [ergoforum](https://www.ergoforum.org/t/decentralized-p2p-options-contracts-on-ergo/3763)

Options contracts can be useful in many situations for profitable trading, reducing risks, hedging portfolio etc. It is desirable to have on-chain options contracts where writing and trading options contracts do not involve additional security risks (in comparison with e.g. trading on ErgoDEX).

In this post I am going to sketch a solution for doing options on top of Ergo, which could be useful in other applications, thus can be considered as a DeFi design pattern. Our solution creates fully p2p decentralized options contracts, following idea of self-sovereign DeFi. UTXO nature of the Ergo blockchain makes the solution truly elegant.

Below we consider European-style options, as American would be even simpler. Futures also could be implemented in a similar way I guess. For European-style we consider settlement period (for example, of ~1 day which is about 720 blocks). For example, we consider a right to sell ERG for USD, then options writer is locking SigUSD in the contract, and options buyer may sell ERG during settlement period.

We consider options contract as an optional trade settlement contract, where right to perform the trade is tradeable per se. Thus we break its implementation into two entities and operations on top of them.

One entity is swap contract, which is like simplest swap contract from ErgoScript tutorial, but non-tradeable and non-refundable before the settlement period, during the settlement the swap could happen if contract NFT (see below) is present in inputs, and swapped asset (ERG in our example) is going to an address associated with NFT. After the settlement period funds locked in swap contract are refundable to options contract writer.

Another entity is NFT, which represents right to execute options contract during the settlement period, and issued in the same transaction (options contract scanner can just skip other options). To settle a trade, NFT should be locked in a receipt box, where register R4 contains a script (as SigmaProp) which swapped asset will be locked with (I guess receipt box is a simplest way to implement it). Before being locked in receipt box, NFT is not locked anywhere so freely tradeable.