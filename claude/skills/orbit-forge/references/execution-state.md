# Source requirements and execution state

Requirements remain in their existing plan or tickets. Record the source path/URL and its revision or retrieval time; if the source changes during execution, reconcile the change before treating it as authorized scope. Do not duplicate or silently rewrite acceptance criteria.

Keep a local execution record at the location configured in `CLAUDE.md`, otherwise `.scratch/orbit-forge/<run-id>/execution.md`. Reuse it when resuming the same run; avoid overwriting unrelated runs. It is a status ledger, not a second backlog. Keep task state in local Markdown; do not retrieve or update an external issue tracker, and do not copy the backlog into Claude's session task tools.

Record only what is needed to resume and verify:

```markdown
# Execution: <goal>
Source: <approved plan or local task files and revision>
Baseline: <HEAD SHA; location of private starting-state snapshot>
State: active | blocked | complete

| Source task | Dependencies | Agent/model | State | Validation evidence |
| --- | --- | --- | --- | --- |
| <existing ID/link> | <IDs> | <agent ID and configuration> | pending | |

Current blocker or next action:
Correction rounds without progress: 0
Review: requirements pending; code quality pending
```

For a conversation-only plan, first save the approved requirements once at the configured plan location, default `docs/plan/YYYY-MM-DD-<slug>.md`. Include goal, scope, acceptance criteria, and bounded tasks with dependencies and checks. Then link to it from the execution record. Existing local task sets need no new plan file.

Task states are `pending`, `active`, `implemented`, `blocked`, and `complete`. Use `implemented` only for a member of a planned integration group whose individual checks passed and whose shared verification is still pending. Link the group's source definition, member IDs, and shared checks; record their results when available. This state permits continuation within the group, not completion or dependent work outside it. Preserve source task statuses unless updating them is authorized.

## Preserve the dirty baseline

Before any worker writes:

- Record HEAD, branch, index/worktree status, and relevant untracked paths.
- Preserve staged and unstaged patches, plus original bytes of in-scope modified and untracked files, in a private local snapshot outside tracked source files. File names or `git status` alone cannot reconstruct the baseline. Include relevant file modes and deletions.
- Do not commit, stage, reset, or stash user changes to obtain a clean baseline. Do not publish private snapshots or secret values. Keep a local pointer to the snapshot for review and resumption.

At acceptance/review, compare the resulting in-scope file contents against this starting snapshot as well as the source requirements. A base-to-final git diff alone also contains pre-existing user work and must not be presented as wholly agent-authored. Include new files and disclose any concurrent edits whose ownership cannot be established; coordinate overlapping edits before continuing.

The root records task status, validation evidence, minor execution adjustments, and accepted/rejected review findings with rationale. A correction round counts as progress only when a confirmed failure is resolved or new evidence materially narrows its cause. Goal or acceptance changes require user direction rather than an execution-record edit alone.
