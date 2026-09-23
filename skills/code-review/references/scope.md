# Capture the review scope

Honor the user's selected scope: changes, selected files, or a repository audit. Ask only when the request and context leave materially different scopes possible; do not require a branch base for local-only work or an audit without a diff.

- **Committed branch changes:** resolve the branch/ref, calculate `git merge-base <base> HEAD`, and capture `git diff <merge-base> HEAD` plus the relevant commit list. For an exact commit range supplied by the user, preserve that range rather than substituting a merge-base.
- **All changes since the branch base, including WIP:** capture `git diff <merge-base>` (tracked files from the base to the current working tree), and enumerate new files with `git ls-files --others --exclude-standard -z`. Read the in-scope new files as additions.
- **Local-only WIP:** capture both `git diff --cached` and `git diff`, and enumerate untracked files as above. Keep staged and unstaged changes distinct when a file has both. For staged-only or unstaged-only requests, use only that requested scope.
- **Selected files or repository audit:** inspect current contents, including relevant local changes, and follow callers or supporting files as needed. Record the scope and current revision/worktree status. No base branch or nonempty diff is required; distinguish existing issues from regressions when evidence permits.

Use shell-safe argument handling for refs and paths. Do not stage, commit, reset, or stash changes just to review them. Untracked files can be ignored build artifacts or local secrets; inspect names first, include only relevant project changes, and never print secret values.

For one reviewer working on a stable state, the recorded scope and revision/worktree status are sufficient. Create a temporary snapshot when reviewers work in parallel, files may change during review, or the review must resume against the same state. Preserve the selected patches and relevant file contents, including untracked files; give each reviewer the same snapshot and scope. If source changes during capture or review, reassess the affected scope or report the limitation.

Only call a changes-only review empty when every selected source is empty, including relevant untracked files. An empty diff does not make a file or repository audit empty.
