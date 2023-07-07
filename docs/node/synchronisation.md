# Blockchain Synchronization

Ergo modifiers can be in one of the following states:

- **Unknown:** The synchronization process for the corresponding modifier is not started yet.
- **Requested:** The modifier was requested from another peer.
- **Received:** The modifier was received from another peer, but is not applied to history yet.
- **Held:** The modifier was held by NodeViewHolder. Persistent Modifiers are held by History, Ephemianl modifiers are held by Mempool.
- **Invalid:** The modifier is permanently invalid.

The goal of the synchronization process is to move modifiers from the Unknown to Held state. 

## From Unknown to Requested

The modifier can transition from the Unknown state to the Requested one in different ways, depending on the current node status (bootstrapping/stable) and modifier type.

### Inv Protocol

The Inv (inventory) message contains a pair: (ModifierTypeId, Seq[ModifierId]). When one node sends an Inv message to another, it is assumed that this node contains modifiers with the specified ids and type and is ready to send on request.

A node broadcasts the Inv message in two cases:

- When it successfully applies a modifier to History, and the modifier is new enough. This approach helps propagate new modifiers as fast as possible when nodes are already synced with the network.
- When it receives an ErgoSyncInfo message (see **Headers synchronization** for more details).

When a node receives an Inv message, it:

- Filters out modifiers that are not in the Unknown state.
- Requests the remaining modifiers from the peer that sent the Inv message. The Modifier then transitions into the Requested state.

### Headers Synchronization

Firstly, a node should synchronize its headers chain with the network. To achieve this, every `syncInterval` seconds, the node calculates an ErgoSyncInfo message, containing ids of the last `ErgoSyncInfo.MaxBlockIds` headers and sends it to peers, defined by function `peersToSyncWith()`.

To achieve more efficient synchronization, the node also sends an ErgoSyncInfo message every time when the headers chain is not synced yet, but the number of requested headers is small enough (less than `desiredInvObjects / 2`).

On receiving an ErgoSyncInfo message, the node calculates OtherNodeSyncingStatus, which contains node status (Younger, Older, Equal, Nonsense or Unknown) and extension - Inv for the next `maxInvObjects` headers missed by ErgoSyncInfo sender. After that, the node sends this Inv message to the ErgoSyncInfo sender.

### Block Section Synchronization

After applying headers, a node should synchronize block sections (BlockTransactions, Extension, and ADProofs), which amount and composition may vary based on node settings.

To achieve this, every `syncInterval` seconds, a node calculates `nextModifiersToDownload()` - block sections for headers starting at the height of the best full block that is in the Unknown state.

These modifiers are requested from random peers (since we do not know a peer who has it) and they switch to the Requested state.

To achieve more efficient synchronization, the node also requests `nextModifiersToDownload()` every time when the headers chain is already synced and the number of requested block sections is small enough (less than `desiredInvObjects / 2`).

When the headers chain is already synced and the node applies a block header, it returns ProgressInfo with a ToDownload section, that contains modifiers our node should download and apply to update the full block chain.

When NVS receives this ToDownload request, it requests these modifiers from random peers, and these modifiers transition to the Requested state.

## From Requested to Received

When our node requests a modifier from another peer, it adds this modifier and corresponding peer to a special map, `requested` in `DeliveryTracker`, and sends `CheckDelivery` to self with a `deliveryTimeout` delay.

When a node receives a modifier in the requested map (and the peer who delivered this modifier is the same as written in requested), NVS parses it and performs initial validation.

If the modifier is invalid, NVS penalizes the peer and moves the modifier to the Invalid state. If the peer has provided incorrect modifier bytes, penalize the peer and move the modifier to the Unknown state. If everything is fine, NVS sends the modifier to `NodeViewHolder(NVH)` and sets the modifier to the Received state.

When `CheckDelivery` message comes, the node checks for the modifier if it is already in the Received state, does nothing. If the modifier is not delivered yet, the node continues to wait for it up to `maxDeliveryChecks` times, and after that penalizes the peer (if not requested from a random peer) and stops expecting after that (the modifier goes to the Unknown state).

## From Received to Held

When `NVH` receives new modifiers, it puts these modifiers into `modifiersCache` and then applies as many modifiers from the cache as possible.

`NVH` publishes a `SyntacticallySuccessfulModifier` message for every applied modifier, and when `NVS` receives this message, it moves the modifier to the Held state.

If after all applications, the cache size exceeds the size limit, `NVH` removes outdated modifiers from the cache and publishes a `ModifiersProcessingResult` message with all just applied and removed modifiers. When `NVS` receives a `ModifiersProcessingResult` message, it moves all modifiers removed from the cache without application to the Unknown state.