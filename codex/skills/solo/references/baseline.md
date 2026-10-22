# Preserve the session baseline

Capture the baseline before the first edit. Record the repository root, HEAD, branch, staged and unstaged status, and relevant untracked paths. For unchanged tracked files, HEAD provides their original contents; a filename/status list is insufficient for files that already contain user changes.

For pre-existing changes in scope, create a private snapshot outside the working tree, readable only by the current user. Preserve:

- Separate staged and unstaged binary patches, including modes and deletions. Use `git diff --cached --binary --full-index --no-ext-diff --no-textconv -- <paths>` and the same command without `--cached`; quote each selected path and save output directly to the snapshot.
- The current bytes and file modes of modified and relevant untracked files, including binary files. Preserve symlinks as links without following their targets; record missing/deleted paths explicitly.
- The selected paths and their relationship to the recorded HEAD, so pre-existing additions can be distinguished from files created during this session.

Inspect names before copying; include only task-relevant paths. Do not print private contents or commit, stage, stash, or reset user changes to create the baseline. Retain the snapshot's path through review and any resumed work. If scope expands, capture the additional paths before first editing them and record when they were captured. Coordinate concurrent edits rather than claiming an uncertain baseline is exact.

For closing review, supply the independent Playback reviewer with the captured starting contents and relevant final files, including newly created paths and deletions. Have it compare them using HEAD for initially unchanged tracked files; a diff against HEAD alone would include pre-existing user work. Report attribution gaps if the original content was not captured, and keep affected acceptance/review items pending until resolved.
