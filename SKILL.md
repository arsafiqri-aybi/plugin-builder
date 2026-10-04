---
name: plugin-builder
description: Design, build, audit, repair, validate, package, create, inspect, update, install when supported, migrate, and prepare AI plugins for release. Use when the user wants a new plugin or changes to an existing plugin, including skills, MCP servers/tools, MCP Apps/UI, extensions, authentication, security, testing, deployment, installation, release history, migration, or public submission readiness. Do not trigger merely to use a plugin or perform the plugin's target-domain task.
---

# Plugin Builder

Create the smallest plugin architecture that can reliably complete the user's job, prove the properties that matter, and carry the result through the requested lifecycle as far as the current host actually permits. Plugin Builder is a specialist builder: its output is a plugin, a verified plugin change, a validated install/release artifact, or a truthfully reported lifecycle state.

## 1. Establish the plugin contract

Identify the user job, target users, supported and unsupported intents, input/output contracts, external systems, authority boundaries, target hosts, distribution mode, critical quality gates, source ownership, and evidence required for completion. Ask only for information that materially changes architecture, authorization, or public claims; otherwise make reversible assumptions and continue.

For nontrivial work, use `references/build-workflow.md` and load relevant neurons from `knowledge/README.md`. Do not load all 168 neurons by default.

## 2. Search architecture when the choice matters

For each capability decide whether it belongs in a Skill, MCP tool/server, resource, prompt, MCP App, OpenAI Extension, backend/storage layer, reused external service, or nowhere. When several materially different topologies are feasible, use `references/architecture-search.md`: generate a small candidate set, reject infeasible routes, prune dominated designs, simulate critical failures, and select the smallest route that can pass the acceptance floor.

Support skills-only, existing remote MCP, local stdio, MCP App/UI, Extension, managed/Site/Git-owned, and cloud-hosted routes when the required real host/deployment capability exists. Do not force every request into one template.

Treat current surface support, SDK APIs, schema versions, submission rules, and product limits as dynamic facts. Recheck authoritative current sources before relying on them for release decisions.

## 3. Build a canonical source, not a disposable scaffold

Start from a portable root `plugin.json` package and add only components required by the selected architecture. Use repository tooling when local execution is available:

- `scripts/init_plugin.py` for a minimal portable scaffold;
- `scripts/validate_plugin.py` for package/component validation;
- `scripts/package_plugin.py` for deterministic packaging;
- `scripts/audit_plugin_package.py` for an additional static secret/symlink audit;
- `scripts/build_chatgpt_plugin.py` for the reproducible ChatGPT Plugin Builder package.

Compatibility overlays are derived from canonical source; they do not become an independent source of truth. Generate structure from the selected topology rather than a maximal starter template.

## 4. Build contracts the model and server can both enforce

Design goal-shaped tools with unambiguous names/descriptions, strict schemas, stable identifiers, useful structured results, truthful annotations, and explicit error semantics. Enforce authentication and authorization on the server for every private or consequential request. The model is not an access-control boundary.

Classify side effects and design retry/idempotency/concurrency behavior before exposing writes. If the status of a prior write is unknown, inspect durable state before retrying.

## 5. Build security, privacy, reliability, and UX into the architecture

Map trust boundaries and treat user input, retrieved documents, webpages, tool results, and external data as untrusted content. Prevent untrusted content from granting authority or steering privileged actions. Apply least privilege, input validation, output handling, secret management, tenant isolation, safe logging, and fail-closed behavior where authorization or integrity is uncertain.

MCP Apps and host Extensions are progressive enhancements. UI-enabled tools must still return useful model-visible results when UI is unavailable. Design visible state, correction, control, accessibility, error recovery, and graceful degradation. Use `references/security-gates.md` for consequential/data-sensitive plugins.

## 6. Verify by property, then repair by root cause

Use deterministic validation for manifests/schemas/packages; contract tests for tools; auth/security tests for trust boundaries; host tests for discovery/UI; and end-to-end user-job evaluations for behavior. Separate static validity, deterministic tests, model-behavior evaluations, human review, and production telemetry.

Every fixed defect should gain a focused regression case. Classify the failure before patching. Re-open architecture search only when the failure is structural.

## 7. Execute the complete plugin lifecycle

Use `references/creator-parity-execution.md` and `references/installation-adapters.md` for create/inspect/update/install/history work.

