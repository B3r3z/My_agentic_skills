# Reconstructing the agreed local chain

Read only for a viable stack after the user agrees the concrete split. A one-PR recommendation does not enter this workflow. This is a reconstruction task: preserve behavior and the source state, not necessarily the original commit boundaries.

## Freeze and isolate

Record the source branch/HEAD, approved target-base SHA, source fork-point SHA, staged and unstaged binary-capable diffs, and selected untracked file contents/modes. Preserve enough information to compare the source index and working tree afterwards, including excluded changes. Keep snapshots outside the source tree and out of the stack's commits. Do not include secrets or ignored files merely because they exist.

Keep original committed work reachable through its existing source ref or a recorded local backup ref when needed. Never overwrite an existing backup name. A dirty checkout is not an error: build in a separate worktree from the approved base. Use the app's managed-worktree lifecycle when available, otherwise an explicit Git worktree in an appropriate local scratch location. Do not alter source files, its index, or its branch to prepare this worktree.

Check proposed names with `git check-ref-format --branch`, existing local refs, and `git worktree list --porcelain`. Do not take over another checkout. If the checkout is detached, preserve the source tip with a new backup ref before reconstruction. Identify a named local target base for the later `gh stack init --base`; never move an existing trunk to match a desired SHA. A local base branch can be created from an agreed existing SHA if necessary.

Read existing gh-stack catalog files only when needed for collisions or a pre-existing stack. Locate the Git common directory with Git rather than assuming `.git` is a directory. Do not create or hand-edit a gh-stack catalog: registration belongs in the user's handoff command.

## Rebuild bottom to top

Create the first agreed branch at the approved base in the build worktree. Reproduce only its owned changes and commit them. Then create the next agreed branch from the previous branch tip, apply its owned changes, and commit; repeat upward. Use the frozen source rather than a live changing source checkout.

Choose the reconstruction method that preserves the evidence:

- Cherry-pick a commit only when its entire content belongs to the current layer and its dependencies are already present.
- For mixed commits or mixed WIP with independent sections, apply only the selected layer's final logic in the build worktree. Use an alternate index or a temporary snapshot if it helps. Preserve deletions, renames, binary contents, symlinks, executable modes, and selected untracked files.
- Stage explicit paths/hunks and inspect the staged diff before committing. Do not use `git add .`, `git add -A`, or a gh-stack auto-stage shortcut to decide scope.

Use a commit subject that explains the layer. Put useful reviewer context in the body when needed. Splitting alone does not authorize unrelated fixes, formatting, or generated files.

If a layer needs temporary logic or fixtures that the next layer would remove, or would revise the same implementation/contract/test setup again, stop reconstruction and return to the scout and user with a regrouped recommendation. Preserve the source and partial local work. Do not silently change the approved partition or force it to pass with throwaway intermediate code.

Check each `parent..branch` diff against its agreed ownership and use `git merge-base --is-ancestor <parent> <branch>` to verify ancestry. Run relevant local checks without fetching dependencies or invoking networked hooks. Inspect configured hook paths before commits; if a hook would cross the local-only boundary, bypass it for these commits and report the skipped validation. An unexpected failure leaves the preserved source and partial local branches available; do not clean them away to hide incomplete work.

## Verify and retain

Compare the top branch's resulting tree with the expected application of the frozen approved diff onto the approved base. If all source changes are included and the base is the original fork point, the top tree should match the frozen source working tree (including selected untracked files). When the target base has advanced or some source changes were excluded, compare against that intended integration instead; do not discard unrelated newer trunk changes to force whole-tree equality.

Verify every approved change appears once in its layer, excluded changes remain absent, intermediate branches are coherent, and the final build worktree is clean. Compare incremental diffs for repeated changes to the same logic or test setup; final-tree equality and green tests do not validate review boundaries. Recheck the source branch/HEAD, index contents, staged/unstaged diffs, and relevant untracked contents against the captured state. If the user concurrently edited the source, retain their edits and explain the drift; do not restore the old snapshot over them.

Keep the verified build worktree available for the user's manual publication command. Report its absolute path, retained source/backup refs, branch chain, checks and skips. If required checks fail, give the blocker and recovery state instead of presenting a ready-to-run publication command. If a check is unavailable, state the limitation explicitly and distinguish it from a failing check.

Before handoff, check installed syntax with `gh stack init --help` and `gh stack submit --help`, and choose the intended GitHub remote from local URLs/configuration. `init` adopts existing branches without reconstructing their ancestry and checks out the last one. It can query PRs and enable repository-local `rerere`; leave execution to the user. `submit --auto` pushes **all active branches in that stack** and creates/updates PRs, so the handed-off chain must contain only the agreed work.
