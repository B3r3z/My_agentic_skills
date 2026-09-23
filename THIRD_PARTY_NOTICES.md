# Third-party notices

The following skills are adapted from [Matt Pocock’s skills](https://github.com/mattpocock/skills), commit `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` (2026-09-23):

- `grill-with-docs`
- `tdd`
- `diagnosing-bugs`
- `code-review`
- `to-tickets`
- `setup-b4rt-skills`
- `domain-modeling`
- `codebase-design`
- `grilling`

Copyright (c) 2026 Matt Pocock. Distributed under the MIT License, included in each copied skill directory. This attribution does not apply to the pre-existing `orbit-forge` skill.

Local changes:

- Renamed `setup-matt-pocock-skills` to `setup-b4rt-skills`, including cross-references and UI name.
- Replaced two references to a harness-specific “Skill tool” with instructions to read the installed skill files for Codex compatibility.
- Included the upstream MIT license in each copied skill so standalone installations retain the notice.
- Preserved invocation policies; workflow adaptations are listed below.
- Removed Claude-specific `disable-model-invocation` frontmatter; retained equivalent existing Codex policies in `agents/openai.yaml`.

Review fixes (2026-09-23):

- Centralized project agent configuration in AGENTS.md; kept glossary and ADR content separate and preserved migration inputs.
- Made labels optional and aligned setup, ticket creation, and review consumers.
- Added WIP-aware review scopes, explicit requirements precedence, and delegation fallbacks.
- Restored the TDD refactor step and clarified existing-behavior tests.
- Allowed evidence-only diagnosis, scoped fixes to the request, clarified interview documentation writes, preserved regression coverage, and corrected context-specific ADR paths.

- Made `to-tickets` local-only: local inputs, Markdown tasks, dependencies, status and follow-up notes; removed remote fetching, publishing and tracker operations.

Instruction migration (2026-09-23):

- Narrowed discovery descriptions and replaced generic process mandates with task outcomes and decision criteria.
- Removed fixed question/hypothesis/design counts, repeat approval gates, and unconditional documentation loading.
- Added conditional scope, experiment, and local-task references; reduced setup seeds to installed workflows.
- Retained local-only task handling, separate domain documents, scoped verification, and Orbit Forge orchestration requirements.
