---
tags:
  - Java
  - Scala
  - Kotlin
owner: docs
last_reviewed: 2026-06-15
source_repos:
  - repo: ergoplatform/ergo-appkit
    branch: develop
    paths:
      - README.md
      - appkit/src
source_of_truth:
  - https://github.com/ergoplatform/ergo-appkit
  - https://github.com/ergoplatform/ergo-appkit/releases/tag/v6.0.0
---
# Appkit

## Overview

[Ergo Appkit](https://github.com/ergoplatform/ergo-appkit) is a library for polyglot development of Ergo applications based on [GraalVM](https://www.graalvm.org/).

## Recent updates

- `Jun 7`: [AppKit v6.0.0](https://github.com/ergoplatform/ergo-appkit/releases/tag/v6.0.0) was released on top of SigmaSDK 6.0.x.
- The release includes the [PR #253](https://github.com/ergoplatform/ergo-appkit/pull/253) EIP-50 upgrade work, Sigma 6.0 alignment, and prover-evaluated tests so contract tests can exercise newer Sigma features consistently.
- AppKit 6 compiles Sigma 6 scripts as ErgoTree v3 when the context has `blockVersion >= 4`, while preserving the legacy v5 path for older contexts. Its Sigma 6 test coverage includes bitwise/shift operations, `serialize`, `deserializeTo`, `fromBigEndianBytes`, `startsWith`, lazy `getOrElse`, `Box.getReg`, `Header.checkPow`, unsigned-bigint operations, and context-extension conversion behavior.

It is a thin wrapper around core components provided by the ErgoScript interpreter and Ergo protocol implementations which are written in Scala. It is published on [maven repository](https://mvnrepository.com/artifact/org.ergoplatform/ergo-appkit) and cross-compiled to both Java 7 and Java 8+ jars.

**AppKit provides methods for the following:**

- Fetch data from Ergo Explorer API
- Interact with Ergo Node, both public and private methods
- Build transactions and sign them
- Helper methods to handle cryptographic like calculating PK addresses from secrets

Using Appkit, Ergo applications can be written in one of the languages supported by GraalVM (i.e. Java, JavaScript, C/C++, Python, Ruby, R) and using this library, applications can communicate with Ergo nodes via unified API and programming model provided by Appkit. In addition, Appkit based Ergo applications can be compiled into native code using native-image ahead of time compiler and then executed without Java VM with very fast startup time and lower runtime memory overhead compared to a Java VM. This is an attractive option for high-performance, low-latency microservices.

## Tutorials

::cards::

[{
    "title": "General Example",
    "content": "",
    "url": "appkit/tutorial.md"
  },
  {
 "title": " AppKit By Example",
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
 }]

::/cards::

## Videos

- [AppKit by Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs)

## Code examples

- [Appkit Examples](https://github.com/aslesarenko/ergo-appkit-examples)
- [Testing Ergo Contracts Off-chain](https://github.com/anon-real/contract-testing)

## How-to Guides

- [Ergo Android](https://github.com/aslesarenko/ergo-android) application that demonstrates how Ergo Appkit can be used to develop Ergo applications running on Android.

## References

- [ErgoTool](https://github.com/aslesarenko/ergo-tool) | A Command Line Interface for Ergo based on Appkit and [GraalVM](https://www.graalvm.org/) native-image. Read the [introduction and overview](https://ergoplatform.org/en/blog/2019_12_31_ergo_tool/).
