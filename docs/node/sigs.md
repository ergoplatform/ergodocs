---
tags:
  - Distributed Signatures
  - Signatures
  - Multisig
  - Node API
  - EIP-11
  - Technical
---

# Improved distributed signatures

The initial implementation of distributed signatures support in the node worked well in simple cases, and ZK Treasury built on top of it. However, in complex cases, it has some problems:

* The hints generated (such as commitments) were not tied to a position of a sub-expression in a sigma-expression. For example, for a statement like "atLeast(2, Coll(pkAlice, pkBob, pkCharlie)) && (pkBob || pkDiana)", the same commitment would be generated for Bob. This is improper and insecure - a signature would reveal Bob's secret key (as the same randomness is used twice for different challenges in Schnorr protocols). Similarly, hints generated were not tied to inputs.

This is fixed with the new API introduced in the distributed-sigs branch. Now all the hints are tied with input indexes and positions in the sigma-tree after script reduction with the current context. Also, API is now simpler-to-use.

So let me provide a new tutorial on collective signing. Like in the previous tutorial, first, we pay to a 2-out-of-3 spending script (with keys stored in registers):


```json
{
val pkA  = SELF.R4[GroupElement].get
val pkB  = SELF.R5[GroupElement].get
val pkC  = SELF.R6[GroupElement].get

atLeast(2, Coll(proveDlog(pkA), proveDlog(pkB), proveDlog(pkC)))
}
```

