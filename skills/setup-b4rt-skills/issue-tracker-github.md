# Github configuration seed

Only include this provider when an existing or requested workflow uses it. Record the explicit owner/repository and the available access method (for example `gh`) in `AGENTS.md`; preserve existing choices.

Document which workflows read external specs and which writes are authorized by their task. Configuration alone does not authorize publishing, commenting, or closing issues. Use current tool help for operation syntax rather than embedding a command catalogue.

`to-tickets` remains local-only and does not use this provider. Do not add wayfinding or PR/MR triage settings unless those workflows are actually configured.
