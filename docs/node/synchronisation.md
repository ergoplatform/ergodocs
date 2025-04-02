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

In Ergo, modifiers (blocks, transactions, etc.) progress through several states during the synchronization process:

- **Unknown:** The node is unaware of this modifier, or the synchronization process for it hasn't started.
- **Requested:** The modifier has been requested from one or more peers.
- **Received:** The modifier's data has been received from a peer but has not yet been fully validated and applied to the node's history or state.
- **Held:** The modifier has been successfully validated and applied. Persistent Modifiers (like Headers, BlockTransactions, ADProofs, Extension) are held by the History component, while Ephemeral Modifiers (like Transactions) are held by the Mempool before being included in a block.
- **Invalid:** The modifier has been determined to be permanently invalid according to consensus rules.

The primary goal of the synchronization process is to transition necessary modifiers from the **Unknown** state to the **Held** state, thereby bringing the node's view of the blockchain up-to-date with the network.

## Transition from Unknown to Requested

The transition of a modifier from the Unknown state to the Requested state can occur in different ways, depending on the current node status (bootstrapping/stable) and the type of modifier.

### Inv Protocol

The Inv (inventory) protocol is a communication protocol used during the synchronization process. It involves the following steps:

1. **Creating Inv Message:** An Inv message contains pairs of `(ModifierTypeId, Seq[ModifierId])`. When Node A sends an Inv message to Node B, it signals that Node A possesses the listed modifiers and is prepared to send them upon request from Node B.

2. **Broadcasting Inv Message:** A node broadcasts Inv messages primarily in two scenarios:
    1. When it successfully applies a new modifier (like a block header or transaction) to its History or Mempool. This helps propagate new information quickly across the network, especially when nodes are already synchronized.
    2. In response to receiving an `ErgoSyncInfo` message from a peer (see Headers Synchronization below).

3. **Receiving Inv Message:** Upon receiving an Inv message from a peer, a node:
    - Filters the list to identify modifiers it doesn't already know about (i.e., those currently in the **Unknown** state).
    - Requests these unknown modifiers from the peer that sent the Inv message.
    - Transitions the state of these requested modifiers to **Requested**.


## Headers Synchronization

Headers synchronization is the initial step in the synchronization process. It ensures that a node's headers chain is in sync with the network. The process involves the following steps:

1. **Sending ErgoSyncInfo:** Periodically (every `syncInterval`), a node calculates and sends an `ErgoSyncInfo` message to a selection of its peers (`peersToSyncWith()`). This message contains the IDs of the last `ErgoSyncInfo.MaxBlockIds` headers in its current best chain, allowing peers to compare chains.

2. **Triggering ErgoSyncInfo:** To speed up synchronization, a node might also send an `ErgoSyncInfo` message more frequently if its headers chain is lagging behind the network's perceived best chain, but the number of headers it still needs to request is relatively small (e.g., less than `desiredInvObjects / 2`).

3. **Receiving ErgoSyncInfo:** Upon receiving an `ErgoSyncInfo` message from a peer, a node compares the received header IDs with its own chain to determine the relative status (`OtherNodeSyncingStatus`: Younger, Older, Equal, Nonsense, or Unknown). Based on this comparison, it identifies any headers the sender might be missing from its own chain.

4. **Responding with Inv:** The node then constructs and sends an Inv message back to the original sender, containing the IDs of up to `maxInvObjects` headers that the sender appears to be missing. This helps the sender catch up.

## Block Section Synchronization

Block section synchronization is a crucial step that occurs after applying headers. A node synchronizes block sections (BlockTransactions, Extension, and ADProofs), the amount and composition of which may vary based on node settings. The process involves the following steps:

1. **Identifying Needed Modifiers:** Periodically (every `syncInterval`), a node determines the next set of block sections (`BlockTransactions`, `Extension`, `ADProofs`) it needs to download (`nextModifiersToDownload()`). This typically corresponds to the headers it has received but for which it lacks the full block data, starting from its current best *fully validated* block height.

