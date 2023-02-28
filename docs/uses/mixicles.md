# Mixicles

[Mixicles](https://research.chain.link/mixicles.pdf) (short for "*mixing oracles and smart contracts*") are a type of smart contract that uses data from an oracle to create a private contract between two or more parties. These contracts are designed to be used in situations where privacy is important, and where the terms of the contract are based on data that is provided by an external source.

Mixicles work by using the data provided by an oracle to trigger the execution of a smart contract. The terms of the contract are then automatically enforced based on the data that is received from the oracle. Because the contract is executed automatically, there is no need for intermediaries or third parties to oversee the transaction.

One use case for mixicles is in the area of supply chain management. For example, a company might use a mixicle to create a private contract with a supplier based on data provided by an oracle about the quality and delivery of raw materials. The terms of the contract could be automatically enforced based on the data received from the oracle, ensuring that both parties are held accountable for their respective obligations.

Overall, mixicles offer a way to create private contracts that are based on trusted external data sources, without the need for intermediaries or third parties to oversee the transaction.

Implementation-wise on Ergo, the onchain part would simple. The P2P off-chain interaction is needed (and would be the most labour-intensive part)