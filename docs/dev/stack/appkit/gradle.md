---
tags:
  - Java
---

# Gradle 


Gradle is a build tool used for many JVM languages and frameworks. You can use it to set up and build Java and Kotlin projects, both client-side (for desktop or Android) or server-side applications (for example Spring).


## Setting up the Gradle project

The first step is setting up a plain Gradle project. How exactly this is done depends on the platform or framework you want to base on.

* Android: Install Android Studio and create a new project with your preferred language
* Spring: Use the [Spring Initializr](https://start.spring.io/) to create a new project with your preferred language, don't forget to select Gradle. Open the project in the IDE of your choice
* For other frameworks, refer to their setup or starter guide

When that is done, you will find one or more `build.gradle` files that define parameters of your project, most important the libraries your project depends on. Search for a `dependencies` block (for Android, it is in `app/build.gradle`, for Spring in the root-level file). You need to add appkit here. Don't get confused with the `dependencies` block inside `buildscripts`, that's not for the project dependencies, but for dependencies Gradle needs to build the project.

For **desktop and server-side applications**, it is just one line to add.

    implementation ('org.ergoplatform:ergo-appkit_2.11:4.0.6')

When you resync your project now, Gradle fetches Appkit and all needed libraries and add them to your classpath.

Things are a bit more complicated when targeting **Android**. Some older Android versions run an older version of Java, and while Appkit itself is compatible, some of the libraries it uses are not. So you need some more steps to do:

Make sure core library desugaring is enabled by checking if the app's `build.gradle` file contains the needed dependency and option [as described here](https://developer.android.com/studio/write/java8-support#library-desugaring)

Additionally, you have to tell gradle to exclude the libraries that are not compatible with Android, but to use compatible versions instead. That is done by changing the line above like this:

    implementation ('org.ergoplatform:ergo-appkit_2.11:4.0.6') {
        exclude group: 'org.bouncycastle', module: 'bcprov-jdk15on'
        exclude group: 'org.bitbucket.inkytonik.kiama', module: 'kiama_2.11'
    }
    // kiama needs an own build for JRE7 compatibility
    implementation "com.github.MrStahlfelge.kiama:core_2.11:2.1.1"
    implementation "com.github.MrStahlfelge.kiama:library_2.11:2.1.1"
    implementation "org.bouncycastle:bcprov-jdk15to18:1.66"

And there you go!

## What to start with
Now you have Appkit enabled in your project, but what can you do now? Appkit provides methods for the following tasks:

* Fetch data from Ergo Explorer API
* Interact with Ergo Node, both public and private methods
* Build transactions and sign them
* Helper methods to handle cryptographics like calculating PK addresses from secrets

So it is up to your plans what you will use! That's why here is just a brief starter on these topics

### Ergo Explorer API
All data available on the [Ergo Explorer](https://explorer.ergoplatform.com/en/) is available through an API as well. Appkit ships with classes defining this API to use with [Retrofit](https://square.github.io/retrofit/). Get started with the following Kotlin code:

    val retrofit = Retrofit.Builder()
                .baseUrl(RestApiErgoClient.defaultMainnetExplorerUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .build()

    val ergoApiService = retrofit.create(DefaultApi::class.java)

You can call Explorer API methods on the ergoApiService now. Check out Retrofit's documentation on how to interact with it.

### Interact with Ergo node, build transactions and sign them
While Ergo Explorer is a central service to request information without the need to have the full blockchain, an Ergo node is part of the decentralized blockchain network. The node offers methods to the public, for example submitting a new transaction, while there are also private methods for its owner only to be used with an API key. These methods can be accessed through a `BlockchainContext` that you can obtain with the following code:

        val ergoClient = RestApiErgoClient.create(
            nodeApiAddress,
            NetworkType.MAINNET,
            "", // for private methods, give API key here
            RestApiErgoClient.defaultMainnetExplorerUrl
        )
        ergoClient.execute { ctx: BlockchainContext ->
            // do something here with the blockchain context
        }

How to obtain the node address? A few known peers [are listed on the node configuration file](https://github.com/ergoplatform/ergo/blob/e68ce6180b13bffb024cf9e26c7c16a7be70a22c/src/main/resources/mainnet.conf#L43). Make sure to use the correct port to connect to the node API, it is 9053 for Mainnet (e.g. http://213.239.193.208:9053/).

Of course, the most interesting part here is to sign and send transactions with smart contracts. See below for examples.

### Helper methods
Appkit provides a lot of helper methods to ease a developer's life and not reinvent the wheel that already is in use. For example, you can construct an Ergo address from a mnemonic, or an ErgoTree from an address. Check out the following classes and their inline documentation: `Address`, `BoxOperations`, `ErgoProverBuilder`, `Mnemonic`, `Parameters`

## Examples

These examples will help you get started and understand the concepts better.

- For sending ERG, check out the [code used in the Android wallet](https://github.com/MrStahlfelge/ergo-wallet-android/blob/0e4e10d5ad18453ca43948514d73255c567fefd1/app/src/main/java/org/ergoplatform/android/ErgoFacade.kt#L86).
- An example for a very simple smart contract freezing an amount of ERG to not to be spent before some time expired can be found on [Appkit's main readme](https://github.com/ergoplatform/ergo-appkit/blob/develop/README.md#using-from-java).
- The [ergoscript by example](https://github.com/ergoplatform/ergoscript-by-example) repository contains two additional smart contract examples (not using Appkit).
- How you can mint new tokens can be seen in [ergo-dex repo](https://github.com/ergoplatform/ergo-dex/blob/50596a92a465f52904b5d8015e8ae0d62e414176/src/main/scala-2.12/org/ergoplatform/dex/commands/IssueTokenCmd.scala).
- [ErgoPay Server example](https://github.com/MrStahlfelge/ergopay-server-example/blob/master/src/main/java/org/ergoplatform/ergopay/ErgoPaySampleController.java) builds transactions for minting and burning token and spending a specific box.
