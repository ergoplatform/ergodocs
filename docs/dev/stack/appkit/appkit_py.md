# Using AppKit from Python
To use Appkit from Python, you need to bridge to a JVM instance running the Appkit code. To do so, we use [JPype](https://github.com/jpype-project/jpype) for this guide. It is presumed that you've already set up a proper Python environment.

### General setup

Install jpype in your Python environment by typing

    pip install JPype1

(or pip3 when using Python3).

For Appkit to work on your system, you'll need a JDK8 or JDK11 installed and you need the appkit "fat jar", that means a jar containing all dependencies to add to your project. You can find this jar on the releases page or build it yourself. ([How to build the fat jar](https://github.com/ergoplatform/ergo-appkit#building-the-appkit-jar-file))

The general wrapper for your Python code is then something like this:

```python
# Enable Java imports
import jpype.imports

# Pull in types
from jpype.types import *

# Launch the JVM
jpype.startJVM()
# Add Appkit fat jar to JVM classpath
jpype.addClassPath("ergo-appkit-fat-jar.jar")

import java.lang

# ----> add your ergo related code here

jpype.shutdownJVM()
```

You have two options to implement your ergo related code: You can do everything in your Python code 
and call all necessary Appkit methods from Python, or you create an own Java/Kotlin/Scala project and
implement your necessary logic in these languages providing some methods for simpler use from Python.

A general recommendation which approach is more useful can't be given - while Appkit is a bit more easier
to use from JVM, you most likely are more comfortable coding Python if you read this guide, so you might
prefer using Python.

A downside is that code completion is not working for Appkit methods within Python (or at least there was
no way found so far). The good news is that most things work pretty straightforward so code completion is
not a must have.

### Construct an Ergo transaction

Let's take a look on how to construct an ergo transaction in Appkit. In Java this is done the following way:

        // file header
        import org.ergoplatform.appkit.Address;
        import org.ergoplatform.appkit.BoxOperations;
        import org.ergoplatform.appkit.NetworkType;
        import org.ergoplatform.appkit.RestApiErgoClient;

        // within a method
        NetworkType networkType = NetworkType.TESTNET;
        RestApiErgoClient.create(
                "http://213.239.193.208:9052/", // use your node or a public node here
                networkType,
                "",
                RestApiErgoClient.getDefaultExplorerUrl(networkType)
        ).execute(ctx -> {
            ErgoTreeContract contract = recipient.toErgoContract();
            UnsignedTransaction unsignedTransaction = BoxOperations.createForSender(sender)
                    .withAmountToSpend(amountToSend)
                    .putToContractTxUnsigned(ctx, contract);

            // reduce the transaction for use with ErgoPay
            return ctx.newProverBuilder().build().reduce(unsignedTransaction, 0);
        });

How to translate this to Python?

At first we need to declare all used imports. These can be done straightforward by looking at the Java imports:

    from org.ergoplatform.appkit import RestApiErgoClient, NetworkType, BoxOperations, Address

Constructing the `ErgoClient` is also a straightforward copy from the Java code:

    network_type = NetworkType.TESTNET
    node_client = RestApiErgoClient.create("http://213.239.193.208:9052/", network_type, "",
                                           RestApiErgoClient.getDefaultExplorerUrl(network_type))

To execute code within a `BlockchainContext`, a lambda function is used within Java:

    ergoClient.execute(ctx -> {
        // ....
        });

Internally, lambda functions in Java are nothing more than an anonymous class implementing a special interface.
So to adapt this construct into Python, we need to define such a class implementing this interface. JPype provides
special annotations for this:

    @JImplements(java.util.function.Function)
    class BlockchainContextExecutor(object):

        @JOverride
        def apply(self, blockchain_context):
            # use blockchain_context here
            return something

Putting this all together, we can use the following code to construct and a 1 ERG roundtrip transaction, convert it
into a `ReducedTransaction` and use Python features for Base64 encoding. This way, we've built the juicy part of an
ErgoPay Request in Python.

```python
import base64
from jpype import JImplements, JOverride

# Enable Java imports
import jpype.imports

# Pull in types
from jpype.types import *

# Launch the JVM
jpype.startJVM()
jpype.addClassPath("ergo-appkit-fat-jar.jar")

import java.lang

from org.ergoplatform.appkit import RestApiErgoClient, NetworkType, BoxOperations, Address


# this executor sends a 1 ERG roundtrip
@JImplements(java.util.function.Function)
class ReducedRoundTripExecutor(object):
    def __init__(self, address):
        self.address = address

    @JOverride
    def apply(self, blockchain_context):
        round_trip_address = self.address
        unsigned_tx = BoxOperations.createForSender(Address.create(round_trip_address),
                                                    blockchain_context).withAmountToSpend(
            1000 * 1000 * 1000).putToContractTxUnsigned(Address.create(round_trip_address).toErgoContract())
        return blockchain_context.newProverBuilder().build().reduce(unsigned_tx, 0)


def get_base64_reduced_tx(executor):
    network_type = NetworkType.TESTNET
    node_client = RestApiErgoClient.create("http://213.239.193.208:9052/", network_type, "",
                                           RestApiErgoClient.getDefaultExplorerUrl(network_type))
    reduced_tx = node_client.execute(executor)
    return base64.urlsafe_b64encode(reduced_tx.toBytes()).decode('utf-8')


# print base64 url encoded reduced transaction - this is the most interesting part of an ErgoPay request
print(get_base64_reduced_tx(ReducedRoundTripExecutor("3Wwxnaem5ojTfp91qfLw3Y4Sr7ZWVcLPvYSzTsZ4LKGcoxujbxd3")))


jpype.shutdownJVM()
```

### Minting a token

For minting a token, you can make use of your knowledge gained above and by using `Boxoperations.mintTokenToContractTxUnsigned()`.
This method takes another lambda for building the actual token, so this time we need two helper classes.

Building the token itself is easy: Eip4TokenBuilder provides all necessary methods to hide away complexity.

```python
# Import the Eip4TokenBuilder class from the ergoplatform library 
from org.ergoplatform.appkit.impl import Eip4TokenBuilder

# Define a helper class for the executor
@JImplements(java.util.function.Function)
class TokenBuilder(object):
    @JOverride
    # Define the apply function for the TokenBuilder class
    def apply(self, token_id):
        # Build a non-fungible picture token with Eip4TokenBuilder
        return Eip4TokenBuilder.buildNftPictureToken(token_id, 1, "Picture token", "Description", 0, bytearray(), "ipfs://...")

# Define the MintTokenExecutor class
@JImplements(java.util.function.Function)
class MintTokenExecutor(object):
    # Initialize the class with a provided address
    def __init__(self, address):
        self.address = address

    @JOverride
    # Define the apply function for the MintTokenExecutor class
    def apply(self, blockchain_context):
        # Set the round_trip_address to the class address
        round_trip_address = self.address
        # Create a BoxOperations object with the sender's address
        unsigned_tx = BoxOperations.createForSender(Address.create(round_trip_address), blockchain_context).withAmountToSpend(1000 * 1000).mintTokenToContractTxUnsigned(Address.create(round_trip_address).toErgoContract(), TokenBuilder())
        # Return the reduced unsigned transaction from the newProverBuilder
        return blockchain_context.newProverBuilder().build().reduce(unsigned_tx, 0)

# Print the reduced transaction from the MintTokenExecutor class
print(get_base64_reduced_tx(MintTokenExecutor("3Wwxnaem5ojTfp91qfLw3Y4Sr7ZWVcLPvYSzTsZ4LKGcoxujbxd3")))

```

This code defines two classes, `TokenBuilder` and `MintTokenExecutor`. The `TokenBuilder` class has a single apply function that creates a non-fungible picture token with `Eip4TokenBuilder.buildNftPictureToken`.

The `MintTokenExecutor` class has an `__init__` function to set the provided address and an apply function that creates a BoxOperations object with the provided address and calls `withAmountToSpend` to spend a specific amount of Ergo to mint the non-fungible picture token to the address. This transaction is unsigned, and the reduce function is used to reduce it to a format suitable for transmission.

The reduced unsigned transaction is then printed using `get_base64_reduced_tx`.


### Please note
You can find published Python artefacts here https://github.com/ergo-pad/ergo-python-appkit