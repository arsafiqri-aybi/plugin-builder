# Lobe 15 — Versioning, Update & Migration

Memperbarui plugin tanpa kehilangan identity, audience, data, compatibility atau behavior yang tidak diminta berubah.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **versioning, update & migration**. Do not load it merely because the project is large.

### 15.N1 — Source-of-truth resolution

**Decision model.** Cari repository/server/site/account release yang benar-benar memiliki perubahan.

**Failure signature.** Edit archive yang bukan source canonical.

**Gate / evidence of mastery.** Owner source diverifikasi sebelum mutation.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-SKILL`

### 15.N2 — Identity preservation

**Decision model.** Plugin ID, scope, audience, server identity, app bindings dan relevant assets dipertahankan.

**Failure signature.** Update menciptakan duplicate plugin.

**Gate / evidence of mastery.** Before/after identity diff clean.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`

### 15.N3 — Concurrent update guard

**Decision model.** Gunakan current release/version precondition dan reconcile jika berubah.

**Failure signature.** Last-write-wins menimpa perubahan lain.

**Gate / evidence of mastery.** Conflict memaksa refresh/rebase.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-GOV`

### 15.N4 — Schema migration

**Decision model.** Mapping legacy→current harus lossless atau stop dengan incompatibility.

**Failure signature.** Validator pass dengan diam-diam membuang behavior.

**Gate / evidence of mastery.** Effective config parity check.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `AGENT-PLUGINS`

### 15.N5 — Server vs package update

**Decision model.** Backend implementation dapat berubah tanpa selalu package ZIP; metadata/skills/package changes mengikuti release flow target.

**Failure signature.** Unnecessary package churn atau stale metadata.

**Gate / evidence of mastery.** Change classified by owning layer.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `OAI-MCP`

### 15.N6 — Backward compatibility

**Decision model.** Published tool names/schema dan stored state evolve additively bila mungkin.

**Failure signature.** Existing workflows break setelah update.

**Gate / evidence of mastery.** Compatibility suite terhadap prior release.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`

### 15.N7 — Data migration safety

**Decision model.** Schema/data migration punya backup/checkpoint, verification, rollback/forward plan.

**Failure signature.** Code release compatible tetapi data corrupt.

**Gate / evidence of mastery.** Migration gate terpisah dari app deploy gate.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`

### 15.N8 — Read-back verification

**Decision model.** Setelah save/update, baca ulang source/release/state dan verifikasi requested change + preservation.

**Failure signature.** Upload success disamakan dengan correct update.

**Gate / evidence of mastery.** Post-write evidence captured.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-PROMPTING`

