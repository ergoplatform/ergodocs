
### voting 
```
"rulesToDisable" = []
```

Example: storage fee factor id = 1, target value = 1000000
`1 = 1000000`


A vote for soft-fork. [protocolVersion](#protocolversion) must be one announced in a block header increased by one also. Then the node will automatically propose a soft fork (in the beginning of an epoch) or vote for it.

Put any non-zero value here to vote for soft-fork or zero to vote against.

`120 = 0`

Put an array of rules to deactivate with the soft-fork
