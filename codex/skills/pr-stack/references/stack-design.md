# Choosing the layers of an existing diff

Adapted from GitHub's gh-stack stack-design guidance. Use this during the scout's analysis.

A stack is linear, bottom to top:

```text
main <- codex/topic-model <- codex/topic-api <- codex/topic-ui
```

Each branch's eventual PR compares it with its immediate parent. Dependencies belong in the same or a lower layer. First compare a stack with reviewing the whole change in one PR. Propose layers only when they own distinct logic and improve review. If the change cannot be separated that way, recommend one PR without proposing an artificial stack.

## Check logical ownership before proposing branches

The same file can appear in several layers when independent sections change. Conversely, different files can share one contract or invariant that needs review as a whole. Inspect changed symbols, their callers, and tests; a shared-file count is evidence to investigate, not a pass/fail threshold.

A stable lower-layer API used by a new upper-layer consumer is a useful dependency. A later layer replacing, undoing, or materially revising lower-layer logic, its contract, or its test setup is logical overlap: keep those changes together. Do not introduce a temporary implementation, adapter, expectation, or fixture solely to keep an artificial lower layer green before replacing it above.

For example, splitting a task-identity change into compatibility and UUID-writing layers is unsuitable when that makes the same constructor and tests go through two versions, including manual UUID substitution removed in the next layer. Treat the complete identity change as one review unit. A smaller diff or a plausible staged rollout that the user has not requested does not establish a review benefit.

Coalesce coupled groups, then reassess the remaining boundaries. If only one coherent group remains, the correct scout result is one PR. Do not preserve a branch count just because it follows implementation tasks or existing commits.

For an existing diff, inspect both the final files and the changes that produced them. Separate behavioral changes from preparatory refactors only when the intermediate refactor preserves behavior and is useful independently. Keep implementation with its focused tests. Put cross-layer integration tests above their dependencies when they cannot sensibly live lower.

Shared files need symbol/hunk-level ownership. Name the separate sections and verify that higher layers leave lower-layer logic and tests intact; assigning the same logic to several successive versions is not a valid split. Account for renames, deletions, binary files, modes, and relevant untracked additions as well as text edits.

Every in-scope change must have exactly one owning layer. A higher branch contains lower changes through ancestry, not duplicated patches. List unrelated or ambiguous work as excluded or unresolved; never silently publish every staged or untracked file. Independent efforts may deserve separate stacks rather than an artificial dependency. Bring that choice to the user.

Prefer a shared topic in names, following user/repository conventions. In their absence use `codex/<topic>-<concern>`. Names are literal: gh-stack does not add a prefix.

The proposal should make it possible to assess the split without reading the entire diff: branch, parent, short purpose, owned changes, validation, and any dependency that constrains the order. Root presents and discusses it before mutations.
