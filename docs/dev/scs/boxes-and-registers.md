---
tags:
  - Box
  - Registers
---

# Boxes and Registers

In [ErgoScript](ergoscript.md), a 'box' is akin to a more versatile version of what a UTXO (Unspent Transaction Output) represents in Bitcoin and many other cryptocurrencies. A box is not only a ledger entry denoting the amount of cryptocurrency owned by a particular address, but it also carries 'registers', allowing it to contain additional data. This data could range from simple values to more complex structures, which can later be integrated into transactions and used in the execution of smart contracts.

This makes Ergo's box different from a traditional UTXO, which only represents an amount of unspent cryptocurrency associated with a certain address. In UTXO-based cryptocurrencies, each transaction consumes one or more UTXOs as inputs and creates one or more UTXOs as outputs, with the 'unspent' outputs being the 'coins' that can be spent in future transactions.

The term 'box' in Ergo's context captures the idea that these entities are like containers holding various types of information (value, tokens, custom data, etc.), beyond just the unspent transaction output balance. This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running scripts or smart contracts, directly on the blockchain.

### Register R0

This register encapsulates the monetary value of the box in nanoERGs. It can be accessed using the `Box.value` command, where `Box` could signify `SELF` or any box in the `INPUTS` or `OUTPUTS` collections.

### Register R1

Register R1 contains the proposition bytes of the guarding ErgoScript contract associated with the box. Access this register using `Box.propositionBytes`.

### Register R2

R2 holds a collection of tokens stored in the box. Each token is identified by two elements: a unique token id and the quantity of the specific token. Use `Box.tokens` to access this collection.

### Register R3

R3 stores information about the box’s creation, such as the originating transaction id, the box's output index (i.e., the index used in `OUTPUTS`), and the block height at the creation time of the transaction from which the box originates. Access this register using `Box.creationInfo`. The creation height plays a role in Ergo's unique storage rent feature, where boxes can be spent after four years, enabling miners to charge a small fee and recycle ERGs back into the blockchain.

### Registers R4 - R9

These registers can contain any data defined when the box first originates from a transaction. The data could be of any common type found in ErgoScript, along with more complex types built from Pairs and Collections. These registers may also contain complex types such as `Box`, `SigmaProp`, `GroupElement`, and `AVLTree`.

### Additional Box Functions

Besides the registers, each box features a unique identification hash that can be referenced using the `id` function. Box ids are computed by applying the `blake2b256` hash function to the box's content, expressed as a `Coll[Byte]`. You can directly access the un-hashed byte collection representing a box using the `bytes` function. Note that each box’s content and id are cryptographically unique, meaning that no two boxes within the blockchain can share the same id or content bytes. This uniqueness is guaranteed by the inclusion of `creationInfo` in each box, as transaction ids and associated output indexes must be unique to a given UTXO. The `bytesWithoutRef` function can be used to retrieve a `Coll[Byte]` that excludes such information.

## Example

```scala
{
	// Retrieve the value and token multipliers from the registers of the current box
	val valueMultiplier = SELF.R4[Int].get
	val tokenMultiplier = INPUTS(1).R4[Int].get

	// Check if the current box is the same as the first input box
	if(SELF.id == INPUTS(0).id){
		// If it is, check if the output box has the correct value and token amounts
		val outputValue = OUTPUTS(0).value == SELF.value * valueMultiplier 
		val outputTokens = OUTPUTS(0).tokens(0)._2 == SELF.value * tokenMultiplier 
		// Return a Sigma proposition that is true only if both outputValue and outputTokens are true
		sigmaProp(outputValue && outputTokens)
	}else{
		// If the current box is not the same as the first input box, check if the output goes to a specified address
		val outputGoesToCheese = {
			// Create a public key that corresponds to a specific address
			PK("9etXmP7D3ZkWssDopWcWkCPpjn22RVuEyXoFSbVPWAvvzDbcDXE").propBytes
				== OUTPUTS(0).propositionBytes
		}
		// Return a Sigma proposition that is true only if outputGoesToCheese is true
		sigmaProp(outputGoesToCheese)
	}
}
```
