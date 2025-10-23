# Integrating a New Chain with RosenBridge

RosenBridge can extend to any blockchain that supports multisignature or threshold signature schemes. This page outlines the required components and high-level steps to add a new network.

See also: [Watcher](watcher.md), [Rosen Guards](rosen-guard.md), background: [Multisig](multisig.md), [Threshold Signatures](threshold.md), flows: [Token Transfer Flows](token-transfer-flows.md)

## Components Required

- Watchers
  - Purpose: Monitor the network’s multisignature/threshold wallet for incoming payments and events.
  - Responsibilities: Detect deposits, fetch transaction details and confirmations, create event boxes on Ergo, and participate in Watcher consensus.

- Guardian Wallets
  - New Wallet Setup: Establish a Guard-controlled multisig/threshold wallet on the new chain.
  - Security: Keys/shares are held by Guards; watchers do not hold spend keys.
  - Policy: Follow m-of-n or threshold policy aligned with Rosen security standards.

- Transaction Verification Mechanism (Guards)
  - Guard Verification: Each Guard must be able to independently verify cross-chain events (confirmations, amounts, destination metadata).
  - Signing: Guards sign chain-specific transactions (target chain or Ergo) only after verification and Watcher consensus.

- Bank Boxes on Ergo
  - Infrastructure: Configure required Bank boxes on Ergo to support inbound/outbound flows for assets related to the new chain.
  - Flows: Ensure mint/burn paths are correctly wired in accordance with [Token Transfer Flows](token-transfer-flows.md).

## High-Level Onboarding Steps

1) Prepare Guard Wallets
- Generate/import keys for a multisig/threshold wallet on the new chain.
- Define m-of-n parameters and operational runbooks (key backups, rotation).

2) Implement/Configure Watchers
- Extend existing Watcher to support the new chain’s RPC/explorer interfaces.
- Implement chain-specific parsing (addresses, tx formats), event detection, and confirmation logic.
- Ensure Watcher produces correct event boxes with required metadata.

3) Define Verification Rules
- Specify Guard-side validation: required confirmations, fee policies, minimum amounts, metadata fields.
- Implement chain-specific transaction builders and signature collection for Guards.

4) Set Up Ergo Bank Boxes
- Create/configure Bank boxes for new chain assets on Ergo.
- Verify mint/burn paths and asset maps for representative tokens (rTokens).

5) Test End-to-End
- Dry-run: Lock on the new chain ➜ event boxes ➜ Guard verification ➜ mint rTokens on Ergo.
- Reverse: Burn rTokens on Ergo ➜ event boxes ➜ Guard verification ➜ unlock on the new chain.
- Measure latency and ensure confirmation thresholds and fee policies are correct.

6) Operationalize
- Document operational procedures (failover, incident response, monitoring).
- Add metrics/alerts for Watchers and Guards across both chains.
- Periodically review thresholds, fees, and dust policies.

## Notes and Best Practices

- Ergo-Centric Consensus
  - Keep core consensus and audit trails on Ergo.
  - Avoid external chain smart contracts unless strictly necessary.

- Confirmation Policies
  - Choose conservative confirmation thresholds on both chains to avoid forks and reorgs.

- Security Separation
  - Watchers are open participation and keyless.
  - Guards are permissioned and hold signing authority under strict policy.

- Iterative Rollout
  - Start with lower-value caps, increase after observing production stability.

For background on roles and assumptions, see:
- [Concepts & Assumptions](concepts-assumptions.md)
- [Rosen Guards](rosen-guard.md)
- [Watcher](watcher.md)
