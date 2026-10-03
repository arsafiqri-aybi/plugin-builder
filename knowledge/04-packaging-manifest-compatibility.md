# Lobe 04 — Packaging, Manifest & Compatibility

Membentuk package yang valid, portable, konsisten, dan aman untuk lifecycle target.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **packaging, manifest & compatibility**. Do not load it merely because the project is large.

### 04.N1 — Canonical root manifest

**Decision model.** Gunakan plugin.json dengan schema version yang tepat dan identity stabil.

**Failure signature.** Multiple manifests menyimpan metadata konflik.

**Gate / evidence of mastery.** Canonical identity/version/presentation sinkron.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `AGENT-PLUGINS`, `OAI-PKG`

### 04.N2 — Portable component locations

**Decision model.** Skills dan MCP config berada pada lokasi yang dapat ditemukan client portable.

**Failure signature.** Custom path lama membuat capability hilang.

**Gate / evidence of mastery.** Inventory effective components cocok dengan package.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-PKG`, `INSTALLED-CREATOR`

### 04.N3 — OpenAI extension namespace

**Decision model.** Tempatkan metadata presentation/review/publication host-specific di extensions.com.openai.

**Failure signature.** Field host-specific mencemari portable root.

**Gate / evidence of mastery.** Namespace separation lulus schema.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-PKG`, `OAI-SUB`

### 04.N4 — Semantic version discipline

**Decision model.** Version mewakili release identity dan perubahan kompatibilitas.

**Failure signature.** Update tanpa bump atau bump tanpa makna.

**Gate / evidence of mastery.** Version policy konsisten dan release dapat ditelusuri.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `NIST-SSDF`

### 04.N5 — Asset integrity

**Decision model.** Referenced icon/UI/template asset ada, ukuran/type sesuai, tanpa symlink/secrets/unrelated files.

**Failure signature.** Manifest valid tetapi asset missing atau package bocor data.

**Gate / evidence of mastery.** Archive inventory diverifikasi sebelum release.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `OAI-SUB`

### 04.N6 — Compatibility overlay

**Decision model.** Legacy/local overlay hanya dipertahankan bila perlu dan disinkronkan.

**Failure signature.** Root manifest menutupi nilai legacy yang belum dimigrasi.

**Gate / evidence of mastery.** Effective config dibandingkan sebelum/after migration.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `AGENT-PLUGINS`

### 04.N7 — Package reproducibility

**Decision model.** Build archive secara deterministik dari source version yang diketahui.

**Failure signature.** ZIP berbeda dari source yang diuji.

**Gate / evidence of mastery.** Artifact hash/inventory terhubung ke source commit/version.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-SKILL`

### 04.N8 — Secret exclusion

**Decision model.** Credential, token, private key, reviewer secret dan environment secret tidak masuk archive.

**Failure signature.** Plugin package menjadi kanal kebocoran.

**Gate / evidence of mastery.** Secret scan + manual inventory pass.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `NIST-SSDF`

