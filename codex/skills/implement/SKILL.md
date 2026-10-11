---
name: implement
description: "Implement one bounded local task, spec, or small task set directly in this session, review it, and close completed local tasks. Use only when explicitly invoked; use orbit-forge for orchestrated multi-task runs."
---

# Implement

Implement the work the user describes, or the local spec or Markdown tasks they point to, directly in this session without subagent orchestration. Read applicable `AGENTS.md` instructions; consult the relevant glossary and ADRs only where they bear on the change.

For a local task path or ID, read it from the configured task directory (default `.scratch/<feature-slug>/issues/`) and state its title before starting; ask if the reference is ambiguous. Confirm its blockers are complete. Do not fetch from or update an external issue tracker; if only an external reference is given, ask for the content or a local export. Fill gaps needed for implementation; ask only when an unresolved decision changes behavior or scope.

Record `git status` before editing. Preserve pre-existing and unrelated work; do not stage, stash, reset, or commit user changes.

Use the installed `tdd` skill when test-first work is requested, agreed, or required by the task; use `diagnosing-bugs` for difficult failures. Run typechecking and the single test files you touch regularly, and the full test suite once at the end. Report checks that could not run.

When done, use the installed `code-review` skill on the changes made in this session, including relevant untracked files, against the task's acceptance criteria; distinguish pre-existing changes recorded at the start. Fix confirmed findings within scope and rerun the affected checks. Optional suggestions do not block completion.

When acceptance and both review axes pass, close each completed local task unless the user asked to leave statuses unchanged: set `**Status:** done`, check the verified acceptance criteria, and append a short `## Completion` note with the date and validation evidence. Leave partial or unreviewed tasks open with a note on what remains. Commit only when the user's task authorizes it, following repository conventions.

If the work turns out to need several dependent tasks or an independent reviewer, stop at a clean point and suggest `$orbit-forge`. End with changes made, validation, review verdicts, closed tasks, and remaining limits.
