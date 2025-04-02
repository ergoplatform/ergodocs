
The initial implementation of distributed signatures support in the Ergo node worked well in simple cases, and ZK Treasury was built on top of it. However, in complex scenarios, it exhibited some problems:

*   Hints generated (such as commitments) were not tied to the position of a sub-expression within the overall sigma-expression. For example, for a statement like `atLeast(2, Coll(pkAlice, pkBob, pkCharlie)) && (pkBob || pkDiana)`, the same commitment would be generated for Bob's public key (`pkBob`) in both parts of the expression. This is improper and insecure, as a signature could potentially reveal Bob's secret key because the same randomness would be used twice for different challenges in the Schnorr protocol.
*   Similarly, generated hints were not tied to specific transaction inputs.

These issues have been fixed with a new API introduced in the `distributed-sigs` branch. Now, all hints are tied to both input indexes and positions within the sigma tree after the script reduction phase (which considers the current context). Additionally, the API is now simpler to use.

Let's walk through a new tutorial on collective signing using this improved API. Similar to the previous tutorial, we first pay to a 2-out-of-3 spending script where the public keys are stored in registers:

```scala
{
  // Retrieve GroupElement pkA, pkB, and pkC from the register R4, R5, and R6 respectively.
  val pkA  = SELF.R4[GroupElement].get
  val pkB  = SELF.R5[GroupElement].get
  val pkC  = SELF.R6[GroupElement].get

  // Require at least two of the three provided public keys to be included in the spending transaction.
  atLeast(2, Coll(proveDlog(pkA), proveDlog(pkB), proveDlog(pkC)))
}

```

This code defines a script requiring signatures corresponding to at least two out of the three specified public keys (`pkA`, `pkB`, `pkC`) to spend the box. The public keys (as `GroupElement` values) are retrieved from registers R4, R5, and R6 of the box being spent (`SELF`). These are then converted into `SigmaProp` objects using `proveDlog`. Finally, the `atLeast` function enforces the 2-out-of-3 condition.

