# Plugin Evaluation Matrix

Evaluate separate properties instead of one global score.

| Layer | Example evidence |
|---|---|
| Package | manifest/schema/inventory validator |
| Tool contract | deterministic input/result/error tests |
| Authorization | denied cross-tenant/object access |
| Side effects | idempotency/retry/partial-failure tests |
| Security | prompt injection, SSRF, malicious input, exfiltration attempts |
| Selection | natural positive and plausible-negative prompts |
| Workflow | end-to-end user job with observable result |
| UI | actual host render, interaction, fallback, accessibility |
| Operations | latency, rate-limit, outage, rollback tests |
| Submission | listing/cases/demo/reviewer access for exact release |

Never convert static validation into a claim that model behavior, security, or installation is proven.


## Comparative builder benchmark

When the goal is to demonstrate that Plugin Builder is stronger than another builder, use `evaluation/BUILDER_BENCHMARK.md`. Run the same tasks, environment, tools, and evaluator gates. Do not infer superiority from file count, neuron count, or self-review.
