# RosenBridge Troubleshooting Guide

This guide helps diagnose and resolve the most common issues users see when bridging with Rosen. It complements the FAQs and Watcher/Guard docs with practical checks and fixes.

See also:
- How it works: [token-transfer-flows.md](token-transfer-flows.md)
- Fees and dust: [fees-and-dust.md](fees-and-dust.md)
- Security posture: [security-model.md](security-model.md)
- Watcher setup/troubleshooting: [watcher.md](watcher.md)
- Team/Operations FAQ: [rosen-faq.md](rosen-faq.md)

Useful links:
- Rosen App: https://app.rosen.tech
- Events Status: https://app.rosen.tech/events
- Asset List (verify tokens): https://app.rosen.tech/assets

## My event looks stuck

Symptoms:
- Event shows “pending,” “detected,” or similar for a long time
- No “approved” or “signed” state after a reasonable period

Checks:
- Confirmations: Verify your source-chain transaction has enough confirmations. Bridge timing depends on chain policy (e.g., BTC takes longer).
- Events page: Check https://app.rosen.tech/events for updates and error notes.
- Congestion: EVM gas spikes or network congestion can delay finality.
- Large transfers: Very large amounts may require cold ➜ hot fund movements by Guards; this can take hours to 1–2 days.

If it remains delayed far beyond normal windows, contact official support channels (Telegram/Discord) with:
- Source/target chains and tx hashes
- Destination address
- Time initiated

## “Insufficient ERG” but I have funds

Cause:
- Your wallet UTXOs may be fragmented into many small boxes, causing insufficient available value for fees in a single transaction.

Fix:
- Use wallet optimization / consolidation (e.g., Nautilus “Wallet Optimization”).
- Try reducing concurrent transactions so available inputs are not locked by pending txs.

More background: [fees-and-dust.md](fees-and-dust.md)

## rsToken not visible on target chain

Symptoms:
- Bridged completed, but token not shown by your wallet/DEX

Checks:
- Verify token on official Asset List: https://app.rosen.tech/assets
- For EVMs, add the token contract manually in your wallet (MetaMask etc.).
- For Cardano/Ergo, ensure your wallet supports the asset standard and is fully synced.

Never trust token addresses from chats/DMs; always cross-check with the official Asset List.

## EVM approval or “allowance” issues

Symptoms:
- Unable to swap/provide LP; DEX asks for repeated approvals

Checks:
- Reset/cancel stuck pending approvals in your wallet
- Use chain explorers’ approval checkers (e.g., BscScan Token Approval Checker)
- Ensure you’re on the correct network and the token contract matches the Asset List

## High or unexpected fees

Symptoms:
- Total fees higher than expected

Understand the fee components:
- Bridge fee: Greater of $10 or 0.5% of transfer value (adjustable by guard set)
- Network fees: Source/target chain network fees (static on Ergo/Cardano, dynamic on EVMs)

Tips:
- Batch actions (where safe) on EVMs to reduce gas overhead
- Avoid tiny transfers that are uneconomical after fees
- See [fees-and-dust.md](fees-and-dust.md)

## Long BTC/UTXO chain delays

Bitcoin & other UTXO chains:
- Delays are normal during fee spikes/mempool congestion
- Watchers require conservative confirmations before proceeding
- If using a self-run node (for Watchers), Bitcoin must be full with txindex=1 (not pruned). See [bitcoin-watcher.md](bitcoin-watcher.md)

## Wrong destination address or chain

If you provided an incorrect destination address or selected the wrong target chain:
- Transactions are final; Rosen cannot reroute assets post-finality
- Provide the full details to support immediately; outcomes depend on chain and status
- Always copy addresses from your wallet; avoid hand-typing

## Event “approved” but no finalization

Symptoms:
- Approved event box visible but no signed/broadcast transaction yet

Checks:
- Guard validation/signature collection is in progress; timing varies with chain and load
- Large-value transfers can be delayed for additional checks or liquidity positioning
- Continue monitoring https://app.rosen.tech/events

## Cardano/Ergo wallet synchronization issues

Symptoms:
- Wallet doesn’t show the bridged asset or updated balance

Fix:
- Ensure wallet fully synced to tip
- Restart wallet app; some wallets cache state
- Re-import account in extreme cases (with seed); verify balances in explorer first

## Bridged token appears but DEX refuses to list/swap

- DEXs may need token metadata or listing; permissionless DEXs usually accept by contract
- Verify the token contract and decimal settings
- Some curated venues require a manual listing process

## Troubleshooting matrix

- Delayed events: Check confirmations → Events page → Chain congestion → Large-value transfers → Support
- Wallet errors (insufficient ERG): Consolidate UTXOs → Retry
- Token visibility: Verify Asset List → Add token contract in wallet → Sync wallet
- EVM approvals: Reset approvals → Use official approval checkers → Confirm correct network/contract
- Watcher operators: See [watcher.md](watcher.md) (logs, volumes, health, minBoxValue, architecture-specific issues)

## When to escalate

Prepare:
- Source chain tx hash and target chain tx hash (if any)
- Destination address and asset
- Event URL from https://app.rosen.tech/events
- Timestamps and screenshots

Contact:
- Public Telegram/Discord channels listed on the Rosen site or dApp
