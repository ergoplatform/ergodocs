---
tags:
  - EIP
---

# EIP-0019 Cold Wallet: an interaction protocol between Hot and Cold mobile wallets

> 🔗 From [EIP-0019](https://github.com/ergoplatform/eips/blob/master/eip-0019.md)

* Author: @MrStahlfelge,@aslesarenko
* Status: Proposed
* Created: 18-August-2021
* License: CC0
* Forking: not needed 

## Contents
- [EIP-0019 Cold Wallet: an interaction protocol between Hot and Cold mobile wallets](#eip-0019-cold-wallet-an-interaction-protocol-between-hot-and-cold-mobile-wallets)
  - [Contents](#contents)
  - [Description](#description)
  - [Background And Motivation](#background-and-motivation)
  - [Cold Signing Problem](#cold-signing-problem)
  - [Simplified Signing using ReducedTransaction](#simplified-signing-using-reducedtransaction)
  - [Transaction Interchange](#transaction-interchange)
    - [ColdSigningRequest](#coldsigningrequest)
    - [ColdSigningResponse:](#coldsigningresponse)
    - [Interchange format](#interchange-format)
  - [Reference Implementation of Hot Wallet](#reference-implementation-of-hot-wallet)
  - [Reference Implementation of Cold Wallet](#reference-implementation-of-cold-wallet)
  - [Benefits](#benefits)

## Description 
This EIP defines a standard for cross-device interaction between "Hot" (online)
and "Cold" (offline) wallets for signing Ergo transactions.

## Background And Motivation

Mobile wallets (like [Ergo Android
Wallet](https://github.com/MrStahlfelge/ergo-wallet-android)) typically store
private keys (aka mnemonics) on the device.

However, modern mobile OSes (Android, iOS) as well as desktop PCs are always connected to the internet
and can be
[hacked](https://latesthackingnews.com/2021/07/30/apple-patched-zero-day-bug-under-attack-for-mac-and-ios-devices/)
and secrets [stolen](https://latesthackingnews.com/2021/07/06/numerous-trojanized-android-apps-caught-stealing-users-facebook-credentials/).
Screenreading and keystroke logging are system-independant ways to steal user data.

That is why specialized [hardware wallets](https://www.ledger.com/) are
considered much more secure to store private keys.

Another option for more security is to use "Cold" wallet - a device which is not connected
to the internet or better, with all connectivity turned-off and internet access blocked.
Candidates could be outdated (but still functioning) mobile devices with clean
factory setup or a Raspberry Pi with a fresh Raspbian setup and only Cold Wallet application installed.
As long as the device never connects to the internet, it is guaranteed that no secrets left the device.

Interaction with the Cold Wallet device can be done via QR codes (in case of mobile devices)
or by transferring files (in case of Raspberry Pi). For simplicity, only QR code is mentioned in the 
following text. This does not mean any restriction of the transportation method.

- A user creates a transaction in the Hot Wallet application and then presses a "Sign With Cold Wallet" button
- The Hot Wallet application shows a QR code with serialized transaction bytes on the screen
- User scans the QR code using the Cold Wallet device, signs the transaction after which QR code of the signed transaction is displayed.
- Then user scans the QR code of the signed transaction and sends it to blockchain.

The design of Ergo contracts allows for a simple and universal implementation
which we describe in [Reference Implementation](#reference-implementation-of-hot-wallet)
section.

In the following sections we:

- describe the main problem we need to solve; 
- describe a solution;  
- specify a protocol with two roles: HotWallet and ColdWallet which must be implemented by complying Wallet applications and 
- describe a reference implementation of both Hot and Cold roles in [Ergo Wallet for Android](https://github.com/MrStahlfelge/ergo-wallet-android).

## Cold Signing Problem

In the Ergo's eUTXO model a box can be protected by an arbitrary complex
contract (aka spending condition) and the spending transaction should satisfy
that condition by adding required context variables, creating expected number of
outputs with specific [registers](registers.md) etc. i.e. a special data structure called
`Context`. The Context should be created for each input of the transaction
and then passed to the Prover which will generate a signature for that input.
See [general overview of signing and
verification](https://github.com/ScorexFoundation/sigmastate-interpreter#sigma-language-background)
process in Ergo for details.

In general, the Context represents the current state of the blockchain and
includes current header, previous 10 headers, current height etc. This data can
be retrieved from blockchain nodes. This is possible on Hot Wallet device, but
is not possible on Cold Wallet device (there is no network connection).

At the same time the prover need to know both the Context data and the private
keys, which are stored on the Cold Wallet device, and so the Prover must run on
the Cold Wallet device.

And finally, which is the problem, we cannot transfer unsigned transaction along
with all the contexts for each input to the Cold Wallet via QR code. 

QR codes have limit of 4K bytes on the maximum size of serialized data. Most of
the transactions with required Contexts will exceed this limit.

## Simplified Signing using ReducedTransaction

To solve the problem of _cold signing_ we need a new data structure and
serialization format called `ReducedTransaction`.

```
ReducedTransaction:
  - unsignedTx: UnsignedTransaction
  - reducedInputs: Seq[ReducedInputData]
  - txCost: Int

UnsignedTransaction:
  - inputs: Seq[UnsignedInput],
  - dataInputs: Seq[DataInput],
  - outputCandidates: Seq[ErgoBoxCandidate]

UnsignedInput:
  - boxId: BoxId
  - extension: ContextExtension
```

ReducedInputData:
  - reductionResult: ReductionResult 
Thus, the `ReducedTransaction` instance contains unsigned transaction augmented with
one `ReductionResult` for each `UnsignedInput`. 

```
ReductionResult:
  - value: SigmaBoolean
  - cost: Long
```

Note that `UnsignedInput` object doesn't contain `ergoTree`, `additionalTokens`,
`additionalRegisters` and other properties of
[ErgoBox](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/4533b6a7ae86ada20f3136c70a67a920ae7c43e1/sigmastate/src/main/scala/org/ergoplatform/ErgoBox.scala#L51)
which are necessary to perform
[ErgoTree](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/1a1b003bc30e490d8b5af30e7670227e54e682c2/sigmastate/src/main/scala/sigmastate/Values.scala#L1014)
reduction and which are part of the
[Context](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/e5127f6743db824f7280881cd5c4ecd336075e2f/sigmastate/src/main/scala/org/ergoplatform/ErgoLikeContext.scala#L51)
data structure required by the
[prove](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/f24833d8d4572d77e4a93e5b69360335cb2d7dc1/sigmastate/src/main/scala/sigmastate/interpreter/ProverInterpreter.scala#L104)
method.

This is because those context data is not required to generate proof (aka signature)
once ErgoTree is reduced to ReductionResult containing sigma proposition.

Having the `ReducedTransaction` data structure the full transaction signing
consists of three steps

1) Create unsigned transaction and then reduce it in the current
blockchain context, which has connection to one of the network nodes. This step
is performed on Hot Wallet and produces ReducedTransaction without requiring
secret keys.

```
val ctx: BlockchainContext = ...
val unsignedIx = createTransaction(ctx, from, to, amountToSend, assets)
val prover = ctx.newProverBuilder.build // prover without secrets
val reducedTx: ReducedTransaction = prover.reduce(unsigned, 0)
```

2) Serialize ReducedTransaction data structure to bytes and then pass it to
the Cold Wallet via QR code.

3) Once scanned in the Cold Wallet, the ReducedTransaction object can be
deserialized back from bytes and then signed using prover configured with local
secrets.

```
val reducedTx = ReducedTransactionSerializer.fromBytes(reducedTxBytes)
val ctx: ColdBlockchainContext = ...
// create prover in the cold context using secrets stored on this device
val prover = ctx.newProverBuilder.withSecretStorage("storage.json").build
val signedTx = prover.signReduced(reducedTx)
```

It is important to note, that signatures for all inputs of the ReducedTransaction
can be generated directly, without script evaluation (aka script reduction) and
and thus, Cold Wallet don't need complex spending contexts.

## Transaction Interchange

For better security and usability additional data can be transfered between Hot
and Cold wallets via QR codes. Hot Wallet passes data to the Cold Wallet using
ColdSigningRequest data format and Cold Wallet replies back with ColdSigningResponse.

### ColdSigningRequest
Json format, holding
* reducedTx (mandatory): Base64-encoded `ReducedTransaction` as defined above
* sender (optional): P2PK address sending the transaction, can be used by cold wallets to determine which secret to use for signing the transaction
* inputs (mandatory): List of base64-encoded serialized input boxes, can be used by cold wallets to show the user which boxes are burnt

### ColdSigningResponse:
Json format, holding
* signedTx (mandatory): Base64-encoded `SignedTransaction`

### Interchange format
As QR codes are length-limited and it could be needed to transfer the data in chunks, it is needed to wrap the actual data sent by a small layer containing information about number of chunk pages and page index of a chunk. This is done by wrapping it in another JSON container with three properties:

* The actual chunk data, named CSR for ColdSigningRequest or CSTX for ColdSigningResponse
* property "p", 1-based page index of current chunk (optional if there is only one page)
* property "n", number of pages (optional if there is only one page)

Examples:
The QR code for a complete ColdSigningRequest contains the following data:

     {"CSR":"{\"reducedTx\":\"....\",\"sender\":\"9...\",\"inputs\":[\"...\"]}"}

The QR code for the first chunk of a ColdSigningResponse with 3 pages total looks like the following:

     {"CSTX":"{\"signedTx\":\"... (actual data, no valid JSON on its own)","n":3,"p":1}


In addition to using the above formats the following requirements are imposed on
Hot Wallet and Cold Wallets:

1) There should be a way for a given unsigned transaction on the HotWallet to
show QR code of ColdSigningRequest on the screen, and then scan the QR code of
the corresponding ColdSigningResponse.

2) There should be a way on ColdWallet to scan QR code of ColdSigningRequest,
show transaction details on the screen and allow user to either sign or reject.
If signed, the QR code of ColdSigningResponse should be shown.

## Reference Implementation of Hot Wallet 
* https://github.com/ergoplatform/ergo-wallet-android

## Reference Implementation of Cold Wallet
* https://github.com/ergoplatform/ergo-wallet-android

A special `ColdErgoClient` instance can be created to perform signing
operations. `ColdErgoClient` don't have connections to Ergo nodes and explorer,
moreover for better security, cold client can forbig operations if any
device connectivity is turned-on, such as WiFi, Bluetooth, NFC, Cellular etc.
Note, using ColdErgoClient is not strictly required and ordinary client can be
used instead, however ColdErgoClient allows this EIP to be easily supported in an
implementation of Cold Wallet application based on Appkit.

## Benefits

Any wallet can become compatible with this EIP by implementing HotWallet
role in addition to basic wallet features. 
Any Hot wallet implementation can interact with any Cold wallet implementation.
Users have an alternative to specialized hardware wallets and can gain more security 
for their funds stored on the Ergo Blockchain.
