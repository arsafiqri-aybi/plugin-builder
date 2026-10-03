# End-to-End Plugin Build Workflow

## Phase A — Contract
1. Normalize user job and intended outcome.
2. Record supported/unsupported intents.
3. Map actors, accounts, resources, permissions and consequential effects.
4. Define acceptance gates and distribution target.

## Phase B — Architecture
1. Map each capability to Skill / MCP / resource / UI / extension / backend.
2. Filter infeasible routes using host, network, auth, storage and deployment constraints.
3. Choose minimum viable topology; document trust boundaries and state ownership.
4. Define failure, degradation and re-plan triggers.

## Phase C — Contracts
1. Define tool schemas, results, stable IDs, annotations and errors.
2. Define authentication/authorization and least-privilege scopes.
3. Define side-effect, idempotency, retry and concurrency semantics.
4. Define UI fallback and context/data minimization.

## Phase D — Implementation
Build the canonical source first. Reuse existing backends/services where appropriate instead of rebuilding them. Keep secrets outside source/package.

## Phase E — Verification
Run static package/schema checks, unit/contract tests, authorization tests, adversarial tests, host discovery/UI checks and user-job evaluations. Add regressions for fixed failures.

## Phase F — Distribution
Build reproducible artifact, inspect its inventory, verify metadata/assets, then follow the requested private/workspace/public lifecycle. Public readiness additionally requires truthful listing/review/policy materials and live portal checks.
