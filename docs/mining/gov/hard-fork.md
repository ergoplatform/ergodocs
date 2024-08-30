---
tags:
  - Forking
  - Fork
---

# Hard Forks in Ergo

## Overview

In the context of the Ergo blockchain, a hard fork typically involves significant changes to the underlying consensus mechanism or core protocol rules, which require all nodes or participants in the network to upgrade to the new version of the software. If a portion of the network's participants do not upgrade, the blockchain splits into two separate chains, with the new chain following the updated protocol and the old chain following the previous one.

## Why Hard Forks Are Necessary

Hard forks are necessary for several reasons:

- **Major Upgrades:** Introducing new features or changing core mechanics of the blockchain, such as changes in the consensus algorithm, transaction validation rules, or other fundamental properties that require all nodes to operate under the new rules.
  
- **Bug Fixes:** Addressing critical vulnerabilities that cannot be patched via soft forks or minor updates. These bugs could potentially threaten the security of the entire network.

- **Governance Decisions:** Implementing decisions made by the community or core developers that require a clean break from previous rules, such as changes in monetary policy or governance structures.

## How Hard Forks Are Implemented in Ergo

The implementation of a hard fork in Ergo follows these general steps:

1. **Development and Testing:** 
    - New protocol rules are developed and rigorously tested in a controlled environment, typically a testnet or developer network. This is crucial to ensure that all changes work as intended and do not introduce new issues.
    
    - The [`ForkResolutionSpec`](https://github.com/ergoplatform/ergo/blob/master/src/it/scala/org/ergoplatform/it/ForkResolutionSpec.scala) file, found in the [Ergo GitHub repository](https://github.com/ergoplatform/ergo), is an example of how forks are tested. This file contains integration tests designed to validate the behavior of the network during and after the fork, ensuring that the nodes correctly resolve different chain forks and eventually converge on a single valid chain.

   ```scala
   it should "Fork resolution after isolated mining" in {
       // Test scenario ensuring that nodes resolve forks correctly after isolated mining periods
   }
   ```

2. **Coordination with the Network:**
   - Developers coordinate with miners, node operators, and the broader community to schedule the fork. Communication is crucial, as all participants need to update their software to the new version by a certain block height or date.

   - The node configuration files, such as `nodes.conf`, play a significant role in setting up the environment for the fork. This file specifies the settings for different nodes in the network and ensures that they are all synchronized and ready for the protocol change.

   ```hocon
   nodes = [
       { scorex { network.nodeName = node01 } },
       { scorex { network.nodeName = node02 } },
       ...
   ]
   ```

3. **Activation and Monitoring:**
    - At the predetermined block height or time, the new protocol rules are activated. The network continues to operate, but now all participants are following the new set of rules.

    - Post-fork, developers and node operators monitor the network for any anomalies or issues that may arise as a result of the fork.

4. **Handling Divergence:**
   - In the event that some nodes do not upgrade, the blockchain may split into two, creating a new chain (following the new rules) and a legacy chain (following the old rules). The `ErgoValidationSettings` class in the Ergo core provides mechanisms to enforce these new rules, ensuring that nodes adhering to the new rules can correctly validate blocks and transactions.

   ```scala
   case class ErgoValidationSettings(
       rules: Map[Short, RuleStatus],
       sigmaSettings: SigmaValidationSettings,
       updateFromInitial: ErgoValidationSettingsUpdate
   ) extends ValidationSettings with BytesSerializable {
       // Validation logic for new rules
   }
   ```

### When to Use Hard Forks

- **Protocol Upgrades:** When a major new feature or change needs to be implemented that is not backward-compatible.
  
- **Security Fixes:** When critical vulnerabilities are discovered that cannot be addressed through a soft fork.

- **Consensus Changes:** When the community decides to make fundamental changes to the consensus algorithm or governance model.

## Conclusion

Hard forks are a powerful tool in the evolution of the Ergo blockchain, allowing for significant changes and improvements. However, they require careful planning, coordination, and communication to ensure the network remains secure and functional during and after the transition. As with any major change, thorough testing and validation are essential to avoid disruptions.

For further details on how these processes are implemented and tested within the Ergo blockchain, you can explore the relevant code and configuration files available in the [Ergo GitHub repository](https://github.com/ergoplatform/ergo). 
