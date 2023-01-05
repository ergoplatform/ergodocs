## Trustless LETS

LETS involves several parties that agree to use some form of "local currency", usually pegged to the country's main currency at a 1:1 rate. Assume that our LETS is based in a European country where the currency is Euros, and the exchange is done in "local Euros", which are considered equivalent to national Euros.

Each user in LETS has an account, which contains the LETS balance of that user (in Local Euros). On joining, each user has a balance of zero. The balance is stored in a (possibly decentralized) ledger. An interesting feature of LETS is that a user with zero balance can also "withdraw" money, but only for paying another LETS user. At any time, the sum of LETS balances of all the users is zero.

As an example, Alice, with zero balance, wishes to purchase one litre of milk for 2 Euros from Bob, a member of LETS with zero balance. She transfers 2 Euros from her account to Bob's, making her balance -2 and Bob's +2. Bob can then transfer some or all of his balance to another LETS user in exchange for goods or services.

### Implementation

Since we desire a trustless LETS, we cannot depend on any trusted group of people to admit users. Note that we will still have a committee to perform tasks such as setting up the LETS parameters (local currency, the maximum number of members, etc.) and consuming any joining fee.

We will only assume a trusted _pricing oracle_ that gives the current rate of euros to ergs identified by some global id (`rateTokenID`) and a _singleton box_ containing exactly one token with this id. A singleton box, described [here](/blog/2019_04_22-lets/), is a box containing a _singleton token_, i.e., a token with only one quantity in existence. This box also contains the rate of ergs to euros at any given period. The rate is updated by spending this box and creating another singleton box with the new rate.

At any instance, our LETS is uniquely defined by a global _token box_ that contains some _membership tokens_ with id `letsTokenID`. This box defines the LETS parameters such as the location, the currency unit, `rateTokenID`, etc. The token box is initially started with, say, 10000 membership tokens. Users can spend this box and create their individual _LETS boxes_ as outputs of the transaction, such that each such output has exactly one membership token. The balance membership tokens are put in a newly created token box. 

A LETS box represents a LETS member and must be used in every transaction. For simplicity, this article restricts all LETS transactions to involve exactly two members, one being the sender and the other the receiver, such that the sender transfers some positive amount of the LETS currency (local euros) to the receiver. Such a transaction consumes the member's boxes and recreates them as output with the updated balance.   

#### Variants

To prevent spam and DDoS attacks, we require at least a minimum number of ergs (`minErgsToJoin`) to be locked in the newly created member's box. The ergs will be locked until at least the `minWithdrawTime` number of blocks has been mined. A box can have a negative LETS balance up to the amount that can be covered by the locked ergs (using the rate at the time of trade).

```scala
// a tokenBox stores the membership tokens and has this script
val tokenBox = OUTPUTS(0) // the first output must also be a tokenBox
// first output contains remaining LETS tokens

def isLets(b:Box) = { // returns true if b is a LETS box
   // A LETS box must have exactly 1 membership token in tokens(0)
   b.tokens(0)._1 == letsTokenID && b.tokens(0)._2 == 1 &&
   blake2b256(b.propositionBytes) == memberBoxScriptHash &&
   SELF.R4[Long].get == 0 && // start the box with zero LETS balance
   b.value >= minErgsToJoin && // the box must contain some minimum ergs
   b.R6[Long].get <= HEIGHT // store the creation height in R6
}

// how many lets boxes creared in the tx
val numLetsBoxes = OUTPUTS.filter({(b:Box) => isLets(b)}).size

// In the transaction following is preserved for the token box ...
tokenBox.tokens(0)._1 == SELF.tokens(0)._1 &&                //  token id
tokenBox.tokens(0)._2 == SELF.tokens(0)._2 - numLetsBoxes && //  quantity
tokenBox.propositionBytes == SELF.propositionBytes           //  script
```

A LETS member's box is protected by the script below, whose hash `memberBoxScriptHash` is used above. The script requires exactly one (sender, receiver) pair per transaction. 

```scala
val validRateOracle = CONTEXT.dataInputs(0).tokens(0)._1 == rateTokenID
val rate = CONTEXT.dataInputs(0).R4[Int].get
val inBalance = SELF.R4[Long].get    // LETS balance of current input
val pubKey = SELF.R5[SigmaProp].get  // owner of the current input
val createdAt = SELF.R6[Long].get    // height at which current input was mined

val index = getVar[Int](0).get       // index of the corresponding output
val out = OUTPUTS(index)
val outBalance = out.R4[Long].get    // LETS balance of the output

// A LETS box is one that has the same script as the current box
val isMemberBox = {(b:Box) => b.propositionBytes == SELF.propositionBytes}
val letsInputs = INPUTS.filter(isMemberBox)    // all LETS input boxes
val letsOutputs = OUTPUTS.filter(isMemberBox)  // all LETS output boxes

// The current input belongs to the receiver if its LETS balance increases
// There may be some ergs in receiver's input box. We need to ensure that
// the receiver's output box also contains the same amount of ergs as input
val receiver = outBalance > inBalance && out.value == SELF.value

val getBalance = {(b:Box) => b.R4[Long].get} // returns LETS balance of a box

val letsBalIn = letsInputs.map(getBalance).fold(0L, {(l:Long, r:Long) => l + r})
val letsBalOut = letsOutputs.map(getBalance).fold(0L, {(l:Long, r:Long) => l + r})

// sender box can contain less amount of ergs (sender may withdraw ergs provided 
// that any negative LETS balance of sender in out is backed by sufficient ergs)
val correctErgs = out.value >= -outBalance * rate && (
  out.value >= SELF.value || SELF.R6[Long].get + minWithdrawTime > HEIGHT
)

// for the receiver, we don't touch the erg balance, 
// since a receiver is not actively involved in the transaction

inBalance != outBalance && // some transaction should occur; balance must change
SELF.tokens(0)._1 == letsTokenID && // the current input has the right token
out.tokens(0)._1 == letsTokenID && // corresponding output has the right token
validRateOracle &&          // oracle providing rate has the correct "rate token"
letsBalIn == letsBalOut &&  // total LETS balance is preserved in the transaction
letsInputs.size == 2 && letsOutputs.size == 2 &&  // only two LETS inputs, outputs
out.propositionBytes == SELF.propositionBytes &&  // out is a LETS box ...
out.R5[SigmaProp].get == pubKey &&                // ... with the right pub key
out.R6[Long].get == SELF.R6[Long].get &&          // ... and creation height
(receiver ||              // either current input belongs to receiver ...
  (pubKey && correctErgs) // ... or out has correct ergs and tx has signature
)
```

