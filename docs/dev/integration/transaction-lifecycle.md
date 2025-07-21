# Transaction Lifecycle

A typical Ergo payment moves through four well‑defined stages. Follow them in order to keep code, wallets, and monitoring tools predictable.

1. **Address creation** – pick or derive addresses for deposits and change
2. **Unsigned composition** – gather inputs, craft outputs, and set the fee
3. **Signature** – sign with the node wallet or an offline keystore
4. **Broadcast & confirmation tracking** – publish the JSON and watch the mempool

Each section links to demo code, REST calls, and common hazards.

---

## 1  Address Creation

Ergo follows BIP‑32/BIP‑44. One seed drives two deterministic chains:

| Chain | Purpose                           |
| ----- | --------------------------------- |
| **0** | external – deposits and invoices  |
| **1** | internal – change and dust sweeps |

> **Best practice** Fix **chain = 1, index = 0** as the change address. The node sends every remainder there and cleans up dust.

### 1.1 Programmatic derivation (preferred)

| Language       | Library                   | Quick link                                                                                                                         |
| -------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Java / Kotlin  | **ergo‑appkit**           | [`AddressGenerationDemo.java`](https://gist.github.com/kushti/70dcfa841dfb504721f09c911b0fc53d)                                    |
| Java utilities | **ergo‑simple‑addresses** | [https://github.com/kushti/ergo-simple-addresses](https://github.com/kushti/ergo-simple-addresses)                                 |
| Java backend   | **ergo‑wallet**           | [https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet](https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet) |
| Rust / WASM    | **sigma‑rust**            | [`tx_builder.rs`](https://git.io/JkzEt)                                                                                            |
| JS / TS        | **ergo‑lib‑wasm**         | [`test_transaction.js`](https://git.io/JkzEj)                                                                                      |
| Go             | **ergo‑lib‑go**           | [https://github.com/sigmaspace-io/ergo-lib-go](https://github.com/sigmaspace-io/ergo-lib-go)                                       |
| Go (early)     | **ergo‑golang**           | [https://github.com/azhiganov/ergo-golang](https://github.com/azhiganov/ergo-golang)                                               |

A withdrawal must target **P2PK**. Other types break audit logic and UX.

**Path template**

```
m / 44' / 429' / account' / chain / index
```

### 1.2 Node wallet derivation

```bash
curl "http://localhost:9053/wallet/deriveNextKey" \
  -H "accept: application/json" \
  -H "api_key: hello"
```

```json
{
  "derivationPath": "m/44'/429'/0'/0/1",
  "address": "9gF9QP33MoPc8uekF95VHdosL4KzgSz7Ec7MLEtuhx4uPAd3eZs"
}
```

---

## 2  Unsigned Composition

A raw transaction selects inputs, defines outputs, and declares a fee. No cryptographic proof appears yet.

### 2.1 Input selection (UTXO lookup)

* Explorer: `GET /transactions/boxes/byAddress/unspent`
* Local node: `GET /wallet/boxes/unspent`

### 2.2 Binary bytes for each box

```bash
curl http://localhost:9053/utxo/byIdBinary/{boxId}
```

Use the resulting `bytes` in `inputsRaw`.

### 2.3 Mempool exclusion

Keep double‑spends out by checking the mempool:

```http
GET /transactions/unconfirmed/byErgoTree/{ergoTree}
```

or download the whole list:

```http
GET /transactions/unconfirmed
```

### 2.4 Batch withdrawals

One transaction may pay many users:

1. Collect pending payouts.
2. Create one output per user.
3. Send the remainder to the change address.

### 2.5 Fee rule

| Context          | Suggested fee             |
| ---------------- | ------------------------- |
| Standard wallet  | **0.001 ERG per box**     |
| Many tiny inputs | raise above the guideline |

---

## 3  Signature

### 3.1 One‑call node workflow

```http
POST /wallet/payment/send
```

Parameters

| Field       | Role                       |
| ----------- | -------------------------- |
| `requests`  | target outputs             |
| `fee`       | optional manual fee        |
| `inputsRaw` | optional manual input list |

The node picks inputs, signs, and broadcasts.

### 3.2 Offline workflow

1. Build the unsigned JSON with a library.
2. Copy the file to an air‑gapped host.
3. Sign with the master or account key.
4. Bring the signed JSON back.
5. Broadcast through any node or explorer.

---

## 4  Broadcast & Confirmation Tracking

### 4.1 Broadcast

If you're using **Java (ergo‑appkit)**, serialize the signed transaction like this:

```java
Json json = JsonCodecsWrapper.ergoLikeTransactionEncoder().apply(tx);
System.out.println(json.toString());
```

* **Public explorer**

  ```bash
  curl -X POST https://api.ergoplatform.com/api/v0/transactions/send \
       -H "Content-Type: application/json" \
       -d '{ ...signedTxJson... }'
  ```

* **Local node**

  ```bash
  curl -X POST http://localhost:9053/transactions \
       -H "Content-Type: application/json" \
       -d '{ ... }'
  ```

### 4.2 Monitor

* Explorer: `GET /transactions/{txId}` → `numConfirmations`
* Node: `GET /transactions/unconfirmed/{txId}` returns 404 after confirmation

A deposit becomes safe after **10 blocks (\~20 min)**.

---

## 5  Troubleshooting

| Error                                                | Cause                           | Fix                                                               |
| ---------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------- |
| `Server was not able to produce a timely response …` | Wallet needs hundreds of inputs | Set `profile="exchange"`, bump `maxInputs` to 300, and sweep dust |
| `MaxInputsExceededError(…100)`                       | `maxInputs` at default 100      | Raise to 300 and restart                                          |
| `Estimated execution cost … exceeds the limit`       | Too many tiny inputs            | Split the payout or sweep dust                                    |
| `invalid length XXX of Hex data`                     | Malformed `inputsRaw`           | Provide even‑length raw hex                                       |
| `NotEnoughErgsError`                                 | `value + fee` exceeds inputs    | Add inputs or reduce outputs                                      |
| Broadcast ok but no confirmation                     | Fee too low or node unsynced    | Check `/info`, raise fee, rebroadcast                             |

---

## 6  FAQ

| Question                              | Answer                                                                           |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| `value` vs `assets`                   | `value` counts ERG. `assets` holds `{tokenId, amount}` pairs.                    |
| `creationHeight` vs `inclusionHeight` | `creationHeight` comes from the sender. `inclusionHeight` marks the mined block. |
| First confirmation block?             | Call `/blocks/{blockId}/header` and read `height`.                               |
| Balance endpoint that sees mempool?   | `/wallet/balances/withUnconfirmed`                                               |
| Minimum fee?                          | 0.001 ERG per box                                                                |
| Safe confirmations?                   | 10 blocks                                                                        |
| `boxId` formula?                      | SHA‑256 of serialized box bytes                                                  |
| Withdraw to non‑P2PK?                 | Avoid in production                                                              |
| Box expiry?                           | Yes, after four years. See `rent.md`.                                            |
| Extra ports?                          | None. Wallet shares 9053.                                                        |
| Whitelist my node IP?                 | Not required                                                                     |

---

Return to the [Node & Wallet Configuration](guide.md) page and confirm the infrastructure settings.
