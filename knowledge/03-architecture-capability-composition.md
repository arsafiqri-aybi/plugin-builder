# Lobe 03 — Architecture & Capability Composition

Memilih struktur terkecil yang dapat memenuhi kontrak kualitas tanpa overengineering.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **architecture & capability composition**. Do not load it merely because the project is large.

### 03.N1 — Capability placement

**Decision model.** Putuskan tiap kebutuhan masuk skill, MCP tool, resource, prompt, app UI, extension, backend atau tidak perlu plugin.

**Failure signature.** Semua kebutuhan diterjemahkan menjadi tool.

**Gate / evidence of mastery.** Placement rationale tersedia per capability.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`, `OAI-PKG`

### 03.N2 — Architecture topology

**Decision model.** Pilih skills-only, MCP-only, skill+MCP, MCP+App, extension-enhanced, local, remote atau hybrid.

**Failure signature.** Menggunakan topology kompleks untuk task sederhana.

**Gate / evidence of mastery.** Topology terkecil yang memenuhi acceptance floor dipilih.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-SCALE`

### 03.N3 — Dependency graph

**Decision model.** Modelkan upstream API, datastore, auth server, UI resources, plugin assets, review dependencies dan host capabilities.

**Failure signature.** Perubahan upstream mematahkan plugin tanpa diketahui.

**Gate / evidence of mastery.** Dependency versions/owners dan critical path tercatat.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`, `NIST-SSDF`

### 03.N4 — State ownership

**Decision model.** Tentukan state mana host, MCP server, external service, UI, plugin config atau user yang memilikinya.

**Failure signature.** Duplicate/stale state dan konflik write.

**Gate / evidence of mastery.** Single source of truth ditetapkan per state domain.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `INTERNAL-GOV`

### 03.N5 — Trust boundaries

**Decision model.** Petakan data/instruction flow antar user, model, tool, retrieved content, server, app iframe dan external API.

**Failure signature.** Untrusted content bisa mengubah privileged action.

**Gate / evidence of mastery.** Trust boundary memiliki validation/policy enforcement.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-PI`, `OWASP-AGENT`

### 03.N6 — Portability vs specialization

**Decision model.** Pertahankan core portable; tambah OpenAI-specific Extensions hanya bila memberi nilai nyata.

**Failure signature.** Plugin terkunci ke host padahal tidak perlu.

**Gate / evidence of mastery.** Host-specific layer punya fallback portable.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `OAI-EXT`

### 03.N7 — Graceful degradation

**Decision model.** Desain fallback untuk UI unavailable, auth unavailable, service partial outage, optional capability missing.

**Failure signature.** Satu capability optional membuat keseluruhan plugin unusable.

**Gate / evidence of mastery.** Core job tetap bisa gagal jelas atau berjalan dalam degraded mode.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `INTERNAL-GOV`

### 03.N8 — Architecture decision records

**Decision model.** Simpan keputusan besar, alternatif ditolak, trigger revisi dan verifier.

**Failure signature.** Tim tidak tahu mengapa arsitektur tertentu dipilih.

**Gate / evidence of mastery.** ADR ringkas tersedia untuk keputusan material.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-SCALE`

