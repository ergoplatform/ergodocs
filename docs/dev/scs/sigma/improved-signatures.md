
The initial implementation of distributed signatures support in the node worked well in simple cases, and ZK Treasury built on top of it. However, in complex cases, it has some problems:

* hints generated (such as commitments) were not tied to a position of a sub-expression in a sigma-expression. For example, for a statement like "atLeast(2, Coll(pkAlice, pkBob, pkCharlie)) && (pkBob || pkDiana)", the same commitment would be generated for Bob. This is improper and insecure - a signature would reveal Bob's secret key (as the same randomness is used twice for different challenges in Schnorr protocols).
* similarly, hints generated were not tied to inputs.

This is fixed with the new API introduced in the distributed-sigs branch. Now all the hints are tied with input indexes and positions in the sigma tree after script reduction with the current context. Also, API is now simpler-to-use.

So let me provide a new tutorial on collective signing. Like in the previous tutorial, first, we pay to 2-out-of-3 spending script (with keys stored in registers):

```
{
val pkA  = SELF.R4[GroupElement].get
val pkB  = SELF.R5[GroupElement].get
val pkC  = SELF.R6[GroupElement].get

atLeast(2, Coll(proveDlog(pkA), proveDlog(pkB), proveDlog(pkC)))
}
```

Then, when a transaction is confirmed (https://explorer.ergoplatform.com/en/transactions/71aa67f95e96827193bdf711f6ccf41b30ef8bbbdaef63ed672dfb7420a4c314), we get output bytes via /utxo/byIdBinary/{boxId}. Then we generate an unsigned transaction by providing inputs directly, in our example, by providing the following input to /wallet/transaction/generateUnsigned : 
 
```
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

Then Alice generates commitments for the unsigned transaction by sending it to the NEW /wallet/generateCommitments (additional secrets to be used along with wallets can also be provided), and in the output, she is getting both secret and public hints:

```
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

Then Alice must store secret hints locally and provide the public with Bob. Bob is signing using Alice's hints by sending a request to /wallet/transaction/sign like: 

```
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

And he sent signed (but invalid) transactions to Alice (he can send hints generated on the next step instead).

Now Alice is extracting a commitment from Bob and Carol from the transaction by sending a request to `/script/extractHints` like:

```
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

And then she adds her secret hint to generate a valid signed transaction, a request to /wallet/transaction/sign would be like this: 

```
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

(secret randomness omitted again)

And now a generated signed valid transaction could be broadcasted. 