When the current host exposes authenticated lifecycle actions, Plugin Builder may use them to:
- create one validated private plugin from a completed archive;
- resolve exact editable plugin identity and metadata;
- inspect current text files;
- retrieve current or historical full archives when necessary;
- list releases/history;
- update the exact plugin with the observed current-release concurrency guard.

These are host privileges, not capabilities created by instructions. Never invent a lifecycle action, endpoint, account permission, plugin ID, release ID, or successful mutation. If the action is unavailable, finish all source/build/package/evaluation work and report `NO_MUTATION_ADAPTER` or `PACKAGE_READY`.

Creation must avoid duplicates. Updates must preserve identity, scope, audience, hosting, data, unrelated files, and source ownership. Account-package overlay semantics must not be mistaken for file deletion support.

## 7.5. Convenience command aliases

Use `references/command-layer.md` for concise creator-style commands such as:

```text
create_personal_plugin(mcp_url="https://example.com/mcp")
```

Treat these as intent aliases, not literal host APIs. Normalize them into the canonical existing-remote-MCP build flow: validate URL → optionally probe MCP with a real MCP-capable action → generate minimal `plugin.json` + `mcp.json` → validate/audit → check duplicate/source ownership → discover real host create adapter → create from archive when available → read back → verify connection/auth/smoke separately. Never invent a `create_personal_plugin` tool or pass the MCP URL directly to an archive-only create action.

## 7.6. Self-update without Plugin Creator dependency

Use `references/self-update.md` when the user asks Plugin Builder to update itself. The canonical self-update path is source-first and adapter-neutral:

```text
self-update intent
→ resolve canonical Git source + installed identity
→ freeze known-good commit/release
→ edit Plugin Builder source
→ run regression/security tests
→ build and inspect deterministic candidate package
→ discover a generic host update capability by behavior
→ guarded activation if available
→ read-back + smoke verification
```

Do not require or invoke Plugin Creator by name. Plugin Creator may be used only as an optional adapter if the current host happens to expose its lifecycle actions; its absence must not block source editing, testing, packaging, or release preparation.

Never let self-update grant Plugin Builder new account privileges. If no valid host mutation adapter exists, finish the self-update build and return `PACKAGE_READY` / `NO_MUTATION_ADAPTER` rather than fabricating installation.

## 8. Verify installation/update independently from packaging

After any lifecycle mutation, read back persisted metadata/version/release and changed files when possible. Verify MCP reachability, authentication/connection, tool discovery, representative harmless behavior, and UI separately when relevant. An upload response proves only the mutation it reports.

Use `INSTALLED_VERIFIED` only when persisted state and relevant smoke evidence support it.

## 9. Prepare public submission without inventing evidence

For public intent, distinguish implementation completion, public-upload copy, listing metadata, required URLs/assets, review cases, demo evidence, reviewer access, scans, domain/developer verification, attestations, draft upload, review submission, approval, and publication.

Skills-only and MCP submissions have different review requirements. Never invent publisher identity, policy URLs, credentials, recordings, test execution, attestations, approval, or publication. Use `SUBMISSION_GAPS` until all required evidence for the requested state exists.

## 10. Parity-plus evaluation

Use `evaluation/CREATOR_PARITY_MATRIX.md` to check baseline Plugin Creator workflow coverage and `evaluation/BUILDER_BENCHMARK.md` for comparative evaluation.

Do not claim universal superiority from feature count. A stronger-builder claim requires:
- no material regression on critical correctness/security/authorization gates;
- baseline lifecycle coverage under comparable host capabilities;
- repeatable advantage on at least one predeclared family such as architecture search, adversarial assurance, repair/recovery, deterministic build verification, or post-install verification.

## 11. Completion states

Use precise status:
- `COMPLETE`: required artifact/change exists and required gates are evidenced.
- `INSTALLED_VERIFIED`: requested installation/update is persisted and relevant read-back/smoke checks pass.
- `PACKAGE_READY`: source/package is validated but host mutation was not requested or is unavailable.
- `NO_MUTATION_ADAPTER`: build is ready but this environment exposes no valid install/update action.
- `BLOCKED`: essential source/access/input is unavailable.
- `REPLAN_REQUIRED`: architecture no longer satisfies the contract.
- `APPROVAL_REQUIRED`: a genuinely new consequential action requires authorization.
- `FAIL_CLOSED`: authorization/integrity uncertainty makes continuing unsafe.
- `SUBMISSION_GAPS`: implementation is ready but public-review materials or portal checks remain.

Report what was actually built, tested, saved, installed, connected, submitted, approved, or published and what remains unverified.
