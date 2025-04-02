---
tags:
  - Blockchain
  - Context
---

# The Blockchain Context

The Blockchain Context represents data taken from the transaction and the state of the blockchain. The data for the blockchain context is stored in the global object `CONTEXT`. `CONTEXT`, therefore, contains the main entities that you will interact with to manipulate your contract’s spending conditions.

### HEIGHT

An integer representing the height of the block currently being validated by miners. This value can be accessed using `HEIGHT`.

### SELF

`SELF` represents the current eUTXO input box which holds the ErgoScript contract. The `SELF` box is of type `Box`, containing information relevant to the specified eUTXO, such as:

*   The value in nanoERGs
*   The box ID
*   The proposition bytes of the guarding script for this eUTXO
*   The tokens stored in the box
*   The box registers

### INPUTS

The eUTXOs used as input boxes to be spent in the transaction. These boxes are stored in a collection and can be accessed using the object called `INPUTS`. The `SELF` box is part of this input box collection.

### Data Inputs

Data inputs are input eUTXOs that are not spent in the transaction. They serve as ‘read-only’ boxes, usually holding information necessary for the spending conditions of the contract. Data inputs can be accessed using `CONTEXT.dataInputs`.

### OUTPUTS

The output box eUTXOs that will be created by the transaction. This collection can be accessed using the `OUTPUTS` object.

### Headers

Block headers are available through the `CONTEXT.headers` function. The `headers` function returns a collection holding the last 10 block headers preceding the current `HEIGHT`. Using this function allows your contract to gain insight into the most recent blocks before the current transaction's execution context. Each `Header` object in the collection returned by `headers` holds various information, much of which pertains to the block miner, such as the miner’s public key (PK), the nonce used to find the block, and the votes the miner submitted when the block was mined.

### Pre-Headers

The `CONTEXT.preHeader` function gives your contract access to the `PreHeader`. The `PreHeader` object represents all the information available to miners attempting to find the next block. Because each block miner must insert their own information to properly mine a block, the data contained within each `PreHeader` object varies depending on who mines the block. This means your contract could execute differently depending on who mines the block containing the transaction that spends your contract’s box.

## Example

```scala
{
	// Focus on how we are accessing this data and using it in our contract

	// Checking if the id of our first input box is the same as the id of our output box
	val selfAtZero = SELF.id == INPUTS(0).id
	// Retrieving a long value from R4 of the first data input and adding it to our output value
	val boxAmountToAdd: Long = CONTEXT.dataInputs(0).R4[Long].get 
	val amountAddedInOutputs = OUTPUTS(0).value == SELF.value + boxAmountToAdd
	// Ensuring the height is greater than 700000
	val heightIsValid: Boolean = HEIGHT > 700000
	// Ensuring the nonce is even
	val randomValueIsEven: Boolean = CONTEXT.headers(0).powNonce(0) % 2 == 0

	// If the first condition is true, then the second condition is not checked
	// Checking if either our output box has the correct value added or the nonce is even and height is greater than 700000
	sigmaProp(amountAddedInOutputs && selfAtZero) 
			|| sigmaProp(heightIsValid && randomValueIsEven)
}

```

The code uses various fields of the `CONTEXT` object to check certain conditions. It then combines these conditions into a final `SigmaProp` result that evaluates to true if either (`amountAddedInOutputs && selfAtZero`) or (`heightIsValid && randomValueIsEven`) is true.
