$$
\newcommand{\peers}{\mathcal{P}}
$$

# Peer management protocol

A *peer* is a pair `addr`, `port`, where `addr` is its IPv4/6 address and `port` is its port.

A *peer management structure* is a tuple (G, B, C), where G is the set of *good peers*, B is the set of *banned peers, and C is the set of *connected peers*, satisfying the following conditions:

- $G \cap B = \emptyset$,
- $C \subseteq G$,
- $G \subseteq \peers$,
- $B \subseteq \peers$.

## Peers penalization and blacklisting\label{subsec:peers-penalization-and-blacklisting

A *penalty* is a tuple `descr`, `score`, where `descr` is a misbehaviour description, and `score` is a penalty score.

A _penalty score_ defines how bad a concrete kind of misbehaviour is.

Penalties are divided into four categories:


* **NonDeliveryPenalty** - applied when a peer did not deliver the requested modifier in time
* **MisbehaviorPenalty** - applied when some modifier delivered by a peer appeared to be invalid
* **SpamPenalty** - applied when a peer-delivered non-requested modifier
* **PermanentPenalty** - applied to peers deviating from an actual network protocol


Once some penalty is applied, a penalised peer is added to the penalty book.

A *penalty book* is a mapping `ip` -> (`score, `ts), where `ip` is a peer IP address, `score` is an accumulated penalty score and `ts` is a timestamp when a corresponding peer was penalised last time.

Penalties of type `NonDeliveryPenalty, `MisbehaviorPenalty, `SpamPenalty` are not applied to the same peer repeatedly within a safe interval.

A *safe* interval is a delay between penalties application.

Once some peer accumulates a critical penalty score it is added to the blacklist.

A *blacklist* is a mapping `ip` -> `ts`, where `ip` is a peer IP address and `ts` is a timestamp a peer is banned till.

The `PermanentPenalty` is applied immediately and leads to a permanent ban of a peer

## Peer Discovery

A peer discovery protocol requests new peers from a source and inserts them into the set of good peers G.

Generally, a source may be another peer, a trusted central server or an untrusted communication channel (e.g. IRC, Twitter, ...).
