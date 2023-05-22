# APIs

Ergo provides several APIs that offer different functionalities and services for developers and users. These APIs allow interaction with the Ergo blockchain, access to network data, and integration of Ergo into various applications. 

Here are some of the APIs available:

- [Node API](https://git.io/fjqwb): The Node API provides comprehensive access to Ergo node functionalities, including blockchain data retrieval, transaction submission, wallet management, and more. It offers a wide range of endpoints to interact with the Ergo network programmatically.
- [Explorer API v1](https://api.ergoplatform.com/api/v1/docs/): The Explorer API allows users to explore the Ergo blockchain and retrieve information about blocks, transactions, addresses, and other relevant data. It provides a user-friendly interface to access blockchain data and monitor network activity.
versions but may have updated features or improvements.
- [Ergo.Watch API](https://api.ergo.watch/docs): The Ergo.Watch API provides access to various data and metrics related to the Ergo blockchain.
- [TokenJay API](https://api.tokenjay.app): The TokenJay API enables developers to interact with Ergo tokens and assets.
- [Spectrum API](https://api.spectrum.fi/v1/docs/): The Spectrum API provides several endpoints for different functionalities related to Automated Market Makers (AMM), price tracking, liquidity mining (LM), history, and more.
- [SkyHarbor API](https://docs.skyharbor.io): The SkyHarbor API provides various routes for interacting with the SkyHarbor marketplace, including accessing collection information, retrieving sales data, obtaining metrics, and utilizing the headless dApp functionality. 
- [Ergopad](https://api.ergopad.io/staking/ergopad/status/): Ergopad provides an API for staking on the Ergopad platform. 

These APIs provide various functionalities and data access points, allowing developers and users to leverage the power of Ergo blockchain in their applications, explore the blockchain network, interact with assets and tokens, and access decentralized exchange services.

## Mirrors

Some popular mirrors for the [explorer](explorer.md) and [graphql](graphql.md)

- [Ergo Explorer API v0 (1.0)](https://api.ergo.aap.cornell.edu/api/v0/docs/): This is another version of the Explorer API that provides similar functionalities.
- [Ergo Explorer API v1 (1.0)](https://api.ergo.aap.cornell.edu/api/v1/docs/): This version of the Explorer API offers functionalities similar to the previous 
- [sigmaexplorer](https://api.sigmaexplorer.org/swagger/index.html): sigmaexplorer hosts a copy of the explorer using a GraphQL backend. 
- [graphql.ergo.aap.cornell.edu](https://graphql.ergo.aap.cornell.edu/) is a GraphQL Server for the Ergo blockchain. It also has an explorer [ergo.aap.cornell.edu](https://ergo.aap.cornell.edu/).
- [api.ergo.aap.cornell.edu](https://api.ergo.aap.cornell.edu/) provides an Explorer API and Web UI for the Ergo blockchain. It also hosts a node at this [address](http://128.253.41.49:9053/).


## How to Use the APIs (For Beginners)

If you are new to using APIs and want to get started with Ergo's APIs, here are some steps to help you get going:

1. **Choose an API**: Determine which Ergo API suits your needs. Consider the specific functionalities and data you require for your application or project.

2. **Read the Documentation**: Visit the API documentation for the chosen API. The documentation provides detailed information on the available endpoints, parameters, and response formats. Familiarize yourself with the API's capabilities and explore any example calls provided.

3. **Understand the Endpoints**: Review the list of available endpoints and their purposes. Each endpoint serves a specific function and allows you to retrieve or interact with different data or services.

4. **Authenticate (If Required)**: Some APIs may require authentication to access certain endpoints or perform specific actions. Refer to the API documentation to understand the authentication mechanisms and requirements. Obtain any necessary credentials or tokens to authenticate your requests.

5. **Test Endpoints**: Use an API testing tool like Postman or cURL to send requests to the API endpoints. Start with simple requests to retrieve basic data, such as blockchain information or transaction details. Verify that you receive the expected responses.

6. **Explore Data Retrieval**: Experiment with different endpoints to retrieve the data you need. For example, if you want to retrieve address-specific data, use the appropriate endpoint and provide the required parameters, such as the address. Study the response structure and extract the relevant information for your application.

7. **Integrate into Your Application**: Once you are comfortable with retrieving data, integrate the API calls into your application or project. Use the retrieved data to power your application's features or display blockchain information to users.

8. **Handle Errors**: Be prepared to handle potential errors or exceptions that may occur during API interactions. Refer to the API documentation to understand the possible error responses and implement appropriate error handling in your code.

9. **Stay Updated**: Keep an eye on the API documentation and any announcements or updates related to the Ergo APIs. APIs may evolve over time, and new functionalities or improvements could be introduced. Stay informed to leverage the latest capabilities.

10. **Seek Community Support**: If you encounter any difficulties or have questions while using the APIs, reach out to the Ergo community for support. Join forums, chat groups, or developer communities where you can connect with other developers working with Ergo. Sharing knowledge and experiences can be helpful in resolving any challenges you may face.

Remember, APIs are powerful tools that allow you to interact with the Ergo blockchain and incorporate its features into your applications. Take your time to understand the API functionalities, experiment with different endpoints, and gradually build your integration to harness the full potential of Ergo's APIs.