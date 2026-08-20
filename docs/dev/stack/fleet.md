---
tags:
  - JavaScript
owner: docs
last_reviewed: 2026-08-20
source_repos:
  - repo: fleet-sdk/fleet
    branch: master
    paths:
      - README.md
  - repo: dungvn3000/ergo-fleet-sdk-example
    branch: main
    paths:
      - README.md
  - repo: paulmillr/noble-ciphers
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/fleet-sdk/fleet
  - https://github.com/fleet-sdk/fleet/pull/202
  - https://github.com/dungvn3000/ergo-fleet-sdk-example
  - https://github.com/paulmillr/noble-ciphers
---

# Fleet

[Fleet](https://fleet-sdk.github.io/docs/) lets you easily create Ergo transactions with a pure JS library.

- Easy to use
- Lightweight: [~12kB minified + gziped](https://bundlephobia.com/package/@fleet-sdk/core)
- Powerful: easily create complex transactions with a fluent API
- 100% code coverage
- Tree-shakeable

For common usage patterns and examples, see the [Fleet SDK Recipes](fleet-sdk-recipes.md).

Fleet handles Ergo wallet keys and transaction construction. If your JavaScript application also needs message encryption or symmetric ciphers around those keys, use a dedicated audited crypto library such as [noble-ciphers](https://github.com/paulmillr/noble-ciphers) rather than expecting Fleet to provide general-purpose encryption APIs.

September 2025 dev updates noted a Fleet build-tooling migration from `tsup` to `tsdown`, with IIFE browser bundles exported for direct browser use. For production apps, still prefer the package entrypoints documented by Fleet unless you specifically need a no-build browser integration.

July 2025 dev updates said Fleet `v0.10.0` added `AvlTree` serialization support. Later that month, Fleet added ErgoTree construction from `ergoc` JSON output in [fleet#202](https://github.com/fleet-sdk/fleet/pull/202).

## Examples

- **[Fleet Examples](https://github.com/fleet-sdk/fleet-by-example)**: Repository showcasing various Fleet SDK usage patterns. [`TS`]
- [ergo-fleet-sdk-example](https://github.com/dungvn3000/ergo-fleet-sdk-example): small TypeScript ErgoScript-by-example repository using Fleet SDK patterns.

/// details | DeepWiki Documentation
    {type: info, open: true}
For an alternative and potentially more detailed documentation source generated from the repository, explore the [Fleet SDK on DeepWiki](https://deepwiki.com/fleet-sdk/fleet/1-overview)
///
