$$
\newcommand{\peers}{\mathcal{P}}
$$
# Peer Management Protocol

## Definitions

A **peer** is a pair consisting of `addr` (IPv4/6 address) and `port` (port number).

A **peer management structure** is a tuple, (G, B, C), where:  

- G represents the set of *good peers*,
- B stands for the set of *banned peers*,
- C signifies the set of *connected peers*.

This structure adheres to the following conditions:

- Good peers (G) and banned peers (B) are disjoint: $G \cap B = \emptyset$.
- Connected peers (C) are a subset of good peers: $C \subseteq G$.
- Good peers (G) and banned peers (B) are subsets of all peers: $G \subseteq \peers$, $B \subseteq \peers$.

## Peer Penalization and Blacklisting

A **penalty** is a tuple `descr`, `score`, where `descr` describes misbehaviour, and `score` is the penalty score that signifies the degree of misbehaviour.

There are four categories of penalties:

* **NonDeliveryPenalty**: Applied when a peer fails to deliver the requested modifier within the stipulated time frame.
* **MisbehaviorPenalty**: Applied when a peer delivers an invalid modifier.
* **SpamPenalty**: Applied when a peer delivers a non-requested modifier.
* **PermanentPenalty**: Levied on peers who deviate from the actual network protocol.

When a penalty is imposed, the penalized peer is added to the penalty book. A **penalty book** is a mapping `ip` -> (`score, `ts), where `ip` represents a peer IP address, `score` signifies the accumulated penalty score, and `ts` is the timestamp of when the peer was last penalized.

Penalties of type `NonDeliveryPenalty`, `MisbehaviorPenalty`, and `SpamPenalty` are not imposed on the same peer repetitively within a specified safe interval. A **safe interval** refers to the delay between the application of penalties.

When a peer accumulates a critical penalty score, it gets added to the blacklist. A **blacklist** is a mapping `ip` -> `ts`, where `ip` stands for a peer IP address and `ts` represents the timestamp when a peer is banned.

The application of `PermanentPenalty` is immediate and results in the permanent ban of the peer.

## Peer Discovery

The peer discovery protocol seeks new peers from a source and introduces them to the set of good peers, G. The source could be another peer, a trusted central server, or an untrusted communication channel such as IRC, Twitter, etc.