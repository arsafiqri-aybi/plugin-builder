# Lobe 01 — Plugin Ontology & Host Mental Model

Memahami objek yang sedang dibangun dan batas antara package, Skill, MCP, App, Extension, host, dan backend.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **plugin ontology & host mental model**. Do not load it merely because the project is large.

### 01.N1 — Plugin as capability package

**Decision model.** Modelkan plugin sebagai identitas distributable yang mengikat skills, MCP connections, assets, metadata dan extension host-specific.

**Failure signature.** Menganggap plugin sama dengan satu MCP server atau satu prompt.

**Gate / evidence of mastery.** Arsitektur menyatakan komponen mana yang benar-benar dibutuhkan.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-PKG`, `AGENT-PLUGINS`

### 01.N2 — Skill vs tool vs resource vs prompt

**Decision model.** Bedakan instruksi reusable, aksi executable, data/context, dan prompt template.

**Failure signature.** Menaruh aksi deterministik dalam prose atau data besar di instruction.

**Gate / evidence of mastery.** Setiap capability ditempatkan pada primitive yang tepat.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`, `INTERNAL-SKILL`

### 01.N3 — MCP server boundary

**Decision model.** Server adalah enforcement boundary untuk tool execution, data access dan authorization; model bukan boundary keamanan.

**Failure signature.** Mengandalkan model untuk memutuskan hak akses.

**Gate / evidence of mastery.** Setiap private/write tool memverifikasi authorization server-side.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OAI-AUTH`

### 01.N4 — MCP App boundary

**Decision model.** UI adalah progressive enhancement atas tool contract; tool harus tetap bermakna tanpa render UI.

**Failure signature.** UI menjadi satu-satunya jalur kerja sehingga host tanpa UI rusak.

**Gate / evidence of mastery.** Ada text/structured fallback untuk UI-enabled tools.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `OAI-QUICK`

### 01.N5 — Extension boundary

**Decision model.** OpenAI Extensions menambah integrasi host dan tidak boleh dicampur dengan core MCP semantics.

**Failure signature.** Mencampur API version/extension metadata ke portable layer.

**Gate / evidence of mastery.** Portable core dan host-specific extension dipisahkan jelas.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-EXT`, `OAI-EXT-SPEC`

### 01.N6 — Local vs cloud vs existing server

**Decision model.** Pilih local untuk akses mesin lokal, cloud untuk multi-surface, existing server bila backend sudah ada.

**Failure signature.** Membangun ulang backend hanya karena Plugin Builder tersedia.

**Gate / evidence of mastery.** Hosting choice didasarkan kebutuhan akses, latency, auth dan ownership.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `OAI-MCP`

### 01.N7 — Private/workspace/public lifecycle

**Decision model.** Scope distribusi memengaruhi package, verification, review, URLs dan identity.

**Failure signature.** Menganggap private success sama dengan public readiness.

**Gate / evidence of mastery.** Status dibedakan: source-ready, private-installed, submission-ready, published.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INSTALLED-CREATOR`

### 01.N8 — Host capability negotiation

**Decision model.** Dukungan MCP Apps/extensions adalah negotiated/host-dependent, bukan asumsi.

**Failure signature.** Plugin gagal karena menganggap semua host mendukung capability yang sama.

**Gate / evidence of mastery.** Capability detection + graceful degradation tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `OAI-EXT`

