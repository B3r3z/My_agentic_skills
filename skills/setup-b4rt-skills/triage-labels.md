# Triage Labels

Reference for the corresponding section of `AGENTS.md`. Adapt only the relevant instructions into that file; do not create a separate project configuration file from this seed.

The skills speak in terms of five canonical triage roles. When labels are enabled, record the required role mappings directly in the Labels section of `AGENTS.md`. Otherwise record `Labels: none`.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table.

Adapt the right-hand column to the project vocabulary; include only roles in use. Before applying a remote label, verify it exists. If it is missing, ask whether to create it or omit it.
