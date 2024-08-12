# Reputation System

## Introduction

Our purpose to the Ergohack-VII is reputation system. A reputation system addresses a fundamental need in the blockchain ecosystem - trust. Trust is essential in any ecosystem, and our system aims to bridge the trust gap by providing a decentralized, user-driven mechanism for assigning and transferring reputation.

**Trust and Reputation:**

Trust is the foundation of any functional ecosystem, including the digital world of blockchain.
In this space, trust is equally vital.
Users must have confidence in the entities they interact with,
whether it's smart contracts, addresses, URLs, or other off-chain entities.
This reputation system aims to establish and maintain this trust.

**Why is it necessary?** 

A reputation system can provide interesting approaches in a blockchain ecosystem. 

On one hand, certain applications require it: 
peer-to-peer versions of Airbnb, Uber, or similar platforms, as the central function of the company 
(in the current versions) is to provide that 
reputation network among interacting agents (hosts or tenants, drivers and passengers, etc.)

On the other hand, current applications (DeFi protocols, bridges, etc.) may not directly require a reputation system, but nonetheless, it is highly necessary.
It is necessary because blockchain is based on trustlessness. 
If we consider that an ecosystem (of a peer-to-peer network like Ergo) is enriched by the number of tools it possesses 
(among other variables), what value do these tools have if users cannot trust them? 
How does a user know which ones are reliable and which are not? 
How does a user know which contracts, URLs, or whatever else they can use without taking too much risk? 

The answer is: based on what others say, meaning the community plays a crucial role. 
For this, two important parts are needed:
1. The tools should be open and auditable. 
2. A platform for sharing reviews, feedback, or opinions about these tools. 
This is where this project aims to help. 
Because currently, a user decides whether to trust a web3 page based on what its users say on Twitter (now X) 
or how they discuss it on YouTube. We believe that this is a problem that no part of the entire ecosystem is currently addressing.

**Basic explanation**

The main characteristic of this system is that it doesn’t require consensus.
That is: *Alice can trust Bob more than Criss.
But Dave can trust Criss more than Bob.*

For that, we suggest a system where Alice, Bob, Criss and Dave submit on who trust. 

Each of them can submit a record in a distributed and trustworthy database
(Ergo) so that the others can see in whom they invest their own reputation.
Each one has an incentive to maintain a good reputation,
and to do so, they should assign a good reputation only to those they consider better.

**Basic initial real-world economy example:**

