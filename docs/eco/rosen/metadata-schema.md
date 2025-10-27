# RosenBridge Metadata Schema

This page outlines a canonical, human‑readable schema for intent metadata used by Rosen flows. The Rosen dApp/tooling constructs and validates metadata; this document helps integrators and power users understand typical fields and structure.

Notes:
- Exact fields and encoding may evolve; rely on the Rosen UI/tooling for production transactions.
- Metadata is recorded or bound to on‑Ergo event boxes and validated by Guards during verification.
- For special chains like Monero (no reliable tx metadata), the metadata is bound to a spend proof message; see [bringing-monero.md](bringing-monero.md).

## Common Concepts

- Direction:
  - ChainX ➜ Ergo: Lock native asset on source chain, mint rToken on Ergo.
  - Ergo ➜ ChainX: Burn rToken on Ergo (via Bank), release native asset on target chain.
- Address formats:
  - toAddress uses the target chain’s native format (Ergo P2PK, EVM/Bech32/addr1… per chain, etc.).
- Fees:
  - bridgeFee is the Rosen fee component.
  - networkFee covers chain‑level fees (e.g., miner/gas fees) where applicable.

## ChainX ➜ Ergo (Lock → Mint)

Purpose:
- Convey the user’s target Ergo address and fee parameters for minting the representative rToken on Ergo.

Illustrative example:
```json
{
  "to": "ergo",
  "toAddress": "9hJTi4GHb9cbLovbxJsAJ9TtU42CDnuWJ8w8Q4CfA3kpExRrAFw",
  "asset": "BTC",
  "amount": "100000",            // minor units if applicable
  "bridgeFee": "12212682",
  "networkFee": "190000",
  "memo": "optional user note",
  "nonce": "optional-unique-tag"
}
```

Field notes:
- to: constant indicating the target platform (“ergo”).
- toAddress: Ergo destination for the minted rTokens.
- asset/amount: asset identifier/symbol and quantity (format depends on source chain conventions).
- bridgeFee/networkFee: values shown in the Rosen UI at submit time.
- memo/nonce: optional, may be ignored by validators.

## Ergo ➜ ChainX (Burn → Release)

Purpose:
- Convey the user's target ChainX address and fee parameters for releasing the native asset on ChainX after burning the rToken on Ergo.

Illustrative example:
```json
{
  "to": "chainx",                     // e.g., "bitcoin", "cardano", "ethereum", "bsc"
  "toAddress": "bc1q.... or 0x.... or addr1....",
  "asset": "rBTC",                    // burned representative token on Ergo
  "amount": "100000",
  "bridgeFee": "12212682",
  "networkFee": "190000",
  "memo": "optional user note",
  "nonce": "optional-unique-tag"
}
```

Field notes:
- to: specifies the external target (e.g., “bitcoin”, “cardano”, “ethereum”, “bsc”).
- toAddress: destination on the target chain (format must match chain).
- asset: the rToken on Ergo corresponding to the native asset on ChainX.

## Monero: Metadata Bound to Spend Proof

Monero wallets do not reliably carry arbitrary tx metadata. For ChainX ➜ Ergo with XMR:
- Users generate a spend proof with the metadata JSON as the message.
- The proof and the plaintext JSON are published/recorded on Ergo (by the user or Rosen tooling).
- Only the locker can create a valid proof for the exact message, protecting integrity.

Reference example (from [bringing-monero.md](bringing-monero.md)):
```json
{
  "to": "ergo",
  "bridgeFee": "12212682",
  "networkFee": "190000",
  "toAddress": "9hJTi4GHb9cbLovbxJsAJ9TtU42CDnuWJ8w8Q4CfA3kpExRrAFw",
  "fromAddress": ["monero_pub_spend_key"]
}
```

## Encoding & Validation

- Encoding:
  - JSON string carried by the chain’s available metadata channel, or bound via proofs (e.g., Monero).
  - On Ergo (Bank/event boxes), metadata fields are carried/linked on‑chain in a canonical format used by Rosen watchers/guards.
- Validation:
  - Watchers/guards validate that metadata and observed source events match (amount, asset, destination, fees).
  - Guard signing occurs only after watcher consensus and independent verification.

## Best Practices

- Construct metadata via the Rosen dApp/tooling to ensure correctness.
- Use canonical formats for addresses and asset identifiers.
- Avoid manual edits; mismatched fields can delay or invalidate events.
- For EVM targets, verify token contracts via the official assets list before interacting:
  - https://app.rosen.tech/assets

## See Also

- Flow details: [token-transfer-flows.md](token-transfer-flows.md)
- Monero binding and verification: [bringing-monero.md](bringing-monero.md)
- Fees and dust handling: [fees-and-dust.md](fees-and-dust.md)
- Events lifecycle: [events-and-status.md](events-and-status.md)
