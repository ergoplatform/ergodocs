---
tags:
  - Java
  - Scala
  - Kotlin
  - JavaScript
  - Python
  - Tutorial
---

# Ergo Platform Basic Starter Tutorial 

This tutorial will teach you the very basics of interacting with the ergo blockchain to receive
and send funds for multiple programming languages. For more in-depth information on the different
SDKs available, please refer to their specific pages.

## Import the SDK

Import the SDK for the build system you are using in your project.

=== "Gradle"

     ```bash
      implementation ("org.ergoplatform:ergo-appkit_2.12:5.0.0")
     ```

=== "Maven"

     
		<dependency>
			<groupId>org.ergoplatform</groupId>
			<artifactId>ergo-appkit_2.12</artifactId>
			<version>5.0.0</version>
		</dependency>
    

=== "SBT"

     
		tbd
    

=== "npm"

    ```bash 
      npm install @fleet-sdk/core    
    ```

=== "yarn"

    ```bash 
      yarn install @fleet-sdk/core    
    ```

=== "pip"

    ```bash
      pip install ergpy    
    ```

## Create keys and an address

Ergo Platform uses public key cryptography to ensure that every transaction is secure: every personal wallet has a keypair consisting of a public key and a secret key. The public key is always safe to share — other people need it to verify that you authorized a transaction. It's like an email address. 
The secret key, however, is private information that proves you own — and gives you access to — your private wallet. It's like a password, and you should never share it with anyone.

On Ergo, the secret key is usually a 15 words mnemonic seed phrase that is used to derive the internally used binary master key. From this master key, an infinite number of private and public keys can be derived with an index. So for every mnemonic seed phrase, there are existing multiple key pairs and addresses defined by an index. The main address is always at index 0. 

You can create this address from a mnemonic phrase the following way:

=== "Java"

    ```Java 
		String ergoAddress = Address.createEip3Address(
          index,
          NetworkType.MAINNET,
          SecretString.create(mnemonic),
          SecretString.empty(),
          false
        ).toString()
    ```
    

=== "Kotlin"

    ```java 
		val ergoAddress = Address.createEip3Address(
          index,
          NetworkType.MAINNET,
          SecretString.create(mnemonic),
          SecretString.empty(),
          false
        ).toString()
    ```
    

=== "Scala"

    ```scala
    val ergoAddress = Address.createEip3Address(
      index, 
      NetworkType.MAINNET, 
      SecretString.create(mnemonic),
      SecretString.empty(),
      false
    ).toString
    ```

=== "JavaScript"

     
      tbd
    

=== "Python"

    ```python
    from jpype import java
    from ergpy import helper_functions, appkit

    ergo = appkit.ErgoAppKit(node_url=node_url)
    ergo_address = helper_functions.get_wallet_address(ergo=ergo, amount=1, wallet_mnemonic=mnemonic)[0]

    # Proper exit()
    helper_functions.exit()
    ```

Having the string representation of the address for your mnemonic, you can already receive payments.

## Sending payments

If you created an address like described above and sent some ERG to it, you can send payments from this address.

Sending payments on Ergo is always done within a transaction. Ergo follows Bitcoin's model: A transaction is a set of input boxes and output boxes. The input boxes are spent within a transaction, and output boxes are created. For a transaction to be valid, it must be signed with 
the private key of the address of the input boxes.

So sending payments needs the following steps to be done:

- Search for unspent boxes covering the amount to be send
- Create an unsigned transaction with the input boxes found and output boxes for the payment recipient
- Sign the transaction
- Submit the transaction to the network

Luckily, our SDKs help you by providing high-level methods for this common task.

=== "Java"

    ```Java
    ErgoClient ergoClient = RestApiErgoClient.create(nodeUrl, NetworkType.MAINNET, "", RestApiErgoClient.getDefaultExplorerUrl(NetworkType.MAINNET));

    //address receiving the tx
    Address recipient = Address.create(recipientAddress);
    //amount to send
    long amountToSend = 1000L * 1000L * 1000L // 1 ERG in nanoERGs
    ergoClient.execute((BlockchainContext ctx) -> {
        ErgoProver prover = ctx.newProverBuilder().withMnemonic(
          SecretString.create(mnemonic),
          SecretString.empty(),
          false
        ).withEip3Secret(0).build()

        String txId = BoxOperations.createForProver(prover, ctx)
                .withAmountToSpend(amountToSend)
                .withInputBoxesLoader(new ExplorerAndPoolUnspentBoxesLoader().withAllowChainedTx(true))
                .send(recipient);
    });
    ```
    

=== "JavaScript"

    ```JavaScript
    import { TransactionBuilder, OutputBuilder } from "@fleet-sdk/core";

    new TransactionBuilder(creationHeight);

    type Box = {
      boxId: string;
      value: string | bigint;
      assets: { tokenId: string; amount: string | bigint }[];
      ergoTree: string;
      creationHeight: number;
      additionalRegisters: NonMandatoryRegisters;
      index: number;
      transactionId: TransactionId;
    };

    new TransactionBuilder(creationHeight)
      .from(inputs)
      .withDataFrom(dataInputs);

    new TransactionBuilder(creationHeight)
      .from(inputs)
      .to(
        new OutputBuilder(
          "1000000", // amount of nanoergs
          "9gNvAv97W71Wm33GoXgSQBFJxinFubKvE6wh2dEhFTSgYEe783j" // recipient address
        )
    );
    ```


    

=== "Python"


    ```py
    from jpype import java
    from ergpy import helper_functions, appkit

    ergo = appkit.ErgoAppKit(node_url=node_url)
    amount_send = 1 # 1 ERG

    helper_functions.simple_send(ergo=ergo, amount=amount_send, wallet_mnemonic=mnemonic,
      receiver_addresses=recipient)

    # Proper exit()
    helper_functions.exit()
    ```
    


## Receiving payments

You don’t actually need to do anything to receive payments: if a payer makes a successful 
transaction to send assets to you, those assets will automatically be added to your wallet.

However, you may want to keep an eye out for incoming payments. For this, you can make use of
our [Ergo Explorer API](https://api.ergoplatform.com/api/v1/docs/). The API's interfaces are 
shipping with some of our SDKs.

=== "Java"

    ```java 
        // appkit ships with a Retrofit interface
        DefaultApi ergoApiService = Retrofit.Builder()
            .baseUrl(RestApiErgoClient.defaultMainnetExplorerUrl)
            .addConverterFactory(GsonConverterFactory.create())
            .build().create(DefaultApi.class)

        // call methods on ergoApiService here
    ```
    

=== "JavaScript"

     
      tbd    
    

=== "Python"

     
      tbd
    
