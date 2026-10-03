# Lobe 09 — Security, Threat Modeling & Prompt-Injection Resistance

Mendesain defense-in-depth ketika model membaca data tak tepercaya dan memiliki tools.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **security, threat modeling & prompt-injection resistance**. Do not load it merely because the project is large.

### 09.N1 — Threat model assets/actors

**Decision model.** Daftar asset, attacker, entry point, trust boundary, privileged action dan abuse case.

**Failure signature.** Security hanya berupa checklist generik.

**Gate / evidence of mastery.** Threat model terikat arsitektur nyata.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `OWASP-AGENT`

### 09.N2 — Direct and indirect prompt injection

**Decision model.** Perlakukan user/retrieved/tool content sebagai data yang tidak menaikkan authority.

**Failure signature.** Dokumen eksternal menyuruh model mengirim secret atau mengubah tujuan.

**Gate / evidence of mastery.** Injection cases tidak memicu privileged action.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-PI`, `INTERNAL-PROMPTING`

### 09.N3 — Action-intent binding

**Decision model.** Consequential tool call harus konsisten dengan original user intent, bukan instruksi dari untrusted intermediate content.

**Failure signature.** Confused deputy melakukan aksi untuk attacker.

**Gate / evidence of mastery.** Action policy memeriksa intent + authority + arguments.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-PI`, `OWASP-AGENT`

### 09.N4 — Privilege separation

**Decision model.** Pisahkan parsing untrusted content dari privileged execution bila risk tinggi.

**Failure signature.** Satu agent membaca malicious content sekaligus punya broad tools.

**Gate / evidence of mastery.** High-risk path memakai constrained parser/guarded executor pattern.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-PI`

### 09.N5 — Input/output validation

**Decision model.** Semua tool input dan upstream response divalidasi; HTML/URL/path/command tidak dipercaya.

**Failure signature.** Injection tradisional, SSRF, path traversal, command injection.

**Gate / evidence of mastery.** Security test suite mencakup malformed/malicious inputs.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `NIST-SSDF`

### 09.N6 — SSRF and outbound controls

**Decision model.** Batasi destination, protocol, DNS/IP class, redirects dan metadata endpoints untuk tools yang fetch URL.

**Failure signature.** Tool menjadi generic network pivot.

**Gate / evidence of mastery.** Allowlist/policy + redirect checks tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OWASP-AGENT`, `NIST-SSDF`

### 09.N7 — Supply-chain security

**Decision model.** Pin/review dependencies, SDK releases, build provenance dan vulnerability response.

**Failure signature.** Compromised dependency masuk plugin release.

**Gate / evidence of mastery.** Dependency inventory + update policy + scan gate.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`

### 09.N8 — Fail-closed boundaries

**Decision model.** Pada uncertainty authorization/integrity untuk action sensitif, berhenti aman dan minta recovery yang tepat.

**Failure signature.** System meneruskan karena ingin menyelesaikan task.

**Gate / evidence of mastery.** Risk gate dapat menghasilkan FAIL_CLOSED.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-GOV`

