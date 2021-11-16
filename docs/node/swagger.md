# View the Swagger UI

A Swagger UI is available at [http://127.0.0.1:9053/swagger](http://127.0.0.1:9053/swagger). 

You use this UI to make API calls for advanced operations that are not available in the panel. Some examples of this are:

1. Creating non-standard transactions with registers and context variables.
2. Creating transactions that issue tokens.
3. Creating transactions that use certain boxes as inputs. 

Note that most methods in the API are protected and you would need to use your secret (from earlier) to access these methods. The following images show the process of setting this secret in the Swagger UI.

Navigate to the top of the page and click the "Authorize" button. Enter your secret in the form that pops-up as shown in the figure below.
![Enter API key](https://user-images.githubusercontent.com/23208922/69916784-450e6a80-1485-11ea-9bb5-681438d11970.png)

After the password is entered and you have clicked "Authorize", you will be shown the popup below:
![Logged in](https://user-images.githubusercontent.com/23208922/69916787-4a6bb500-1485-11ea-90c8-39b274d0f36d.png)

Now navigate to [http://127.0.0.1:9053/swagger#/wallet/walletAddresses](http://127.0.0.1:9053/swagger#/wallet/walletAddresses) **in the same tab where you entered the password** and click on "Try it out". You should see the same list of addresses as you saw earlier from the panel. 

![Get addresses](https://user-images.githubusercontent.com/23208922/69916855-f9a88c00-1485-11ea-8705-887ccffe6471.png)


# API


An Ergo node provides a REST API accessible via HTTP. The full API specification (in OpenAPI format) is available [here](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml). 

## Accessing the API

Once the node is running, the API can be accessed at [`127.0.0.1:9052`](http://127.0.0.1:9052). You can also use Swagger to make API requests by going to [`127.0.0.1:9052/swagger`](http://127.0.0.1:9052/swagger). To access protected API routes (such as for wallet), you must provide your secret phrase in the request headers `[api_key, Content-Type]`, or click the `Authorize` button in swagger and enter your secret phrase there.

## Setting an API key

For accessing any protected methods you must configure `apiKeyHash` parameter in the node configuration file:
```
   `scorex.restApi.apiKeyHash = "replace_this_with_your_unique_api_key_hash"`
```
   The parameter is the hex-encoded Blake2b256 hash of your secret phrase that will be used to authenticate your API requests. You can use this [Python script](https://gist.github.com/oskin1/704ef3fba8d40bb1e7691919bf1e9cf9/) or any other script to securely generate the secret and the `blake2b256` hash of it. The secret phrase acts as an API key and can be any string but please ensure that it remains secret and is not sent to any untrusted services. 

The following REST API endpoint also provides a (non-protected) method to compute the hash:
```
   [`/utils/hashBlake2b`](http://127.0.0.1:9052/swagger#/utils/hashBlake2b)
```
### Main methods:

* */wallet/init* and */wallet/restore* to create a wallet (and a secret mnemonic) and restore wallet from mnemonic
* */wallet/unlock* to unlock the wallet (it is unlocked after init but locked after restart)
* */wallet/lock* to lock the wallet
* */wallet/payment/send* to send a simple payment
* */wallet/status* to get wallet status
* */wallet/deriveNextKey* to derive a new key according to EIP-3 (BIP 44 implementation for Ergo)
* */wallet/balances* to get wallet balance (for all the addresses) 
* */wallet/transactions* to get wallet transactions (for all the addresses) 