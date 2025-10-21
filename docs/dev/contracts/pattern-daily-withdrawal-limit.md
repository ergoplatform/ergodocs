# Daily Withdrawal Limit

## Summary

- Problem: Enforce a maximum spendable amount per 24-hour window from a controlled box/vault.
- When to use: Custodial wallets, treasury safes, DAO treasuries, or user vaults where rate-limiting withdrawals reduces risk.
- Category: Access Control
- Status: Done

## Canonical Code & Tests

- Upstream  
  - PR: https://github.com/ergoplatform/sigmastate-interpreter/pull/1083 — Adds a daily withdrawal limit contract example with tests.
- Commit(s)  
  - Prefer pinned SHAs when available; add here once merged and stable.

## Security & Correctness Notes

- Assumptions  
  - Time semantics rely on block height or timestamp (per chosen approach) as a proxy for 24-hour windows.
  - State (e.g., “spent in current window”) is tracked in the contract box registers or successor state.
- Known limitations  
  - Block timestamps/heights are approximate; windows may not align perfectly with wall-clock time.
  - Off-chain must avoid crafting transactions that exceed the per-window limit across multiple chained spends.
- Test coverage  
  - Upstream tests validate enforcement within a window and reset across windows.

## Off-chain Integration

- Required flows  
  - Track per-window cumulative withdrawals in the box state; on each spend, update the accumulator and/or window marker (height/timestamp).
  - If the window has rolled over, reset accumulator before applying new withdrawal.
- SDK/API calls  
  - Fleet/AppKit: on transaction build, read current state and requested amount; fail early if it would exceed the limit.
- Data requirements  
  - Registers store: window marker (height/timestamp) and cumulative amount; ensure outputs propagate updated values.

## UI Considerations

- Minimal UI  
  - Show “remaining allowance” for the current window.
  - If a request exceeds remaining allowance, present next available time or suggest a smaller amount.
- Edge cases  
  - Handle close-to-window-boundary requests; warn users about possible miner ordering affecting acceptance.

## MCP Usage

- Provide a “rate-limited withdrawal” builder:  
  - Inputs: requestedAmount, policy (limitPerWindow, windowMetric), current state.  
  - Output: transaction template that updates state and prevents exceeding policy.
- Composition  
  - Can be combined with multisig governance for elevated limits or admin overrides (document separately).

## References

- Blockchain context (height/timestamp): dev/scs/blockchain-context.md
- Boxes and registers (state persistence): dev/scs/boxes-and-registers.md
- Read-only inputs / data inputs (state reads): dev/protocol/tx/read-only-inputs.md
- Talks/ErgoHack: Add references when collected.
- Related patterns: [pattern-stealth-address.md](pattern-stealth-address.md), [pattern-whitelist-token.md](pattern-whitelist-token.md)

## See also

- [Library index](contracts-library.md)
- [Additional contracts index](contracts.md)

## Contributor Checklist

- [x] Upstream code link(s) verified
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section at least outlines key flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section filled or explicitly marked N/A
- [x] Cross-linked from relevant category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Time windows on-chain are approximate; if precise wall-clock semantics are needed, consider oracle-assisted windows, noting added trust assumptions.
