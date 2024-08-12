# Ergo Scaling Roadmap

Join our discussions on scaling on [Telegram](https://t.me/ErgoLayer2) or [#layer2 on discord](https://discord.gg/nr4JRnhAyV). We welcome all insights and contributions.

## Current Focus

With the successful integration of UTXO set snapshots and Non-Interactive Proofs of Proof-of-Work (NiPoPoWs) for ultra-fast bootstrapping in the pruned full node, our focus has now shifted towards optimizing this implementation. We are also exploring ways to further increase block limits for miners, given the live status of the pruned full node.

## Recent Developments

- (TBA) Planning for Node V6 & scalability improvements
- (WIP) Development of SPV Client
- Pruned Full Node is [now live](pruned-full-node.md)
- Release of [Node V5](jitc.md)
- GetBlok released the [Plasma Library](plasma.md)
- Plasma Tutorials have been published

## Roadmaps

### Ergo Design and Implementation Roadmap

#### Phase 1: Foundations

- Start with the basic design of Ergo as digital gold (commodity money).
- Introduce programmability features including:
  - Crypto contracts
  - Stealth addresses
  - Arbitrarily complex signatures
  - Mixing schemes
- Position Ergo as a basis for unstoppable, grassroots economies, serving as a decentralized central bank digital currency [(CBDC)](cbdc.md) for the people.

#### Phase 2: Initial Experiments

- Conduct initial experiments to test functionality and user engagement.
- Evaluate the outcomes considering the initial motivations.

#### Phase 3: Defining Adoption

- Clarify the term "adoption" as it is often ambiguous in industry discussions.
- Develop metrics or KPIs to measure adoption success.

#### Phase 4: Scaling and Optimization

- Peer-to-peer (P2P) level optimizations and rework.
- Consider pre-block commitments to transaction ordering (sub-blocks).
- Aim to increase transactions per second (TPS) while maintaining security.

#### Constraints for Scaling

- Limitations include requirements for a flat P2P network running on commodity hardware.
- No use of centralized or "bankster" data centers for scalability.

#### Phase 5: Offloading Solutions

- Propose options for offloading transactions to Layer 2 or sidechains, if not already implemented.
- Introduce "Know Your Algorithm" [KYA](kya.md) as a way to explain security in offloading options in a concise and understandable manner.

#### Phase 6: Convergence

- Multiple developments in scaling, optimization, and offloading are expected to converge, culminating in a comprehensive solution for widespread adoption.

Summarised from [Kushti, 7 Aug, 2023](https://t.me/ergoplatform/419168)


- (Nov 22) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226/4?u=glasgowm)
- (Dec 21) [Ergo protocol research and client development roadmap](https://www.reddit.com/r/ergonauts/comments/qfjhw4/ergo_protocol_research_and_client_development/)
- (Sep 21) [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629)
- (Jul 21) [Network congestion on Jul 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
- (May 20) [Protecting mempool from computationally heavy transactions](https://www.ergoforum.org/t/protecting-mempool-from-computationally-heavy-transactions/231)
- (May 20) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)


