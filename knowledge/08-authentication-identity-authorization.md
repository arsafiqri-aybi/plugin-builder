# Lobe 08 — Authentication, Identity & Authorization

Menjaga siapa yang bertindak, atas resource apa, dengan scope apa, dan bagaimana token divalidasi.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **authentication, identity & authorization**. Do not load it merely because the project is large.

### 08.N1 — Authentication necessity decision

**Decision model.** Anonymous hanya untuk data/action yang aman publik; private data/write membutuhkan auth.

**Failure signature.** Over-auth menambah friction atau under-auth membuka data.

**Gate / evidence of mastery.** Auth requirement ditentukan per tool/resource.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-AUTH`, `HAX`

### 08.N2 — Resource vs authorization server

**Decision model.** Pisahkan MCP resource server dan authorization server dengan discovery metadata yang benar.

**Failure signature.** Client diarahkan ke issuer/resource yang salah.

**Gate / evidence of mastery.** Resource metadata dan AS metadata konsisten.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `RFC-9728`, `RFC-8414`

### 08.N3 — PKCE and modern OAuth posture

**Decision model.** Gunakan authorization code + PKCE dan security BCP sesuai contract platform.

**Failure signature.** Legacy flow rentan interception/misconfiguration.

**Gate / evidence of mastery.** Flow diuji terhadap redirect/state/token handling.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-AUTH`, `RFC-9700`

### 08.N4 — Token validation

**Decision model.** Validasi issuer, audience/resource, expiry, signature, scopes dan claims per request.

**Failure signature.** Token valid secara kriptografis tetapi untuk resource lain.

**Gate / evidence of mastery.** Unauthorized scope/resource selalu ditolak server-side.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-AUTH`, `RFC-9728`

### 08.N5 — Scope design

**Decision model.** Scope minimal, meaningful, separable read/write/admin, dan tidak lebih luas dari job.

**Failure signature.** Broad scope menjadi blast radius besar.

**Gate / evidence of mastery.** Tool-to-scope matrix memenuhi least privilege.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-AUTH`, `OWASP-AGENT`

### 08.N6 — Authorization policy

**Decision model.** Object-level/tenant-level authorization dilakukan pada backend terhadap validated identity.

**Failure signature.** IDOR/cross-tenant access melalui tool args.

**Gate / evidence of mastery.** Negative authorization tests lulus.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `OWASP-AGENT`

### 08.N7 — Credential lifecycle

**Decision model.** Secret/token disimpan di secret store, rotation/revocation/error path jelas.

**Failure signature.** Token muncul di logs, package atau model result.

**Gate / evidence of mastery.** Secret exposure scan + revoke path tested.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `NIST-SSDF`, `OAI-MCP`

### 08.N8 — Multi-account UX

**Decision model.** Account identity harus terlihat cukup untuk mencegah aksi pada akun salah tanpa mengekspos data berlebihan.

**Failure signature.** User menyangka plugin bertindak di akun lain.

**Gate / evidence of mastery.** Profile/read-only identity path dan confirmation context jelas.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-MCP`, `HAX`

