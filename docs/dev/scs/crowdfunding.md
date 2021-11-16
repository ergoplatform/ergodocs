
## What is Crowdfunding?

Crowdfunding is a way of raising capital through the collective efforts of individuals. The campaigns are mostly started via the world wide web and allow projects and businesses to be funded by raising small amounts of money from a large number of people.
One of the best known examples for successful crowdfunding startups is Oculus Rift, a virtual reality headset. The company Oculus VR initiated its campaign in 2012 and was only two years later acquired by Facebook for $2 billion total. Besides the usual startups, there are also a lot of blockchain projects which went the way of crowdfunding, for example, Ethereum, Tron and EOS. Today, numerous platforms exist that allow you to publish your campaign. Some of the bigger ones are Indiegogo, Kickstarter, and Gofundme, only to name a few. 
Crowdfunding has a lot of benefits: a wide reach, efficiency, and marketing aspects being the most convincing... But for now, let's get onto what's really important! 


## ErgoFund

- [Ergo Crowdfunding CLI](https://github.com/robkorn/ergo-crowdfunding-cli) | Command-line tool which enables participating and interacting with crowdfunding campaigns on Ergo
- [Scanner](https://github.com/ergoplatform/scanner) 
- ZK Treasury |  a tool for joint spendings with on-chain privacy 
  - [Server](https://github.com/anon-real/DistributedSigsServer) 
  - [Client](https://github.com/anon-real/DistributedSigsClient)
- ['A Collective Spending Appproach'](https://www.reddit.com/r/ergonauts/comments/ohftim/ergoteam_a_simpler_collective_spending_approach/)



## Introducing Crowdfunding on Ergo

A few days ago, on August 28th, core developer [Kushti](https://www.ergoforum.org/u/kushti) stated on the (Ergo forum)[www.ergoforum.org] that he managed to successfully write and implement code that allows users to start a crowdfunding campaign on top of the Ergo blockchain (as mentioned in the [whitepaper page 6](https://ergoplatform.org/docs/ErgoScript.pdf). This code even works with the current wallet API. [Here](https://ergoplatform.org/en/blog/2019_06_04_wallet-documentation/) is a quick guide on how to set up the wallet.
In this article, you will learn how to do exactly that: crowdfunding on top of Ergo! It also takes you through the proposal of the first campaign ever, which is to fund the [post-EIP1](https://github.com/ergoplatform/eips/blob/master/eip-0001.md) crowdfunding script development.
If you want to go into all the details, please read the following section, “The Script”. Otherwise, you can simply skip to reading the “How To Donate”, "How To Collect Donations", and “Crowdfunding Project Proposal” sections below that.

## The Script

The simplest crowdfunding script, according to the [ErgoScript White Paper (page 6)](https://ergoplatform.org/docs/ErgoScript.pdf), is “a script for the following crowdfunding situation: a project backer (with key backerPubKey) wishes to give money to a project (with key projectPubKey), but only if the project raises enough money (at least minToRaise) from other sources by a deadline (expressed in terms of HEIGHT). 
To give money to the project, the backer will create an output box protected by the following script. The script contains two conditions: one for the case the deadline has passed (enabling the backer to get the money back) and one for the case it succeeded (enabling the project to spend the money if the amount is at least minToRaise before the deadline). 

In order to ensure enough money has been raised, the script will search the output collection for a box with a sufficient value going to the projectPubKey. To check where the value of the output box is going, the script will read the script protecting the output box and compare it to the script corresponding to proveDlog(projectPubKey); this script can be obtained byprojectPubKey.propBytes.

As currently the API does not support embedding of custom environment variables (only predefined ones like HEIGHT), the only way to compile the script is to replace such variables in the script from the white-paper with concrete values. For example, consider that a crowdfunding campaign is successful if it is raising 500 Ergs before block number 50,000. For backerPubKey and projectPubKey we can use PK() function which accepts only P2PK serialized keys at the moment. Then the modified script from the WhitePaper becomes the following:

```scala
{
   val backerPubKey = PK("9h7DHKSDgE4uvP8313GVGdsEg3AvdAWSSTG7XZsLwBfeth4aePG")
   val projectPubKey = PK("9gBSqNT9LH9WjvWbyqEvFirMbYp4nfGHnoWdceKGu45AKiya3Fq") 
    
   val deadline = 50000
   val minToRaise = 500L * 1000000000 
   
   val fundraisingFailure = HEIGHT >= deadline && backerPubKey
   val enoughRaised = {(outBox: Box) =>outBox.value >= minToRaise 
                              && outBox.propositionBytes == projectPubKey.propBytes
                      }
        
   val fundraisingSuccess = HEIGHT < deadline && projectPubKey && OUTPUTS.exists(enoughRaised)
   fundraisingFailure || fundraisingSuccess                     
 }                              
```

## How to Donate

First of all, JSON is not supporting multi-line strings, so you need to replace line breaks with `\n`.
Also, quotes are to be escaped, so use " instead of ". The resulting JSON will be sent to `/script/p2sAddress`.
To donate to a project, first get your address from /wallet/addresses, take e.g. the first of them. Put the address into the backerPubKey, so a request to /script/p2sAddress will look like the following after this step:

```scala
{
  "source": "{ 
    val backerPubKey = PK(\"9...\")
    val projectPubKey = PK(\"9gBSqNT9LH9WjvWbyqEvFirMbYp4nfGHnoWdceKGu45AKiya3Fq\")
    val deadline = 50000
    val minToRaise = 500L * 1000000000
    val fundraisingFailure = HEIGHT >= deadline && backerPubKey
    val enoughRaised = {
      (outBox: Box) => 
        outBox.value >= minToRaise && outBox.propositionBytes == projectPubKey.propBytes
    } 
    val fundraisingSuccess = HEIGHT < deadline && projectPubKey && OUTPUTS.exists(enoughRaised) 
    fundraisingFailure || fundraisingSuccess 
  }"
}    
```

with your address instead of “9…”.

Send the string to `/script/p2sAddress` to get a response like:

```scala
{
  "address": "GB3kh2izpWKvyZfMboQwsEscjPaZcz9WrzGqZB4ZrkzRreiFMV6HZYWXGMK3rqCjDCoPgWGNzfnYSUhivW4a1VRYPE7uZXwKnBcqWcRkiuTx6QW55EcPcWeELUsumwdtKoFtWY583nWnKZff"
}     
```

Copy address string (GB3… in our example) and send the money to it via `/wallet/payment/send` . A request to the API method to send 10 Ergs (10 Billion nanoErgs) will be like following:

```scala
[
 {
   "address": "GB3kh2izpWKvyZfMboQwsEscjPaZcz9WrzGqZB4ZrkzRreiFMV6HZYWXGMK3rqCjDCoPgWGNzfnYSUhivW4a1VRYPE7uZXwKnBcqWcRkiuTx6QW55EcPcWeELUsumwdtKoFtWY583nWnKZff",
   "value": 10000000000
 }
]
```

That’s all!

Now the wallet will automatically find the box on the blockchain, as it contains the public key which belongs to the wallet in the refund condition. The wallet then periodically checks whether the box is spendable by constructing a simplest transaction with the box as an input and just one output (to the same address). After refund height (50,000 in our example) the wallet will be able to spend the box and so the box value will be added to /wallet/balances.
Please note that this will not be the case after EIP-1 3 implementation as the wallet will use narrow recognition patterns by then.

## How to Collect Donations

The wallet which is associated with the project public key will find incoming boxes on the blockchain. However, it will fail to make sure that boxes are spendable, as the wallet currently is using a simplest transaction for that, and the script is failing for such a spending transaction.
Before `/wallet/boxes/uncertain` method being implemented, the only way for a project to find incoming boxes. Then `/wallet/transaction/send` with manually provided (in “inputsRaw”) serialized boxes (use `/utxo/byIdBinary` to get the serialized box by its identifier).

Kushti did that by himself and got the following [transaction](https://explorer.ergoplatform.com/en/transactions/3d5a1102296b6159754097f33e780cae2692d9a2ec2b6daf26219651bcc2ae48).

Please note that [EIP-1](https://github.com/ergoplatform/eips/blob/master/eip-0001.md) will break this workflow as well.

Kushti proposes to raise 500 Ergs before block 50,000 to develop command-line scripts (in Python) for organizing and participating in crowdfunding campaigns after EIP-1 implementation. Command-line scripts are more suitable than doing requests manually and also could be used for building graphic interfaces on top of them.

The treasury did provide [half of the funds](https://explorer.ergoplatform.com/en/transactions/2fc882792b94f8210e4378f2f5bab90896523e212d927ed16600170d76f46ac9), so others need to contribute the missing 250 Erg collectively. In case of a campaign failure refunds will be given automatically. As collecting pledges is not trivial at the moment, Kushti will lead the project role, so please use the following key, which is controlled by him: 

`9gBSqNT9LH9WjvWbyqEvFirMbYp4nfGHnoWdceKGu45AKiya3Fq`

In order to donate any amount of money, please follow the `“How To Donate”` section above with replacing backerPubKey with your public key, and pledge amount with a proper value (please note that it is in nanoErgs, `1 Erg = 1.000.000.000 nanoErgs`).
