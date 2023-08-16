# Understanding Difficulty Adjustment in Ergo
> Utilize the [Difficulty & Epoch Monitor](https://cds.oette.info/ergo_diff.htm) to predict upcoming difficulty adjustments. 

Before the introduction of [EIP37](https://docs.ergoplatform.com/mining/standards/eip37/), Ergo's Autolykos protocol employed a steady difficulty adjustment mechanism to counter hash rate variations. This approach, superior to Bitcoin's with a 1.9% error rate compared to Bitcoin's 9.1%, was designed to deter adversarial hopping. The adjustment mechanism, based on the linear least squares method, used the previous eight epochs (equivalent to 8,192 blocks) to predict the difficulty function, as explained in [this paper](https://eprint.iacr.org/2017/731.pdf). The goal was to maintain a 120-second (or 2-minute) block interval during stable hash rate periods.

However, this system was vulnerable to significant hash rate surges over several epochs, especially when the hash rate growth was super-linear over time (as observed during the ETH merge). This vulnerability could result in severe difficulty spikes. Similarly, during slow epochs, the difficulty could drop significantly. To address these issues, EIP37 was proposed and later implemented. This new protocol offered a more responsive difficulty adjustment by considering a shorter, recent block history, thereby minimizing the impact of sudden hash rate changes. With EIP37, Ergo's mining process has become more robust and secure against adversarial disruptions.

## The Rationale Behind a 2-Minute Block Interval

Ergo's 2-minute target block interval was selected to offer a crucial security margin against various potential issues and attacks in a peer-to-peer cryptocurrency network that supports smart contracts. These potential threats include propagation delays, spam attacks, verifier dilemmas, among others. 

A shorter block interval might expose the network to Timewarp attacks — a type of difficulty manipulation attack that can cause blocks to be mined too quickly or too slowly. In a Timewarp attack, a miner manipulates the timestamps of the blocks they mine to trick the network into thinking more time has passed than actually has. This can lead to the network lowering the mining difficulty, allowing the attacker to mine blocks more quickly. 

Moreover, a shorter block interval could also increase the risk of orphaned blocks. Orphaned blocks occur when two miners solve a block at nearly the same time. The network can only accept one, leaving the other as an 'orphan'. This not only wastes computational resources but can also lead to double-spending attacks if not properly managed.

Ergo's epoch length is approximately 4.2 hours (assuming a normal block rate), a significant improvement over Bitcoin's two-week parameter. In summary, a 2-minute block interval strikes a balance between ensuring network security and maintaining transaction speed, making Ergo an efficient and secure cryptocurrency suitable for everyday use.