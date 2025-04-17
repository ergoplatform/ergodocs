# ergo-lib-python Documentation

## Overview

`ergo-lib-python` provides [Python](python.md) bindings for the core [`sigma-rust`](sigma-rust.md) library (implemented in [Rust](rust.md)), enabling interaction with the [Ergo blockchain](why.md) directly from Python applications. The underlying Rust implementation can be found in the `sigma-rust` repository: `https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-python`.

This library equips developers with tools to:

* Build and structure [Ergo transactions](transactions.md).
* Generate cryptographic keys and [wallet addresses](wallets.md).
* Sign transactions securely.
* Utilize various Ergo-specific data types and chain structures.

## Installation

Install the library using pip:

```bash
pip install ergo-lib-python
```

## Core Concepts & Usage Examples

Below are examples showcasing common operations using `ergo-lib-python`.

**1. Generate Mnemonic and Address**

Create a new mnemonic phrase, derive the corresponding keys, and obtain an Ergo address.

```python
from ergo_lib_python.wallet import MnemonicGenerator, ExtSecretKey, DerivationPath
from ergo_lib_python.chain import NetworkPrefix

# Generate a 128-bit entropy mnemonic using the English wordlist
mnemonic = MnemonicGenerator("english", 128).generate()
print(f"Generated Mnemonic: {mnemonic}")

# Create an Extended Secret Key from the mnemonic (optional password)
# Derive the secret key using the default derivation path (m/44'/429'/0'/0/0)
ext_secret_key = ExtSecretKey.from_mnemonic(mnemonic, password="").derive(DerivationPath())

# Get the public key and the corresponding address
address = ext_secret_key.public_key().address()

# Display the address in Mainnet format (starts with '9')
print(f"Mainnet Address: {address.to_str(NetworkPrefix.Mainnet)}")
```

**2. Build a Simple ERG Transfer Transaction**

Construct an unsigned transaction to send ERG to a specified address.

```python
from ergo_lib_python.chain import ErgoBoxCandidate, Address
from ergo_lib_python.transaction import TxBuilder
from ergo_lib_python.wallet import select_boxes_simple
# Note: You'll need [ErgoBox](box-structure.md) instances for input_boxes

# --- Transaction Parameters ---
recipient_address_str = "9egnPnrYskFS8k1gYiKZEXZ2bhP9fvX9GZvsG1V3BzH3n8sBXrf" # Example recipient
amount_to_send_nanoerg = 1_000_000_000 # 1 ERG
miner_fee_nanoerg = 1_000_000 # 0.001 ERG (example fee)
current_blockchain_height = 1000000 # Example current height
change_address_str = "YOUR_CHANGE_ADDRESS_HERE" # Replace with your address
# input_boxes: This should be a list of ErgoBox objects you own and control
#              These objects hold the funds needed for the transaction.
input_boxes = [] # Populate with actual ErgoBox instances
# --- End Parameters ---

# 1. Define the output box for the recipient
output_candidate = ErgoBoxCandidate(
    value=amount_to_send_nanoerg,
    script=Address(recipient_address_str),
    creation_height=current_blockchain_height
)

# 2. Select input boxes to cover the transfer amount and miner fee
# This simple selector finds boxes with enough ERG.
# For transactions involving tokens, provide target_tokens list.
selection = select_boxes_simple(
    boxes=input_boxes,
    target_balance=output_candidate.value + miner_fee_nanoerg,
    target_tokens=[]
)

if not selection:
    raise ValueError("Insufficient funds or suitable boxes not found in input_boxes.")

# 3. Build the unsigned transaction
tx_builder = TxBuilder(
    box_selection=selection,
    output_candidates=[output_candidate],
    current_height=current_blockchain_height,
    fee_amount=miner_fee_nanoerg,
    change_address=Address(change_address_str)
)
unsigned_tx = tx_builder.build()

print(f"Unsigned Transaction ID: {unsigned_tx.id().to_str()}")
# Next step: Sign unsigned_tx using your wallet implementation

```

**3. Mint a Token (e.g., an NFT)**

Create a transaction that mints a new token. The ID of the newly minted token is derived from the ID of the first input box used in the transaction.

```python
from ergo_lib_python.chain import Token, TokenId, ErgoBoxCandidate, Address
from ergo_lib_python.transaction import TxBuilder
from ergo_lib_python.wallet import select_boxes_simple
# Note: You'll need ErgoBox instances for input_boxes

# --- Transaction Parameters ---
mint_amount = 1 # Quantity of the token to mint
token_name = "MyAwesomeNFT"
token_description = "This is a unique digital collectible."
token_decimals = 0 # 0 indicates the token is not divisible (common for NFTs)
box_value_nanoerg = 100_000_000 # Min box value (e.g., 0.1 ERG) for the token box
miner_fee_nanoerg = 1_000_000 # 0.001 ERG (example fee)
current_blockchain_height = 1000000 # Example current height
recipient_address_str = "YOUR_RECIPIENT_ADDRESS_HERE" # Who receives the minted token
change_address_str = "YOUR_CHANGE_ADDRESS_HERE" # Your change address
# input_boxes: List of ErgoBox objects you own. The first box's ID will become the token ID.
input_boxes = [] # Populate with actual ErgoBox instances
# --- End Parameters ---

# 1. Select input boxes to cover the box value and miner fee
selection = select_boxes_simple(
    boxes=input_boxes,
    target_balance=box_value_nanoerg + miner_fee_nanoerg,
    target_tokens=[]
)

if not selection or not selection.boxes:
    raise ValueError("Input box selection failed. Ensure input_boxes has sufficient funds and suitable boxes.")

# 2. Define the token properties. TokenId comes from the first input box.
first_input_box_id = selection.boxes[0].box_id
token_to_mint = Token(token_id=TokenId(first_input_box_id), amount=mint_amount)

# 3. Create the output box candidate that will hold the new token
mint_candidate = ErgoBoxCandidate(
    value=box_value_nanoerg,
    script=Address(recipient_address_str),
    creation_height=current_blockchain_height,
    mint_token=token_to_mint,
    mint_token_name=token_name,
    mint_token_desc=token_description,
    mint_token_decimals=token_decimals
)

# 4. Build the unsigned transaction
tx_builder = TxBuilder(
    box_selection=selection,
    output_candidates=[mint_candidate], # Output includes the token minting box
    current_height=current_blockchain_height,
    fee_amount=miner_fee_nanoerg,
    change_address=Address(change_address_str)
)
unsigned_tx = tx_builder.build()

print(f"Unsigned Token Mint Transaction ID: {unsigned_tx.id().to_str()}")
print(f"Minted Token ID: {token_to_mint.token_id.to_str()}") # This ID matches the first input box ID
# Next step: Sign unsigned_tx using your wallet implementation
```

## API Reference

A detailed API reference, generated directly from the library's source code, provides comprehensive information on all available modules, classes (like `ExtSecretKey`, `Address`, `ErgoBoxCandidate`, `TxBuilder`, `Token`), and functions (like `select_boxes_simple`). Consult this reference for specific method signatures, properties, and usage details.

*(Typically, this reference is available alongside the library's main documentation or can be generated locally using standard Python documentation tools like Sphinx.)*
