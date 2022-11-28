*Ergo’s Zero-Knowledge Treasury enables users to easily create joint digital signatures, with bespoke conditions for spending funds while ensuring the signatories to the created address remain hidden.*

Zero-Knowledge (ZK) cryptography offers lots of powerful use cases. The benefit of ZK operations is that they are secure, but they’re private.

Imagine you find a smartphone on the ground in the park. A woman close by claims it’s hers, but you don’t trust her. Perhaps she wants the phone. She could give you the unlock code, but then you’d gain information that, as the owner, she wouldn’t want you to have. So, you close your eyes and hold out the phone, and when you open them, the screen is unlocked. She has proved ownership without giving away sensitive information. That’s a simple example of zero-knowledge proof.

The applications in the blockchain world are compelling. Consider a conventional two-of-three multi-sig address on the Bitcoin blockchain. This requires that any two out of three private key holders for that address have to sign a transaction for funds to be moved. It’s much more secure than a single-signature address, but it lacks privacy. Anyone can look at the blockchain and know exactly who signed the transaction.

With a zero-knowledge signature, no one knows who is responsible for a transaction – only that the required number of private keys have signed it.

Ergo’s Sigma Protocols are excellent for creating composable ZK signatures. In other words, a group of users can get together and create an address with the conditions they specify. For example, five users could create an address that any three of them need to sign to make a transaction. Or the conditions could be more complicated. A startup consisting of seven people could create an address whereby the CEO and CFO must sign to release funds. Any five key holders can sign a transaction (offering an insurance policy if either CEO or CFO is out of action).

Ergo has always been a community-driven project, and we’ve always had solid and enthusiastic support from our developers, many of whom prefer to remain anonymous. One of our anons has pioneered a user-friendly interface that makes it easy to form joint spending groups that require a quorum of signatories to make a transaction (since the process for doing this was previously complex, even for more technical users).

*User [‘anon_real’ writes](https://www.ergoforum.org/t/app-on-distributed-signatures/342):*

*This project contains two separate apps, server and client.*

*The server is accessible by everyone who can propose ideas and ask for funds from a team.*

*On the other hand, every team member has to set up the client app, which will interact with their secret, node, explorer, and server to create the necessary proofs for approved proposals.*

*If a proposal is marked as fully approved (enough approvals have been collected based on the team’s signature), then client apps will generate necessary proofs and transactions in the background without needing any intervention by members.*

![](/img/uploads/ergsig.jpg)

You can find further [discussion of the Zero-Knowledge Treasury on the Ergo forum](https://www.ergoforum.org/t/zero-knowledge-treasury-on-top-of-ergo/354/3).

There are many use cases for this application beyond securely spending funds on Ergo. For example, a similar interface could be the foundation of decentralised [public key infrastructure](https://www.ssh.com/pki/) (dPKI): a means of generating and managing public/private keypairs to authenticate users and devices, but without the centralised points of failure that exist in trusted PKI setups.

A big thanks to anon_real, and we look forward to seeing the ZK Treasury used in the Ergo community!

