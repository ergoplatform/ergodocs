# Rosen Guards

Rosen is an Ergo-centric bridge fortified with multi-layered security protection. In the initial layer, [Watchers](rosen-watcher.md) monitor network activities and report valid bridge-related events to the subsequent layer, Guards. These Guards then carefully process the reported events and execute required actions. In brief, Guards are dedicated to security maintenance and executing responses, while Watchers are focused on the ongoing monitoring of activities and transparent reporting.

Guards are a federated group of entities managing the Rosen core. Their authority over Rosen is restricted through multisignature contracts and wallets. Failure or collusion of Guards will be tolerated while the majority of Guards are healthy. Each Guard has a reasonable amount of funds locked as collateral and will lose all their funds at once in case of malicious behaviour.

Guards need to lock RSN as collateral. Funds will be emitted to the Guard Set and involved Watchers in case of any successful bridge transfers. However, funds will be slashed/collected in case of malicious behavior. When RSN emission has ended, all bridge fees will be collected in the RSN token. Holding RSN will have special fee benefits for projects.

/// details | Who can become a Guard?
     {type: info, open: false}
Becoming a guard is effort-intensive and permission-based, starting with selected known entities and later admissions by the guard set. Guards buy and lock RSN tokens in a multisig wallet, with stakes lost for misconduct or inactivity.
///

/// details | Who are the current Guards?
     {type: info, open: false}
The Guard Set can be seen on [rosen.tech](https://rosen.tech/)
///