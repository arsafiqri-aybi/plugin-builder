# Lobe 19 — Host Installation & Release Adaptation

Memisahkan intelligence Plugin Builder dari mekanisme pemasangan tertentu. Plugin Builder menghasilkan paket canonical sendiri, lalu memilih adapter instalasi/update yang benar-benar tersedia pada host. Tidak ada instruksi yang boleh mengarang tool, endpoint, scope, atau status instalasi.

## Lobe decision flow

Use this lobe when the user asks to install, save, update, connect, publish, or verify a plugin in a host. Skip it for source-only design requests.

### 19.N1 — Host capability discovery

**Decision model.** Determine which real mutation paths are exposed now: account create/update action, local marketplace/CLI, Git-synced release, developer portal/browser flow, Sites/App-owned flow, or package-only handoff. Capability is discovered from the host/tooling, not assumed from the Plugin Builder instructions.

**Failure signature.** The builder claims it can install because it knows how installation works, even though no mutation capability exists in the current environment.

**Gate / evidence of mastery.** The chosen install path names a real available mechanism or explicitly records `NO_MUTATION_ADAPTER`.

**Synapses.** Exchange state with 01 host model, 14 environment, 15 source ownership, 16 distribution, and 18 feasibility filtering.

**Primary sources.** `OAI-PKG`, `OAI-SUB`, `INSTALLED-CREATOR`

### 19.N2 — Installation adapter selection

**Decision model.** Choose the adapter that owns the target plugin lifecycle: account archive create/update for eligible private plugins, source repository/deployment for managed apps, local marketplace/CLI for local plugins, submission portal for public releases, or artifact handoff when mutation is unavailable.

**Failure signature.** A Site/Git-managed or local plugin is wrapped into a second unrelated private plugin, or the wrong lifecycle is used.

**Gate / evidence of mastery.** Adapter matches source ownership, target audience, hosting model, and requested action.

**Synapses.** Exchange state with 15 source-of-truth, 16 distribution, 18 architecture, and 19.N5 guarded mutation.

**Primary sources.** `INSTALLED-CREATOR`, `OAI-PKG`, `OAI-SUB`

### 19.N3 — Artifact normalization per adapter

**Decision model.** Start from one canonical portable package, then generate only the compatibility overlay or upload copy required by the selected adapter. Preserve identity, behavior, assets, and server bindings across representations.

**Failure signature.** The package is reshaped for installation and silently loses skills, MCP servers, prompts, assets, or version metadata.

**Gate / evidence of mastery.** Effective configuration before and after adaptation is equivalent except for intentional adapter-specific fields.

**Synapses.** Exchange state with 04 packaging, 15 migration, 16 submission, and 17 scaffold generation.

**Primary sources.** `OAI-PKG`, `AGENT-PLUGINS`, `INSTALLED-CREATOR`

### 19.N4 — Mutation authorization boundary

**Decision model.** Distinguish build/package permission from account mutation, deployment, sharing, submission, and publication. Proceed with an already authorized mutation; obtain authorization only for a genuinely new consequential action.

**Failure signature.** Building a ZIP is treated as permission to publish, or an authorized install is repeatedly re-confirmed without reason.

**Gate / evidence of mastery.** Every external mutation maps to explicit user intent and current host policy.

**Synapses.** Exchange state with 02 actor/authority map, 08 authorization, 09 security, and 16 release state machine.

**Primary sources.** `INTERNAL-PROMPTING`, `INTERNAL-SKILL`, `OAI-SUB`

### 19.N5 — Guarded create/update

**Decision model.** For creation, ensure the target is genuinely new and avoid placeholder/duplicate creation. For updates, resolve exact plugin identity and source, preserve scope/audience, use current release/version guards when supported, and reconcile concurrent changes before retrying.

**Failure signature.** A similarly named plugin is modified, a duplicate is created, or stale source overwrites a newer release.

**Gate / evidence of mastery.** Mutation uses verified identity and current-state guard; uncertain success is inspected before any retry.

**Synapses.** Exchange state with 10 unknown-effect handling, 15 identity/concurrency, 17 diagnosis, and 19.N7 read-back verification.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-GOV`

### 19.N6 — Connection and authentication handoff

**Decision model.** Treat package installation, MCP reachability, OAuth/account connection, and user authorization as separate states. After install, complete or guide only the connection steps actually required by the plugin and host.

**Failure signature.** “Installed” is reported as “working” even though the MCP server is unreachable or the user has not authenticated.

**Gate / evidence of mastery.** Connection/auth state is verified independently from package mutation.

**Synapses.** Exchange state with 05 protocol lifecycle, 08 authentication, 14 deployment, and 16 submission setup.

**Primary sources.** `OAI-MCP`, `OAI-AUTH`, `OAI-SUB`

### 19.N7 — Read-back and smoke verification

**Decision model.** After mutation, read back stored metadata/files when possible, verify release/version identity, confirm skill/tool discovery, make a harmless representative call, and render UI when the change affects UI. Match verification depth to the changed property.

**Failure signature.** An API returned success so the builder declares the plugin fully operational without inspecting the persisted state or host behavior.

**Gate / evidence of mastery.** Saved state and at least one relevant host behavior are evidenced, or explicitly marked unverified.

**Synapses.** Exchange state with 13 evaluation, 15 read-back verification, 17 generate-verify loop, and 19.N6 connection state.

**Primary sources.** `INSTALLED-CREATOR`, `INTERNAL-SKILL`, `INTERNAL-PROMPTING`

### 19.N8 — Adapter failure recovery

**Decision model.** Classify installation failure as packaging, identity, access, connection, host support, conflict, or transient tool failure. Preserve the verified package and source; switch adapter only when it still satisfies the user's target. Never fabricate success or repeatedly create/update after an unknown outcome.

**Failure signature.** A failed install causes duplicate plugins, blind retries, lost source, or a claim that the user must rebuild from scratch.

**Gate / evidence of mastery.** The builder returns the last known-good artifact, exact failure class, and the minimum next action while keeping completed work reusable.

**Synapses.** Exchange state with 10 recovery, 14 incident handling, 15 update guard, and 17 diagnosis-before-repair.

**Primary sources.** `INTERNAL-GOV`, `INSTALLED-CREATOR`, `INTERNAL-SKILL`
