# Lobe 11 — MCP Apps, Extensions & Human-AI UX

Membuat UI yang benar-benar membantu, portable bila mungkin, accessible, dan jujur tentang state/AI limits.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **mcp apps, extensions & human-ai ux**. Do not load it merely because the project is large.

### 11.N1 — UI necessity test

**Decision model.** Tambahkan UI hanya jika visual interaction mengurangi ambiguity/cognitive load atau memungkinkan task yang buruk via prose.

**Failure signature.** UI dibuat sebagai dekorasi.

**Gate / evidence of mastery.** Ada measurable interaction benefit.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `HAX`

### 11.N2 — Progressive enhancement

**Decision model.** Tool memberi meaningful structured/text result tanpa UI; UI memperkaya host yang mendukung.

**Failure signature.** No-UI host kehilangan core functionality.

**Gate / evidence of mastery.** Fallback tested.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`

### 11.N3 — Capability negotiation

**Decision model.** Register UI/extension behavior berdasarkan host capability dan version.

**Failure signature.** API mix menyebabkan runtime mismatch.

**Gate / evidence of mastery.** Target SDK/spec version dicatat dan diuji.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-APPS`, `OAI-EXT-SPEC`

### 11.N4 — System status visibility

**Decision model.** Tampilkan loading, pending action, success, partial failure dan stale state tepat waktu.

**Failure signature.** User tidak tahu apakah action terjadi.

**Gate / evidence of mastery.** UI status berasal dari backend state, bukan optimistic fiction.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NNG`, `HAX`

### 11.N5 — User control and reversibility

**Decision model.** Berikan cancel/back/undo bila meaningful; consequence dijelaskan sebelum irreversible action.

**Failure signature.** AI flow mengunci user dalam action.

**Gate / evidence of mastery.** Control tersedia sesuai reversibility class.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NNG`, `HAX`

### 11.N6 — AI uncertainty and correction

**Decision model.** Tampilkan limits, allow correction, recover gracefully when model/tool wrong.

**Failure signature.** UI mempresentasikan inference sebagai fakta pasti.

**Gate / evidence of mastery.** Correction loop diuji.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `HAX`

### 11.N7 — Accessibility

**Decision model.** Keyboard, focus, semantics, contrast, text alternatives dan responsive interaction mengikuti WCAG.

**Failure signature.** Plugin usable hanya via pointer/visual assumptions.

**Gate / evidence of mastery.** Relevant WCAG 2.2 checks dilakukan.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `WCAG`

### 11.N8 — OpenAI-specific extension restraint

**Decision model.** Gunakan sidebar/composer/file/settings/deep-link hanya jika workflow membutuhkannya dan ada fallback.

**Failure signature.** Extension membuat architecture hostage pada satu surface.

**Gate / evidence of mastery.** Host-specific value > portability cost.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-EXT`, `OAI-EXT-SPEC`

