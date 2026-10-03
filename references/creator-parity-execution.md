# Plugin Creator Parity Execution Contract

Plugin Builder targets functional coverage of the baseline Plugin Creator workflows while retaining its own broader architecture/evaluation system.

## Baseline lifecycle actions

When the host exposes the corresponding authenticated lifecycle actions, Plugin Builder may use them as execution adapters:

- **Create private plugin** — install one validated standalone ZIP/tar package and retain plugin/release IDs.
- **Inspect metadata** — read exact plugin identity, version, scope, discoverability, and current release.
- **Inspect files** — list/read current text files for focused edits; page large inventories.
- **Retrieve archive** — use current or historical full archive only when binary/large/history work requires it.
- **List releases** — inspect release history without confusing attachment order with semantic-version order.
- **Guarded update** — update the exact editable plugin using the observed current release ID; preserve audience/source/unrelated files.
- **Submission preparation** — prepare public upload separately from private/workspace source; collect truthful listing/review/publication evidence and keep draft/review/publish states distinct.

These actions are **host privileges**, not portable Agent Plugin capabilities. Plugin Builder must never invent them. If unavailable, finish all source/build/package/evaluation work and return `NO_MUTATION_ADAPTER` or `PACKAGE_READY`.

## Creation routes

Plugin Builder must cover:
1. skills-only plugins;
2. existing remote MCP servers;
3. local stdio plugins;
4. MCP Apps/UI;
5. OpenAI Extensions where useful;
6. cloud-hosted MCP/App architecture when a real deployment capability exists;
7. existing managed/Site/Git sources without duplicating ownership.

Unlike a fixed creator template, route selection is preceded by contract + architecture search when ambiguity is material.

## Update routes

Resolve the source that owns the change before editing:
- standalone account package → account-source adapter;
- Site-hosted plugin → Site source;
- local plugin → local directory and local install/reload;
- separately hosted MCP/App → server/UI repository and deployment;
- Git-managed plugin → Git/release source;
- public submission draft → submission lifecycle rules.

## Verification after mutation

Creation/update success is not sufficient evidence of working behavior. When possible:
1. read back metadata/version/release;
2. read back changed files;
3. verify MCP reachability separately;
4. verify auth/connection separately;
5. run a harmless representative tool/workflow smoke test;
6. render UI when UI changed;
7. report unverified layers explicitly.

## Parity-plus capabilities

Plugin Builder adds:
- candidate architecture generation;
- feasibility filtering and dominance pruning;
- build-versus-reuse reasoning;
- failure-mode simulation before implementation;
- adversarial prompt-injection/authorization evaluation;
- deterministic native scaffold/validate/package pipeline;
- repair-by-root-cause with regression memory;
- installation read-back/smoke verification;
- explicit comparative benchmark rather than unmeasured superiority claims.
