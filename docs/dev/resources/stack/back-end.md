# Back-end

This page provides an overview of the tools used to interact with the Ergo blockchain. Developers can use these tools to read data from the blockchain, compute using that data and create transactions to be broadcast. Each tool requires the developer to "program" in some language.

Users of AppKit will usually write Scala code (although AppKit supports many other languages). HDF users will need to write Rust code, allowing it to be used across platforms. (The HDF also provides some additional abstractions on top of the original ergo API). JDE users will have to write JSON.

- [Appkit](appkit.md)
- [Headless dApp Framework](headless.md)
- [JDE](jde.md)

## HDF vs AppKit

HDF is based on Rust

Appkit, on the other hand, reflects the Ergo programming model and provides Java friendly interfaces to interact with Ergo.

There is also [JS SDK](https://github.com/ergolabs/ergo-dex-sdk-js) from Ergo Labs
