---
tags:
  - Security
  - Audit
---

# Security Audit

Ergo has successfully passed a security audit of certain (most critical) parts of the code. The audit was performed by Jean-Philipee Aumasson (aka veorq, [aumasson.jp/](https://aumasson.jp/)).

The detailed report is below. Nothing critical is found. Comments on issues found:

1. On wallet password, we'll provide a recommendation in subsequent versions of the protocol client. Not sure hard enforcement on passwords will take place, but we'll do more consultations on this.

2. Changing "n" and "k" parameters makes sense only when launching a new network. Changing these parameters in the mining node will make blocks produced invalid for other nodes. Changing these parameters in the protocol client means going on another fork (blocks coming from the honest protocol participants will be rejected). So no need for extra checks, as people launching new networks will set "n" and "k" properly.

3. Currently, the Ergo node (as well as other blockchain protocol clients and wallets we're aware of and the cryptographic libraries we're using) does not protect from side-channel attacks running locally (e.g. timing attacks or memory inspection by malware or viruses). So please protect the machines you're running wallets on!  


> Ergo security assessment by Jean-Philippe Aumasson on 07/Dec/19

## Summary

Ergo solicited us to perform a security assessment of several components of their Ergo Platform:

* Sigma protocol proofs creation and verification
* Wallet's secure storage of secrets
* Proof-of-Work validation

​This brief report summarises our assessment and describes our findings and mitigation recommendations.

## Sigma protocol proofs

​The Ergo protocol relies on ErgoScript, a scripting language supporting sigma-statements, which can be proven and verified through non-interactive proofs of knowledge.

These proofs are statements described as a tree of AND, OR, and threshold conditions, whose leaves are proofs of knowledge of a discrete logarithm problem.

The proof of the sigma-statement is then made non-interactive thanks to the Fiat-Shamir transform.

This logic is specified in the [ErgoScript paper](https://ergoplatform.org/docs/ErgoScript.pdf), and the specific
proving and verification routines described in Appendix A.

​Implementation challenges are then to:

* Define encoding of the proofs that are safe and efficient, and implement serialisation and deserialisation that always successfully processes valid input and gracefully fails to process invalid input.

* Implement the proving and verification functionalities correctly, in compliance with the specification, and most importantly, no invalid statement can successfully pass verification.

We reviewed these two aspects, based on the code in the repository [sigmastate-interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter), and the [ErgoScript paper](https://ergoplatform.org/docs/ErgoScript.pdf), carefully comparing the intended behaviour (in Appendix A) with the actual behaviour as implemented.

​We notably reviewed code from the [SigSerializer](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/master/sigmastate/src/main/scala/sigmastate/SigSerializer.scala), [Interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/master/sigmastate/src/main/scala/sigmastate/interpreter/Interpreter.scala), and [ProverInterpreter](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/master/sigmastate/src/main/scala/sigmastate/interpreter/ProverInterpreter.scala) traits and objects.

​We mainly sought bugs from the following classes:

* ​Unsafe processing of malformed input
* Unsafe processing of unusually long or short input
* Behavior when large tree depth or recursion level
* Unsafe use Scala types and structures
* Inappropriate variable types
* Integer overflows
* Race conditions
* Logic bugs 

​Despite the extensive review, we did not identify any security issue.

The protocol's logic and internals are relatively complex, and we believe the highest risk is in parsing and verifying proofs. To exploit such issues, however, an attacker would have to create a semantically correct script that somehow benefits them yet that passes verification when it does not ought to.

Regarding software security, Scala eliminates certain classes of bugs, but Scala code may still suffer from bugs due to Scala's specific behaviour or to unhandled errors.

## Wallet

Ergo's wallet functionality enables its users to store a secret on disk and recover it, initialising the wallet with a new seed when it's first used.

​This logic is mainly defined in [ErgoWalletActor](https://github.com/ergoplatform/ergo/blob/master/src/main/scala/org/ergoplatform/nodeView/wallet/ErgoWalletActor.scala), and a key component regarding secrets' storage is [JsonSecretStorage](https://github.com/ergoplatform/ergo/blob/master/ergo-wallet/src/main/scala/org/ergoplatform/wallet/secrets/JsonSecretStorage.scala).

​The first time a wallet is created, the `InitWallet` command does the following:

* Generate `settings.walletSettings.seedStrengthBits` random bits, as initial entropy. [By default](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/application.conf), 160 bits are generated.

* Generate a BIP39 from the random bits generated, which can be seen as encoding the entropy bits. The standard BIP39 logic is used with an optional password.
* Derive a seed from the mnemonic using BIP39's PBKDF2-based derivation logic.

* Encrypt this seed to disk with AES-GCM, using a random nonce, and a key derives from the password using PBKDF2-HMAC-SHA256 with [128000](https://github.com/ergoplatform/ergo/blob/master/src/test/resources/application.conf#L107) iterations, using a random salt.

To unlock a wallet already created, a user provides the password and the wallet attempts to decrypt the stored data.

​A similar process as initialisation is performed to restore an existing account from a BIP39 passphrase, except that the wallet will derive the seed from the mnemonic instead of picking a random mnemonic.

​The two risks we identified here are:

* The absence of checks on the password's length: since the password is sufficient to access the seed given the wallet's on-disk stored secret, the password should, in theory, have at least as much entropy as the mnemonic, and in practice, should be practically hard to crack. We thus recommend enforcing a minimal password length, for example of 16 characters.

* Copies of secret values (password, seed, and derive private keys) are likely to remain in memory after wallet software execution, an intrinsic limitation of garbage-collected languages such as Scala.

Another process or user sharing the same memory address space could potentially recover the secrets, and they could also appear in crash dumps. To the best of our knowledge, there is no effective mitigation in pure Scala.

​
# PoW validation

​After previously reviewing the security of the Autolykos PoW, we performed another round of review focusing on its latest verification logic, and notably, the changes in the commit [eb0f85a](https://github.com/ergoplatform/ergo/commit/eb0f85ac48b0ee8194c12369faf4cc5f16954af9).

​The main relevant file is [AutolykosPowScheme](https://github.com/ergoplatform/ergo/blob/master/src/main/scala/org/ergoplatform/mining/AutolykosPowScheme.scala), and other important operations are for example implemented in
[HeadersProcessor](https://github.com/ergoplatform/ergo/blob/master/src/main/scala/org/ergoplatform/nodeView/history/storage/modifierprocessors/HeadersProcessor.scala) and [ModifierValidator](https://github.com/ScorexFoundation/Scorex/blob/master/src/main/scala/scorex/core/validation/ModifierValidator.scala).

​We checked that the implemented verification logic is consistent with that specified in the Autolykos specifications and that it is appropriately integrated into the block header validation logic.

​We believe the following points should be addressed:

* Stricter validation of `k` and `n`: although the class enforces `k<=32` (number of elements in the solution) and `n<31` (log2 of the total number of elements), weak could still be created from the authorised parameters. The `validate()` function may therefore have additional validation that `n` and `k` are equal to the intended
values.

* Assert that `k` and `n` are positive values, since currently negative ones (as `Int's) would pass the `assert` statements.
