# Archival Node Mode in Ergo

The Archival Node Mode is the complete full node in Ergo. It is designed to store all blocks from the genesis block onwards. This mode not only checks the proofs of work and the correctness of the linking structure but also maintains a copy of the entire UTXO set. This allows it to validate any transaction, regardless of its complexity or origin.

## Key Features and Functionalities

The Archival Node Mode offers several unique features and functionalities:

- **Comprehensive Blockchain Storage**: The archival node mode ensures the storage of every block since the genesis block. This guarantees the availability of the complete history of the blockchain.

- **Proof-of-Work Verification**: This feature allows the node to check the proofs of work for each block. This is crucial for maintaining the integrity and validity of the blockchain's consensus mechanism.

- **Linking Structure Verification**: The node is capable of verifying the correctness of the linking structure. This includes parent block IDs and interlink elements, which are essential for the blockchain's operation.

- **UTXO Set Storage**: The archival node mode maintains a copy of the entire UTXO set. This feature enables it to validate any transaction, regardless of its complexity or origin.

For detailed instructions on setting up a full node, please refer to [this page](manual.md).