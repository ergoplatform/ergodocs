# ErgoAuth: user authentication protocol between wallet applications and dApps

* Author: @MrStahlfelge
* Status: Implemented
* Created: 25-Jan-2022
* Last change: 24-Oct-2022
* License: CC0
* Forking: not needed

## Contents
- [ErgoAuth: user authentication protocol between wallet applications and dApps](#ergoauth-user-authentication-protocol-between-wallet-applications-and-dapps)
  - [Contents](#contents)
  - [Description](#description)
  - [Background And Motivation](#background-and-motivation)
  - [ErgoAuth authentication protocol](#ergoauth-authentication-protocol)
  - [Data Formats](#data-formats)
      - [Response body: ErgoAuthRequest](#response-body-ergoauthrequest)
  - [Cold wallet support](#cold-wallet-support)
  - [Implementation in wallet app](#implementation-in-wallet-app)
  - [Implementation in dApp](#implementation-in-dapp)
  - [Benefits for dApps](#benefits-for-dapps)

## Description
This EIP defines a standard for trustless authentication of users of a wallet app and an online dApp.

## Background And Motivation

dApps might want to validate if dApp users are really who they pretend to be. This is especially
useful for dApps that grant certain abilities to holders of special tokens. At the moment,
proving that a user owns a token can only be done by sending the token to a depositary address.
By sending the token, the user proofed to have access privileges to the token.
However, sending token around is not always desirable. Especially for valuable tokens, users might
not want to send it away, and doing two transactions (one to send it to the depositary address, one
to refund it back) costs both time and transaction fees.

To overcome this, ErgoAuth proposes a way to authenticate users trustless to have access to certain
addresses storing a box. The protocol is trustless in both ways: The users don't need to trust
the dApp, because the dApp does not get access to funds or secrets. The dApp don't need to trust
the users or the wallet app, because it can validate the authentication keys.

## ErgoAuth authentication protocol

An authentication with ErgoAuth is driven by a dApp that needs to authenticate a user.

1) The user enters the necessary information in the dApp's UI for the dApp to know if authentication
is necessary. For example, users might enter their P2PK address (or, instead of manually entering,
use ErgoPay to send the address to the dApp automatically).

2) The dApp determines that authenticating the user is needed. For this, the dApp prepares a unique
message that the wallet app should sign with a user's private key, and a SigmaBoolean that the user
needs to authenticate for. This might be a P2PK address wrapped in a SigmaBoolean.

3) The dApp presents an ErgoAuth link for the user to click and open the wallet app and a QR code
for mobile users to scan from within the wallet app.

4) The wallet application parses the QR code/link data and obtains a
`ErgoAuthRequestUrl` to fetch the actual `ErgoAuthRequest` data from
(see [Data Formats](#data-formats) section).

5) When `ErgoAuthRequest` is obtained, the wallet presents a screen showing that a dApp wants to
authenticate the user, and the address the request is for. The wallet app should also inform the
user that no funds or moved and no secrets will leave the device.
In a future enhancement, the Auth Request could be relayed to a Cold wallet device. This is an enhancement 
of EIP-0019 and would not change ErgoAuth protocol.

6) When the user agrees, the wallet app adds some own bytes to the obtained message from ErgoAuthRequest,
signs it  and sends the signed message to the ErgoAuthRequest's replyToUrl. The added bytes include
the host address the authentication request was fetched from, added right after the message defined
by the dApp. This way, dApp can check if a user authenticated via the right domain and there is no
middleman. 

8) The dApp validates the signed message. When successful, it can proceed with its flow.

## Data Formats

Wallet apps should be able to initiate ErgoAuth both by using URI schemes
(clickable links) or QR codes.

`ergoauth://<URL>`

An URL is provided without the https prefix. http communication is not allowed except for IP addresses
(in order to test within a local network).

Examples:
* `ergoauth://sigmavalley.io/auth/2021-16b8-66c4-b800-6e52-8ce4` will make the wallet app request
`https://sigmausd.io/auth/2021-16b8-66c4-b800-6e52-8ce4`
* `ergoauth://192.168.0.1/auth` will make the wallet app request
`http://192.168.0.1/auth`

#### Response body: ErgoAuthRequest

The wallet application should request URL and obtain the following data (json format)

```
ErgoAuthRequest:
  - signingMessage: String
  - sigmaBoolean: String (base64 from serialized SigmaBoolean)
  - userMessage: String (optional*)
  - messageSeverity: String (optional) "INFORMATION", "WARNING"
  - replyToUrl: String
```

(Remark: An Ergo p2pk address is a SigmaBoolean, so authenticating a wallet address is possible with this)

The **signingMessage** is a String that is not user-friendly to read in general, as it might contain
information the dApp adds to make it unique. If the signingMessage contains 0-byte character (unicode 0000), 
the part of the signingMessage before this sign is interpreted as the user prompt what he is going to sign for
and must be shown to the user.

If provided, the wallet application should show the **userMessage** and display the **messageSeverity**
in a suitable way. It should also show the replyToUrl's hostname so that the user knows to where 
the authentication is sent. The replyToUrl's hostname must be the same as the one the request was
fetched from - a wallet application should verify that.

After signing is performed, the
wallet must POST the following data to the dApp using **replyToUrl** from the
request (json format).

```
ErgoAuthResponse:
  - signedMessage: String
  - proof: String (Base64)
```

`signedMessage`: Message containing the `signingMessage` sent by the dApp with additional bytes added by the 
wallet. The addition of random bytes is done to prevent letting the user signing a message that might be used
for unwanted malicious tasks. Besides random based, the signed message must also contain the replyToUrl's 
hostname right after the original signing message. This way, the dApp can check if an authentication was done by
the user for that dApp, or if another middleman reuses an authentication.

`proof`: Output of signing `signedMessage`

In case there was an error building the ErgoAuthRequest on the dApp side, the dApp might reply
with an `ErgoAuthRequestError` to inform the user about the error:

```
ErgoAuthRequestError:
  - userMessage: String
```

The wallet application will show the user message to the user.

## Cold wallet support
Similar to [EIP-0019](eip19.md) for signing transactions from devices not connected to the internet 
("cold wallets"), ErgoAuth can be used to sign messages from cold wallets. This is transparent for 
dApps and handled by the wallet connected to the internet ("hot wallet").

For this, the `ErgoAuthRequest` must be transferred to the cold wallet via files or QR codes and 
the `ErgoAuthResponse` must be transferred back the same way.

The [interchange format to transfer chunks between hot wallet and cold wallet is similar to the one 
defined in EIP-0019](eip19.md#interchange-format), with name "EARQ" for ErgoAuthRequest and "EARS" 
for ErgoAuthResponse. Examples:

     {"EARQ":"{\"signingMessage\":\"....\",\"sigmaBoolean\":\"...\",\"userMessage\":\"...\",...}"}

     {"EARS":"{\"signedMessage\":\"....\",\"proof\":\"...\"}

The ErgoAuthRequest's `replyToUrl` field must be omitted to save data bandwidth.

Chunking as described in EIP-0019 is supported as well.

## Implementation in wallet app
[Ergo Wallet App #112](https://github.com/ergoplatform/ergo-wallet-app/issues/112)

## Implementation in dApp

[Ergo Appkit #157](https://github.com/ergoplatform/ergo-appkit/pull/157)

dApp: 
* [ErgoPay backend example](https://github.com/MrStahlfelge/ergopay-server-example/commit/9271f0ef890d6c8e63789f6c82b65595efe8549a)
* Login to https://www.paideia.im/

## Benefits for dApps
- A dApp or website don’t need to handle user's secrets (mnemonic/private keys), but can
safely validate if a user has access to certain Ergo addresses.
- dApp's users don't need to worry about security of their private keys as the
wallet guarantees they never leave the device. This is especially true if authentication
is done with a cold device.

