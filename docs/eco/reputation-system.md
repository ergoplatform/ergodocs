---
tags:
  - Reputation System
  - Trust
  - Decentralized
  - dApp
---

# Reputation System

## Introduction

A reputation system addresses a fundamental need in the blockchain ecosystem - trust. Trust is essential in any ecosystem, and this system aims to bridge the trust gap by providing a decentralized, user-driven mechanism for assigning and transferring reputation.

View the [Sigma Reputation System](https://github.com/sigma-rps) repository on GitHub and this [explainer post](https://www.ergoforum.org/t/reputation-system/4782)

**Trust and Reputation:**

Trust is the foundation of any functional ecosystem, including the digital world of blockchain. In this space, trust is equally vital. Users must have confidence in the entities they interact with, whether it's smart contracts, addresses, URLs, or other off-chain entities. This reputation system aims to establish and maintain this trust.

**Why is it necessary?**

A reputation system can provide interesting approaches in a blockchain ecosystem.

On one hand, certain applications require it: peer-to-peer versions of Airbnb, Uber, or similar platforms, as the central function of the company (in the current versions) is to provide that reputation network among interacting agents (hosts or tenants, drivers and passengers, etc.)

On the other hand, current applications (DeFi protocols, bridges, etc.) may not directly require a reputation system, but nonetheless, it is highly necessary. It is necessary because blockchain is based on trustlessness. If we consider that an ecosystem (of a peer-to-peer network like Ergo) is enriched by the number of tools it possesses (among other variables), what value do these tools have if users cannot trust them? How does a user know which ones are reliable and which are not? How does a user know which contracts, URLs, or whatever else they can use without taking too much risk?

The answer is: based on what others say, meaning the community plays a crucial role. For this, two important parts are needed:
1. The tools should be open and auditable.
2. A platform for sharing reviews, feedback, or opinions about these tools.
This is where this project aims to help. Because currently, a user decides whether to trust a web3 page based on what its users say on Twitter (now X) or how they discuss it on YouTube. The project believes that this is a problem that no part of the entire ecosystem is currently addressing.

**Basic explanation**

The main characteristic of this system is that it doesn't require consensus. That is: *Alice can trust Bob more than Criss. But Dave can trust Criss more than Bob.*

For that, the system suggests a system where Alice, Bob, Criss and Dave submit on who they trust.

Each of them can submit a record in a distributed and trustworthy database (Ergo) so that the others can see in whom they invest their own reputation. Each one has an incentive to maintain a good reputation, and to do so, they should assign a good reputation only to those they consider better.

**Basic initial real-world economy example:**

This way, in, for example, an application like Airbnb, the cost of accommodation for a user will be inversely proportional to the reputation assigned to them by the tenant, which may be different from what other tenants assign (they don't have to reach a consensus, so they can rely on different ways to evaluate each other - giving more importance to punctuality than cleanliness, for example).

## **Alignment with the [Ergo Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/):**

Why is this an *ergonomic system*?

Well, in accordance with Ergo's principles, the system:

- It's completely decentralized (****Decentralization First****), there's virtually no consensus among parties, as there isn't even a common token to represent reputation across all parties.

- It's open and auditable (****Open Permissionless and Secure****), as a user can upload a different reputation contract (different from the one presented in this project), and it wouldn't fragment the system. The reputation proofs defined here could point to this new test with a different design as well.

- It's ****Created for Regular People****, as there are no major entry barriers other than those inherent to the Ergo network.

- It's focused on remaining cost-competitive ****(Platform for Contractual Money),**** as it allows providing economic agents with evidence of their past good behavior, preserving privacy.
    - This remains cost-competitive because it allows agents to consider a wider range of options. The lower the quality of reputation systems, the higher the cost of switching between services (e.g., switching from one dentist to another is more expensive if I have no reviews for either; if people share their experiences, there will be more competition).
    
- It Has a ****Long-term Focus****, as the development team has not based its approach on short-term vision.

## System Design

Each reputation proof has a token used to reflect the amount of reputation that can be assigned. When creating a reputation proof, you can either:  

- Generate it from scratch with a new token.
- Extract it from another reputation proof, so the amount of reputation will be extracted from the previous proof.

Each reputation proof is a Box. Only the users themselves can delegate reputation from their proofs to new proofs they generate. However, any user can assign reputation to any reputation proof: without transferring the token, simply by locking the value of their proof and entering the proof to which reputation is being assigned as metadata. This way, reputation graphs are created.

The value of each reputation token is subjective for each user, so everyone must calculate the reputation that their reputation proof graph assigns to each object.

**ErgoScript Contract:**

All reputation proofs have the same script. The first two conditions check if the reputation proof assigns reputation to an object; if it does, it cannot be spent. The second one ensures that the one spending the test is only the wallet with permissions to do so. The third one ensures that reputation is delegated only to reputation proofs.

## Project Context: CELAUT

CELAUT is a network paradigm similar to Kubernetes but operates in a peer-to-peer manner. It enables services to deploy other services dynamically. Although CELAUT is not necessarily tied to Ergo or blockchain technology, it requires a robust reputation system and payment mechanism. The reputation system is being integrated into CELAUT to facilitate trust and accountability among the services deployed on the network.

## Interacting with the System

Engaging with the reputation system is facilitated through two primary avenues:

- **Browser Interface**: Accessible via [this link](https://reputation-systems.github.io/), the browser-based interface serves as the main gateway for general users to connect with the network. It offers an intuitive platform for users of all levels of expertise and acts as the foundational bedrock upon which more specialized applications can be built.
- **Library Integration**: Utilizing the library available at [this repository](https://github.com/reputation-systems/reputation-system-lib), users can deploy servers capable of harnessing the system's functionalities. This integration empowers the creation of bots proficient in data analysis and reputation staking. These bots play a vital role in enriching the ecosystem by contributing their own reputation, thus fostering a dynamic and self-sustaining network.

The browser interface caters to everyday users, providing a seamless entry point into the system. Meanwhile, the library integration enables more advanced interactions, allowing bots to actively participate and bolster the ecosystem's integrity. This dual-pronged approach ensures that the reputation system remains accessible to all users while facilitating sophisticated, automated interactions that reinforce the overall reliability of the blockchain environment.

## A Market Application Example

Imagine immersing ourselves in a decentralized market within Sigma Chains, where users trade products using smart contracts. In this setting, each bot acts as a product evaluator, fiercely competing to reach the pinnacle of reputation and providing simple ratings of "good" or "bad" based on their analysis.

In each buying and selling transaction, the bots spring into action, meticulously scrutinizing each product. They analyze details such as the item description, associated images, proposed price, and seller reputation. Driven by the desire for excellence and the opportunity to enhance their own reputation, each bot delivers its verdict on the product. By investing a portion of their reputation and determining whether this amount translates into a positive ("good") or negative ("bad") rating, the bots delve into evaluating every aspect of the product. This action not only contributes to their reputation but also enriches the reputation system as a whole by offering diverse perspectives on the quality and integrity of the products traded in the market.

In the heat of competition, each bot strives to achieve excellence. This tireless dedication is reflected in the issuance of accurate and insightful ratings, with the aim of gaining the trust and respect of users. When deciding which ratings to follow, users may consider the consistency and historical integrity of each bot.

Furthermore, bot developers enjoy great flexibility in designing their algorithms and evaluation parameters. They can customize which aspects of the product are highlighted most, which criteria are prioritized, and how ratings are assigned. This flexibility allows for a variety of approaches and strategies among the bots, further enriching the evaluation process.

The bots persist in their evaluative work, keeping abreast of new transactions in the market. This constant dedication ensures that ratings are current and accurately represent the quality and integrity of the products available.
