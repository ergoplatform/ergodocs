# Privacy Tools

Use this page as the entry point for privacy-related tools and concepts in the Ergo ecosystem.

## Start Here

| Goal | Page |
| --- | --- |
| Understand mixing | [ErgoMixer](ergomixer.md), [ErgoMixer FAQ](mixer-faq.md) |
| Use mixer safely | [Best Practices](best-practices.md), [Identifiability](identifiability.md) |
| Install on Android | [ErgoMixer on Android](mixer-android.md) |
| Explore other privacy patterns | [SigmaJoin](sigmajoin.md), [Stealth Addresses](stealth-address.md), [ZK Treasury](zkt.md) |

## Background

Coin mixers or tumblers are tools that improve fungibility by making transaction history harder to link. On Ergo, privacy tooling includes mixer designs, stealth-address patterns, and zero-knowledge contract ideas.

The basic mixing scheme used by ErgoMixer, ZeroJoin, is based on ring signatures and proof of knowledge for a [Diffie-Hellman tuple](diffie.md).

## Safety Notes

- Privacy tools do not remove the need for wallet safety.
- Learn the workflow with small amounts before using larger funds.
- Be careful with timing, address reuse, and metadata outside the blockchain.
