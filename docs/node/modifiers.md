# Ergo Modifiers

## Block


Unlike most blockchain systems, an Ergo block consists of four parts:


* **Header**  is the minimum required to synchronise the chain and check PoW correctness. It also contains hashes of other sections.
* **BlockTransactions**  is a sequence of transactions included in this block.
* **ADProofs**  are proofs for transactions included in the corresponding BlockTransactions section of a block. Allows light clients to verify all the transactions and calculate new root hash.
* **Extension** stores additional data that does not correspond to previous sections. It contains interlinks and current parameters of the chain (when an extension belongs to a block at the end of the voting epoch).


## Header

| Field            | Size   | Description                                                     |
|------------------|--------|-----------------------------------------------------------------|
| version          | 1      | block version, to be increased on every soft- and hardfork      |
| parentId         | 32     | id of parent block                                              |
| ADProofsRoot     | 32     | hash of ADProofs for transactions in a block                    |
| stateRoot        | 32     | root hash (for an AVL+ tree) of a state after block application |
| transactionsRoot | 32     | root hash (for a Merkle tree) of transactions in a block        |
| timestamp        | 8      | block timestamp(in milliseconds since beginning of Unix Epoch)  |
| nBits            | 8      | current difficulty in a compressed form                         |
| height           | 4      | block height                                                    |
| extensionRoot    | 32     | root hash of extension section                                  |
| powSolution      | 75-107 | solution of Autolykos PoW puzzle                                |
| votes            | 3      | votes for changes in system parameteres, one byte per vote      |

Some of these fields may be calculated by the node by itself if it is in a certain mode:


- **parentId**: `if(status==bootstrap` AND `PoPoWBootstrap == false)`.
- **ADProofsRoot**: `if(status==regular` AND `ADState==false AND BlocksToKeep>0)`.
- **stateRoot**: `if(status==regular` AND `ADState==false AND BlocksToKeep>0)`.


## Extension


Extension is a key-value storage for a variety of data.

A key is always 2-bytes long, maximum size of a value is 64 bytes. Extension could be no more than of $16,384$ bytes.

Some keys have predefined semantics. In particular, if the first byte of a key equals to $0x00$, then the second byte defines parameter identifier, and the value defines value of the parameter. See Section~\ref{sec:params-table for details. Another predefined key is used for storing interlinks vector - the first byte of the key is $0x01$, the second one corresponds to index of the link in the vector and the value contains actual link (32 bytes) prefixed with the number of times it appears in the vector (1 byte). Other prefixes may be used freely.



