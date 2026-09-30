---
name: orbit-forge
description: Execute an approved plan or local task set sequentially with Sonnet or Opus implementers and an independent Opus review. Use only when the user explicitly requests Orbit Forge orchestration.
disable-model-invocation: true
---

# Orbit Forge

Root owns dispatch, execution state, scope decisions, and acceptance. One implementation agent works at a time. Reuse the approved requirements; do not repeat product discovery or rebuild an existing backlog.

## 1. Establish the execution contract

Read applicable `CLAUDE.md` instructions and Orbit Forge overrides. Use approved plans and local task files available in the workspace, including their IDs, dependencies, scope, and acceptance criteria. Read the linked glossary and ADRs only where relevant. Fill gaps needed for execution; ask only when an unresolved decision changes behavior or scope.

If the approved plan exists only in conversation, save it once at the configured plan location (default `docs/plan/`). If tickets already exist, link them without copying them into a second backlog. Split work only when it lacks bounded, verifiable tasks. Planning with `grill-with-docs` or `to-tickets` is optional upstream work, not a prerequisite to run again.

Before dispatch, capture the starting state and initialize the small execution record described in [execution-state.md](references/execution-state.md). Root alone maintains this record. Source tickets and execution state stay in local Markdown; Claude's session task tools do not replace them. Commits, pushes, deployments, and other external writes require authorization in the user's task. Do not retrieve or update an external issue tracker.

## 2. Dispatch a ready task

Choose an incomplete task whose dependencies are satisfied. Within an explicitly planned integration group, a prerequisite's `implemented` state permits the next member to start; dependencies outside the group must be `complete`.

Choose the implementer:

- Clear, bounded work: `orbit-forge-sonnet`, configured with `model: sonnet` and `effort: high`.
- Consequential design decisions, concurrency, complex algorithms, or substantial uncertainty: `orbit-forge-opus`, configured with `model: opus` and `effort: high`.

These agent definitions ship in this collection's `claude/agents/` and must be installed in `~/.claude/agents/` or the project's `.claude/agents/`. Use Claude Code's `Agent` tool with the selected custom agent type and a self-contained assignment. The definitions set model and effort; do not send Codex reasoning or history-fork parameters. Start a regular subagent with fresh context rather than a conversation fork. Do not enable agent teams, change session permission settings, or create a worktree just to run this workflow. If a required definition or configuration is unavailable or Claude Code reports model substitution, report the actual configuration and blocker instead of silently accepting the change. Reuse a suitable existing implementer for corrections using the available resume mechanism; preserve capacity for an independent final reviewer.

Give the implementer the source task, repository instructions, owned paths, relevant context, acceptance criteria, and validation expectations. Preserve all pre-existing and unrelated work. The implementer may change assigned code, tests, and implementation documentation, but not the source requirements or execution record.

Use the installed `tdd` skill when test-first work is requested or agreed; use `diagnosing-bugs` for difficult failures when appropriate. Do not impose either workflow on every task.

## 3. Wait and accept

Mark the task active, then follow [waiting.md](references/waiting.md). A wait timeout is not evidence of failure. Do not poll diffs, logs, or status while the implementer is working.

On completion, inspect the actual changes and validation evidence. Rerun or extend checks when code changed after validation, integration needs checking, or evidence is incomplete. Do not repeat identical checks solely because a different agent ran them. Send concrete contract failures back to the implementer. Normally, mark the task complete only after its criteria pass, then start the next ready task.

For an explicitly planned integration group, check each member's independently verifiable criteria and record it as `implemented` while the named shared checks remain pending. Continue sequentially through the group without requiring those shared checks to pass early. This exception does not defer unrelated failures. After all members are implemented, run the shared checks and mark members complete only when all their criteria pass. Until then, the group remains unverified and does not unblock dependent work outside it. Do not invent a group to bypass a failed check.

Root may make small mechanical integration fixes, then validate those changes. Delegate feature work. Changes to the approved goal, scope, or acceptance criteria need user direction.

## 4. Review and finish

After implementation, start a fresh `orbit-forge-reviewer` subagent, configured with `model: opus` and `effort: high`, independent of the implementer. Root captures the final review scope using the installed `code-review` skill's [scope rules](../code-review/references/scope.md), including WIP and relevant untracked files, and supplies readable patches/status evidence alongside the source requirements, execution record, preserved baseline, final files, and validation evidence. The reviewer has only read/search/skill tools, so root supplies any required git or validation output. Its preloaded `code-review` skill assesses Standards and Spec without another reviewer layer. Standards must also cover correctness and regressions.

Require evidence and a separate verdict for requirements and code quality. Root checks the validity of findings before reopening tasks. Route confirmed failures through the same implementation gate, then ask the independent reviewer to reassess the corrected scope; reuse that reviewer rather than creating a new instance for every round. Optional suggestions do not automatically fail a review.

After the configured no-progress limit (default two correction rounds on confirmed failures), stop the loop and report the blocker and open items. Missing reviewer capacity leaves review pending, never passed. Report completion only when acceptance and both review axes pass; otherwise state the exact incomplete checks. End with changes made, validation, and remaining limits.
