
# FAQ

### Why is this better than Tornado Cash? 

Tornado.Cash uses `zk-SNARKs`, which requires a "ceremony" to generate parameters required by the zk-SNARKs algorithm itself. This  Multi-party-computation means if only one participant of the MPC setup was honest, all others could try to cheat, and it would be secure. 

However, if all participants cheated and cooperated, they would have the ability to generate fake proofs later, and nobody will know about it.

In the specific case of tornado cash, it would mean that if all of the 1114 ceremony setup participants cheated, they could generate fake proofs and drain money from the tornado.cash smart contract.

However, if only one of them were honest, it would be secure for people to use.

ErgoMixer doesn't require this "ceremony" setup.

The computer where the MPC ceremony holds place should also be secure and destroyed after the ceremony. Otherwise, it could leak keys that a malicious attack can use to construct fake proofs. There's a really strong game theoric incentive to integrate some backdoor to the software or even hardware of MPC computer. 

### Showing as 'corrupted' on Mac

This can happen due to security preferences on Mac. Please run the following command.

```
sudo xattr -r -d com.apple.quarantine /Applications/ergoMixer.app
```
