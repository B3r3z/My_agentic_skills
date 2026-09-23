# My agentic skills

Personal skills collection for Codex and other compatible coding agents.

## Selected engineering skills

| Skill | Purpose |
| --- | --- |
| `setup-b4rt-skills` | Configure a project's issue tracker and domain documentation. |
| `grill-with-docs` | Refine a plan while recording terminology and decisions. |
| `tdd` | Implement behavior in small test-first steps. |
| `diagnosing-bugs` | Reproduce, investigate, and verify bug fixes. |
| `code-review` | Review changes against requirements and coding standards. |
| `to-tickets` | Split work into local Markdown tasks with acceptance criteria and dependencies; no external tracker interaction. |

Included dependencies: `grilling`, `domain-modeling`, and `codebase-design`.

`orbit-forge` executes an approved plan or ticket set sequentially using Luna MAX / Sol HIGH and an independent Sol HIGH review. It reuses the source requirements, records execution state locally, and waits for agent events instead of repeatedly polling progress. Waiting and state-location overrides belong in `AGENTS.md`.

## Installation

```sh
npx skills add B3r3z/My_agentic_skills
```

Select the skills above and their dependencies for your agent. For manual Codex installation, copy each selected directory under `skills/` into `~/.codex/skills/`, keeping its supporting files and license. Do not overwrite an existing installation without reviewing local changes.

In each project, invoke `$setup-b4rt-skills` to configure tracker settings, optional labels, and documentation paths directly in `AGENTS.md`. Glossaries stay in `CONTEXT.md` (or per-context files), and decisions stay in ADR files. You can choose local Markdown for tasks instead of an external issue tracker. Installing this collection does not run project setup automatically.

Suggested use: `$grill-with-docs` for design, `$to-tickets` for larger plans, `$tdd` during implementation, `$code-review` before a PR, and `$diagnosing-bugs` for difficult failures.

These are adaptations of Matt Pocock's skills. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the source revision and changes; each copied skill includes its MIT license.

## Instruction design

Updated using [OpenAI’s guidance on skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): narrow discovery descriptions, outcome-focused instructions, and supporting files read only when relevant. Setup generates conditional documentation guidance in `AGENTS.md` rather than mandatory reading lists. Existing invocation policies and Orbit Forge’s explicit Luna/Sol routing remain intact; this is an instruction migration, not a model configuration change.
