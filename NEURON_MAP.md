# Plugin Builder Neuron Map

## Global architecture

```text
USER JOB / EXISTING PLUGIN
        ↓
Requirements & evidence
        ↓
Architecture / capability placement
        ↓
Package + MCP + Tool + Auth + Security + UI
        ↓
Implementation & operations
        ↓
Testing / adversarial evaluation / host verification
        ↓
Repair loop
        ↓
Packaging / update / review / publication
        ↓
Maintenance & learning
```

## Neuron graph

Each neuron has: **decision → failure signal → quality gate → synapses → evidence sources**.

- **00.N1 Source authority graph** → sources: OAI-PKG, MCP-SPEC, AGENT-PLUGINS, INTERNAL-SKILL
- **00.N2 Freshness and version discipline** → sources: OAI-EXT, OAI-SUB, MCP-APPS
- **00.N3 Normative language parsing** → sources: MCP-SPEC, AGENT-PLUGINS
- **00.N4 Evidence-to-decision trace** → sources: INTERNAL-PROMPTING, INTERNAL-SCALE
- **00.N5 Uncertainty ledger** → sources: INTERNAL-PROMPTING, INTERNAL-GOV
- **00.N6 Counterexample search** → sources: INTERNAL-SKILL, HAX
- **00.N7 Failure-driven learning** → sources: INTERNAL-GOV, NIST-SSDF
- **00.N8 Knowledge promotion gate** → sources: INTERNAL-SKILL, INTERNAL-PROMPTING

### Lobe 00 — Epistemic Core & Research Method
- Purpose: Menentukan apa yang dianggap fakta platform, spesifikasi, praktik rekayasa, heuristik, atau hipotesis yang masih perlu diuji.
- File: `knowledge/00-epistemic-core-research-method.md`

- **01.N1 Plugin as capability package** → sources: OAI-PKG, AGENT-PLUGINS
- **01.N2 Skill vs tool vs resource vs prompt** → sources: MCP-SPEC, INTERNAL-SKILL
- **01.N3 MCP server boundary** → sources: OAI-MCP, OAI-AUTH
- **01.N4 MCP App boundary** → sources: MCP-APPS, OAI-QUICK
- **01.N5 Extension boundary** → sources: OAI-EXT, OAI-EXT-SPEC
- **01.N6 Local vs cloud vs existing server** → sources: INSTALLED-CREATOR, OAI-MCP
- **01.N7 Private/workspace/public lifecycle** → sources: OAI-SUB, INSTALLED-CREATOR
- **01.N8 Host capability negotiation** → sources: MCP-APPS, OAI-EXT

### Lobe 01 — Plugin Ontology & Host Mental Model
- Purpose: Memahami objek yang sedang dibangun dan batas antara package, Skill, MCP, App, Extension, host, dan backend.
- File: `knowledge/01-plugin-ontology-host-mental-model.md`

- **02.N1 User job definition** → sources: INTERNAL-PROMPTING, HAX
- **02.N2 Actor and authority map** → sources: OAI-AUTH, INSTALLED-CREATOR
- **02.N3 Input/output contract** → sources: JSON-SCHEMA, OAI-MCP
- **02.N4 Supported and unsupported intents** → sources: OAI-SUB, INTERNAL-SKILL
- **02.N5 Acceptance criteria hierarchy** → sources: INTERNAL-SCALE, INTERNAL-GOV
- **02.N6 Reversibility and consequence** → sources: OAI-MCP, OWASP-AGENT
- **02.N7 Environment constraints** → sources: INTERNAL-SCALE, OAI-MCP
- **02.N8 Definition of done** → sources: INTERNAL-SKILL, OAI-SUB

### Lobe 02 — Requirements, Jobs & Product Contract
- Purpose: Mengubah keinginan pengguna menjadi kontrak plugin yang bisa dibangun dan diuji.
- File: `knowledge/02-requirements-jobs-product-contract.md`

- **03.N1 Capability placement** → sources: MCP-SPEC, OAI-PKG
- **03.N2 Architecture topology** → sources: INSTALLED-CREATOR, INTERNAL-SCALE
- **03.N3 Dependency graph** → sources: INTERNAL-SCALE, NIST-SSDF
- **03.N4 State ownership** → sources: MCP-APPS, INTERNAL-GOV
- **03.N5 Trust boundaries** → sources: OWASP-PI, OWASP-AGENT
- **03.N6 Portability vs specialization** → sources: MCP-APPS, OAI-EXT
- **03.N7 Graceful degradation** → sources: MCP-APPS, INTERNAL-GOV
- **03.N8 Architecture decision records** → sources: NIST-SSDF, INTERNAL-SCALE

