# The Blockchain Context

The Blockchain Context represents data taken from the transaction and the state of the blockchain. The data for the blockchain context is stored in the global object `CONTEXT`. `CONTEXT`, therefore, contains the main entities that you will interact with to manipulate your contract’s spending conditions.

### HEIGHT

An integer representing the height of the current block is to be validated by miners. The number can be accessed using `HEIGHT`.

### SELF

`SELF` represents the current eUTxO input box which holds the ErgoScript contract. The SELF box is of type `Box`, which contains information relevant to the specified eUTXO such as:

the value in nanoERGs; the box id; the proposition bytes of the guarding script for this eUTXO, the tokens stored in the box; and the box registers.

### INPUTS

The eUTxOs are used as input boxes to be spent in the transaction. The boxes are stored in a collection and can be accessed using the object called `INPUTS`. The `SELF` box is part of this input box collection.

### Data Inputs

Data inputs are input eUTXOs that are not spent in the transaction. They serve as ‘read-only’ boxes, usually holding information necessary for the spending conditions of the contract. Data inputs can be accessed using `CONTEXT.dataInputs`.

### OUTPUTS

The output box eUTXOs will be created from the transaction. The collection can be accessed using the `OUTPUTS` object.

### Headers

Block headers (Parts of each block that hold information representing the block) are available through the `CONTEXT.headers` function. The `headers` function returns a collection holding the last 10 block headers present before the current `HEIGHT`. Using this function allows your contract to gain insight into the most recent blocks that occurred before the transaction that your contract is being executed in. Each `Header` object in the collection returned by `headers` holds a variety of different information, much of this information pertains to the block miner, such as the miner’s PK, the nonce used to find the block, and the votes the miner submitted when the block was mined.

### Pre-Headers

The `CONTEXT.preHeader` function gives your contract access to the `PreHeader`. The `PreHeader` object represents all of the information available to miners who are working to find the next block. Because each block miner must insert their own information to properly mine a block, the data contained within each `PreHeader` object is completely different depending on who mines the block. This means that your contract could execute differently depending on who ends up mining the block that spends your contract’s box.

## Example

```scala
{
	// Don't worry about the fields accessed in our CONTEXT data, we will go more in depth
	// in the next section. Instead focus on how we are accessing this data and then using
	// using it in our contract.
	val selfAtZero = SELF.id == INPUTS(0).id
	val boxAmountToAdd: Long = CONTEXT.dataInputs(0).R4[Long].get // Get's a long from R4
	val amountAddedInOutputs = OUTPUTS(0).value == SELF.value + boxAmountToAdd
	val heightIsValid: Boolean = HEIGHT > 700000
	val randomValueIsEven: Boolean = CONTEXT.headers(0).powNonce(0) % 2 == 0

	sigmaProp(amountAddedInOutputs && selfAtZero) 
			|| sigmaProp(heightIsValid && randomValueIsEven)
}
```
