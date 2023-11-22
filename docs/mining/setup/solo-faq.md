# Solo Mining FAQ

## Why Aren't My Funds Visible in My Wallet?

When you mine, the rewards are initially linked to a *time-and-pubkey lock script*, not your standard P2PK address. To make these funds visible in your wallet, you need to transfer all the funds to your own address in the node wallet. Once the transfer is confirmed on the chain, the Explorer will display them.

## Why Do My Rewards Go to a Different Address?

Mining rewards are initially directed to UTXOs (Unspent Transaction Outputs) associated with specific scripts. These scripts lock the rewards to the miner's public keys for 720 blocks. You can see an example of such a script [here](https://explorer.ergoplatform.com/en/addresses/88dhgzEuTXaQ3tvkG8KeHesmXdvVomxHoHK5ExawGuxhs3nwBKkoQTxZogna6Dx9Jbu7KG2Wor22Uy73).

These UTXOs are not part of the node wallet before the locking height, so they are not included in your balance. However, they are stored in a special node application with `id = 9` (wallet application id = 10). You can locate them via the `/scan/unspentBoxes/9` API endpoint.

After 720 confirmations, the wallet will display the mined rewards, even if they are still associated with long scripts instead of short P2PK addresses.

## How Do I Verify If a Block Is Mined by Me?

You can obtain your mining rewards address with the `/mining/rewardAddress` API call. The response should look something like this:

```json
{
“rewardAddress”: “mPdcmQkPPvyMGoCDNg9oiasLyPpKJhHjgjpt89uJZE1oN9PJ9fKbdKDcfomtWoy3d1E7RFLTUbXbt1AS”
}
```
You can then verify your rewards on the [Ergo Explorer](https://explorer.ergoplatform.com/).

You can also obtain your "raw" public key via the `/mining/rewardPublicKey` endpoint:

```json
{
“rewardPubkey”: “03aa53abda9e6c958ed6046e6092b901662a26a01a2029c417b1c3f29b4b1c2799”
}
```

Then, you can check block headers (`pk` field) for this public key.



##  ​/mining​/solution API Endpoint

```json
{
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
  "n": "0000000000000000",
  "d": 987654321
}
```

- **pk** is the public key *in binary format*
- **n** is the nonce
- **w** and **d** are no longer used in Autolykos2 and are **constant**.

