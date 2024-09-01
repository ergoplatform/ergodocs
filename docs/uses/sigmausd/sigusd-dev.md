### Accessing SigmaUSD as a Developer

SigmaUSD is a decentralized stablecoin protocol on the Ergo blockchain. Developers can interact with SigmaUSD through various frameworks and approaches, such as Mosaik, AppKit, and Sigma-Rust. This tutorial provides a detailed guide on how to build new dApps that interact with SigmaUSD using these tools, with special focus on the mechanisms demonstrated in ErgoMix for robust integration.

---

### 1. **Accessing SigmaUSD through Mosaik**

Mosaik is a lightweight framework designed for building decentralized applications on Ergo. It provides an intuitive way to access and interact with SigmaUSD.

#### **Setup**

1. **Mosaik Integration**:
   - Mosaik uses the `AgeUsdService.kt` to interact with SigmaUSD. This service manages key operations such as fetching the current state of the AgeUSD bank and calculating exchange rates for SigmaUSD and SigmaRSV.

   ```kotlin
   // Fetching current bank details
   fun getAgeUsdBank(): AgeUsdBank {
       Thread.sleep(1000)
       return AgeUsdBank(340, 4184100, 623497)
   }

   // Calculating SigmaUSD exchange
   fun calcSigmaUsdExchange(sigmaUsdAmount: Long): AgeUsdExchangeInfo {
       val ageUsdBank = getAgeUsdBank()
       val ergAmount = ageUsdBank.sigUsdPrice * sigmaUsdAmount
       val feeAmount = kotlin.math.abs((ergAmount * 2) / 100)
       return AgeUsdExchangeInfo(
           ageUsdBank.sigUsdPrice,
           ergAmount,
           "${formatSigmaUsdAmount(sigmaUsdAmount)} x ${formatErgAmount(ageUsdBank.sigUsdPrice)} ERG",
           feeAmount,
           "2% AgeUSD bank fee",
           ergAmount + feeAmount
       )
   }
   ```

   - **Source Files**:
     - [AgeUsdService.kt](https://github.com/MrStahlfelge/mosaik-ageusddemo/blob/master/src/main/kotlin/org/ergoplatform/mosaik/example/ageusd/AgeUsdService.kt)
     - [AgeUsdController.kt](https://github.com/MrStahlfelge/mosaik-ageusddemo/blob/master/src/main/kotlin/org/ergoplatform/mosaik/example/ageusd/AgeUsdController.kt)

2. **User Interface**:
   - The Mosaik DSL is used to create user interfaces that interact with SigmaUSD. The example UI from the Mosaik demo application demonstrates how users can interact with the protocol.

   ```kotlin
   column(Padding.DEFAULT) {
       layout(HAlignment.JUSTIFY) {
           card(Padding.HALF_DEFAULT) {
               layout(HAlignment.JUSTIFY, VAlignment.CENTER) {
                   column(Padding.HALF_DEFAULT) {
                       label("Reserve ratio", LabelStyle.HEADLINE2)
                       label("${ageUsdBank.reserveRatio}%", LabelStyle.HEADLINE1)
                   }
               }
           }
       }
   }
   ```

---

### 2. **Accessing SigmaUSD through AppKit**

AppKit is a comprehensive framework for interacting with Ergo smart contracts and UTXO management, making it ideal for integrating SigmaUSD into your dApp.

#### **Setup**

1. **Setting Up Ergo Node**:
   - Set up an Ergo node and install the necessary dependencies. AppKit integrates seamlessly with Java or Kotlin-based projects, providing a powerful API to interact with the Ergo blockchain.

2. **Creating Transactions**:
   - Use AppKit to interact with the SigmaUSD contract. This involves creating transactions, managing UTXOs, and signing transactions before submitting them to the Ergo network.

   ```java
   ErgoClient client = RestApiErgoClient.create("http://node:9053/", NetworkType.MAINNET, "", "");
   UnsignedTransactionBuilder txB = client.getUnsignedTransactionBuilder();

   OutBoxBuilder outBoxB = txB.outBoxBuilder()
       .value(1000000L)  // set value in nanoERGs
       .contract(SigmaUSDContract);

   List<InputBox> inputs = txB.boxesToSpend(inputsList).build();
   UnsignedTransaction tx = txB.build();

   // Signing the transaction
   SignedTransaction signedTx = client.getWallet().sign(tx);

   // Sending the transaction
   String txId = client.getNode().sendTransaction(signedTx);
   ```

   - **Source Files**:
     - [AppKit Examples and Documentation](https://github.com/ergoplatform/ergo-appkit)

---

### 3. **Building New dApps with ErgoMix Approach**

ErgoMix demonstrates a robust mechanism for integrating SigmaUSD into backend services. It uses a service-oriented approach to handle transactions, ensuring privacy and seamless interaction with the SigmaUSD protocol.

#### **Setup**

1. **Understanding ErgoMix's Approach**:
   - ErgoMix utilizes services like `ErgoMixService.scala` to manage SigmaUSD interactions. This service constructs and sends transactions that involve SigmaUSD, embedding these operations within privacy-enhancing mix transactions.

   ```scala
   def createSigmaUsdTransaction(amount: Long): SignedTransaction = {
       val boxesToSpend = findBoxesToSpend(amount)
       val unsignedTx = createUnsignedTransaction(boxesToSpend, amount)
       signTransaction(unsignedTx)
   }
   ```

   - **Source Files**:
     - [ErgoMixService.scala](https://github.com/ergoMixer/ergoMixBack/blob/master/app/services/ErgoMixService.scala)

2. **Transaction Handling**:
   - The transaction handling involves fetching relevant UTXOs, creating unsigned transactions, and signing them before sending them to the Ergo network. ErgoMixService provides methods that can be adapted to new dApps, ensuring that SigmaUSD can be seamlessly integrated.

   - **Example Usage**:
     - Creating a transaction that involves SigmaUSD can follow the pattern used in ErgoMixService, where UTXOs are selected, transactions are built, and signed securely before submission.

---

### Conclusion

Developers have several robust tools at their disposal for integrating SigmaUSD into new or existing dApps. Mosaik provides a lightweight and user-friendly approach, while AppKit offers comprehensive access to the Ergo blockchain's capabilities. ErgoMix demonstrates how SigmaUSD can be embedded within a service-oriented architecture, making it an excellent guide for new developments.

By understanding these frameworks and their implementations, developers can choose the best method for their needs, ensuring seamless and efficient interaction with SigmaUSD on the Ergo blockchain.

For further reading and source code, please refer to the links provided in each section above.