The transaction spending a box with the above script requires:
- The sum of the LETS balance of inputs and outputs is preserved
- There are two LETS inputs and two LETS outputs
- The public keys (stored in R5) are preserved in the corresponding output
- The creation height (stored in R6) be preserved in the corresponding output

> **Some public key is the receiver if the LETS balance of its output is higher than that of its input.**

The last condition requires that either the input and output boxes belong to the receiver (so that the ergs are preserved), or, if they belong to the sender, a signature is provided. The required number of ergs backs the output if its LETS balance is negative. Furthermore, it requires that the sender's ergs balance cannot be reduced until at least the `minWithdrawTime` number of blocks have been mined after the ergs were locked.

Compared to the managed LETS, the above system has the following differences:

* **No membership record**: Unlike the managed LETS, We don't store any membership information here. 
* **Multiple-boxes**: A person can create multiple membership boxes, which is permitted. We only require that any negative balance be backed by the corresponding number of ergs locked. 

##### LETS-1: Zero Sum, Collateral

The above is the basic variant, which we call **LETS-1**. It has the following features:

* **Time-locked Joining-Fee**: To prevent spam attacks, a member has to pay a certain minimum fee in ergs at the time of joining. This fee is refundable but only after a predefined number of blocks.
* **Zero-Sum**: The sum of the LETS balances of all member boxes is zero. Member boxes can have a negative balance as long as it is within a certain limit.
* **Collateral**: For the sender's output, ergs are used as collateral to cover the negative LETS balance at the current exchange rate.

The following are some variations of LETS-1.

##### LETS-2: Zero Sum, No collateral

(A slight variation of LETS-1)

* **Non-refundable joining fee**: Like LETS-1, a joining fee is needed to prevent spam attacks. However, unlike LETS-1, this fee is non-refundable and must be sent to some predefined management committee.
* **Zero-Sum**: As in LETS-1.

##### LETS-3: Positive-Sum, Collateral


The above two variants require the total LETS balance to be always zero. Here we consider a positive value for this sum. In particular, this variant has the following properties:

* **Time-locked Joining Fee**: As in LETS-1.
* **Positive Sum**: The LETS balance of every member must always be non-negative, which ensures that the sum of the LETS balances of all member boxes is positive. The initial LETS balance is set to a positive value based on the joining fee at the current rate, capped to some maximum value.
* **Collateral**: Any reduction in the ergs balance of the sender must be accompanied by a reduction of the corresponding LETS balance at the current exchange rate. 

We can also allow topping up the LETS balance during a transaction by adding the equivalent amount of ergs. 

##### LETS-4: Positive-Sum, No collateral

This is similar to LETS-3 but with some small variations:

* **Non-refundable Joining Fee**: As in LETS-2
* **Positive-Sum**: As in LETS-3

The following table summarizes the variants:

|   |Zero Sum|Positive Sum|
|---|---|---|
|**Collateral**|LETS-1|LETS-3|
|**No collateral**|LETS-2|LETS-4|

We considered LETS transactions involving a single sender-receiver pair. More advanced models can allow multiple senders and receivers and need not be in pairs. 


**Crossing the last mile**


*The need to reform the global financial system has been clear since the last crisis in 2008. Now, COVID-19 has forced our hands. We cannot delay, and the best way to start is from the grassroots.*

As lockdowns across the world effectively shut down whole sectors and a large part of the economy, we are entering a new era at a breakneck pace. Central banks are taking unprecedented action in the form of money printing, but, just like last time around, they will almost certainly fail at the 'last mile' (intentionally or otherwise): while their efforts will benefit the financial sector and the wealthy, the funds will not reach those small businesses and individuals who need them the most.

Technology like the Ergo platform can address this problem efficiently, building bridges into and within our local economies without the need for commercial or central banks. A key principle of Ergo, and one stated in the white paper, is that it is for regular people. The developers have spent considerable time building technology that can be applied to real-world use cases. (This is the idea behind '[Smart contracts for the people](http://chepurnoy.org/blog/2018/10/smart-contracts-for-the-people/)', for example.)

