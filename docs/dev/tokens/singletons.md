# Singletons

In the UTXO model, a token issued with a quantity of exactly one unit is referred to as a `singleton` token. Singleton tokens can be used to emulate long-lived accounts similar to those found in Waves, Ethereum Classic, etc. A transaction that spends an old box with the singleton token and creates a new one can be controlled by the script of the old box, requiring the new box to have certain characteristics (such as a specific script or amount). This allows a smart account, marked with the token, to exist and alter its state as dictated by the smart account contract through a chain of transactions.

One specific example of a singular token is an [oracle](oracles.md). For instance, a token can be created to act as an ERG/EUR exchange rates oracle. A box that contains this token would encode the exchange rate in a specific register. Since the oracle is a long-lived account, contracts can know the oracle token identifier beforehand and refer to it.
