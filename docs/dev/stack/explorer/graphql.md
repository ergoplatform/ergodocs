# GraphQL


GraphQL queries allow flexible data fetching, reducing over-fetching and under-fetching. [gql.ergoplatform.com](https://gql.ergoplatform.com) is a GraphQL server on top of Ergo Platform's explorer database schema.


## Instances

Public community/partner-maintained explorer instances with GraphQL support:

- [gql.ergoplatform.com](https://gql.ergoplatform.com)
- [explore.sigmaspace.io/api/graphql](https://explore.sigmaspace.io/api/graphql)
- [graphql.erg.zelcore.io/](https://graphql.erg.zelcore.io/)
- [sigmaexplorer.org/](https://sigmaexplorer.org/)

## Testnet Instances

- [gql-testnet.ergoplatform.com/](https://gql-testnet.ergoplatform.com/)

## Resources

- [Ergo GraphQL Github](https://github.com/capt-nemo429/ergo-graphql)


## Examples

Play around with Apollo Studio on the GraphQL instance to explore the schema and make queries easily. 

Here are some query categories based on the schema:

- Fetching Box Details
- Fetching Multiple Boxes with Specific Conditions
- Fetching Specific Tokens
- Fetching Tokens Associated with a Box
- Fetching Inputs by Transaction or Box ID
- Fetching Transactions with Specific Conditions
- Fetching Data Inputs by Transaction or Box ID
- Fetching Block Headers by Height or Header ID
- Fetching Addresses with Balance and Transaction Count
- Fetching the State of the Mempool
- Fetching Blocks by Height or Header ID
- Fetching the Current State of the Blockchain
- Fetching Information about the Blockchain
- Fetching the Balance for a List of Addresses
- Fetching Transactions for Specific Addresses
- Fetching Box Details with Assets
- Fetching Unconfirmed Transactions from the Mempool
- Fetching Unconfirmed Boxes from the Mempool
- Fetching Unconfirmed Inputs from the Mempool
- Fetching Unconfirmed Addresses from the Mempool

Let's start with basic queries and gradually move to more complex ones.

### Fetching Box Details with Assets

Query to fetch details about a particular box including its associated assets:

```graphql
query {
  boxes(boxId: "your_box_id") {
    boxId
    transactionId
    value
    address
    assets {
      tokenId
      amount
    }
  }
}
```

### Fetching Transactions for Specific Addresses

Query to fetch transactions associated with a list of addresses:

```graphql
query {
  transactions(addresses: ["address1", "address2"]) {
    transactionId
    inclusionHeight
    timestamp
  }
}
```

### Fetching Balance for a List of Addresses

Query to fetch the balance for a list of addresses:

```graphql
query {
  addresses(addresses: ["address1", "address2"]) {
    address
    balance {
      nanoErgs
      assets(tokenId: "your_token_id") {
        amount
        tokenId
      }
    }
  }
}
```

### Fetching Details of Specific Tokens

Query to fetch details of specific tokens:

```graphql
query {
  tokens(tokenIds: ["token_id1", "token_id2"]) {
    tokenId
    boxId
    name
    description
  }
}
```

### Fetching State of the Blockchain

Query to fetch the current state of the blockchain:

```graphql
query {
  state {
    blockId
    height
    boxGlobalIndex
    transactionGlobalIndex
    network
    difficulty
  }
}
```

### Fetching Box Details with Assets

Query to fetch details about a particular box including its associated assets:

```graphql
query {
  boxes(boxId: "your_box_id") {
    boxId
    transactionId
    value
    address
    assets {
      tokenId
      amount
    }
  }
}
```

### Transactions

Query to fetch the first 10 transactions in the database:

```graphql
query {
  transactions(take: 10) {
    transactionId
    size
    inclusionHeight
    timestamp
    inputs {
      boxId
      transactionId
    }
    outputs {
      boxId
      value
    }
  }
}
```

### Advanced Query Example 1

Query to fetch a list of boxes created between specific block heights:

```graphql
query {
  boxes(minHeight

: 1000, maxHeight: 2000) {
    boxId
    creationHeight
    value
    address
  }
}
```

### Advanced Query Example 2

Query to fetch the first 5 transactions and the boxes linked to them:

```graphql
query {
  transactions(take: 5) {
    transactionId
    timestamp
    outputs {
      boxId
      value
      assets {
        tokenId
        amount
      }
    }
  }
}
```

In this query, we're asking for the first 5 transactions (`take: 5`). For each transaction, we're requesting `transactionId`, `timestamp`, and the `outputs` (which are boxes). For each box in `outputs`, we also want to fetch the `assets` related to that box, including the `tokenId` and `amount`.


### Mutation Example

Mutations are used to modify data. Let's submit a transaction using a mutation:

```graphql
mutation {
  submitTransaction(signedTransaction: {
    id: "your_transaction_id",
    inputs: [
      {
        boxId: "your_box_id",
        spendingProof: {
          proofBytes: "your_proof_bytes",
          extension: {}
        }
      }
    ],
    dataInputs: [
      {
        boxId: "your_data_input_box_id"
      }
    ],
    outputs: [
      {
        value: "1000",
        ergoTree: "your_ergo_tree",
        creationHeight: 1000,
        assets: [
          {
            tokenId: "your_token_id",
            amount: "100"
          }
        ],
        additionalRegisters: {},
        index: 0
      }
    ],
    size: 100
  }) 
}
```

In this mutation, we're submitting a transaction with a single input, data input, and output. For each of these, we fill in the necessary data according to the `SignedTransaction` input type in the schema.

