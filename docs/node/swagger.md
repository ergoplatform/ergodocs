# Swagger UI

An Ergo node provides a REST API accessible via HTTP. The full API specification (in OpenAPI format) is available [here](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml). When running the node, a user interface for Swagger is available at `127.0.0.1:9053/swagger`. 

> Note: 127.0.0.1 is your local machine. 

You use this UI to make API calls for advanced operations that are not available in the panel such as;

1. Creating non-standard transactions with [registers](registers.md) and context variables.
2. Creating transactions that issue tokens.
3. Creating transactions that use certain boxes as inputs. 


## Accessing the API

Once the node is running, the API can be accessed at `127.0.0.1:9052`. 

To have a look at the methods without setting up your own node, check out one of the public nodes like [204.48.31.129:9053/swagger#](http://204.48.31.129:9053/swagger#)

To access protected API routes, you must provide your secret phrase in the request headers `[api_key, Content-Type]`. Alternatively, you can Authorize via the web interface in your browser by clicking the `Authorize` button in swagger and entering your secret phrase there.


Note that most methods in the API are protected and you would need to use your secret (that you configured earlier) to access these methods. The following images show the process of setting this secret in the Swagger UI.

Navigate to the top of the page and click the `"Authorize"` button. 

Enter your secret in the form that pops-up as shown in the figure below.
![Enter API key](https://user-images.githubusercontent.com/23208922/69916784-450e6a80-1485-11ea-9bb5-681438d11970.png)

After the password is entered and you have clicked `"Authorize"`, you'll see the popup below:

![Logged in](https://user-images.githubusercontent.com/23208922/69916787-4a6bb500-1485-11ea-90c8-39b274d0f36d.png)

Now navigate to `127.0.0.1:9053/swagger#/wallet/walletAddresses` **in the same tab where you entered the password** and click `"Try it out"`. 

You should see the same list of addresses as you saw earlier from the panel. 

![Get addresses](https://user-images.githubusercontent.com/23208922/69916855-f9a88c00-1485-11ea-8705-887ccffe6471.png)

Please note that Swagger will accept any password in the UI, but will fail to execute commands if the password provided is incorrect. If you are certain the password you're using is correct, this issue can occur during database corruption. First, attempt to restart and see if the node can fix itself.  Otherwise, a resync will be required. 


## Main methods

* `/wallet/init` and `/wallet/restore` to create a wallet (and a secret mnemonic) and restore wallet from mnemonic
* `/wallet/unlock` to unlock the wallet (it is unlocked after init but locked after restart)
* `/wallet/lock` to lock the wallet
* `/wallet/payment/send` to send a simple payment
* `/wallet/status` to get wallet status
* `/wallet/deriveNextKey` to derive a new key according to EIP-3 (BIP 44 implementation for Ergo)
* `/wallet/balances` to get wallet balance (for all the addresses) 
* `/wallet/transactions` to get wallet transactions (for all the addresses) 


### Example: Deriving Addresses

Navigate to `localhost:9053/swagger#/wallet/walletDeriveKey` 

and then click *Try it out*

```bash
"derivationPath": "m/44'/429'/0'/0/0" 
```





