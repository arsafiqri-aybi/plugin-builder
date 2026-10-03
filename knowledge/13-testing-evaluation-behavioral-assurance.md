# Lobe 13 — Testing, Evaluation & Behavioral Assurance

Membuktikan plugin bukan hanya valid secara struktur tetapi benar pada user workflow dan failure modes.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **testing, evaluation & behavioral assurance**. Do not load it merely because the project is large.

### 13.N1 — Test pyramid for plugins

**Decision model.** Gabungkan schema/unit, contract, integration, auth/security, host behavior, UI dan end-to-end user-job tests.

**Failure signature.** Hanya happy-path manual test.

**Gate / evidence of mastery.** Setiap critical property punya verifier channel.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `NIST-SSDF`

### 13.N2 — Tool contract tests

**Decision model.** Normal, boundary, invalid, auth denied, upstream error dan result schema diuji per tool.

**Failure signature.** Tool discovered tapi behavior tidak konsisten.

**Gate / evidence of mastery.** Contract tests deterministic dan repeatable.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`

### 13.N3 — Selection/trigger eval

**Decision model.** Natural prompts menguji tool/plugin dipilih saat tepat dan tidak dipilih pada negatives.

**Failure signature.** Correct tools tapi routing unreliable.

**Gate / evidence of mastery.** Positive/negative selection rate tracked.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INTERNAL-SKILL`

### 13.N4 — Workflow end-to-end eval

**Decision model.** Uji job completion lintas beberapa tools/state dengan observable final outcome.

**Failure signature.** Individual tool pass tetapi workflow gagal.

**Gate / evidence of mastery.** Pass condition user-centric.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-PROMPTING`

### 13.N5 — Security/adversarial eval

**Decision model.** Prompt injection, privilege escalation, malformed input, SSRF, cross-tenant, duplicate action, stale state.

**Failure signature.** Security hanya review statis.

**Gate / evidence of mastery.** Abuse cases menjadi regression suite.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-PI`, `OWASP-AGENT`

### 13.N6 — UI/host eval

**Decision model.** Verify actual render, controls, focus, placement, fallback dan state changes di intended host.

**Failure signature.** JSON result dianggap membuktikan UI sukses.

**Gate / evidence of mastery.** Visual/interaction evidence recorded.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-EXT`, `MCP-APPS`

### 13.N7 — Evaluation evidence classes

**Decision model.** Pisahkan static validation, deterministic tests, behavioral model eval, human review dan production telemetry.

**Failure signature.** Satu skor dijadikan klaim kualitas universal.

**Gate / evidence of mastery.** Report menyatakan jenis evidence dan limits.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `INTERNAL-GOV`

### 13.N8 — Regression memory

**Decision model.** Setiap fixed defect mendapat fixture/test minimal yang mencegah recurrence.

**Failure signature.** Bug lama kembali setelah refactor.

**Gate / evidence of mastery.** Change cannot pass gate if regression reappears.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `INTERNAL-GOV`

