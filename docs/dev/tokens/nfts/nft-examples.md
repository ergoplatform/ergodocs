# NFT Examples

Here is a simple example that demonstrates how to build a V2 NFT picture token using [Ergo Python Appkit](https://github.com/ergo-pad/ergo-python-appkit) The the [Eip4TokenBuilder](https://github.com/ergoplatform/ergo-appkit/blob/master/lib-impl/src/main/java/org/ergoplatform/appkit/impl/Eip4TokenBuilder.java) class in [Appkit](appkit.md) which provides several methods for minting different types of NFTs.

This code defines two classes, `TokenBuilder` and `MintTokenExecutor`. 

The `TokenBuilder` class has a single apply function that creates the NFT with `Eip4TokenBuilder.buildNftPictureToken`.


```python
from ergo_appkit import Eip4TokenBuilder, BoxOperations

class TokenBuilder:
    @staticmethod
    def apply(address: str):
        # Add the required attributes for V2 NFT
        version = 2
        royalty_recipients = [('recipient_address', 5)]  # Replace 'recipient_address' with the actual address
        traits = {
            'properties': {'property1': 'value1', 'property2': 'value2'},
            'levels': {'level1': 10, 'level2': 20},
            'stats': {'stat1': 30, 'stat2': 40}
        }
        collection_id = 'your_collection_id'  # Replace with the actual collection ID
        additional_info = {
            'explicit_content': False,
            'linkToImage': 'https://example.com/image.jpg'  # Replace with the actual image URL
        }

        # Use buildNftPictureTokenV2 for creating a V2 NFT
        return Eip4TokenBuilder.buildNftPictureTokenV2(
            address,
            version,
            royalty_recipients,
            traits,
            collection_id,
            additional_info
        )

class MintTokenExecutor:
    def __init__(self, address: str):
        self.address = address

    # Function to mint the NFT created by TokenBuilder
    def apply(self, token: dict):

        # Create a BoxOperations object with the provided address
        box_operations = BoxOperations(self.address)
        
        # Spend a specific amount of Ergo to mint the NFT
        box_operations = box_operations.withAmountToSpend(token['ergs_to_mint'])

        # Reduce the unsigned transaction to a suitable format for transmission
        reduced_tx = box_operations.reduce(token['unsigned_tx'])

        return reduced_tx

# Instantiate the TokenBuilder and MintTokenExecutor classes
token_builder = TokenBuilder()
mint_token_executor = MintTokenExecutor("your_address_here")

# Create the NFT using TokenBuilder
token = token_builder.apply("your_address_here")

# Mint the NFT using MintTokenExecutor
reduced_tx = mint_token_executor.apply(token)

# Print the reduced unsigned transaction
print(reduced_tx.get_base64_reduced_tx())
```

## More Examples

- [Bulk Mint with Royalties using v1 design in Python](https://github.com/mgpai22/ergpy/blob/main/examples/example_5_bulk_mint_with_royalty.py)
- [On-Chain NFTs](on-chain.md)

