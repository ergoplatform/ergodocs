---
tags:
  - Synchronization
  - Node
  - P2P
  - Protocol
  - Modifiers
  - Networking
  - Technical
---

# Blockchain Synchronization

In Ergo, modifiers can exist in one of the following states:

- **Unknown:** The synchronization process for the corresponding modifier has not started yet.
- **Requested:** The modifier has been requested from another peer.
- **Received:** The modifier has been received from another peer but has not been applied to history yet.
- **Held:** The modifier is held by NodeViewHolder. Persistent Modifiers are held by History, while Ephemeral modifiers are held by Mempool.
- **Invalid:** The modifier is permanently invalid.

The goal of the synchronization process is to transition modifiers from the Unknown state to the Held state. 

## Transition from Unknown to Requested

The transition of a modifier from the Unknown state to the Requested state can occur in different ways, depending on the current node status (bootstrapping/stable) and the type of modifier.

### Inv Protocol

The Inv (inventory) protocol is a communication protocol used during the synchronization process. It involves the following steps:

1. **Creating Inv Message:** The Inv message contains a pair: (ModifierTypeId, Seq[ModifierId]). When one node sends an Inv message to another, it indicates that this node contains modifiers with the specified IDs and type and is ready to send them upon request.

2. **Broadcasting Inv Message:** A node broadcasts the Inv message in two scenarios:
    1. When it successfully applies a modifier to History, and the modifier is new enough. This method helps propagate new modifiers as quickly as possible when nodes are already synced with the network.
    2. When it receives an ErgoSyncInfo message.

3. **Receiving Inv Message:** Upon receiving an Inv message, a node:
    - Filters out modifiers that are not in the Unknown state.
    - Requests the remaining modifiers from the peer that sent the Inv message. The Modifier then transitions into the Requested state.


## Headers Synchronization

Headers synchronization is the initial step in the synchronization process. It ensures that a node's headers chain is in sync with the network. The process involves the following steps:

1. **Calculating ErgoSyncInfo:** Every `syncInterval` seconds, the node calculates an ErgoSyncInfo message. This message contains IDs of the last `ErgoSyncInfo.MaxBlockIds` headers and is sent to peers, as defined by the function `peersToSyncWith()`.

2. **Efficient Synchronization:** To achieve more efficient synchronization, the node also sends an ErgoSyncInfo message every time when the headers chain is not synced yet, but the number of requested headers is small enough (less than `desiredInvObjects / 2`).

3. **Receiving ErgoSyncInfo:** Upon receiving an ErgoSyncInfo message, the node calculates OtherNodeSyncingStatus. This contains the node status (Younger, Older, Equal, Nonsense, or Unknown) and an extension - Inv for the next `maxInvObjects` headers missed by the ErgoSyncInfo sender.

4. **Sending Inv Message:** After calculating OtherNodeSyncingStatus, the node sends the resulting Inv message to the ErgoSyncInfo sender.

## Block Section Synchronization

Block section synchronization is a crucial step that occurs after applying headers. A node synchronizes block sections (BlockTransactions, Extension, and ADProofs), the amount and composition of which may vary based on node settings. The process involves the following steps:

1. **Calculating Modifiers:** Every `syncInterval` seconds, a node calculates `nextModifiersToDownload()`. This represents block sections for headers starting at the height of the best full block that is in the Unknown state.

2. **Requesting Modifiers:** These modifiers are requested from random peers (since we do not know which peer has them), and they transition to the Requested state.

3. **Efficient Synchronization:** To achieve more efficient synchronization, the node also requests `nextModifiersToDownload()` every time when the headers chain is already synced and the number of requested block sections is small enough (less than `desiredInvObjects / 2`).

4. **Applying Block Header:** When the headers chain is already synced and the node applies a block header, it returns a ProgressInfo with a ToDownload section. This contains modifiers our node should download and apply to update the full block chain.

5. **Processing ToDownload Request:** When the NodeViewSynchronizer (NVS) receives this ToDownload request, it requests these modifiers from random peers, and these modifiers transition to the Requested state.

## Transition from Requested to Received

The transition from the Requested state to the Received state involves the following steps:

1. **Requesting Modifiers:** When our node requests a modifier from another peer, it adds this modifier and the corresponding peer to a special map, `requested`, in the `DeliveryTracker`. It then sends a `CheckDelivery` message to itself with a `deliveryTimeout` delay.

2. **Receiving Modifiers:** When a node receives a modifier that exists in the requested map (and the peer who delivered this modifier is the same as the one recorded in the requested map), the NodeViewSynchronizer (`NVS`) parses it and performs initial validation.

3. **Handling Invalid Modifiers:** If the modifier is invalid, the `NVS` penalizes the peer and transitions the modifier to the Invalid state. If the peer has provided incorrect modifier bytes, the `NVS` penalizes the peer and transitions the modifier back to the Unknown state.

4. **Processing Valid Modifiers:** If the modifier is valid, the `NVS` sends the modifier to the NodeViewHolder (`NVH`) and transitions the modifier to the Received state.

5. **Checking Delivery:** When a `CheckDelivery` message is received, the node checks the state of the modifier. If it is already in the Received state, no action is taken. If the modifier has not been delivered yet, the node continues to wait for it up to `maxDeliveryChecks` times. After that, it penalizes the peer (if the modifier was not requested from a random peer) and stops expecting the delivery, transitioning the modifier back to the Unknown state.

## Transition from Received to Held

The transition from the Received state to the Held state involves the following steps:

1. **Receiving New Modifiers:** When the NodeViewHolder (`NVH`) receives new modifiers, it stores these modifiers in the `modifiersCache`.

2. **Applying Modifiers:** The `NVH` then applies as many modifiers from the cache as possible.

3. **Publishing Successful Modifiers:** For every successfully applied modifier, the `NVH` publishes a `SyntacticallySuccessfulModifier` message. When the NodeViewSynchronizer (`NVS`) receives this message, it transitions the modifier to the Held state.

4. **Handling Cache Size Limit:** If the cache size exceeds the limit after all applications, the `NVH` removes outdated modifiers from the cache.

5. **Publishing Processing Results:** The `NVH` publishes a `ModifiersProcessingResult` message containing all just applied and removed modifiers. When the `NVS` receives a `ModifiersProcessingResult` message, it transitions all modifiers that were removed from the cache without application back to the Unknown state.
