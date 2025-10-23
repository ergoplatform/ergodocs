# Benefits of RosenBridge

RosenBridge is designed for secure, efficient, and scalable cross-chain transfers centered on Ergo. This page summarizes the core advantages for users, integrators, and ecosystem builders.

See also: [Concepts & Assumptions](concepts-assumptions.md), [Token Transfer Flows](token-transfer-flows.md)

## Universal Compatibility

- Versatile bridge: Connects Ergo with any blockchain that supports multisignature or threshold signatures.
- Expanding coverage: Initially focused on Cardano, Ergo, and Ethereum/EVMs, with additional chains onboarded via the standard integration path.

## Cost Efficiency

- Ergo-centric consensus: By conducting consensus and most logic on Ergo, Rosen minimizes operational complexity and reduces costs across chains.
- Predictable operations: Fees are displayed up-front, and the system favors conservative confirmations for security.

## Enhanced Security

- Federated signing: Guards use m-of-n or threshold signing on target chains to minimize single points of failure.
- Cold storage options: Bridge funds can be managed with multisig cold storage policies on connected chains.
- Independent verification: Guards validate approved events before signing, protecting against watcher malfunctions.

## Integration Simplicity

- Minimal assumptions: External chains only need multisig/threshold support—no custom smart contracts required.
- Streamlined onboarding: Adding a chain involves Guard wallets, Watchers, verification rules, and Bank boxes on Ergo.

## Transparency and Auditability

- Ergo-first audit trail: Bridge actions are recorded and auditable on Ergo, reducing cross-chain complexity.
- Open architecture: Most operational logic is visible to the public, improving accountability.

## Scalability

- Role separation: Watchers propose and report; Guards verify and sign. This separation enables parallel observation without burdening Guard computation.
- DoS resistance: Many Watchers can participate independently, increasing liveness and network resilience.

For next steps and implementation details, see:
- [New Chain Integration](new-chain-integration.md)
- [Fees & Dust](fees-and-dust.md)