### Lobe 03 — Architecture & Capability Composition
- Purpose: Memilih struktur terkecil yang dapat memenuhi kontrak kualitas tanpa overengineering.
- File: `knowledge/03-architecture-capability-composition.md`

- **04.N1 Canonical root manifest** → sources: AGENT-PLUGINS, OAI-PKG
- **04.N2 Portable component locations** → sources: OAI-PKG, INSTALLED-CREATOR
- **04.N3 OpenAI extension namespace** → sources: OAI-PKG, OAI-SUB
- **04.N4 Semantic version discipline** → sources: INSTALLED-CREATOR, NIST-SSDF
- **04.N5 Asset integrity** → sources: INSTALLED-CREATOR, OAI-SUB
- **04.N6 Compatibility overlay** → sources: INSTALLED-CREATOR, AGENT-PLUGINS
- **04.N7 Package reproducibility** → sources: NIST-SSDF, INTERNAL-SKILL
- **04.N8 Secret exclusion** → sources: OAI-SUB, NIST-SSDF

### Lobe 04 — Packaging, Manifest & Compatibility
- Purpose: Membentuk package yang valid, portable, konsisten, dan aman untuk lifecycle target.
- File: `knowledge/04-packaging-manifest-compatibility.md`

- **05.N1 Initialization and capability negotiation** → sources: MCP-SPEC, MCP-APPS
- **05.N2 Tool lifecycle** → sources: OAI-MCP, MCP-SPEC
- **05.N3 Resources and prompts** → sources: MCP-SPEC
- **05.N4 Transport selection** → sources: OAI-MCP, INSTALLED-CREATOR
- **05.N5 Progress/cancellation/tasks** → sources: MCP-SPEC, NNG
- **05.N6 Error taxonomy** → sources: OAI-MCP, INTERNAL-GOV
- **05.N7 Protocol observability** → sources: OAI-MCP, NIST-SSDF
- **05.N8 Backward-compatible evolution** → sources: OAI-MCP, INTERNAL-SCALE

### Lobe 05 — MCP Protocol & Server Lifecycle
- Purpose: Menguasai lifecycle protocol dan perilaku server agar plugin interoperable dan dapat didiagnosis.
- File: `knowledge/05-mcp-protocol-server-lifecycle.md`

- **06.N1 Goal-shaped tool granularity** → sources: OAI-MCP, INTERNAL-PROMPTING
- **06.N2 Naming and description semantics** → sources: OAI-MCP, INTERNAL-SKILL
- **06.N3 Input schema design** → sources: JSON-SCHEMA, OAI-MCP
- **06.N4 Structured result design** → sources: OAI-MCP
- **06.N5 Annotation truthfulness** → sources: OAI-MCP, INSTALLED-CREATOR
- **06.N6 Elicitation boundary** → sources: OAI-MCP
- **06.N7 Tool chaining contract** → sources: OAI-MCP, INTERNAL-SCALE
- **06.N8 Selection collision testing** → sources: OAI-SUB, INTERNAL-SKILL

### Lobe 06 — Tool Contract, Schema & Model Affordance
- Purpose: Merancang tools yang mudah dipilih model, sulit disalahgunakan, dan mudah dirangkai.
- File: `knowledge/06-tool-contract-schema-model-affordance.md`

- **07.N1 Data source authority** → sources: INTERNAL-PROMPTING, INTERNAL-GOV
- **07.N2 Search/fetch architecture** → sources: OAI-MCP
- **07.N3 Context minimization** → sources: INTERNAL-GOV, OAI-MCP
- **07.N4 Freshness policy** → sources: INTERNAL-GOV
- **07.N5 Provenance and citations** → sources: OAI-MCP, INTERNAL-PROMPTING
- **07.N6 Pagination and bounded retrieval** → sources: MCP-SPEC, INTERNAL-GOV
- **07.N7 Multi-account isolation** → sources: OAI-MCP, OAI-AUTH
- **07.N8 Knowledge update lifecycle** → sources: OAI-MCP, OAI-SUB

