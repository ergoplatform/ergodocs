
# Blockchain synchronization

Ergo modifiers can be in one of the following states:


* Unknown synchronization process for corresponding modifier is not started yet.
* Requested modifier was requested from another peer.
* Received modifier was received from another peer, but is not applied to history yet.
* Held modifier was held by NodeViewHolder PersistentModifiers are held by History, Ephemeral modifiers are held by Mempool.
* Invalid modifier is permanently invalid.


The goal of the synchronization process is to move modifiers from Unknown to Held state.

In the success path modifier changes his statuses Unknown->Requested->Received->Held, however if something went wrong (e.g. modifier was not delivered) it goes back to Unknown state (if node is going to receive it in future) or to Invalidstate (if node is not going to receive this modifier anymore).

## From Unknown to Requested

Modifier can go from Unknown state to Requested one by different ways, that depend on
current node status (bootstrapping/stable) and modifier type.

**Inv protocol

Inv (inventory) message contains a pair: (ModifierTypeId, Seq[ModifierId]).
When one node sends Inv message to another one, it is assumed that this node
contains modifiers with the specified ids and type and is ready to send on request.

Node broadcasts Inv message in 2 cases:

    *  When it successfully applies a modifier to History and modifier is new enough.
    This is useful to propagate new modifiers as fast as possible when nodes are already synced with the network
    *  When it receives ErgoSyncInfo message (see **Headers synchronization for more details)


When node received Inv message it

    *  filter out modifiers, that are not in state Unknown
    *  request remaining modifiers from the peer that sent Inv message.
    Modifier goes into Requested state.


**Headers synchronization

First, node should synchronize it's headers chain with the network.
In order to achieve this every syncInterval seconds node calculates ErgoSyncInfo message,
containing ids of last ErgoSyncInfo.MaxBlockIds headers and send it to peers,
defined by function peersToSyncWith().
If there are outdated peers (peers, which status
was last updated earlier than syncStatusRefresh seconds ago) peersToSyncWith() return outdated peers,
otherwise it returns one random peer which blockchain is better and all peers with status Unknown
\dnote{peersToSyncWith() logic is not intuitive, it's better to write description, why this choice?.

To achieve more efficient synchronization, node also sends ErgoSyncInfo message every time when headers chain is
not synced yet, but number of requested headers is small enough (less than $desiredInvObjects / 2$).

On receiving ErgoSyncInfo message, node calculates OtherNodeSyncingStatus,
which contains node status (Younger, Older, Equal, Nonsense or Unknown) and extension -
Inv for next maxInvObjects headers missed by ErgoSyncInfo sender.
After that node sends this Inv message to ErgoSyncInfo sender.

**Block section synchronization**

After headers application, a node should synchronize block sections (BlockTransactions, Extension and ADProofs), which amount and composition may vary on node settings (node with UTXO state does not need to download ADProofs, node with non-negative blocksToKeep should download only block sections for last blocksToKeep blocks, etc.).

In order to achieve this, every syncInterval seconds node calculate nextModifiersToDownload() - block sections for headers starting at height of best full block, that are in Unknown state.

These modifiers are requested from random peers (since we does not know a peer who have it), \footnote{we can keep a separate modifierId->peers map for modifiers, that are not received yet and try to download from this peers first.
and they switch to state Requested.

To achieve more efficient synchronization, node also requests nextModifiersToDownload() every time when
headers chain is already synced and number of requested block sections is small enough (less than $desiredInvObjects / 2$).

When headers chain is already synced and node applies block header, it return ProgressInfo with ToDownload section, that contains modifiers our node should download and apply to update full block chain.

When NVS receives this ToDownload request, it requests these modifiers from random peers and these modifiers goes to state Requested.

## From Requested to Received

When our node requests a modifier from other peer, it puts this modifier and corresponding peer to special map requested in DeliveryTracker and sends CheckDelivery to self with deliveryTimeout delay.

When a node receives modifier in requested map (and peer delivered this modifier is the same as written in requested) -
NVS parse it and perform initial validation.

If modifier is invalid (and we know, that this modifier will always be invalid) NVS penalize peer and move modifier to state Invalid.
If the peer have provided incorrect modifier bytes (we can not check, that these bytes corresponds to current id) penalize peer and move modifier to state Unknown.
If everything is fine, NVS sends modifier to NodeViewHolder(NVH) and set modifier to state Received.

When CheckDelivery message comes, node check for modifier if it is already in Received state, do nothing.

If modifier is not delivered yet, node continue to wait it up to maxDeliveryChecks times, and after that
penalize peer (if not requested from random peer) and stop expecting after that (modifier goes to Unknown state).

## From Received to Held

When NVH receives new modifiers it puts these modifiers to modifiersCache and then applies as much modifiers from cache as possible.

NVH publish SyntacticallySuccessfulModifier message for every applied modifier and when NVS receives this message it moves modifier to state Held.

If after all applications cache size exceeds size limit, NVH remove outdated modifiers from cache and publish
ModifiersProcessingResult message with all just applied and removed modifiers.
When NVS receives ModifiersProcessingResult message it moves all modifiers removed from cache without application to state Unknown.