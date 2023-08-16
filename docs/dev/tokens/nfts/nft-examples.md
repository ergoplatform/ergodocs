# NFT Examples


## Using Scala

[minting-for-dummies](https://github.com/lucagdangelo/minting-for-dummies) is a basic tool for NFT minting quickly in Scala. 

You can see the [mint() logic here](https://github.com/lucagdangelo/minting-for-dummies/blob/cd99049f13eb6ab4489f0f880e8d36e33b27bdb2/src/main/scala/app/MintForDummiesCommands.scala#L11)


## Using Ergo Python Appkit

To mint an NFT using the [Ergo Python Appkit](https://github.com/ergo-pad/ergo-python-appkit), you can utilize the `mintToken` method provided by the `ErgoAppKit` class. First, you need to initialize the ErgoAppKit instance with the appropriate parameters such as nodeUrl, networkType, explorerUrl, and nodeApiKey. Then, you can call the mintToken method with the required parameters, including the value, tokenId, tokenName, tokenDesc, mintAmount, decimals, and contract.

Here's an example of how to mint an NFT using the ergo-python-appkit:

```python
from ergo_python_appkit import ErgoAppKit
from org.ergoplatform.appkit import ErgoContract

# Initialize ErgoAppKit instance
appKit = ErgoAppKit(nodeUrl="https://ergo-node-url", networkType="mainnet", explorerUrl="https://ergo-explorer-url", nodeApiKey="your-node-api-key")

# Define the NFT parameters
value = 1000000
tokenId = "your-token-id"
tokenName = "Your Token Name"
tokenDesc = "Your Token Description"
mintAmount = 1
decimals = 0

# Compile the contract
contract = ErgoContract.compile("sigmaProp(true)")

# Mint the NFT
appKit.mintToken(value, tokenId, tokenName, tokenDesc, mintAmount, decimals, contract)
```

After minting the NFT, you can use other methods provided by the ErgoAppKit class to interact with the NFT, such as transferring it to another address or querying its properties.

Reference links:

- [ErgoBox](https://github.com/ergo-pad/ergo-python-appkit/ergo_python_appkit/ErgoBox.py)
- [ErgoAppKit](https://github.com/ergo-pad/ergo-python-appkit/ergo_python_appkit/appkit.py)
- [ErgoTransaction](https://github.com/ergo-pad/ergo-python-appkit/ergo_python_appkit/ErgoTransaction.py)
- [ergo-python-appkit module](https://github.com/ergo-pad/ergo-python-appkit/ergo_python_appkit/__init__.py)
- [Building transaction and minting a token using AppKit from Python](appkit-node.md). 

## More Examples

- [Bulk Mint with Royalties using v1 design in Python](https://github.com/mgpai22/ergpy/blob/main/examples/example_5_bulk_mint_with_royalty.py)
- [On-Chain NFTs](on-chain.md)

## References

* [Eip4TokenBuilder on GitHub](https://github.com/ergoplatform/ergo-appkit/lib-impl/src/main/java/org/ergoplatform/appkit/impl/Eip4TokenBuilder.java)
* [Eip4Token on GitHub](https://github.com/ergoplatform/ergo-appkit/common/src/main/java/org/ergoplatform/appkit/Eip4Token.java)


