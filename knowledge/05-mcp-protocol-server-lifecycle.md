# Lobe 05 — MCP Protocol & Server Lifecycle

Menguasai lifecycle protocol dan perilaku server agar plugin interoperable dan dapat didiagnosis.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **mcp protocol & server lifecycle**. Do not load it merely because the project is large.

### 05.N1 — Initialization and capability negotiation

**Decision model.** Pahami initialize, protocol version, advertised capabilities dan extension negotiation.

**Failure signature.** Server mendaftarkan fitur yang client tidak dukung.

**Gate / evidence of mastery.** Capability-dependent behavior diuji pada target host.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`, `MCP-APPS`

### 05.N2 — Tool lifecycle

**Decision model.** Tool discovery, call semantics, result/error shape dan list-change behavior harus konsisten.

**Failure signature.** Tool exists di code tetapi tidak discovered atau schema stale.

**Gate / evidence of mastery.** Inspector menunjukkan tool list/schema sesuai source.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `MCP-SPEC`

### 05.N3 — Resources and prompts

**Decision model.** Gunakan resources untuk context/data dan prompts untuk template user-facing saat tepat, bukan memaksa semuanya menjadi tool.

**Failure signature.** Protocol primitives dipakai tanpa semantik yang benar.

**Gate / evidence of mastery.** Primitive selection dapat dijelaskan per use case.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`

### 05.N4 — Transport selection

**Decision model.** Remote public plugin memakai stable HTTPS streamable HTTP; local process dapat stdio sesuai host.

**Failure signature.** Temporary tunnel/local path dianggap production endpoint.

**Gate / evidence of mastery.** Transport cocok dengan deployment scope.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INSTALLED-CREATOR`

### 05.N5 — Progress/cancellation/tasks

**Decision model.** Long-running operation harus punya progress, cancellation atau task handle bila protocol/host mendukung.

**Failure signature.** User tidak tahu status dan duplicate action terjadi karena retry.

**Gate / evidence of mastery.** Long task memiliki explicit lifecycle state.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`, `NNG`

### 05.N6 — Error taxonomy

**Decision model.** Bedakan validation, auth, permission, rate limit, transient upstream, conflict, not-found, partial success dan internal errors.

**Failure signature.** Semua failure menjadi generic error sehingga model retry buta.

**Gate / evidence of mastery.** Error response mengarahkan recovery aman.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-GOV`

### 05.N7 — Protocol observability

**Decision model.** Log initialization, discovery, tool call correlation, latency dan outcome tanpa secret.

**Failure signature.** Debugging hanya berdasarkan user report.

**Gate / evidence of mastery.** Trace dapat merekonstruksi failure boundary.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `NIST-SSDF`

### 05.N8 — Backward-compatible evolution

**Decision model.** Pertahankan nama/schema published sebisa mungkin; perubahan breaking butuh migration/version strategy.

**Failure signature.** Model/client memakai contract lama setelah server berubah.

**Gate / evidence of mastery.** Compatibility tests ada untuk released contract.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `INTERNAL-SCALE`

