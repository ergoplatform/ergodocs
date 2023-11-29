---
tags:
  - Fees
  - Transaction Fees
---

# Transaction Fees in Ergo

## Dust-prevent Fees

Due to the Spam-preventing strategy, each box in Ergo should contain a minimal nanoerg, which is decided by the parameter voted by miners and the box's size. Every output box in a transaction should comply this rule. It is used for preventing dust in ergo thus alleviating spam attack to Ergo.
To be more clear, Dust-prevent Fees is not a real fee users must pay to others(for example, to the miners). It is just a secure to the box, if users do not create more new boxes, the Dust-prevent Fees can be reused by putting the same amount into the newly created single box and if the newly created box is still under your control, you are guaranteed no money loss.

## Transaction Fees

Ergo's transaction fee system is both flexible and explicit, with a minimum threshold defined by the protocol (the Dust-prevent Fees). This transaction fee is contained in a special output box and should be no less than the minimum threshold, known as the **fee box**.

/// details | Transactions
    {type: info, open: true}
Each Ergo [transaction](transaction.md) is an atomic state transition operation, destroying one or more [boxes](format.md) from the state and creating new ones. Unlike Bitcoin's implicit fee system, Ergo's fee structure is explicit, which means users should explicitly provide a fee box to the miner, which also means transaction requires a distinct output to a specific address for fees (the **fee box**). **This is in addition to the minimal ERG value required for a box to exist.**
///

## Fee Calculation

Transaction fees depend on the users willing to the speed of transaction being processed, with a minimum of **360 nanoerg per byte** (the Dust-prevent Fees). A good rule of thumb is **0.001 ERG (1,000,000 NanoErg) per box**. The more Erg you put into this fee box, the faster your transaction may be included in a block and be processed.

## Miner Transaction Prioritization

Miners prioritize transactions based on either the fee per byte or the fee per validation cost unit. These criteria are adjustable via a [voting mechanism among miners](governance.md). Nodes can sort transactions based on these metrics, settable in the [node configuration](conf-node.md#mempool).

```conf
# Mempool transaction sorting scheme ("random", "bySize", or "byExecutionCost")
mempoolSorting = "random"
```

/// details | Special Considerations
    {type: info, open: true}
While the minimal fee is a standard, miners have the discretion to select transactions based on economic incentives. This means that while transactions offering higher fees per byte or per execution unit are usually be prioritized. They can choose to include their transactions above others when [collecting storage rent](rent-fees.md).
When calculating the fee per byte or the fee per validation cost unit, miners firstly filter out the fee boxs by checking the propositionBytes in R1 register using **feeProposition**, and then sum up these boxs' Erg value, finally, the sum is divided by the transaction's size or total validation cost to get a result. The final result is the basis for sorting those transactions in mempool.
///

## Collecting Fees

Transaction fees are locked in a [contract](https://ergexplorer.com/addresses#2iHkR7CWvD1R4j1yZg5bkeDRQavjAaVPeTDFGGLZduHyfWMuYpmhHocX8GJoaieTx78FntzJbCBVL6rf96ocJoZdmWBL2fci7NqWgAirppPQmZ7fN9V6z13Ay6brPriBKYqLp1bT2Fk4FkFLCfdPpe), spendable only through a miner's script. The address used for fees is not protocol-fixed but is standard in the Ergo node reference implementation. The ErgoScript for this contract, implicitly defined in the ErgoTree, is detailed in [this method](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/f85f03cc8f063ae7f68d559371733c2b6bbc929a/sigmastate/src/main/scala/org/ergoplatform/ErgoScriptPredef.scala#L72).

```
 /**
    * Proposition that allows to send coins to a box which is protected by the following proposition:
    * prove dlog of miner's public key and height is at least `delta` blocks bigger then the current one.
    */
  def feeProposition(delta: Int = 720): ErgoTree = {
    val out = ByIndex(Outputs, IntConstant(0))
    AND(
      EQ(Height, boxCreationHeight(out)),
      EQ(ExtractScriptBytes(out), expectedMinerOutScriptBytesVal(delta, MinerPubkey)),
      EQ(SizeOf(Outputs), 1)
    ).toSigmaProp.treeWithSegregation
  }
```

And the method to extract the transaction fee method is below:

```
  private def extractFee(tx: ErgoTransaction): Long = {
    tx.outputs
      .filter(_.ergoTree == settings.chainSettings.monetary.feeProposition)
      .map(_.value)
      .sum
  }
```


## Determining Appropriate Fees

The appropriate transaction fee must meet the protocol's minimum requirements (the Dust-prevent Fees), based on the box size. But miners can also set a **minimalFeeAmount** to prevent those transactions with fee box's Erg value smaller than this **minimalFeeAmount** being into mempool. For best practices, see the [ErgoTransaction.scala](https://github.com/ergoplatform/ergo/blob/e784a70b8fabf7ae41f2ac9aa593a647f488100c/src/main/scala/org/ergoplatform/modifiers/mempool/ErgoTransaction.scala#L163).

## Confirmation Levels and Security

The recommended confirmation levels vary depending on the network hashrate. Higher hashrates reduce double-spend attack risks, thus requiring fewer confirmations.

## Related

### Babel Fees

Babel Fees enable users to pay transaction fees using tokens like SigmaUSD instead of ERG. This involves creating a new box with Babel tokens as change. The necessary ERGs for the transaction recipient and the miner's fee are sourced from this Babel fee box. For more details, see [Babel Fees documentation](babel-fees.md).

### ErgoMixer

ErgoMixe offers token mixing and dynamic fee management for consistent transaction inclusion in blocks. It uses blockchain-stored parameters for client guidance, supporting transparent and flexible fee and token management. For more insights, see this [forum post](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318/10?u=anon2020s).
