
A lot of blockchain-related news these days are telling us that a bank _X_ or a corporation _Y_
is going to use a "blockchain" to "reduce costs". Basically, it means that just another buzzword is 
considered by big banksters as just another tool to extract value from everywhere in a more efficient way
and also to save on cutting job positions.  

While I am avoiding to say anything about "Satoshi's vision" (nothing but speculations could be dug thereafter 
his exodus), a broad view I witnessed in the early years around online forums users is that a cryptocurrency 
should provide tools to enrich the ordinary people behind their small businesses providing no much above making ends meet, not depersonalized big financial capital. The tools of 
a cryptocurrency, in the eyes of the original broad community vision, should allow people to do economic activity dependless on business size, geographic location, interest rates set by big players, and so on. 
The tools should allow people to do contracts (no paper contracts, but digital, self-enforcing, and reasonably smart contracts) dependless on differences in jurisdictions, traditions, followed business practices etc.

I hope Ergo would be useful here. Thousands of small cooperatives and individual entrepreneurs are more important to healthy and sustainable wealth growth around the globe than a couple of corporations hiding profits in offshore heavens. 

As an example, let's consider a cooperative federation (such as [Radical Routes](http://www.radicalroutes.org.uk/)) willing to provide financial help to an entrepreneur thousands kilometers away (say, in Rojava). 

We need to assume some details now. In the first place, assume that there are four cooperatives in the network. They collectively lock _10,000_ Ergs (in equal parts, so _2,500_ Ergs each) in a contract, which says the following:

