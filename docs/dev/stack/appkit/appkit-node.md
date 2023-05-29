# Interacting with a local node.

Among other things, the Appkit library allows us to communicate with Ergo nodes via the [REST API](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml). 

Let's see how we can write ErgoTool - a simple Java console application (similar to [ergo-tool](https://github.com/ergoplatform/ergo-tool) utility) which uses Appkit library. 

ErgoTool allows to create and send a new transaction to any existing Ergo node on the network which. A new node can also be started locally and thus available at `http://localhost:9052/`. 

Suppose we [set up a full node](https://github.com/ergoplatform/ergo/wiki/Set-up-a-full-node) and started it using the following command.

```shell
$ java -jar -Xmx4G target/scala-2.12/ergo-4.0.8.jar --testnet -c ergo-testnet.conf
```

We will need some configuration parameters which can be loaded from `ergotool.json` file

```json
{
  "node": {
    "nodeApi": {
      "apiUrl": "http://139.59.29.87:9053",
      "apiKey": "82344a18c24adc42b78f52c58facfdf19c8cc38858a5f22e68070959499076e1"
    },
    "wallet": {
      "mnemonic": "slow silly start wash bundle suffer bulb ancient height spin express remind today effort helmet",
      "password": "",
      "mnemonicPassword": ""
    },
    "networkType": "MAINNET"
  },
  "parameters": {
    "newBoxSpendingDelay": "30"
  }
}
```

Here `apiKey` is the secret key required for API authentication which can be obtained as described [here](swagger.md). And mnemonic is the secret phrase obtained during [setup of a new wallet](wallet.md) or if you don't want to set up your node using ergo-tool's [mnemonic](https://github.com/ergoplatform/ergo-tool#supported-commands) command.

Our example app also reads the amount of NanoErg to put into a new box from command line arguments

```java
public static void main(String[] args) {
    long amountToPay = Long.parseLong(args[0]);
    ErgoToolConfig conf = ErgoToolConfig.load("ergotool.json");
    int newBoxSpendingDelay = Integer.parseInt(conf.getParameters().get("newBoxSpendingDelay"));
    // the rest of the code shown below 
    ...
}
```

Next, we connect to the running testnet node from our Java application by creating a `ErgoClient` instance.

```java
ErgoNodeConfig nodeConf = conf.getNode();
ErgoClient ergoClient = RestApiErgoClient.create(nodeConf, null);
```

Using `ErgoClient` we can execute `lib-api/src/main/java/org/ergoplatform/appkit/ErgoClient.java` any block of code in the current blockchain context.

```java
String txJson = ergoClient.execute((BlockchainContext ctx) -> {
    // here we will use ctx to create and sign a new transaction
    // which then be sent to the node and also serialized into Json
});
```

The lambda passed to `execute` is called when the current blockchain context is loaded from the node. This is where we shall put our application logic.

We start with some auxiliary steps.

```java
// access wallet embedded in Ergo node
ErgoWallet wallet = ctx.getWallet();

// calculate total amount of NanoErgs we need to create the new box 
// and pay transaction fees
long totalToSpend = amountToPay + Parameters.MinFee;

// request wallet for unspent boxes that cover required amount of NanoErgs
Optional<List<InputBox>> boxes = wallet.getUnspentBoxes(totalToSpend);
if (!boxes.isPresent())
    throw new ErgoClientException(
        "Not enough coins in the wallet to pay " + totalToSpend, null);
    
// create a so called prover, a special object which will be used for signing the transaction
// the prover should be configured with secrets, which are necessary to generate signatures (aka proofs)
ErgoProver prover = ctx.newProverBuilder()
    .withMnemonic(
            SecretString.create(nodeConf.getWallet().getMnemonic()),
            SecretString.create(nodeConf.getWallet().getMnemonicPassword()))
    .build();
```

Now that we have the input boxes to spend in the transaction, we need to create an output box with the requested `amountToPay` and the specific contract protecting that box.

```java
// the only way to create transaction is using builder obtained from the context
// the builder keeps relationship with the context to access necessary blockchain data.
UnsignedTransactionBuilder txB = ctx.newTxBuilder();

// create new box using new builder obtained from the transaction builder
// in this case we compile new ErgoContract from source ErgoScript code
OutBox newBox = txB.outBoxBuilder()
        .value(amountToPay)
        .contract(ctx.compileContract(
                ConstantsBuilder.create()
                        .item("freezeDeadline", ctx.getHeight() + newBoxDelay)
                        .item("pkOwner", prover.getP2PKAddress().pubkey())
                        .build(),
                "{ sigmaProp(HEIGHT > freezeDeadline) && pkOwner }"))
        .build();
```
Note, in order to compile `ErgoContract` from source, the `compileContract` method requires us to provide values for named constants which are used in the script.

If no such constants are used, then `ConstantsBuilder.empty()` can be passed.

In this specific case, we pass the public key of the `prover` for `pkOwner` placeholder of the script meaning the box can be spent only by the owner of the public key from the `wallet` section of `ergotool.json`.


Next, we create an unsigned transaction using all the data collected so far.

```java
// tell transaction builder which boxes we are going to spend, which outputs
// to create, amount of transaction fees and address for change coins.
UnsignedTransaction tx = txB.boxesToSpend(boxes.get())
        .outputs(newBox)
        .fee(Parameters.MinFee)
        .sendChangeTo(prover.getP2PKAddress()) // i.e. back to the wallet's pk
        .build();
```

And finally, we use `prover` to sign the transaction, obtain a new `SignedTransaction` instance and use context to send it to the Ergo node. 

The resulting `txId` can be used to refer to this transaction later and is not used here.

```java
SignedTransaction signed = prover.sign(tx);
String txId = ctx.sendTransaction(signed);
return signed.toJson(/*prettyPrint=*/true, /*formatJson=*/true);
```

As the last step, we serialize signed transactions into Json with pretty printing turned-on. 

Please see the [full source code](https://github.com/aslesarenko/ergo-appkit-examples/blob/master/java-examples/src/main/java/org/ergoplatform/appkit/examples/FreezeCoin.java) of the example.