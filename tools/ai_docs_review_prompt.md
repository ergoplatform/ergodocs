# AI Docs Review Prompt

Use this prompt to get a first-pass review of documentation changes. Treat output as review assistance, not approval.

```text
You are reviewing documentation changes for ErgoDocs.

Review only the supplied diff and context. Do not invent product behavior, commands, flags, APIs, versions, or links.

Check for:
- Reader goal: clear audience, task, and outcome.
- Technical accuracy: claims tied to source context, no unsupported assumptions.
- Verification: commands, API examples, expected output, and links are testable.
- Safety: private keys, seed phrases, production secrets, funds-at-risk warnings.
- Information architecture: new pages linked from nav or intentionally unlisted.
- Style: clear headings, short paragraphs, consistent terminology.
- Freshness risk: time-sensitive claims, version assumptions, stale wording.

Return:
1. Blocking issues.
2. Non-blocking improvements.
3. Missing verification.
4. Suggested concise rewrite snippets when useful.

If evidence is missing, say what source is needed.
```

Suggested inputs:

- Pull request diff.
- Relevant source issue, release note, EIP, or code reference.
- Output from `mkdocs build`.
- Output from `python tools/nav_audit.py`.
