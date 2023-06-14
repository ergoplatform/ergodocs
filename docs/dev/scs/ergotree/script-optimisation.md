
# Potential Script Processing Optimization

Before an ErgoScript contract can be stored in a blockchain, it must be compiled from its source code into ErgoTree and then serialized into a byte array. The ErgoTree compiler, due to its purely functional graph-based IR, can perform various optimizations to reduce the tree's size. This results in normalization/unification, where different original scripts may compile into identical ErgoTrees and, consequently, identical serialized bytes. 

The obstacle to this optimization is the constants embedded in contracts. A

 simple solution to this problem is to avoid embedding constants. Each constant in the body of ErgoTree can be replaced with an indexed placeholder node. Each placeholder has an index of the constant in the constants collection of ErgoTree.

The format of serialized ErgoTree thus contains the bytes of a collection with segregated constants and the bytes of script expression with placeholders. 

[EIP5 is based on this ErgoTree feature](https://github.com/ergoplatform/eips/blob/master/eip-0005.md)