### Lobe 07 — Data, Retrieval, Context & Knowledge
- Purpose: Mengatur bagaimana plugin mencari, mengirim, membatasi, dan menyegarkan data untuk model/user.
- File: `knowledge/07-data-retrieval-context-knowledge.md`

- **08.N1 Authentication necessity decision** → sources: OAI-AUTH, HAX
- **08.N2 Resource vs authorization server** → sources: RFC-9728, RFC-8414
- **08.N3 PKCE and modern OAuth posture** → sources: OAI-AUTH, RFC-9700
- **08.N4 Token validation** → sources: OAI-AUTH, RFC-9728
- **08.N5 Scope design** → sources: OAI-AUTH, OWASP-AGENT
- **08.N6 Authorization policy** → sources: OAI-MCP, OWASP-AGENT
- **08.N7 Credential lifecycle** → sources: NIST-SSDF, OAI-MCP
- **08.N8 Multi-account UX** → sources: OAI-MCP, HAX

### Lobe 08 — Authentication, Identity & Authorization
- Purpose: Menjaga siapa yang bertindak, atas resource apa, dengan scope apa, dan bagaimana token divalidasi.
- File: `knowledge/08-authentication-identity-authorization.md`

- **09.N1 Threat model assets/actors** → sources: NIST-SSDF, OWASP-AGENT
- **09.N2 Direct and indirect prompt injection** → sources: OWASP-PI, INTERNAL-PROMPTING
- **09.N3 Action-intent binding** → sources: OWASP-PI, OWASP-AGENT
- **09.N4 Privilege separation** → sources: OWASP-PI
- **09.N5 Input/output validation** → sources: OAI-MCP, NIST-SSDF
- **09.N6 SSRF and outbound controls** → sources: OWASP-AGENT, NIST-SSDF
- **09.N7 Supply-chain security** → sources: NIST-SSDF
- **09.N8 Fail-closed boundaries** → sources: INTERNAL-SCALE, INTERNAL-GOV

### Lobe 09 — Security, Threat Modeling & Prompt-Injection Resistance
- Purpose: Mendesain defense-in-depth ketika model membaca data tak tepercaya dan memiliki tools.
- File: `knowledge/09-security-threat-modeling-prompt-injection-resistance.md`

- **10.N1 Idempotency classification** → sources: OAI-MCP, INTERNAL-GOV
- **10.N2 Idempotency keys** → sources: INTERNAL-GOV
- **10.N3 Optimistic concurrency** → sources: INSTALLED-CREATOR, NIST-SSDF
- **10.N4 Partial failure semantics** → sources: INTERNAL-SCALE, INTERNAL-GOV
- **10.N5 State inspection before retry** → sources: INTERNAL-GOV
- **10.N6 Timeout/backoff/circuit breaker** → sources: NIST-SSDF, INTERNAL-GOV
- **10.N7 Compensation and rollback** → sources: INTERNAL-SCALE
- **10.N8 Consistency visibility** → sources: NNG, INTERNAL-GOV

### Lobe 10 — Side Effects, Transactions & Distributed Reliability
- Purpose: Mencegah duplicate effects, partial writes dan state corruption pada plugin yang bertindak di dunia nyata.
- File: `knowledge/10-side-effects-transactions-distributed-reliability.md`

- **11.N1 UI necessity test** → sources: MCP-APPS, HAX
- **11.N2 Progressive enhancement** → sources: MCP-APPS
- **11.N3 Capability negotiation** → sources: MCP-APPS, OAI-EXT-SPEC
- **11.N4 System status visibility** → sources: NNG, HAX
- **11.N5 User control and reversibility** → sources: NNG, HAX
- **11.N6 AI uncertainty and correction** → sources: HAX
- **11.N7 Accessibility** → sources: WCAG
- **11.N8 OpenAI-specific extension restraint** → sources: OAI-EXT, OAI-EXT-SPEC

### Lobe 11 — MCP Apps, Extensions & Human-AI UX
- Purpose: Membuat UI yang benar-benar membantu, portable bila mungkin, accessible, dan jujur tentang state/AI limits.
- File: `knowledge/11-mcp-apps-extensions-human-ai-ux.md`

