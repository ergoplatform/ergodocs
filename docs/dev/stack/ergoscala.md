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

  def buyerContract(
    tokenId: Coll[Byte],
    tokenAmount: Long,
    buyerPk: SigmaProp
  ): ErgoContract =
    ErgoScalaCompiler.contract {
      buyerPk || {
        (OUTPUTS.nonEmpty && OUTPUTS(0).R4[Coll[Byte]].isDefined) && {
          val tokens = OUTPUTS(0).tokens
          val tokenDataCorrect = tokens.nonEmpty &&
            tokens(0)._1 == tokenId &&
            tokens(0)._2 >= tokenAmount

          val knownId = OUTPUTS(0).R4[Coll[Byte]].get == SELF.id
          tokenDataCorrect && OUTPUTS(0).propositionBytes == buyerPk.propBytes && knownId
        }
      }
    }
```

### Verified contract code in a separate method call
For verified contracts, the compilation is done differently. Formal verification is done using Stainless in [ergo-contracts](https://github.com/ergoplatform/ergo-contracts). Verified contract code can be compiled by providing the method call where contract code resides.
```scala
  def buyerContractInstance(tokenId: Coll[Byte], tokenAmount: Long, pkA: SigmaProp): ErgoContract =
    ErgoContractCompiler.compile { context: Context =>
      buyer(context, tokenId, tokenAmount, pkA)
    }
```
see [sources](https://github.com/ergoplatform/ergo-contracts/blob/63e494c9d33af25e23efea88d27f31742ad31f64/verified-contracts/src/main/scala/org/ergoplatform/contracts/AssetsAtomicExchange.scala#L150-L157)

where `buyer` method holds verified smart contract:
```scala
  def buyer(
    ctx: Context,
    tokenId: Coll[Byte],
    tokenAmount: Long,
    buyerPk: SigmaProp
  ): SigmaProp = {
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
