# Security Gates

A consequential/data-sensitive plugin does not pass until applicable gates are evidenced:

1. **Identity gate** — authenticated identity is resolved from validated credentials.
2. **Authorization gate** — resource/action permission is enforced server-side.
3. **Intent gate** — proposed consequential action matches the user's authorized goal.
4. **Input gate** — schemas and domain validation reject malformed/malicious values.
5. **Trust gate** — untrusted content cannot grant authority or silently rewrite privileged action arguments.
6. **Side-effect gate** — retry/idempotency/unknown-result policy is explicit.
7. **Secret gate** — no credential in package, model-visible result, UI props or logs.
8. **Tenant gate** — cross-user/workspace isolation is tested.
9. **Network gate** — open-world/network tools constrain SSRF/exfiltration surface.
10. **Evidence gate** — failures produce enough trace to diagnose without logging sensitive content.
