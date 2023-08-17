# Archival Node Mode

The archival node mode in Ergo is a type of full node that stores all the blocks since the genesis block. In addition to checking the proofs of work and linking structure correctness, an archival node keeps a copy of the entire UTXO set, allowing it to validate arbitrary transactions.

## Features and Functionality

The archival node mode provides the following features and functionality:

- **Full Blockchain Storage**: An archival node stores every block since the genesis block, ensuring the complete history of the blockchain is available.
- **Proof-of-Work Verification**: The node checks the proofs of work for each block, ensuring the validity of the blockchain's consensus mechanism.
- **Linking Structure Correctness**: The node verifies the correctness of the linking structure, including parent block IDs and interlink elements.
- **UTXO Set Storage**: An archival node keeps a copy of the entire UTXO set, enabling it to validate arbitrary transactions.

To set up a full node, you can refer to [this page](manual.md) for detailed instructions.

