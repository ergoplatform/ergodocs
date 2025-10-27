# RosenBridge Security Model

This page summarizes RosenBridge’s security goals, trust assumptions, and mitigations against common attack scenarios. Rosen is Ergo‑centric: consensus, auditability, and final decisions happen on Ergo. External chains only require a Guard‑controlled multisig/threshold wallet.

See also: [concepts-assumptions.md](concepts-assumptions.md), [token-transfer-flows.md](token-transfer-flows.md), [rosen-guard.md](rosen-guard.md), [watcher.md](watcher.md), [rosen-tokenomics.md](rosen-tokenomics.md)

## Security Goals

- Integrity: Bridged assets on Ergo (rTokens) always correspond to locked assets on source chains; burns correspond to releases on the target chain.
- Availability/Liveness: Events observed on source chains eventually finalize on Ergo and vice‑versa under normal network conditions.
- Auditability: The lifecycle of each bridge event is observable and verifiable on Ergo (event boxes, approved events, Guard signatures).
- Least Trust: Minimize assumptions about external chains and avoid deploying foreign‑chain smart contracts when a Guard multisig/threshold wallet suffices.

## Trust Model and Roles

- Guards (Federated Signers)
  - Hold shares/keys for m‑of‑n multisig or threshold signatures on external chains.
  - Independently validate approved events before signing.
  - Federated by design: no single Guard can move funds.
- Watchers (Open Participation)
  - Keyless observers that monitor chains, verify, and propose events.
  - Reach on‑Ergo consensus via event boxes and approved event boxes.
  - Incentivized by fees/emissions, penalized for fraud via slashing mechanisms (see [rosen-tokenomics.md](rosen-tokenomics.md)).

Background reading: [multisig.md](multisig.md), [threshold.md](threshold.md)

## Finality, Confirmations, and Consensus

- Source chain finality
  - Watchers wait for conservative confirmation counts before proposing an event.
- Watcher consensus on Ergo
  - Multiple watcher “event boxes” converge to an “approved event box” after agreement.
- Guard validation and signing
  - Guards re‑validate events and only sign once thresholds and integrity checks are satisfied.
- Target chain finality
  - Guards monitor mined transactions for final confirmation thresholds before considering events closed.

This pipeline prioritizes security and avoids reorgs, double spends, and race conditions at the cost of some latency.

## Threat Scenarios and Mitigations

- Malicious/Erroneous Watchers
  - Threat: Fabricated events or spam.
  - Mitigations:
    - Watcher consensus: a single watcher cannot advance state.
    - Guard re‑validation: Guards independently verify each approved event.
    - Economic penalties: Slashing of permits/collateral discourages fraud (see [rosen-tokenomics.md](rosen-tokenomics.md)).

- Guard Collusion or Compromise
  - Threat: A subset of Guards attempts to exfiltrate funds or sign invalid transactions.
  - Mitigations:
    - m‑of‑n/threshold enforcement; attacker must control ≥ m signers.
    - Segregated hot/cold policies and operational controls.
    - Collateral and reputation costs; public auditability.

- Chain Reorgs and Forks
  - Threat: Reorg invalidates an observed deposit/withdrawal.
  - Mitigations:
    - Conservative confirmation thresholds on all chains.
    - Watcher consensus time on Ergo.
    - Guard re‑checks before signing.

- DoS and Permit Exhaustion
  - Threat: Spam events to exhaust watcher permits or Guard resources.
  - Mitigations:
    - Fee structure and minimums reduce low‑value spam.
    - Independent watcher operation and scalable observation layer.
    - Rate‑limit and operational alerting on Guard services.

- Replay / Duplicate Event Claims
  - Threat: Reusing the same claim/proof/metadata to trigger multiple actions.
  - Mitigations:
    - Unique event identifiers and idempotent processing.
    - Commit‑reveal, honeypots, and anti‑replay strategies for watcher incentives.
    - Guard verification of correspondence between source event and Ergo metadata.

- Metadata Tampering
  - Threat: Altering destination parameters (e.g., toAddress).
  - Mitigations:
    - Message/metadata embedded in on‑Ergo event boxes.
    - For chains like Monero PoC, metadata is bound to spend proofs; only the locker can produce valid proofs (see [bringing-monero.md](bringing-monero.md)).

- Key Management and Operational Risks
  - Threat: Signer key loss/theft, node outages, drift between nodes.
  - Mitigations:
    - Multisig/threshold with rotation procedures.
    - Redundant full nodes and health monitoring.
    - Access control, HSMs or secure enclaves where practical.

## Economics and Incentives

- Fees fund operations and align incentives for liveness.
- Event‑based emissions (bootstrap phase) reward honest participation.
- Slashing (loss of RosenEvent/permits/collateral) penalizes dishonest or low‑quality behavior.
- See: [rosen-tokenomics.md](rosen-tokenomics.md), [fees-and-dust.md](fees-and-dust.md)

## Operational Guidance (High‑Level)

- Redundancy: Multiple full nodes per chain, with monitoring and alerting.
- Change Management: Staged rollouts, conservative parameter updates (confirmations, fees).
- Key Policies: Clear procedures for key rotation, cold/hot segregation, and incident response.
- Observability: Track event lifecycles end‑to‑end; use the Rosen events UI and internal telemetry.

## Limitations and Expectations

- Latency: Security‑first confirmation policies mean transfers are not instant.
- External Dependencies: Liveness depends on external node availability and network conditions.
- Federated Model: Rosen is not trustless like a light‑client‑verified 2‑way peg; it is a federated bridge with strong auditability and incentives.

For practical flows and user guidance, start with:
- [token-transfer-flows.md](token-transfer-flows.md)
- [fees-and-dust.md](fees-and-dust.md)
