# Language Operations

## Opcodes

|   Code	|   Operation	|   Comment	|
|---	|---	|---	|
|   1	| $LT(left: Value[SInt], right: Value[SInt])$$	|   	|
|   2	| $LE(left: Value[SInt], right: Value[SInt])$  	|   	|
|   3	| $GT(left: Value[SInt], right: Value[SInt])$  	|   	|
|   4	| $GE(left: Value[SInt], right: Value[SInt])$  	|   	|
|   5	| $EQ$[$T1 <: SType, T2 <: SType$]$(left: Value[T1], right: Value[T2])$  	|   	|
|   6	| $NEQ$[$T1 <: SType, T2 <: SType$]$(left: Value[T1], right: Value[T2])$  	|   	|
|   7	| $OR(input: Value[SCollection[SBoolean]])$  	|   	|
|   8	| $AND(input: Value[SCollection[SBoolean]])$  	|   	|
|   9	| $CAND(sigmaTrees: Seq[SigmaTree])$  	|   	|
|   10	| $COR(sigmaTrees: Seq[SigmaTree])$  	|   	|
|   11	| $Plus(left: Value[SInt], right: Value[SInt])$  	|   	|
|   12	| $Minus(left: Value[SInt], right: Value[SInt])$  	|   	|
|   13	| $Xor(left: Value[SByteArray], right: Value[SByteArray])$  	|   	|
|   14	| $AppendBytes(left: Value[SByteArray], right: Value[SByteArray])$  	|   	|
|   15	| $Exponentiate(left: Value[SGroupElement], right: Value[SBigInt])$  	|   	|
|   16	| $MultiplyGroup(left: Value[SGroupElement], right: Value[SGroupElement])$  	|   	|
|   17	| $IntToByteArray(input: Value[SInt])$  	|   	|
|   18	| $ByteArrayToBigInt(input: Value[SByteArray])$  	|   	|
|   19	| $CalcBlake2b256(input: Value[SByteArray])$  	|   	|
|   20	| $ProveDiffieHellmanTuple(gv: Value[SGroupElement], hv: Value[SGroupElement], uv: Value[SGroupElement], vv: Value[SGroupElement])$  	|   	|
|   21	| $IsMember(tree: Value[SAvlTree], key: Value[SByteArray], proof: Value[SByteArray])$  	|   	|
|   22	| $IntConstant(value: Long)$ 	|   	|
|   23	| $TaggedInt(id: Byte)$  	|   	|
|   24	| $BigIntConstant(value: BigInteger)$  	|   	|
|   25	| $TaggedBigInt(id: Byte)$  	|   	|
|   26	| $ByteArrayConstant(value: Array[Byte])$  	|   	|
|   27	| $TaggedByteArray(id: Byte)$  	|   	|
|   28	| $PropConstant(value: Array[Byte])$  	|   	|
|   29	| $TaggedProp(id: Byte)$  	|   	|
|   30	| $AvlTreeConstant(value: AvlTreeData)$  	|   	|
|   31	| $TaggedAvlTree(id: Byte)$  	|   	|
|   32	| $GroupElementConstant(value: GroupElement)$  	|   	|
|   33	| $GroupGenerator$  	|   	|
|   34	| $TaggedGroupElement(id: Byte)$  	|   	|
|   35	| $BooleanConstant(val value: Boolean)$  	|   	|
|   36	| $TaggedBoolean(id: Byte)$  	|   	|
|   37	| $TaggedBox(id: Byte)$  	|   	|
|   38	| $ConcreteCollection$[$V <: SType$]$(value: IndexedSeq[Value[V]])$  	|   	|
|   39	| $MapCollection$[$IV <: SType, OV <: SType](input: Value[SCollection[IV]], id: Byte, mapper: Transformer[IV, OV])$  	|   	|
|   40	| $Exists$[$IV <: SType](input: Value$[SCollection[IV]], id: Byte, relations: Relation[_, _]*)$	|   	|
|   41	| $ForAll$[$IV <: SType](input: Value[SCollection[IV]], id: Byte, relations: Relation[_, _])$ 	|   	|
|   42	| $Fold$[$IV <: SType](input: Value[SCollection[IV]], id: Byte, zero: Value[IV], accId: Byte, foldOp: TwoArgumentsOperation[IV, IV, IV])$  	|   	|
|   43	| $ByIndex$[$V <: SType](input: Value[SCollection[V]], index: Int)$  	|   	|
|   44	| $SizeOf$[$V <: SType](input: Value[SCollection[V]])$  	|   	|
|   45	| $ExtractHeight(input: Value[SBox])$  	|   	|
|   46	| $Height$  	| ???	|
|   47	| $ExtractAmount(input: Value[SBox])$  	|   	|
|   48	| $ExtractScript(input: Value[SBox])$  	|   	|
|   49	| $ExtractBytes(input: Value[SBox])$  	|   	|
|   50	| $ExtractId(input: Value[SBox])$  	|   	|
|   51	| $ExtractRegisterAs$[$V <: SType](input: Value[SBox], registerId: RegisterIdentifier, default: Option[Value[V]] = None)$  	|   	|
|   52	| $TxOutput(outIndex: Int)$  	|   	|
|   53	| $ProveDlog(value: Value[SGroupElement])$  	|   	|



## UnknownByteArray

## TaggedVariable

- [Remove unused TaggedVariable node #657](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/657)
  
## SGroupElement

The 'S' in front of `SGroupElement` refers to the sigma state code under the ErgoScript. When working on the ErgoScript directly, you will use `GroupElement`.


## Blockchain related objects 

### BoxLeafConstant 
### SAvlTree (AvlTreeData)

- ["AvlTree" -> SAvlTree](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/fe7319f6ddd131d4bc02f46313f3590721f39f3b/parsers/shared/src/main/scala/sigmastate/lang/Types.scala#L40)

- [case class AvlTreeData(digest: ADDigest](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/fe7319f6ddd131d4bc02f46313f3590721f39f3b/interpreter/shared/src/main/scala/sigmastate/AvlTreeData.scala#L54)

## Height