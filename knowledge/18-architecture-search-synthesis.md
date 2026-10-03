# Lobe 18 — Architecture Search & Synthesis

Membuat Plugin Builder tidak berhenti pada satu arsitektur pertama yang terasa masuk akal. Lobe ini membentuk beberapa kandidat yang benar-benar berbeda, menyaring yang tidak feasible, membandingkan trade-off, mensimulasikan kegagalan, lalu memilih struktur paling sederhana yang tetap memenuhi kontrak.

## Lobe decision flow

Use this lobe when more than one materially different topology could satisfy the user job, when architecture choice has high downstream cost, or when a prior design failed. Do not generate alternatives for trivial skills-only plugins with an obvious route.

### 18.N1 — Candidate topology generation

**Decision model.** Generate a small set of materially different architectures only when architecture uncertainty is real: for example skills-only, existing-MCP reuse, new remote MCP, local stdio, or MCP + App/Extension. Variants must differ in capability placement or operational boundary, not cosmetic file layout.

**Failure signature.** The first plausible topology becomes the design without comparing a simpler, safer, or more portable route.

**Gate / evidence of mastery.** At least two materially different candidates exist for consequential ambiguous builds, or the builder records why a single route is obviously sufficient.

**Synapses.** Exchange state with 02 requirements, 03 capability placement, 14 operations, 16 distribution, and 19 installation adaptation.

**Primary sources.** `INTERNAL-SCALE`, `OAI-PKG`, `OAI-MCP`

### 18.N2 — Feasibility filtering

**Decision model.** Reject candidates that cannot satisfy required host, transport, authentication, storage, network, deployment, persistence, or permission constraints before comparing quality.

**Failure signature.** An elegant design is selected even though the target host cannot run, connect, authenticate, or install it.

**Gate / evidence of mastery.** Every surviving candidate has an explicit feasible path for every hard dependency.

**Synapses.** Exchange state with 03 architecture, 05 protocol, 08 auth, 14 deployment, and 19 host capability discovery.

**Primary sources.** `INTERNAL-SCALE`, `OAI-PKG`, `OAI-MCP`, `OAI-AUTH`

### 18.N3 — Dominance pruning

**Decision model.** Remove a candidate when another candidate satisfies the same hard requirements with no worse critical risk/quality properties and materially less complexity, coupling, operational burden, or privilege.

**Failure signature.** The design keeps redundant layers merely because they are technically possible.

**Gate / evidence of mastery.** Every retained component or topology difference has a user-job, quality, security, portability, or lifecycle reason.

**Synapses.** Exchange state with 03 capability composition, 09 security, 12 privacy, 14 operations, and 17 quality-floor stopping.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-GOV`, `NIST-SSDF`

### 18.N4 — Quality-attribute trade-off map

**Decision model.** Compare candidates on the properties that matter for this plugin: correctness, security, privacy, latency, portability, usability, maintainability, observability, availability, cost/resource demand, and migration burden. Do not collapse them into one invented universal score.

**Failure signature.** A single vague label such as “best architecture” hides a critical trade-off.

**Gate / evidence of mastery.** The selected route exposes material gains and sacrifices, and no critical acceptance criterion is traded away silently.

**Synapses.** Exchange state with 02 acceptance hierarchy, 11 UX, 12 privacy, 13 evaluation, 14 operations, and 17 stopping.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-GOV`, `NIST-SSDF`, `HAX`

### 18.N5 — Failure-mode simulation

**Decision model.** Before implementation, walk the selected candidate through likely failures: auth denial, stale data, malformed input, prompt injection, dependency outage, rate limiting, partial write, duplicate retry, stale version, host incompatibility, and UI absence when applicable.

**Failure signature.** Failure handling is added only after an incident exposes an architectural gap.

**Gate / evidence of mastery.** Critical failure modes map to detection, containment, recovery, and a verifier before release.

**Synapses.** Exchange state with 08 auth, 09 security, 10 distributed reliability, 13 evaluation, and 14 operations.

**Primary sources.** `OWASP-AGENT`, `NIST-SSDF`, `INTERNAL-GOV`

### 18.N6 — Build-versus-reuse decision

**Decision model.** Reuse a verified existing MCP server, API, app, storage system, or backend when it already satisfies the contract and ownership/security constraints. Build new infrastructure only when reuse leaves a material gap.

**Failure signature.** Plugin Builder rebuilds an existing service, multiplying attack surface and maintenance for no user benefit.

**Gate / evidence of mastery.** Every newly introduced service has a documented capability gap that reuse could not satisfy.

**Synapses.** Exchange state with 03 dependencies, 08 authorization, 09 supply chain, 14 operations, and 15 source-of-truth resolution.

**Primary sources.** `OAI-MCP`, `INSTALLED-CREATOR`, `NIST-SSDF`

### 18.N7 — Evolution runway

**Decision model.** Check whether identifiers, schemas, state ownership, tool boundaries, and versioning allow likely near-term evolution without breaking users. Add extension points only for plausible requirements, not speculative frameworks.

**Failure signature.** Either the first small change becomes a breaking rewrite, or the initial plugin is burdened with unused abstraction.

**Gate / evidence of mastery.** The chosen design supports known next-step changes through bounded versioned interfaces while remaining minimal today.

**Synapses.** Exchange state with 04 packaging, 05 protocol evolution, 10 state, 15 migration, and 16 release lifecycle.

**Primary sources.** `NIST-SSDF`, `OAI-MCP`, `INTERNAL-SCALE`

### 18.N8 — Architecture proof and decision record

**Decision model.** Record selected topology, rejected alternatives, hard constraints, decisive trade-offs, unresolved assumptions, and the tests that will prove the selection was adequate.

**Failure signature.** Future repairs cannot distinguish intentional design from accidental structure.

**Gate / evidence of mastery.** Architecture choice is reproducible from the contract and can be revisited when a recorded assumption changes.

**Synapses.** Exchange state with 00 evidence trace, 02 contract, 13 evaluation, 15 migration, and 17 learning loop.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-SKILL`, `NIST-SSDF`
