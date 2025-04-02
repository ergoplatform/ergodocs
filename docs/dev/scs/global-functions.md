---
tags:
  - Global Functions
  - ErgoScript
---

# Global Functions

There are a variety of global functions available for use in ErgoScript. Here, we will go through some of the most commonly used functions (besides `sigmaProp`). A complete reference for all global functions and types can be found in the [ErgoScript LangSpec](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md).

## Logical Functions

Logical functions are global functions that operate on booleans. These functions include operators such as `&&` and `||`, along with the following commonly used functions.

### AllOf

The `allOf` function takes a collection of booleans and returns a boolean indicating whether all booleans within the collection evaluate to true. It is equivalent to inserting `&&` between each boolean in the collection.

### AnyOf

The `anyOf` function takes a collection of booleans and returns a boolean indicating whether at least one boolean within the collection evaluates to true. It is equivalent to inserting `||` between each boolean in the collection.

### XorOf

The `xorOf` function takes a collection of booleans and applies the XOR operation across the booleans within the collection. Therefore, `xorOf` returns true if an odd number of booleans within the collection evaluates to true, and false if an even number evaluates to true.

## Zero-Knowledge Functions

Zero-knowledge functions allow evaluating SigmaProps while preserving the zero-knowledge properties needed to verify the truth of the given SigmaProps.

### AtLeast

The `atLeast` function takes an integer `k` and a collection of SigmaProps and returns whether at least `k` SigmaProps within the collection evaluate to true. All SigmaProps are evaluated with zero knowledge.

### ZKProof

The `ZKProof` function takes a block of code and evaluates all operations within the code block under zero-knowledge scoping. This may be useful if some operations within your contract must be kept private. The code block must not use boolean operations to ensure zero-knowledge and must evaluate to a single root SigmaProp.

## Cryptographic Functions

Cryptographic functions are functions related to cryptography, such as hashing and calculations over `GroupElement` values.

### Blake2b256

`blake2b256` takes a `Coll[Byte]` and returns a new `Coll[Byte]` representing the hash according to the Blake2b256 algorithm. The Blake2b256 algorithm is the main hashing algorithm used within Ergo and is also incorporated as part of the Autolykos PoW algorithm used to mine Ergo.

### Sha256

`sha256` takes a `Coll[Byte]` and returns a new `Coll[Byte]` representing the hash according to the SHA256 hashing function.

### DecodePoint

`decodePoint` takes a `Coll[Byte]` representing a group element and converts it into the `GroupElement` type.

### ProveDHTuple

`proveDHTuple` takes four `GroupElement` values and constructs a public key represented by a SigmaProp according to the Diffie-Hellman signature protocol. This is useful for creating shared public keys in multisignature and ring signature settings.

### ProveDLog

`proveDlog` takes a `GroupElement` and creates a SigmaProp representing a public key based on the discrete logarithm problem.

## Compile-Time Functions

Compile-time functions are not evaluated during the spending of the script; instead, these functions are used when compiling an ErgoScript contract into the native ErgoTree language. These functions take Strings (which is not an actual ErgoScript type) and convert them into an ErgoScript type during contract compilation. These values are stored directly within the contract and cannot change once the contract has been compiled.

### FromBase

Two functions, `fromBase64` and `fromBase58`, take strings in their respective base and convert them into a `Coll[Byte]` at compile time.

### PK

The `PK` function takes an address string (which is a base58 encoded `GroupElement` with a network identifier prefix) and converts it into a `SigmaProp` representing a public key at compile time. This is done using many of the functions listed above.

### Deserialize

The `deserialize[T]` function takes a type parameter `T` and a base58 encoded string of binary data. The string value is converted into a value of ErgoScript type `T` at compile time.

## Other Functions

### GetVar
`getVar[T]` takes a type parameter `T` and an integer `tag`, returning a Context Variable of the given type associated with that `tag`. Context Variables are specific off-chain variables that can be attached to any box at the time of transaction creation. Context variables allow for robust changes to certain parameters within your contract. It is especially useful for providing generic contracts that rely on off-chain information that may change between different spending transactions.

### SubstConstants

The `substConstants` function has the following signature:

```scala
def substConstants[T](scriptBytes: Coll[Byte],
 positions: Coll[Int], newValues: Coll[T]): Coll[Byte]
```

It allows constructing another contract’s proposition bytes using the given parameters. Because a contract’s address is created using its contents, inputting different constants within a contract can change its address (and therefore, the contract itself). This function allows for a contract of the same “template” to be created using a new set of constants. To be used properly, one must provide a sample of the contract’s proposition bytes (parameter `scriptBytes`), along with the `positions` at which certain constants of type `T` must be replaced with the corresponding values in the `newValues` parameter.


## Example: Alcohol Sale Proxy Contract

