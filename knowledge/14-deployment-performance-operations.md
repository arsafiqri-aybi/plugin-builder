# Lobe 14 — Deployment, Performance & Operations

Membawa plugin dari local/dev ke stable production dengan latency, availability, security dan rollback yang sesuai.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **deployment, performance & operations**. Do not load it merely because the project is large.

### 14.N1 — Environment parity

**Decision model.** Dev/staging/prod config berbeda hanya pada values yang memang environment-specific.

**Failure signature.** Works locally karena hidden dependency.

**Gate / evidence of mastery.** Deployment manifests/secrets/network assumptions terdokumentasi.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `NIST-SSDF`

### 14.N2 — Stable endpoint and TLS

**Decision model.** Public MCP memakai stable reachable HTTPS, bukan temporary tunnel.

**Failure signature.** Review/runtime gagal karena endpoint ephemeral.

**Gate / evidence of mastery.** Production health + TLS + domain verified.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OAI-SUB`

### 14.N3 — Latency budget

**Decision model.** Break down model→MCP→upstream→storage→UI latency dan target per critical path.

**Failure signature.** User experience lambat tanpa tahu bottleneck.

**Gate / evidence of mastery.** p50/p95 per dependency terlihat.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-GOV`

### 14.N4 — Rate limiting and quotas

**Decision model.** Protect expensive/public actions dengan per-user/tenant/tool limits dan informative errors.

**Failure signature.** Abuse atau cascade failure.

**Gate / evidence of mastery.** Limits diuji dan error recoverable.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OWASP-AGENT`

### 14.N5 — Caching with semantics

**Decision model.** Cache hanya read results yang freshness/scope/dependency match; side effects tidak replay.

**Failure signature.** Stale/private result leak atau duplicate effect.

**Gate / evidence of mastery.** Cache key mencakup identity/version yang material.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`

### 14.N6 — Health and readiness

**Decision model.** Pisahkan process alive, dependency readiness, auth/config sanity dan tool functionality.

**Failure signature.** Load balancer mengirim traffic ke instance belum siap.

**Gate / evidence of mastery.** Health probes meaningful.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`

### 14.N7 — Rollback strategy

**Decision model.** Release dapat dikembalikan ke last-known-good tanpa corrupting schema/state.

**Failure signature.** Bad deploy membutuhkan hotfix langsung di prod.

**Gate / evidence of mastery.** Rollback rehearsal/version compatibility ada.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-SCALE`

### 14.N8 — Incident response

**Decision model.** Detection→containment→diagnosis→communication→recovery→postmortem→regression.

**Failure signature.** Incident ditangani ad hoc dan penyebab berulang.

**Gate / evidence of mastery.** Runbook + owner + evidence retention tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-GOV`

