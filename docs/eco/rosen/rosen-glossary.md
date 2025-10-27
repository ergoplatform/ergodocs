# RosenBridge Glossary

Quick definitions of RosenBridge-specific terms. For deeper context, see: [concepts-assumptions.md](concepts-assumptions.md), [token-transfer-flows.md](token-transfer-flows.md), [security-model.md](security-model.md), [rosen-tokenomics.md](rosen-tokenomics.md)

- Guard
  - A permissioned signer that independently verifies approved events and signs transactions on Ergo or external chains using multisig/threshold signatures.
  - See: [rosen-guard.md](rosen-guard.md)

- Watcher
  - A keyless participant that monitors chains, verifies deposits/withdrawals, creates “event boxes” on Ergo, and helps reach on-chain consensus about events.
  - See: [watcher.md](watcher.md)

- Event Box
  - An Ergo box created by a Watcher to record a detected event (e.g., a confirmed deposit on the source chain). Multiple event boxes aggregate toward consensus.

- Approved Event Box
  - The on-Ergo confirmation that enough Watchers have converged on the same event. Guards scan for approved event boxes to start verification and signing.

- Bank Box (Ergo)
  - A contract box on Ergo that accepts rToken burns (or holds state) for reverse flows back to source chains.
  - See: [token-transfer-flows.md](token-transfer-flows.md)

- rToken (Representative Token)
  - A token on Ergo representing locked native assets held on a source chain (e.g., rBTC). Minted on ChainX ➜ Ergo; burned on Ergo ➜ ChainX.

- RSN (Rosen Token)
  - The Rosen ecosystem token used for fees, incentives, staking, and watcher permits. See: [rosen-tokenomics.md](rosen-tokenomics.md)

- RosenEvent Token
  - A token watchers receive (backed by staked RSN) to create event boxes. Returned on successful events; forfeited on fraudulent reports (slashing).
  - See: [rosen-tokenomics.md](rosen-tokenomics.md)

- Permit
  - A watcher’s right to participate in reporting events. Multiple permits may be needed to report concurrent events. Can be slashed for fraud.

- Collateral
  - RSN and ERG staked by watchers (and RSN by guards) that can be slashed in case of malicious behavior. Aligns incentives for honest participation.

- Guard Set
  - The current group of federated signers managing chain wallets and final signatures. Typically curated for diversity and resilience.

- ChainX
  - A placeholder term for any external blockchain in the bridge (e.g., Bitcoin, Cardano, Ethereum, BSC, Dogecoin).

- Fees
  - Bridge fee (greater of $10 or 0.5% initially, adjustable) plus network fees on the involved chains. Displayed in the UI.
  - See: [fees-and-dust.md](fees-and-dust.md)

- Dust (UTXO Dust)
  - Small leftover balances in Ergo boxes (e.g., underutilized event boxes). Consolidated periodically to keep UTXO hygiene.
  - See: [fees-and-dust.md](fees-and-dust.md)

- Finality / Confirmations
  - Minimum number of blocks required before events are considered safe. Watchers wait for source-chain confirmations; Guards may require more before signing.
  - See: [security-model.md](security-model.md)

- Multisig / Threshold Signatures
  - Cryptographic schemes requiring m-of-n signatures (or equivalent threshold) to authorize a spend. Used by Guards on external chains.
  - See: [multisig.md](multisig.md), [threshold.md](threshold.md)

- Hot / Cold Wallets
  - Operational separation for security. Cold storage for bulk funds, hot wallets for day-to-day event settlements. Large transfers can involve cold ➜ hot moves.

- Spend Proof (Monero PoC)
  - A Monero wallet proof binding a transaction to a message (Rosen metadata). Used to prove lock intent without embedding metadata in tx_extra.
  - See: [bringing-monero.md](bringing-monero.md)

For user help and diagnostics, see the [troubleshooting guide](rosen-troubleshooting.md) and [rosen-faq.md](rosen-faq.md).
