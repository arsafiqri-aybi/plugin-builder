# Lobe 20 — Plugin Lifecycle Execution & Creator Parity

Menjamin Plugin Builder mencakup seluruh lifecycle operasional yang dilakukan Plugin Creator: membuat plugin baru, menemukan dan menginspeksi plugin existing, membaca source/release history, memperbarui secara guarded, menangani cloud/local/existing-MCP routes, dan menyiapkan submission/publication. Privileged account mutation tetap harus menggunakan host action nyata; knowledge tidak boleh mengarang permission.

## Lobe decision flow

Use this lobe when the task asks to create/save/install, inspect, update, recover, migrate, package for submission, submit, or publish a plugin. Pair it with lobe 19 for adapter discovery and with lobe 16 for public distribution.

### 20.N1 — Creator capability inventory

**Decision model.** Normalize lifecycle requests into concrete capabilities: create private plugin, inspect metadata/files, retrieve archive/history, list releases, guarded update, cloud/local/existing-MCP routing, and public-submission preparation.

**Failure signature.** Plugin Builder claims parity while one or more lifecycle families remain unsupported or undefined.

**Gate / evidence of mastery.** The parity matrix maps every baseline Plugin Creator workflow to a Plugin Builder workflow and evidence requirement.

**Synapses.** Exchange state with 01 host ontology, 15 update/migration, 16 distribution, 19 adapters, and 20.N8 parity regression.

**Primary sources.** `INSTALLED-CREATOR`, `OAI-PKG`, `OAI-SUB`

### 20.N2 — Create-private execution contract

**Decision model.** When the user requests account installation of a completed standalone package, prefer the real authenticated private-plugin create action exposed by the host. Validate the package first, avoid duplicate creation, perform the mutation once, retain returned plugin/release IDs, then read back state.

**Failure signature.** A placeholder is created, create is retried after an uncertain result, or packaging is reported as installation.

**Gate / evidence of mastery.** Creation returns verified identity/release evidence or the builder reports the exact unavailable adapter without fabricating success.

**Synapses.** Exchange state with 04 package integrity, 10 unknown side effects, 19 guarded mutation, and 20.N7 post-mutation verification.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-GOV`

### 20.N3 — Source inspection and history contract

**Decision model.** For an editable plugin, resolve the exact backend ID; read metadata/files for focused text work; retrieve full archives only when binary/large/history content requires it; list releases for historical inspection.

**Failure signature.** Name/slug is treated as backend ID, full archives are downloaded unnecessarily, or historical state is confused with current state.

**Gate / evidence of mastery.** Source access is minimal, exact-identity based, and the current release ID is retained for guarded update.

**Synapses.** Exchange state with 07 retrieval minimization, 15 source-of-truth, 19 host discovery, and 20.N4 guarded update.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-GOV`

### 20.N4 — Guarded update parity

**Decision model.** Update only the intended owned/editable plugin, preserve identity/scope/audience/hosting/unrelated files, use the observed current release ID as an optimistic concurrency guard, and reconcile if stale. Omitted files are treated according to the adapter's overlay semantics; deletion requires a supported source workflow rather than pretending overlay can delete.

**Failure signature.** Stale release overwrites newer work, similarly named plugin is edited, or unrelated files disappear.

**Gate / evidence of mastery.** Update evidence includes exact plugin ID, prior release guard, new release/version, and read-back of affected state.

**Synapses.** Exchange state with 10 concurrency, 15 migration, 19 guarded mutation, and 20.N7 verification.

**Primary sources.** `INSTALLED-CREATOR`, `NIST-SSDF`, `INTERNAL-GOV`

### 20.N5 — Source-owner routing parity

**Decision model.** Match change to its owning source: Site-hosted plugin → Site source; local plugin → local source/install; separately hosted MCP/app → its repository/deployment; standalone account plugin → account source/update; Git-managed plugin → Git/release process. Never wrap an existing managed plugin into an unrelated duplicate.

**Failure signature.** The wrong source is edited or a duplicate private plugin is created to patch a managed/Site plugin.

**Gate / evidence of mastery.** The mutation path preserves project/app/plugin identity and existing hosting/data relationships.

**Synapses.** Exchange state with 03 architecture, 14 deployment, 15 source ownership, 18 build-vs-reuse, and 19 adapter selection.

**Primary sources.** `INSTALLED-CREATOR`, `OAI-PKG`

### 20.N6 — Create-route parity: skills, MCP, Apps, Extensions, local/cloud

**Decision model.** Support the same creation families as the baseline creator: skills-only standalone package; existing remote MCP integration; local stdio plugin; cloud-hosted MCP/App route when a suitable hosting/build capability is available; optional host Extensions when the user job benefits. Choose by architecture evidence, not by one default template.

**Failure signature.** Every request is forced into skills-only, every plugin gets an unnecessary server, or a cloud path is claimed without a deployable host.

**Gate / evidence of mastery.** Each supported route has a complete source/build/test/install path and a graceful package-ready fallback when the required host is absent.

**Synapses.** Exchange state with 03 capability placement, 05 MCP, 11 Apps/Extensions, 14 deploy, 18 architecture search, and 19 install adapter.

**Primary sources.** `OAI-PKG`, `OAI-MCP`, `MCP-APPS`, `OAI-EXT`, `INSTALLED-CREATOR`

### 20.N7 — Submission preparation and state separation

**Decision model.** For public intent, separate implementation completion from public-upload copy, listing metadata, icon/URLs, review cases, demo, reviewer access, scans, domain/developer verification, attestations, draft upload, review submission, approval, and publication. Skills-only and MCP submissions have different evidence requirements.

**Failure signature.** A valid ZIP is called submission-ready despite missing dashboard/review requirements, or upload is called publication.

**Gate / evidence of mastery.** The builder reports the exact lifecycle state and never invents publisher facts, URLs, credentials, demos, test execution, or approval.

**Synapses.** Exchange state with 12 policy truthfulness, 13 evaluation, 16 distribution, 19 adapter state, and 20.N8 parity regression.

**Primary sources.** `OAI-SUB`, `OAI-GUIDE`, `INSTALLED-CREATOR`

### 20.N8 — Parity-plus regression gate

**Decision model.** Before claiming baseline parity, run the creator-parity matrix. Before claiming advantage, additionally test Plugin Builder-only families: multi-candidate architecture search, dominance pruning, failure simulation, adversarial security, native deterministic build validation, repair regressions, and read-back/smoke verification.

**Failure signature.** “Better than Plugin Creator” is asserted from feature count or self-description rather than comparable evidence.

**Gate / evidence of mastery.** All baseline critical workflows pass with no material regression, and at least one predeclared parity-plus family shows repeatable improvement under comparable conditions.

**Synapses.** Exchange state with 13 evaluation, 17 learning, 18 architecture search, 19 install verification, and 20.N1 capability inventory.

**Primary sources.** `INTERNAL-SKILL`, `INTERNAL-SCALE`, `INTERNAL-GOV`, `INSTALLED-CREATOR`
