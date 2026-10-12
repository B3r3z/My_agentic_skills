---
name: solo
description: "Implement one bounded local task, spec, or small task set solo in this session, without subagents, then review it and close completed local tasks. Use only when explicitly invoked; use maestro for orchestrated multi-task runs."
disable-model-invocation: true
---

# Solo

Implement the work the user describes, or the local spec or Markdown tasks they point to, directly in this session without subagent orchestration. Read applicable `CLAUDE.md` instructions; consult the relevant glossary and ADRs only where they bear on the change.

For a local task path or ID, read it from the configured task directory (default `.scratch/<feature-slug>/issues/`) and state its title before starting; ask if the reference is ambiguous. Confirm its blockers are complete. Do not fetch from or update an external issue tracker; if only an external reference is given, ask for the content or a local export. Fill gaps needed for implementation; ask only when an unresolved decision changes behavior or scope.

Before editing, capture HEAD, branch, staged/unstaged status, and relevant untracked paths. Preserve any pre-existing changes in scope using [baseline.md](references/baseline.md), including their original contents; keep this baseline through review. Preserve unrelated work; do not stage, stash, reset, or commit user changes.

Use the installed `tdd` skill when test-first work is requested, agreed, or required by the task; use `diagnosing-bugs` for difficult failures. Follow the user's validation constraints and the repository's required checks. Run focused checks for changed behavior; include typechecking where applicable and broader suites when required or when affected contracts cross module boundaries. Once checks pass, repeat or expand them only for subsequent changes, failures, or unresolved concerns. Report required checks that could not run and leave the corresponding acceptance criteria unverified.

When done, use the installed `playback` skill on the changes made in this session, including relevant untracked files, against the task's acceptance criteria; distinguish pre-existing changes using the preserved baseline. Assess both review axes in this session without spawning reviewers. Fix confirmed findings within scope and rerun the affected checks. Optional suggestions do not block completion.

When acceptance and both review axes pass, close each completed local task unless the user asked to leave statuses unchanged: set `**Status:** done`, check the verified acceptance criteria, and append a short `## Completion` note with the date and validation evidence. Leave partial or unreviewed tasks open with a note on what remains. Commit only when the user's task authorizes it, following repository conventions.

If the work turns out to need several dependent tasks or an independent reviewer, stop at a clean point and suggest `/maestro`. End with changes made, validation, review verdicts, closed tasks, and remaining limits.
