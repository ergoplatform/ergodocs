---
tags:
  - EIP
---

# EIP-0022: Auction Contract

> 🔗 From [EIP-0022:](https://github.com/ergoplatform/eips/blob/master/eip-0022.md)

## Motivation

Decentralized auctioning of any kind of tokens (artwork, share tokens, etc.) is an important part of any blockchain. This EIP is proposing the auction contract with various features listed in the [Design](#design) section

## Design

This proposed contract allows any kind of tokens to be auctioned while supporting the following features:  

- Any token as the auction's currency alongside ERG
- "Buy it now" which allows a buyer to instantly buy the auctioned token by paying the predefined amount in the auction's currency
- Auction duration as timestamp which is much more precise than block height and is independent of the network difficulty
- Auto extending the duration near the end of the auction based on a global config
- Minimum bid step - each bidder has to increase the previous bid at least by this amount
- Royalty - The original owner (whomever issued the token) gets a share of the auction every time his/her token is auctioned using a global config

## The contract

```scala
{
  // R4: The seller's ergo tree
  // R5: Current bidder's ergo tree
  // R6: (Minimum bid, minimum step)
  // R7: The auction's end time in timestamp
  // R8: The auction's "Buy it now" amount. -1 if it is not enabled.
  // R9: Auction info that is needed for UI/UX purposes - stringfied json encoded as Coll[Byte]:
  //     - initialBid: The auction's initial bid
  //     - startTime: The auction's start time
  //     - description: The auction's description
  //     - Any other info needed in the future
  //
  // tokens(0): auctioned token
  // tokens(1): current bid for non-ERG auctions - doesn't exist otherwise
  //
  // dataInputs(0): Auction house configuration - contains configs like UI fee and artist fee
  //     - R4: UI fee in thousand, e.g. 10 for 1% or 5 for 0.5%
  //     - R5: UI implementor's ergo tree
  //     - R6: Maximum miner fee for withdrawal
  //     - R7: Extend configuration as a Coll[Long] with two values (extendThreshold, extendNum)
  //             e.g., (30 * 60 * 1000L, 40 * 60 * 1000L) to extend the duration for 40min if 30min is left when the bid is placed

  // originalIssuanceBox: Spent box with ID equal to the NFT ID
  //     - R4: Royalty percentage - 0 if empty
  //     - R5: Artist address

  val seller = SELF.R4[Coll[Byte]].get
  val currBidder = SELF.R5[Coll[Byte]].get
  val minBid = SELF.R6[Coll[Long]].get(0)
  val minStep = SELF.R6[Coll[Long]].get(1)
  val endTime = SELF.R7[Long].get
  val buyItNowAmount = SELF.R8[Long].get

  // auction currency can be any token like SigUSD
  val auctionCurrency = if (SELF.tokens.size > 1) SELF.tokens(1)._1
                        else Coll[Byte]()
  val isCurrencyERG = auctionCurrency.size == 0
  val getBoxVal = {(b: Box) => {
     if (isCurrencyERG) b.value
     else {
       if (b.tokens.size == 1 && b.tokens(0)._1 == auctionCurrency) b.tokens(0)._2
       else if (b.tokens.size == 2 && b.tokens(1)._1 == auctionCurrency) b.tokens(1)._2
       else 0L
     }
  }}

  val currBid = getBoxVal(SELF)

  val auctionConfig = CONTEXT.dataInputs(0)

  // auction is not finished, a bid is being placed
  val isNextBid = {
     val extendConfig = auctionConfig.R7[Coll[Long]]
     val extendThreshold = extendConfig.get(0)
     val extendNum = extendConfig.get(1)
     // we extend the auction end time by extendNum if the bid is placed near the very end (extendThreshold)
     val newEndTime = if (endTime - CONTEXT.preHeader.timestamp <= extendThreshold) endTime + extendNum
                      else endTime


     val newSelf = OUTPUTS(0) // new auction box
     val oldBidRefundBox = OUTPUTS(1) // refund box

     val isUsingBuyItNow = buyItNowAmount != -1 && getBoxVal(newSelf) >= buyItNowAmount

     // as a general check, ERG value can not be less than the current
     newSelf.value >= SELF.value &&
     // auction is not finished
     CONTEXT.preHeader.timestamp < endTime &&
     // preserve auctioned tokens
     newSelf.tokens(0) == SELF.tokens(0) &&
     // correct value and contract for the new box
     (getBoxVal(newSelf) >= getBoxVal(SELF) + minStep || getBoxVal(SELF) < minBid || isUsingBuyItNow) &&
     getBoxVal(newSelf) >= minBid &&
     newSelf.propositionBytes == SELF.propositionBytes &&
     // shouldn't be able to add tokens - will change the currency from ERG to a worthless token
     SELF.tokens.size == newSelf.tokens.size &&
     // currency must be the same
     // refund the previous bidder
     oldBidRefundBox.propositionBytes == currBidder &&
     getBoxVal(oldBidRefundBox) >= currBid &&
     // preserve the auction config
     newSelf.R4[Coll[Byte]].get == seller &&
     // just making sure that the new R5's type is Coll[Byte]
     newSelf.R5[Coll[Byte]].get.size > 0 &&
     newSelf.R6[Coll[Long]].get.size == 2 &&
     newSelf.R6[Coll[Long]].get(0) == minBid &&
     newSelf.R6[Coll[Long]].get(1) == minStep &&
     newSelf.R7[Long].get == newEndTime &&
     newSelf.R8[Long].get == buyItNowAmount &&
     newSelf.R9[Coll[Byte]] == SELF.R9[Coll[Byte]]

  }

  // either auction has ended due to time or "Buy it now" is being used
  val isFinishedWithBid = {
     val winnerBox = OUTPUTS(0)
     val auctionFeeBox = OUTPUTS(1)
     val sellerBox = if (OUTPUTS.size < 3) SELF
                         else OUTPUTS(2)
     val artistRoyalty = if (OUTPUTS.size < 4) SELF
                         else OUTPUTS(3)
     val originalIssuanceBox = if (auctionFeeBox.R4[Box].isDefined) auctionFeeBox.R4[Box].get
                               else OUTPUTS(OUTPUTS.size - 1)

     val auctionFee = (currBid * auctionConfig.R4[Int].get) / 1000
     val auctionFeeTo = auctionConfig.R5[Coll[Byte]].get // ui implementor's ergo tree

     val artistSharePerc = if (originalIssuanceBox.R4[Int].isDefined) max(originalIssuanceBox.R4[Int].get, 0)
                           else 0
     val artistShare = (currBid * artistSharePerc) / 1000

     val maxFee = auctionConfig.R6[Long].get
     // if currency is not ERG, then nothing has to be deducted from it for miner fee. Otherwise, 2 * maxFee will be deducted
     val minerFeeInCurrency = if (isCurrencyERG) maxFee * 2 // one maxFee for the miner fee and one for the seller box
                              else 0L

     val artistGetsHisShare = {
       artistShare == 0L || {
         blake2b256(originalIssuanceBox.bytes) == SELF.tokens(0)._1 && // the same ID as the NFT - the integrity of the box is also ensured with this line
         getBoxVal(artistRoyalty) >= artistShare && // gets at least the percentage defined in the auction config box
         artistRoyalty.propositionBytes == originalIssuanceBox.propositionBytes // goes to the artist
       }
     }

     val buyItNow = (currBid >= buyItNowAmount && buyItNowAmount != -1)

     val outSize = if (artistShare == 0L) 4
                   else 5

     // either auction is finished or "Buy it now" is used
     (CONTEXT.preHeader.timestamp >= endTime || buyItNow) &&
     getBoxVal(auctionFeeBox) >= auctionFee &&
     auctionFeeBox.propositionBytes == auctionFeeTo &&
     winnerBox.tokens(0) == SELF.tokens(0) &&
     winnerBox.propositionBytes == currBidder &&
     getBoxVal(sellerBox) >= currBid - auctionFee - artistShare - minerFeeInCurrency &&
     sellerBox.propositionBytes == seller &&
     artistGetsHisShare &&
     OUTPUTS.size == outSize
  }

  // in this case, there is no winner and the seller doesn't need to pay any fee to the auction house or the artist
  val isFinishedWithoutBid = {
     val maxFee = auctionConfig.R6[Long].get
     val minerFeeInCurrency = if (isCurrencyERG) maxFee
                              else 0L
     currBid < minBid &&
     CONTEXT.preHeader.timestamp >= endTime &&
     OUTPUTS.size == 2 &&
     OUTPUTS(0).tokens(0) == SELF.tokens(0) &&
     OUTPUTS(0).propositionBytes == seller &&
     getBoxVal(OUTPUTS(0)) >= currBid - minerFeeInCurrency
  }

  val validConfig = auctionConfig.tokens(0)._1 == AUCTION_CONFIG_TOKEN_ID
  sigmaProp((isNextBid || isFinishedWithBid || isFinishedWithoutBid) && validConfig)
}
```