- **12.N1 Data inventory** → sources: OAI-GUIDE, NIST-SSDF
- **12.N2 Data minimization** → sources: OAI-MCP, OWASP-AGENT
- **12.N3 Retention and deletion** → sources: OAI-SUB, NIST-SSDF
- **12.N4 Log hygiene** → sources: OAI-MCP, NIST-SSDF
- **12.N5 Audit trail** → sources: OWASP-AGENT, NIST-SSDF
- **12.N6 Telemetry purpose limitation** → sources: OAI-GUIDE
- **12.N7 Tenant isolation** → sources: OAI-AUTH, OWASP-AGENT
- **12.N8 Policy truthfulness** → sources: OAI-SUB, INSTALLED-CREATOR

### Lobe 12 — Privacy, Data Governance & Observability
- Purpose: Menyimpan cukup data untuk fungsi/debugging tanpa memperluas risiko privasi.
- File: `knowledge/12-privacy-data-governance-observability.md`

- **13.N1 Test pyramid for plugins** → sources: OAI-MCP, NIST-SSDF
- **13.N2 Tool contract tests** → sources: OAI-MCP
- **13.N3 Selection/trigger eval** → sources: OAI-SUB, INTERNAL-SKILL
- **13.N4 Workflow end-to-end eval** → sources: INTERNAL-SCALE, INTERNAL-PROMPTING
- **13.N5 Security/adversarial eval** → sources: OWASP-PI, OWASP-AGENT
- **13.N6 UI/host eval** → sources: OAI-EXT, MCP-APPS
- **13.N7 Evaluation evidence classes** → sources: INTERNAL-SKILL, INTERNAL-GOV
- **13.N8 Regression memory** → sources: NIST-SSDF, INTERNAL-GOV

### Lobe 13 — Testing, Evaluation & Behavioral Assurance
- Purpose: Membuktikan plugin bukan hanya valid secara struktur tetapi benar pada user workflow dan failure modes.
- File: `knowledge/13-testing-evaluation-behavioral-assurance.md`

- **14.N1 Environment parity** → sources: OAI-MCP, NIST-SSDF
- **14.N2 Stable endpoint and TLS** → sources: OAI-MCP, OAI-SUB
- **14.N3 Latency budget** → sources: OAI-MCP, INTERNAL-GOV
- **14.N4 Rate limiting and quotas** → sources: OAI-MCP, OWASP-AGENT
- **14.N5 Caching with semantics** → sources: INTERNAL-GOV
- **14.N6 Health and readiness** → sources: NIST-SSDF
- **14.N7 Rollback strategy** → sources: NIST-SSDF, INTERNAL-SCALE
- **14.N8 Incident response** → sources: NIST-SSDF, INTERNAL-GOV

### Lobe 14 — Deployment, Performance & Operations
- Purpose: Membawa plugin dari local/dev ke stable production dengan latency, availability, security dan rollback yang sesuai.
- File: `knowledge/14-deployment-performance-operations.md`

- **15.N1 Source-of-truth resolution** → sources: INSTALLED-CREATOR, INTERNAL-SKILL
- **15.N2 Identity preservation** → sources: INSTALLED-CREATOR
- **15.N3 Concurrent update guard** → sources: INSTALLED-CREATOR, INTERNAL-GOV
- **15.N4 Schema migration** → sources: INSTALLED-CREATOR, AGENT-PLUGINS
- **15.N5 Server vs package update** → sources: OAI-SUB, OAI-MCP
- **15.N6 Backward compatibility** → sources: OAI-MCP
- **15.N7 Data migration safety** → sources: NIST-SSDF
- **15.N8 Read-back verification** → sources: INSTALLED-CREATOR, INTERNAL-PROMPTING

### Lobe 15 — Versioning, Update & Migration
- Purpose: Memperbarui plugin tanpa kehilangan identity, audience, data, compatibility atau behavior yang tidak diminta berubah.
- File: `knowledge/15-versioning-update-migration.md`

- **16.N1 Distribution mode decision** → sources: OAI-PKG, OAI-SUB
- **16.N2 Listing truthfulness** → sources: OAI-SUB, OAI-GUIDE
- **16.N3 Publisher identity and URLs** → sources: OAI-SUB, INSTALLED-CREATOR
- **16.N4 Review case design** → sources: INSTALLED-CREATOR, OAI-SUB
- **16.N5 Demo evidence** → sources: INSTALLED-CREATOR
- **16.N6 Reviewer access** → sources: INSTALLED-CREATOR
- **16.N7 Draft/review/publish state machine** → sources: OAI-SUB, INSTALLED-CREATOR
- **16.N8 Post-publication maintenance** → sources: OAI-SUB, NIST-SSDF

