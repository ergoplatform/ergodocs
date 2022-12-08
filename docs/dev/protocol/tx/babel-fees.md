# Babel Fees

> From [EIP-31](https://github.com/ergoplatform/eips/blob/6fb344914b98f81117910ae7f486533f0db6fea9/eip-0031.md)

The term “babel fees“ refers to the concept of paying transaction fees in tokens (fe. stablecoins) instead of the platform’s primary token (ERG). For more information about the origin of the term and concepts behind “babel fees“, please see the following articles:

  * [Babel fees - denominating transaction costs in native tokens](https://iohk.io/en/blog/posts/2021/02/25/babel-fees/)
  * [Paying fee in ErgoMix in primary tokens](https://www.ergoforum.org/t/paying-fee-in-ergomix-in-primary-tokens/73)

EIP-0031 aims to provide the standard for paying fees in tokens and thus has the same goal as Cardano’s “babel fees“; however, it chooses a different approach, with the main difference being that EIP-0031 does not require any forking.

With Cardano’s approach, the user publishes an “invalid"(incomplete) transaction and has to wait, hoping that somebody will take his tokens and pay the transaction fees in a primary token (ADA), therefore completing the transaction. EIP-0031, on the other hand, chooses the opposite approach.

> **On Cardano**, you will send an “incomplete” transaction, offering to pay the fee using x amount of tokens and wait until a third party accepts your tokens in exchange for ADA to pay the fees.
> 
> **On Ergo**, we have pre-defined Babel Fee pools, so there is no waiting, and we can know in advance what tokens we can use to pay fees and the best price available.


Supporters wishing to make money from EIP-0031 will publish UTXOs, containing primary tokens locked by a smart contract. These will contain price attributes (i.e. how much of the primary tokens is that one specific supporter is willing to pay for one piece of user’s tokens (i,e. stablecoins)). Let us call this user’s token a “babel token”.

The user willing to pay the transaction fee in babel tokens can now find whether any UTXOs belonging to the P2S address specified by the corresponding smart contract for that specific babel token exist. If any UTXO contains enough primary tokens for required fees, the user can calculate the price of buying the required amount of primary tokens from this UTXO and then decide whether or not he wishes to use it. If he accepts this exchange ratio (defined by the UTXO’s price attribute), he can consequently spend this UTXO in his transaction to cover the transaction fees. This spending user now has to recreate the UTXO with the same parameters and insert the required amount of babel tokens into it (primary tokens difference should be less or equal to inserted babel tokens amount times price), which is going to be ensured by the smart contract.

A strong advantage of this approach (compared to Cardano’s one) is that the user always knows in advance whether there is an opportunity to pay via “babel fees” or not and, if there is, what is the exchange ratio. He can be (almost) certain that if he decides to use it, his transaction will be included in the blockchain ledger. Be aware, however, that there exist some exceptions to this rule, which is later discussed in the “Wallets implementation” section.

Motivation
--------------------------------------------

Many users use blockchain solely for transferring (native)tokens, such as stablecoins or even “meme” coins. These users, understandably, do not want to be bothered with keeping an eye on the amount of blockchain’s primary token they own or even obtaining this primary token in the first place.

Once they run out of primary tokens, they have to, difficultly (and often costly) swap their tokens of interest for the primary tokens they can later use to cover transaction fees. Since primary tokens are also needed for these swaps, users may be forced to introduce new capital to their portfolio solely to purchase primary tokens used for fee-paying. 

Since basic transactional fees on the Ergo blockchain are generally quite low, the "babel fees" users would probably be willing to pay a fee that could be higher than that of a primary token transaction in exchange for being able to pay in their token of interest and not having to bother with the blockchain’s primary token purchase.

This brings up a financial incentive for “EIP-0031 supporters”, who could benefit from this arbitrage by providing liquidity for such “babel fees” users, with the primary token’s selling price (expressed in tokens of interest) being higher compared to the same token pair on the exchanges.

Smart contract specification
--------------------------------------------
Here is the smart contract's source code in ErgoScript which will be used to protect the babel fee box:
```scala
{

    // ===== Contract Information ===== //
    // Name: EIP-0031 Babel Fees Contract
    // Description: Contract guarding the babel fee box, checking if the valid output babel box was recreated and the token exchange was valid.
    // Version: 1.0.0

    // ===== Relevant Variables ===== //
    val babelFeeBoxCreator: SigmaProp = SELF.R4[SigmaProp].get
    val ergPricePerToken: Long = SELF.R5[Long].get
    val tokenId: Coll[Byte] = _tokenId
    val recreatedBabelBoxIndex: Option[Int] = getVar[Int](0)

    // ===== Perform Babel Fee Swap ===== //
    if (recreatedBabelBoxIndex.isDefined) {

        // Check conditions for a valid babel fee swap
        val validBabelFeeSwap: Boolean = {
            
            // Output babel fee box
            val recreatedBabelBox: Box = OUTPUTS(recreatedBabelBoxIndex.get)
        
            // Check that the babel fee box is recreated correctly
            val validBabelFeeBoxRecreation: Boolean = {

                allOf(Coll(
                    (recreatedBabelBox.propositionBytes == SELF.propositionBytes),
                    (recreatedBabelBox.tokens(0)._1 == tokenId),
                    (recreatedBabelBox.R4[SigmaProp].get == babelFeeBoxCreator),
                    (recreatedBabelBox.R5[Long].get == ergPricePerToken),
                    (recreatedBabelBox.R6[Coll[Byte]].get == SELF.id)
                ))

            }

            // Check that the user's token was exchanged correctly
            val validBabelFeeExchange: Boolean = {

                val nanoErgsDifference: Long = SELF.value - recreatedBabelBox.value
                val babelTokensBefore: Long = if (SELF.tokens.size > 0) SELF.tokens(0)._2 else 0L 
                val babelTokensDifference: Long = recreatedBabelBox.tokens(0)._2 - babelTokensBefore

                allOf(Coll(
                    (babelTokensDifference * ergPricePerToken >= nanoErgsDifference),
                    (nanoErgsDifference >= 0)
                ))

            }

            allOf(Coll(
                validBabelFeeBoxRecreation,
                validBabelFeeExchange
            ))

        }

        sigmaProp(validBabelFeeSwap)

    } else {

        // ===== Perform Babel Fee Box Withdrawl ===== //
        babelFeeBoxCreator

    }

}
```

### Contract Template
Compilation of babel fee box smart contracts for different tokens of interest will result in different P2S addresses, leading to each token having a unique corresponding ErgoTree and, consequently, a unique P2S babel fee box smart contract address. To avoid rebuilding the contract for each token, the implementer can use the following contract template, where the `{tokenId}` fragment must be replaced by the hexadecimal identifier of the token of interest.

```
100604000e20{tokenId}0400040005000500d803d601e30004d602e4c6a70408d603e4c6a7050595e67201d804d604b2a5e4720100d605b2db63087204730000d606db6308a7d60799c1a7c17204d1968302019683050193c27204c2a7938c720501730193e4c672040408720293e4c672040505720393e4c67204060ec5a796830201929c998c7205029591b1720673028cb272067303000273047203720792720773057202
```

### Output position

The position of the recreated Babel Box in the transaction's outputs must be set as a context extension variable in the spending Babel Box.

1. Context variable `0`
    * Type: `SInt`
    * Value: position of the recreated Babel Box in the transaction's outputs

### Parameters
Parameters (creator’s public key and price) are specified via registers, meaning the resulting babel fee boxes from different creators will always belong to the same P2S address, improving their searchability.

1. Register R4
    * Type: `SigmaProp`
    * Value: creator's public key
2. Register R5
    * Type: `SLong`
    * Value: how much nanoErgs is the creator willing to pay for one babel token

Babel fee box creator can spend the babel box in any circumstances.

Other users, on the other hand, can spend this box as input to their transaction only when they also recreate it as the output of their transaction with the very same registers (R4, R5) values together with the insertion of a required amount of babel tokens (the amount of inserted babel tokens multiplied by the price specified in the R5 register has to be equal to or bigger than the amount of nanoErgs spent from the babel fee box).

Wallets implementation
--------------------------------------------

Wallet developers will need to decide whether they want to support EIP-0031. If they do decide to support this standard, they should also decide on which tokens they want to support (this could be done based on user requirements – e.g. implementing big stablecoins or “meme” coins, etc.), as this could be more convenient than supporting all tokens.

As P2S addresses belonging to a specific token of interest stay the same, these addresses could be easily “hardcoded” when supporting only a few tokens. Suppose the developers decide to support any token. In that case, the previously mentioned smart contract for each token that which user holds should be compiled or "mounted" as described in ["Contract Template"](#contract-template) subsection, and the availability of Babel Fee boxes (UTXOs) for the specific tokens of interest in the blockchain should be subsequently checked.

The proposed babel fee smart contract is general and does not impose many restrictions on the transaction. It is possible to transact some tokens while paying babel fees with another token, etc. 

Once the wallet finds a babel fee box which could be used to pay required transaction fees, it should calculate the required price for the transaction fee and present it to the user, so he can decide whether to use this particular option.

The wallet should also check the current mempool and determine whether someone is trying to spend this specific babel fee box. In that case, the wallet should construct a “chained” transaction (using the mempool’s transaction output (recreated babel fee output) as the new babel fee box input). This way, many transactions spending “the same” box could be chained and mined inside a single block. A situation can also occur when the babel fee box owner is trying to spend his own box. In that case, the wallet should select another babel fee box, if available. 

Once the wallet successfully crafts and relays the transaction to the mempool, it MUST keep an eye on the transaction until it is mined. This is important because the wallet cannot prevent somebody else from spending the same babel fee box as our user’s transaction is trying to spend. When two transactions are trying to spend the same box, only one from them can be mined and therefore included in the blockchain, while the other has to be recrafted with the new babel fee box and relayed again to the network. Such a thing should occur rarely, but when it does, the wallet has to handle the situation correctly while notifying the user that the transaction did not go through.

Reference implementations
--------------------------------------------
* [Nautilus Wallet implementation](https://github.com/capt-nemo429/nautilus-wallet/pull/82)
* [AppKit implementation](https://github.com/ergoplatform/ergo-appkit/pull/204)