This way, in, for example, an application like Airbnb, the cost of accommodation for a user will be inversely proportional to the reputation assigned to them by the tenant, which may be different from what other tenants assign (they don't have to reach a consensus, so they can rely on different ways to evaluate each other - giving more importance to punctuality than cleanliness, for example).

## **Aligment with the [Ergo Manifiesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/):**

Why is this an *ergonomic system*?

Well, in accordance with Ergo's principles, the system:

- It’s completely decentralized (****Decentralization First****), there's virtually no consensus among parties, as there isn't even a common token to represent reputation across all parties.

- It’s open and auditable (****Open Permissionless and Secure****), as a user can upload a different reputation contract (different from the one presented in this project), and it wouldn't fragment the system. The reputation proofs defined here could point to this new test with a different design as well.

- It’s ****Created for Regular People****, as there are no major entry barriers other than those inherent to the Ergo network.

- It’s focused on remaining cost-competitive ****(Platform for Contractual Money),**** as it allows providing economic agents with evidence of their past good behavior, preserving privacy.
    - This remains cost-competitive because it allows agents to consider a wider range of options. The lower the quality of reputation systems, the higher the cost of switching between services (e.g., switching from one dentist to another is more expensive if I have no reviews for either; if people share their experiences, there will be more competition).
    
- It Has a ****Long-term Focus****, as the development team has not based its approach on short-term vision.


## System design

Each reputation proof has a token used to reflect the amount of reputation that can be assigned. 
When creating a reputation proof, you can either: 
- Generate it from scratch with a new token. 
- Extract it from another reputation proof, so the amount of reputation will be extracted from the previous proof. 

Each reputation proof is a Box. 
Only the users themselves can delegate reputation from their proofs to new proofs they generate. 
However, any user can assign reputation to any reputation proof: without transferring the token, 
simply by locking the value of their proof and entering the proof to which reputation is being assigned as metadata. 
This way, reputation graphs are created.

The value of each reputation token is subjective for each user, so everyone must calculate the reputation that their 
reputation proof graph assigns to each object.

**ErgoScript Contract:**

All reputation proofs have the same script. 
<br>The first two conditions check if the reputation proof assigns reputation 
to an object; if it does, it cannot be spent. 
<br>The second one ensures that the one spending the test is only the wallet with permissions to do so.
<br>The third one ensures that reputation is delegated only to reputation proofs.

```javascript
/*
Reputation Proof  -   2Ud2Ryh6MkC8Lstg1BiSE86Vbs7FTBdChEMo2c3ZK3pyGaQoY2Ck9QQiz2n4vWP6


    R4 -> owner public key
    R5 -> Reputation on-chain object
    R6 -> Reputation off-chain object
    
*/
    // An optional object where the proof assign it's reputation 
    // (it could be different types of data, like other Reputation systems, urls, git repositories, etc).
SELF.R5[Box].isDefined != true &&
SELF.R6[(Coll[Byte], Coll[Byte])].isDefined != true &&
    // 
    // The proof's creator (or, at least, the one chosen by the box's creator) can spend the tokens
    // Owner's public key.  Without it, the box can't be expended. 
proveDlog(decodePoint(SELF.R4[Coll[Byte]].get)) &&
    //
    // Assign them ONLY to other reputation proofs.
OUTPUTS.forall({(x: Box) => x.propositionBytes == SELF.propositionBytes})
```


**Reputation Trees:**
At the core of our system are Reputation Trees. These trees serve as hierarchical repositories of trust, with each tree containing a root Box representing 100% reputation. Within these trees, there are branches and leaves. 
Branches point to other reputation proofs, creating a hierarchy of trust, while leaves represent reputation proofs assigned to external objects in the form of metadata. 
This structure provides a systematic and scalable approach to reputation management.

<!--
![reputation_system-example.svg](resources/reputation_system-example.svg)
-->
**User-Generated Reputation:**
A feature of this system is the ability for any user to submit reputation proofs.
It's a truly democratic approach to trust, empowering users to assign and transfer reputation.
Moreover, the system **does not require consensus** for reputation assignments,
allowing individual users to express their trust independently.

**User Interface:**
We've designed an intuitive user interface that simplifies the process of submitting reputation proofs. 
The "Generate Reputation Proof" button allows users to specify the reputation amount from a new token or from another 
reputation proof (if they can spend it). 

- If the new Reputation Proof box has reputation object (could be called a pointer to an object too), it will be a leaf 
of the tree. That means that it will be unspendable.
- If not, the Reputation Proof is only a branch to assign reputation in the future.

**Versatile Use Cases:**
Reputation proofs can be assigned to 
various entities, including software, URLs, Git repositories, and more.

- The R5 registry allows assigning to other Ergo’s boxes (probably to other reputation systems).
  Due to that, it's a Box field.
- The R6 registry allows assigning to any external object (URLs, Git repositories, etc.).
   To do this, we consider that the best option is a scheme of (Coll[Byte], Coll[Byte]), 
    where the first part allows specifying the value type, and the second part the value to assign reputation to.

**Scalability and Interoperability:**
As the blockchain ecosystem grows, scalability is paramount. Our system is designed to handle an increasing number 
of users and reputation assignments efficiently thanks to the eUTXO paradigm. We also consider interoperability with 
other blockchains and external services to create a seamless user experience.

**Accountability and Determinism:**
If the reputation proof is assigning reputation to an object (it has the R5 or R6 registers), the token cannot be spent,
ensuring a direct link between reputation and the object.
This restriction enhances accountability and trust in the system.

## **Problems not resolved**

Unfortunately, these past three days, we haven't been able to have a working version,
so we've had to settle for a version with demo data.
Nevertheless,
we will continue with the development and keep engaging with the community to receive feedback or any assistance.

There are certain things that we are not able to solve these two days, they are:

- The transaction builder with Fleet SDK:
    - Actually, we are taking the inputs from all the user’s unspended boxes but, on the UI, he selects a specific 
      reputation proof (a specific box). So, we need to do that:
        - Solving the usage of the explorer api from off-chain code.
        - Doing that with Fleet from the browser.
- On the on-chain side:
    - The reputation object (or pointer to an object) uses to registers (R5 and R6) because it can have to type: a 
       Box or a Tuple of bytes. That’s because ErgoScript don’t allow to use something like 
       `type AssignedReputation = Box || (Cell[Byte], Cell[Byte])` types. We don’t know if there is a better way to do it.
    - We would want to limit the number of possible tokens to one, for a more specific contract.
- On the off-chain side:
    - We need to develop the `compute_reputation.py` script. It will allow computing the reputation of an object based 
      on the user’s reputation proofs (and from those external proofs to which the user has assigned reputation).
    - The `extract_unexpended_reputation_proofs.py` script it’s only using random demo data for the user’s unexpended 
      reputation proofs. It has the code to use the api explorer, but it didn't work.

## **Future aproaches**

This is a long-term project. Due to that, we recognize that reputation management needs to be adaptable.

Some possible branches to expand are:

- The UI allows seeing graphic reputation trees (owned to manage and external to be judged.)
- Allow to a more complex token/monetary policies on the on-chain side.
- Each branch of the reputation tree could have its own rules and policies, allowing for customization to meet the 
  unique needs of different communities and contexts. Events within the system can also trigger reputation transfers, 
  creating a dynamic ecosystem. <br>For example:<br>
        *A reputation proof is directed towards a smart contract. Another reputation proof is directed towards a Git repository (or a specific commit) that serves as an interface to the contract. The second test is dependent on the first one, so if the contract's reputation drops, the interface's reputation will automatically decrease as well. (This could be achieved with a certain structure and monetary policies of the tree).*


*Thanks for reading.*

[GitHub repository](https://github.com/jossemii/ergohack-vii)