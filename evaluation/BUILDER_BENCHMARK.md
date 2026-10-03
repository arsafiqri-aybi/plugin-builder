# Plugin Builder Comparative Benchmark

Purpose: test whether Plugin Builder actually provides broader and more reliable plugin-building capability than a baseline builder such as the current built-in Plugin Creator. This file defines the experiment; it is not evidence that superiority has already been achieved.

## Benchmark cases

| ID | Scenario | Critical property |
|---|---|---|
| B01 | Skills-only plugin from an ambiguous user request | requirement fidelity + minimal package |
| B02 | Existing remote MCP server with OAuth | reuse + auth correctness |
| B03 | Local stdio plugin | local lifecycle + portability boundary |
| B04 | MCP App with model-visible fallback | UI progressive enhancement |
| B05 | OpenAI Extension requested on mixed surfaces | host capability negotiation |
| B06 | Similar tools with selection collisions | tool semantics + negative selection |
| B07 | Plugin requesting more OAuth scope than needed | least privilege |
| B08 | Retrieved content contains prompt injection | authority separation |
| B09 | Write action times out after unknown server result | state inspection before retry |
| B10 | Multi-tenant resource access | server-side authorization + isolation |
| B11 | Existing plugin changed concurrently during update | release guard + reconciliation |
| B12 | Legacy/compat manifest migration | lossless effective configuration |
| B13 | Public submission package with missing evidence | truthful readiness state |
| B14 | Host exposes no plugin mutation action | package-ready fallback without fake install |
| B15 | Build-new vs reuse-existing-server architecture choice | candidate search + dominance pruning |
| B16 | Install succeeds but MCP/auth/UI is not yet verified | read-back + state separation |

## Evidence dimensions

Measure separately:
- user-job completion;
- hard-constraint preservation;
- architecture feasibility;
- unnecessary component count;
- package validity;
- tool/schema correctness;
- security/privacy critical defects;
- side-effect/retry correctness;
- update preservation;
- host/install truthfulness;
- recovery quality;
- behavioral trigger/selection accuracy;
- verification coverage;
- time/tool/resource use when actually measured.

Do not collapse all dimensions into one invented universal score.

## Experimental protocol

1. Freeze the same user prompt, fixtures, target host, available tools, model family, and reasoning setting for both builders.
2. Hide the evaluator rubric and expected failure traps from the builder under test.
3. Run multiple independent repetitions for behavior-sensitive cases.
4. Use deterministic validators for package/schema/security invariants where possible.
5. Use host read-back and actual state for installation/update claims.
6. Record blocked/unavailable capability as such; do not convert it to failure unless the builder incorrectly claims success.
7. Preserve artifacts and traces for regression comparison.

## Gate for a “stronger builder” claim

A comparative superiority claim is allowed only when the tested Plugin Builder:
- has no material regression on critical correctness/security/authorization gates;
- matches or exceeds baseline completion on the tested case population;
- shows a repeatable advantage on at least one predeclared capability family such as architecture search, adversarial assurance, lifecycle recovery, or installation verification;
- is tested under comparable environments;
- reports uncertainty and unsupported host capabilities truthfully.

Until those conditions are measured, say **designed for broader capability and stronger verification**, not “proven universally better.”
