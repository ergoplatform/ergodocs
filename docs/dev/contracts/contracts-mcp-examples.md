---
title: MCP Examples — Contracts Library
---

# MCP Examples — Contracts Library

## Overview

This page sketches how contract patterns can be exposed and composed via ErgoScript MCP. It maps patterns to MCP-style builders/helpers and defines inputs/outputs for each.

## Conventions

- Builders return either:
  - a transaction template ready for signing, or
  - a guard/predicate object used by a higher-level builder
- Inputs are plain types (tokenId, addresses, proofs, bytes), outputs are templates or booleans for guards
- Code snippets/stubs here are illustrative; contribute real examples as MCP components evolve

## Tokens

- Perpetual Token → Builder: enforceConservation
  - Inputs: tokenId, outputs schema
  - Output: tx template that preserves total token supply across inputs/outputs
- Whitelist-only Token → Builder: whitelistTransfer
  - Inputs: tokenId, recipient, whitelistRoot, membershipProof
  - Output: tx template enforcing recipient membership at spend time

## Access Control

- Daily Withdrawal Limit → Builder: rateLimitedWithdrawal
  - Inputs: requestedAmount, limitPerWindow, windowMetric (height/time), currentState
  - Output: tx template updating accumulator/window; rejects if over limit

## Privacy

- Stealth Address → Helpers: deriveOneTimeAddress, scanForStealthOutputs
  - Inputs: recipient params, sender randomness (derive); stealth keys/indexer results (scan)
  - Output: derived address/ErgoTree; list of spendable stealth outputs

## Oracles

- Trustless Hashrate Oracle → Builders: submitReport, aggregateWindow, readLatest
  - Inputs: window params, reporter data, commitments/reveals
  - Output: submission/aggregation tx; or read guard for latest value accessor

## Proofs

- Bulletproof Range Proof → Guard: verifyRangeProof
  - Inputs: commitment(s), proof bytes, bounds
  - Output: boolean/guard used within a composition
- Schnorr Verification → Guard: verifySchnorr
  - Inputs: public key(s), message/context digest, proof bytes
  - Output: boolean/guard used within a composition

## Interoperability

- Trustless Peg → Builders: verifyProof, mintOrRelease
  - Inputs: proof bytes, asset mapping, current state
  - Output: tx updating peg state for deposit/withdrawal
- Bitcoin Relay → Builders: updateHeaders, verifyInclusion
  - Inputs: header batch, txid, Merkle path, confirmation threshold
  - Output: relay update tx; boolean/guard for inclusion verification
- Import Off-chain Bank → Builders: importBatch, reconcileCorrection
  - Inputs: batch id, statement hash/data, attestation; correction entries
  - Output: state update or correction tx with audit trail

## Randomness

- Randomness from ErgoRaffle → Builders: commit, reveal, selectWinner
  - Inputs: participant salt, reveal payload, block data reference
  - Output: commit/reveal tx; winner-selection tx using derived seed

## Composition Examples (stubs)

- Confidential, Whitelisted Transfer
  - verifyRangeProof(...) AND whitelistTransfer(...)
- Rate-Limited DAO Treasury
  - multisigGuard(...) AND rateLimitedWithdrawal(...)
- Pegged Asset Redemption with BTC Proof
  - verifyInclusion(...) THEN mintOrRelease(...)

## See also

- [Library index](contracts-library.md)
- Off-chain & UI References: [contracts-offchain-references.md](contracts-offchain-references.md)

## Contributing MCP Examples

- Add concrete examples for any builder/guard above
- Include repo links, minimal code snippets, and expected IO
- Keep snippets short; link to full source for details
