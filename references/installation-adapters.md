# Installation & Release Adapters

Plugin Builder owns the **design/build intelligence**. Installation is delegated to a real host adapter when available.

## Adapter selection

| Target/source | Preferred adapter | Evidence after mutation |
|---|---|---|
| New eligible private account plugin | host account create action | stored plugin id + release/version + read-back |
| Existing eligible private account plugin | host account update action with current-release guard | new release + affected files read back |
| Git-synced/managed plugin | owning repository and release process | source commit/release + host refresh |
| Existing Site/App-owned plugin | owning Site/App source and publish flow | same project/app/plugin identity + tool/UI check |
| Local plugin | target host marketplace/CLI/local install flow | startup + discovery + harmless call |
| Public plugin | submission portal/review lifecycle | exact draft/review/publish state |
| No mutation capability | artifact handoff | validated package + exact remaining install step |

## Rules

- Never create a second plugin when the requested plugin already has an owning source.
- Never equate package validation with installation.
- Never equate installation with MCP reachability, authentication, or working UI.
- Never repeat a side-effecting create/update when the previous result is unknown; inspect state first.
- Preserve plugin identity, scope, audience, hosting, data, and unrelated behavior on updates.
- Use read-back verification whenever the adapter exposes it.
- If an adapter is unavailable, finish source/package/evaluation work and return `NO_MUTATION_ADAPTER`; do not claim success.
