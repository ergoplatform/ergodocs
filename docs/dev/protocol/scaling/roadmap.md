# Scaling Roadmap

For discussions on scaling please join the [Telegram](https://t.me/ErgoLayer2) or [#layer2 on discord](https://discord.gg/nr4JRnhAyV)

## Timeline

Currently, our focus is on integrating UTXO set snapshots and Non-Interactive Proofs of Proof-of-Work (NiPoPoWs) to achieve ultra-fast bootstrapping. This approach will provide a fast sync with the same level of security as if they had processed every block since genesis. Upon successful stabilization of this implementation, we advise miners to contemplate increasing block limits once more.

- (TBA) Node V6 Planning & scalability improvements
- (WIP) SPV Client
- Bootstrapping with UTXO Set [now live](pruned-full-node.md)
- [Node V5](jitc.md) released.
- GetBlok release [Plasma Library](plasma.md)
- Plasma Tutorials released.

## Roadmaps

> [Kushti, 7 Aug, 2023](https://t.me/ergoplatform/419168)
> 
> Starting to design things. I think better to start from foundations. Ergo was designed as commodity money (digital gold) with programmability (even more, possibility for crypto contracts, like stealth addresses, arbitrarily complex signatures, mixing schemes and so on),to be a basis for unstoppable (by banksters or "regulators") grassroot economies, these days can be thought as cbdcs for the people (while cbdcs for large scale governments do not have sense imho). Initial experiments are going well considering the motivation.

> Now it is time for scaling and adoption. Which needs in the first place for defining adoption, as this term does not really mean anything concrete in most conversations in the space I've witnessed.

>  Then p2p level optimizations and rework, with considering options for pre block commitments to tx ordering (sub blocks), while increasing tps securily significantly as well. There are limits here anyway as there is requirement to have flat p2p network run on commodity hardware (not banksters' datacenters). Thus at the same time options for offloading transactions to l2 or sidechains also should be proposed (if not implemented). [KYA](kya.md) was in particular introduced to explain offloading options security in concise and understandable fashion.

>  Thus few developments are going to converge.


- (Nov 22) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226/4?u=glasgowm)
- (Dec 21) [Ergo protocol research and client development roadmap](https://www.reddit.com/r/ergonauts/comments/qfjhw4/ergo_protocol_research_and_client_development/)
- (Sep 21) [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629)
- (Jul 21) [Network congestion on Jul 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
- (May 20) [Protecting mempool from computationally heavy transactions](https://www.ergoforum.org/t/protecting-mempool-from-computationally-heavy-transactions/231)
- (May 20) [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)

