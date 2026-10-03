# Lobe 06 — Tool Contract, Schema & Model Affordance

Merancang tools yang mudah dipilih model, sulit disalahgunakan, dan mudah dirangkai.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **tool contract, schema & model affordance**. Do not load it merely because the project is large.

### 06.N1 — Goal-shaped tool granularity

**Decision model.** Satu tool menyelesaikan langkah user yang recognizable, bukan endpoint mentah atau mega-tool ambigu.

**Failure signature.** Terlalu granular memicu orchestration burden; terlalu besar menyembunyikan authority.

**Gate / evidence of mastery.** Tool set minim tetapi composable.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-PROMPTING`

### 06.N2 — Naming and description semantics

**Decision model.** Nama/deskripsi menyatakan aksi, objek, precondition, limits dan side effect.

**Failure signature.** Model salah memilih tool karena descriptions overlap.

**Gate / evidence of mastery.** Positive/negative selection eval membedakan tool tetangga.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-SKILL`

### 06.N3 — Input schema design

**Decision model.** Gunakan types, required, enum, bounds, identifiers dan mutually exclusive shape yang jelas.

**Failure signature.** Free-form strings membawa ambiguity/validation bugs.

**Gate / evidence of mastery.** Invalid input ditolak sebelum side effect.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `JSON-SCHEMA`, `OAI-MCP`

### 06.N4 — Structured result design

**Decision model.** Return stable identifiers, typed fields, provenance dan next-action-relevant data.

**Failure signature.** Model harus parse prose untuk melanjutkan workflow.

**Gate / evidence of mastery.** Result cukup untuk next step tanpa UI.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`

### 06.N5 — Annotation truthfulness

**Decision model.** readOnlyHint, destructiveHint, openWorldHint mencerminkan behavior nyata.

**Failure signature.** Safety/confirmation behavior host salah akibat annotation palsu.

**Gate / evidence of mastery.** Annotation diuji terhadap implementation.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INSTALLED-CREATOR`

### 06.N6 — Elicitation boundary

**Decision model.** Gunakan elicitation untuk missing structured user input, bukan secret/auth atau info yang sudah ada.

**Failure signature.** Server mengumpulkan credential lewat tool conversation.

**Gate / evidence of mastery.** Elicitation fields minimal dan user-answerable.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`

### 06.N7 — Tool chaining contract

**Decision model.** IDs dan state version memungkinkan output tool A menjadi input tool B tanpa guessing.

**Failure signature.** Chaining bergantung nama display yang mutable.

**Gate / evidence of mastery.** Stable identifiers + version preconditions tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-SCALE`

### 06.N8 — Selection collision testing

**Decision model.** Uji prompt natural yang bisa cocok ke dua tools dan out-of-scope prompt.

**Failure signature.** Tool individually correct tapi router/model selection unreliable.

**Gate / evidence of mastery.** Collision matrix dan prohibited-call cases lulus.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INTERNAL-SKILL`

