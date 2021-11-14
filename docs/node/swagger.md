# View the Swagger UI

A Swagger UI is available at [http://127.0.0.1:9053/swagger](http://127.0.0.1:9053/swagger). You had already used it earlier to compute the hash of your secret. 
You can also use this UI to make API calls for advanced operations that are not (yet) available in the panel. Some examples of this are:

1. Creating non-standard transactions with registers and context variables.
2. Creating transactions that issue tokens.
3. Creating transactions that use certain boxes as inputs. 

A future article will discuss each of these operations in detail. 

Note that most methods in the API are protected and you would need to use your secret (from earlier) to access these methods. The following images show the process of setting this secret in the Swagger UI.

Navigate to the top of the page and click the "Authorize" button. Enter your secret in the form that pops-up as shown in the figure below.
![Enter API key](https://user-images.githubusercontent.com/23208922/69916784-450e6a80-1485-11ea-9bb5-681438d11970.png)

After the password is entered and you have clicked "Authorize", you will be shown the popup below:
![Logged in](https://user-images.githubusercontent.com/23208922/69916787-4a6bb500-1485-11ea-90c8-39b274d0f36d.png)

Now navigate to [http://127.0.0.1:9053/swagger#/wallet/walletAddresses](http://127.0.0.1:9053/swagger#/wallet/walletAddresses) **in the same tab where you entered the password** and click on "Try it out". You should see the same list of addresses as you saw earlier from the panel. 

![Get addresses](https://user-images.githubusercontent.com/23208922/69916855-f9a88c00-1485-11ea-8705-887ccffe6471.png)