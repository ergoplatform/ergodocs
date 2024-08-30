---
tags:
  - Forking
  - Fork
---

# Forking

## Overview

Ergo's view is that disruptive hard forks should be avoided unless absolutely critical. Ergo implements various measures to prevent hard forks, such as pushing complexity to the application layer and enabling many things to be implemented via soft-forks.

If a supermajority (90%+) of the network accepts a new feature, it is activated; however, old nodes that do not upgrade continue to operate normally and skip over this feature validation.

## Fork Types

- [**Velvet-Fork**](velvet-fork.md): Only requires a minority of nodes to upgrade. Introduced by the NiPoPoW paper, the key idea is that you can use the scheme even if only some blocks in the chain include the interlink structure and allows for "gradual deployment" without harming the miners that haven't upgraded to the new rules. In this way, it acts similar to a soft fork in that clients that upgrade to new rules are still compatible with those that don't.
- [**Soft-fork:**](soft-fork.md) Requires some nodes to upgrade. The recent re-emission Soft-Fork EIP37 was possible as it's enforced on miner nodes only via protocol rules. These can be approved with 90% support from miners.
- [**Hard-Fork:**](hard-fork.md) Requires all nodes to upgrade.

## Additional Information

For more information, refer to the [Ergo Improvement Proposals (EIPs)](https://github.com/ergoplatform/eips).

## Fork Prevention Measures

Ergo employs various measures to prevent disruptive hard forks:

- **Pushing complexity to the application layer**: By keeping the core protocol simple and pushing complexity to the application layer, Ergo reduces the need for frequent protocol-level changes that could lead to hard forks.
- **Enabling soft-forks**: Many features and improvements can be implemented through soft-forks, which allow for backward compatibility and gradual adoption without disrupting the network.

## Fork Activation Process

When a new feature or change is proposed, it goes through the following process:

1. **Proposal and Discussion**: The proposed change is discussed and evaluated by the Ergo community and developers.
2. **Consensus and Approval**: If the proposal gains consensus and is approved, it is scheduled for implementation.
3. **Fork Type Determination**: Based on the nature of the change, it is determined whether a velvet-fork, soft-fork, or hard-fork is required.
4. **Activation**: If a supermajority (90%+) of the network accepts the new feature, it is activated. Old nodes that do not upgrade continue to operate normally and skip over the new feature validation.

By following this process and leveraging the various fork types, Ergo aims to maintain a stable and secure network while enabling continuous improvement and innovation.
