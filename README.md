# Plugin Builder — Deep Knowledge Architecture

Plugin Builder is a specialist system for **creating, auditing, repairing, validating, packaging, and evolving high-quality AI plugins**. Its output is a plugin; it is not an orchestrator for unrelated projects.

This package is the research/architecture foundation produced on **2026-10-04**. It integrates current OpenAI Plugin Creator behavior, current OpenAI plugin/MCP documentation, open MCP and Agent Plugins specifications, security standards, HCI guidance, and the user's existing Prompting, Skill Builder, Scale, and Governor engineering methods.

## Brain model

- **21 lobes** = major decision domains.
- **8 neurons per lobe** = operational knowledge units.
- **168 neurons total**.
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

## Native builder tooling

Plugin Builder is not only a knowledge package. It contains its own deterministic authoring path:

- `scripts/init_plugin.py` — minimal portable plugin scaffold from explicit components.
- `scripts/validate_plugin.py` — canonical package/component/security checks.
- `scripts/package_plugin.py` — deterministic single-directory ZIP packaging.
- `scripts/audit_plugin_package.py` — additional static audit.
- `scripts/test_plugin_tooling.py` — regression tests for the native builder path.

Architecture search and installation are separated: Plugin Builder chooses/builds the canonical design itself, then uses a real host adapter only for the final mutation when one exists.


## Creator parity execution

Plugin Builder v0.3 adds an explicit baseline-parity lifecycle layer covering the Plugin Creator workflow families: skills-only / existing-MCP / local / Apps / Extensions creation, private account create when a real host action exists, exact-identity inspection, current/historical source retrieval, release listing, guarded update, source-owner routing, and public-submission preparation.

Privileged ChatGPT account mutations remain host capabilities. Plugin Builder orchestrates them when exposed and never claims that packaged instructions create those permissions. The parity gate is tracked in `evaluation/CREATOR_PARITY_MATRIX.md`; broader advantages are tested separately rather than asserted from feature count.
