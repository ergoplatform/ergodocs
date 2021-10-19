An Ergo node provides a REST API accessible via HTTP. The full API specification (in OpenAPI format) is available [here](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml). 

## Accessing the API

Once the node is running, the API can be accessed at [`127.0.0.1:9052`](http://127.0.0.1:9052). You can also use Swagger to make API requests by going to [`127.0.0.1:9052/swagger`](http://127.0.0.1:9052/swagger). To access protected API routes (such as for wallet), you must provide your secret phrase in the request headers `[api_key, Content-Type]`, or click the `Authorize` button in swagger and enter your secret phrase there.

## Setting an API key

For accessing any protected methods you must configure `apiKeyHash` parameter in the node configuration file:

   `scorex.restApi.apiKeyHash = "replace_this_with_your_unique_api_key_hash"`

   The parameter is the hex-encoded Blake2b256 hash of your secret phrase that will be used to authenticate your API requests. You can use this [Python script](https://gist.github.com/oskin1/704ef3fba8d40bb1e7691919bf1e9cf9/) or any other script to securely generate the secret and the `blake2b256` hash of it. The secret phrase acts as an API key and can be any string but please ensure that it remains secret and is not sent to any untrusted services. 

The following REST API endpoint also provides a (non-protected) method to compute the hash:

   [`/utils/hashBlake2b`](http://127.0.0.1:9052/swagger#/utils/hashBlake2b)