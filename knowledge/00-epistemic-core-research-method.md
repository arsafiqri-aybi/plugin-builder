# Lobe 00 — Epistemic Core & Research Method

Menentukan apa yang dianggap fakta platform, spesifikasi, praktik rekayasa, heuristik, atau hipotesis yang masih perlu diuji.

## Lobe decision flow

Use this lobe when the active build uncertainty is primarily about **epistemic core & research method**. Do not load it merely because the project is large.

### 00.N1 — Source authority graph

**Decision model.** Klasifikasikan sumber menjadi spesifikasi normatif, dokumentasi produk, standar keamanan, riset HCI, implementasi contoh, dan heuristik internal.

**Failure signature.** Menganggap contoh atau dokumentasi lama sebagai aturan universal.

**Gate / evidence of mastery.** Setiap aturan penting memiliki kelas bukti, tanggal, dan sumber pembaruan.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-PKG`, `MCP-SPEC`, `AGENT-PLUGINS`, `INTERNAL-SKILL`

### 00.N2 — Freshness and version discipline

**Decision model.** Pisahkan prinsip stabil dari fakta yang cepat berubah seperti surface support, submission rules, SDK API, schema version, dan limits.

**Failure signature.** Hard-code matriks dukungan atau batas platform tanpa tanggal.

**Gate / evidence of mastery.** Fakta dinamis menyimpan checked_at dan refresh trigger.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `OAI-EXT`, `OAI-SUB`, `MCP-APPS`

### 00.N3 — Normative language parsing

**Decision model.** Bedakan MUST/SHOULD/MAY dari saran produk atau keputusan desain lokal.

**Failure signature.** Mengubah rekomendasi menjadi kewajiban atau mengabaikan MUST.

**Gate / evidence of mastery.** Keputusan menyebut apakah berasal dari spec, policy, atau heuristic.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `MCP-SPEC`, `AGENT-PLUGINS`

### 00.N4 — Evidence-to-decision trace

**Decision model.** Hubungkan keputusan arsitektur, auth, tool schema, UI dan publishing ke bukti yang mendukung.

**Failure signature.** Keputusan penting tidak dapat ditelusuri saat terjadi regresi.

**Gate / evidence of mastery.** Setiap keputusan material punya rationale + evidence refs.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-PROMPTING`, `INTERNAL-SCALE`

### 00.N5 — Uncertainty ledger

**Decision model.** Catat ketidakpastian material, cara membuktikan, dan dampaknya bila salah.

**Failure signature.** AI menutup gap dengan asumsi yang terdengar pasti.

**Gate / evidence of mastery.** Unknown tetap unknown sampai ada verifikasi atau keputusan eksplisit.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-PROMPTING`, `INTERNAL-GOV`

### 00.N6 — Counterexample search

**Decision model.** Untuk setiap pola desain, cari situasi ketika pola itu tidak cocok.

**Failure signature.** Satu pola dipakai ke semua plugin karena berhasil pada contoh pertama.

**Gate / evidence of mastery.** Ada minimal satu anti-pattern/counterexample untuk keputusan besar.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `HAX`

### 00.N7 — Failure-driven learning

**Decision model.** Jadikan kegagalan build/test/review sebagai data untuk memperbaiki neuron yang tepat.

**Failure signature.** Menambah aturan global setelah satu bug lokal.

**Gate / evidence of mastery.** Root cause dipetakan ke neuron dan regression case spesifik.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-GOV`, `NIST-SSDF`

### 00.N8 — Knowledge promotion gate

**Decision model.** Pisahkan riset mentah, canonical knowledge, runtime instruction, dan test fixture.

**Failure signature.** Riset panjang langsung dimasukkan ke runtime sehingga context bloat.

**Gate / evidence of mastery.** Hanya keputusan runtime yang stabil dipromosikan ke SKILL.md.

**Synapses.** This neuron should exchange state with the requirement contract, architecture graph, risk model, and verifier that depend on this decision; escalate to another lobe when the root cause leaves this domain.

**Primary sources.** `INTERNAL-SKILL`, `INTERNAL-PROMPTING`

