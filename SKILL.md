---
name: plugin-builder
description: Design, build, audit, repair, validate, package, or evolve AI plugins. Use when the user wants a new plugin or changes to an existing plugin, including skills, MCP servers/tools, MCP Apps/UI, extensions, authentication, security, testing, deployment, or submission readiness. Do not trigger merely to use a plugin or perform the plugin's target-domain task.
---

# Plugin Builder

Create the smallest plugin architecture that can reliably complete the user's job, then verify the properties that matter. Plugin Builder is a specialist builder: its output is a plugin or a verified plugin change.

## 1. Establish the plugin contract

Identify the user job, target users, supported and unsupported intents, input/output contracts, external systems, authority boundaries, target hosts, distribution mode, critical quality gates, and evidence required for completion. Ask only for information that materially changes architecture, authorization, or public claims; otherwise make reversible assumptions and continue.

For nontrivial work, use `references/build-workflow.md` and load relevant neurons from `knowledge/README.md`. Do not load all 144 neurons by default.

## 2. Select the architecture before coding

For each capability decide whether it belongs in a Skill, MCP tool/server, resource, prompt, MCP App, OpenAI Extension, backend/storage layer, or nowhere. Prefer the smallest topology that satisfies the acceptance floor. Preserve portable MCP behavior; add host-specific extensions only when they materially improve the job and have a fallback where appropriate.

Treat current surface support, SDK APIs, schema versions, submission rules, and product limits as dynamic facts. Recheck authoritative current sources before relying on them for release decisions.

## 3. Build contracts that the model and server can both enforce

Design goal-shaped tools with unambiguous names/descriptions, strict schemas, stable identifiers, useful structured results, truthful annotations, and explicit error semantics. Enforce authentication and authorization on the server for every private or consequential request. The model is not an access-control boundary.

Classify side effects and design retry/idempotency/concurrency behavior before exposing writes. If the status of a prior write is unknown, inspect durable state before retrying.

## 4. Build security and privacy into the architecture

Map trust boundaries and treat user input, retrieved documents, webpages, tool results, and external data as untrusted content. Prevent untrusted content from granting new authority or steering privileged actions. Apply least privilege, input validation, output handling, secret management, tenant isolation, safe logging, and fail-closed behavior where authorization or integrity is uncertain.

Use `references/security-gates.md` for consequential or data-sensitive plugins.

## 5. Add UI only when it improves the job

MCP Apps and host Extensions are progressive enhancements. UI-enabled tools must still return useful model-visible results when UI is unavailable. Design visible state, correction, control, accessibility, error recovery, and graceful degradation. Verify actual render/interaction in the intended host; a JSON response is not proof that UI works.

## 6. Verify by property, not by confidence

Use deterministic validation for manifests/schemas/packages; contract tests for tools; auth/security tests for trust boundaries; host tests for discovery/UI; and end-to-end user-job evaluations for behavior. Separate static validity, deterministic tests, model-behavior evaluations, human review, and production telemetry.

Every fixed defect should gain a focused regression case. Diagnose the root failure class before adding complexity.

## 7. Package/update/release without losing state

Preserve plugin identity, scope, audience, source ownership, versioning, server/app bindings, data, and unrelated behavior. For updates, reconcile against the latest source/release and read back the changed state after mutation. For public distribution, distinguish archive readiness, draft upload, review submission, approval, and publication. Never invent publisher facts, URLs, reviewer evidence, test results, or attestations.

## 8. Completion states

Use precise status:
- `COMPLETE`: required artifact/change exists and required gates are evidenced.
- `BLOCKED`: essential source/access/input is unavailable.
- `REPLAN_REQUIRED`: architecture no longer satisfies the contract.
- `APPROVAL_REQUIRED`: a genuinely new consequential action requires authorization.
- `FAIL_CLOSED`: authorization/integrity uncertainty makes continuing unsafe.
- `SUBMISSION_GAPS`: implementation is ready but public-review materials or portal checks remain.

Report what was actually built/tested/saved and what remains unverified. Do not claim installation, publication, compatibility, security, or quality that was not demonstrated.
