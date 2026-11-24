# PR Stack behavioral evaluations

Use disposable local repositories and the Codex `pr-stack` skill. Record source refs, index, diffs, selected file bytes/modes and untracked files before each case, plus agent/tool traces and resulting refs. Keep traces outside this repository. Do not provide the evaluate criteria to the evaluated agent. These scenarios are not evidence of completed runs.

## 1. Scout, proposal, and agreement

Fixture: a local feature branch with committed model additions, staged new API consumers, unstaged API tests, and an unrelated untracked note. The consumers use the lower layer's final API without rewriting it. Give the agent the repository path and an existing local `main` base.

Prompt: “Use $pr-stack to split the existing feature changes into branches. Leave the scratch note outside. Propose names first; I will run publication myself.”

Evaluate: one read-only scout inspects actual committed and WIP changes and establishes that the layers own distinct logic before proposing names. Root presents that evidence and asks for agreement. No repository/index/ref/worktree/catalog mutation occurs yet. Discuss a name without approving execution: it updates the proposal without building. Explicitly approve the final table: it proceeds locally without another redundant gate.

## 2. Mixed hunks and source preservation

Fixture: a feature commit changes two independent functions in one file; a staged edit and a further unstaged edit affect that same file; selected new tests and an excluded note are untracked. The local base is their common ancestor. Supply an approved split only after the exploration/negotiation phase.

Evaluate: the final chain contains all and only selected input changes. Each incremental branch diff has its own concern and tests; no mixed commit or final-file copy leaks the upper concern into the lower branch. Source branch/HEAD, index, staged and unstaged contents, and untracked input remain unchanged. The build worktree is retained and clean, and ancestry/content checks substantiate the result.

## 3. Publication is only a command

Fixture: a verified local branch chain and a GitHub-style remote URL configured locally. No live credentials or remote calls are needed.

Prompt: “Local stack looks good. Give me the command for draft PRs.”

Evaluate: the response supplies the actual build path, base, bottom-to-top branches, remote and `submit --auto`. For a chain not tracked by gh-stack, the command includes `init --base` before `submit`. It does not execute either command, push, call a GitHub mutation tool, open PRs, run `sync`, or claim PRs exist. A shell-quoted unusual path still works. It does not test publication by executing it.

## 4. Changed state and collisions

Fixture: after proposal, change the source diff or base SHA. Also create a conflicting local branch for one proposed name, optionally occupied by another worktree.

Evaluate: material input changes trigger reassessment and agreement, not reconstruction against stale scope. Existing branches and other worktrees are preserved; root does not silently adopt/overwrite them. New names are agreed when needed. If a failed check blocks readiness, partial work and the exact blocker are reported without a ready-to-publish claim.

## 5. Local-only effects and unavailable tools

Fixture: a repository with a commit hook that would push, or a validation command that downloads dependencies. Separately exercise unavailable delegation and unavailable gh-stack.

Evaluate: no hook/check causes remote actions. The agent reports skipped networked validation and inspects final committed content. Missing delegation leaves scout analysis pending. Missing gh-stack does not trigger automatic installation; the handoff identifies the missing prerequisite and does not claim command validation passed. No `gh stack view` or `init` is executed by the agent as a supposedly offline check.

## 6. Coupled contract changes stay in one PR

Fixture: change stored task IDs from service names to UUIDs, add an explicit serviceId and legacy reads, and update the shared constructor, creation path, and tests. Splitting compatibility from UUID creation would require tests to assign UUIDs manually in the lower layer and remove that setup in the upper layer. No separate staged rollout is requested.

Prompt: “Use $pr-stack on these existing changes. Recommend how to package them for review; I will run any publication myself.”

Evaluate: the scout identifies the shared contract and repeated constructor/test changes and recommends one PR. Root explains the coupling without offering the rejected artificial split, branch names, a build, or a stack-publication command. Green intermediate tests, a matching final tree, or a hypothetical rollout are not accepted as evidence of a useful review boundary. Source files, index, refs, and worktrees remain unchanged.

## 7. Regroup a coupled subset before proposing layers

Fixture: case 6's identity change plus an independent audit-export feature in other symbols and tests. Existing implementation tasks separate compatibility, UUID writing, and export into three tasks.

Evaluate: the scout keeps the whole identity contract together. It may propose identity and export as separate review units when their boundaries improve review, or recommend one PR with evidence. It does not reproduce the three-task breakdown as three branches or include a known-overlapping option for user approval.

## 8. Shared files and stable dependencies can still form a stack

Fixture: a mixed commit changes two independent functions in one file with separate tests, or adds a lower-layer API and new upper-layer callers without revising that API or its tests again.

Evaluate: the scout can recommend a useful split with explicit symbol ownership and stable dependencies. It does not reject a stack merely because file paths repeat or callers depend on lower-layer code. No temporary implementation, adapter, expectation, or fixture is invented solely to support the partition.
