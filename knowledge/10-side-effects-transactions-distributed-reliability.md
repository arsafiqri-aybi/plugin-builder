# Lobe 10 — Side Effects, Transactions & Distributed Reliability

Mencegah duplicate effects, partial writes dan state corruption pada plugin yang bertindak di dunia nyata.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **side effects, transactions & distributed reliability**. Do not load it merely because the project is large.

### 10.N1 — Idempotency classification

**Decision model.** Tandai operasi safe-to-retry, idempotent-with-key, non-idempotent dan destructive.

**Failure signature.** Retry otomatis mengirim email/order dua kali.

**Gate / evidence of mastery.** Retry policy berasal dari operation class.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-GOV`

### 10.N2 — Idempotency keys

**Decision model.** Untuk create/action yang mendukung, gunakan client/request key dan dedupe store.

**Failure signature.** Timeout membuat status effect unknown.

**Gate / evidence of mastery.** Repeated same key menghasilkan satu effect.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`

### 10.N3 — Optimistic concurrency

**Decision model.** Gunakan version/ETag/expected state untuk edit resource bersama.

**Failure signature.** Lost update menimpa perubahan user lain.

**Gate / evidence of mastery.** Conflict menghasilkan explicit recovery.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `NIST-SSDF`

### 10.N4 — Partial failure semantics

**Decision model.** Definisikan apakah batch atomic, best-effort, compensatable atau resumable.

**Failure signature.** Model menganggap semua item berhasil ketika sebagian gagal.

**Gate / evidence of mastery.** Result melaporkan per-item state dan next action.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-GOV`

### 10.N5 — State inspection before retry

**Decision model.** Jika write response ambiguous, baca state aktual sebelum mencoba lagi.

**Failure signature.** Blind retry menggandakan side effect.

**Gate / evidence of mastery.** Unknown effect status selalu menuju inspect/reconcile.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`

### 10.N6 — Timeout/backoff/circuit breaker

**Decision model.** Timeout per dependency, retry jitter/backoff dan breaker untuk outage sesuai semantics.

**Failure signature.** Thundering herd dan latency spiral.

**Gate / evidence of mastery.** Transient failure tidak menjadi infinite retry.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-GOV`

### 10.N7 — Compensation and rollback

**Decision model.** Untuk workflow multi-step, tentukan rollback/compensation dan irreversible boundary.

**Failure signature.** Step 3 gagal setelah step 1-2 sukses tanpa recovery.

**Gate / evidence of mastery.** Saga/recovery plan ada bila atomic transaction tidak tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`

### 10.N8 — Consistency visibility

**Decision model.** User/model harus tahu committed, pending, failed, rolled-back atau unknown.

**Failure signature.** UI menampilkan sukses sebelum backend commit.

**Gate / evidence of mastery.** Status language cocok dengan durable state.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NNG`, `INTERNAL-GOV`

