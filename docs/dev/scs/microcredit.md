
---
tags:
  - Microcredit
  - ErgoScript
  - Example
---

A lot of blockchain-related news these days **is** telling us that a bank _X_ or a corporation _Y_ is going to use a "blockchain" to "reduce costs". Basically, it means that just another buzzword is considered by large financial institutions as just another tool to extract value more efficiently and to save costs by cutting jobs.

While I am avoiding saying anything about "Satoshi's vision" (nothing but speculation could be dug up after his exodus), a broad view I witnessed among online forum users in the early years is that a cryptocurrency should provide tools to enrich ordinary people running small businesses providing not much above making ends meet, rather than depersonalized big financial capital. The tools of a cryptocurrency, in the eyes of the original broad community vision, should allow people to conduct economic activity regardless of business size, geographic location, interest rates set by big players, and so on. The tools should allow people to create contracts (not paper contracts, but digital, self-enforcing, and reasonably smart contracts) regardless of differences in jurisdictions, traditions, business practices, etc.

I hope Ergo **will** be useful here. Thousands of small cooperatives and individual entrepreneurs are more important **for** healthy and sustainable wealth growth around the globe than a couple of corporations hiding profits in offshore **havens**.

As an example, let's consider a cooperative federation (such as [Radical Routes](http://www.radicalroutes.org.uk/)) willing to provide financial help to an entrepreneur thousands **of** kilometers away (say, in Rojava).

We need to assume some details now. First, assume that there are four cooperatives in the network. They collectively lock _10,000_ Ergs (in equal parts, so _2,500_ Ergs each) in a contract with the following conditions:

1. The cooperatives are associated with public keys _pubkeyA_, _pubkeyB_, _pubkeyC_, _pubkeyD_. The entrepreneur is associated with a public key _businessKey_.
2. The cooperatives lock money in a coin protected by a funding contract, then perform due diligence and **vote** on whether to fund the entrepreneur. The entire contract fund (_10,000_ Ergs) **goes** to the entrepreneur if _3_ out of _4_ votes are in favor. Technically, the voting is done via a 3-out-of-4 threshold signature. If voting is not successful (_3_ out of _4_ signatures are not collected) before block number _1,000_, any cooperative (actually, anyone) can submit a **withdrawal** transaction, which returns at least _2,500_ Ergs to every cooperative. This funding contract will also be called the voting contract.
3. The investments can be spent on three goals, with strict bounds. Namely, the entrepreneur must spend at least _5,000_ Ergs on equipment and at least _2,000_ Ergs on the construction of a needed building; other funds the entrepreneur may spend arbitrarily.
4. To ensure that equipment money will be spent on equipment, the cooperative federation uses public keys of known equipment sellers in the entrepreneur's area. For example, consider equipment sellers with public keys _pubkeyTool1_, _pubkeyTool2_, _pubkeyTool3_, _pubkeyTool4_ in the area. Technically, the transfer is organized as a collective signature of one **of the** equipment sellers (thus a ring signature from **the** equipment sellers' ring AND the entrepreneur's signature).
5. Similarly, assume that there are _3_ builders in the **area the** cooperative federation recognizes, associated with public keys _pubkeyConstr1_, _pubkeyConstr2_, and _pubkeyConstr3_.
6. Similarly to the voting contract, if equipment and construction contracts are not co-signed before block number _5000_, the federation cooperatives **can** withdraw funds.

There are different ways to define contracts in Ergo. A script in the low-level language, **ErgoTree**, describes a (single) logical condition on whether a coin can be spent according **to it**, and also requires a spending proof provided by a spending transaction. Internally, the condition is represented as a typed syntax tree, hence the name. The structure allows us to do ahead-of-time cost analysis, etc. A higher-level language called **ErgoScript** allows **for a** more traditional and readable description, using variables and breaking logic into subroutines.

Let's start with the main contract defined in points (1-3) above:

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

This **ErgoScript** script is to be compiled into a syntax tree (which is written into the blockchain in a serialized form) by binding it with concrete values for variables (_pubkeyA_, _pubkeyB_, _pubkeyC_, _pubkeyD_, _spendingContract1Hash_, _spendingContract2Hash_). _spendingContract1Hash_ is a hash of the (serialized) equipment spending script, which will be provided below; _spendingContract2Hash_ is a hash of the construction spending script.


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

Now assume that the cooperative federation has created a coin protected by the voting contract. Below is how the entrepreneur can conduct their business:

1. Create a transaction which consumes the coin and **creates** at least three new coins: one with the equipment spending contract, another with the construction spending contract, and **a** third **creates** a coin protected by **the** entrepreneur's public key.
2. Send the transaction to the cooperatives; wait for the transaction with the threshold-signed input to be published on the blockchain.
3. Enter into a contract with an equipment seller; co-sign a spending transaction.
4. Enter into a contract with a builder; co-sign a spending transaction.


The entrepreneur can easily run away without doing any business, but with no more than _3,000_ Ergs. This can be fixed; e.g., this money could be made spendable only after block number _5,000_; before that, **the** money could be withdrawn by the cooperatives. For equipment and construction spending, the entrepreneur works alongside some presumably already reputable businesses. Thus, the investor reduces their risks.

You can find [code and example transactions online](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sc/src/test/scala/sigmastate/utxo/examples/CoopExampleSpecification.scala). Please note that we have more examples of complex signature schemes, multi-step contracts (with on-the-go execution paths revealing, like MAST in Bitcoin but with cycles allowed), oracles, crowdfunding, and so on. Please check our [examples repository](https://github.com/ScorexFoundation/sigmastate-interpreter/tree/develop/sc/src/test/scala/sigmastate/utxo/examples).
