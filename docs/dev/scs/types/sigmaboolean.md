# SigmaBoolean

SigmaBoolean is a fundamental component in the world of SigmaScript and SigmaDsl, serving as an algebraic data type for sigma proposition expressions. This data type enables developers to work with boolean-like logic for sigma propositions, and it's worth noting that SigmaBoolean is a recursive data structure, adding complexity to its parsing process.

## Understanding the Structure of SigmaBoolean

To comprehend SigmaBoolean better, let's delve into its structure:

```scala
/** Represents the algebraic data type of sigma proposition expressions.
 * 
 */
trait SigmaBoolean {
  /** A unique identifier for the node class, used during serialization. */
  val opCode: OpCode
  /** Returns the size of the proposition tree (number of nodes). */
  def size: Int
}
```
Within this structure, `opCode` serves as an identifier for the node class, especially during the serialization process. Concurrently, the `size` method provides a means to determine the size of the proposition tree in terms of its nodes.


Check out [Values.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/Values.scala#L745) for full details


## Serializing SigmaBoolean from a P2PK Address

Serializing SigmaBoolean from a P2PK address is a key process in Ergo blockchain development. This process enables the creation and execution of sophisticated smart contracts. Through the encoding of SigmaBoolean from a P2PK address, developers can articulate intricate contract conditions, bolster privacy features, ensure seamless interoperability, tailor contract logic, enhance security auditing measures, and facilitate cross-platform compatibility.

Serializing SigmaBoolean from a P2PK (Pay-to-Public-Key) address involves several steps:

1. **Decode P2PK Address**: Begin by decoding the P2PK address using Base58 encoding.

2. **Extract Public Key Bytes**: From the decoded data, remove the first byte, retain the last 4 bytes, and prepend it with `0xCD, 0x03`.

3. **Incorporate Instruction Code**: Integrate the `ProveDlog` instruction code with the public key bytes by prepending "08cd" to the bytes. This produces a serialized SigmaBoolean value.

To obtain the ErgoTree, prepend `0x00` (header byte) to the serialized SigmaBoolean.

### Serialization using Fleet (TypeScript)

Here's how you can serialize SigmaBoolean using Fleet in TypeScript:

```typescript
// Extract the public key from the encoded address
const pk = ErgoAddress.fromBase58("address_here").getPublicKeys()[0];

// For base64 encoding (typically required for ergopay):
const encodedProp = base64.encode(SSigmaProp(SGroupElement(pk)).toBytes());

// Without base64 encoding:
const encodedProp = SSigmaProp(SGroupElement(pk)).toHex();
```

### Serialization with bs58 (TypeScript)

Alternatively, you can use bs58 for serialization in TypeScript:

```typescript
const decodedBuffer = bs58.decode(ergoAddress);
const rawBytes = Uint8Array.from(decodedBuffer);
const slicedBytes = rawBytes.subarray(2, rawBytes.length - 4);
const combinedBytes = new Uint8Array([0xCD, 0x03, ...slicedBytes]);
const sigmaBoolean = Buffer.from(combinedBytes).toString('base64');
```

## Data Serialization in SigmaState

Within the SigmaState framework, data serialization is crucial, including the serialization and deserialization of SigmaBoolean, which is handled as follows:

```scala
...
case SSigmaProp =>
    val p = v.asInstanceOf[SigmaProp]
    SigmaBoolean.serializer.serialize(sigmaPropToSigmaBoolean(p), w)
...
case SSigmaProp =>
    SigmaDsl.SigmaProp(SigmaBoolean.serializer.parse(r))
...
```

Key points to note:

1. **Serialization**: The serialization of `SigmaBoolean` is accomplished using the `SigmaBoolean.serializer.serialize` method.

2. **Deserialization**: During deserialization, when encountering the `SSigmaProp` type, the `SigmaBoolean.serializer` is employed to parse and deserialize the sigma proposition from the provided reader `r`.

3. **Type Matching**: The type `SSigmaProp` specifically represents sigma propositions in the provided code, and its serialization and deserialization are managed with precision.
