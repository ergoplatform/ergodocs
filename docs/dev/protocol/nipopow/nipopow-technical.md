---
tags:
  - NIPoPoWs
---
# Ergo NiPoPoW Technical Documentation

## Overview

Ergo’s **Non-Interactive Proofs of Proof-of-Work (NiPoPoWs)** enable secure, succinct blockchain proofs for light clients, sidechains, and cross-chain protocols. This implementation reduces the need for full chain downloads by allowing verification with only a *logarithmic number* of block headers.

---

## What Are NiPoPoWs?

**NiPoPoWs** are cryptographic proofs that demonstrate a blockchain’s proof-of-work history up to the present in a trustless, compressed format. They rely on the presence of *superblocks* — blocks whose proof-of-work difficulty exceeds a given level — creating a succinct chain summary that a verifier can check non-interactively.

They were formalized in the paper “[Non-Interactive Proofs of Proof-of-Work](https://eprint.iacr.org/2017/963.pdf)” by Bünz et al.

---

## How It Works in Ergo

### 1. **Superblock Hierarchy**

Each block’s PoW solution is analyzed to determine its *level*:

* **Level-0** blocks are all blocks.
* **Level-1+** blocks are those whose PoW hash has extra leading zeros, representing exponentially higher difficulty.

This hierarchy ensures there are a logarithmic number of superblocks relative to the chain length.

### 2. **Proof Construction**

When a light client requests a NiPoPoW, the full node:

* Samples superblocks at various levels up to the highest.
* Constructs interlink pointers to maintain chain-of-trust.
* Adds some context blocks to prevent block reordering attacks.
* Attaches a succinct suffix to prove recency.

A typical **NiPoPoW proof** size is:

* **Header-only:** \~5–30 KB for a multi-year chain snapshot.
* **Combined with UTXO snapshot:** \~200–600 MB for the snapshot file, plus the proof.

  * Snapshots are compressed Merkleized state digests.

Thus, a new light client can bootstrap in minutes instead of days.

---

## Example Data Flow

**Example: NiPoPoW-based bootstrap for a light wallet**

1. The wallet requests:

      * Latest block headers.
      * NiPoPoW proof covering the chain up to a chosen block.
      * UTXO snapshot hash and file.

2. The node responds with:

      * `PoPoWProof` file (5–30 KB).
      * Signed UTXO snapshot (\~200–600 MB).
      * Relevant metadata: height, root hash, signatures.

3. The wallet:

      * Verifies the NiPoPoW proof by checking that sampled superblocks link correctly and cumulative PoW is valid.
      * Validates the snapshot’s Merkle root matches the expected state root.
      * Begins operations with trusted state.

---

## Where It’s Implemented

In [**ergoplatform/ergo**](https://github.com/ergoplatform/ergo):

**Proof generation**

`ergo-core/src/main/scala/org/ergoplatform/modifiers/history/PoPoWProof.scala`

 **Bootstrap flow**

`src/main/scala/org/ergoplatform/nodeView/history/`
  
**NiPoPoW settings**

```hocon
ergo.node.nipopow.nipopowBootstrap = true
```

**UTXO snapshot generation**

`src/main/scala/org/ergoplatform/nodeView/state/`

---

## 🔒 Security Considerations

| Aspect                          | Details                                                                                                                             |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Adversary model**             | Assumes honest majority in PoW mining and difficulty consistency.                                                                   |
| **Proof size security**         | Proof size is logarithmic in chain length; small enough for light clients but includes enough context to resist reordering attacks. |
| **UTXO snapshot**               | Must be signed and validated against the proof’s final block header to prevent fake states.                                         |
| **Replay protection**           | Clients verify timestamps to avoid accepting stale or replayed proofs.                                                              |
| **Expected bootstrapping time** | Typically under **5–10 minutes** on modern connections with a \~600 MB snapshot.                                                    |

---

## ⚡ Expected Proof Sizes

| Chain Age      | Typical Proof Size |
| -------------- | ------------------ |
| \~1 week chain | \~1 KB             |
| \~1 year chain | \~10–15 KB         |
| \~5 year chain | \~30–40 KB         |
| UTXO snapshot  | \~200–600 MB       |

> 📝 **Note:** These estimates depend on the block interval and superblock level parameters. Ergo uses 2-minute blocks, so the number of superblocks grows slowly.

---

## 🛠️ Using NiPoPoWs in Practice

To enable:

```hocon
ergo {
  node {
    nipopow {
      nipopowBootstrap = true
    }
  }
}
```

Clients can download and verify proofs using:

* HTTP API endpoints for snapshots and proofs.
* A NiPoPoW verifier (e.g., the reference Scala implementation or libraries in other languages).

---

## Example Verifier Flow

A verifier:

1. Receives the `PoPoWProof`.
2. Verifies the chain-of-trust from genesis to last superblock.
3. Checks the cumulative PoW.
4. Validates the UTXO snapshot root hash.
5. Accepts the snapshot as the starting point for their wallet or application.

---

## Learn More

* [NiPoPoW White Paper](https://eprint.iacr.org/2017/963.pdf)
* [UTXO Bootstrapping](https://docs.ergoplatform.com/node/utxo-bootstrapping/)
* [Ergo Protocol White Paper](https://ergoplatform.org/docs/whitepaper.pdf)

---

## Related Components

* **UTXO Bootstrapping:** Efficient state syncing.
* **Stateless Clients:** Fully NiPoPoW-compatible clients.
* **Sidechains:** NiPoPoWs enable succinct cross-chain proofs.

---

## Conclusion

Ergo’s NiPoPoW implementation is a practical, production-grade use of succinct proofs for real-world blockchain scalability. It is actively used by wallets and services that need trustless syncing without storing the entire chain.
