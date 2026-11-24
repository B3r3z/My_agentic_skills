# Claude Code configuration

`skills/` contains 16 Claude Code skills, with supporting references, templates, and licenses. `agents/` contains the `maestro` subagents: `maestro-sonnet` and `maestro-opus` implementers, the optional `maestro-scout` explorer, and the independent `maestro-critic` reviewer.

## Install

From the repository root:

```sh
python3 scripts/install.py claude --dry-run
python3 scripts/install.py claude
```

This links the collection into `~/.claude/skills/` and its subagents into `~/.claude/agents/`. For one project, pass `--target /path/to/project/.claude`. Existing entries are never replaced. Keep this repository at the installed path or copy the skill directories and agent files instead.

Start a Claude Code session and check the `/` menu for skills and `/agents` for the Maestro definitions. Run `/setup-b4rt-skills` in the project to add its task and domain documentation settings to `CLAUDE.md`.

## Use

```text
/grill-with-docs   Refine a design and record agreed terminology/decisions
/wayfinder        Map decisions across sessions
/research         Investigate a question and save cited findings
/to-spec          Save agreed decisions as a local specification
/to-tickets       Write local Markdown implementation tasks
/solo             Build locally, obtain a Playback subagent review, and close
/maestro          Conduct an approved plan with independent review
/tdd              Implement requested behavior test-first
/playback         Review code against the spec and standards
/diagnosing-bugs  Investigate a failure
/code-coach       Understand code, assumptions, and tradeoffs through discussion
/simple-english   Write or review technical text in plain English or requested STE
```

`grilling`, `domain-modeling`, and `codebase-design` are also available independently and as supporting skills.

Solo uses a fresh read-only reviewer through `Agent`, explicitly instructed to load `playback`. Maestro uses `maestro-critic`, which preloads `playback`. Each reviewer assesses both Standards and Spec; the main session waits for its verdicts before closing tasks.

The seven explicit-only skills are `setup-b4rt-skills`, `grill-with-docs`, `wayfinder`, `to-spec`, `to-tickets`, `solo`, and `maestro`. Their `disable-model-invocation: true` setting preserves the Codex collection's invocation policy. Other skills remain available for automatic selection.

Project configuration belongs in `CLAUDE.md`; domain terminology stays in `CONTEXT.md`, decisions in `docs/adr/`, specifications in `docs/plan/`, and implementation tasks in `.scratch/<feature-slug>/issues/` unless configured otherwise. Planning and ticket skills retain their local-only behavior.

For parallel Maestro runs, enable the mode in the request or in `CLAUDE.md`, for example:

```markdown
### Maestro

- Parallel worktree mode: enabled, up to 3 implementers, merging into the current branch.
```

Root creates task worktrees with `git worktree add` from the working-branch tip rather than the `Agent` tool's worktree isolation, which branches from the remote default branch unless `worktree.baseRef` is `head`.

The main checkout's entire index must be clean. Maestro checks it before dispatch and each merge with its bundled `scripts/check_git_state.py`; unrelated staged changes also block merging. Before dispatch it falls back to sequential work; after dispatch it pauses integration and keeps task worktrees. The helper also resolves Git's exclude-file path. If the worktree root is not ignored, root adds its directory pattern there without editing tracked ignore files; this works when the main checkout is itself a linked worktree.

## Compatibility

This variant uses Claude's skill frontmatter rather than `agents/openai.yaml`, and `/name` rather than Codex's `$name`. Conversation-based skills run in the main session to retain the agreed context. Maestro reads its installed subagent definitions; its model choices are documented there instead of using GPT model identifiers.

Implementation follows the official [skill locations and invocation documentation](https://code.claude.com/docs/en/skills), [subagent configuration](https://code.claude.com/docs/en/sub-agents), and [project memory documentation](https://code.claude.com/docs/en/memory), checked on 2026-09-30, and the [worktree documentation](https://code.claude.com/docs/en/worktrees), checked on 2026-10-11.
