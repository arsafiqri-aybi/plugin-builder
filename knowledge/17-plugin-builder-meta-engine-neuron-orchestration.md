# Lobe 17 — Plugin Builder Meta-Engine & Neuron Orchestration

Mengubah seluruh ilmu menjadi builder yang memilih neuron relevan, menghasilkan plugin, menguji, memperbaiki, dan berhenti dengan evidence.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **plugin builder meta-engine & neuron orchestration**. Do not load it merely because the project is large.

### 17.N1 — Intent-to-neuron routing

**Decision model.** Dari request, aktifkan hanya lobes/neurons yang material terhadap plugin target.

**Failure signature.** Semua 160 neuron dimuat setiap saat.

**Gate / evidence of mastery.** Retrieval plan kecil dan dapat dijelaskan.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `INTERNAL-GOV`

### 17.N2 — Builder contract synthesis

**Decision model.** Gabungkan job, acceptance gates, architecture, risk, environment, distribution dan evidence plan menjadi build contract.

**Failure signature.** Coding dimulai sebelum masalah dan done-state jelas.

**Gate / evidence of mastery.** Contract menjadi source of truth selama build.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-PROMPTING`, `INTERNAL-SCALE`

### 17.N3 — Scaffold from architecture

**Decision model.** Generate file/server/UI structure berdasarkan capability placement, bukan starter template tetap.

**Failure signature.** Semua plugin terlihat sama dan membawa file tidak perlu.

**Gate / evidence of mastery.** Scaffold minimal sesuai topology.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `OAI-PKG`

### 17.N4 — Generate then verify loop

**Decision model.** Setiap generation step diikuti verifier yang sesuai properti: schema/test/host/state/security.

**Failure signature.** AI menilai kodenya sendiri hanya dengan membaca.

**Gate / evidence of mastery.** Evidence channel eksternal/deterministic dipakai bila tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `INTERNAL-SCALE`

### 17.N5 — Diagnosis before repair

**Decision model.** Failure diklasifikasikan ke requirement, architecture, schema, auth, security, state, host, deployment, review, atau UX.

**Failure signature.** Perbaikan shotgun menambah complexity.

**Gate / evidence of mastery.** Patch menyasar root cause dan punya regression test.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`

### 17.N6 — Quality-floor stopping

**Decision model.** Berhenti ketika critical gates pass dan additional work tak mengurangi risiko material, bukan saat terasa sempurna.

**Failure signature.** Infinite polish atau premature done.

**Gate / evidence of mastery.** Stop condition explicit.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`, `INTERNAL-SCALE`

### 17.N7 — Self-contained expertise

**Decision model.** Plugin Builder membawa knowledge/build logic sendiri; tool resmi host adalah accelerator/compatibility layer, bukan dependency epistemik.

**Failure signature.** Builder mati ketika Plugin Creator built-in tidak tersedia.

**Gate / evidence of mastery.** Core design/build/audit tetap berjalan dengan repo sendiri.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `INSTALLED-CREATOR`

### 17.N8 — Learning and maintenance loop

**Decision model.** Update neuron berdasarkan spec/product changes, failed evals, incidents dan review feedback dengan provenance.

**Failure signature.** Knowledge membusuk atau rules bertambah tanpa bukti.

**Gate / evidence of mastery.** Change log maps update→source/evidence→affected tests.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-SKILL`

