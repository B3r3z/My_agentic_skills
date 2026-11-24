# My agentic skills

Personal skills collection with separate configurations for Codex and Claude Code.

```text
codex/skills/    Existing Codex skills, including agents/openai.yaml
claude/skills/   Claude Code adaptations with native invocation policies
claude/agents/   Claude Code subagents used by Maestro
scripts/        Installer for the selected agent
tests/          Git helper regression tests in temporary repositories
evals/          Behavioral scenarios for skill evaluation
```

Both collections share 16 skills and their supporting files. Codex also includes `pr-stack` and `okr-summary`. The Codex configuration is preserved. Claude Code uses `CLAUDE.md`, `/skill-name` commands, and its own subagent configuration. See [claude/README.md](claude/README.md) for the Claude workflow.

## Selected engineering skills

| Skill | Purpose |
| --- | --- |
| `setup-b4rt-skills` | Configure local task paths and domain documentation. |
| `grill-with-docs` | Refine a plan while recording terminology and decisions. |
| `tdd` | Implement behavior in small test-first steps. |
| `diagnosing-bugs` | Reproduce, investigate, and verify bug fixes. |
| `code-coach` | Understand code and review comments through grounded explanations and critical discussion of assumptions and tradeoffs. |
| [`simple-english`](codex/skills/simple-english/SKILL.md) | Write or review technical text in plain English. Apply ASD-STE100 when requested. |
| `playback` | Review changes against requirements and coding standards. |
| `to-tickets` | Split work into local Markdown tasks with acceptance criteria and dependencies; no external tracker interaction. |
| `to-spec` | Synthesize agreed decisions into a local spec for Markdown-ticket planning. |
| `wayfinder` | Map a multi-session effort as local Markdown decision tickets. |
| `research` | Save cited primary-source findings as local Markdown notes linked to decisions when relevant. |
| `solo` | Build one local task or small spec in the current session, obtain an independent Playback subagent review, and close completed tasks. |
| `maestro` | Execute an approved local plan sequentially or in parallel git worktrees, obtain an independent review, and close completed tasks. |
| `pr-stack` (Codex) | Assess whether a diff has logically separate review layers; recommend one PR when it does not, otherwise agree and build local branches and hand publication to the user. |
| [`okr-summary`](codex/skills/okr-summary/SKILL.md) (Codex) | Read a GitHub OKR, its child issues and their comments, then draft a quarterly summary for leadership as copyable Markdown in chat. |

Included dependencies: `grilling`, `domain-modeling`, and `codebase-design`.

When installing individual skills, include the dependencies needed for your workflow:

| Skill | Required dependencies | Optional dependencies |
| --- | --- | --- |
| `grill-with-docs` | `grilling`; `domain-modeling` when recording docs | None |
| `solo` | `playback` for the closing review | `tdd` for requested test-first work; `diagnosing-bugs` for difficult failures |
| `maestro` | `playback` for final review | `tdd` for requested test-first work; `diagnosing-bugs` for difficult failures |
| `tdd` | None | `codebase-design` when interface design needs work |

Other skills have no required skill dependencies. Keep each installed skill's supporting files. `wayfinder` can use `grilling`, `domain-modeling`, and `research` when those workflows help; it does not require an external tracker or an uninstalled `prototype` skill.

The Codex `maestro` uses GPT-6.1 Sol at HIGH reasoning effort for implementation and independent review. The Claude version uses Sonnet / Opus workers, an optional Sonnet scout, and an independent Opus critic. Both reuse source requirements, record execution state locally, pass agents pointers to tasks and shared exploration notes rather than copies, and close completed local tasks after the final review passes. Project overrides belong in `AGENTS.md` for Codex and `CLAUDE.md` for Claude Code.

Both `solo` and `maestro` delegate the closing review to one fresh read-only subagent that applies `playback` and returns separate Standards and Spec verdicts. Solo keeps implementation in the current session. If delegation or Playback is unavailable, review remains pending and tasks stay open.

Maestro runs one implementer at a time by default. Parallel worktree mode is opt-in: ask for it in the request or enable it in the project's Maestro settings, optionally with a concurrency limit (default 3), working branch, and worktree root. Enabling it authorizes local task branches, commits on them, and merges into the working branch, never pushes. Root creates one worktree per ready task from the working-branch tip, runs only tasks with disjoint owned paths together, merges each accepted branch, and removes merged worktrees and branches. Unmerged or blocked work is kept and reported. The default worktree root is `.claude/worktrees/maestro-<run-id>/` for Claude Code and `.scratch/maestro/<run-id>/worktrees/` for Codex. If an in-checkout root is not ignored, root adds its directory pattern to the exclude file resolved by Git, which also works from an existing linked worktree.

