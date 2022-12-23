## Why are mining rewards going to some strange address?

Mining rewards are sent to UTXOs associated with special scripts that lock rewards to miner public keys for 720 blocks (72 in the testnet). You can see an example of such a script [here](https://explorer.ergoplatform.com/en/addresses/88dhgzEuTXaQ3tvkG8KeHesmXdvVomxHoHK5ExawGuxhs3nwBKkoQTxZogna6Dx9Jbu7KG2Wor22Uy73).

Such UTXOs do not belong to the node wallet before the locking height, so the wallet does not include them into your balance. 

However, such UTXOs are stored in a special node application with `id = 9` (wallet application id = 10), thus they can be found via `/scan/unspentBoxes/9` (so /scan/unspentBoxes node [Swagger](swagger.md) API method with id = 9).

After enough confirmations (720 for the mainnet, 72 for the testnet) wallet shows mined rewards even if they still associated with long scripts, not short P2PK addresses.

## How to check if a block is yours. 

You can retrieve your mining rewards address with `/mining/rewardAddress` API call, which should return something like this:

```
{
“rewardAddress”: “mPdcmQkPPvyMGoCDNg9oiasLyPpKJhHjgjpt89uJZE1oN9PJ9fKbdKDcfomtWoy3d1E7RFLTUbXbt1AS”
}
```

Then you can check rewards on the [ergo explorer](https://explorer.ergoplatform.com/). 

You can also retrieve your “raw” public key via the `/mining/rewardPublicKey` endpoint. 

```
{
“rewardPubkey”: “03aa53abda9e6c958ed6046e6092b901662a26a01a2029c417b1c3f29b4b1c2799”
}
```

Then check block headers (`pk` field) for this public key.

## Funds not showing in wallet 

Mining rewards belong to time-and-pubkey lock script, not your "normal" p2pk address. Just send all the funds to yourself in the node wallet, and Explorer will show them after the transfer is confirmed on chain 


##  ​/mining​/solution entrypoint

```
{
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
  "n": "0000000000000000",
  "d": 987654321
}
```

- **pk** is public key *as binary*
- **n** is nonce
- **w** and d are not used anymore in Autolykos2 and **constant**.
