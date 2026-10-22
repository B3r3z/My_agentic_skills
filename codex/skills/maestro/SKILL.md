---
name: maestro
description: Conduct an approved plan or local task set, sequentially or in parallel git worktrees, with GPT-6.1 Sol at HIGH reasoning effort for implementation and independent review. Use only when the user explicitly requests Maestro orchestration.
---

# Maestro

Root owns dispatch, execution state, scope decisions, merges, and acceptance. By default one implementation agent works at a time; parallel worktree mode is opt-in. Reuse the approved requirements; do not repeat product discovery or rebuild an existing backlog.

## 1. Establish the execution contract

Read applicable `AGENTS.md` instructions and Maestro overrides. Use approved plans and local task files available in the workspace, including their IDs, dependencies, scope, and acceptance criteria. Read the linked glossary and ADRs only where relevant. Fill gaps needed for execution; ask only when an unresolved decision changes behavior or scope.

If the approved plan exists only in conversation, save it once at the configured plan location (default `docs/plan/`). If tickets already exist, link them without copying them into a second backlog. Split work only when it lacks bounded, verifiable tasks. Planning with `grill-with-docs` or `to-tickets` is optional upstream work, not a prerequisite to run again.

Before dispatch, capture the starting state and initialize the small execution record described in [execution-state.md](references/execution-state.md). Root alone maintains this record. Commits, pushes, deployments, and other external writes require authorization in the user's task.

Run sequentially unless the user's request or the Maestro settings in `AGENTS.md` enable parallel worktree mode; then follow [parallel.md](references/parallel.md). Enabling it authorizes local task branches, worktrees, commits on those branches, and merges into the working branch, but not pushes or other external writes.

When several tasks need the same codebase or external-documentation exploration, optionally delegate one exploration agent (`gpt-6.1-sol` / `high`) before dispatch. It reads code and documentation, writes concise notes only in the run's notes directory, and changes nothing else. Link the notes from the execution record and point implementers to them instead of repeating the exploration. Notes are context, not requirements: where they conflict with the source, the source wins.

## 2. Dispatch a ready task

Choose an incomplete task whose dependencies are satisfied. Within an explicitly planned integration group, a prerequisite's `implemented` state permits the next member to start; dependencies outside the group must be `complete`.

Use `gpt-6.1-sol` with reasoning effort `high` for implementation tasks, including clear, bounded work and tasks with consequential design decisions, concurrency, complex algorithms, or substantial uncertainty.

Pass model and effort directly to the available delegation tool, with an empty or bounded history fork. Do not rely on named custom roles. If the required configuration is unavailable, report the blocker without silently substituting it. Reuse an existing suitable implementer for corrections or subsequent tasks when supported; preserve capacity for an independent final reviewer.

A delegated agent lacks the conversation, so its assignment must stand alone, built from context pointers rather than copies: paths to the source task, saved plan, relevant notes, glossary or ADRs, and relevant commits, plus owned paths, validation expectations, and any decision not yet written down. Do not paste content available through a pointer. Ask for a concise report of changed paths, acceptance evidence, and blockers. Preserve all pre-existing and unrelated work. The implementer may change assigned code, tests, and implementation documentation, but not the source requirements or execution record.

Use the installed `tdd` skill when test-first work is requested or agreed; use `diagnosing-bugs` for difficult failures when appropriate. Do not impose either workflow on every task.

## 3. Wait and accept

Mark the task active, then follow [waiting.md](references/waiting.md). A wait timeout is not evidence of failure. Do not poll diffs, logs, or status while the implementer is working.

On completion, inspect the actual changes and validation evidence. Rerun or extend checks when code changed after validation, integration needs checking, or evidence is incomplete. Do not repeat identical checks solely because a different agent ran them. Send concrete contract failures back to the implementer. Normally, mark the task complete only after its criteria pass, then start the next ready task. In parallel mode, completion also requires the merge into the working branch and its integration checks.

For an explicitly planned integration group, check each member's independently verifiable criteria and record it as `implemented` while the named shared checks remain pending. Continue sequentially through the group without requiring those shared checks to pass early. This exception does not defer unrelated failures. After all members are implemented, run the shared checks and mark members complete only when all their criteria pass. Until then, the group remains unverified and does not unblock dependent work outside it. Do not invent a group to bypass a failed check.

Root may make small mechanical integration fixes, then validate those changes. Delegate feature work. Changes to the approved goal, scope, or acceptance criteria need user direction.

## 4. Review and finish

After implementation, use the delegation tool to spawn a fresh read-only `gpt-6.1-sol` / `high` reviewer subagent, independent of the implementer. Explicitly instruct it to read and apply the installed [playback skill](../playback/SKILL.md), including its scope capture, and assess both Standards and Spec itself without spawning further reviewers. Supply the source requirements, execution record, preserved baseline, final changes including WIP and relevant untracked files, and validation evidence. In parallel mode, the scope is the working branch from the baseline commit to its tip, plus any uncommitted root fixes. Standards must also cover correctness and regressions. Root does not perform the closing Playback review itself.

Require evidence and a separate verdict for requirements and code quality. Root checks the validity of findings before reopening tasks. Route confirmed failures through the same implementation gate, then ask the independent reviewer to reassess the corrected scope; reuse that reviewer rather than creating a new instance for every round. Optional suggestions do not automatically fail a review.

After the configured no-progress limit (default two correction rounds on confirmed failures), stop the loop and report the blocker and open items. Unavailable delegation, reviewer capacity, or `playback` leaves review pending, never passed.

When acceptance and both review axes pass, close each completed local source task unless the user asked to leave statuses unchanged: set its status to `done`, check the verified acceptance criteria, and append a short `## Completion` note linking the execution record and, in parallel mode, the merge commit. Leave blocked, partial, or unreviewed tasks open with a note on what remains. In parallel mode, finish the worktree cleanup.

Report completion only when acceptance and both review axes pass; otherwise state the exact incomplete checks. End with changes made, validation, closed tasks, and remaining limits.
