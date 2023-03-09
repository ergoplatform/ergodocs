# Boxes and Registers

Boxes are the main entity used to hold ERG according to the eUTXO model. Registers are pieces of data that can be attached to any box. They allow your contract to store data and incorporate it into transactions at a later point. There are 4 mandatory registers present within each box in the Ergo blockchain, these registers describe information that is necessary for a box to exist and be valid. Besides the mandatory registers, there are 5 additional registers that may store arbitrary data. This data could be obtained both off-chain and on-chain and allows you to incorporate more data when creating the spending conditions for your contract.

### R0

Contains the monetary value of the box in nanoERGs. This register is accessed using `Box.value`, where `Box` could represent either `SELF` or one of the boxes in the `INPUTS` or `OUTPUTS` collection.

### R1

Contains the collection of proposition bytes of the guarding ErgoScript contract for the box. It is accessed using `Box.propositionBytes`.

### R2

Contains a collection of the tokens stored in the box. A token contains is represented by two pieces of information: the unique token id; and the amount of the specified token. The collection is accessed using `Box.tokens`.

### R3

Contains information about the box’s creation such as: the transaction id from which the box was created as an output; the outputs index of the box (i.e. the index used in `OUTPUTS`); and the creation height of the block of the transaction from which the box came from. This collection is accessed using `Box.creationInfo`. The height referenced here is used as part of Ergo’s unique storage rent feature, where boxes may be spent after 4 years so that miners may take some fee and recycle ERG back into the blockchain.

### R4 - R9

Contains arbitrary data that is set whenever the box is first outputted from a transaction. This data may essentially be any type commonly found in ErgoScript, along with more complex types built from Pairs and Collections. Registers may also store more complex types such as `Box`, `SigmaProp`, `GroupElement`, and `AVLTree`.

### Other Box Functions

Outside of the registers themselves, each box has a specific identification hash that may be referenced using the `id` function. Box ids are formed by taking the `blake2b256` hash of the boxes content as a `Coll[Byte]` . You may directly reference the un-hashed collection of bytes representing a box using the `bytes` function. Keep in mind that each box’s content and id are cryptographically unique, meaning that no two boxes within the blockchain may have the same id or content bytes. This is achieved due to the inclusion of `creationInfo` within each box, as transaction ids and associated output indexes are all values that must be unique to a given UTXO.  You may use the `bytesWithoutRef` function to return a `Coll[Byte]` that does not contain such information.

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
