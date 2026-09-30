---
name: to-tickets
description: "Convert a plan or spec into local Markdown tasks with acceptance criteria and dependencies. No external tracker interaction or implementation."
---

# To Tickets

Use only the conversation and local project files. Create or revise local Markdown tasks; do not implement them. Read task paths from `AGENTS.md`, defaulting to `.scratch/<feature-slug>/issues/`.

All ticket interaction stays local. Do not fetch, create, update, comment on, close, sync, or publish tasks in external systems. Remote tracker settings do not override this rule. If the only input is an external reference, ask for pasted content or a local export. Retain a supplied URL as plain text if useful, without opening it.

Reuse the approved plan and existing task IDs. Inspect relevant local code or domain documents where needed to make tasks feasible. Prefer bounded, independently verifiable vertical slices; include prerequisite work and genuine blocking dependencies. Avoid artificial tasks for every layer. For broad mechanical migrations, use a compatible expand–migrate–contract sequence, with a final integration gate if batches cannot pass independently.

Resolve material gaps in behavior, scope, or dependency order with the user. An already approved breakdown needs no repeat approval. For authorized planning, save a useful breakdown and flag remaining assumptions rather than forcing a questionnaire.

Use [local-tasks.md](references/local-tasks.md) when writing files. Preserve existing work, IDs, statuses, and notes. Finish with task paths and the next executable tasks, respecting dependency and integration-group rules. Specification readiness does not imply execution readiness. Stop after planning unless implementation is separately requested.
