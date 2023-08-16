
# Efficient Global Context Claims on Ergo Platform Blockchain


Ergo offers a unique approach to smart contract-enabled blockchains, providing efficient global context claims through the concept of data inputs. This documentation aims to explain the benefits and implications of global context claims and how they contribute to the trustless and decentralized nature of the Ergo blockchain.

## Understanding Global Context Claims

Smart contract-enabled blockchains typically have limited access to context data from other accounts, UTXOs (Unspent Transaction Outputs), or contracts. However, Ergo introduces a groundbreaking feature called data inputs, which allow referencing UTXOs in transactions without spending them. This means that any dApp or contract on the Ergo blockchain can access the data and value stored within any UTXO without requiring explicit permission or additional contract modifications.

Global context claims leverage data inputs to enable anyone to make generic claims about the entire Ergo system. For example, a smart contract can specify that a particular UTXO can only be spent if another UTXO exists with specific data in its registers. By creating a transaction that references the required UTXO as a data input, the claim can be proven, granting the right to spend the UTXO.

## Monetary Incentives and Verification

To incentivize users to validate and prove global context claims, Ergo allows the inclusion of a reward in the form of Ergs within smart contracts. Users, who are not validators, can scan the UTXO set to find a UTXO that satisfies the claim's conditions and earn the specified reward. This approach outsources the scanning and verification of the blockchain's global state to users, ensuring trustlessness and efficiency through data inputs.

By streamlining this process with automated software, Ergo users can easily participate in the validation task and earn Erg as a reward. The greater the reward, the stronger the incentive for verifiers to ensure the claim's validity, increasing the overall assurance of the system. This decentralized network of verifiers forms a crucial component of Ergo's efficient global context claims, providing a low barrier of entry for users to contribute to the blockchain ecosystem.

## Global Context Data Accumulators

The Ergo blockchain goes beyond simple boolean checks by introducing the concept of context data accumulators. With data inputs providing full context information, these accumulators can apply arbitrary functions to the accumulated data rather than performing only boolean checks. Accumulators scan the entire blockchain to collect relevant boxes' data and consolidate it into a single or set of values, which are then stored in a new box.

For example, a context data accumulator could calculate the total number of Ergs held in a specific smart contract address. By posting a reward-bearing box with a contract specifying the accumulation conditions, participants can contribute data inputs and create new boxes with relevant data. Once the accumulation is finalized after a predetermined number of blocks, the user who contributed the most data inputs can claim the reward and move the accumulated value into a new box accessible to the entire network.

Context data accumulators offer practical use cases in various domains, such as DeFi, where accurate calculation of funds in a liquidity pool is essential for determining interest rates. By checkpointing the state of the blockchain with accumulators, users can parallelize actions within dApps while contributing to a global shared core state. Future possibilities include integrating these accumulation schemes with sharding or side-chains to scale smart contracts efficiently, leveraging Ergo's UTXO model.

## Security and Improvement of Global Context Claims with Pools

To enhance the security of claims and accumulations, Ergo introduces the concept of pools. In the case of claims, participants join a "Claim Pool" by staking collateral, indicating their active involvement in checking the claim's validity. The first participant to provide a counter-proof to

 the claim receives the reward. All other participants must also present counterclaims within a specified time duration to prove their active participation. Failure to do so results in the distribution of their collateral among all active participants.

Furthermore, residual payout schemes can be incorporated into Claim Pools. Participants receive ongoing rewards for actively checking the claim, even if no counter-proof is produced in a given epoch. This incentivizes continued active participation while ensuring sufficient funds for verifiers. Outsiders can also provide counter-proofs after an epoch ends, allowing them to claim the reward and the collateral of all pool participants if they can prove the claim's invalidity.

These pool-based mechanisms foster a more robust and secure environment, providing active checking incentives, preventing collusion, and allowing external verification to maintain integrity.

## Trustless Prediction Markets and Beyond

Global context claims also enable the creation of trustless prediction markets on the Ergo blockchain. By minting two different tokens representing "True" and "False" outcomes, users can participate in prediction markets to speculate on the state of dApps, contracts, or data on the blockchain. These tokens are locked in a contract that includes a claim, and the outcome is determined by the proof or counter-proof provided through data inputs.

The flexibility and versatility of Ergo's global context claims and data accumulators offer a wide range of applications and possibilities. As Ergo continues to evolve, users can explore further improvements and security measures, leveraging pools, encoding entry conditions, and integrating with other technologies like NFTs, sharding, or side chains.

## Conclusion

Ergo revolutionizes smart contract-enabled blockchains with its efficient global context claims and data accumulators. By leveraging data inputs, users can make claims about the entire system, verify them with monetary incentives, and accumulate data into a single box accessible to all. The trustless and decentralized nature of Ergo, combined with the ability to parallelize actions and accumulate data, opens up new possibilities for decentralized finance, prediction markets, and more.

The concepts presented here provide a solid foundation to understand the power and potential of global context claims and data accumulation on Ergo. As the ecosystem evolves, the community can further explore and develop these concepts, building a robust and efficient blockchain platform.