---
name: plugin-builder
description: Design, build, audit, repair, validate, package, install when supported, or evolve AI plugins. Use when the user wants a new plugin or changes to an existing plugin, including skills, MCP servers/tools, MCP Apps/UI, extensions, authentication, security, testing, deployment, installation, migration, or submission readiness. Do not trigger merely to use a plugin or perform the plugin's target-domain task.
---

# Plugin Builder

Create the smallest plugin architecture that can reliably complete the user's job, prove the properties that matter, and carry the result through the requested lifecycle as far as the current host actually permits. Plugin Builder is a specialist builder: its output is a plugin, a verified plugin change, or a validated install/release artifact.

## 1. Establish the plugin contract

Identify the user job, target users, supported and unsupported intents, input/output contracts, external systems, authority boundaries, target hosts, distribution mode, critical quality gates, and evidence required for completion. Ask only for information that materially changes architecture, authorization, or public claims; otherwise make reversible assumptions and continue.

For nontrivial work, use `references/build-workflow.md` and load relevant neurons from `knowledge/README.md`. Do not load all 160 neurons by default.

## 2. Search architecture when the choice matters

For each capability decide whether it belongs in a Skill, MCP tool/server, resource, prompt, MCP App, OpenAI Extension, backend/storage layer, reused external service, or nowhere. When several materially different topologies are feasible, use `references/architecture-search.md`: generate a small candidate set, reject infeasible routes, prune dominated designs, simulate critical failures, and select the smallest route that can pass the acceptance floor.

Do not confuse “more components” with “more capable”. Reuse verified existing infrastructure when it already satisfies the contract. Preserve portable MCP behavior; add host-specific extensions only when they materially improve the job and have an appropriate fallback.

Treat current surface support, SDK APIs, schema versions, submission rules, and product limits as dynamic facts. Recheck authoritative current sources before relying on them for release decisions.

## 3. Build a canonical source, not a disposable scaffold

Start from a portable root `plugin.json` package and add only components required by the selected architecture. Use repository tooling when local execution is available:

- `scripts/init_plugin.py` for a minimal portable scaffold;
- `scripts/validate_plugin.py` for package/component validation;
- `scripts/package_plugin.py` for deterministic packaging;
- `scripts/audit_plugin_package.py` for an additional static secret/symlink audit.

Compatibility overlays are derived from the canonical source; they do not become an independent source of truth. Generate file/server/UI structure from the architecture, not from a fixed maximal template.

## 4. Build contracts the model and server can both enforce

Design goal-shaped tools with unambiguous names/descriptions, strict schemas, stable identifiers, useful structured results, truthful annotations, and explicit error semantics. Enforce authentication and authorization on the server for every private or consequential request. The model is not an access-control boundary.

Classify side effects and design retry/idempotency/concurrency behavior before exposing writes. If the status of a prior write is unknown, inspect durable state before retrying.

## 5. Build security, privacy, reliability, and UX into the architecture

Map trust boundaries and treat user input, retrieved documents, webpages, tool results, and external data as untrusted content. Prevent untrusted content from granting authority or steering privileged actions. Apply least privilege, input validation, output handling, secret management, tenant isolation, safe logging, and fail-closed behavior where authorization or integrity is uncertain.

MCP Apps and host Extensions are progressive enhancements. UI-enabled tools must still return useful model-visible results when UI is unavailable. Design visible state, correction, control, accessibility, error recovery, and graceful degradation. Use `references/security-gates.md` for consequential/data-sensitive plugins.

## 6. Verify by property, then repair by root cause

Use deterministic validation for manifests/schemas/packages; contract tests for tools; auth/security tests for trust boundaries; host tests for discovery/UI; and end-to-end user-job evaluations for behavior. Separate static validity, deterministic tests, model-behavior evaluations, human review, and production telemetry.

Every fixed defect should gain a focused regression case. Classify the failure before patching. Re-open architecture search only when the failure is structural; do not add layers to repair a local schema, auth, state, or implementation defect.

## 7. Install/update through a real host adapter

When the user asks to install, save, connect, or update, use `references/installation-adapters.md`. Discover the actual mutation path exposed by the current environment and by the plugin's owning source. Prefer direct account create/update only when that capability is genuinely available and appropriate; otherwise use the owning Git/Site/local/submission flow or return the validated package with the exact remaining step.

Creation must avoid duplicates. Updates must resolve exact identity, preserve scope/audience/unrelated behavior, guard against stale releases when supported, and reconcile concurrent changes. Package mutation, MCP reachability, authentication, and working host behavior are separate states.

After any mutation, read back persisted state when possible, verify release/version and affected files, then perform a harmless representative discovery/call/UI check appropriate to the change. Never claim installation from packaging alone or working behavior from an upload response alone.

## 8. Release without losing state

Preserve plugin identity, source ownership, versioning, server/app bindings, data, and unrelated behavior. For public distribution, distinguish archive readiness, draft upload, connection/setup, review submission, approval, and publication. Never invent publisher facts, URLs, reviewer evidence, test results, credentials, or attestations.

## 9. Completion states

Use precise status:
- `COMPLETE`: required artifact/change exists and required gates are evidenced.
- `INSTALLED_VERIFIED`: requested installation/update is persisted and relevant read-back/smoke checks pass.
- `PACKAGE_READY`: source/package is validated but host mutation was not requested or is unavailable.
- `NO_MUTATION_ADAPTER`: build is ready but this environment exposes no valid install/update path.
- `BLOCKED`: essential source/access/input is unavailable.
- `REPLAN_REQUIRED`: architecture no longer satisfies the contract.
- `APPROVAL_REQUIRED`: a genuinely new consequential action requires authorization.
- `FAIL_CLOSED`: authorization/integrity uncertainty makes continuing unsafe.
- `SUBMISSION_GAPS`: implementation is ready but public-review materials or portal checks remain.

Report what was actually built, tested, saved, installed, connected, or published and what remains unverified. Do not claim universal superiority. Demonstrate improvement with broader capability coverage, stronger gates, or comparative evaluation when evidence exists.
