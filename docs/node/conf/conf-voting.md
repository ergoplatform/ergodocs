---
tags:
  - Voting
---

# Voting Configuration Settings

The `voting` configuration is an important part of the system, allowing a node to propose changes to the network or vote on existing proposals. This can include soft-forks or the deactivation of specific rules.

## Rules to Disable
```bash
"rulesToDisable" = []
```
This configuration allows specifying an array of rule identifiers that you would like to propose for deactivation with a soft-fork. If you are not proposing any rules for deactivation, this can be left as an empty array.

For example, if you want to propose the deactivation of the storage fee factor, you would list its ID here.

## Voting on Soft-Fork

To propose or vote on a soft-fork, the `protocolVersion` must be increased by one in a block header. Once this is done, the node will automatically propose a soft-fork (at the beginning of an epoch) or vote for it.

As an example, suppose you want to vote on changing the target value for storage fee factor (ID: 1) to 1000000, you would use the following configuration:

```bash
1 = 1000000
```

Setting any non-zero value will vote for the soft-fork, while setting it to zero votes against it. For instance, to vote against a proposed change with ID 120, you would set:

```bash
120 = 0
```

The `voting` configurations allow for flexible network changes, promoting adaptability in the blockchain's operation as conditions or requirements change over time.
