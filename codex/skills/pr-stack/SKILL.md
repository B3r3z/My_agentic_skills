---
name: pr-stack
description: Assess whether existing changes have logically non-overlapping review layers. Delegate diff analysis; recommend one PR when no useful split exists, otherwise agree and build local branches and hand publication to the user.
---

# PR Stack

Find the clearest way to review an existing diff. One read-only scout first decides whether logically non-overlapping layers exist. Recommend one PR when they do not; a stack is not a required outcome. Root owns the conversation and all mutations. For a viable stack, the user agrees the concrete plan before root creates branches or commits.

Adapted from [GitHub's gh-stack skill](https://github.com/github/gh-stack/tree/2a49e6751238633db504655d8a8eba3e433e827d/skills/gh-stack). This variant prepares existing changes locally and hands publication to the user.

## Local-only boundary

Skill invocation authorizes analysis, then the agreed local branch/commit work. It does **not** authorize publication. Never push, create/edit/link/merge PRs, or mutate GitHub through a CLI, connector, browser, hook, or subagent. Do not execute a generated publication command, even as a validation step.

Use local Git state without fetching or pulling. Do not run `gh stack push`, `submit`, `sync`, `link`, `merge`, bare `unstack`, remote `checkout`, or a fetching rebase. `gh stack init` can query GitHub for existing PRs, and `view --json` can refresh PR metadata, so leave both out of agent execution as well. Build branch ancestry with Git; include gh-stack registration in the command handed to the user. `gh stack <command> --help` is suitable for checking installed syntax. Do not install or update tools automatically.

Do not interpret “stack ready” as “PRs exist”. Report local branches and manual publication separately.

## 1. Delegate exploration and assess whether a stack helps

Read applicable `AGENTS.md`. Establish the repository, source checkout, current HEAD/branch, candidate base from local refs, and the requested scope. Include committed changes since the source fork point, staged and unstaged diffs, and relevant untracked files; do not assume `git diff` alone covers the work. Treat remote-tracking refs as potentially stale.

Spawn one scout subagent using the available delegation tool. Pass the source path, candidate base/range, user constraints, and this skill. The scout must read [stack-design.md](references/stack-design.md), inspect the actual diff and relevant callers/tests, and return:

- A concise inventory of concerns with file/hunk or commit evidence.
- A recommendation: one PR, or a stack with evidence that its layers own distinct logic and are easier to review separately.
- Only for a viable stack: branches bottom to top, with name, parent, purpose, exact owned symbols/hunks, stable dependencies, and local validation. For shared files, explain why the changed sections are logically separate.
- Any coupled changes that must stay together, ambiguity, and work to leave outside the stack.

Do not propose a boundary when higher layers would replace, undo, or materially revise the implementation, contract, or test setup introduced below. Coalesce coupled work before proposing branches. Stable additive dependencies are compatible with a stack; repeated versions of the same logic are not. Do not invent temporary code or fixtures to make an artificial layer pass tests. File counts, commit boundaries, and implementation-task boundaries do not justify a split. If no useful multi-layer split remains, the scout must recommend one PR instead of producing branch names.

Explicitly restrict the scout to local read-only inspection: no file edits, staging, commits, refs, worktrees, stack metadata, remote operations, or further delegation. Do not give it an answer to rubber-stamp. Root can collect context but must not replace the scout's analysis with its own. If delegation is unavailable, report that exploration is pending instead of pretending it happened.

## 2. Present the recommendation and agree a viable split

Check the scout's evidence, including overlap at the level of logic and tests. Return an unsuitable split to the scout for regrouping rather than offering it for approval. Present the recommendation in the user's language. If it is one PR, explain the coupling and finish without repository mutations or a stack-publication command; preparing a single-PR branch requires a follow-up request.

For a viable stack, show the base and source range, an ordered branch table (name, parent, owned logic), shared-file boundaries and why they do not overlap logically, excluded changes, and unresolved decisions. Use repository naming rules or the user's names; otherwise suggest `codex/<topic>-<concern>`.

Ask the user to confirm or revise the split and names. **Pause before any repository, index, ref, worktree, or stack-catalog mutation.** Answer questions and revise the proposal as needed; suggesting a name or discussing a boundary is not automatically approval to execute. Use an already explicit approval of the concrete plan without asking again. Approval covers local work only; do not request permission to publish.

If the diff or approved base changes during discussion, reassess the affected scope before building. Reuse the scout when new analysis is needed. A material change to the agreed partition or names needs renewed agreement; routine mechanics do not.

## 3. Build locally

After agreement, read [local-build.md](references/local-build.md). Freeze the approved input and build bottom to top in a separate worktree, leaving the source checkout and its staged/unstaged distinction intact. Keep original commits reachable. Never reset, clean, stash, or rewrite the user's source branch to make splitting easier.

Use explicit files or selected hunks for staging. For independent sections of a shared file, apply only the current layer's owned changes. Keep behavior and its focused tests together; do not blindly cherry-pick a mixed commit or copy the entire final file into the first layer. Make no feature changes beyond the agreed diff. If reconstruction reveals logical overlap or requires temporary code to preserve the planned layers, stop and return to recommendation/agreement instead of forcing the split.

Each branch must contain its approved parent and only its own incremental concern. Do not adopt, overwrite, delete, or rename a conflicting existing branch silently. Resolve routine reconstruction conflicts from the frozen input; return to the user if the resolution would change intended behavior or the agreed scope.

Run appropriate available local checks for each layer and compare the final result with the frozen scope. Inspect the incremental diffs for repeated revisions to the same logic or test setup; passing tests and matching the final tree do not establish a good split. Verify excluded changes stayed out, no approved hunks were lost or duplicated, and the source HEAD/index/worktree stayed unchanged. Inspect hooks before invoking commits or checks if their effects are unknown; skip a networked step and report it rather than allowing publication through a hook. Do not claim unavailable checks passed.

## 4. Hand off publication

Report the local branch chain, build worktree path, relevant validation, source preservation, and any remaining blocker. Give a copyable command with the **actual** shell-quoted path, base, branch names in bottom-to-top order, and remote selected from local configuration. Ask only if the publication destination is ambiguous; do not invent one.

For a new local chain, the manual command has this shape:

```sh
cd -- '/absolute/build/worktree' && gh stack init --base 'main' 'codex/topic-core' 'codex/topic-api' && gh stack submit --auto --remote 'origin'
```

The user runs it: `init` adopts the prepared branches, then `submit` pushes and creates/updates the GitHub stack. `--auto` creates draft PRs by default; add `--open` only if the user requests ready-for-review PRs. Check the installed `--help` instead of assuming a flag exists. If an existing local gh-stack catalog already tracks the approved chain, omit `init`; do not replace unrelated catalog entries. Supply only commands that match the verified local state.

Use useful commit subjects/bodies because `submit --auto` derives PR text from them (a single commit supplies the title/body; multiple commits use a humanized branch name). If PR text needs customization, explain it in the handoff; do not edit PRs yourself. State that GitHub stacked-PR availability and remote branch collisions were not verified locally. The command is a handoff, not evidence of successful publication.
