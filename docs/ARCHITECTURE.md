# Architecture

```text
plugin-builder/
├── SKILL.md
├── knowledge/           # 20 lobes, 160 neurons
├── references/          # operational procedures and source registry
├── scripts/             # deterministic validation/audit
├── assets/              # reusable contracts/templates
├── evaluation/          # evidence boundaries
├── agents/openai.yaml   # host-facing metadata
└── .github/workflows/   # CI validation
```

## Authority order
1. Host/system/user instructions and real permissions.
2. Current target platform specifications/documentation.
3. `SKILL.md` runtime behavior.
4. Operational references.
5. Knowledge neurons.
6. Historical or example material.

Knowledge is selectively retrieved. No lobe grants new platform capability or permission.


## Architecture-search layer

Lobe 18 prevents first-solution lock-in. It generates alternatives only when useful, removes infeasible/dominated routes, compares explicit quality attributes, simulates material failures, and records the decision/re-plan boundary.

## Installation-adapter layer

Lobe 19 separates Plugin Builder intelligence from host-specific mutations. The canonical plugin is built and validated first; then a discovered adapter handles account installation/update, managed-source release, local marketplace installation, public submission, or package-only handoff. A missing adapter never becomes a fabricated success.
