# Wallet Configuration

## Secret Storage

### Secret Directory
```conf
secretDir = ${ergo.directory}"/wallet/keystore"
```
This configures the directory where the wallet's secret information, such as private keys, will be stored. The directory is set to a "keystore" folder inside the "wallet" folder at the location specified by `${ergo.directory}`.

### Encryption
The encryption section contains configurations related to how the wallet's secret information is encrypted.

#### Pseudo-random function
```conf
prf = "HmacSHA256"
```
The `prf` configures the pseudo-random function used in the encryption. In this case, it is set to "HmacSHA256".

#### Number of PBKDF2 Iterations
```conf
c = 128000
```
The `c` configures the number of iterations used in the PBKDF2 (Password-Based Key Derivation Function 2) encryption algorithm.

#### Desired Bit-length of the Derived Key
```conf
dkLen = 256
```
The `dkLen` sets the desired length of the derived encryption key, in bits.

## Seed Strength Bits
```conf
seedStrengthBits = 160
```
This configures the length of the seed used in generating the wallet's private keys, in bits. Options include 128, 160, 192, 224, and 256.

## Mnemonic Phrase Language
```conf
mnemonicPhraseLanguage = "english"
```
This sets the language to be used for the wallet's mnemonic seed phrase. Options include "chinese_simplified", "chinese_traditional", "english", "french", "italian", "japanese", "korean", and "spanish".

## Keep Spent Boxes
```conf
keepSpentBoxes = false
```
This option determines whether to keep spent transaction outputs or to delete them immediately. 

## Default Transaction Fee
```conf
defaultTransactionFee = 1000000
```
This sets the default transaction fee the wallet uses when a fee is not specified.

## Use Pre-EIP3 Derivation
```conf
usePreEip3Derivation = false
```
This setting determines whether to use the pre-EIP3 key derivation scheme or not.

## Dust Limit
```conf
dustLimit = null
```
The `dustLimit` sets the minimum amount of tokens that can be included in a transaction output. If it's set to null (default), there is no minimum limit.

For example, with `dustLimit = 1000000`, the node wallet will ignore boxes to self that contain less than .001 ERG.

## Maximum and Optimal Inputs
```conf
maxInputs = 100
optimalInputs = 3
```

### Configuration Parameters Explained

- **maxInputs**: Defines the hard upper limit on how many input boxes can be included in a single transaction. This prevents transactions from becoming excessively large, which could impact network performance.

- **optimalInputs**: Controls the target number of inputs the wallet attempts to use when building transactions, playing a crucial role in UTXO management.

### How Optimal Inputs Works

The wallet's box selector uses the `optimalInputs` parameter as a threshold for dust collection. When creating a transaction:

- If the transaction naturally requires fewer inputs than `optimalInputs`, the wallet will automatically add small-value UTXOs (dust) from your wallet to reach this target number.
- If adding more inputs would exceed `maxInputs`, the wallet respects the maximum limit.

### Benefits of This Approach

1. **Automatic Dust Management**: Small UTXOs that would otherwise accumulate in your wallet are gradually consumed, preventing wallet bloat.

2. **Efficient UTXO Set**: By consolidating multiple small UTXOs into fewer, larger ones, the wallet maintains an efficient UTXO set.

3. **Improved Performance**: With fewer UTXOs to process, wallet operations become faster and more efficient.

For example, if `optimalInputs = 3` and your payment only requires one input box, the wallet will automatically select two additional small-value UTXOs to include in the transaction, resulting in fewer total UTXOs after the transaction completes.

This mechanism works alongside the `dustLimit` setting (if configured) to optimize wallet performance, which is especially valuable for high-transaction environments like exchanges.
## Test Mnemonic and Keys Quantity
```conf
# testMnemonic = "ozone drill grab fiber curtain grace pudding thank cruise elder eight picnic"
# testKeysQty = 5
```
These settings are used for testing purposes. If a `testMnemonic` is set, the wallet will operate in test mode, using this mnemonic seed. The `testKeysQty` determines the number of keys to generate for the test.

## Tokens Whitelist
```conf
tokensWhitelist = null
```
If set, the wallet will automatically burn non-whitelisted tokens from inputs when making transactions. If it's null, no tokens will be automatically burnt.

## Check EIP27
```conf
checkEIP27 = false
```
This setting determines whether to handle re-emission tokens in the wallet correctly. For example, it affects how transfers are done in the presence of re-emission tokens.

## Profile


```conf
profile = "user"
```
The wallet profile helps the wallet understand the expected load and allocate memory for caches and Bloom filters accordingly. Options are: "user" (for ordinary usage), "exchange" (for high load situations, consuming ~20MB of RAM for Bloom filters), and "appServer" (in between).