After funding a box with this script (e.g., transaction [71aa67...](https://explorer.ergoplatform.com/en/transactions/71aa67f95e96827193bdf711f6ccf41b30ef8bbbdaef63ed672dfb7420a4c314)), we can retrieve its details using the explorer or node API (e.g., `/utxo/byIdBinary/{boxId}`). To spend this box, we first generate an unsigned transaction. In this example, we provide the input box directly using the `inputsRaw` field in a request to the `/wallet/transaction/generateUnsigned` endpoint:
 
```json
{
  "requests": [
    {
      "address": "4MQyML64GnzMxZgm",
      "value": 999000000
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
"8094ebdc0310010404987300830308cde4c6a70407cde4c6a70507cde4c6a706079a8f1300030702b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f070354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380070235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d71aa67f95e96827193bdf711f6ccf41b30ef8bbbdaef63ed672dfb7420a4c31400"
  ],
  "dataInputsRaw": [ 
  ]
}
```

Then, Alice (possessing the secret key for `pkA`) generates commitments for this unsigned transaction by sending it to the `/wallet/generateCommitments` endpoint (note: additional secrets besides those in the wallet can be provided if needed). The response contains both secret hints (for Alice to keep) and public hints (to share with other participants):

```json
{
  "secretHints": {
    "0": [
      {
        "type": "dlog",
        "a": "03c855c50d173f1b0e2797390b71d82023dcb8e12950e4fa0b9ae3be17bacca2a1",
        "pubkey": {
          "op": -51,
          "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
        },
        "position": "0-0",
        "hint": "cmtWithSecret",
        "secret": "..."
      }
    ]
  },
  "publicHints": {
    "0": [
      {
        "type": "dlog",
        "a": "03c855c50d173f1b0e2797390b71d82023dcb8e12950e4fa0b9ae3be17bacca2a1",
        "pubkey": {
          "op": -51,
          "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
        },
        "position": "0-0",
        "hint": "cmtReal"
      }
    ]
  }
}
```

(secret randomness is omitted to avoid private key extraction).

Alice must store her secret hints locally and share the public hints with Bob (who possesses the secret key for `pkB`). Bob then uses his secret key and Alice's public hints to generate his part of the signature. He sends a request to `/wallet/transaction/sign` like the following (note the `hints` section containing Alice's public hints):

```json
{
  "tx": {
  "id": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
  "inputs": [
    {
      "boxId": "9bcbbce28b19132c28b2e088ddea03f792673e9c4509a239145c241c891ca4b9",
      "extension": {}
    }
  ],
  "dataInputs": [],
  "outputs": [
    {
      "boxId": "5bb78563af3843e5bf816c9dd50bd7c0a0b09c7fd2da2da075a8e5d8f545cb7f",
      "value": 999000000,
      "ergoTree": "10010101d17300",
      "assets": [],
      "creationHeight": 313682,
      "additionalRegisters": {},
      "transactionId": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
      "index": 0
    },
    {
      "boxId": "b5a1a069015f94bf7daaec46fc121044607603c844d1c6d6a8e9b2322379b375",
      "value": 1000000,
      "ergoTree": "1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304",
      "assets": [],
      "creationHeight": 313682,
      "additionalRegisters": {},
      "transactionId": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
      "index": 1
    }
  ]
},
  "inputsRaw": [
"8094ebdc0310010404987300830308cde4c6a70407cde4c6a70507cde4c6a706079a8f1300030702b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f070354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380070235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d71aa67f95e96827193bdf711f6ccf41b30ef8bbbdaef63ed672dfb7420a4c31400"
  ],
  "dataInputsRaw": [
    
  ],
  "secrets": {
    
  },
  "hints": {
  "secretHints": {
    
  },
  "publicHints": {
    "0": [
      {
        "type": "dlog",
        "a": "03c855c50d173f1b0e2797390b71d82023dcb8e12950e4fa0b9ae3be17bacca2a1",
        "pubkey": {
          "op": -51,
          "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
        },
        "position": "0-0",
        "hint": "cmtReal"
      }
    ]
  }
}
}
```

Bob sends the resulting partially signed transaction (which is still invalid as it only contains Bob's signature contribution) back to Alice. Alternatively, Bob could just send the hints generated by his signing step.

Now, Alice needs to combine her secret hints with the public hints generated by Bob (and potentially Carol, if she were involved). Alice can extract Bob's public hints from the partially signed transaction using the `/script/extractHints` endpoint:

```json
{
  "transaction": {
  "id": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
  "inputs": [
    {
      "boxId": "9bcbbce28b19132c28b2e088ddea03f792673e9c4509a239145c241c891ca4b9",
      "spendingProof": {
        "proofBytes": "7d64cd47d3dc8bc5c336297e494f48d601c586175b37da228a54a77f52eb1ce307c22c7541368b73307bf37be4051406b49e989b4aee9f27789de0c426a8231fead96178544cbb54b37286f2630dcd9d5794ae9905697e8eeb0d03540d4cb8352a0734187d5e84b6d0825f12e3fcf287ee24e48d3a2a6dfb56471c41767ef88a3279e8fdc70274d85baf16686b641eaa",
        "extension": {}
      }
    }
  ],
  "dataInputs": [],
  "outputs": [
    {
      "boxId": "5bb78563af3843e5bf816c9dd50bd7c0a0b09c7fd2da2da075a8e5d8f545cb7f",
      "value": 999000000,
      "ergoTree": "10010101d17300",
      "assets": [],
      "creationHeight": 313682,
      "additionalRegisters": {},
      "transactionId": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
      "index": 0
    },
    {
      "boxId": "b5a1a069015f94bf7daaec46fc121044607603c844d1c6d6a8e9b2322379b375",
      "value": 1000000,
      "ergoTree": "1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304",
      "assets": [],
      "creationHeight": 313682,
      "additionalRegisters": {},
      "transactionId": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
      "index": 1
    }
  ],
  "size": 313
},
  "real": [
    {
      "op": -51,
      "h": "0354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380"
    }
  ],
  "simulated": [
    {
      "op": -51,
      "h": "0235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d"     
    }
  ]
}
```

Finally, Alice combines her locally stored secret hints with the public hints extracted from Bob's contribution. She sends a final request to `/wallet/transaction/sign` containing the unsigned transaction and all the collected hints (her secret ones and Bob's public ones):

```json
{
  "tx": {
  "id": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
  "inputs": [
    {
      "boxId": "9bcbbce28b19132c28b2e088ddea03f792673e9c4509a239145c241c891ca4b9",
      "extension": {}
    }
  ],
  "dataInputs": [],
  "outputs": [
    {
      "boxId": "5bb78563af3843e5bf816c9dd50bd7c0a0b09c7fd2da2da075a8e5d8f545cb7f",
      "value": 999000000,
      "ergoTree": "10010101d17300",
      "assets": [],
      "creationHeight": 313682,
      "additionalRegisters": {},
      "transactionId": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
      "index": 0
    },
    {
      "boxId": "b5a1a069015f94bf7daaec46fc121044607603c844d1c6d6a8e9b2322379b375",
      "value": 1000000,
      "ergoTree": "1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304",
      "assets": [],
      "creationHeight": 313682,
      "additionalRegisters": {},
      "transactionId": "6c7bf7a9720d26bec5c3b5bf1bc6199e9a5b876ba5994ab5e4214b0d8eed1492",
      "index": 1
    }
  ]
},
  "inputsRaw": [
"8094ebdc0310010404987300830308cde4c6a70407cde4c6a70507cde4c6a706079a8f1300030702b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f070354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380070235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d71aa67f95e96827193bdf711f6ccf41b30ef8bbbdaef63ed672dfb7420a4c31400"
  ],
  "dataInputsRaw": [
  ],
  "secrets": { 
  },
  "hints": {
  "secretHints": {
    "0": [
      {
        "type": "dlog",
        "a": "03c855c50d173f1b0e2797390b71d82023dcb8e12950e4fa0b9ae3be17bacca2a1",
        "pubkey": {
          "op": -51,
          "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
        },
        "position": "0-0",
        "hint": "cmtWithSecret",
        "secret": "...."
      }
    ]
  },
  "publicHints": {
    "0": [
      {
        "type": "dlog",
        "a": "02b6c2b73e59ad061211cebb37a7d9b238b9388cdb0c3b96ae2152ba174f67de90",
        "pubkey": {
          "op": -51,
          "h": "0235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d"
        },
        "position": "0-2",
        "hint": "cmtSimulated"
      },
      {
        "hint": "proofSimulated",
        "challenge": "e39924c725e1aee0cb705ce18a15d5425148939b7739e628",
        "pubkey": {
          "op": -51,
          "h": "0235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d"
        },
        "proof": "e39924c725e1aee0cb705ce18a15d5425148939b7739e628ee24e48d3a2a6dfb56471c41767ef88a3279e8fdc70274d85baf16686b641eaa",
        "position": "0-2"
      },
      {
        "type": "dlog",
        "a": "0323bd7f1b87280aa2b7cb2a374da1897ef7d5fae7ab3948440907d303427740ba",
        "pubkey": {
          "op": -51,
          "h": "0354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380"
        },
        "position": "0-1",
        "hint": "cmtReal"
      },
      {
        "hint": "proofReal",
        "challenge": "69cd83b8770ab203ccb27094cb235e31613360e0933cf22e",
        "pubkey": {
          "op": -51,
          "h": "0354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380"
        },
        "proof": "69cd83b8770ab203ccb27094cb235e31613360e0933cf22e5794ae9905697e8eeb0d03540d4cb8352a0734187d5e84b6d0825f12e3fcf287",
        "position": "0-1"
      }
    ]
  }
}
}
```

(Secret randomness omitted again for security).

This final request produces a fully signed, valid transaction that satisfies the 2-out-of-3 condition, which can now be broadcast to the network.