```scala
{
	// ====== Alcohol Sale Proxy Contract Example ====== // 

	// Hard-coded constants expected at compile time are written in UpperCamelCase.
	
	// INPUTS:
	// license          = INPUTS(0)
	// buyerProxyInputs = INPUTS - INPUTS(0)
	//
	// OUTPUTS:
	// storeBox              = OUTPUTS(0)
	// provincialSalesTaxBox = OUTPUTS(1)
	// federalSalesTaxBox    = OUTPUTS(2)
	// buyerWalletBox        = OUTPUTS(3)
	// minerFeeBox           = OUTPUTS(4)
	//
	// (*) Note: 
	//           1. Mining fee box is always the last box in the set of OUTPUTS of a transaction,
	//              I am just showing this for clarity, but it will not be accessed in this contract.
    	//           2. If there is any that change remains in the proxy, 
	//				it is sent back to the buyer wallet.

	// Contract variables
  	val buyerPK: SigmaProp          = PK(buyerPKString)
	val buyerProxyInputs: Coll[Box] = INPUTS.filter({ (input: Box) => input.propositionBytes == SELF.propositionBytes })
	val buyerAmount: Long           = buyerProxyInputs.fold(0L)({ (input: Box, acc: Long) => acc + input.value })
	val provincialSalesTax: Long    = (AlcoholSaleAmount * ProvincialSalesTaxNum) / ProvincialSalesTaxDenom
	val federalSalesTax: Long       = (AlcoholSaleAmount * FederalSalesTaxNum) / FederalSalesTaxDenom
	val totalCost: Long             = AlcoholSaleAmount + provincialSalesTax + federalSalesTax + MinerFee
	
	// Variables associated with the buyer's license
	val license = INPUTS(0)
	val id      = license.R4[Coll[Byte]].get
	val name    = license.R5[Coll[Byte]].get
	val bDay    = license.R6[Coll[Byte]].get
	val address = license.R7[Coll[Byte]].get
	val expDate = license.R8[Coll[Byte]].get

	// Context variables needed for the proxy contract, assuming they are provided correctly
	val licenseTemplateContractBytes = getVar[Coll[Byte]](0).get

	// Substitute the constants of the license template contract bytes
	// and create the new contract bytes for the buyer's license
	val newLicenseContractBytes = {
		
		// New positions
		val newPositions_SigmaProp: Coll[Int] = Coll(0)
		val newPositions_Coll_Byte: Coll[Int] = Coll(1, 2, 3, 4, 5)
	
		// New constants
		val newConstants_SigmaProp: Coll[SigmaProp] = Coll(buyerPK)
		val newConstants_Coll_Byte: Coll[Byte] = Coll(id, name, bDay, address, expDate)

		// New contract bytes with substituted buyer PK
		val newContractBytes_SigmaProp = substConstants(licenseTemplateContractBytes, newPositions_SigmaProp, newConstants_SigmaProp)
		
		// New contract bytes with substituted buyer license information
		val newContractBytes_Coll_Byte = substConstants(newContractBytes_SigmaProp, newPositions_Coll_Byte, newConstants_Coll_Byte)
		val newContractBytes = newContractBytes_Coll_Byte
		
		newContractBytes
	}

	// Check for a valid sale
	val validSale = {

		// Check for a valid license 
		val validLicense = {
			allOf(Coll(
				BuyerLicenseContractBytes == newLicenseContractBytes,
				license.propositionBytes == newLicenseContractBytes
			))
		}

		// Check for a valid proxy amount
    		val validProxyAmount = {
	    		buyerAmount >= totalAmount
		}

		// Check for a valid store
		val validStore = {
			val storeBox = OUTPUTS(0)
			storeBox.propBytes == StoreBoxPropositionBytes
		}

		// Check for valid sales taxes
		val validSalesTaxes = {
			
			// Check for a valid provincial tax
			val validProvincialSalesTax = {
				val provincialSalesTaxBox = OUTPUTS(1)
				allOf(Coll(
					(provincialSalesTaxBox.propositionBytes == ProvincialSalesTaxPK),
					(provincialSalesTaxBox.value >= provincialSalesTax)
				))
			}

			// Check for a valid federal tax
			val validFederalSalesTax = {
				val federalSalesTaxBox = OUTPUTS(2)
				allOf(Coll(
					(federalSalesTaxBox.propositionBytes == FederalSalesTaxPK),
					(federalSalesTaxBox.value >= federalSalesTax)
				))
			}
      
      			// Demand that both sales taxes are valid
      			allOf(Coll(
        			validProvincialSalesTax,
        			validFederalSalesTax
      			))

		}

		// Check for a valid buyer wallet to return any change
		val validBuyerWallet = {
			if (buyerAmount > totalCost) {
				val buyerWalletBox = OUTPUTS(3)
				buyerWalletBox.propositionBytes == buyerPK.propBytes
			} else {
				true
			}
		}		
	
		// Demand that all the conditions are valid
		allOf(Coll(
			validLicense,
			validProxyAmount,
			validStore,
			validSalesTaxes,
			validBuyerWallet
		))

	}

	// Check for a valid refund
	val validRefund = {
		val refundWalletBox = OUTPUTS(0)
		allOf(Coll(
			(refundWalletBox.propositionBytes == buyerPK.propBytes),
			(refundWalletBox.value >= buyerAmount - MinerFee)
		))
	}

	// Obtain the appropriate sigma proposition
	sigmaProp(anyOf(Coll(
		validSale,
		validRefund
	)))

}
```
