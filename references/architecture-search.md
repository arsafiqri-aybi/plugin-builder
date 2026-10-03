# Architecture Search & Synthesis

Use this only when architecture choice is material. Do not turn obvious plugins into a design contest.

## Search loop

1. Freeze the user job, hard constraints, target hosts, authority boundaries, distribution mode, and critical gates.
2. Generate 2–5 **materially different** candidates. Differences must change capability placement, server boundary, UI model, hosting, or reuse/build choice.
3. Filter infeasible candidates before ranking anything.
4. Prune dominated candidates: if another candidate satisfies the same hard requirements with no worse critical properties and materially less complexity/risk, remove the dominated one.
5. Compare the survivors across only relevant quality attributes. Keep dimensions separate; do not invent one universal score.
6. Simulate critical failures and trust-boundary attacks on the leading candidate.
7. Select the smallest candidate whose evidence plan can prove the acceptance floor.
8. Record why alternatives were rejected and what future condition would trigger re-plan.

## Candidate record

Each candidate should state:
- topology and component ownership;
- reused vs newly built dependencies;
- trust boundaries and privileged actions;
- state owner and durability assumptions;
- host/install path;
- critical quality gates;
- operational burden and failure modes;
- unresolved assumptions.

Architecture search ends before implementation. Re-open it only when a material assumption fails or the selected route cannot pass a required gate.
