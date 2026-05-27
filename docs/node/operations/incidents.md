---
tags:
  - Deploy
  - Operations
  - Incidents
  - Troubleshooting
owner: docs
last_reviewed: 2026-05-27
---

# Incident Runbooks

## Node Not Syncing

- Check `/info` and `/peers/syncInfo`.
- Check connected peers.
- Check system clock.
- Check disk free.
- Review logs for repeated modifier or database errors.
- Confirm P2P port and `declaredAddress` only if inbound reachability matters.

## Indexed API Lag

- Compare node height with `/blockchain/indexedHeight`.
- Confirm `ergo.node.extraIndex = true`.
- Check disk I/O and DB/log growth.
- Reduce public query load or add proxy limits.

## API Auth Fails

- Confirm plain API key sent in `api_key` header.
- Confirm `apiKeyHash` is Blake2b256 hash of that exact key.
- Restart node after config changes.
- Avoid browser cache confusion by testing with `curl`.

## Disk Full

- Stop write-heavy services.
- Preserve wallet/config/secrets first.
- Free logs or move data volume.
- Restart and check node/index consistency.
- Do not delete database directories blindly.

## Rosen Watcher Stuck

- Confirm target-chain source reachable.
- Confirm Ergo source reachable.
- Confirm initial height was recent and correct.
- Check PostgreSQL container.
- If initial height must change after first scan, expect volume reset/rescan work.

## Guard Manual Signing Left Enabled

- Set `isManualTxRequestActive: false`.
- Set `isArbitraryOrderRequestActive: false`.
- Restart guard.
- Review submitted requests before returning service to normal operation.

