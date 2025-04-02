---
tags:
  - contribute
  - development
  - build
  - ci
  - dependencies
  - bouncycastle
  - troubleshooting
  - guidelines
---

# Technical Contribution Guidelines

Contributing code to Ergo's core repositories (like `ergo`, `sigmastate-interpreter`, `sigma-rust`, `ergo-appkit`) involves adhering to certain technical standards and being aware of common build and dependency considerations. This guide provides pointers for developers looking to contribute technically.

## General Workflow

1.  **Find an Issue/Task:** Look for issues tagged `good first issue` or `help wanted` in the relevant GitHub repository. Check the [Bounties Board](bounties.md) for funded tasks. Discuss potential contributions in the development channels on [Discord](https://discord.gg/ergo-platform-668903786361651200).
2.  **Fork & Branch:** Fork the repository and create a new branch for your changes.
3.  **Develop & Test:** Write your code, adhering to the project's style guide (e.g., [Ergo Scala Style Guide](https://github.com/ergoplatform/ergo-scala-style-guide)). Add relevant unit and integration tests. Ensure all existing tests pass.
4.  **Submit Pull Request:** Push your changes to your fork and open a Pull Request (PR) against the main repository's appropriate branch (usually `master` or a specific release branch). Clearly describe the changes made and reference the issue number if applicable.
5.  **Code Review:** Project maintainers will review your PR, provide feedback, and potentially request changes. Respond to feedback and update your PR accordingly.
6.  **Merge:** Once approved, maintainers will merge your PR.

## Build & CI Troubleshooting

Continuous Integration (CI) systems (primarily GitHub Actions) are used to automatically build and test code upon PR submission. Occasionally, builds or tests might fail for reasons unrelated to your direct code changes.

*   **GitHub Actions Updates:** Workflows can sometimes break due to updates in the underlying GitHub Actions runners or referenced actions (e.g., `actions/checkout@v4`). Check the workflow logs (`.github/workflows/`) for errors related to action versions or syntax changes. Consult recent successful builds on the main branch for comparison.
*   **Flaky/Random Test Failures:** Distributed systems testing can sometimes exhibit intermittent failures due to timing, resource contention, or network issues within the CI environment.
    *   **Action:** Re-running the failed job often resolves transient issues. If failures persist, try running the specific tests locally with increased verbosity or logging to isolate the problem. Check for recent changes in related code that might have introduced race conditions or resource leaks. Report persistent flaky tests as issues.
*   **Dependency Conflicts/Plugin Issues:** Updates to dependencies or build tool plugins (e.g., SBT plugins) can sometimes introduce conflicts or breakages. Check the build logs for errors related to dependency resolution or plugin execution. Ensure your local build environment (SBT version, JDK version) matches the one used in CI.

## Dependency Management Guidelines

### BouncyCastle Variants

Several Ergo projects rely on the BouncyCastle cryptographic library. Be aware that different variants exist (e.g., `bcprov-jdk15on`, `bcprov-jdk15to18`, `bcprov-jdk18on`).

*   **Inconsistency Issue:** Historically, different projects within the ecosystem may have used inconsistent versions or variants. This can lead to classpath conflicts or subtle runtime issues if libraries depending on different variants are used together.
*   **Recommendation:** When adding or updating BouncyCastle dependencies, strive to use a consistent, modern variant across projects where feasible (e.g., the latest compatible `jdk18on` variant is often preferred over older `jdk15on` or ranged `jdk15to18` variants). Check the specific project's existing dependencies and contribution guidelines. If introducing a change, document the rationale. Using older variants might be necessary for compatibility with specific platforms (like older Android versions) but should be carefully considered.

### General Dependencies

*   Keep dependencies updated where possible, but test thoroughly after updates.
*   Minimize adding new dependencies unless necessary, especially in core libraries, to avoid bloating and potential conflicts.
*   Follow the specific dependency management practices of the repository you are contributing to (e.g., versions specified in `build.sbt`, `Cargo.toml`, `pom.xml`).

By following these guidelines and collaborating with the community, you can contribute effectively to the technical development of the Ergo ecosystem.
