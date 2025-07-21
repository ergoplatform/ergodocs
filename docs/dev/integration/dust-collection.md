# Dust Collection

*Back to the main [Integration Guide](guide.md)*

A **dust set** is a large group of ERG outputs worth tiny amounts. A node signs a transaction by loading every input box from disk. When the wallet owns thousands of dust boxes the process slows down. The node may hit limits or time out. Exchange and mining‑pool wallets reach that state first.


## Automatic Collection in the Node

Turn the wallet into “self‑cleaning” mode before dust appears. The node merges dust during every withdrawal when the wallet owns enough surplus inputs.

Add the block below to your **ergo.conf**. Full syntax is in [conf‑wallet.md](conf-wallet.md).

```hocon
ergo {
  wallet {
    # larger Bloom filters and caches
    profile        = "exchange"       

    # hard cap per transaction (default 50)
    maxInputs      = 300

    # extra sweep when withdrawal needs <100 inputs             
    optimalInputs  = 100

    # ignore deposits ≤ 0.001 ERG              
    dustLimit      = 1000000

    # burn every token that is not on this list
    tokensWhitelist = [         
      
      # SigUSD      
      "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
      # SigRSV 
      "003bd19d0187117f130b62e1bcab0939929ff5c7709f843c5c4dd158949285d0"  
    ]
  }
}
```

| Key               | Value / Unit | Purpose                                                         |
| ----------------- | ------------ | --------------------------------------------------------------- |
| `profile`         | `"exchange"` | Bloom filters and caches suit high‑load wallets.                |
| `maxInputs`       | `300`        | Raises the hard cap for inputs in one transaction.              |
| `optimalInputs`   | `100`        | A sweep runs whenever a withdrawal uses fewer than this number. |
| `dustLimit`       | `1000000`    | The wallet ignores payments at or below 0.001 ERG.              |
| `tokensWhitelist` | list of IDs  | The wallet keeps the listed tokens and burns every other asset. |

Restart the node after saving the file. The wallet merges dust in the background from the first block it scans.

### Fast clean‑up for an existing dusty wallet

1. Send **0.001 ERG** from the wallet to its own change address.
2. Wait **60 seconds** for confirmation.
3. Repeat until the UTXO count drops below **500**.

Each self‑payment pulls about `optimalInputs` dust boxes into one output, so the backlog shrinks quickly.



## Manual Collection (fallback)

Choose this path when every automatic sweep fails because the node exhausts limits before it can pay the fee.

| Step  | Call                                              | Result / Note                                         |
| ----- | ------------------------------------------------- | ----------------------------------------------------- |
|  1    | `GET /wallet/boxes/unspent?limit=100`             | Record every `boxId`.                                 |
|  2    | `GET /utxo/byIdBinary/{boxId}` for each id        | Record the `bytes` field. Plain even‑length hex only. |
|  3    | Sum every `value`                                 | Keep at least 1 000 000 nanoERG for the fee.          |
|  4    | Assemble JSON                                     | See the example below.                                |
|  5    | `POST /wallet/transaction/send` (api\_key header) | The node broadcasts the sweep.                        |
|  6    | Repeat with fresh inputs                          | Stop when UTXO count is small.                        |

Query `minConfirmations`, `minInclusionHeight`, or both if you want mature inputs only. Example:

```bash
curl "http://127.0.0.1:9053/wallet/boxes/unspent?minConfirmations=10&limit=100" \
  -H "accept: application/json" -H "api_key: hello"
```

Example request body:

```json
{
  "inputsRaw": [
    "8e7a…00",
    "d1f5…42"
  ],
  "fee": 1000000,
  "requests": [
    {
      "address": "9hChangeAddressHere",
      "value": 25123456789
    }
  ]
}
```

Make sure the fee plus the output value equals the sum of your inputs.


## Troubleshooting

| Symptom or Log Entry                                 | Probable Cause                      | Fix                                                                                 |
| ---------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------- |
| `MaxInputsExceededError(…100)`                       | `maxInputs` still at default        | Set `maxInputs = 300`, restart the node.                                            |
| “Server was not able to produce a timely response …” | Too many inputs or node overload    | Sweep dust; verify `profile = "exchange"`; lower `optimalInputs` if needed.         |
| Sweep transaction shows few inputs                   | Node did not load the new config    | Check startup log for config path; confirm `wallet { … }` sits inside `ergo { … }`. |
| `invalid length XXX of Hex data`                     | An `inputsRaw` entry has odd length | Remove wrappers and whitespace; every hex string must have even length.             |
| `NotEnoughErgsError`                                 | Output + fee exceeds input total    | Lower the output amount, add inputs, or choose higher‑value boxes.                  |
| Wallet fills again right after clean‑up              | Constant tiny deposits              | Keep the self‑payment cron job running or raise the minimum deposit limit.          |



## Native Assets (tokens)

Users sometimes send random tokens to exchange addresses. A future node version will offer **auto‑burn** (see [Issue #1604](https://github.com/ergoplatform/ergo/issues/1604)). Until that release, destroy unwanted tokens with one step:

* Send them to the burn address `4MQyMKvMbnCJG3aJ` in a zero‑ERG transaction.

Community lists such as the [ergotipper token list](https://github.com/Luivatra/ergotipper-tokens) help you recognise unknown assets.



