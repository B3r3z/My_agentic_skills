---
name: orbit-forge
description: Execute an approved plan or tickets sequentially with Luna MAX or Sol HIGH implementers and an independent Sol HIGH review. Use explicitly for repository implementation.
---

# Orbit Forge

Root owns dispatch, execution state, scope decisions, and acceptance. One implementation agent works at a time. Reuse the approved requirements; do not repeat product discovery or rebuild an existing backlog.

## 1. Establish the execution contract

Read `AGENTS.md` for project instructions, tracker settings, documentation paths, and any Orbit Forge overrides. Use existing plan/ticket IDs, dependencies, scope, and acceptance criteria. Read the linked glossary and ADRs only where relevant. Fill gaps needed for execution; ask only when an unresolved decision changes behavior or scope.

If the approved plan exists only in conversation, save it once at the configured plan location (default `docs/plan/`). If tickets already exist, link them without copying them into a second backlog. Split work only when it lacks bounded, verifiable tasks. Planning with `grill-with-docs` or `to-tickets` is optional upstream work, not a prerequisite to run again.

Before dispatch, capture the starting state and initialize the small execution record described in [execution-state.md](references/execution-state.md). Root alone maintains this record. Tracker updates, commits, pushes, deployments, and other external writes require authorization in the user's task.

## 2. Dispatch a ready task

Choose an incomplete task whose dependencies are satisfied:

- Clear, bounded work: `gpt-5.6-luna`, reasoning effort `max`.
- Consequential design decisions, concurrency, complex algorithms, or substantial uncertainty: `gpt-5.6-sol`, reasoning effort `high`.

Pass model and effort directly to the available delegation tool, with an empty or bounded history fork and a self-contained assignment. Do not rely on named custom roles. If the required configuration is unavailable, report the blocker without silently substituting it. Reuse an existing suitable implementer for corrections or subsequent tasks when supported; preserve capacity for an independent final reviewer.

Give the implementer the source task, repository instructions, owned paths, relevant context, acceptance criteria, and validation expectations. Preserve all pre-existing and unrelated work. The implementer may change assigned code, tests, and implementation documentation, but not the source requirements or execution record.

Use the installed `tdd` skill when test-first work is requested or agreed; use `diagnosing-bugs` for difficult failures when appropriate. Do not impose either workflow on every task.

## 3. Wait and accept

Mark the task active, then follow [waiting.md](references/waiting.md). A wait timeout is not evidence of failure. Do not poll diffs, logs, or status while the implementer is working.

On completion, inspect the actual changes and validation evidence. Rerun or extend checks when code changed after validation, integration needs checking, or evidence is incomplete. Do not repeat identical checks solely because a different agent ran them. Send concrete contract failures back to the implementer; mark the task complete only after its criteria pass. Start the next ready task afterward.

Root may make small mechanical integration fixes, then validate those changes. Delegate feature work. Changes to the approved goal, scope, or acceptance criteria need user direction.

## 4. Review and finish

After implementation, obtain a fresh read-only `gpt-5.6-sol` / `high` reviewer, independent of the implementer. Supply the source requirements, execution record, preserved baseline, final changes including WIP, and validation evidence. Use the installed `code-review` skill's scope capture and Standards/Spec criteria; have this reviewer assess both axes without spawning another reviewer layer. Its Code quality assessment must also cover correctness and regressions.

Require evidence and a separate verdict for requirements and code quality. Root checks the validity of findings before reopening tasks. Route confirmed failures through the same implementation gate, then ask the independent reviewer to reassess the corrected scope; reuse that reviewer rather than creating a new instance for every round. Optional suggestions do not automatically fail a review.

After the configured no-progress limit (default two correction rounds on confirmed failures), stop the loop and report the blocker and open items. Missing reviewer capacity leaves review pending, never passed. Report completion only when acceptance and both review axes pass; otherwise state the exact incomplete checks. End with changes made, validation, and remaining limits.
