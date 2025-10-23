# Bringing Monero to RosenBridge

Monero’s privacy features make it a special case for cross-chain bridges. Transactions reveal neither sender nor amount, and common wallets avoid arbitrary metadata. Rosen still needs a shared vault that Guards can control and verifiable user intent that Watchers can observe. This proof-of-concept outlines how to achieve both without compromising Monero’s privacy model.

Status: Proof of Concept. Operational guidance below is for engineering evaluation; harden before production.

See also: [Concepts & Assumptions](concepts-assumptions.md), [Token Transfer Flows](token-transfer-flows.md), [Rosen Guards](rosen-guard.md), [Watcher](watcher.md)

## TL;DR

- Guards manage a shared Monero vault via multisig and wallet RPC.
- Users prove lock intent by attaching Rosen metadata to a Monero spend proof and publishing the proof on Ergo (directly or via Rosen tooling).
- Watchers and Guards verify the proof automatically; no custom wallet builds required.
- To go live, invest in reliable full nodes, wrap scripts into services, and streamline the user proof flow.

## Why Monero Is Tricky to Bridge

- Stealth outputs and ring signatures hide which outputs are spendable. Only wallets that share multisig state can view deposits.
- RingCT masks amounts, so bridges must trust wallet RPC balance reports instead of public explorer data.
- No reliable metadata channel: wallets ignore arbitrary tx_extra, removing the usual “lock data in transaction” approach.

## Architecture at a Glance

1. Guards bootstrap a shared Monero multisig wallet (e.g., 2-of-4) via wallet RPC.
2. Users lock XMR into that shared address.
3. Users generate a spend proof (check_tx_proof) with Rosen metadata in the message field.
4. Users publish the proof plus plaintext metadata on Ergo—or submit to Rosen tooling that posts it on their behalf.
5. Watchers verify the proof, pair it with the Monero deposit, and pass the event to the Guard service for finalization.

## Building the Shared Vault (Multisig)

Monero multisig setup is interactive. Enable experimental multisig once per wallet and iterate exchanges until “ready”.

```python
import json
import requests
from requests.auth import HTTPDigestAuth

RPC_URL = "http://localhost:18083/json_rpc"
auth = HTTPDigestAuth("testuser", "testpass")
wallets = [
    {"filename": "multi181", "password": "pass1"},
    {"filename": "multi182", "password": "pass2"},
    {"filename": "multi183", "password": "pass3"},
    {"filename": "multi184", "password": "pass4"},
]

def call(method, params=None):
    payload = {"jsonrpc": "2.0", "id": "0", "method": method, "params": params or {}}
    res = requests.post(
        RPC_URL,
        auth=auth,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
    ).json()
    if "error" in res:
        raise RuntimeError(res["error"])
    return res["result"]

prepared = []
for wallet in wallets:
    call("open_wallet", wallet)
    prepared.append(call("prepare_multisig"))

round_infos = []
for idx, wallet in enumerate(wallets):
    peers = [info for j, info in enumerate(prepared) if j != idx]
    call("open_wallet", wallet)
    round_infos.append(
        call("make_multisig", {"multisig_info": peers, "threshold": 2, "password": wallet["password"]})
    )

for _ in range(8):
    if all(call("is_multisig")["ready"] for _ in wallets):
        break
    updated = []
    for wallet in wallets:
        call("open_wallet", wallet)
        updated.append(
            call("exchange_multisig_keys", {"password": wallet["password"], "multisig_info": round_infos})
        )
    round_infos = [info for info in updated if info]

addresses = []
for wallet in wallets:
    call("open_wallet", wallet)
    addresses.append(call("get_address")["address"])
assert len(set(addresses)) == 1
print(f"Shared multisig address: {addresses[0]}")
```

To rediscover the address later:

```python
call("open_wallet", {"filename": "multi181", "password": "pass1"})
print(call("get_address")["address"])
```

Tracking balances and incoming transfers:

```python
status = call("get_balance", {"account_index": 0})
print(f"Total balance: {status['balance'] * 1e-12:.6f} XMR")
print(f"Unlocked balance: {status['unlocked_balance'] * 1e-12:.6f} XMR")

incoming = call("get_transfers", {"in": True, "pending": True, "account_index": 0})
for payment in incoming.get("in", []):
    print(payment["txid"], payment["amount"] * 1e-12)
```

### What Exactly Is a “Private View Key”?

- Spend key: authorizes transfers.
- View key: reveals which incoming outputs belong to the wallet.
- Sharing the private view key grants read-only visibility (deposits/amounts) without spend authority—useful for Watchers’ observation.

Giving Watchers read-only access:

```python
view_key = call("query_key", {"key_type": "view_key"})["key"]
print(f"Share this read-only view key with watchers: {view_key}")
```

Watchers can run monero-wallet-rpc with a view-only wallet to monitor deposits in near real time. Guards keep exclusive control of spend keys.

## Spending from the Vault

Approve payouts with a draft transfer, collect signatures, then submit.

