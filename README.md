# Plugin Builder — Deep Knowledge Architecture

Plugin Builder is a specialist system for **creating, auditing, repairing, validating, packaging, and evolving high-quality AI plugins**. Its output is a plugin; it is not an orchestrator for unrelated projects.

This package is the research/architecture foundation produced on **2026-10-04**. It integrates current OpenAI Plugin Creator behavior, current OpenAI plugin/MCP documentation, open MCP and Agent Plugins specifications, security standards, HCI guidance, and the user's existing Prompting, Skill Builder, Scale, and Governor engineering methods.

## Brain model

- **18 lobes** = major decision domains.
- **8 neurons per lobe** = operational knowledge units.
- **144 neurons total**.
- **Synapses** connect neurons across requirements, architecture, security, UX, operations, evaluation, and release.
- Runtime should load only the lobes needed for the active build decision. Full access is not full-context loading.

## Status

The knowledge architecture and runtime draft are built and statically validated. This package is **not yet evidence that every behavioral route works in every ChatGPT/Codex surface**. See `evaluation/STATUS.md`.

## Start here

1. `SKILL.md` — runtime draft.
2. `knowledge/README.md` — retrieval map.
3. `NEURON_MAP.md` — global brain/synapse map.
4. `references/build-workflow.md` — end-to-end plugin creation workflow.
5. `references/source-registry.md` — evidence/provenance.