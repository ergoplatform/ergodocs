# RosenBridge Fees & Dust Collection

RosenBridge applies fees and performs periodic dust cleanup on Ergo to keep the system efficient and sustainable. This page explains how fees are handled and how “dust” (residual balances) is consolidated.

See also: [Token Transfer Flows](token-transfer-flows.md), background: [Dust Collection](dust-collection.md)

## Fees on Ergo

- Fee Scope
  - Bridge operations incur processing fees on the Ergo side to fund maintenance and operations.
  - Fees are automatically deducted during the transaction flow on Ergo, consistent with network policies.
- Visibility
  - Fees are shown in the Rosen UI prior to confirmation.
  - Network fees can vary with chain conditions and bridge configuration.

## Dust Collection

Certain bridge operations on Ergo produce underutilized “event boxes” or small residual balances (dust). Over time, these can accumulate. RosenBridge periodically consolidates dust to keep the chain usage clean and economical.

- Periodic Review
  - A dust collector function scans for underutilized event boxes and small residual balances.
- Consolidation
  - Identified boxes are spent and consolidated to reduce chain clutter and improve UTXO hygiene.
- Scope
  - Dust collection covers event boxes and other residuals that may occur through normal bridge operations.
- Benefits
  - Fewer tiny fragments, improved performance, and lower long-term maintenance cost.

## Operational Notes

- Security First
  - Dust collection follows the same security posture as core bridge actions—only safe consolidations are performed.
- Transparency
  - Actions are visible on Ergo and auditable like other bridge operations.
- Configuration
  - Intervals and thresholds may be tuned as operations evolve.

For a practical walkthrough of when fees appear in the flow, see:
- [Token Transfer Flows](token-transfer-flows.md)
