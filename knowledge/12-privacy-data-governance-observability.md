# Lobe 12 — Privacy, Data Governance & Observability

Menyimpan cukup data untuk fungsi/debugging tanpa memperluas risiko privasi.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **privacy, data governance & observability**. Do not load it merely because the project is large.

### 12.N1 — Data inventory

**Decision model.** Catat kategori data, source, purpose, sensitivity, destination dan retention.

**Failure signature.** Tidak tahu data apa yang plugin proses.

**Gate / evidence of mastery.** Inventory cocok dengan privacy disclosure dan code.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-GUIDE`, `NIST-SSDF`

### 12.N2 — Data minimization

**Decision model.** Ambil/kirim/simpan minimum yang dibutuhkan untuk job aktif.

**Failure signature.** Whole-record payload dikirim padahal hanya satu field dibutuhkan.

**Gate / evidence of mastery.** Field-level justification tersedia untuk sensitive data.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OWASP-AGENT`

### 12.N3 — Retention and deletion

**Decision model.** Tetapkan retention berdasarkan kebutuhan, user expectation, legal/policy; punya deletion path.

**Failure signature.** Logs/cache menyimpan PII selamanya.

**Gate / evidence of mastery.** Retention config + deletion test ada.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `NIST-SSDF`

### 12.N4 — Log hygiene

**Decision model.** Jangan log token, secret, unnecessary personal/tool result; redact structured fields.

**Failure signature.** Observability menjadi data leak.

**Gate / evidence of mastery.** Log sample melewati secret/PII review.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `NIST-SSDF`

### 12.N5 — Audit trail

**Decision model.** Consequential action merekam who/what/when/resource/outcome tanpa sensitive payload berlebihan.

**Failure signature.** Tidak dapat investigasi tindakan salah.

**Gate / evidence of mastery.** Audit record correlatable dan tamper-aware sesuai risk.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-AGENT`, `NIST-SSDF`

### 12.N6 — Telemetry purpose limitation

**Decision model.** Metric untuk reliability/product improvement tidak otomatis membenarkan collection lain.

**Failure signature.** Analytics scope melebar tanpa kebutuhan.

**Gate / evidence of mastery.** Telemetry dictionary dan purpose explicit.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-GUIDE`

### 12.N7 — Tenant isolation

**Decision model.** Storage/cache/log/index partitioning mencegah cross-user/workspace leakage.

**Failure signature.** Shared cache mengembalikan data tenant lain.

**Gate / evidence of mastery.** Isolation tests mencakup IDs dan cache keys.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-AUTH`, `OWASP-AGENT`

### 12.N8 — Policy truthfulness

**Decision model.** Privacy/support/terms/listing harus mencerminkan behavior aktual, bukan template aspiratif.

**Failure signature.** Submission lolos text check tetapi policy palsu.

**Gate / evidence of mastery.** Claim-to-implementation review dilakukan.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INSTALLED-CREATOR`

