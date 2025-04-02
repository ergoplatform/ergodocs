---
tags:
  - Peer Management
  - Node
  - P2P
  - Protocol
  - Networking
---

$$
\newcommand{\peers}{\mathcal{P}}
$$
# Peer Management Protocol

## Definitions

A **peer** is identified by a pair consisting of an `addr` (IPv4/IPv6 address) and a `port` number.

A **peer management structure** within a node can be represented as a tuple (G, B, C), where:  

- G is the set of known *good peers*.
- B is the set of *banned peers*.
- C is the set of currently *connected peers*.

This structure adheres to the following invariants:

- The sets of good peers and banned peers are disjoint: $G \cap B = \emptyset$.
- The set of connected peers is always a subset of the good peers: $C \subseteq G$.
- Both G and B are subsets of the set of all possible peers $\peers$: $G \subseteq \peers$, $B \subseteq \peers$.

## Peer Penalization and Blacklisting

A **penalty** is represented as a tuple (`descr`, `score`), where `descr` describes the type of misbehavior, and `score` quantifies its severity.

There are four categories of penalties:

* **NonDeliveryPenalty**: Applied when a peer fails to deliver a requested modifier within the expected timeframe.
* **MisbehaviorPenalty**: Applied when a peer delivers an invalid modifier (e.g., one failing validation rules).
* **SpamPenalty**: Applied when a peer delivers an unsolicited modifier (one that was not requested).
* **PermanentPenalty**: Applied for severe protocol deviations, resulting in an immediate and permanent ban.

When a penalty is imposed, the penalized peer's information is updated in the **penalty book**. The penalty book maps an IP address (`ip`) to its current accumulated penalty `score` and the timestamp (`ts`) of the last penalty event: `ip` -> (`score`, `ts`).

To prevent excessive penalization for transient issues, penalties of type `NonDeliveryPenalty`, `MisbehaviorPenalty`, and `SpamPenalty` are not applied repeatedly to the same peer within a defined **safe interval** (a cooldown period between penalties).

When a peer's accumulated `score` reaches a predefined critical threshold, the peer is added to the **blacklist**. The blacklist maps a banned peer's IP address (`ip`) to the timestamp (`ts`) when the ban was initiated: `ip` -> `ts`. Peers typically remain on the blacklist for a configurable duration, after which they might be removed and potentially re-added to the set of good peers.

Applying a `PermanentPenalty`, however, results in the peer being added to the blacklist indefinitely.

## Peer Discovery

The peer discovery protocol aims to find new potential peers from various sources and add them to the set of good peers (G). Sources for discovery can include:

- Other connected peers (exchanging peer lists).
- Predefined bootstrap nodes.
- Trusted central servers (less common in decentralized networks).
- Potentially untrusted channels like DNS seeds, IRC, Twitter, etc. (requiring careful validation).
