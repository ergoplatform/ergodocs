# Governance

Many parameters in Ergo can be changed on-the-fly via miners voting. Things like instructions costs, computational cost limit per block, block size limit, storage fee factor, and block version. Meaning the long-term economic security of the protocol is up to miners to decide. 

In addition to the protocol parameters [listed below](#parameters-table) that can be changed via on-chain miner voting, most things on Ergo can be changed via a soft-forking protocol (90% support required). This excludes critical changes such as changing the max supply. 

Voting for the block version lasts **32 epochs** and requires more than **90 percent** of the miners to vote for the change. A simple majority is enough for less critical changes such as block size limit. We will further refer to the changes of the first kind as 'foundational changes', and we refer to the changes of the second kind as 'everyday changes'. 

> Per block, a miner can vote for two everyday changes and one foundational change, with the votes to be included in the block's header.

- To vote **Yes** and propose a change in the first block of an epoch, a miner publishes the identifier of the change directly in the block header. 
- To vote **No** (or avoid voting at all, which is the same), a miner writes zero value instead of a corresponding byte (another option is to provide a vote identifier not considered within the epoch).

## System constants:

- Voting epoch length = `1024` blocks.
- Voting epochs per foundational change = `32`
- Voting epochs before approved foundational change activation = `128`


## Current settings

- `maxBlockSize` : 1271009 bytes
- Max box size: 4096 bytes
- Max transaction size: 96kb

## Parameters table

The following table describes vote identifiers, default values (during launch), possible steps, and minimum and maximum values. 

- If the step is not defined in the table, its value is defined as $\max(\lfloor current\_value / 100 \rfloor, 1)$. 
- If the minimum value for a parameter is not defined, it equals zero. 
- If the maximum value is not defined, it equals `1,073,741,823`.

A miner includes a parameter identifier ($id$) into the block header to propose or vote for increasing a parameter. If the miner supports decreasing the parameter, they would include ($-id$) into the block header.

> Try out these parameters on [deadit.github.io/paizo/](https://deadit.github.io/paizo/)

| ID | Description | Default | Step | Min | Max |
|---|---|---|---|---|---|
| 1 | Storage fee factor (per byte storage period) | 1250000 | 25000 | 0 | 2500000 |
| 2 | Minimum monetary value of a box | 360 | 10 | 0 | 10000 |
| 3 | Maximum block size | 524288 |  | 16384 |  |
| 4 | Maximum cummulative computational cost of a block | 1000000 |  | 16384 |  |
| 5 | Token access cost | 100 |  |  |  |
| 6 | Cost per one transaction input | 2000 |  |  |  |
| 7 | Cost per one data input | 100 |  |  |  |
| 8 | Cost per one transaction output | 100 |  |  |  |
| 120 | Soft-fork (increasing version of a block) |  |  |  |  |

Parameter values are to be written into the extension section on the first block of a voting epoch,
that is, in the extension of a block when its $height\,mod\,1024 = 0$.

Parameters for the initial moment of time~$(height = 1)$ are hardcoded.

## Proposing a change and voting for it

To propose a change, in the first block of a voting epoch (of $1,024$ blocks, so in a block of
$height\,mod\,1024 = 0$), a miner is posting an identifier of a vote for a change. There are three slots (three bytes)
in a block header for proposed changes, with two slots reserved for everyday changes and the third one for
proposing a soft fork. A slot not occupied by a proposal is to be set to zero. Votes could come in any order.
Examples of the bytes: $(0, 1, 120)$, $(120, -3, 0)$. In the first case, a miner is proposing to increase the storage fee factor ($id:1$), and
also proposes a soft-fork ($id:120$); in the second case, a miner is proposing to decrease block size ($id:-3$), and also
 is proposing a soft-fork ($id:120$).

To vote for a proposal~(which is proposed in the first block of an epoch) within the epoch, a miner includes the vote identifier into the block header. Identifiers not proposed in the first block of the epoch are ignored.

If a majority of votes within an epoch support an everyday change (so at least 513 blocks contain an identifier), a new value of the parameter should be written into the extension section of the first block of the next epoch.

## Voting for a soft-fork

A soft-fork happens when a protocol version supported by the network is being increased.
The protocol version is being written into every block header, with the initial value during launch to be set to 1.

The semantics behind versioning is not defined ahead of time by the protocol and so up to clients and their developers.
Protocol developers can disable some existing validation rules from the [Validation](#validation) section during a soft-fork while introducing new ones.

The protocol version upgrade is to be done in the following steps:

- A protocol developer implements and releases software with changed rules and this software may deactivate some existing rules while also introducing new logic.
- A miner proposes increasing the protocol version and putting deactivated rules into extension.
- Other miners are voting within 32 epochs for the proposal
- If the soft-fork proposal is being rejected~(so if it gathers no more than $90\%$ of votes during the voting period, i.e. no more than $\lfloor 32 * 1024 * 90 / 100 \rfloor = 29491$ votes), new voting may be proposed next epoch after the voting is done.
- If the soft-fork proposal is approved, an activation period of 32 epochs is starting. The first block
after the activation period is called activation height. It is prohibited to vote for a new soft fork during the activation and the activation height. Soft-fork data is still to be written to corresponding extension sections~(see below) during the activation period and on activation height.
Block version written into extensions is to be increased from the first block of the activation period, while the protocol version in headers is still the same. The protocol version in headers is increased from the activation height.

To start voting for a soft fork, a miner needs to publish the identifier $120$ in the first block of the epoch; consider, for example, that its height is $h_s$. Next epoch, a miner should post height when the start fork was proposed ($122: h_s$) in the extension section of the block, and the number of votes collected in the previous epochs $v_s$ should be written there as well as ($121: v_s$).

See this [ergoforum post](https://www.ergoforum.org/t/voting-for-a-soft-fork-in-ergo/2958) for an example. 

### Examples:

- Assume that a vote for soft-fork is proposed in block number $1024$ (by writing a record into the extension with a key equal to $120$ and any value). Assume that within this epoch, before block number $2048$, $500$ votes were collected. A miner who generates block $\#2048$ must write the height when the soft-fork voting has been started in the extension section of the block as ($122: 1024$ key-value pair), as well as the number of votes supporting the fork gathered within the epoch done (in the form of $121: 500$). Assume that the new epoch started with the block $\#2048$ brings 600 votes for the fork. Then a miner generating the block $\#3072$ must write down the following pairs: $(121, 1100)$ and $(122, 1024)$.
- The voting is to be done on height $1024 + 1024*32 = 33792$, with the last vote written into block $\#33791$. Block $\#33792$ still should contain correct values for votes collected and voting starting height.
- let us assume that voting for the soft-fork was not successful, i.e. no more than $29491$ votes for soft-fork have been gathered between blocks $\#1024$~(inclusive) and $\#33792$~(exclusive). Then the next epoch block, the block $\#34816$ should clear the old voting parameter values. New voting for soft-fork may be started in this new epoch, so in the block $\#34816$, if the block contains a vote for the soft-fork (i.e. a record with key = 120 in the extension section), then the block must contain new starting height and votes collected values (i.e. following pairs: $(121: 0)$ and $(122: 34816)$). If there is no new voting started, all the parameters regarding soft-fork voting must be cleared off of the block $\#34816$.
- Now, assume that the voting for the soft-fork was successful, i.e. more than $29491$ votes for soft-fork have been gathered between blocks $\#1024$~(inclusive) and $\#33792$~(exclusive). In this case, the activation epoch is starting immediately after the voting has been done, so on height $33792$. The activation epoch lasts for 32 epochs, so the first block after the activation period has a height of $33792$. Please note that any vote for a soft-fork during the activation period is prohibited. Also, on the first block of a voting epoch, soft-fork voting parameters should be written~(height when voting had been started and also the number of votes collected). On the first block after activation, the protocol version written into a block must be increased. The first block after activation should carry soft-fork voting parameters. The parameters must be cleared next epoch so in a block $\#33792$. New voting may be started in the block $\#33792$, similarly to the case of a non-successful vote.