2. **Requesting Modifiers:** The node requests these needed modifiers from random peers (as it doesn't know which specific peer has them). The state of these modifiers transitions to **Requested**.

3. **Triggering Downloads:** To speed up synchronization, the node might also request `nextModifiersToDownload()` more frequently if its header chain is synchronized but it's lagging behind in downloading block sections, provided the number of pending sections is small (e.g., less than `desiredInvObjects / 2`).

4. **Applying Block Header (Triggering Download):** When a node successfully applies a new block header while its header chain is considered synchronized, the History component might return `ProgressInfo` indicating which block sections (`ToDownload`) are now needed to fully validate and apply this new block and potentially older blocks.

5. **Processing ToDownload Request:** When the NodeViewSynchronizer (NVS) receives this `ToDownload` information (either from periodic checks or header application), it requests the necessary modifiers from random peers, transitioning their state to **Requested**.

## Transition from Requested to Received

The transition from the Requested state to the Received state involves the following steps:

1. **Tracking Requests:** When a node requests a modifier from a specific peer, it records this request (modifier ID and peer) in its `DeliveryTracker`. It also schedules a `CheckDelivery` message to itself after a `deliveryTimeout`.

2. **Receiving Modifiers:** When a node receives a modifier:
    - It checks if the modifier was requested from the sending peer using the `DeliveryTracker`.
    - If it was requested, the NodeViewSynchronizer (NVS) attempts to parse and perform initial validation on the received data.

3. **Handling Invalid Modifiers:**
    - If the received data fails parsing or initial validation (e.g., incorrect format, size limits exceeded), the NVS penalizes the sending peer and transitions the modifier's state to **Invalid**.
    - If the peer provided syntactically correct but semantically incorrect modifier bytes (which might fail later validation stages), the NVS penalizes the peer, and the modifier might revert to **Unknown** or be marked **Invalid** depending on the failure type.

4. **Processing Valid Modifiers:** If the modifier passes initial parsing and validation, the NVS sends it to the NodeViewHolder (NVH) for further processing and transitions the modifier's state to **Received**.

5. **Checking Delivery Timeout:** When the scheduled `CheckDelivery` message is processed:
    - If the modifier is already in the **Received** or **Held** state, no action is needed.
    - If the modifier is still in the **Requested** state (i.e., not delivered within the timeout), the node might retry the request a few times (`maxDeliveryChecks`).
    - If delivery ultimately fails after retries, the node penalizes the peer from which it was requested (unless it was requested from a random peer initially) and transitions the modifier's state back to **Unknown** so it can be requested again later, potentially from a different peer.

## Transition from Received to Held

The transition from the Received state to the Held state involves the following steps:

1. **Receiving Modifiers:** When the NodeViewHolder (NVH) receives new modifiers (in the **Received** state) from the NVS, it stores them temporarily in its `modifiersCache`.

2. **Applying Modifiers:** The NVH attempts to apply modifiers from the cache to the History and State components in the correct order (respecting dependencies).

3. **Handling Successful Application:** For every modifier successfully applied (passing all validation rules and updating History/State), the NVH publishes a `SyntacticallySuccessfulModifier` event. Upon receiving this event, the NVS transitions the modifier's state to **Held**.

4. **Handling Cache Size Limit:** If the `modifiersCache` exceeds its size limit after attempting applications, the NVH removes older or less relevant modifiers from the cache.

5. **Handling Processing Results:** After attempting to apply modifiers, the NVH publishes a `ModifiersProcessingResult` message listing which modifiers were successfully applied and which were removed from the cache (potentially because they were invalid or their dependencies weren't met yet). When the NVS receives this message, it transitions any modifiers that were removed from the cache *without* being successfully applied back to the **Unknown** state, allowing them to be potentially requested and processed again later. Modifiers that failed validation might be transitioned to **Invalid**.
