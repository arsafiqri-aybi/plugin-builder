# Plugin Builder Knowledge Base

## Loading rule

1. Start with `SKILL.md`.
2. Use `references/` for operational procedures.
3. Load only lobes relevant to the current decision.
4. Within a lobe, load only neurons needed for the active uncertainty/failure.
5. Platform-dependent claims must be refreshed from current authoritative sources before release.

## Lobes

| Lobe | Domain | Purpose |
|---|---|---|
| `00` | [Epistemic Core & Research Method](00-epistemic-core-research-method.md) | Menentukan apa yang dianggap fakta platform, spesifikasi, praktik rekayasa, heuristik, atau hipotesis yang masih perlu diuji. |
| `01` | [Plugin Ontology & Host Mental Model](01-plugin-ontology-host-mental-model.md) | Memahami objek yang sedang dibangun dan batas antara package, Skill, MCP, App, Extension, host, dan backend. |
| `02` | [Requirements, Jobs & Product Contract](02-requirements-jobs-product-contract.md) | Mengubah keinginan pengguna menjadi kontrak plugin yang bisa dibangun dan diuji. |
| `03` | [Architecture & Capability Composition](03-architecture-capability-composition.md) | Memilih struktur terkecil yang dapat memenuhi kontrak kualitas tanpa overengineering. |
| `04` | [Packaging, Manifest & Compatibility](04-packaging-manifest-compatibility.md) | Membentuk package yang valid, portable, konsisten, dan aman untuk lifecycle target. |
| `05` | [MCP Protocol & Server Lifecycle](05-mcp-protocol-server-lifecycle.md) | Menguasai lifecycle protocol dan perilaku server agar plugin interoperable dan dapat didiagnosis. |
| `06` | [Tool Contract, Schema & Model Affordance](06-tool-contract-schema-model-affordance.md) | Merancang tools yang mudah dipilih model, sulit disalahgunakan, dan mudah dirangkai. |
| `07` | [Data, Retrieval, Context & Knowledge](07-data-retrieval-context-knowledge.md) | Mengatur bagaimana plugin mencari, mengirim, membatasi, dan menyegarkan data untuk model/user. |
| `08` | [Authentication, Identity & Authorization](08-authentication-identity-authorization.md) | Menjaga siapa yang bertindak, atas resource apa, dengan scope apa, dan bagaimana token divalidasi. |
| `09` | [Security, Threat Modeling & Prompt-Injection Resistance](09-security-threat-modeling-prompt-injection-resistance.md) | Mendesain defense-in-depth ketika model membaca data tak tepercaya dan memiliki tools. |
| `10` | [Side Effects, Transactions & Distributed Reliability](10-side-effects-transactions-distributed-reliability.md) | Mencegah duplicate effects, partial writes dan state corruption pada plugin yang bertindak di dunia nyata. |
| `11` | [MCP Apps, Extensions & Human-AI UX](11-mcp-apps-extensions-human-ai-ux.md) | Membuat UI yang benar-benar membantu, portable bila mungkin, accessible, dan jujur tentang state/AI limits. |
| `12` | [Privacy, Data Governance & Observability](12-privacy-data-governance-observability.md) | Menyimpan cukup data untuk fungsi/debugging tanpa memperluas risiko privasi. |
| `13` | [Testing, Evaluation & Behavioral Assurance](13-testing-evaluation-behavioral-assurance.md) | Membuktikan plugin bukan hanya valid secara struktur tetapi benar pada user workflow dan failure modes. |
| `14` | [Deployment, Performance & Operations](14-deployment-performance-operations.md) | Membawa plugin dari local/dev ke stable production dengan latency, availability, security dan rollback yang sesuai. |
| `15` | [Versioning, Update & Migration](15-versioning-update-migration.md) | Memperbarui plugin tanpa kehilangan identity, audience, data, compatibility atau behavior yang tidak diminta berubah. |
| `16` | [Distribution, Review & Publication](16-distribution-review-publication.md) | Menyiapkan plugin untuk private/workspace/public distribution dengan evidence dan metadata yang benar. |
| `17` | [Plugin Builder Meta-Engine & Neuron Orchestration](17-plugin-builder-meta-engine-neuron-orchestration.md) | Mengubah seluruh ilmu menjadi builder yang memilih neuron relevan, menghasilkan plugin, menguji, memperbaiki, dan berhenti dengan evidence. |
| `18` | [Architecture Search & Synthesis](18-architecture-search-synthesis.md) | Mencari topology yang layak, menyaring infeasible/dominated routes, mensimulasikan failure, dan memilih arsitektur paling sederhana yang memenuhi kontrak. |
| `19` | [Host Installation & Release Adaptation](19-host-installation-release-adaptation.md) | Memilih adapter install/update nyata, menjaga identity/state, dan memverifikasi persisted result serta host behavior tanpa mengarang capability. |

**Total: 20 lobes × 8 neurons = 160 neurons.**
