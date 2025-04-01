---
tags:
  - Java
  - Scala
  - Kotlin
---
# Appkit



[Ergo Appkit](https://github.com/aslesarenko/ergo-appkit) is a library for polyglot development of Ergo Applications based on [GraalVM](https://www.graalvm.org/).

It is a thin wrapper around core components provided by the ErgoScript interpreter and Ergo protocol implementations which are written in Scala. It is published on [maven repository](https://mvnrepository.com/artifact/org.ergoplatform/ergo-appkit) and cross-compiled to both Java 7 and Java 8+ jars.


**AppKit provides methods for the following:**

- Fetch data from Ergo Explorer API
- Interact with Ergo Node, both public and private methods
- Build transactions and sign them
- Helper methods to handle cryptographic like calculating PK addresses from secrets


Using Appkit, Ergo applications can be written in one of the languages supported by GraalVM (i.e. Java, JavaScript, C/C++, Python, Ruby, R) and using this library, applications can communicate with Ergo nodes via unified API and programming model provided by Appkit. In addition, Appkit based Ergo applications can be compiled into native code using native-image ahead of time compiler and then executed without Java VM with very fast startup time and lower runtime memory overhead compared to a Java VM. This is an attractive option for high-performance, low-latency microservices.


## Tutorials

::cards::

[
  {
    "title": "General Example",
    "content": "",
    "url": "appkit/tutorial.md"
  },
  {
    "title": "🔗 AppKit By Example",
    "content": "Follow this example to create and programmaticaly send a transaction.",
    "url": "https://www.youtube.com/watch?v=Md5s-XV6-Hs"
  },
  {
    "title": "ErgoPay Example",
    "url": "../wallet/payments/ergopay/ergo-pay.md"
  },
  {
    "title": "Gradle",
    "url": "appkit/gradle.md"
  },
  

]

::/cards::



## Videos

- [AppKit by Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs)

## Code examples

- [Appkit Examples](https://github.com/aslesarenko/ergo-appkit-examples)
- [Testing Ergo Contracts Off-chain](https://github.com/anon-real/contract-testing)


## How-to Guides

-  [Ergo Android](https://github.com/aslesarenko/ergo-android) application that demonstrates how Ergo Appkit can be used to develop Ergo applications running on Android.

## References

- [ErgoTool](https://github.com/aslesarenko/ergo-tool) | A Command Line Interface for Ergo based on Appkit and [GraalVM](https://www.graalvm.org/) native-image. Read the [introduction and overview](https://ergoplatform.org/en/blog/2019_12_31_ergo_tool/).
