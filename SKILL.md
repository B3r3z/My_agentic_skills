---
name: sol-luna-dev
description: Execute an approved repository implementation plan through a root-orchestrated, sequential Luna MAX or Sol HIGH workflow with an independent Sol plan-conformance review. Use explicitly for local development, not for coaching or non-development conversations.
---

# Plan-led Sol / Luna Development

The root session is the orchestrator. It owns the plan contract, decomposition,
routing, integration gates, and final response. Implementation belongs to
subagents. Keep one implementation subagent active at a time.

## 1. Materialize the plan

Before dispatching implementation, root turns the supplied or approved plan
into `docs/plan/YYYY-MM-DD-<title>.md`, using the repository's local date and a
short kebab-case title. Create `docs/plan/` when needed. Do not overwrite an
unrelated plan with the same name.

The plan file is the execution contract and must contain:

```markdown
# <Title>

- Date: YYYY-MM-DD
- Status: active
- Source: <where the supplied or approved plan came from>
- Baseline: <git ref and pre-existing working-tree changes>

## Goal
## In scope
## Out of scope
## Acceptance criteria

## Subtasks

### T01 - <bounded outcome>
- Status: pending
- Depends on: none
- Agent: Luna MAX | Sol HIGH
- Owned paths: <paths or modules>
- Covers: <acceptance-criterion IDs>
- Work: <required behavior, not an implementation guess>
- Validate: <commands or observable checks>

## Plan changes
## Final review
```

Split the plan into the smallest independently verifiable subtasks that still
produce coherent changes. Order them by real dependency. Every acceptance
criterion must map to at least one subtask, and every subtask must state its
scope and completion check. Record assumptions; ask the user only when a
missing decision would materially change scope or behavior.

Only root edits the plan contract or task status. A subagent may report that a
change is needed but must not silently widen its task. Root records necessary
minor corrections in `Plan changes` before implementation. Obtain user
direction before changing the goal, agreed scope, or acceptance criteria.

## 2. Route each subtask

Choose one implementer for the current subtask:

- **Luna MAX** for clear, bounded work with explicit acceptance criteria. Use
  `luna_implementer`; its role pins GPT-5.6 Luna at `max` effort.
- **Sol HIGH** for consequential design tradeoffs, complex algorithms or
  concurrency, security-sensitive logic, broad unfamiliar code, or unresolved
  implementation uncertainty. Spawn a write-capable `worker` with model
  `gpt-5.6-sol`, reasoning effort `high`, and a bounded or empty history fork;
  include all required context in its assignment.

If the required model and effort are unavailable, stop and report the missing
capability. Do not silently substitute another configuration.

Give the implementer the plan path, exact task ID and text, repository
instructions, owned paths, relevant context, acceptance criteria, and targeted
validation. State that other work may exist in the tree and must be preserved.
The implementer changes only its assigned code, tests, and implementation-facing
documentation; it does not edit the plan file, commit, push, deploy, or perform
live/external writes without explicit user authorization.

## 3. Execute sequentially

For each subtask in order:

1. Root marks only that task `in_progress` and dispatches one implementer.
2. The implementer returns the files changed, validation results, remaining
   uncertainty, and any requested plan decision.
3. Root inspects the actual diff and reruns or extends proportionate tests.
4. If the task misses its contract, send precise corrections back to the same
   implementer and repeat the gate.
5. Mark the task `complete` only when its mapped acceptance criteria and
   validation pass. Then, and only then, start the next task.

Keep later tasks out of implementation until their dependencies are complete.
Root may make plan/status edits and small mechanical integration fixes; feature
implementation remains delegated while the required agent is available.

## 4. Run the Sol HIGH final review

After all subtasks are complete, spawn a fresh, read-only reviewer with model
`gpt-5.6-sol`, reasoning effort `high`, and a bounded or empty history fork.
Give it the complete plan file, repository instructions, the baseline and final
diff, and all validation evidence. The reviewer inspects the repository itself
and reports two independent axes:

1. **Plan conformance** - map every acceptance criterion and subtask to concrete
   implementation and test evidence; identify omissions, extra scope, changed
   behavior, and undocumented deviations.
2. **Code quality** - check correctness, regressions, maintainability, security,
   edge cases, and whether tests meaningfully cover the changed behavior.

Require file-and-line evidence for findings, severity, and a separate
`PASS`/`FAIL` verdict for each axis. The reviewer does not edit files.

Any `FAIL` reopens the affected subtask. Root sends each finding through the
same sequential implementation and validation gate, then runs a fresh SOL HIGH
review of the corrected final diff. Finish only when both axes pass, or report a
specific blocker and the still-open plan items.

Preserve unrelated working-tree and staging changes throughout the workflow.

