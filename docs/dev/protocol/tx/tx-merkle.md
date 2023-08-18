# Transaction Merkle Tree 

In Ergo, similar to Bitcoin where a miner builds a Merkle tree of block transactions and a Merkle tree of transaction witnesses (post the Segwit upgrade), a miner is required to construct a Merkle tree. This tree, however, combines both transactions and their corresponding spending proofs. The correct root hash of this tree is then included in the block header.

The construction of this tree follows a specific process. A leaf of the tree can either be empty or contain a data block of 64 bytes in length. If the data block is 64 bytes long, it includes the transaction identifier (a 256-bit digest of transaction bytes excluding spending proofs) and a 256-bit digest of all combined spending proofs for that transaction. The data for the $i-th$ transaction in the block (starting from 0) is authenticated by the $i-th$ leaf. 

A leaf is defined as $hash(0 || pos || data)$ if the $data$ is not empty (a prefix is added for domain separation), or $null$ if it is empty. Here, $pos$ represents the position of the transaction in the block. For internal nodes, a node is defined as $hash(1 || left\_child || right\_child)$ if either the left child or the right child of the node is not $null$, or $null$ if both are empty. If the root hash is $null$, it is replaced with all zeros (of the hash function output length).