```python
import json
import requests
from requests.auth import HTTPDigestAuth

RPC_URL = "http://localhost:18083/json_rpc"
auth = HTTPDigestAuth("testuser", "testpass")
wallets = [
    {"filename": "multi181", "password": "pass1"},
    {"filename": "multi182", "password": "pass2"},
]

def call(method, params=None):
    payload = {"jsonrpc": "2.0", "id": "0", "method": method, "params": params or {}}
    res = requests.post(
        RPC_URL,
        auth=auth,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
    ).json()
    if "error" in res:
        raise RuntimeError(res["error"])
    return res["result"]

for wallet in wallets:
    call("open_wallet", wallet)
    exported = call("export_multisig_info")
    call("import_multisig_info", {"info": [exported]})

creator = wallets[0]
call("open_wallet", creator)
call("set_daemon", {"address": "http://127.0.0.1:18081", "trusted": True})
transfer = call(
    "transfer",
    {
        "destinations": [{"address": "44AFFq5kSiGBoZ...", "amount": int(0.001 * 1e12)}],
        "account_index": 0,
        "do_not_relay": True,
        "priority": 1,
        "ring_size": 16,
    },
)
multisig_txset = transfer.get("multisig_txset") or transfer.get("tx_data_hex")

co_signer = wallets[1]
call("open_wallet", co_signer)
signed = call("sign_multisig", {"tx_data_hex": multisig_txset})
final_data = signed.get("tx_data_hex", multisig_txset)
result = call("submit_multisig", {"tx_data_hex": final_data})
print(f"Broadcasted hashes: {result.get('tx_hash_list', [])}")
```

Guardrails:
- Sync multisig info before building: export_multisig_info/import_multisig_info.
- Use do_not_relay on drafts until enough signatures are collected.
- Production services should orchestrate signer order, retries, and fee policy.

## Asking Users to Prove Their Lock

In the Monero GUI wallet:
1. Open the Prove/check tab.
2. Paste the lock transaction ID and the Rosen multisig address.
3. Enter the Rosen metadata JSON in the Message field.

Example metadata:

```json
{
  "to": "ergo",
  "bridgeFee": "12212682",
  "networkFee": "190000",
  "toAddress": "9hJTi4GHb9cbLovbxJsAJ9TtU42CDnuWJ8w8Q4CfA3kpExRrAFw",
  "fromAddress": ["monero_pub_spend_key"]
}
```

The wallet outputs a base58 proof string. Users then publish both the proof and plaintext JSON on Ergo (via a helper app or form). Because only the locker could have created the proof, Rosen can accept the proof directly and post it to Ergo on the user’s behalf without sacrificing integrity.

## Verifying Proofs Automatically

```python
import argparse
import json
import requests
from requests.auth import HTTPDigestAuth

def call(url, auth, method, params=None):
    payload = {"jsonrpc": "2.0", "id": "0", "method": method, "params": params or {}}
    res = requests.post(url, auth=auth, headers={"Content-Type": "application/json"}, data=json.dumps(payload)).json()
    if "error" in res:
        raise RuntimeError(res["error"])
    return res["result"]

def verify(url, auth, tx_id, address, message, proof):
    return call(
        url,
        auth,
        "check_tx_proof",
        {"txid": tx_id, "address": address, "message": message, "signature": proof},
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rpc-url", default="http://localhost:18083/json_rpc")
    parser.add_argument("--rpc-user", default="testuser")
    parser.add_argument("--rpc-pass", default="testpass")
    parser.add_argument("--wallet", default="multi181")
    parser.add_argument("--wallet-password", default="pass1")
    parser.add_argument("--txid", required=True)
    parser.add_argument("--address", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--proof", required=True)
    args = parser.parse_args()

    auth = HTTPDigestAuth(args.rpc_user, args.rpc_pass)
    call(args.rpc_url, auth, "open_wallet", {"filename": args.wallet, "password": args.wallet_password})
    print(json.dumps(verify(args.rpc_url, auth, args.txid, args.address, args.message, args.proof), indent=2))

if __name__ == "__main__":
    main()
```

A response with `good: true` confirms the proof matches the transaction and message. Guards enforce a confirmation threshold before treating the event as final.

## Why This Holds Up

- Soundness: Only the owner of the output can generate a valid proof for the exact message, preventing metadata tampering.
- Completeness: Any Monero wallet with spend proofs can produce one—no custom tooling required.
- Operations: Guards need redundant monerod and wallet RPC nodes, automated multisig syncing, and alerting for height drift.

## Path to Production

- Harden automation (error handling, resumable workflows, secret storage) and wrap inside Guard services.
- Define a canonical metadata schema and add Ergo endpoints for proof submission.
- Build a user helper (CLI or lightweight desktop) that generates the proof and submits the Ergo payload automatically.
- Implement a Monero scanner that watches wallet RPC for new deposits and correlates them with submitted proofs.

## What Would Make This Even Better

- A Monero dApp connector for seamless wallet integrations (extension or desktop bridge).
- Streamlined proof UX via a URI scheme or helper that pre-fills metadata to reduce errors.
- Automated Ergo submission service that posts the proof and metadata on the user’s behalf.

## Closing Thoughts

RosenBridge can embrace Monero without compromising privacy. Guards retain custody through familiar multisig flows, users keep privacy, and Watchers get verifiable intent data. The primary work ahead is polishing UX and running reliable infrastructure—not inventing new cryptography.
