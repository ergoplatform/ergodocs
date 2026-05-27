---
title: Ergo Agent SDK
description: Python SDK for AI agents interacting with Ergo.
tags:
  - Python
  - AI
  - agents
  - SDK
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: a-shannon/ergo-agent-sdk
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/a-shannon/ergo-agent-sdk
  - https://ergo-agent-sdk.readthedocs.io/
---

# Ergo Agent SDK

[Ergo Agent SDK](https://github.com/a-shannon/ergo-agent-sdk) is a Python SDK for connecting LLM agents and automation frameworks to Ergo workflows. The project targets agent stacks such as Claude, GPT-based systems, LangChain, CrewAI, and AutoGPT-style tools.

## Scope

The SDK is designed around agent actions such as:

- reading wallet balances;
- fetching prices;
- interacting with Spectrum DEX;
- minting stablecoins;
- bridging assets;
- applying safety guardrails before autonomous actions.

The project frames Ergo as useful for agents because eUTXO transactions are deterministic, can be built offline, and avoid gas-auction behavior. Those properties can make transaction outcomes easier for agents to reason about before broadcasting.

## Safety Notes

Agent automation should be treated as high risk. Use explicit spending limits, testnet flows, narrow API permissions, and human approval for irreversible actions. Do not expose wallet secrets or node API tokens to generic agent prompts.

## Links

- [Ergo Agent SDK repository](https://github.com/a-shannon/ergo-agent-sdk)
- [Ergo Agent SDK documentation](https://ergo-agent-sdk.readthedocs.io/)
