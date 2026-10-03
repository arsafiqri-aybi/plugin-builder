# Source Registry

Checked: **2026-10-04**. Dynamic platform facts must be refreshed before release decisions.

| Key | Source | Location | Role |
|---|---|---|---|
| `OAI-PKG` | OpenAI — Package your plugin | https://developers.openai.com/plugins/build/plugins | Portable plugin packaging, skills/MCP composition, universal directory. |
| `OAI-MCP` | OpenAI — Build an MCP server | https://developers.openai.com/plugins/build/mcp-server | Tool/server design, annotations, testing, deployment, company knowledge, auth boundaries. |
| `OAI-AUTH` | OpenAI — Authentication | https://developers.openai.com/plugins/build/auth | OAuth 2.1 expectations for authenticated plugin MCP servers. |
| `OAI-EXT` | OpenAI — Plugin Extensions | https://developers.openai.com/plugins/build/extensions | OpenAI-specific host integrations and surface behavior. |
| `OAI-SUB` | OpenAI — Upload and submit your plugin | https://developers.openai.com/plugins/deploy/submission | Draft, automated checks, MCP connection, review, approval, publishing. |
| `OAI-GUIDE` | OpenAI — Plugin guidelines | https://developers.openai.com/plugins/app-guidelines | Publication quality, privacy, safety, UI and behavior expectations. |
| `OAI-QUICK` | OpenAI — MCP server and UI quickstart | https://developers.openai.com/plugins/build/app-quickstart | Current server/UI construction pattern. |
| `AGENT-PLUGINS` | Agent Plugins Specification 1.0 | https://agent-plugins.org/specification | Portable manifest semantics and validation rules. |
| `MCP-SPEC` | Model Context Protocol Specification 2026-07-28 | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/index.mdx | Authoritative MCP protocol concepts, capabilities, lifecycle and extensions. |
| `MCP-APPS` | MCP Apps Specification 2026-01-26 | https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx | Portable interactive UI resources and host communication. |
| `OAI-EXT-SPEC` | OpenAI MCP Extensions Specification | https://github.com/openai/mcp-extensions/blob/main/docs/spec.md | ChatGPT-specific host integration primitives. |
| `JSON-SCHEMA` | JSON Schema 2020-12 | https://json-schema.org/specification | Schema vocabulary and validation model. |
| `NIST-SSDF` | NIST SP 800-218 SSDF 1.1 | https://csrc.nist.gov/pubs/sp/800/218/final | Secure software development lifecycle practices. |
| `OWASP-PI` | OWASP LLM Prompt Injection Prevention Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html | Prompt injection threat patterns and layered mitigations. |
| `OWASP-AGENT` | OWASP AI Agent Security Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html | Agent/tool risks: privilege escalation, exfiltration, memory poisoning. |
| `RFC-9728` | RFC 9728 — OAuth Protected Resource Metadata | https://datatracker.ietf.org/doc/html/rfc9728 | Protected resource metadata and discovery. |
| `RFC-9700` | RFC 9700 — OAuth 2.0 Security BCP | https://datatracker.ietf.org/doc/html/rfc9700 | OAuth security best current practices. |
| `RFC-8414` | RFC 8414 — OAuth Authorization Server Metadata | https://datatracker.ietf.org/doc/rfc8414/ | Authorization-server discovery metadata. |
| `HAX` | Microsoft — Guidelines for Human-AI Interaction | https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ | Evidence-based human-AI interaction guidelines. |
| `NNG` | Nielsen Norman Group — 10 Usability Heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ | General usability principles: status, control, consistency, error recovery. |
| `WCAG` | W3C — WCAG 2.2 | https://www.w3.org/TR/wcag/ | Accessibility success criteria for web UI. |
| `INTERNAL-PROMPTING` | Internal repo — Prompting | arsafiqri-aybi/Prompting | Intent, context, evidence, tool use and verification discipline. |
| `INTERNAL-SKILL` | Internal repo — Skill Builder | arsafiqri-aybi/skill-builder | Reusable capability architecture, knowledge loading, evaluation and self-contained authoring. |
| `INTERNAL-SCALE` | Internal repo — Scale | arsafiqri-aybi/scale | Execution architecture, dependencies, quality gates and re-planning. |
| `INTERNAL-GOV` | Internal repo — Governor | arsafiqri-aybi/governor | Adaptive resource use, retrieval, retries, stopping and evidence separation. |
| `INSTALLED-CREATOR` | Installed OpenAI Plugin Creator snapshot | ChatGPT environment snapshot 2026-10-04 | Create/update/submission workflows, package rules and operational edge cases. |
