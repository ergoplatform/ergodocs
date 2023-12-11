
# FAQs: Rosen Bridge Operations and Features

### What is the bridge fee structure?

Initially, it's the greater of $10 or 0.5% of the transaction value, plus network fees, adjustable by the guard set. The fee is collected in the transferred token on Ergo. Network fees vary: static for Ergo and Cardano, dynamic for EVM-based networks.

### Is there a maximum amount for a single transaction on Rosen Bridge?

No fixed maximum, but large transfers may take longer, from hours to 1-2 days, due to manual guard intervention for fund transfers from cold to hot wallets.

### How is ADA managed within the system for transactions to Cardano?

Network fees in the transaction token on Ergo are sent to a dedicated address for covering network fees on different chains. Currently, the Rosen team manually manages this, with plans for future automation.

### How can a project add new token options to the bridge?

Projects pay a listing fee to the Rosen Fund, with potential discounts for open-source projects. This involves minting wrapped tokens and updating the token map. Fees are distributed to watchers and guards.

### What are the next chains to be added following ADA?

The roadmap includes BTC, BSC (EVM-chains), and Dogecoin in the midterm. Code refactoring aims to facilitate adding new chains, with initial chains being the most challenging.

### What is the size and composition of your team?

The team includes 8 developers, with some frontend and UI tasks outsourced. Additionally, 2-3 developers have worked part-time over the past year, supported by several advisors.

## Watcher FAQs

### Role and Rewards
Watchers are essential for accurate reporting and receive 70% of transaction fees as rewards for successful and accurate reporting. (while 30% goes to the guard set).

### Collateral Requirements: 
Each instance requires 800 ERG and 30,000 RSN as collateral. This collateral is fully redeemable and the amount is adjustable.

### Permit Acquisition: 
To report, watchers must acquire permits, costing an additional 3,000 RSN. Multiple permits are necessary for reporting concurrent events, and permits can be seized if reports are found fraudulent.

### Reporting Process:
- Watchers report deposit events as part of a collective effort.
- A consensus among watchers on an event triggers a final report and guard intervention.
- Guards take necessary actions based on these reports.
- Watchers involved in successful cross-chain settlements are rewarded.

### Is there a limit on the number of watchers?
Effectively, yes. A a minimum of 70%+1 of watchers required to trigger an event, and a maximum of 20 commitments, adjustable by the guard set.

### Can I run multiple watchers?
Yes, but it incurs financial considerations to prevent abuse. Each instance needs a unique folder and WATCHER_PORT.

### What if my report is successful?
You'll receive rewards and your staked amount will be returned.

### What if my report is incorrect and uncorroborated?
You'll get a refund of your stake without any additional penalties.

### What are the consequences of collusion and fraud in reporting?
Colluding watchers will lose the amount they staked.

### Are permits spent or staked for reporting?
Permits are staked, not spent, and can be managed through your dashboard.

### Can I adjust my permits?
Yes, you can increase or decrease your permits at any time and redeem them when leaving.

### How many permits are needed for concurrent reporting?
The number depends on bridge activity, with about 160 needed to report one transaction per minute. 

### How do I redeem my collateral?
You can redeem it after redeeming your last permit token, but if you have unsettled reports, you must wait until those permits are returned.

### Do I still need RSN on Ergo to be a watcher on another chain?
Yes, all permit operations are conducted on the Ergo platform, and Rosen's logic is Ergo-based.

### Common Issues

#### Permit Health Broken

By default, the permit health warning parameter is set quite high. This is adjustable locally by adding the following into local.yaml


```yaml
healthCheck:
  permit:
     warnCommitmentCount: 1
     criticalCommitmentCount: 0
```

Adjust the numbers as you wish.

`warnCommitmentCount`` will change the warning to yellow when the available Permits reduce to the number.

`criticalCommitmentCount`` will change to red when the available Permits reduce to this number. 