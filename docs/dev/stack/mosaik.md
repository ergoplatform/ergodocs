---
title: Mosaik
description: Overview of Ergo Mosaik, a JSON-based UI system for Ergo dApps.
tags:
  - development
  - dapp
  - kotlin
  - wallet
owner: docs
last_reviewed: 2026-05-28
source_repos:
  - repo: MrStahlfelge/mosaik
    branch: develop
    paths:
      - README.md
      - backend-demo
      - backend-demo-kotlin
source_of_truth:
  - https://github.com/MrStahlfelge/mosaik
---

# Mosaik

Mosaik is a UI system for Ergo dApps. It uses JSON served over a REST API so wallet apps, desktop debuggers, or browser executors can render dApp interfaces without each dApp building a separate native client.

For current hands-on material, use the maintained tutorial pages:

| Goal | Page |
| --- | --- |
| Understand the model | [Mosaik Intro](intro.md) |
| Build a simple UI | [A Simple UI](tutorial2.md) |
| Process user input | [Processing Data](tutorial3.md) |
| Add ErgoPay flows | [ErgoPay UI](tutorial4.md) |
| Run in web browsers | [Web UI](tutorial5.md) |
| Dockerize and deploy | [Deployment](mosaik-docker-flux.md) |
| Study examples | Example Apps page in this section |

## When to Use It

Mosaik fits dApps that want wallet-rendered UI, Kotlin/JVM backend code, ErgoPay-style signing flows, or reusable UI definitions that can run across executors.

Use a normal web frontend instead when you need full control over visual styling, pixel-level layout, or browser-only wallet connector flows.

## Related Pages

- [Frameworks](frameworks.md)
- [Kotlin](kotlin.md)
- [AppKit](appkit.md)
- [ErgoPay](ergo-pay.md)
- [dApp Connector](dApp.md)
