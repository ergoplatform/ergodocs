# ErgoScala compiler

Compiler for Ergo smart contracts written in ErgoScala (a subset of Scala). Compilation from formally verified smart contracts from [ergo-contracts](https://github.com/ergoplatform/ergo-contracts) is supported.

# Usage

```scala
libraryDependencies += "org.ergoplatform" %% "ergo-scala-compiler" % "0.0.0-32-aaadbee1-SNAPSHOT",
```

Compilation results in producing `ErgoContract` that provides:

- `ErgoTree` instance, Ergo's IR, which is used to define logical propositions protecting boxes (a generalization of coins) in the Ergo blockchain. Serialized ErgoTree expressions are written into UTXO boxes and then evaluated by the transaction verifier;
- Scala anonymous function that when called with a `Context` parameter evaluates(reduces) the contract code to a sigma property. It allows us to "call" the contract code without loading up the interpreter.

## Example

### Contract code in  `contract` call
Ergo contract code can be compiled with `ErgoScalaCompiler.contract` call:

```scala
import org.ergoplatform.compiler.ErgoScalaCompiler

// Define a function that takes token id, amount, and buyer's public key as input parameters and returns an ErgoContract.
def buyerContract(
  tokenId: Coll[Byte],
  tokenAmount: Long,
  buyerPk: SigmaProp
): ErgoContract =
  ErgoScalaCompiler.contract { // Compile the contract using the ErgoScalaCompiler library.
    // If the buyer's public key is valid, the contract can be spent without any additional conditions.
    buyerPk || {
      // Otherwise, some additional conditions must be met.
      // Check if there are any outputs and the first output has a non-empty R4 register.
      (OUTPUTS.nonEmpty && OUTPUTS(0).R4[Coll[Byte]].isDefined) && {
        // Get the tokens of the first output and verify that the specified token id and amount are correct.
        val tokens = OUTPUTS(0).tokens
        val tokenDataCorrect = tokens.nonEmpty &&
          tokens(0)._1 == tokenId &&
          tokens(0)._2 >= tokenAmount

        // Check if the first output's R4 register matches the id of the current box (SELF) and its proposition bytes matches the buyer's public key.
        val knownId = OUTPUTS(0).R4[Coll[Byte]].get == SELF.id
        tokenDataCorrect && OUTPUTS(0).propositionBytes == buyerPk.propBytes && knownId
      }
    }
  }

```

### Verified contract code in a separate method call
For verified contracts, the compilation is done differently. Formal verification is done using Stainless in [ergo-contracts](https://github.com/ergoplatform/ergo-contracts). Verified contract code can be compiled by providing the method call where contract code resides.

```scala
/**
 * This function creates a new instance of the buyer contract, compiled with the provided parameters.
 * @param tokenId - the id of the token to be exchanged
 * @param tokenAmount - the amount of tokens to be exchanged
 * @param pkA - the public key of the buyer
 * @return a compiled instance of the buyer contract
 */
def buyerContractInstance(tokenId: Coll[Byte], tokenAmount: Long, pkA: SigmaProp): ErgoContract =
  ErgoContractCompiler.compile { context: Context =>
    buyer(context, tokenId, tokenAmount, pkA)
  }

```

see [sources](https://github.com/ergoplatform/ergo-contracts/blob/63e494c9d33af25e23efea88d27f31742ad31f64/verified-contracts/src/main/scala/org/ergoplatform/contracts/AssetsAtomicExchange.scala#L150-L157)

where `buyer` method holds verified smart contract:
```scala
/**
  * Function that returns a SigmaProp indicating whether a buyer can spend the funds locked in a box.
  * A buyer can spend the funds if either the buyerPk is provided, or if the OUTPUTS have a valid tokenData
  * for the given tokenId and the box id is known.
  *
  * @param ctx The context where the function is being evaluated.
  * @param tokenId The Coll[Byte] representing the token id.
  * @param tokenAmount The amount of tokens needed.
  * @param buyerPk The SigmaProp of the buyer.
  * @return A SigmaProp indicating whether a buyer can spend the funds locked in a box.
  */
def buyer(ctx: Context, tokenId: Coll[Byte], tokenAmount: Long, buyerPk: SigmaProp): SigmaProp = {
  import ctx._
  buyerPk || {
    (OUTPUTS.nonEmpty && OUTPUTS(0).R4[Coll[Byte]].isDefined) && {
      val tokens = OUTPUTS(0).tokens
      val tokenDataCorrect = tokens.nonEmpty &&
        tokens(0)._1 == tokenId &&
        tokens(0)._2 >= tokenAmount

      val knownId = OUTPUTS(0).R4[Coll[Byte]].get == SELF.id
      tokenDataCorrect &&
      OUTPUTS(0).propositionBytes == buyerPk.propBytes &&
      knownId
    }
  }
}
```

see [sources](https://github.com/ergoplatform/ergo-contracts/blob/63e494c9d33af25e23efea88d27f31742ad31f64/verified-contracts/src/main/scala/org/ergoplatform/contracts/AssetsAtomicExchange.scala#L24-L44)
