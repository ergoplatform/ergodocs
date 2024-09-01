# Basic Implementation of a Local Exchange Trading System (LETS)

## Overview

The basic blueprint of our system encompasses two contracts: an administrative contract and a trade contract. Before delving into the details, we recommend acquainting yourself with the foundational aspects of Ergo by reviewing [this ICO article](ico.md) as well as [ErgoScript](ergoscript.md) tutorials.

Despite the aforementioned recommendations, we will elucidate a few novel terms in the upcoming sections.

### Singleton Tokens and Boxes

In Ergo, when a token is minted with a value of one, it is termed a **singleton token**. Similarly, a box containing a singleton token is known as a **singleton box**.

## Administrative Contract

### Purpose

- The administrative contract oversees a singleton box that encompasses the members of the LETS system. 
- This contract facilitates the addition of new members, at a rate of one member per transaction. 
- Instead of storing members, the box merely holds a succinct digest of an authenticated data structure based on the members' directory. 
- Each member is linked with a singleton token minted during a transaction that adds the member to the directory. 
- This transaction generates a new member's box, housing the member's singleton token. 
- The trade contract safeguards the member's box. 
- Moreover, the freshly generated member's box records the initial balance in the R4 register, which in this case is zero.
- The transaction that adds a new member is obligated to validate the correctness of the directory transformation.

### Committee Management

A committee generally manages the administrative contract box, and the composition of this committee may change over time. To accommodate this, we allow the committee's logic to reside in the R5 register. For instance, if a new member is added to both the committee and the LETS system, the incoming administrative contract box would require signatures from two out of three members, while the outgoing box would require three out of four signatures. Consequently, the data within the R5 register of the input and output boxes would vary.

Below, we provide the administrative contract's code written in ErgoScript, complete with comments. Note that `userContractHash` corresponds to the hash of the trade contract. 

```scala
    val selfOut = OUTPUTS(0)
 
    // Administrative script
    val adminScript = selfOut.R5[SigmaProp].get
 
    // Confirming that the script replicates itself and the administrative script is satisfied
    val scriptIsCorrect = (selfOut.propositionBytes == SELF.propositionBytes) && adminScript
 
    // A spending transaction creates boxes for the directory, user, and fee
    val isOutputSizeCorrect = OUTPUTS.size == 3
 
    // Verifies the replication of the administrative label token 
    val isTokenOutputCorrect = (selfOut.tokens.size == 1) && (selfOut.tokens(0)._1 == letsToken)
 
    // Validates the issuance of a new token and its amount
    // OUTPUTS(0) tokens are already checked via isTokenOutputCorrect
    val issuedTokenId = INPUTS(0).id
    val userOut = OUTPUTS(1)
    val areTokenAmountsCorrect =
      (userOut.tokens.size == 1 &&
        userOut.tokens(0)._1 == issuedTokenId &&
        userOut.tokens(0)._2 == 1 &&
        OUTPUTS(2).tokens.size == 0 &&
        isTokenOutputCorrect)
 
    // Verifies that the new user is created with a zero balance
    val isUserBalanceZero  = userOut.R4[Long

].get == 0
 
    val isUserScriptProper = blake2b256(userOut.propositionBytes) == userContractHash
 
    // Validates the addition of the new token identifier to the directory
    val selfTree = SELF.R4[AvlTree].get
    val toAdd: Coll[(Coll[Byte], Coll[Byte])] = Coll((issuedTokenId, Coll[Byte]()))
    val proof = getVar[Coll[Byte]](1).get
    val updatedTree = selfTree.insert(toAdd, proof).get
    val expectedTree = selfOut.R4[AvlTree].get
    val isTreeCorrect = updatedTree == expectedTree
 
    areTokenAmountsCorrect && scriptIsCorrect && isTreeCorrect && isUserBalanceZero && isUserScriptProper      
```

The trade contract script, presented below with explanatory comments, is fairly straightforward. The contract requires that a transaction spending an exchange contract box should have at least two inputs. The first two inputs must be protected by the exchange contract script and contain LETS member tokens. To validate the legitimacy of singleton member tokens in the inputs, the transaction provides the administrative contract box as the first read-only data input and also supplies proof that the member tokens indeed belong to the directory authenticated via the R4 register of the administrative contract box. The "letsToken" in the script refers to the singleton token of the administrative box. 

```scala
  // Minimum balance allowed for a LETS trader
  val minBalance = -20000

  val lookupProof = getVar[Coll[Byte]](1).get

  // Read-only box containing the directory of LETS members
  val treeHolderBox = CONTEXT.dataInputs(0)
  val isLetsTokenProper = treeHolderBox.tokens(0)._1 == letsToken
  val membersTree = treeHolderBox.R4[AvlTree].get

  // A spending transaction takes two LETS members' boxes willing to make a trade, 
  // and returns boxes with updated balances.
  val participant0 = INPUTS(0)
  val participant1 = INPUTS(1)
  val participantOut0 = OUTPUTS(0)
  val participantOut1 = OUTPUTS(1)

  // Check that members do indeed belong to the LETS
  val token0 = participant0.tokens(0)._1
  val token1 = participant1.tokens(0)._1
  val memberTokens = Coll(token0, token1)
  val doMembersExist = membersTree.getMany(memberTokens, lookupProof).forall({ (o: Option[Coll[Byte]]) => o.isDefined })

  // Verify that changes in LETS member balances during the transaction are correct
  val initialBalance0 = participant0.R4[Long].get
  val initialBalance1 = participant1.R4[Long].get
  val finalBalance0  = participantOut0.R4[Long].get
  val finalBalance1  = participantOut1.R4[Long].get
  val balanceDifference0 = finalBalance0 - initialBalance0
  val balanceDifference1 = finalBalance1 - initialBalance1
  val areBalanceDifferencesCorrect = balanceDifference0 == -balanceDifference1
  val areBalancesCorrect = (finalBalance0 > minBalance) && (finalBalance1 > minBalance) && areBalanceDifferencesCorrect

  // Check that member boxes retain their scripts.
  val isScript0Preserved = participantOut0.propositionBytes == participant0.propositionBytes
  val isScript1Preserved = participantOut1.propositionBytes == participant1.propositionBytes
  val areScriptsPreserved = isScript0Preserved && isScript1Pres

erved

  // Protection specific to member boxes
  val selfPubKey = SELF.R5[SigmaProp].get

  selfPubKey && isLetsTokenProper && doMembersExist && areBalanceDifferencesCorrect && areScriptsPreserved
```

Please note that both the administrative and trade contracts can be modified in various ways to create new systems with different characteristics.