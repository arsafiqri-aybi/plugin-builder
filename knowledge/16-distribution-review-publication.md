# Lobe 16 — Distribution, Review & Publication

Menyiapkan plugin untuk private/workspace/public distribution dengan evidence dan metadata yang benar.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **distribution, review & publication**. Do not load it merely because the project is large.

### 16.N1 — Distribution mode decision

**Decision model.** Tentukan private, workspace, local marketplace, public directory berdasarkan audience dan risk.

**Failure signature.** Public submission overhead untuk internal-only plugin.

**Gate / evidence of mastery.** Distribution mode tercatat dalam contract.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-PKG`, `OAI-SUB`

### 16.N2 — Listing truthfulness

**Decision model.** Display name, descriptions, prompts, URLs, icons dan capabilities harus menggambarkan implementation nyata.

**Failure signature.** Marketing menjanjikan capability yang tidak ada.

**Gate / evidence of mastery.** Listing-to-test mapping tersedia.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `OAI-GUIDE`

### 16.N3 — Publisher identity and URLs

**Decision model.** Publisher verified; website/support/privacy/terms accessible dan relevan.

**Failure signature.** Placeholder/guessed URL atau identity mismatch.

**Gate / evidence of mastery.** URL content inspected, bukan hanya HTTP 200.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INSTALLED-CREATOR`

### 16.N4 — Review case design

**Decision model.** Positive cases distinct; negative cases plausible neighbors; expected tools/arguments/outcome observable.

**Failure signature.** Cases berupa paraphrase atau vague works-correctly.

**Gate / evidence of mastery.** Coverage map + reproducible setup.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`, `OAI-SUB`

### 16.N5 — Demo evidence

**Decision model.** Demo menunjukkan actual packaged behavior dengan readable prompts/results dan no secrets.

**Failure signature.** Script/mockup dianggap recording.

**Gate / evidence of mastery.** Recording link verified reviewer-accessible.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`

### 16.N6 — Reviewer access

**Decision model.** Dedicated test account/sample data + exact login steps tanpa private mailbox/phone dependency.

**Failure signature.** Reviewer tidak dapat menjalankan cases.

**Gate / evidence of mastery.** Access rehearsed end-to-end.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INSTALLED-CREATOR`

### 16.N7 — Draft/review/publish state machine

**Decision model.** Upload draft, submit review, approval, publish adalah state berbeda dengan authorization berbeda.

**Failure signature.** Upload success disebut published.

**Gate / evidence of mastery.** Final report menyebut actual state.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `INSTALLED-CREATOR`

### 16.N8 — Post-publication maintenance

**Decision model.** Tool/server changes, metadata/skill releases, scans, incidents dan deprecation punya process berkelanjutan.

**Failure signature.** Plugin published lalu tak dipelihara.

**Gate / evidence of mastery.** Maintenance owner + refresh cadence + rollback path.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-SUB`, `NIST-SSDF`

