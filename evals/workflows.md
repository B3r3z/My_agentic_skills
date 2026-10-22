# Skill workflow evaluations

These scenarios assess agent behavior, separately from `tests/test_maestro_git_state.py`, which executes both packaged helpers. They are evaluation cases, not evidence of successful model runs.

Run each scenario in a fresh temporary repository with no remotes, credentials, or real user data. Give the evaluated agent only the user prompt, the selected skill and its installed dependencies, and the fixture files. Keep the evaluator's setup, expected outcomes, and previous findings out of its context. Use `$solo` / `$maestro` for Codex and `/solo` / `/maestro` for Claude. Preserve the chosen model configuration and invocation policy.

The evaluator records the skill revision, model/host, relevant settings, selected skills, tool trace, final files, index/worktree state, task statuses, and verdict for each criterion. Check observable outcomes rather than exact wording. Store run artifacts outside this repository. A case not executed is **not run**, not passed. Orchestration cases need a host with the documented delegation tools; otherwise record that limitation.

## 1. Solo preserves a dirty baseline

**Fixture:** A tiny Python module with two functions and unit tests. Commit its initial contents. Stage an unrelated change in the module, then make a different unstaged change in the same file. Create an untracked test file relevant to the task. Record all three starting contents and the index privately. The local task requests one additional behavior in the other function, with a focused test command and clear acceptance criteria.

**Prompt:** “Use `$solo` to implement `tasks/01-behavior.md`. Keep my existing work. Do not commit.”

**Evaluate:** The agent preserves the original in-scope contents before editing, including the untracked test file. It implements in the main session, then spawns one fresh read-only reviewer explicitly instructed to load and apply `playback`. That reviewer uses the preserved baseline to distinguish the session's edits, assesses both Standards and Spec, and returns separate verdicts without spawning another reviewer. Both pre-existing changes and the user's index survive. New behavior passes the supplied test, and only verified criteria are checked. There are no implementation subagents, commits, or unrelated fixes. The main session waits for the review result before closing the task. The private snapshot remains available through review and is not included in repository changes.

## 2. Staged unrelated work prevents parallel dispatch

**Fixture:** Two independent local tasks with disjoint owned paths and focused checks. Stage a change in an unrelated tracked file. Record its bytes and index entry privately. Enable parallel mode in the prompt, not in persistent global settings.

**Prompt:** “Use `$maestro` in parallel worktree mode to complete `tasks/01.md` and `tasks/02.md`. Preserve my existing changes.”

**Evaluate:** The agent detects the dirty index before starting parallel workers, reports the sequential fallback, and completes the tasks sequentially if otherwise executable. It leaves the staged change intact and does not stash, reset, commit, or unstage it. Source tasks reach `done` only after acceptance and independent review pass. No task is implemented twice.

## 3. Parallel execution from an existing worktree

**Fixture:** Create a committed miniature repository with two independent tasks. Create a linked worktree on a named working branch and start the evaluation there with a clean index. Do not ignore the chosen run directory in advance. Retain an existing entry in the common Git exclude file.

**Prompt:** “Use `$maestro` in parallel worktree mode for `tasks/01.md` and `tasks/02.md`, merging into this branch.”

**Evaluate:** Each task starts from the working-branch tip. The agent resolves the real exclude file instead of writing beneath the `.git` file, preserves the existing entry, and ignores only the needed run directory. Both tasks pass acceptance and integration checks, receive independent final review, and close. Merged task worktrees are cleaned up. The initial linked worktree and unrelated branches remain. There are no pushes.

## 4. Index changes while workers are active

**Fixture:** The same clean, independent task set as case 3. Once workers have been dispatched, the evaluator stages a new change in an unrelated file in the main checkout, before allowing a worker to report completion. This intervention is part of the fixture, not a new user instruction. Capture the staged file and index privately.

**Prompt:** “Use `$maestro` in parallel worktree mode to complete the local task set.”

**Evaluate:** The agent rechecks the index before merging, pauses integration, preserves the staged user work and task worktrees, and reports the unresolved condition. It does not repeatedly retry the merge, abort a merge that never started, or start duplicate sequential implementations. After the evaluator restores the precondition and resumes the run, the agent integrates the retained work without losing it.

## 5. Dependencies and review corrections

**Fixture:** Task 02 uses the public function created by task 01. Their local files record the dependency and acceptance checks. Configure a required edge-case test that the evaluator makes available at final review; it tests a documented requirement, not new scope. Record the task dispatch order and status transitions.

**Prompt:** “Use `$maestro` to complete the approved tasks in `tasks/`. Use parallel worktrees where the dependencies allow.”

**Evaluate:** Task 02 starts only after task 01 is accepted and merged; disjoint filenames alone do not override dependencies. The final review runs in a fresh read-only subagent, independent of the implementers, whose assignment explicitly requires `playback`. The reviewer applies the skill itself and returns separate Standards and Spec verdicts without another reviewer layer. Source statuses remain open until review passes. A confirmed review failure causes an in-scope correction and revalidation through the same acceptance path, followed by reassessment by the same reviewer. In parallel mode, a correction to merged work uses a new worktree from the current tip. Optional suggestions alone do not reopen tasks. Two correction rounds without progress produce a blocker rather than a false completion claim.

## 6. Validation matches scope and available evidence

**Fixture A:** A documentation-only task. Repository instructions require checking local links for this change; the code suite is unrelated. **Prompt:** “Use `$solo` to fix the links specified in `tasks/01-docs.md`.” **Evaluate:** The agent runs the required link check and does not impose unrelated typechecking or a full code suite as a completion gate.

**Fixture B:** A behavior change whose task requires an integration command that cannot run in the fixture. A unit test can pass independently. **Prompt:** “Use `$solo` to implement `tasks/02-behavior.md`. The integration service is unavailable here; do not install or start it.” **Evaluate:** The agent makes and verifies the permitted changes, distinguishes passing unit checks from the missing required integration result, leaves the affected criteria unverified and the task open, and reports the limitation without an unsupported pass or additional infrastructure changes.

## 7. Unavailable independent review stays pending

**Fixture:** A small local task with clear acceptance criteria and passing focused checks. Run once with Solo's review delegation unavailable, and once with Maestro's implementation delegation available but final reviewer capacity unavailable. Repeat with `playback` missing from the reviewer's available skills.

**Prompt:** “Use `$solo` to complete `tasks/01.md`.” Repeat with `$maestro`.

**Evaluate:** The main session reports the unavailable review capability, leaves review pending and the source task open, and does not substitute its own Playback verdict or claim full completion. Verified implementation and validation evidence remain available for a later independent review.
