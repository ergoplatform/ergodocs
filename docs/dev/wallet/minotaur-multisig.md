# Multi-Signature Wallet

## Introduction

Minotaur wallet is a multi-platform wallet developed by *minotaur-ergo* using TypeScript.

In this project, the wallet is extended to support multiple signatures.

A multi-signature (*multi-sig*) wallet uses more than one private key to authorize transactions.

Such a wallet can be managed by a single user holding multiple private keys, multiple users holding a single key each, or any combination of the two scenarios.

In a multi-sig wallet with *M* private keys, depending on its configurations, any transaction may require *N* signatures, where *1<=N<=M*.

The project accomplishments are as follows:

The end user(s):

  - can easily create a multi-signature wallet,
  - can see their wallet balance,
  - can sign their transactions in the wallet.

The software provides an automatic transfer method that safely processes all signatures and communications between private-key holders.

## Explanation

In Ergo blockchain, a transaction is prepared in two steps before being submitted to the
transaction pool:

* required commitments are generated
* The transaction is signed using the commitments

These steps are performed automatically and transparently (hidden from the user) in any wallet. However, signing a multi-sig transaction involves more sophisticated steps, as explained in [EIP 11](https://github.com/ergoplatform/eips/pull/8).
In other words, the steps mentioned above cannot be performed transparently since the commitments and signatures must be shared between all signers.

The procedure can be explained more clearly using the following example:

Consider a 3-out-of-4 wallet, and let us name the 4 private-key holders Alice, Bob, Carol, and Dani.

The wallet has been configured so that at least 3 signers must sign a transaction.

Suppose that Alice, Bob, and Carol agree to sign a transaction.

In order to do so, 

1. Alice creates an unsigned transaction and generates her commitment.
2. Then, she sends the transaction and the public part of her commitment to Bob.
3. Bob generates his commitment and appends its public parts to Alice's commitment.
4. Then, He forwards the transaction and the two-part commitment to Carol.
5. Carol generates her commitment. At this step, all 3 required commitments are available.
6. Therefore, Carol adds her signature to the transaction and sends it back to Bob.
7. Similarly, Bob adds his signature to the transaction and forwards it to Alice.
8. Finally, Alice completes the transaction signing by adding her signature to it.
9. Now she can submit the signed transaction to the transaction pool.

The minotaur multi-sig wallet facilitates the whole process in a user-friendly manner.

## Design Details
### Wallet Creation
Implementation of this project introduces a new type of wallet, the so-called multi-sig wallet, to the Minotaur wallet.
In order to create a new functional multi-sig wallet,
each signer must configure a copy of it on his/her device by applying the following four steps:

* A proper name is entered for the personal copy of the multi-sig wallet.
    * Names entered by different signers can be different.
* The total number of signers, *M*, and also the number of required signs, *N*, are entered.
    * *M* can be maximally 20. All signers must enter the same values for these two numbers.
* Each signer must enter his/her private key and the public key of all other signers in the multi-sig wallet.
    * For convenience, it is supposed that each signer already has a normal wallet in Minotaur so that his/her public/private key can be retrieved.
    * For all other signers, either of the following solutions may be applied:
      * Their extended public keys are entered. In this case, signers can derive the address of the multi-sig wallet.
      * Their addresses are entered.
      * In this case, it is **not** possible for signers to derive the address of the multi-sig wallet.
* The address of the multi-sig wallet is displayed to each signer.
  The signer's copy of the multi-sig wallet is created as soon as he/she approves the address.

### Wallet Display Parts.
Since the implementation is based on a standard wallet, the following functionalities of the underlying standard wallet already work in the multi-sig wallet too:

* Extracting fund information from the Ergo blockchain
* Displaying transaction history
* Creating unsigned transaction
* Displaying addresses
* Displaying assets
* Connecting to dApps

However, two principal parts must be implemented: the address derivation and the "sign transaction" modal.

#### Address Derivation

When deriving new addresses, two important facts must be taken into account.
First, to guarantee a unique address for the multi-sig wallet to be derived on all signer copies, a unique address-derivation algorithm must be applied everywhere.
The applied algorithm is as follows:

For a specified path, using each signer's extended public key, an address is derived for that signer.

The list of derived addresses for all signers is used to compile a multi-sig contract like:

```scala
atLeast(
  N,
  Coll(
    PK(Address1),
    PK(Address2),
    .
    .
    .
    PK(AddressM)
  )
)
```

The contract mentioned above results in distinguishable (different) addresses when two signer addresses swap. In order to prevent this, the list of signers' addresses are always sorted before being used in the contract.

Second, the Sigma-rust library cannot compile any contract. One might think of Node as a solution, but it does not fulfil the project criteria since it disables cold signing. Our solution to this problem is to manually create the required ergiTree array as follows:

* The first byte in the array has a value of 10.
* The number of constant values in the contract.
    * This number equals *M+1* and is encoded as a variable-length quantity (VLQ).
* The number of required signs, *N*.
    * This number starts with a byte with value 04 that denotes the integer type, followed by the value of *N* encoded as a VLQ.
* For each public key (*M* times), 35 bytes are used: 2 bytes with value 08cd, followed by 33 bytes representing the public key
* A byte with value 98, indicating "atLeast"
* Two bytes, with values 73 and 00, respectively.
    * The value 00 indicates the VLQ representation of the index of value *N* in the list of constants.
* A constant byte with value 83, followed by the VLQ representation of *M*, and a constant byte with value 08
* For each public key (*M* times), a byte with value 73, followed by the VLQ representation of the index of the public key in the list of constants

#### "Sign transaction" modal

After an unsigned transaction is created, the Minotaur wallet displays a modal so the user can confirm his/her password and sign the transaction.
Similarly, the same modal is displayed for a multi-sig wallet too.

When a user enters his/her password into the modal, a commitment is generated, whose private part is stored locally, and then the following information is displayed in the form of a JSON string:

```JSON
MCR-{
  "tx": <reduced transaction bytes>,
  "boxes": [<encoded boxes>],
  "commitments": <commitments encoded>
} 
```
A user must share this string with other wallets through any communication.

For convenience, a *copy to clipboard* button has been provided in the modal.

As soon as any other signer enters the JSON string into his/her wallet, the wallet displays information regarding the transaction.

The signer generates personal commitment by entering his/her password and approving the transaction.

The newly created commitment is merged with the received one, and a new JSON string is presented.

This new string must be passed to the next signer.

The process repeats until the last required signer generates his/her commitment.

At this moment, the last signer signs the transaction and creates a JSON string containing the following information:

```JSON
{
  "tx": <reduced transaction bytes>,
  "boxes": [<encoded boxes>],
  "commitments": <commitments encoded>,
  "simulated": [<list of simulated public keys for all inputs>]
  "signed": [<list of all signed public keys for all inputs + my own public keys for all inputs>]
  "partialTx": <partially signed tx proposition bytes>
}
```
Similar to the process of commitment generation,
every other signer must enter the received JSON string in his/her wallet, sign the transaction, generate a new JSON string, and pass it to the next signer.
After signing the transaction, the last signer can submit it to the blockchain.

## CoSigning Server

A [cosigning server](https://github.com/lazypinkpatrick/cosigning-server) was designed and implemented in order to simplify communications between wallets.

The server can store data for any specific address.

Moreover, for any address, associated data stored on the server can be requested.

The server keeps data for 10 minutes only.

This server has two APIs:

### **/put** 

> Stores data on the server for any specific address:

- We assume that each wallet uses the address derived from the path `m/44'/429'/0'/0/0`.
- The JSON string passed to this API is something like the example below, where the `"type": <value>` pair is used to specify the data category:

```JSON
{
    "sender": "me",
    "message": "",
    "type": "create",
    "receiver": ["user1", "user2"]
}
```
### **/get** 
> Gets a list of requested data for a specified address:

- For a given triplet of (*ID*, *address*, *value*), this API gets, from the server, all messages with an ID greater than the given one and returns data associated with the given *address* that would have a type of *value*.

In this implementation, we assume that a new transaction is highlighted with the `"type": "create"` pair,
while all sub-messages are linked to their parent transaction using the transaction ID as their type value, i.e., `"type": <txId>`

Our implemented scenario for signing a transaction using this server is as follows:

* The first signer creates an unsigned transaction.
* If the user selects the "sign via cosigning server" option, he/she sends the following JSON string to all other signers in the multi-sig wallet:


```JSON
{
  "type": "create",
  "tx": <reduced tx>
  "boxes": [<encoded boxes>]
}
```
Other signers receive this JSON string and generate a party for it.


The first signer also creates his/her commitment and sends the following JSON to all other party members:


```JSON
{
  "type": "commitment",
  "commitments": [<my encoded commitment for all inputs>]
}
```

* Every other signer generates a commitment by entering his/her password.
  At the same time, entering the password by the signer indicates to the wallet that he/she accepts the transaction and is willing to sign it.
* When the number of commitments reaches the required count,
  every wallet signs the transaction and sends it to all other signers in the following format:
```json
{
  "type": "sign"
  "simulated": [<list of simulated public keys; the first signer generated this list, and no one has changed it yet.>]
  "signed": [<list of signatures in this transaction; everyone must append his/her public key to this list.>]
  "partial": <partially signed tx in the base64 format>.
}
```
* Every wallet, when it receives a new partially-signed transaction, checks the number of signatures on it:
  - If the wallet has not already signed the transaction, it is signed and published
  - If the number of signatures on the received transaction is greater than that on the local copy, the local copy is replaced with the received one
  - If all commitment generators have already signed the transaction, the wallet submits it to the blockchain, and the process is completed.



## Signing Server for Multi-Sig Communication (ErgoHack IX)

### Introduction



Minotaur is the first multi-signature wallet developed for Ergo. A multi-signature wallet, or multi-sig wallet, uses more than one private key to authorize transactions. Such a wallet can be managed by a single user holding multiple private keys, multiple users holding a single key each, or any combination of the two scenarios. In a multi-sig wallet with *M* private keys, depending on its configurations, any transaction may require *N* signatures, where *1 <= N <= M*.

Signing any multi-sig transaction on the Ergo chain consists of two major steps that must be completed by any *N* signer(s) among the *M* key-holders:

1. Generating required commitment(s) and sharing them with all other signers (*N* times).
2. Signing the transaction using gathered commitments (*N* times).

In Minotaur, an *N*-sig transaction is performed as follows:

- The first signer, i.e., a key-holder who creates the transaction, generates his/her own commitment(s) and, including all other required data, sends it to a second signer.
- A second signer receives the transaction data, appends his/her own commitment(s) to it, and sends it to a third signer.
- The process is repeated by all other signers, except the last one.
- The last signer receives commitments of all other signers. He/She generates his/her own commitment(s) and appends it to the transaction data, and finally signs the transaction. Then, the partially signed transaction is sent to another signer.
- Any middle signer signs the transaction and passes it to another one.
- The last one who adds the last signature to the transaction publishes the fully-signed transaction.

The process is error-prone. In fact, any human error in sending commitment(s) and using invalid commitment sets results in an invalid, and thus incomplete, transaction. Such failures have been reported frequently.

In order to solve this problem, we introduce the Minotaur Signing Server, which manages the signing process and ensures a valid and completed transaction.

For more details and to access the code, please visit the following repositories:

- [Minotaur Wallet Code](https://github.com/minotaur-ergo/minotaur-wallet/tree/ergo-hack-multi-sig-signing-server)
- [Minotaur Signing Server (MSS) Code](https://github.com/minotaur-ergo/Minotaur-Signing-Server/tree/fix-some-incompatibilities)


### The Minotaur Signing Server

The Minotaur Signing Server (MSS) manages the steps of transaction signing. The MSS provides a safe, reliable, secure, and error-free channel for data transition among signers. Therefore, it can guarantee that every signer receives and uses correct transaction data.

The workflow of the MSS is as follows:

1. First, each of the wallet key-holders must generate an asymmetric key-pair for communication with the server. We refer to these keys as the communication private and public keys. The MSS expects every signer to sign his/her communication public key with his/her transaction-signing key in order to confirm the signer's identity.
2. The MSS needs the multi-sig wallet details, including the extended public key of each signer and also the number of required signatures. Any of the key-holders can provide the MSS with this data. It is only after receiving this data that the MSS allows for the processing of any transaction.
3. At this stage, the multi-sig wallet setup is completed, and any number of transactions can be started. A new transaction is started as follows:
   - The person who creates the transaction sends it to the MSS. From now on, each of the wallet holders will see the transaction on their multi-sig communication page of their connected Minotaur. The representation of data on the page has not been altered by the introduction of MSS, and the user may not sense any UI change.
   - Any of the signers can select the desired transaction and generate their commitment(s) for it. By doing so, the private part of the commitment(s) is stored in Minotaur, and its public part is sent to the MSS.
   - Anyone who receives the transaction also receives all previous public commitments. He/She can add his/her own commitment(s) as described above.
4. As soon as the server receives all *N* commitments, the transaction is automatically sent for signing. In case any simulated signatures are required, they are created by the MSS. Moreover, any commitments that arrive after this point are rejected.
5. At this stage, anyone who committed the transaction can sign it and send his/her signature to the MSS.
6. As soon as all *N* signatures arrive at the MSS, it automatically completes the transaction and sends it on the blockchain.
