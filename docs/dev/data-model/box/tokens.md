## Standards for Asset Issuance

Ergo treats custom tokens as first-class citizens. A particular [register](registers.md) (`R2`) within a [box](box.md) holds pairs of `tokenId` and `amount`. There's a hard limit on the number of tokens per box or transaction, which is quite generous, allowing up to **255** secondary tokens in a transaction or a box. However, there are indirect restrictions too: a box can't exceed **4** kilobytes, and the addition of tokens also increases the computational cost estimation of the transaction.

The amount of Erg is specified directly in the register `R0`, written as a number without any identifier. 

However, Ergs differ from other tokens in the following significant ways:

* **ERGs cannot be burnt**: the total amount of ergs in transaction inputs must equal the total amount in the outputs. Other tokens, unlike **ERGs**, can be burnt: the total amount of a token in transaction inputs must be no less than the amount in the outputs.
* [Storage rent](rent.md) is **payable in ERG only**.

Tokens can be representative of a variety of things, like shares, units of complementary currency, or any other conceivable item.

### Singletons

In the UTXO model, a token issued with a quantity of exactly one unit is referred to as a `singleton` token. Singleton tokens can be used to emulate long-lived accounts similar to those found in Waves, Ethereum Classic, etc. A transaction that spends an old box with the singleton token and creates a new one can be controlled by the script of the old box, requiring the new box to have certain characteristics (such as a specific script or amount). This allows a smart account, marked with the token, to exist and alter its state as dictated by the smart account contract through a chain of transactions.

One specific example of a singular token is an [oracle](oracles.md). For instance, a token can be created to act as an ERG/EUR exchange rates oracle. A box that contains this token would encode the exchange rate in a specific register. Since the oracle is a long-lived account, contracts can know the oracle token identifier beforehand and refer to it.

**How can new assets be created?**

There is an exception to the rule of weak preservation *(the total amount in inputs is no less than the total amount in outputs)*: a transaction can create tokens from thin air in its outputs if the asset identifier matches the identifier of the transaction's first input box. Since the box identifier is cryptographically unique, it's impossible to have a second asset with the same identifier, assuming the hash function used is collision-resistant (which it indeed is). This rule also implies that only one new asset can be created per transaction.

The Ergo reference implementation wallet employs specific [registers](registers.md) in a particular manner, though the protocol doesn't mandate this: 

* `R4` - verbose name
* `R5` - description
* `R6` - number of decimal places
* Additional registers (`R7`, `R8`, `R9`) can hold asset-specific information

Applications can follow this convention, but the protocol does not enforce it.