1. The cooperatives are associated with public keys _pubkeyA_, _pubkeyB_, _pubkeyC_, _pubkeyD_. The entrepreneur is associated with a public key _businessKey_.
2. The cooperatives are locking money in a coin protected by a funding contract, then doing due diligence and vote on whether to fund the entrepreneur or not. All the contract fund (_10,000_ Ergs) is going to the entrepreneur if _3_ votes out of _4_ are for that. Technically, the voting is done via 3-out-of-4 threshold signature. If voting is not successful (_3_ out of _4_ signatures are not collected) before the block number _1,000_, any cooperative (actually, anyone) can submit withdraw transaction, which is returning _2,500_ Ergs (at least) to every cooperative. Further, the funding contract will also be called the voting contract.
3. The investments could be spent on three goals, with some strict bounds. Namely, the entrepreneur must spend at least _5,000_ Ergs on equipment, at least _2,000_ Ergs on construction of a building needed, other funds the entrepreneur may spend arbitrarily.
4. To be sure that equipment money will be spent on equipment, the cooperative federation is using public keys of known equipment sellers in the area of the entrepreneur. For example, consider that there are equipment sellers with public keys _pubkeyTool1_, _pubkeyTool2_, _pubkeyTool3_, _pubkeyTool4_ in the area. Technically, the transfer is organized as a collective signature of one equipment sellers (thus ring signature from equipment sellers ring AND entrepreneur's signature)
5. Similarly, assume that there are _3_ builders in the are cooperative federation is recognizing, associated with public keys _pubkeyConstr1_, _pubkeyConstr2_, and _pubkeyConstr3_.
6. Similarly to the voting contract, if equipment and construction contracts are not co-signed before block number _5000_, the federation cooperatives could withdraw funds. 

There are different ways to define contracts in Ergo. A script in the low-level language, **ErgoTree**, is describing a (single) logical condition on whether a coin could be spent according it, and also a spending proof provided by a spending transaction. Internally, the condition is represented as a typed syntax tree thus the name. The structure is allowing us to do ahead-of-time cost analysis etc. Higher-level language called **ErgoScript** allows to have more traditional and readable description, use variables and break logic into subroutines. 

Let's start with the main contract defined in (1-3) above:

```scala
{
 val votingSuccess  = atLeast(3, Array(pubkeyA, pubkeyB, pubkeyC, pubkeyD))
 val properSpending = OUTPUTS(0).value >= 5000L &&
                      blake2b256(OUTPUTS(0).propositionBytes) == spendingContract1Hash &&
                      OUTPUTS(1).value >= 2000L &&
                      blake2b256(OUTPUTS(1).propositionBytes) == spendingContract2Hash

 val withdrawCondition = HEIGHT >= 1000L &&
                         OUTPUTS(0).value >= 2500L && OUTPUTS(0).propositionBytes == pubkeyA.propBytes &&
                         OUTPUTS(1).value >= 2500L && OUTPUTS(1).propositionBytes == pubkeyB.propBytes &&
                         OUTPUTS(2).value >= 2500L && OUTPUTS(2).propositionBytes == pubkeyC.propBytes &&
                         OUTPUTS(3).value >= 2500L && OUTPUTS(3).propositionBytes == pubkeyD.propBytes 

 (votingSuccess && properSpending) || withdrawCondition
}
```

This script in the **ErgoScript** is to be compiled into a syntax tree (which is to be written into the blockchain in a serialized form) by binding it with concrete values for variables (_pubkeyA_, _pubkeyB_, _pubkeyC_, _pubkeyD_, _spendingContract1Hash_, _spendingContract2Hash_). _spendingContract1Hash_ is a hash of (serialized) equipment spending script which will be provided below, _spendingContract2Hash_ is a hash of construction spending script. 


The equipment spending script is below: 

```scala
{
 val spendingSuccess = (pubkeyTool1 || pubkeyTool2 || pubkeyTool3 || pubkeyTool4) && businessKey

 val withdrawCondition = HEIGHT > 5000L &&
                         OUTPUTS(0).value >= 1250L && OUTPUTS(0).propositionBytes == pubkeyA.propBytes &&
                         OUTPUTS(1).value >= 1250L && OUTPUTS(1).propositionBytes == pubkeyB.propBytes &&
                         OUTPUTS(2).value >= 1250L && OUTPUTS(2).propositionBytes == pubkeyC.propBytes &&
                         OUTPUTS(3).value >= 1250L && OUTPUTS(3).propositionBytes == pubkeyD.propBytes 

 spendingSuccess || withdrawCondition
}
```

And the construction script is: 

```scala
{
 val spendingSuccess = (pubkeyConstr1 || pubkeyConstr2 || pubkeyConstr3) && businessKey

 val withdrawCondition = HEIGHT > 5000L &&
                         OUTPUTS(0).value >= 500L && OUTPUTS(0).propositionBytes == pubkeyA.propBytes &&
                         OUTPUTS(1).value >= 500L && OUTPUTS(1).propositionBytes == pubkeyB.propBytes &&
                         OUTPUTS(2).value >= 500L && OUTPUTS(2).propositionBytes == pubkeyC.propBytes &&
                         OUTPUTS(3).value >= 500L && OUTPUTS(3).propositionBytes == pubkeyD.propBytes 

 spendingSuccess || withdrawCondition
}
```

Now assume that the cooperative federation has created a coin protected by the voting contract. Below is how the entrepreneur can do his business:

1. Create a transaction which consumes the coin and create at least three coins, one with equipment spending contract, another with construction spending contract, third is creating a coin protected by entrepreneur's public key.  
2. Send the transaction to the cooperatives, wait for the transaction with the threshold-signed input being published on the blockchain.  
3. Consider a contract with an equipment seller, co-sign a spending transaction.
4. Consider a contract with a builder, co-sign a spending transaction.


The entrepreneur can easily run away without doing any business, but with no more than _3,000_ Ergs. This can be fixed, e.g. this money could be made spendable only after block number _5,000_, and before that money could be withdrawn by the cooperatives. For equipment and construction spendings, the entrepreneur is working along with some, presumably already reputable, business. Thus the investor is reducing its risks.

You can find [code and example transactions online](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sc/src/test/scala/sigmastate/utxo/examples/CoopExampleSpecification.scala). Please note that we have more examples of complex signature schemes, multi-step contracts (with on-the-go execution paths revealing, like MAST in Bitcoin, but with cycles allowed), oracles, crowdfunding and so on. Please check our [examples repository](https://github.com/ScorexFoundation/sigmastate-interpreter/tree/develop/sc/src/test/scala/sigmastate/utxo/examples). 
