# End-to-End Plugin Build Workflow

## Phase A — Contract
1. Normalize user job and intended outcome.
2. Record supported/unsupported intents.
3. Map actors, accounts, resources, permissions and consequential effects.
4. Define acceptance gates, target hosts, source ownership and distribution target.

## Phase B — Architecture search
1. Map each capability to Skill / MCP / resource / UI / extension / backend / reused service / nowhere.
2. If architecture is non-obvious, generate a small set of materially different candidates.
3. Filter infeasible routes using host, network, auth, storage, deployment and permission constraints.
4. Prune dominated routes; compare relevant quality attributes without an invented universal score.
5. Simulate critical failures/trust-boundary attacks on the leading route.
6. Select the smallest topology that can pass the acceptance floor and record re-plan triggers.

## Phase C — Contracts
1. Define tool schemas, results, stable IDs, annotations and errors.
2. Define authentication/authorization and least-privilege scopes.
3. Define side-effect, idempotency, retry and concurrency semantics.
4. Define UI fallback, state ownership and context/data minimization.

## Phase D — Canonical implementation
Build portable canonical source first. Generate only components required by architecture. Reuse existing backends/services where appropriate. Keep secrets outside source/package. Add compatibility overlays from canonical state rather than maintaining divergent copies.

## Phase E — Verification & repair
Run static package/schema checks, unit/contract tests, authorization tests, adversarial tests, host discovery/UI checks and user-job evaluations. Diagnose failures by layer. Add regressions for fixed defects. Re-open Phase B only for structural failure.

## Phase F — Package
Create a reproducible package, inspect inventory, verify metadata/assets and ensure effective skills/MCP configuration matches the canonical source. Public-upload copies receive public-specific validation without mutating the private/source package.

## Phase G — Install/update adapter
1. Discover real host mutation capabilities and source ownership.
2. Select account, managed-source, local-marketplace, submission-portal, or package-only adapter.
3. Check authorization and current identity/release before mutation.
4. Perform the authorized mutation once.
5. Read back persisted state; verify connection/auth separately; run a harmless representative smoke check.
6. On failure, classify the adapter failure and preserve the last-known-good artifact rather than blindly retrying.

## Phase H — Distribution/publication
For public release, prepare truthful listing, policy URLs, cases, demo, reviewer access and publication metadata, then follow the exact draft → connection/test → review → approval → publish lifecycle requested by the user.
