
# FleetSharp

[FleetSharp](https://github.com/pulsarz/FleetSharp) is a C# library for building transactions on the Ergo blockchain, inspired by the excellent TypeScript [fleet-sdk](fleet.md).


## Usage

#### Example that sends a simple ERG only transaction from the node's wallet
```cs
var unspentWalletBoxes = await node.GetAllUnspentBoxesInWallet(false);
var currentHeight = await node.GetCurrentHeight();

var tx = new TransactionBuilder(currentHeight)
    .from(unspentWalletBoxes)
    .to(new List<OutputBuilder> { new OutputBuilder(1000000000L, ErgoAddress.fromBase58("9iJyQKGYN4agM8UyJKjj8UoxWRa89dfDr2ptXYKEd7fJxLsYcuF")) })
    .sendChangeTo(ErgoAddress.fromBase58("9gzGJworU5a4yrwLndgLoJa8N4MPMpn7p9mj8TShUTJ7wYhabKn"))
    .payMinFee()
    .build().ToPlainObject();

var signedTx = await node.SignTransaction(tx);
var transactionId = await node.SubmitSignedTransaction(signedTx);
```

#### Example that sends a transaction with some tokens from the node's wallet
```cs
var unspentWalletBoxes = await node.GetAllUnspentBoxesInWallet(false);
var currentHeight = await node.GetCurrentHeight();

var tx = new TransactionBuilder(currentHeight)
    .from(unspentWalletBoxes)
    .to(new List<OutputBuilder>
    { 
        new OutputBuilder(1000000000L, ErgoAddress.fromBase58("9iJyQKGYN4agM8UyJKjj8UoxWRa89dfDr2ptXYKEd7fJxLsYcuF"))
            .AddToken(new TokenAmount<long>
            {
                tokenId = "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
                amount = 10000L
            })
     })
    .sendChangeTo(ErgoAddress.fromBase58("9gzGJworU5a4yrwLndgLoJa8N4MPMpn7p9mj8TShUTJ7wYhabKn"))
    .payMinFee()
    .build().ToPlainObject();

var signedTx = await node.SignTransaction(tx);
var transactionId = await node.SubmitSignedTransaction(signedTx);
```

#### Example minting tokens
```cs
var unspentWalletBoxes = await node.GetAllUnspentBoxesInWallet(false);
var currentHeight = await node.GetCurrentHeight();

var tx = new TransactionBuilder(currentHeight)
    .from(unspentWalletBoxes)
    .to(new List<OutputBuilder>
    { 
        new OutputBuilder(OutputBuilder.SAFE_MIN_BOX_VALUE, ErgoAddress.fromBase58("9iJyQKGYN4agM8UyJKjj8UoxWRa89dfDr2ptXYKEd7fJxLsYcuF"))
            .mintToken(new NewToken<long>
            {
                amount = 100,
                name = "FleetSharp test mint token #1",
                decimals = 0,
                description = "This is a test token minted with FleetSharp"
            })
    })
    .sendChangeTo(ErgoAddress.fromBase58("9gzGJworU5a4yrwLndgLoJa8N4MPMpn7p9mj8TShUTJ7wYhabKn"))
    .payMinFee()
    .build().ToPlainObject();

var signedTx = await node.SignTransaction(tx);
var transactionId = await node.SubmitSignedTransaction(signedTx);
```

#### Interacting with a contract by ensuring input selection and setting registers (this is purely a fictional example to demonstrate what is possible)
```cs
using static FleetSharp.Sigma.ConstantSerializer;
using static FleetSharp.Sigma.ISigmaCollection;
using static FleetSharp.Sigma.IPrimitiveSigmaType;

var unspentWalletBoxes = await node.GetAllUnspentBoxesInWallet(false);
var currentHeight = await node.GetCurrentHeight();

var spendBox = await node.GetBox("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff");

var tx = new TransactionBuilder(currentHeight)
    .from(unspentWalletBoxes)
    .to(new List<OutputBuilder>
    { 
        new OutputBuilder(OutputBuilder.SAFE_MIN_BOX_VALUE, ErgoAddress.fromErgoTree(spendBox.ergoTree, Network.Mainnet))
            .SetAdditionalRegisters(new NonMandatoryRegisters
            {
                R4 = SConstant(SInt(47851)),/*integer*/
                R5 = SConstant(SColl(SigmaTypeCode.Byte, FleetSharp.Tools.HexToBytes("e218ee38a9fa71a770968f2746d624f8")))/*hex string as Coll[Byte]*/
            })
    })
    .sendChangeTo(ErgoAddress.fromBase58("9gzGJworU5a4yrwLndgLoJa8N4MPMpn7p9mj8TShUTJ7wYhabKn"))
    .payMinFee()
    .build().ToPlainObject();

var signedTx = await node.SignTransaction(tx);
var transactionId = await node.SubmitSignedTransaction(signedTx);
```

#### Reading registers from a box
```cs
using static FleetSharp.Sigma.ConstantSerializer;
using static FleetSharp.Sigma.ISigmaCollection;
using static FleetSharp.Sigma.IPrimitiveSigmaType;

var box = await node.GetBox("07b1276dd8207767c320a76a0a7ba9c76feb1f414c58cb9335810341a02236dc");

byte[] borrower = SParse(box.additionalRegisters.R4);
long amount = SParse(box.additionalRegisters.R5);
long repayment = SParse(box.additionalRegisters.R6);
int maturityLength = SParse(box.additionalRegisters.R7);
```
