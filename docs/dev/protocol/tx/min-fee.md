---
tags:
  - Fees
  - Transaction Fees
---

# Transaction Fees in Ergo

Ergo's transaction fee system is both flexible and explicit, with a minimum threshold defined by the protocol. This minimum fee is determined by the serialized size of the box being created, known as the **fee box**.

/// details | Transactions
    {type: info, open: true}
Each Ergo [transaction](transaction.md) is an atomic state transition operation, destroying one or more [boxes](format.md) from the state and creating new ones. Unlike Bitcoin's implicit fee system, Ergo's fee structure is explicit, requiring a distinct output to a specific address for fees. **This is in addition to the minimal ERG value required for a box to exist.**
///

## Fee Calculation

Transaction fees depend on the fee box's serialized size, with a minimum of **360 nanoerg per byte**. A good rule of thumb is **0.001 ERG (1,000,000 NanoErg) per box**.

## Miner Transaction Prioritization

Miners prioritize transactions based on either the fee per byte or the validation cost unit. These criteria are adjustable via a decentralized voting mechanism among miners. Nodes can sort transactions based on these metrics, settable in the [node configuration](conf-node.md#mempool).

```conf
# Mempool transaction sorting scheme ("random", "bySize", or "byExecutionCost")
mempoolSorting = "random"
```

/// details | Special Considerations
    {type: info, open: true}
While the minimal fee is a standard, miners have the discretion to select transactions based on economic incentives. This means that while transactions offering higher fees per byte or per execution unit are usually be prioritized. They can choose to include their transactions above others when [collecting storage rent](rent-fees.md).
///

## Collecting Fees

Transaction fees are locked in a [contract](https://ergexplorer.com/addresses#2iHkR7CWvD1R4j1yZg5bkeDRQavjAaVPeTDFGGLZduHyfWMuYpmhHocX8GJoaieTx78FntzJbCBVL6rf96ocJoZdmWBL2fci7NqWgAirppPQmZ7fN9V6z13Ay6brPriBKYqLp1bT2Fk4FkFLCfdPpe), spendable only through a miner's script. The address used for fees is not protocol-fixed but is standard in the Ergo node reference implementation. The ErgoScript for this contract, implicitly defined in the ErgoTree, is detailed in [this method](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/f85f03cc8f063ae7f68d559371733c2b6bbc929a/sigmastate/src/main/scala/org/ergoplatform/ErgoScriptPredef.scala#L72).

## Determining Appropriate Fees

The appropriate fee must meet the protocol's minimum requirements, based on the box size. For best practices, see the [Ergo GitHub repository](https://github.com/ergoplatform/ergo/blob/e784a70b8fabf7ae41f2ac9aa593a647f488100c/src/main/scala/org/ergoplatform/modifiers/mempool/ErgoTransaction.scala#L163).

## Confirmation Levels and Security

The recommended confirmation levels vary depending on the network hashrate. Higher hashrates reduce double-spend attack risks, thus requiring fewer confirmations.

## Related

### Babel Fees

Babel Fees enable users to pay transaction fees using tokens like SigmaUSD instead of ERG. This involves creating a new box with Babel tokens as change. The necessary ERGs for the transaction recipient and the miner's fee are sourced from this Babel fee box. For more details, see [Babel Fees documentation](babel-fees.md).

### ErgoMixer

ErgoMixe offers token mixing and dynamic fee management for consistent transaction inclusion in blocks. It uses blockchain-stored parameters for client guidance, supporting transparent and flexible fee and token management. For more insights, see this [forum post](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318/10?u=anon2020s).
