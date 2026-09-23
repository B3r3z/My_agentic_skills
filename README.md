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
| `to-tickets` | Split work into independently verifiable slices. |

Included dependencies: `grilling`, `domain-modeling`, and `codebase-design`.

The collection also retains the existing `orbit-forge` skill.

## Installation

```sh
npx skills add B3r3z/My_agentic_skills
```

Select the skills above and their dependencies for your agent. For manual Codex installation, copy each selected directory under `skills/` into `~/.codex/skills/`, keeping its supporting files and license. Do not overwrite an existing installation without reviewing local changes.

In each project, invoke `$setup-b4rt-skills` to configure tracker settings, optional labels, and documentation paths directly in `AGENTS.md`. Glossaries stay in `CONTEXT.md` (or per-context files), and decisions stay in ADR files. You can choose local Markdown for tasks instead of an external issue tracker. Installing this collection does not run project setup automatically.

Suggested use: `$grill-with-docs` for design, `$to-tickets` for larger plans, `$tdd` during implementation, `$code-review` before a PR, and `$diagnosing-bugs` for difficult failures.

These are adaptations of Matt Pocock's skills. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the source revision and changes; each copied skill includes its MIT license.
