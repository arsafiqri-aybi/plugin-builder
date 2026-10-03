# Lobe 02 — Requirements, Jobs & Product Contract

Mengubah keinginan pengguna menjadi kontrak plugin yang bisa dibangun dan diuji.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **requirements, jobs & product contract**. Do not load it merely because the project is large.

### 02.N1 — User job definition

**Decision model.** Definisikan pekerjaan pengguna, bukan daftar fitur.

**Failure signature.** Feature-rich plugin tanpa job yang jelas.

**Gate / evidence of mastery.** Satu kalimat job + outcome yang dapat diamati.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-PROMPTING`, `HAX`

### 02.N2 — Actor and authority map

**Decision model.** Identifikasi user, workspace, external account, reviewer, admin dan sistem yang punya authority berbeda.

**Failure signature.** Plugin bertindak sebagai user yang salah atau scope salah.

**Gate / evidence of mastery.** Authority matrix ada untuk semua action sensitif.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-AUTH`, `INSTALLED-CREATOR`

### 02.N3 — Input/output contract

**Decision model.** Tentukan input wajib/opsional, structured output, identifiers, errors dan evidence.

**Failure signature.** Tool memerlukan tebakan atau output sulit dipakai tool berikutnya.

**Gate / evidence of mastery.** Kontrak I/O dapat divalidasi dan dirangkai.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `JSON-SCHEMA`, `OAI-MCP`

### 02.N4 — Supported and unsupported intents

**Decision model.** Tulis positive, adjacent-negative, out-of-scope, auth-error dan no-result scenarios.

**Failure signature.** Plugin terlalu sering terpicu atau memalsukan kemampuan.

**Gate / evidence of mastery.** Set kasus mencakup supported + plausible unsupported.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INTERNAL-SKILL`

### 02.N5 — Acceptance criteria hierarchy

**Decision model.** Pisahkan critical, important, optional, usability dan operational criteria.

**Failure signature.** Polish UI menutupi kegagalan authorization atau correctness.

**Gate / evidence of mastery.** Critical gates tidak bisa diturunkan oleh optimisasi.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`, `INTERNAL-GOV`

### 02.N6 — Reversibility and consequence

**Decision model.** Klasifikasi read, reversible write, destructive write, financial/external effect.

**Failure signature.** Confirmation dan retry sama untuk semua action.

**Gate / evidence of mastery.** Risk class memengaruhi UX, idempotency, approval dan logging.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OWASP-AGENT`

### 02.N7 — Environment constraints

**Decision model.** Petakan host, network, local files, auth provider, data residency, deployment, runtime dan SDK.

**Failure signature.** Desain tidak bisa dijalankan pada target surface.

**Gate / evidence of mastery.** Feasibility check dilakukan sebelum implementasi.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SCALE`, `OAI-MCP`

### 02.N8 — Definition of done

**Decision model.** Selesai berarti package valid + behavior tested + effects verified sesuai scope, bukan sekadar file ada.

**Failure signature.** Mengklaim plugin selesai setelah scaffold.

**Gate / evidence of mastery.** Done status punya evidence checklist dan explicit unverified items.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `OAI-SUB`

