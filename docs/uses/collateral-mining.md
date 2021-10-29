As some of you know, I've been working on my own collateral-based mining pool.  This will just be another option along with @mhs_sam's pool.  I thought I would post my collateral box script here for public review, in case I've missed any obvious issues:
```
    {
      val poolReward = 67500000000L
      {
        // Case 1: block was mined by alice.
        // Either: (a) we have 1 output of value poolReward,
        // or: (b) we have 2 outputs, 1st is poolReward, 2nd goes to self.
        decodePoint(CONTEXT.minerPubKey) == alice &&
        HEIGHT > SELF.creationInfo._1 &&
        OUTPUTS(0).value == poolReward && {
          OUTPUTS.size == 1 || {
            OUTPUTS.size == 2 &&
            OUTPUTS(1).propositionBytes == SELF.propositionBytes &&
            OUTPUTS(1).creationInfo._1 == HEIGHT
          }
        }
      } || {
        // Case 2: anyone can top-up with more collateral funds.
        OUTPUTS(0).propositionBytes == SELF.propositionBytes &&
        OUTPUTS(0).creationInfo._1 >= SELF.creationInfo._1 &&
        OUTPUTS(0).value > SELF.value
      } || {
        // Case 3: alice can withdraw collateral at any time.
        proveDlog(alice)
      }
    }
```

*Edit: fixed a bug that would have allowed chained spends in a single block.*

The main limitation of this approach is that only one unspent collateral box should exist at any time for a given miner public key, otherwise a pool can spend more than one box in the same block and claim a multiple of the reward.  However, I think this is reasonable and it becomes too complex if miners have to create special signatures to avoid this.  The top-up mechanism (case 2) allows anyone to top-up a given collateral box.

Another small point is that the pool reward could be adjusted to be a bit under 67.5 ERG to provide additional incentives, though I would note that the miner already gets to keep all the fees if they mine a block.

This collateral mechanism was proposed here by @scalahub back in July 2019!

https://www.ergoforum.org/t/creating-an-ergo-mining-pool/42

The paper by @kushti and @scalahub is [here](https://eprint.iacr.org/2020/044).

Full discussion [here](https://www.ergoforum.org/t/collateral-script-for-pool-mining/200)