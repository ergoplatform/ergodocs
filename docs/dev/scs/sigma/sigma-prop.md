# Sigma Propositions

Sigma Propositions (`SigmaProp`) are the core return type of every ErgoScript contract.

- `SigmaProp` values represent conditions related to the transaction that must be met to spend a specific box.
- They are similar to booleans in that they ultimately reduce to either `true` or `false` during verification.
- `SigmaProp` enables the use of Zero-Knowledge Proofs, a crucial aspect of modern cryptography and a defining privacy feature of Ergo.
- **All contracts in ErgoScript must return a `SigmaProp` value at the very end.** 
    - This final `SigmaProp` represents the complete set of conditions required to spend the box protected by the contract. Therefore, all logic within an ErgoScript contract should contribute to the outcome of this final `SigmaProp`.

`SigmaProp` values can be constructed in several ways, but two common methods are used frequently in ErgoScript contracts.

## SigmaProps From Booleans

You can create `SigmaProp` values from standard boolean expressions using the `sigmaProp` function. This allows you to define arbitrary spending conditions based on context variables, register values, etc.

```scala
{
  val mathIsHard: Boolean = (1 + 1) != 2
  sigmaProp(mathIsHard) // SigmaProp created from a boolean using the sigmaProp function
                        // What would this contract evaluate to?
}

```

## SigmaProps From Public Keys

Public Keys (represented as `GroupElement` in ErgoScript, essentially the part of your address that makes it unique) can be directly converted into `SigmaProp` values using functions like `proveDlog`. When such a `SigmaProp` is used, the contract checks if the transaction was signed by the corresponding private key. You can think of this as literally signing the transaction with your digital signature to prove authorization.

```scala
{
  // You can use the PK function to
  // hardcode an address's public key into your contract
  val myPK: SigmaProp = PK("9etXmP7D3ZkWssDopWcWkCPpjn22RVuEyXoFSbVPWAvvzDbcDXE")

  myPK
}

```

## SigmaProp Operations

Much like booleans, you can use logical operations (`&&` for AND, `||` for OR) on `SigmaProp` values to build more complex spending logic for your contract.

```scala
{
  val enoughERG = INPUTS(0).value > 1000000
  val myPK = PK("9etXmP7D3ZkWssDopWcWkCPpjn22RVuEyXoFSbVPWAvvzDbcDXE")

  sigmaProp(enoughERG) || myPK // What does this contract do? Under what conditions could such a contract be spent?
}
```



You can see in the contract above that using `||` creates two distinct spending paths (conditions under which the box can be spent).

Now that you've seen the basics, let's look at a simple ErgoScript contract example: the pin-lock contract mentioned earlier.

## Pin-lock Contract

```scala
{
  sigmaProp( INPUTS(0).R4[Coll[Byte]].get == blake2b256(OUTPUTS(0).R4[Coll[Byte]].get) )
}

```

Don't worry if you don't understand all the functions used here (`blake2b256`, `.get`); these are global functions covered elsewhere. What's happening here is:

We can spend `INPUTS(0)` (the first input box of the transaction) if and only if there exists an output box (specifically `OUTPUTS(0)`, the first output) whose register `R4` contains the Blake2b256 hash of the byte collection found in register `R4` of `INPUTS(0)`.

This contract implicitly assumes the box being spent *is* `INPUTS(0)`. For a clearer example where the box explicitly refers to itself within its own contract, consider the version below using the `SELF` context variable:

## Pin-lock Contract (with SELF)

```scala
{
  sigmaProp( SELF.R4[Coll[Byte]].get == blake2b256(OUTPUTS(0).R4[Coll[Byte]].get) )
}

```

Are these two pin-lock contracts equivalent? That is, under what spending conditions might one contract evaluate to true while the other evaluates to false? (Hint: Consider what `INPUTS(0)` refers to versus what `SELF` refers to).



> 🔗 From [Deco Education - ErgoScript Developer Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course/blob/main/Class-Documents/Class-1/Materials/Class1.MD)
