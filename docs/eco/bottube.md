---
title: BoTTube
description: AI-native video platform with Ergo bridge integration work.
tags:
  - ecosystem
  - applications
  - AI
  - video
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: Scottcjn/bottube
    branch: main
    paths:
      - README.md
      - ergo_bridge_blueprint.py
source_of_truth:
  - https://github.com/Scottcjn/bottube
  - https://www.bottube.ai
---

# BoTTube

[BoTTube](https://www.bottube.ai) is an AI-native video platform for humans and agents to publish, curate, and interact with video content. The project describes itself as part of the RustChain DePIN ecosystem and emphasizes "Proof of Physical AI" for some in-house content generation.

The platform is not Ergo-specific, but the public repository includes an Ergo bridge blueprint for deposit verification and address handling through Ergo Explorer APIs.

## Ergo Integration

The Ergo bridge blueprint covers:

- deposit verification through Ergo Explorer;
- P2PK address handling;
- ERG-to-RTC exchange-rate handling for the platform integration.

Treat the bridge code as project-specific integration work, not a general bridge standard. Review the upstream repository before reusing any contract, exchange-rate, or deposit-verification logic.

## Links

- [BoTTube live platform](https://www.bottube.ai)
- [BoTTube repository](https://github.com/Scottcjn/bottube)
- [Ergo bridge blueprint](https://github.com/Scottcjn/bottube/blob/main/ergo_bridge_blueprint.py)
