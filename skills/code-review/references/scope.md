# Capture the review scope

Honor the user's selected scope. If unclear, ask whether the review covers committed changes, current local changes, or both; do not require a branch base for an explicitly local-only review.

- **Committed branch changes:** resolve the branch/ref, calculate `git merge-base <base> HEAD`, and capture `git diff <merge-base> HEAD` plus the relevant commit list. For an exact commit range supplied by the user, preserve that range rather than substituting a merge-base.
- **All changes since the branch base, including WIP:** capture `git diff <merge-base>` (tracked files from the base to the current working tree), and enumerate new files with `git ls-files --others --exclude-standard -z`. Read the in-scope new files as additions.
- **Local-only WIP:** capture both `git diff --cached` and `git diff`, and enumerate untracked files as above. Keep staged and unstaged changes distinct when a file has both. For staged-only or unstaged-only requests, use only that requested scope.

Use shell-safe argument handling for refs and paths. Do not stage, commit, reset, or stash changes just to review them. Untracked files can be ignored build artifacts or local secrets; inspect names first, include only relevant project changes, and never print secret values.

Preserve the selected patches and the contents of included new files in a temporary review snapshot so both reviewers assess the same state. If source changes during capture, capture again or report the limitation. Only call the review empty when every selected source is empty, including relevant untracked files. Supply the snapshot, included-file list, scope, and commit list (if applicable) to each reviewer.
