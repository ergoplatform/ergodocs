
## Basic Implementation

Our reference implementation is simple and consists of two contracts: a management contract and an exchange contract. We skip Ergo preliminaries, so please read [the ICO article](https://github.com/ergoplatform/ergo/wiki/An-ICO-Example-On-Top-Of-Ergo) and ErgoScript tutorials([basic](https://ergoplatform.org/docs/ErgoScript.pdf) and [advanced](https://ergoplatform.org/docs/sigmastate_protocols.pdf)) for starters.

Nevertheless, we will introduce a couple of new terms in the following sentences.

If a token is issued with an amount equal to one, we call it the **singleton token**. Similarly, a box that contains the singleton token is called the **singleton box**.

- The management contract controls a singleton box that holds members of the LETS system. 
- The contract enables the adding of new members at the pace of one member per transaction. 
- The box is not storing members but only a small digest of authenticated data structure built on top of the members' directory. 
- A member is associated with a singleton token issued in a transaction that adds the member to the directory. 
- The transaction creates a new member's box containing the member's singleton token. 
- The exchange contract protects the member's box. 
- Also, the newly created member's box has the initial balance written down into the R4 register, and the balance is equal to zero in our example.
- The transaction creating a new member must provide proof of correctness for directory transformation.

The management contract box is controlled usually by a committee, and the committee could evolve over time. To support that, we allow committee logic to reside in the register R5. For example, assume that a new committee member has been added along with a new LETS member, the input management contract box requires 2-out-of-3 signatures, and the output box requires 3-out-of-4 signatures. In this case, the contents of the R5 register in the input and the output box would differ.

The management contract code in ErgoScript with comments is provided below. Please note that  `userContractHash` is about the exchange contract hash. 

```scala
    val selfOut = OUTPUTS(0)
 
    // Management script
    val managementScript = selfOut.R5[SigmaProp].get
 
    // The management script template is replicating self, and management script is satisfied
    val scriptCorrect = (selfOut.propositionBytes == SELF.propositionBytes) && managementScript
 
    // A spending transaction is creating boxes for directory, user, fee.
    val outsSizeCorrect = OUTPUTS.size == 3
 
    // Checks that the management label token is replicating self
    val outTokenCorrect = (selfOut.tokens.size == 1) && (selfOut.tokens(0)._1 == letsToken)
 
    // Checks that new token is issued, and its amount is correct
    // OUTPUTS(0) tokens already checked via outtokenCorrect
    val issuedTokenId = INPUTS(0).id
    val userOut = OUTPUTS(1)
    val correctTokenAmounts =
      (userOut.tokens.size == 1 &&
        userOut.tokens(0)._1 == issuedTokenId &&
        userOut.tokens(0)._2 == 1 &&
        OUTPUTS(2).tokens.size == 0 &&
        outTokenCorrect)
 
    // Checks that the new user has been created with the zero balance
    val zeroUserBalance  = userOut.R4[Long].get == 0
 
    val properUserScript = blake2b256(userOut.propositionBytes) == userContractHash
 
    // Checks that the new token identifier has been added to the directory
    val selfTree = SELF.R4[AvlTree].get
    val toAdd: Coll[(Coll[Byte], Coll[Byte])] = Coll((issuedTokenId, Coll[Byte]()))
    val proof = getVar[Coll[Byte]](1).get
    val modifiedTree = selfTree.insert(toAdd, proof).get
    val expectedTree = selfOut.R4[AvlTree].get
    val treeCorrect = modifiedTree == expectedTree
 
    correctTokenAmounts && scriptCorrect && treeCorrect && zeroUserBalance && properUserScript       
    correctTokenAmounts && scriptCorrect && treeCorrect && zeroUserBalance && properUserScript correctTokenAmounts && scriptCorrect && treeCorrect && zeroUserBalance && properUserScript      
```

The exchange contract script is fairly straightforward and provided below, along with comments describing its logic. The contract assumes that a spending transaction for an exchange contract box receives at least two inputs, and the first two inputs should be protected by the exchange contract script and contain LETS member tokens. To check
that singleton member tokens in the inputs do indeed belong to the LETS system; a spending transaction provides the management
contract box as the first read-only data input and also should provide proof that the member tokens do belong to 
the directory authenticated via the R4 register of the management contract box. "letsToken" in the script is about
the singleton token of the management box. 

```scala
  // Minimal balance allowed for LETS trader
  val minBalance = -20000

  val lookupProof = getVar[Coll[Byte]](1).get

  // The read-only box which contains directory of LETS members
  val treeHolderBox = CONTEXT.dataInputs(0)
  val properLetsToken = treeHolderBox.tokens(0)._1 == letsToken
  val membersTree = treeHolderBox.R4[AvlTree].get

  // A spending transaction is taking two boxes of LETS members willing to make a deal,
  // and returns boxes with modified balances.
  val participant0 = INPUTS(0)
  val participant1 = INPUTS(1)
  val participantOut0 = OUTPUTS(0)
  val participantOut1 = OUTPUTS(1)

  //Check that members do indeed belong to the LETS
  val token0 = participant0.tokens(0)._1
  val token1 = participant1.tokens(0)._1
  val memberTokens = Coll(token0, token1)
  val membersExist = membersTree.getMany(memberTokens, lookupProof).forall({ (o: Option[Coll[Byte]]) => o.isDefined })

  // Check that LETS member balance changes during the deal are correct
  val initialBalance0 = participant0.R4[Long].get
  val initialBalance1 = participant1.R4[Long].get
  val finishBalance0  = participantOut0.R4[Long].get
  val finishBalance1  = participantOut1.R4[Long].get
  val diff0 = finishBalance0 - initialBalance0
  val diff1 = finishBalance1 - initialBalance1
  val diffCorrect = diff0 == -diff1
  val balancesCorrect = (finishBalance0 > minBalance) && (finishBalance1 > minBalance) && diffCorrect

  // Check that member boxes save their scripts.
  // todo: optimization could be made here
  val script0Saved = participantOut0.propositionBytes == participant0.propositionBytes
  val script1Saved = participantOut1.propositionBytes == participant1.propositionBytes
  val scriptsSaved = script0Saved && script1Saved

  // Member-specific box protection
  val selfPubKey = SELF.R5[SigmaProp].get

  selfPubKey && properLetsToken && membersExist && diffCorrect && scriptsSaved
```

> Note that we can modify both contracts in many ways to get new systems with different properties. 




