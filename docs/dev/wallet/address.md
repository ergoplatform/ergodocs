# Addresses

- Addresses in Ergo are short strings that correspond to specific scripts and serve as a means to protect a [box](box.md).
- Unlike Bitcoin (BTC), where addresses store a single amount, in Ergo's [eUTxO](eutxo.md) model, a box contains [registers](registers.md) that can store various values, including its native tokens.
- So, each [box](box.md) has an ERG amount and may or may not have a bunch of `{tokenid, token amount}` pairs, all in the UTXO model.
- Unlike account-based models like eth, ergo tokens are *native* and are not smart contracts.

## Address Types

Learn about the different types of addresses used in Ergo and their corresponding address types by visiting the [Address Types](address_types.md) page. 

## Address Validation

Learn how to validate Ergo addresses by visiting the [Address Validation](address_validation.md) page, which provides essential insights and methods for verifying P2S, P2SH, and P2PK addresses.


## Resources

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
