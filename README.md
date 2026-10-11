# My agentic skills

Personal skills collection with separate configurations for Codex and Claude Code.

```text
codex/skills/    Existing Codex skills, including agents/openai.yaml
claude/skills/   Claude Code adaptations with native invocation policies
claude/agents/   Claude Code subagents used by Maestro
scripts/        Installer for the selected agent
```

Both collections contain the same 14 skills and their supporting files. The Codex configuration is preserved. Claude Code uses `CLAUDE.md`, `/skill-name` commands, and its own subagent configuration. See [claude/README.md](claude/README.md) for the Claude workflow.

## Selected engineering skills

| Skill | Purpose |
| --- | --- |
| `setup-b4rt-skills` | Configure local task paths and domain documentation. |
| `grill-with-docs` | Refine a plan while recording terminology and decisions. |
| `tdd` | Implement behavior in small test-first steps. |
| `diagnosing-bugs` | Reproduce, investigate, and verify bug fixes. |
| `code-review` | Review changes against requirements and coding standards. |
| `to-tickets` | Split work into local Markdown tasks with acceptance criteria and dependencies; no external tracker interaction. |
| `to-spec` | Synthesize agreed decisions into a local spec for Markdown-ticket planning. |
| `wayfinder` | Map a multi-session effort as local Markdown decision tickets. |
| `research` | Save cited primary-source findings as local Markdown notes linked to decisions when relevant. |
| `solo` | Build one local task or small spec in the current session, review it, and close completed tasks. |
| `maestro` | Execute an approved local plan sequentially or in parallel git worktrees, obtain an independent review, and close completed tasks. |

Included dependencies: `grilling`, `domain-modeling`, and `codebase-design`.

When installing individual skills, include the dependencies needed for your workflow:

| Skill | Required dependencies | Optional dependencies |
| --- | --- | --- |
| `grill-with-docs` | `grilling`; `domain-modeling` when recording docs | None |
| `solo` | `code-review` for the closing review | `tdd` for requested test-first work; `diagnosing-bugs` for difficult failures |
| `maestro` | `code-review` for final review | `tdd` for requested test-first work; `diagnosing-bugs` for difficult failures |
| `tdd` | None | `codebase-design` when interface design needs work |

Other skills have no required skill dependencies. Keep each installed skill's supporting files. `wayfinder` can use `grilling`, `domain-modeling`, and `research` when those workflows help; it does not require an external tracker or an uninstalled `prototype` skill.

The Codex `maestro` uses GPT-6.1 Sol at HIGH reasoning effort for implementation and independent review. The Claude version uses Sonnet / Opus workers, an optional Sonnet scout, and an independent Opus critic. Both reuse source requirements, record execution state locally, pass agents pointers to tasks and shared exploration notes rather than copies, and close completed local tasks after the final review passes. Project overrides belong in `AGENTS.md` for Codex and `CLAUDE.md` for Claude Code.

Maestro runs one implementer at a time by default. Parallel worktree mode is opt-in: ask for it in the request or enable it in the project's Maestro settings, optionally with a concurrency limit (default 3), working branch, and worktree root. Enabling it authorizes local task branches, commits on them, and merges into the working branch, never pushes. Root creates one worktree per ready task from the working-branch tip, runs only tasks with disjoint owned paths together, merges each accepted branch, and removes merged worktrees and branches. Unmerged or blocked work is kept and reported. The default worktree root is `.claude/worktrees/maestro-<run-id>/` for Claude Code, whose documentation recommends ignoring `.claude/worktrees/`, and `.scratch/maestro/<run-id>/worktrees/` for Codex; root adds it to `.git/info/exclude` when git does not already ignore it.

## Installation

Run from this repository, choosing one configuration:

```sh
python3 scripts/install.py claude --dry-run
python3 scripts/install.py claude
# Or, for Codex:
python3 scripts/install.py codex
```

The installer links skills into `~/.claude/skills/` or `~/.codex/skills/`. For Claude it also links the Maestro definitions into `~/.claude/agents/`. It leaves existing configuration intact and stops before writing if a destination conflicts. Re-running it keeps links already pointing to this checkout. Keep the checkout at its installed path, since the links refer to it.

For a project-only Claude installation, use `python3 scripts/install.py claude --target /path/to/project/.claude`. For a manual installation, copy the selected directories from `codex/skills/` or `claude/skills/` into the corresponding agent's skills directory, preserving supporting files and licenses. Copy `claude/agents/*.md` into the agent's `agents/` directory if using Maestro. Do not mix both variants in one skills directory.

`maestro` was previously named `orbit-forge`. When upgrading an existing installation, remove the old `skills/orbit-forge` link and `agents/orbit-forge-*.md` links from the agent directory, then rerun the installer.

In each project, invoke `$setup-b4rt-skills` in Codex or `/setup-b4rt-skills` in Claude Code to configure local paths in `AGENTS.md` or `CLAUDE.md`, respectively. Installing the collection does not run project setup automatically.

All ticket state stays in local Markdown: `wayfinder` keeps a map and decision tickets beside the feature's implementation-ticket directory, `to-spec` writes a plan/spec file (default `docs/plan/`), and `to-tickets` writes executable tasks (default `.scratch/<feature-slug>/issues/`). `research` writes cited local notes and links them to decision tickets when relevant. `solo` and `maestro` close completed tasks by setting their status to `done` after acceptance and review pass. None of these skills reads or writes an external issue tracker. Glossaries stay in `CONTEXT.md` (or per-context files), and decisions stay in ADR files.

Suggested flow: `grill-with-docs` for a design that fits one conversation; `wayfinder` when decisions span sessions; `research` for source-backed facts; `to-spec` for a durable spec; `to-tickets` for implementation tasks; `solo` for one task at a time in a fresh session; and `maestro` when orchestration is explicitly requested. Use `$name` in Codex and `/name` in Claude Code. `tdd`, `code-review`, and `diagnosing-bugs` remain available during implementation.

These are adaptations of Matt Pocock's skills, including the now local-only `to-spec`, `wayfinder`, `research`, and `solo`. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source revisions and changes; each copied skill includes its MIT license.

## Instruction design

The existing Codex instructions follow [OpenAI’s guidance on skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): narrow discovery descriptions, outcome-focused instructions, and supporting files read only when relevant. Setup generates conditional documentation guidance rather than mandatory reading lists. Claude adaptations preserve the same workflow boundaries and explicit invocation policies using [Claude Code skills](https://code.claude.com/docs/en/skills) and [subagent configuration](https://code.claude.com/docs/en/sub-agents).
