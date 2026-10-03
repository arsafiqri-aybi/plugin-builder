# Plugin Creator Parity Matrix

This matrix is the release gate for baseline functional coverage. “Supported” means Plugin Builder has a defined workflow and can execute it when the required host capability exists. Host-only privileges are explicitly marked adapter-dependent.

| ID | Baseline capability | Plugin Builder v0.3 target | Evidence |
|---|---|---|---|
| P01 | Create skills-only plugin | Native | scaffold + validate + package tests |
| P02 | Create plugin using existing remote MCP | Native | architecture + mcp config validator |
| P03 | Create local stdio plugin | Native route | local source/transport contract |
| P04 | MCP App / interactive UI | Native design/build route | host/UI evaluation gate |
| P05 | OpenAI Extensions | Native design route | capability negotiation + fallback |
| P06 | Cloud/Site-style plugin route | Adapter-dependent | real hosting/deploy capability required |
| P07 | Save private plugin to account | Host-adapter dependent | create action + read-back |
| P08 | Inspect plugin metadata | Host-adapter dependent | exact backend ID metadata read |
| P09 | Inspect current files | Host-adapter dependent | paged file inventory/read |
| P10 | Retrieve current/historical archive | Host-adapter dependent | archive + release identity |
| P11 | List release history | Host-adapter dependent | release list + current marker |
| P12 | Guarded account update | Host-adapter dependent | expected release guard + read-back |
| P13 | Preserve managed/Site/Git/local source ownership | Native orchestration | source-owner routing gate |
| P14 | Legacy/package migration | Native | effective-config preservation gate |
| P15 | Prepare public listing | Native preparation | metadata validation |
| P16 | Positive/negative review cases | Native preparation | review-case validation |
| P17 | Demo/reviewer-access guidance | Native preparation | truthfulness + secure-channel boundary |
| P18 | Draft/review/publish state separation | Native orchestration | lifecycle state machine |
| P19 | Package validation | Native deterministic tooling | CI validator |
| P20 | Post-install verification | Native orchestration | read-back + smoke evidence |

## Beyond-baseline families

- X01 multi-candidate architecture search;
- X02 feasibility + dominance pruning;
- X03 pre-build failure simulation;
- X04 adversarial security/authority evaluation;
- X05 deterministic reproducible ChatGPT package build in CI;
- X06 failure diagnosis → focused repair → regression;
- X07 explicit resource/complexity stopping gates;
- X08 comparative benchmark with evidence boundaries.

A claim of “better than Plugin Creator” requires measured comparative results, not this matrix alone.