Then, when a transaction is confirmed (https://explorer.ergoplatform.com/en/transactions/71aa67f95e96827193bdf711f6ccf41b30ef8bbbdaef63ed672dfb7420a4c314), we get output bytes via /utxo/byIdBinary/{boxId}. Then we generate an unsigned transaction by providing inputs directly, in our example, by providing the following input to /wallet/transaction/generateUnsigned : 
 
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

Then Alice generates commitments for the unsigned transaction by sending it to the NEW /wallet/generateCommitments (additional secrets to be used along with wallets can also be provided), and in the output, she is getting both secret and public hints:

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

Then Alice must store secret hints locally and provide the public to Bob. Bob is signing using Alice's hints by sending a request to /wallet/transaction/sign like: 

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

And sending signed (but invalid) transactions to Alice (he can send hints generated on the next step instead).

Now Alice is extracting a commitment from Bob and Carol from the transaction by sending a request to /script/extractHints like:

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

And then she adds her secret hint to generate a valid signed transaction, a request to /wallet/transaction/sign would be like this: 

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

(secret randomness omitted again)

And now generated signed valid transactions can be broadcasted. 

Taken from the forum post [Improved distributed signatures](https://www.ergoforum.org/t/improved-distributed-signatures/366) ~ Sept 2020

## Let’s sign collectively! Distributed signatures API

It is well-known (among hardcore Ergonauts) that Ergo supports various composable and efficient zero-knowledge proofs of knowledge in its authentication language. In particular, it provides the possibility for ring and threshold signatures preserving zero-knowledge, so, for example, by observing 2-out-of-3 threshold signatures associated with public keys of (Alice, Bob, and Carol) on the blockchain, it is not possible to figure out who were those two parties who signed.

While Ergo protocol supports threshold and ring signatures since day one, concrete applications doing signing were not available eventually. First, the ErgoMix implementations (by @ anon92048 and then @ anon2020s) use a ring signature, hiding a spending path. Moreover, recently [EIP-11](https://github.com/ergoplatform/eips/pull/8) was introduced, which is about adding support for distributed signing to the reference client (and not only).  The implementation of EIP-11 is mostly done in [this PR](https://github.com/ergoplatform/ergo/pull/1118), which explains how to use the new API method

First, make a script for a box protected with a 2-out-of-3 threshold signature. One option is about to hardcode public keys in the script; I've chosen another way, namely, to put the public keys of signers into registers:

    {
    val pkA  = SELF.R4[GroupElement].get
    val pkB  = SELF.R5[GroupElement].get
    val pkC  = SELF.R6[GroupElement].get

    atLeast(2, Coll(proveDlog(pkA), proveDlog(pkB), proveDlog(pkC)))
    }
.
Then we need to lock money with concrete keys. It seems the node Swagger API is the most convenient way to do that, e.g. by posting the following payment request to /wallet/payment/send:
   
    [
        {
          "address": "umRXw8E7PmdHbswncxFe3jmE51oGFzL4CqfZYfiRr4aL",
          "value": 1000000000,    
          "registers": {
              "R4": "0702b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f",
              "R5": "070354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380",
              "R6": "070235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d"
          }
        }
    ]

(use /utils/addressToRaw/{address} method to get encoded points from P2PK addresses shown by the wallet and prepend group element type descriptor "07" then).  

Thus we are getting the following box, for example [(output #0)](https://explorer.ergoplatform.com/en/transactions/0ffc5ba326262f25016c59c58a34b2f7fed2ea1b69f8f007d270f6ef07bced49):. We can get the binary representation of unspent box via **/utxo/byIdBinary** API method, e.g. `utxo/byIdBinary/f1892011ed31b8e51f3f3ae44f6d9132070343a7bf6db61b3342696a7873a085` gives us:

```
"8094ebdc0310010404987300830308cde4c6a70407cde4c6a70507cde4c6a70607abdd0f00030702b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f070354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380070235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d0ffc5ba326262f25016c59c58a34b2f7fed2ea1b69f8f007d270f6ef07bced4900"
```
We use the first two keys for signing (as it is 2-out-of). Please note that members of the signing ring know (and choose) who is signing and who will be simulated.   

Let us assume that the first key belongs to Alice and the second key belongs to Bob. The signing procedure could be as follows:

First, Alice generates secret randomness and public commitment to it by posting the following request to /script/generateCommitment : 

    {
      "op": -51,
      "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
    } 

Result is :
    {
       "r": "...",
      "a": "02c103443ab26655a1ef36f44643700cc5f4730a2a1830085dda1072ccfb30940f"
     }
  
("r" is omitted to avoid private key recovery) 
She then sends "a" value to Bob, and an unsigned transaction is generated via /wallet/transaction/generateUnsigned.

Now Bob is generating an invalid (partial) signature by sending the following signing request to /wallet/transaction/sign with Alice's commitment included as a hint: 

    {
      "tx": {
      "id": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
      "inputs": [
        {
          "boxId": "f1892011ed31b8e51f3f3ae44f6d9132070343a7bf6db61b3342696a7873a085",
          "extension": {}
        }
      ],
      "dataInputs": [],
      "outputs": [
        {
          "boxId": "49974195f916dcc95e94c72bcf6e90200bbf2c06e5cc7a22a505bad1da77927d",
          "value": 999000000,
          "ergoTree": "10010101d17300",
          "assets": [],
          "creationHeight": 257748,
          "additionalRegisters": {},
          "transactionId": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
          "index": 0
        },
        {
          "boxId": "096192e25b691697b5afdd4a5cf39c69b84fba8b483f475c2e2d3cf47758abb1",
          "value": 1000000,
          "ergoTree": "1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304",
          "assets": [],
          "creationHeight": 257748,
          "additionalRegisters": {},
          "transactionId": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
          "index": 1
        }
      ]
    },
      
      "secrets": {
        "dlog": [      
        ],
        "dht": [     
        ]
      },

      "hints": [
        {
          "hint": "cmtReal",
          "type": "dlog",
          "pubkey":{
             "op": -51,
             "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
          },
          "a": "02c103443ab26655a1ef36f44643700cc5f4730a2a1830085dda1072ccfb30940f"  
        }
      ]
    }

Bob is sending a transaction with an invalid signature to Alice. First, she extracts Bob's and Carol's (simulated by Bob actually) commitments and partial signatures by feeding Bob's invalid transaction and Bob's and Carol's pubkeys into /script/extractHints : 

    {
      "transaction": {
      "id": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
      "inputs": [
        {
          "boxId": "f1892011ed31b8e51f3f3ae44f6d9132070343a7bf6db61b3342696a7873a085",
          "spendingProof": {
            "proofBytes": "2c429642fba49717349dbeafb5c4a0725d012e901352fdcc390d53103824fcadb82553ddef404d69794679327c976bc3195dc78926c8161437d595a0a04dac8d3fe08d999d3c70f18c92cddaa1260d3a564c7431c478825d52bd28673637d986f545e871bd07a99cf6c3e04c2342da40f4608fb322f213c2b1f9166ad526cb7d7a931b02b8966f6ba4cc98aa435156f4",
            "extension": {}
          }
        }
      ],
      "dataInputs": [],
      "outputs": [
        {
          "boxId": "49974195f916dcc95e94c72bcf6e90200bbf2c06e5cc7a22a505bad1da77927d",
          "value": 999000000,
          "ergoTree": "10010101d17300",
          "assets": [],
          "creationHeight": 257748,
          "additionalRegisters": {},
          "transactionId": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
          "index": 0
        },
        {
          "boxId": "096192e25b691697b5afdd4a5cf39c69b84fba8b483f475c2e2d3cf47758abb1",
          "value": 1000000,
          "ergoTree": "1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304",
          "assets": [],
          "creationHeight": 257748,
          "additionalRegisters": {},
          "transactionId": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
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

And then, she adds a hint of her commitment and randomness and produces a transaction. A request to /wallet/transaction/sign is as follows:

    {
      "tx": {
      "id": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
      "inputs": [
        {
          "boxId": "f1892011ed31b8e51f3f3ae44f6d9132070343a7bf6db61b3342696a7873a085",
          "extension": {}
        }
      ],
      "dataInputs": [],
      "outputs": [
        {
          "boxId": "49974195f916dcc95e94c72bcf6e90200bbf2c06e5cc7a22a505bad1da77927d",
          "value": 999000000,
          "ergoTree": "10010101d17300",
          "assets": [],
          "creationHeight": 257748,
          "additionalRegisters": {},
          "transactionId": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
          "index": 0
        },
        {
          "boxId": "096192e25b691697b5afdd4a5cf39c69b84fba8b483f475c2e2d3cf47758abb1",
          "value": 1000000,
          "ergoTree": "1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304",
          "assets": [],
          "creationHeight": 257748,
          "additionalRegisters": {},
          "transactionId": "ebafdd3a00bd3d9aa26be4056c4f742e9cb0702cce9864567aa4e34cda185d54",
          "index": 1
        }
      ]
    },
     

      "hints": [
        {
          "hint": "cmtWithSecret",
          "type": "dlog",
          "pubkey": {
             "op": -51,
             "h": "02b353df14cd94849c36194bba03000dafaeb91b3a425a863f5660565189ddfe8f"
          },
          "a": "02c103443ab26655a1ef36f44643700cc5f4730a2a1830085dda1072ccfb30940f" ,
          "secret": "..." 
        },
         {
        "type": "dlog",
        "a": "035e5bcc7edcf47454fc41bf4b824e7357cb1b6a95df89c79d10cf867713d2d5ac",
        "pubkey": {
          "op": -51,
          "h": "0235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d"
        },
        "hint": "cmtSimulated"
      },
      {
        "hint": "proofSimulated",
        "challenge": "e0556372b3c893e1fdf34bc8850577c9d6cba5c697eb4189",
        "pubkey": {
          "op": -51,
          "h": "0235647199b150d8fab315d74e44b78866787d0330241fd471f98bf6c2bffe1e8d"
        },
        "proof": "e0556372b3c893e1fdf34bc8850577c9d6cba5c697eb4189f4608fb322f213c2b1f9166ad526cb7d7a931b02b8966f6ba4cc98aa435156f4"
      },
      {
        "type": "dlog",
        "a": "0277755feea497330c74d6442dfe9895e8de037a6b4e0d96e555b13f0f17d8869c",
        "pubkey": {
          "op": -51,
          "h": "0354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380"
        },
        "hint": "cmtReal"
      },
      {
        "hint": "proofReal",
        "challenge": "d95830628bec6f4c45d618156a453aa0af8ddcf4eb7c2a4a",
        "pubkey": {
          "op": -51,
          "h": "0354efc32652cad6cf1231be987afa29a686af30b5735995e3ce51339c4d0ca380"
        },
        "proof": "d95830628bec6f4c45d618156a453aa0af8ddcf4eb7c2a4a564c7431c478825d52bd28673637d986f545e871bd07a99cf6c3e04c2342da40"
      }
      ]
    }

("secret" aka "r" skipped again)

As a result, we're getting JSON-encoded transactions which can be broadcasted via a POST request to /transactions to get the transaction on the blockchain.

Still, the code is not finalized ("op": -51 looks ugly; however, it was done previously) and is not user-friendly, so as a next step, some applications working with the API are needed.
- [Let’s sign collectively! Distributed signatures API](https://www.ergoforum.org/t/lets-sign-collectively-distributed-signatures-api/259) ~ June, 2020

## Resources

- [EIP-11 on distributed signatures](https://github.com/ergoplatform/eips/pull/8)
