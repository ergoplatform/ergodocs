# Indexed Node API

The Ergo Blockchain API provides a set of endpoints to interact with the Ergo blockchain and retrieve various information about transactions, boxes, tokens, and balances. This documentation will guide you through the usage of each API method, including example requests and responses.

An indexed node is available [here](http://128.253.41.49:9053/swagger), the base URL for all the indexed API endpoints available is `/blockchain/`.



Please note that this is a public instance, but for anything beyond testing you should host your own version of the [node](install.md) and enable the indexing by setting the `ergo.node.extraIndex` property to true in the config file.


## Methods

### GET /blockchain/indexedHeight

Retrieves the current block height that the indexer is at.


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

Retrieves a transaction by its ID.


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

Retrieves a transaction by its global index number.



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

Retrieves transactions by their associated address.



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

Retrieves a range of transaction IDs.



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

Retrieves a box by its ID.



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

Retrieves a box by its global index number.



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

Retrieves boxes by their associated address.



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

Retrieves unspent boxes by their associated address.



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

Retrieves a range of box IDs.



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

Retrieves boxes by their associated ergotree.



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

Retrieves unspent boxes by their associated ergotree.



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

Retrieves minting information about a token by its ID.



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

Retrieves confirmed and unconfirmed balance of an address.



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

This documentation covers the available API methods provided by the Ergo Blockchain API for retrieving information about transactions, boxes, tokens, and balances. You can use these endpoints to interact with the Ergo blockchain and build applications on top of it.


https://github.com/Luivatra/indexed-node-explorer