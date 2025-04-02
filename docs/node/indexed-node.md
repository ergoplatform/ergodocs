---
tags:
  - Indexed Node
  - Node
  - API
  - Blockchain
  - Explorer
---

# Indexed Node API

An indexed Ergo node provides an enhanced set of API endpoints (beyond the standard [Node API](swagger.md)) for querying blockchain data efficiently. These endpoints allow retrieving information about transactions, boxes, tokens, and balances based on various criteria like address, ErgoTree, or global index. This documentation guides you through the usage of these indexed API methods, including example requests and responses.

A public instance of an indexed node's API explorer (Swagger UI) is available [here](http://128.253.41.49:9053/swagger). The base path for all indexed API endpoints described below is `/blockchain`.


/// admonition | Disclaimer
Please note that this is a public instance intended for exploration and testing. For production use or heavy querying, you should host your own instance of an [Ergo node](install.md) and enable indexing by setting `ergo.node.extraIndex = true` in the node's configuration file.
///





## Methods

### GET /blockchain/indexedHeight

Retrieves the current block height up to which the node's indexer has processed the blockchain.


**Request:**

```
GET /indexedHeight
```

**Response:**

```json
{
  "indexedHeight": 123456
}
```

### GET /blockchain/transaction/byId/{txId}

Retrieves details of a specific transaction by its ID.


**Request:**

```
GET /transaction/byId/123abc
```

**Response:**

```json
{
  "transactionId": "123abc",
  "blockHeight": 1234,
  "inputs": [
    {
      "boxId": "abc123",
      "value": 1000000
    }
  ],
  "outputs": [
    {
      "boxId": "def456",
      "value": 500000
    },
    {
      "boxId": "ghi789",
      "value": 500000
    }
  ]
}
```

### GET /blockchain/transaction/byIndex/{txIndex}

Retrieves details of a specific transaction by its global index number (sequential order in the blockchain).



**Request:**

```
GET /transaction/byIndex/1234
```

**Response:**

```json
{
  "transactionId": "123abc",
  "blockHeight": 1234,
  "inputs": [
    {
      "boxId": "abc123",
      "value": 1000000
    }
  ],
  "outputs": [
    {
      "boxId": "def456",
      "value": 500000
    },
    {
      "boxId": "ghi789",
      "value": 500000
    }
  ]
}
```

### POST /blockchain/transaction/byAddress

Retrieves a list of transactions associated with a given address (either as input or output). Requires the address in the request body.



**Request:**

```
POST /transaction/byAddress
Content-Type: application/json

{
  "address": "your_address"
}
```

**Response:**

```json
{
  "transactions": [
    {
      "transactionId": "123abc",
      "blockHeight": 1234,
      "inputs": [
        {
          "boxId": "abc123",
          "value": 1000000
        }
      ],
      "outputs": [
        {
          "boxId": "def456",
          "value": 500000
        },
        {
          "boxId": "ghi789",
          "value": 500000
        }
      ]
    },
    {
      "transactionId": "456def",
      "blockHeight": 5678,
      "inputs": [
        {
          "boxId": "jkl012",
          "value": 2000000
        }
      ],
      "outputs": [
        {
          "boxId": "mno345",
          "value": 1000000
        },
        {
          "boxId": "pqr678",
          "value": 1000000
        }
      ]
    }
  ]
}
```

### GET /blockchain/transaction/range

Retrieves a list of transaction IDs within a specified global index range (`start` and `end` query parameters).



**Request:**

```
GET /transaction/range?start=0&end=100
```

**Response:**



```json
{
  "transactionIds": ["123abc", "456def", "789ghi", ...]
}
```

### GET /blockchain/box/byId/{boxId}

Retrieves details of a specific box by its ID.



**Request:**

```
GET /box/byId/abc123
```

**Response:**

```json
{
  "boxId": "abc123",
  "value": 1000000,
  "ergoTree": "your_ergo_tree",
  "address": "your_address"
}
```

### GET /blockchain/box/byIndex/{boxIndex}

Retrieves details of a specific box by its global index number.



**Request:**

```
GET /box/byIndex/1234
```

**Response:**

```json
{
  "boxId": "abc123",
  "value": 1000000,
  "ergoTree": "your_ergo_tree",
  "address": "your_address"
}
```

### POST /blockchain/box/byAddress

Retrieves a list of boxes associated with a given address. Requires the address in the request body.



**Request:**

```
POST /box/byAddress
Content-Type: application/json

{
  "address": "your_address"
}
```

**Response:**

```json
{
  "boxes": [
    {
      "boxId": "abc123",
      "value": 1000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    },
    {
      "boxId": "def456",
      "value": 2000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    }
  ]
}
```

### POST /blockchain/box/unspent/byAddress

Retrieves a list of *unspent* boxes associated with a given address. Requires the address in the request body.



**Request:**

```
POST /box/unspent/byAddress
Content-Type: application/json

{
  "address": "your_address"
}
```

**Response:**

```json
{
  "boxes": [
    {
      "boxId": "abc123",
      "value": 1000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    },
    {
      "boxId": "def456",
      "value": 2000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    }
  ]
}
```

### GET /blockchain/box/range

Retrieves a list of box IDs within a specified global index range (`start` and `end` query parameters).



**Request:**

```
GET /box/range?start=0&end=100
```

**Response:**

```json
{
  "boxIds": ["abc123", "def456", "ghi789", ...]
}
```

### POST /blockchain/box/byErgoTree

Retrieves a list of boxes protected by a specific ErgoTree script (provided in hex format in the request body).



**Request:**

```
POST /box/byErgoTree
Content-Type: application/json

{
  "ergoTree": "your_ergo_tree"
}
```

**Response:**

```json
{
  "boxes": [
    {
      "boxId": "abc123",
      "value": 1000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    },
    {
      "boxId": "def456",
      "value": 2000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    }


  ]
}
```

### POST /blockchain/box/unspent/byErgoTree

Retrieves a list of *unspent* boxes protected by a specific ErgoTree script (provided in hex format in the request body).



**Request:**

```
POST /box/unspent/byErgoTree
Content-Type: application/json

{
  "ergoTree": "your_ergo_tree"
}
```

**Response:**

```json
{
  "boxes": [
    {
      "boxId": "abc123",
      "value": 1000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    },
    {
      "boxId": "def456",
      "value": 2000000,
      "ergoTree": "your_ergo_tree",
      "address": "your_address"
    }
  ]
}
```

### GET /blockchain/token/byId/{tokenId}

Retrieves information about a specific token (name, description, decimals, etc.) by its ID. Note that the token ID is the ID of the first input box in the token issuance transaction.



**Request:**

```
GET /token/byId/123abc
```

**Response:**

```json
{
  "tokenId": "123abc",
  "name": "Your Token",
  "description": "Description of your token",
  "totalSupply": 1000000,
  "decimals": 8,
  "issuer": "your_address"
}
```

### POST /blockchain/balance

Retrieves the confirmed and unconfirmed ERG and token balances for a given address (provided in the request body).



**Request:**

```
POST /balance
Content-Type: application/json

{
  "address": "your_address"
}
```

**Response:**

```json
{
  "confirmedBalance": 1000000,
  "unconfirmedBalance": 500000
}
```

This documentation covers the indexed API methods provided by an Ergo node with `extraIndex = true`. You can use these endpoints to efficiently query blockchain data and build applications on top of Ergo.


An example explorer utilizing these indexed endpoints can be found here: https://github.com/Luivatra/indexed-node-explorer
