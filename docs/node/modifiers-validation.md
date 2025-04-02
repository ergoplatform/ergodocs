---
tags:
  - Modifiers
  - Validation
  - Node
  - Technical
  - Consensus
---

# Ergo Modifiers Validation

This section contains a list of all consensus-critical validation rules that every node in the network should perform; rules that are not listed in this table should not be considered consensus-critical and enforced by the network.

Every rule is enumerated and is initially activated.

Rules that could not lead to money printing and are not enforced by serialisers may be disabled later by a miner
voting via soft forks, while new rules may also be added at the same time.



**Transaction validation:**

 **Id** | **Validation rule**                                                                                                        | **Soft-forkable** | **Active** | **Modifiers**   
--------|----------------------------------------------------------------------------------------------------------------------------|-------------------|------------|-----------------
 100    | A transaction should have at least one input.                                                                              | x            | √     | ErgoTransaction 
 101    | A transaction should have at least one output.                                                                             | x            | √     | ErgoTransaction 
 102    | A number of transaction inputs should not exceed 32767.                                                                    | x            | √     | ErgoTransaction 
 103    | A number transaction data inputs should not exceed 32767.                                                                  | x            | √     | ErgoTransaction 
 104    | A number of transaction outputs should not exceed 32767.                                                                   | x            | √     | ErgoTransaction 
 105    | Erg amount for a transaction output should not be negative.                                                                | x            | √     | ErgoTransaction 
 106    | Sum of transaction output values should not exceed 9223372036854775807.                                                    | x            | √     | ErgoTransaction 
 107    | There should be no duplicate inputs.                                                                                       | x            | √     | ErgoTransaction 
 108    | All token amounts of transaction outputs should be positive.                                                               | x            | √     | ErgoTransaction 
 109    | A number of tokens within a box should not exceed 255 and sum of assets of one type should not exceed 9223372036854775807. | x            | √     | ErgoTransaction 
 111    | Every output of the transaction should contain at least <minValuePerByte * outputSize> nanoErgs.                           | √            | √     | ErgoTransaction 
 112    | Transaction outputs should have creationHeight not exceeding block height.                                                 | x            | √     | ErgoTransaction 
 113    | Every input of the transaction should be in UTXO.                                                                          | x            | √     | ErgoTransaction 
 114    | Every data input of the transaction should be in UTXO.                                                                     | x            | √     | ErgoTransaction 
 115    | Sum of transaction inputs should not exceed 9223372036854775807.                                                           | x            | √     | ErgoTransaction 
 116    | Amount of Ergs in inputs should be equal to amount of Erg in outputs.                                                      | x            | √     | ErgoTransaction 
 117    | For every token, its amount in outputs should not exceed its amount in inputs.                                             | x            | √     | ErgoTransaction 
 119    | Scripts of all transaction inputs should pass verification.                                                                | x            | √     | ErgoTransaction 
 120    | Box size should not exceed 4096.                                                                                           | √            | √     | ErgoTransaction 
 121    | Box proposition size should not exceed 4096.                                                                               | √            | √     | ErgoTransaction 
 122    | Transaction outputs should have non-negative creationHeight.                                                               | x            | √     | ErgoTransaction 




**Header validation:**

 **Id** | **Validation rule**                                                                                                                        | **Soft-forkable** | **Active** | **Modifiers** 
--------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------|---------------
 200    | Genesis header should have genesis parent id.                                                                                              | x            | √     | Header        
 201    | Genesis header id should be equal to id from the config.                                                                                   | x            | √     | Header        
 203    | Genesis height should be 1.                                                                                                                | x            | √     | Header        
 205    | Header timestamp should be greater than the parent's.                                                                                      | x            | √     | Header        
 206    | A header height should be greater by one than the parent's.                                                                                | x            | √     | Header        
 207    | A header should contain correct PoW solution.                                                                                              | x            | √     | Header        
 208    | A header should contain correct required difficulty.                                                                                       | x            | √     | Header        
 209    | A header height should not be older than current height minus <config.keepVersions>.                                                       | x            | √     | Header        
 210    | Parent header should not be marked as invalid.                                                                                             | x            | √     | Header        
 212    | Number of non-zero votes should be <= 2.                                                                                                   | √            | √     | Header        
 213    | A header votes should contain no duplicates.                                                                                               | x            | √     | Header        
 214    | A header votes should contain no contradictory votes.                                                                                      | x            | √     | Header        
 215    | First header of an epoch should not contain a vote for unknown parameter.                                                                  | √            | √     | Header        
 216    | First v2 header on mainnet at height 417,729 should have ID =  0ba60a7db44877aade553beb05200f7d67b586945418d733e455840d283e0508. | x            | √     | Header        




**Block sections validation:**

 **Id** | **Validation rule**                                                       | **Soft-forkable** | **Active** | **Modifiers**                                  
--------|---------------------------------------------------------------------------|-------------------|------------|------------------------------------------------
 300    | Double application of a modifier is prohibited.                           | x            | √     | Header, ADProofs, Extension, BlockTransactions 
 302    | Block sections should correspond to the declared header.                  | x            | √     | ADProofs, Extension, BlockTransactions         
 303    | A header for the block section should not be marked as invalid.           | x            | √     | ADProofs, Extension, BlockTransactions         
 305    | Block section should correspond to a block header that is not pruned yet. | x            | √     | ADProofs, Extension, BlockTransactions         
 306    | Size of block transactions section should not exceed <maxBlockSize>.      | √            | √     | BlockTransactions                              
 307    | Accumulated cost of block transactions should not exceed <maxBlockCost>.  | x            | √     | ErgoTransaction, BlockTransactions             




**Extension validation:**


 **Id** | **Validation rule**                                                                               | **Soft-forkable** | **Active** | **Modifiers** 
--------|---------------------------------------------------------------------------------------------------|-------------------|------------|---------------
 400    | Size of extension section should not exceed 32768.                                                | √            | √     | Extension     
 401    | Interlinks should be packed properly.                                                             | √            | √     | Extension     
 402    | Interlinks should have the correct structure.                                                     | √            | √     | Extension     
 403    | Extension fields key length should be 2.                                                          | x            | √     | Extension     
 404    | Extension field value length should be <= 64.                                                     | √            | √     | Extension     
 405    | An extension should not contain duplicate keys.                                                   | √            | √     | Extension     
 406    | Extension of non-genesis block should not be empty.                                               | √            | √     | Extension     
 407    | Voting for fork could be started only after activation period of a previous soft-fork.            | √            | √     | Extension     
 408    | At the beginning of the epoch, the extension should contain correctly packed parameters.          | √            | √     | Extension     
 409    | At the beginning of the epoch, the extension should contain all the system parameters.            | √            | √     | Extension     
 410    | Versions in header and parameters section should be equal.                                        | √            | √     | Extension     
 411    | At the beginning of the epoch, the extension should contain correctly packed validation settings. | √            | √     | Extension     
 412    | At the beginning of the epoch, the extension should contain all the validation settings.          | √            | √     | Extension     




**Block application to state validation:**

 **Id** | **Validation rule**                                                        | **Soft-forkable** | **Active** | **Modifiers** 
--------|----------------------------------------------------------------------------|-------------------|------------|---------------
 500    | Operations against the state AVL+ tree should be successful.               | x            | √     | ErgoFullBlock 
 501    | Calculated AVL+ digest should be equal to one written in the block header. | x            | √     | ErgoFullBlock
