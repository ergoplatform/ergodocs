---
tags:
  - Forking
  - Fork
---

# Forking

Ergo's view is that disruptive hard forks should be avoided in Ergo unless absolutely critical. Ergo implements various measures to prevent hard forks, such as pushing complexity to the application layer and enabling many things to be implemented via soft-forks.

If a supermajority (90%+) of the network accepts a new feature, it is activated; however, old nodes that do not upgrade continue to operate normally and skip over this feature validation.

- [**Velvet-Fork**](velvet-fork.md): Only requires a minority of nodes to upgrade. Introduced by the NiPoPoW paper, the key idea is that you can use the scheme even if only some blocks in the chain include the interlink structure and allows for "gradual deployment" without harming the miners that haven't upgraded to the new rules. In this way, it acts similar to a soft fork in that clients that upgrade to new rules are still compatible with those that don't.
- [**Soft-fork:**](soft-fork.md) Requires some nodes to upgrade. The recent re-emission Soft-Fork EIP37 was possible as it's enforced on miner nodes only via protocol rules. These can be approved with 90% support from miners.
- **Hard-Fork:** Requires all nodes to upgrade.

For more information, refer to the [Ergo Improvement Proposals (EIPs)](https://github.com/ergoplatform/eips).
