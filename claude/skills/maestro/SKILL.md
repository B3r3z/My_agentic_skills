---
name: maestro
description: Conduct an approved plan or local task set with Sonnet or Opus implementers, sequentially or in parallel git worktrees, and an independent Opus critic. Use only when the user explicitly requests Maestro orchestration.
disable-model-invocation: true
---

# Maestro

Root owns dispatch, execution state, scope decisions, merges, and acceptance. By default one implementation agent works at a time; parallel worktree mode is opt-in. Reuse the approved requirements; do not repeat product discovery or rebuild an existing backlog.

## 1. Establish the execution contract

Read applicable `CLAUDE.md` instructions and Maestro overrides. Use approved plans and local task files available in the workspace, including their IDs, dependencies, scope, and acceptance criteria. Read the linked glossary and ADRs only where relevant. Fill gaps needed for execution; ask only when an unresolved decision changes behavior or scope.

If the approved plan exists only in conversation, save it once at the configured plan location (default `docs/plan/`). If tickets already exist, link them without copying them into a second backlog. Split work only when it lacks bounded, verifiable tasks. Planning with `grill-with-docs` or `to-tickets` is optional upstream work, not a prerequisite to run again.

Before dispatch, capture the starting state and initialize the small execution record described in [execution-state.md](references/execution-state.md). Root alone maintains this record. Source tickets and execution state stay in local Markdown; Claude's session task tools do not replace them. Commits, pushes, deployments, and other external writes require authorization in the user's task. Do not retrieve or update an external issue tracker.

Run sequentially unless the user's request or the Maestro settings in `CLAUDE.md` enable parallel worktree mode; then follow [parallel.md](references/parallel.md). Enabling it authorizes local task branches, worktrees, commits on those branches, and merges into the working branch, but not pushes or other external writes.

When several tasks need the same codebase or external-documentation exploration, optionally start one `maestro-scout` subagent before dispatch. It saves concise notes in the run's notes directory; link them from the execution record and point implementers to them instead of repeating the exploration. Notes are context, not requirements: where they conflict with the source, the source wins.

## 2. Dispatch a ready task

Choose an incomplete task whose dependencies are satisfied. Within an explicitly planned integration group, a prerequisite's `implemented` state permits the next member to start; dependencies outside the group must be `complete`.

Choose the implementer:

- Clear, bounded work: `maestro-sonnet`, configured with `model: sonnet` and `effort: high`.
- Consequential design decisions, concurrency, complex algorithms, or substantial uncertainty: `maestro-opus`, configured with `model: opus` and `effort: high`.

These agent definitions, with `maestro-scout` and `maestro-critic`, ship in this collection's `claude/agents/` and must be installed in `~/.claude/agents/` or the project's `.claude/agents/`. Use Claude Code's `Agent` tool with the selected custom agent type. The definitions set model and effort; do not send Codex reasoning or history-fork parameters. Start a regular subagent with fresh context rather than a conversation fork. Do not enable agent teams or change session permission settings; create worktrees only in parallel mode. If a required definition or configuration is unavailable or Claude Code reports model substitution, report the actual configuration and blocker instead of silently accepting the change. Reuse a suitable existing implementer for corrections using the available resume mechanism; preserve capacity for an independent final reviewer.

A fresh subagent lacks the conversation, so its assignment must stand alone, built from context pointers rather than copies: paths to the source task, saved plan, relevant notes, glossary or ADRs, and relevant commits, plus owned paths, validation expectations, and any decision not yet written down. Do not paste content available through a pointer. Ask for a concise report of changed paths, acceptance evidence, and blockers. Preserve all pre-existing and unrelated work. The implementer may change assigned code, tests, and implementation documentation, but not the source requirements or execution record.

Use the installed `tdd` skill when test-first work is requested or agreed; use `diagnosing-bugs` for difficult failures when appropriate. Do not impose either workflow on every task.

## 3. Wait and accept

Mark the task active, then follow [waiting.md](references/waiting.md). A wait timeout is not evidence of failure. Do not poll diffs, logs, or status while the implementer is working.

On completion, inspect the actual changes and validation evidence. Rerun or extend checks when code changed after validation, integration needs checking, or evidence is incomplete. Do not repeat identical checks solely because a different agent ran them. Send concrete contract failures back to the implementer. Normally, mark the task complete only after its criteria pass, then start the next ready task. In parallel mode, completion also requires the merge into the working branch and its integration checks.

For an explicitly planned integration group, check each member's independently verifiable criteria and record it as `implemented` while the named shared checks remain pending. Continue sequentially through the group without requiring those shared checks to pass early. This exception does not defer unrelated failures. After all members are implemented, run the shared checks and mark members complete only when all their criteria pass. Until then, the group remains unverified and does not unblock dependent work outside it. Do not invent a group to bypass a failed check.

Root may make small mechanical integration fixes, then validate those changes. Delegate feature work. Changes to the approved goal, scope, or acceptance criteria need user direction.

## 4. Review and finish

After implementation, use Claude Code's `Agent` tool to start a fresh read-only `maestro-critic` subagent, configured with `model: opus` and `effort: high`, independent of the implementer. Explicitly instruct it to apply its preloaded `playback` skill and assess both Standards and Spec itself without spawning further reviewers. Root captures the final review scope using the installed `playback` skill's [scope rules](../playback/references/scope.md), including WIP and relevant untracked files, and supplies readable patches/status evidence alongside the source requirements, execution record, preserved baseline, final files, and validation evidence. In parallel mode, the scope is the working branch from the baseline commit to its tip, plus any uncommitted root fixes. The reviewer has only read/search/skill tools, so root supplies any required git or validation output. Standards must also cover correctness and regressions. Root does not perform the closing Playback review itself.

Require evidence and a separate verdict for requirements and code quality. Root checks the validity of findings before reopening tasks. Route confirmed failures through the same implementation gate, then ask the independent reviewer to reassess the corrected scope; reuse that reviewer rather than creating a new instance for every round. Optional suggestions do not automatically fail a review.

After the configured no-progress limit (default two correction rounds on confirmed failures), stop the loop and report the blocker and open items. Unavailable delegation, reviewer capacity, or `playback` leaves review pending, never passed.

When acceptance and both review axes pass, close each completed local source task unless the user asked to leave statuses unchanged: set its status to `done`, check the verified acceptance criteria, and append a short `## Completion` note linking the execution record and, in parallel mode, the merge commit. Leave blocked, partial, or unreviewed tasks open with a note on what remains. In parallel mode, finish the worktree cleanup.

Report completion only when acceptance and both review axes pass; otherwise state the exact incomplete checks. End with changes made, validation, closed tasks, and remaining limits.
