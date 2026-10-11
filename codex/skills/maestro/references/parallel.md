# Parallel worktree mode

Use this mode only when the user's request or the Maestro settings in `AGENTS.md` enable it. Settings there may override the concurrency limit (default 3 implementers), the working branch (default: the branch checked out at baseline), and the worktree root (default `.scratch/maestro/<run-id>/worktrees/`).

Root creates and removes worktrees with git directly, so every task branch starts from the working branch rather than a host default.

## Preconditions

- The main checkout is on the working branch, not a detached HEAD, and stays there for the whole run.
- No path a task may change has staged, unstaged, or untracked changes. Unrelated dirty files may remain; the baseline snapshot covers them and they are never committed. Otherwise run sequentially or ask the user.
- Git ignores the worktree root (`git check-ignore`). If not, add it to `.git/info/exclude` rather than editing tracked files, and record that.
- Worktrees contain only committed files. Source tasks, the plan, notes, and the execution record stay in the main checkout, so assignments use absolute paths to them.

If the sandbox or host blocks worktree creation or commits, request the needed approval under the user's authorization; otherwise report it and continue sequentially.

## Dispatch

Start up to the concurrency limit from the ready frontier. Run tasks together only when their owned paths are disjoint, including shared files such as lockfiles, generated code, migrations, and registries; otherwise queue the later task. Run an integration group in one worktree on one group branch, member by member, and merge it only after its shared checks pass.

For each task, create a worktree from the current working-branch tip:

```sh
git worktree add -b maestro/<run-id>/<task-id> <worktree-root>/<task-id> <working-branch>
```

Record the path, branch, and base commit, then delegate with them in the assignment. The implementer works only inside its worktree, confirms the branch and base before editing, commits its task changes on the task branch, merges the latest working-branch tip into it, resolves conflicts within its task's scope, and reruns relevant checks before reporting. It never pushes, rebases, force-updates, or changes other branches.

## Accept and merge

Inspect `git diff <working-branch>...<task-branch>` and the validation evidence; send failures back to the same implementer and worktree. After acceptance, merge from the main checkout following the repository's merge convention, default `git merge --no-ff <task-branch>`. Never rebase, reset, or force-update, and do not resolve feature conflicts at root: on a conflict, abort the merge and return the task to its implementer to merge the new tip.

After the merge, run the checks that cover integration with work merged since the task's base, record the merge commit, mark the task complete, and dispatch newly ready tasks. Commit root's small mechanical integration fixes separately on the working branch. Corrections to merged work, including review corrections, use a new worktree from the current tip and the same merge path.

## Cleanup

Once a task's branch is merged and its checks pass, remove its worktree with `git worktree remove <path>` and delete its branch with `git branch -d <branch>`. At the end of the run, run `git worktree prune`, confirm no run worktrees remain, and remove the run's empty worktree root. Never force-remove a worktree with uncommitted changes or delete an unmerged branch: keep blocked or unmerged work, list its path and branch in the execution record, and report it.