### Lobe 16 — Distribution, Review & Publication
- Purpose: Menyiapkan plugin untuk private/workspace/public distribution dengan evidence dan metadata yang benar.
- File: `knowledge/16-distribution-review-publication.md`

- **17.N1 Intent-to-neuron routing** → sources: INTERNAL-SKILL, INTERNAL-GOV
- **17.N2 Builder contract synthesis** → sources: INTERNAL-PROMPTING, INTERNAL-SCALE
- **17.N3 Scaffold from architecture** → sources: INTERNAL-SKILL, OAI-PKG
- **17.N4 Generate then verify loop** → sources: INTERNAL-SKILL, INTERNAL-SCALE
- **17.N5 Diagnosis before repair** → sources: INTERNAL-GOV
- **17.N6 Quality-floor stopping** → sources: INTERNAL-GOV, INTERNAL-SCALE
- **17.N7 Self-contained expertise** → sources: INTERNAL-SKILL, INSTALLED-CREATOR
- **17.N8 Learning and maintenance loop** → sources: NIST-SSDF, INTERNAL-SKILL

### Lobe 17 — Plugin Builder Meta-Engine & Neuron Orchestration
- Purpose: Mengubah seluruh ilmu menjadi builder yang memilih neuron relevan, menghasilkan plugin, menguji, memperbaiki, dan berhenti dengan evidence.
- File: `knowledge/17-plugin-builder-meta-engine-neuron-orchestration.md`


- **18.N1 Candidate topology generation** → sources: INTERNAL-SCALE, OAI-PKG, OAI-MCP
- **18.N2 Feasibility filtering** → sources: INTERNAL-SCALE, OAI-PKG, OAI-MCP, OAI-AUTH
- **18.N3 Dominance pruning** → sources: INTERNAL-SCALE, INTERNAL-GOV, NIST-SSDF
- **18.N4 Quality-attribute trade-off map** → sources: INTERNAL-SCALE, INTERNAL-GOV, NIST-SSDF, HAX
- **18.N5 Failure-mode simulation** → sources: OWASP-AGENT, NIST-SSDF, INTERNAL-GOV
- **18.N6 Build-versus-reuse decision** → sources: OAI-MCP, INSTALLED-CREATOR, NIST-SSDF
- **18.N7 Evolution runway** → sources: NIST-SSDF, OAI-MCP, INTERNAL-SCALE
- **18.N8 Architecture proof and decision record** → sources: INTERNAL-SCALE, INTERNAL-SKILL, NIST-SSDF

### Lobe 18 — Architecture Search & Synthesis
- Purpose: Mencari beberapa topology yang layak, menyaring infeasible/dominated routes, mensimulasikan failure, dan memilih arsitektur paling sederhana yang memenuhi kontrak.
- File: `knowledge/18-architecture-search-synthesis.md`

- **19.N1 Host capability discovery** → sources: OAI-PKG, OAI-SUB, INSTALLED-CREATOR
- **19.N2 Installation adapter selection** → sources: INSTALLED-CREATOR, OAI-PKG, OAI-SUB
- **19.N3 Artifact normalization per adapter** → sources: OAI-PKG, AGENT-PLUGINS, INSTALLED-CREATOR
- **19.N4 Mutation authorization boundary** → sources: INTERNAL-PROMPTING, INTERNAL-SKILL, OAI-SUB
- **19.N5 Guarded create/update** → sources: INSTALLED-CREATOR, INTERNAL-GOV
- **19.N6 Connection and authentication handoff** → sources: OAI-MCP, OAI-AUTH, OAI-SUB
- **19.N7 Read-back and smoke verification** → sources: INSTALLED-CREATOR, INTERNAL-SKILL, INTERNAL-PROMPTING
- **19.N8 Adapter failure recovery** → sources: INTERNAL-GOV, INSTALLED-CREATOR, INTERNAL-SKILL

### Lobe 19 — Host Installation & Release Adaptation
- Purpose: Memilih adapter install/update nyata, menjaga identity/state, dan memverifikasi persisted result serta host behavior tanpa mengarang capability.
- File: `knowledge/19-host-installation-release-adaptation.md`
