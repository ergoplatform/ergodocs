---
tags:
  - EIP
---
# Proxy contracts

> 🔗 From [EIP-0017](https://raw.githubusercontent.com/ergoplatform/eips/master/eip-0017.md)

* Author: anon_real
* Status: Proposed
* Created: 05-May-2021
* License: CC0
* Forking: not needed

## Motivation

Outsourcing transaction generation to an external service/dApp can be useful or even needed in various circumstances. For example, avoiding wallet limitations to generate any transaction on behalf of the user - [Ergo Assembler](https://github.com/anon-real/ergo-assembler) is designed for this purpose. Another example is to scale dApps to be able to fulfill many requests without double-spending or data invalidation - SigmaUSD dApp can use proxy contracts to avoid bank double-spending and ERG/USD oracle data invalidation.

## Background

The idea of proxy contracts came to life with the [Ergo Assembler](https://github.com/anon-real/ergo-assembler) which helped dApp developments like [Ergo Auction House](https://ergoauctions.org/), [ErgoUtils](https://ergoutils.org/), and [SigmaUSD web interface](https://sigmausd.io/#/) despite not having a wallet-bridge like MetaMask (Ethereum wallet) in the ecosystem.

During this time, the structure of proxy contracts evolved as some malicious users tried to take advantage of some minor vulnerabilities, mostly in the [SigmaUSD dApp](https://sigmausd.io/#/).

## The structure

In the beginning, the sole purpose of proxy contracts was to protect users from losing their funds (not to be cheated) when they outsource their assets to engage with some dApp. While the initial structure succeeded to achieve this, it proved to be not sufficient for the whole dApp infrastructure to work without malicious activities. Some examples of dApp infrastructure violations are as follows:

* A malicious whale tried to take advantage of this simple structure by stealing UI fees from SigmaUSD web interface developers for some period of time. This happened because the proxy contracts were simply only trying to protect users from malicious activities, not the dApp infrastructure.

* The same whale tried to prevent user's requests (minting/redeeming) from being executed by the assembler service by retuning their funds as soon as funds were broadcasted in the network. This happened also because of the same reasons.

* Moreover, the whale tried to sell SigUSD/SigRSV tokens to users by imitating the bank box. He succeeded to do that and take 2.25% fee for each request which was supposed to go to the SigRSV holders (2%) and UI devs (0.25%).

The above attacks were possible because proxy contracts were not designed to preserve the integrity of the whole dApp infrastructure but only the user's funds.

Generally, proxy contracts should be designed to:  

* prevent dApp developers or any other attacker from taking advantage of user's funds in any manner
* preserve the integrity of the dApp by preventing attacks like the ones explained in the above examples.

To achieve all of the above, the below contract structure is proposed as an example:

```scala
{
  // dApp-specific part ensuring that user will receive what he is paying for
  val properFundUsage = {
    val userOut = OUTPUTS(1)
    userOut.propositionBytes == fromBase64("$userAddress") && // user must be the recipient
      userOut.tokens(0)._1 == fromBase64("$scTokenId") && // user must receive SigmaUSD
      userOut.tokens(0)._2 >= $scAmountL && // the amount of SigmaUSD must be at least what user is paying for
      HEIGHT < $timestampL // this part is always true (timestamp is the unix-timestamp at the time of the request), it will cause compiled address to differ everytime
  }
  
  // ensuring dApp integrity is preserved - any dApp specific condition to ensure designed procedures won't be violated
  val UIFeeOk = OUTPUTS(2).propositionBytes == fromBase64("$implementor") && OUTPUTS.size == 4 // UI fee must go to UI devs not any random person who assembles the transaction
  val properBank = OUTPUTS(0).tokens(2)._1 == fromBase64("$bankNFT") // the real bank box of the sigmaUSD protocol must be used so not any random person can behave as the bank box
  val dAppWorksFine = properFundUsage && UIFeeOk && properBank

  // in any case, whether assembler refuses to execute the request or the request fails for any reason, user must be able to get back his funds
  val returnFunds = { 
    val total = INPUTS.fold(0L, {(x:Long, b:Box) => x + b.value}) - $returnFee // only refund transactions's fee must be deducted from user's funds
    OUTPUTS(0).value >= total && OUTPUTS(0).propositionBytes == fromBase64("$userAddress") // user must receive the appropriate amount
    && (PK("$assemblerNodeAddr") || HEIGHT > $refundHeightThreshold) && // either dApp-specific node can return user's funds or some time (block) has to be passed first. This is useful for many reasons.
    OUTPUTS.size == 2 // only refund box and transaction fee box is needed
  }

  sigmaProp(dAppWorksFine || returnFunds) // either dApp must work as it is supposed to or user's funds must be returned
}
```

The above contract is the proxy contract of minting operation in the [SigmaUSD dApp](https://sigmausd.io/#/). Anything started with `$` in the contract must be provided to it based on the user's request at the time of compilation.

The contract has three main parts:  

* Ensuring proper usage of user's funds, i.e., user will receive what he is paying for in proper amount without anyone being able to cheat.
* Ensuring the integrity of the dApp procedures.
* Ensuring that user will be refunded in any case of failures.

Now we will go through some parts of the above contract which are both important and ambiguous at the first glance.

* `(PK("$assemblerNodeAddr") || HEIGHT > $refundHeightThreshold)`: Either dApps's specific node can refund the user (at any time) or some time has to be passed for refunding without any secrets involved. This part prevents malicious users from sending refunds to users, preventing user's request (minting, in this case) from being executed. The same logic can be used to only allow a certain (or multiple) entities to execute requests. This enables dApps to control the order of execution which makes scaling dApps possible as it allows them to control double-spending and other similar problems.
* `HEIGHT < $timestampL`: This will result in different address every time the contract is compiled. This is useful from the UI perspective to be able to track user's requests in an address-specific manner.
