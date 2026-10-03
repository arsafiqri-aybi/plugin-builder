# Architecture

```text
plugin-builder/
├── SKILL.md
├── knowledge/           # 18 lobes, 144 neurons
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
