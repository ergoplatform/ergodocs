# Debugging

ErgoScript is a text, usually placed in strings (in string literals, to be precise). It is not possible to put a breakpoint in strings. 

However, ErgoScript is a subset of Scala (by design), and there is a comprehensive test suite (see SigmaDslSpecification) that checks ErgoScript - Scala equivalence.
[There is an example in the sigmastate-interpreter repo](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/83dc78b5c80b11dcab41ba8aa75a0a8a650e6473/sigmastate/src/test/scala/sigmastate/utxo/examples/)

`AssetsAtomicExchange.scala#L29`, which demonstrates debugging capability.

Put a breakpoint on the line above and then do debug run of [this test](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/401d40a22430661ed5a397098633465b1e39e3bc/sigmastate/src/test/scala/sigmastate/utxo/examples/AssetsAtomicExchangeTests.scala#L46). 

It should stop at the breakpoint. 