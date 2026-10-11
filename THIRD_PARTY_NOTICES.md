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

The following skills were copied from the same upstream commit and subsequently adapted for this collection:

- `to-spec`
- `wayfinder`
- `research`

The following skill was copied from upstream commit `49dd158d1076134a641b33efb035946536778336` (2026-10-09) and adapted for this collection:

- `implement`

Copyright (c) 2026 Matt Pocock. Distributed under the MIT License, included in each copied skill directory under both `codex/skills/` and `claude/skills/`. This attribution does not apply to the pre-existing `orbit-forge` skill, whose optional exploration notes, pointer-based assignments, and parallel worktree mode were informed by upstream `implement-spec` without copying its text.

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

Local Markdown flow adaptation (2026-09-26):

- `to-spec` now writes one local spec at the configured plan path (default `docs/plan/`), keeps open decisions explicit, and hands off to `to-tickets` only when requested; removed issue publishing and triage labels.
- `wayfinder` now keeps a local map and decision tickets separate from implementation tickets, with file-based blockers, claims, resolutions, and research links; removed external tracker, branch, and harness-specific Skill tool instructions.
- `research` now saves a cited local note, links it to a decision ticket when applicable, and works without mandatory background delegation or an external task system.
- Preserved existing Codex explicit-invocation policies for `to-spec` and `wayfinder`; removed their Claude-specific `disable-model-invocation` frontmatter.

Agent configuration split (2026-09-30):

- Moved the existing collection into `codex/skills/` without changing skill contents or supporting resources.
- Added separate Claude Code adaptations in `claude/skills/`, preserving licenses and local Markdown workflows.
- Replaced Codex invocation syntax and project configuration paths with Claude slash commands and `CLAUDE.md`; changed setup migration to read existing `AGENTS.md` settings where relevant.
- Mapped existing explicit-only Codex policies to Claude's `disable-model-invocation: true`; omitted `agents/openai.yaml` from the Claude distribution.
- Adapted the local Orbit Forge workflow to Claude Code subagents, Sonnet/Opus routing, and Claude's supported waiting behavior.

Implementation workflow adaptation (2026-10-11):

- Added `implement` as a local-only adaptation: reads local Markdown tasks instead of fetching from an issue tracker, uses `tdd` when test-first work is requested, agreed, or required, keeps the upstream validation cadence and closing `code-review`, closes completed local tasks with status `done`, and commits only when authorized.
- Documented the `done` task status in the local task format used by `to-tickets`.
