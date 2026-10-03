# Lobe 07 — Data, Retrieval, Context & Knowledge

Mengatur bagaimana plugin mencari, mengirim, membatasi, dan menyegarkan data untuk model/user.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **data, retrieval, context & knowledge**. Do not load it merely because the project is large.

### 07.N1 — Data source authority

**Decision model.** Tentukan system of record, cache, derived data dan provenance.

**Failure signature.** Plugin mencampur stale cache dengan authoritative state.

**Gate / evidence of mastery.** Setiap material datum punya source/freshness class.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-PROMPTING`, `INTERNAL-GOV`

### 07.N2 — Search/fetch architecture

**Decision model.** Untuk knowledge, pisahkan discovery/search dari fetch detail dan gunakan stable IDs/URLs.

**Failure signature.** Tool mengembalikan terlalu banyak data atau citation unusable.

**Gate / evidence of mastery.** Search recall + fetch precision diuji.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`

### 07.N3 — Context minimization

**Decision model.** Kirim hanya data yang dibutuhkan model untuk task aktif; data UI/private tidak otomatis masuk model context.

**Failure signature.** Privacy leak dan context bloat.

**Gate / evidence of mastery.** Context packet punya justification.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`, `OAI-MCP`

### 07.N4 — Freshness policy

**Decision model.** TTL dan refresh trigger mengikuti volatility domain dan consequence of stale data.

**Failure signature.** Cache dianggap valid tanpa dependency/version check.

**Gate / evidence of mastery.** Freshness explicit atau unknown.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`

### 07.N5 — Provenance and citations

**Decision model.** Berikan user-openable source URLs bila workflow memerlukan evidence/citation.

**Failure signature.** Model membuat klaim tanpa traceable source.

**Gate / evidence of mastery.** Result menyimpan source identity dan evidence relation.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-PROMPTING`

### 07.N6 — Pagination and bounded retrieval

**Decision model.** Support cursor/paging dan bounded result sizes.

**Failure signature.** Unbounded list menghabiskan latency/context.

**Gate / evidence of mastery.** Pagination contract diuji pada empty/large datasets.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`, `INTERNAL-GOV`

### 07.N7 — Multi-account isolation

**Decision model.** Account identity dan data scope harus berasal dari validated credentials, bukan model inference.

**Failure signature.** Cross-account data leak.

**Gate / evidence of mastery.** Profile/account discriminator dan server-side scope checks lulus.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OAI-AUTH`

### 07.N8 — Knowledge update lifecycle

**Decision model.** Server-imported skills/knowledge snapshots butuh rescan/version awareness bila platform memakai snapshot.

**Failure signature.** Source updated tetapi plugin release masih memakai snapshot lama.

**Gate / evidence of mastery.** Update trigger dan release note mencatat knowledge refresh.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OAI-SUB`

