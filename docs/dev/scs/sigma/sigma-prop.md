## Sigma Propositions

> 🔗 From [Deco Education - ErgoScript Developer Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course/blob/main/Class-Documents/Class-1/Materials/Class1.MD)


Sigma Propositions are the core of every single ErgoScript contract
SigmaProps represent some conditions about the transaction that must be met in order to spend a certain box.
They are quite similar to booleans, in that they may be reduced into two values, `true` or `false`.
SigmaProps enable the usage of Zero-Knowledge Proofs, an important part of modern-day cryptography and one of the defining features of Ergo in terms of its privacy

**All contracts in ErgoScript return a Sigma Proposition at the very end**. This SigmaProp represents the conditions needed
to spend the box protected by your contract. For this reason, all the code you make within an ErgoScript contract should affect the outcome of your Sigma Proposition in some way.

SigmaProps come in a few different forms, but there are two main ways you will see them in ErgoScript contracts.

### SigmaProps From Booleans

You may create SigmaProps from booleans using the `sigmaProp` function. This
allows you to define arbitrary spending conditions for any contract.

```scala
{
  val mathIsHard: Boolean = (1 + 1) != 2
  sigmaProp(mathIsHard) // SigmaProp created from a boolean using the sigmaProp function
                        // What would this contract evaluate to?
}

```

### SigmaProps From Public Keys

Public Keys (Essentially, the part of your address that makes it different from everyone else's)
are also SigmaProps. When a public key is passed as a SigmaProp, your contract checks whether or not the given PK is the one that signed the transaction
You may think of signing a transaction, as quite literally signing it with your signature to prove
that the transaction was authorized by you.

```scala
{
  // You can use the PK function to
  // hardcode an address's public key into your contract
  val myPK: SigmaProp = PK("9etXmP7D3ZkWssDopWcWkCPpjn22RVuEyXoFSbVPWAvvzDbcDXE")

  myPK
}

```

### SigmaProp Operations

Much like booleans, you may use logical operations on SigmaProps in order to build more complex spending logic for your contract

```scala
{
  val enoughERG = INPUTS(0).value > 1000000
  val myPK = PK("9etXmP7D3ZkWssDopWcWkCPpjn22RVuEyXoFSbVPWAvvzDbcDXE")

  sigmaProp(enoughERG) || myPK // What does this contract do? Under what conditions could such a contract be spent?
}

```

You can see in the above contract that usage of `||` actually creates two spending paths for the given contract.

Now you've seen the basics, for the end of this section, lets look at a simple ErgoScript contract, the pin-lock we mentioned earlier

### Pin-lock Contract

```scala
{
  sigmaProp( INPUTS(0).R4[Coll[Byte]].get == blake2b256(OUTPUTS(0).R4[Coll[Byte]].get) )
}

```

Don't worry if you don't understand the functions used here, these are global functions that we will get into the next section.
What's happening here is this:

We may spend Input 0 of this transaction if and only if there exists an output whose `R4` (register 4)
contains the hash of the collection of bytes found in R4 of the Input.
This contract refers to itself as `INPUTS(0)`, for a more clear example, look at the following, where the box being spent refers to itself within its own contract:

### Pin-lock Contract (with SELF)

```scala
{
  sigmaProp( SELF.R4[Coll[Byte]].get == blake2b256(OUTPUTS(0).R4[Coll[Byte]].get) )
}

```

Are these two contracts equivalent?
That is, are there any spending conditions that exist in which one contract could evaluate to true, and one could evaluate to false?



