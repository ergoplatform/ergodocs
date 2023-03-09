
# wallet 

## secretStorage
### secretDir
```conf
secretDir = ${ergo.directory}"/wallet/keystore"
```
### encryption

#### prf
```conf
prf = "HmacSHA256"
```

Pseudo-random function with an output of length `dkLen` (PBKDF2 param)

#### c
```conf
c = 128000
```
Number of PBKDF2 iterations (PBKDF2 param)

#### dkLen

```conf
dkLen = 256
```

Desired bit-length of the derived key (PBKDF2 param)
## seedStrengthBits
```conf
seedStrengthBits = 160
```

Generating seed length in bits
Options: 128, 160, 192, 224, 256


## mnemonicPhraseLanguage
```conf
mnemonicPhraseLanguage = "english"
```

Language to be used in the mnemonic seed.

Options: "chinese_simplified", "chinese_traditional", "english", "french", "italian", "japanese", "korean", "spanish"


## keepSpentBoxes
```conf
keepSpentBoxes = false
```
Save used boxes (may consume additional disk space) or delete them immediately
## defaultTransactionFee
```conf
defaultTransactionFee = 1000000
```

The default fee the wallet uses when the fee is not specified.

## usePreEip3Derivation
```conf
usePreEip3Derivation = false
```

Use the pre-EIP3 key derivation scheme.

## dustLimit
```conf
dustLimit = null
```
## maxInputs
```
maxInputs = 100
```

## optimalInputs
```conf
optimalInputs = 3
```
## testMnemonic
```conf
# testMnemonic = "ozone drill grab fiber curtain grace pudding thank cruise elder eight picnic"
```
The mnemonic seed to be used in the wallet for tests. If set, the wallet operates in test mode.

## testKeysQty
```
# testKeysQty = 5
```
Number of keys to be generated for tests

## tokensWhitelist
```conf
tokensWhitelist = null
```

Whitelisted tokens, if non-null, the wallet will automatically burn non-whitelisted tokens from inputs when doing transactions.

If `tokensWhitelist = []`, any incoming tokens will be burnt, `tokensWhitelist = ["example"]` means that all the tokens except for "example" will be burnt

tokensWhitelist = null means no tokens burnt automatically
## checkEIP27
```conf
checkEIP27 = false
```
Enable this setting to handle re-emission tokens in the wallet properly,
e.g. doing transfers correctly in the presence of re-emission tokens
## profile
```conf
profile = "user"
```

Wallet profile allows to say wallet what kind of load it should expect, and so spend memory on caches and Bloom filters accordingly.

There are three options: user, exchange, and appServer.

The user profile is about ordinary planned usage.

Exchange consumes ~20 MB of RAM for high-load ready Bloom filters.

AppServer is in between