Before parallel dispatch and each merge, Maestro's bundled read-only `scripts/check_git_state.py` checks the working branch and the entire index, and reports the absolute exclude-file path. An unrelated staged change also prevents parallel dispatch; root falls back to sequential work without changing the user's index. If the index changes after dispatch, root pauses integration and retains the task worktrees. Owned-path overlap and ignore rules are checked separately. Solo preserves the original contents of pre-existing changes for its closing review and selects validation according to user constraints, repository requirements, and affected behavior.

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

`maestro` was previously named `orbit-forge`, and `playback` was `code-review` (renamed to avoid Claude Code's built-in `/code-review`). When upgrading an existing installation, remove the old `skills/orbit-forge` and `skills/code-review` links and the `agents/orbit-forge-*.md` links from the agent directory, then rerun the installer.

In each project, invoke `$setup-b4rt-skills` in Codex or `/setup-b4rt-skills` in Claude Code to configure local paths in `AGENTS.md` or `CLAUDE.md`, respectively. Installing the collection does not run project setup automatically.

Invoke `$pr-stack` in Codex to assess existing changes for review. A read-only scout recommends one PR when the changes cannot be split into logically separate layers. It keeps coupled implementation, contract, and test changes together instead of inventing temporary versions for successive PRs. For a viable stack, the main session agrees the split and branch names with you before creating local branches and commits in a separate worktree. It preserves your source checkout and staging. It never pushes or creates PRs: it gives you the command to register the prepared branches with [gh-stack](https://github.com/github/gh-stack) and publish them yourself. Git, an available subagent tool, and the gh-stack CLI are required for the full stack workflow; tool installation is separate.

All ticket state stays in local Markdown: `wayfinder` keeps a map and decision tickets beside the feature's implementation-ticket directory, `to-spec` writes a plan/spec file (default `docs/plan/`), and `to-tickets` writes executable tasks (default `.scratch/<feature-slug>/issues/`). `research` writes cited local notes and links them to decision tickets when relevant. `solo` and `maestro` close completed tasks by setting their status to `done` after acceptance and review pass. None of these skills reads or writes an external issue tracker. Glossaries stay in `CONTEXT.md` (or per-context files), and decisions stay in ADR files.

Suggested flow: `grill-with-docs` for a design that fits one conversation; `wayfinder` when decisions span sessions; `research` for source-backed facts; `to-spec` for a durable spec; `to-tickets` for implementation tasks; `solo` for one task at a time in a fresh session; and `maestro` when orchestration is explicitly requested. Use `$name` in Codex and `/name` in Claude Code. `tdd`, `playback`, and `diagnosing-bugs` remain available during implementation.

For learning, invoke `$code-coach` in Codex or `/code-coach` in Claude Code with a code fragment, symbol, or review comment. It explains the selected material and challenges reasoning with relevant counterexamples, assumptions, and tradeoffs. It checks comments against implementation. Learning questions are selective and must require a new inference; there is no routine quiz or recall check after an explanation. A request to understand code does not authorize repository edits.

The collection includes adaptations of Matt Pocock's skills, including the now local-only `to-spec`, `wayfinder`, `research`, and `solo`, alongside original skills such as `code-coach`. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source revisions and changes; each copied skill includes its MIT license.

## Instruction design

The existing Codex instructions follow [OpenAI’s guidance on skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): narrow discovery descriptions, outcome-focused instructions, and supporting files read only when relevant. Setup generates conditional documentation guidance rather than mandatory reading lists. Claude adaptations preserve the same workflow boundaries and explicit invocation policies using [Claude Code skills](https://code.claude.com/docs/en/skills) and [subagent configuration](https://code.claude.com/docs/en/sub-agents).

## Validation

Run `python3 -B -m unittest discover -s tests -v` with Python 3 and Git. These tests run both shipped Maestro helpers against temporary repositories, including staged user work, linked worktrees, and state changes between dispatch and merge; they do not alter the real checkout or agent installation. Each Maestro variant includes its helper so copying an individual skill remains supported.

Use the separate [behavioral evaluation scenarios](evals/workflows.md) to assess agent decisions and outcomes. Passing helper tests does not establish that the full skill workflow passes those scenarios.

The [Code Coach scenarios](evals/code-coach.md) cover explanation quality, question relevance, feedback, misleading comments, user control, and skill selection. They require conversational evaluation; structural checks alone do not establish a pass.

The [PR Stack scenarios](evals/pr-stack.md) cover delegated analysis, one-PR recommendations for coupled changes, useful shared-file boundaries, agreement before mutations, mixed diffs, source preservation, and manual publication.
