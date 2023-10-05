# SigmaBoolean

SigmaBoolean is a crucial data type in ErgoScript that represents propositions proven using Sigma protocols. It is derived from the base type [`ProveDlog`](global-functions.md#provedlog), which is used for discrete logarithm proofs. What sets SigmaBoolean apart is its dual functionality - it is used by the prover to construct the proof and by the verifier to check the proof. This dual role makes SigmaBoolean a key player in creating and verifying proofs within [ErgoScript](ergoscript.md).

As an algebraic data type in SigmaScript and SigmaDsl, SigmaBoolean allows developers to use boolean-like logic when working with [Sigma Propositions](sigma-prop.md). It's worth noting that SigmaBoolean is a recursive data structure, which adds complexity to the parsing process.

## Exploring SigmaBoolean Structure

To gain a deeper understanding of SigmaBoolean, let's examine its structure:

```scala
/** SigmaBoolean represents the algebraic data type of sigma proposition expressions.
 * 
 */
trait SigmaBoolean {
  /** A unique identifier for the node class, used during serialization. */
  val opCode: OpCode
  /** Returns the number of nodes in the proposition tree, indicating its size. */
  def size: Int
}
```

In Ergo, a node class represents a specific type or category of nodes within the proposition tree. Each node class has unique attributes and behaviors that dictate its interactions with other nodes and contribute to the overall tree structure. These node classes are identified by their [`opCodes`](lang-ops.md#opcodes), which correspond to various logical operations or conditions within the proposition tree. These operations can include AND (&&), OR (||), and THRESHOLD, as well as conditions like proveDlog and proveDHtuple.

By strategically combining and arranging these node classes, developers can construct intricate proposition trees that define the conditions and requirements for validating Ergo transactions. To determine the `size` of the proposition tree, developers can use the size method, which counts the number of nodes in the tree. This count provides an estimate of the tree's complexity or magnitude.

For the complete code, refer to [Values.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/Values.scala#L745).


## Serializing SigmaBoolean from a P2PK Address

You may want to serialize a SigmaBoolean from a [P2PK (Pay-to-Public-Key)](public-keys.md) address when you need to create a proof of knowledge for a specific public key. This process allows developers to create complex smart contracts. By encoding SigmaBoolean from a P2PK address, developers can define detailed contract conditions, improve privacy, ensure smooth interoperability, customize contract logic, enhance security audits, and support cross-platform compatibility.

Serializing SigmaBoolean from a P2PK  address involves several steps:

1. **Decode P2PK Address**: Begin by decoding the P2PK address using Base58 encoding.

2. **Extract Public Key Bytes**: From the decoded data, remove the first byte, retain the last 4 bytes, and prepend it with `0xCD, 0x03`.

3. **Incorporate Instruction Code**: Integrate the `ProveDlog` instruction code with the public key bytes by prepending "08cd" to the bytes. This produces a serialized SigmaBoolean value.

### Serialization with bs58 (TypeScript)

Alternatively, you can use bs58 for serialization in TypeScript:

```typescript
const decodedBuffer = bs58.decode(ergoAddress);
const rawBytes = Uint8Array.from(decodedBuffer);
const slicedBytes = rawBytes.subarray(2, rawBytes.length - 4);
const combinedBytes = new Uint8Array([0xCD, 0x03, ...slicedBytes]);
const sigmaBoolean = Buffer.from(combinedBytes).toString('base64');
```

### Serialization using Fleet (TypeScript)

Here's how you can serialize SigmaBoolean using [Fleet](fleet.md) in TypeScript:

```typescript
// Extract the public key from the encoded address
const pk = ErgoAddress.fromBase58("address_here").getPublicKeys()[0];

// For base64 encoding (typically required for ergopay):
const encodedProp = base64.encode(SSigmaProp(SGroupElement(pk)).toBytes());

// Without base64 encoding:
const encodedProp = SSigmaProp(SGroupElement(pk)).toHex();
```

### ErgoTree and its Role in Transactions

The [ErgoTree](ergotree.md) plays a vital role in Ergo transactions as it encompasses the spending conditions required for a box to be spent. To create an ErgoTree, it is necessary to prepend `0x00` (header byte) to the serialized SigmaBoolean. This step is not just a formality, but a crucial operation that enables the creation of intricate spending conditions. By supporting complex logical constructs, ErgoTree enhances the flexibility of contract design and strengthens the security of Ergo transactions.
